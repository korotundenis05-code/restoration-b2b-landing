"""Focused checks for the page Yandex classified as low value."""

import json
import unittest

from scripts.validate_site import ROOT, Document, has_type, validate_faq


class YandexIndexationRepairTests(unittest.TestCase):
    META_DESCRIPTION = (
        "Ремонт сколов сантехники в Санкт-Петербурге: раковины, унитазы, "
        "бачки и локальные сколы акриловых и керамических ванн. Фото до "
        "и после, единичные изделия и партии."
    )
    SERVICE_DESCRIPTION = (
        "Оценка и косметическое восстановление сколов на сантехнической "
        "керамике, а также локальных сколов акриловых и керамических ванн. "
        "Без структурного ремонта и полного обновления покрытия."
    )
    VISIBLE_SCOPE_FACTS = (
        "Мы не восстанавливаем прочность треснувшего корпуса, не устраняем "
        "протечки, не ремонтируем арматуру и крепления.",
        "Полное обновление покрытия, а также работы с чугунными и стальными "
        "ваннами в услугу не входят.",
    )

    def setUp(self):
        self.path = ROOT / "vosstanovlenie-skolov-santehniki.html"
        self.source = self.path.read_text()
        self.document = Document(self.source)

    def graph(self):
        scripts = self.document.select("script", type="application/ld+json")
        self.assertEqual(len(scripts), 1)
        return json.loads(scripts[0]["text"])["@graph"]

    def test_direct_answer_and_distinct_decision_content(self):
        summaries = self.document.select("p", **{"class": "answer-summary"})
        self.assertEqual(len(summaries), 1)
        for phrase in (
            "Когда косметический ремонт скола возможен",
            "Когда восстановление скола не подходит",
            "Как оцениваем одно изделие и партию",
            "Какие фотографии нужны для оценки",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.source)

    def assert_service_scope(self, source):
        document = Document(source)
        metadata = document.select("meta", name="description")
        self.assertEqual(len(metadata), 1)
        self.assertEqual(metadata[0]["attrs"]["content"], self.META_DESCRIPTION)

        scripts = document.select("script", type="application/ld+json")
        self.assertEqual(len(scripts), 1)
        graph = json.loads(scripts[0]["text"])["@graph"]
        service = next(item for item in graph if has_type(item, "Service"))
        self.assertEqual(service["description"], self.SERVICE_DESCRIPTION)

        for fact in self.VISIBLE_SCOPE_FACTS:
            self.assertIn(fact, source)

        for contradiction in (
            "Мы восстанавливаем прочность треснувшего корпуса",
            "выполняем полное обновление покрытия",
            "чугунными и стальными ваннами в услугу входят",
            "гарантированный выезд на дом",
        ):
            self.assertNotIn(contradiction, source)

    def test_service_scope_is_consistent_and_factually_bounded(self):
        self.assert_service_scope(self.source)

    def test_scope_contradictions_are_rejected(self):
        mutations = (
            self.source.replace(
                self.META_DESCRIPTION,
                self.META_DESCRIPTION + " Также работаем с чугунными и стальными ваннами.",
            ),
            self.source.replace(
                self.SERVICE_DESCRIPTION,
                self.SERVICE_DESCRIPTION + " Выполняем полное обновление покрытия.",
            ),
            self.source.replace(
                "чугунными и стальными ваннами в услугу не входят",
                "чугунными и стальными ваннами в услугу входят",
            ),
            self.source.replace(
                self.VISIBLE_SCOPE_FACTS[0],
                self.VISIBLE_SCOPE_FACTS[0] + " Предусмотрен гарантированный выезд на дом.",
            ),
        )
        for number, mutated_source in enumerate(mutations, start=1):
            with self.subTest(mutation=number), self.assertRaises(AssertionError):
                self.assert_service_scope(mutated_source)

    def test_first_party_before_after_image(self):
        images = self.document.select("img", src="assets/images/case-transport-chip.webp")
        self.assertEqual(len(images), 1)
        attrs = images[0]["attrs"]
        self.assertEqual(attrs.get("width"), "821")
        self.assertEqual(attrs.get("height"), "1100")
        self.assertEqual(attrs.get("loading"), "lazy")
        self.assertIn("до и после", attrs.get("alt", ""))

    def test_five_visible_faq_answers_match_schema(self):
        pairs = self.document.faq_pairs()
        self.assertEqual(len(pairs), 5)
        graph = self.graph()
        validate_faq(self.document, graph, self.path.name)
        faq = next(item for item in graph if has_type(item, "FAQPage"))
        self.assertEqual(len(faq["mainEntity"]), 5)

    def test_modified_dates_match_release(self):
        webpage = next(item for item in self.graph() if has_type(item, "WebPage"))
        self.assertEqual(webpage["dateModified"], "2026-09-14")
        sitemap = (ROOT / "sitemap.xml").read_text()
        block = sitemap.split("https://restb2b.fun/vosstanovlenie-skolov-santehniki.html", 1)[1]
        self.assertIn("<lastmod>2026-09-14</lastmod>", block.split("</url>", 1)[0])


if __name__ == "__main__":
    unittest.main()
