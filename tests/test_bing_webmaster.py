"""Regression checks for Bing Webmaster verification and reported SEO signals."""

import json
import unittest
import xml.etree.ElementTree as ET

from scripts.validate_site import ROOT, Document, has_type, is_accessible_image, validate_image_alt


class BingWebmasterVerificationTests(unittest.TestCase):
    EXPECTED_XML = (
        b'<?xml version="1.0"?>\n'
        b"<users>\n"
        b"\t<user>9F43905F2BE154A8D51F956CFDE8BCE2</user>\n"
        b"</users>\n"
    )

    def assert_bing_auth(self, source):
        self.assertEqual(source, self.EXPECTED_XML)
        root = ET.fromstring(source)
        self.assertEqual(root.tag, "users")
        self.assertEqual(root.attrib, {})
        self.assertEqual(len(root), 1)
        user = root[0]
        self.assertEqual(user.tag, "user")
        self.assertEqual(user.attrib, {})
        self.assertEqual(user.text, "9F43905F2BE154A8D51F956CFDE8BCE2")

    def test_bing_site_auth_file(self):
        path = ROOT / "BingSiteAuth.xml"
        self.assertTrue(path.is_file())
        self.assert_bing_auth(path.read_bytes())

    def test_structural_mutations_are_rejected(self):
        mutations = (
            self.EXPECTED_XML.replace(b"<users>", b'<users source="other">'),
            self.EXPECTED_XML.replace(b"<user>", b'<user role="owner">'),
            self.EXPECTED_XML.replace(b"</users>", b"\t<extra />\n</users>"),
            self.EXPECTED_XML.replace(b"9F43905F2BE154A8D51F956CFDE8BCE2", b"CHANGED"),
            self.EXPECTED_XML.replace(b"\n", b"\r\n"),
        )
        for number, mutation in enumerate(mutations, start=1):
            with self.subTest(mutation=number), self.assertRaises(AssertionError):
                self.assert_bing_auth(mutation)


class BingSeoSignalTests(unittest.TestCase):
    HERO_ALT = "Керамический унитаз со сколом до и после локальной реставрации"

    def test_homepage_hero_has_meaningful_alt_text(self):
        source = (ROOT / "index.html").read_text()
        document = Document(source)
        hero = document.select("div", **{"class": "hero-media"})
        self.assertEqual(len(hero), 1)
        self.assertNotEqual(hero[0]["attrs"].get("aria-hidden"), "true")
        images = document.descendants(hero[0], "img")
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0]["attrs"].get("alt"), self.HERO_ALT)
        self.assertTrue(is_accessible_image(images[0]))

    def test_homepage_modified_dates_match_release(self):
        source = (ROOT / "index.html").read_text()
        graph = json.loads(Document(source).select("script", type="application/ld+json")[0]["text"])["@graph"]
        self.assertEqual(next(item for item in graph if has_type(item, "WebSite"))["dateModified"], "2026-09-17")
        self.assertEqual(next(item for item in graph if has_type(item, "WebPage"))["dateModified"], "2026-09-17")
        sitemap = (ROOT / "sitemap.xml").read_text()
        homepage = next(block for block in sitemap.split("<url>")[1:] if "<loc>https://restb2b.fun/</loc>" in block)
        self.assertIn("<lastmod>2026-09-17</lastmod>", homepage)

    def test_decorative_hidden_images_remain_valid(self):
        hidden = Document('<div aria-hidden="true"><img src="decorative.webp"></div>')
        visible = Document('<div><img src="informative.webp" alt="Описание"></div>')
        self.assertFalse(is_accessible_image(hidden.select("img")[0]))
        self.assertTrue(is_accessible_image(visible.select("img")[0]))
        validate_image_alt(hidden.select("img")[0], "fixture.html")
        validate_image_alt(visible.select("img")[0], "fixture.html")
        with self.assertRaises(AssertionError):
            validate_image_alt(Document('<img src="informative.webp" alt="">').select("img")[0], "fixture.html")


if __name__ == "__main__":
    unittest.main()
