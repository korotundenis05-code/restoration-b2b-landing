#!/usr/bin/env python3
"""Build one square before/after WebP collage from two supplied photos."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageOps, UnidentifiedImageError


CANVAS_SIZE = 1600
MARGIN = 28
GAP = 24
RADIUS = 42


def cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Resize and center-crop a photo without stretching it."""
    scale = max(size[0] / image.width, size[1] / image.height)
    resized = image.resize(
        (round(image.width * scale), round(image.height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - size[0]) // 2
    top = (resized.height - size[1]) // 2
    return resized.crop((left, top, left + size[0], top + size[1]))


def panel_mask(size: tuple[int, int]) -> Image.Image:
    mask = Image.new("L", size)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *size), radius=RADIUS, fill=255)
    return mask


def heif_converter() -> str | None:
    """Return an explicitly configured or PATH-discoverable HEIF converter."""
    return os.environ.get("HEIF_CONVERT") or shutil.which("heif-convert")


def load_photo(path: Path) -> Image.Image:
    try:
        with Image.open(path) as source:
            return ImageOps.exif_transpose(source).convert("RGB")
    except UnidentifiedImageError:
        if path.suffix.lower() not in {".heic", ".heif"}:
            raise
        converter = heif_converter()
        if not converter:
            raise RuntimeError(
                "HEIC input requires heif-convert. Install libheif or set HEIF_CONVERT "
                "to the converter path."
            ) from None
        with tempfile.TemporaryDirectory(prefix="before-after-heic-") as directory:
            converted = Path(directory) / "converted.jpg"
            subprocess.run([converter, str(path), str(converted)], check=True)
            return load_photo(converted)


def build_collage(before: Path, after: Path, output: Path) -> None:
    panel_width = (CANVAS_SIZE - 2 * MARGIN - GAP) // 2
    panel_size = (panel_width, CANVAS_SIZE - 2 * MARGIN)
    canvas = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    mask = panel_mask(panel_size)

    for x, source in ((MARGIN, before), (MARGIN + panel_width + GAP, after)):
        canvas.paste(cover(load_photo(source), panel_size), (x, MARGIN), mask)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, "WEBP", quality=92, method=6)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", type=Path, required=True)
    parser.add_argument("--after", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    build_collage(args.before, args.after, args.output)
