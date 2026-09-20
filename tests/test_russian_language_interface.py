"""Keep customer-facing text in Russian while retaining technical identifiers."""

import re
import unittest
from html.parser import HTMLParser

from scripts.validate_site import ROOT


class ClientTextParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._ignored_depth = 0
        self.values = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self._ignored_depth += 1
            return
        if self._ignored_depth:
            return

        attributes = dict(attrs)
        for name in ("alt", "aria-label", "title"):
            if attributes.get(name):
                self.values.append(attributes[name])
        if tag == "meta" and (
            attributes.get("name") in {"author", "description"}
            or attributes.get("property") in {"og:site_name", "og:title", "og:description", "twitter:title", "twitter:description"}
        ):
            self.values.append(attributes.get("content", ""))

    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self._ignored_depth:
            self._ignored_depth -= 1

    def handle_data(self, data):
        if not self._ignored_depth and data.strip():
            self.values.append(data)


class RussianLanguageInterfaceTests(unittest.TestCase):
    latin_word = re.compile(r"[A-Za-z]{2,}")

    def client_text(self, path):
        parser = ClientTextParser()
        parser.feed(path.read_text())
        return "\n".join(parser.values).replace("das05@list.ru", "")

    def test_public_client_text_has_no_unnecessary_latin_words(self):
        for path in sorted(ROOT.glob("*.html")):
            if path.name.startswith(("google", "yandex_")):
                continue
            with self.subTest(path=path.name):
                match = self.latin_word.search(self.client_text(path))
                if match:
                    self.fail(f"foreign client text in {path.name}: {match.group(0)}")

    def test_previous_brand_and_b2b_abbreviation_are_absent_from_public_content(self):
        for path in sorted(ROOT.glob("*.html")):
            if path.name.startswith(("google", "yandex_")):
                continue
            with self.subTest(path=path.name):
                source = path.read_text()
                self.assertNotIn("Restoration B2B", source)
                self.assertNotIn("B2B", source)

    def test_navigation_uses_russian_faq_label_without_changing_its_anchor(self):
        for path in sorted(ROOT.glob("*.html")):
            if path.name.startswith(("google", "yandex_")):
                continue
            source = path.read_text()
            with self.subTest(path=path.name):
                self.assertNotIn(">FAQ<", source)
                if "#faq" in source:
                    self.assertIn(">Вопросы и ответы<", source)

    def test_translated_copy_has_no_mechanical_replacement_artifacts(self):
        unwanted = (
            "в Реставрация для бизнеса",
            "для компанийа",
            "для компаний-заказчика",
            "компании-клиентов",
            "процесс для компанийа",
        )
        for path in sorted(ROOT.glob("*.html")):
            if path.name.startswith(("google", "yandex_")):
                continue
            source = path.read_text()
            with self.subTest(path=path.name):
                for phrase in unwanted:
                    self.assertNotIn(phrase, source)

        self.assertIn("Какую керамику мы реставрируем?", (ROOT / "index.html").read_text())
        self.assertIn(
            "Пять этапов работы с рекламационной партией",
            (ROOT / "kak-prohodit-restavratsiya-reklamatsionnoy-partii.html").read_text(),
        )

    def test_llm_summaries_use_the_russian_service_name(self):
        for filename in ("llms.txt", "llms-full.txt"):
            source = (ROOT / filename).read_text()
            with self.subTest(filename=filename):
                self.assertIn("Реставрация для бизнеса", source)
                self.assertNotIn("Restoration B2B", source)
                self.assertNotIn("B2B", source)


if __name__ == "__main__":
    unittest.main()
