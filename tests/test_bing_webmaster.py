"""Regression checks for Bing Webmaster ownership verification."""

import unittest
import xml.etree.ElementTree as ET

from scripts.validate_site import ROOT


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


if __name__ == "__main__":
    unittest.main()
