"""Regression checks for the source folders 36-42 before/after gallery cases."""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.validate_site import Document, ROOT


class CaseGalleryTests(unittest.TestCase):
    CASE_NUMBERS = range(36, 43)
    ASSET_VERSION = "20260920"

    @staticmethod
    def sha256(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    @staticmethod
    def webp_dimensions(path):
        """Read dimensions from the WebP RIFF header using only the standard library."""
        data = path.read_bytes()
        if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
            raise AssertionError(f"not a WebP RIFF file: {path}")
        offset = 12
        while offset + 8 <= len(data):
            chunk, length = data[offset:offset + 4], int.from_bytes(data[offset + 4:offset + 8], "little")
            payload = offset + 8
            if chunk == b"VP8 ":
                if data[payload + 3:payload + 6] != b"\x9d\x01\x2a":
                    raise AssertionError(f"invalid VP8 frame: {path}")
                width = int.from_bytes(data[payload + 6:payload + 8], "little") & 0x3FFF
                height = int.from_bytes(data[payload + 8:payload + 10], "little") & 0x3FFF
                return width, height
            if chunk == b"VP8X":
                width = int.from_bytes(data[payload + 4:payload + 7], "little") + 1
                height = int.from_bytes(data[payload + 7:payload + 10], "little") + 1
                return width, height
            offset = payload + length + (length % 2)
        raise AssertionError(f"no supported WebP image header: {path}")

    def test_new_collages_are_published_as_deferred_gallery_cards(self):
        source = (ROOT / "index.html").read_text()
        document = Document(source)
        gallery_cards = {
            node["attrs"].get("data-gallery"): node
            for node in document.select("button")
            if node["attrs"].get("data-gallery")
        }
        structured_images = {}
        for node in document.select("script", type="application/ld+json"):
            graph = json.loads(node["text"]).get("@graph", [])
            for item in graph:
                if item.get("@type") != "ImageGallery":
                    continue
                structured_images.update({
                    image.get("contentUrl"): image.get("caption")
                    for image in item.get("associatedMedia", [])
                })

        for number in self.CASE_NUMBERS:
            with self.subTest(number=number):
                path = f"assets/images/gallery/work-{number:02d}.webp?v={self.ASSET_VERSION}"
                self.assertIn(path, gallery_cards)
                card_images = document.descendants(gallery_cards[path], "img")
                self.assertEqual(len(card_images), 1)
                image = card_images[0]["attrs"]
                self.assertEqual(
                    image.get("src"),
                    "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==",
                )
                self.assertEqual(image.get("data-src"), path)
                self.assertTrue(image.get("alt", "").strip())
                asset = ROOT / f"assets/images/gallery/work-{number:02d}.webp"
                self.assertTrue(asset.is_file())
                self.assertGreater(asset.stat().st_size, 10_000)
                self.assertEqual(self.webp_dimensions(asset), (1600, 1600))
                canonical_url = f"https://restb2b.fun/assets/images/gallery/work-{number:02d}.webp"
                self.assertEqual(
                    structured_images.get(canonical_url),
                    image["alt"],
                )

        self.assertIn("data-gallery-toggle", source)

    def test_case_manifest_records_source_pairs_and_hashes(self):
        manifest = json.loads((ROOT / "scripts/case-gallery-36-42-manifest.json").read_text())
        self.assertEqual(manifest["source_root_environment"], "CASE_GALLERY_SOURCE_ROOT")
        self.assertEqual([case["work"] for case in manifest["cases"]], list(self.CASE_NUMBERS))
        for case in manifest["cases"]:
            with self.subTest(work=case["work"]):
                self.assertTrue(case["before"].startswith(f'{case["work"]}/'))
                self.assertTrue(case["after"].startswith(f'{case["work"]}/'))
                self.assertRegex(case["before_sha256"], r"^[0-9a-f]{64}$")
                self.assertRegex(case["after_sha256"], r"^[0-9a-f]{64}$")
                self.assertEqual(case["output"], f'assets/images/gallery/work-{case["work"]:02d}.webp')
                self.assertRegex(case["output_sha256"], r"^[0-9a-f]{64}$")
                self.assertEqual(self.sha256(ROOT / case["output"]), case["output_sha256"])

    def test_source_hashes_match_manifest_when_source_root_is_available(self):
        source_root = os.environ.get("CASE_GALLERY_SOURCE_ROOT")
        if not source_root:
            self.skipTest("set CASE_GALLERY_SOURCE_ROOT to verify private source photos")
        manifest = json.loads((ROOT / "scripts/case-gallery-36-42-manifest.json").read_text())
        for case in manifest["cases"]:
            with self.subTest(work=case["work"]):
                self.assertEqual(
                    self.sha256(Path(source_root) / case["before"]),
                    case["before_sha256"],
                )
                self.assertEqual(
                    self.sha256(Path(source_root) / case["after"]),
                    case["after_sha256"],
                )

    @unittest.skipUnless(importlib.util.find_spec("PIL"), "Pillow is only needed by the local asset builder")
    def test_collage_builder_converts_heic_with_configured_converter(self):
        spec = importlib.util.spec_from_file_location(
            "before_after_builder", ROOT / "scripts/build_before_after_collage.py"
        )
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            before = root / "before.heic"
            after = root / "after.jpg"
            output = root / "collage.webp"
            before.write_bytes(b"not a HEIC image")
            builder.Image.new("RGB", (40, 30), "#d9d9d9").save(after)

            def convert(args, **kwargs):
                self.assertEqual(args[:2], ["/tools/heif-convert", str(before)])
                builder.Image.new("RGB", (40, 30), "#f7f7f7").save(args[2])

            with patch.dict(os.environ, {"HEIF_CONVERT": "/tools/heif-convert"}):
                with patch.object(builder.subprocess, "run", side_effect=convert) as run:
                    builder.build_collage(before, after, output)

            run.assert_called_once()
            self.assertEqual(self.webp_dimensions(output), (1600, 1600))


if __name__ == "__main__":
    unittest.main()
