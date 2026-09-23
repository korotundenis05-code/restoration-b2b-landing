"""Regression checks for visible FAQ / JSON-LD agreement."""

import json
import unittest

from scripts.validate_site import ROOT, SUMMARY_FACTS, Document, has_type, main, validate_faq, validate_summary


class FaqValidationTests(unittest.TestCase):
    def document(self, answer="One <a href='mailto:example.test'>item</a>."):
        return Document(f'<div class="service-faq"><article><h3>Question?</h3><p>{answer}</p></article></div>')

    def graph(self, answer="One item."):
        return [{"@type": "FAQPage", "mainEntity": [{"name": "Question?", "acceptedAnswer": {"text": answer}}]}]

    def test_inline_links_and_whitespace(self):
        validate_faq(self.document(), self.graph("One   item."), "fixture")

    def test_incorrect_schema_answer_is_rejected(self):
        with self.assertRaisesRegex(AssertionError, "FAQ answer mismatch"):
            validate_faq(self.document(), self.graph("A batch is required."), "fixture")

    def test_missing_or_hidden_schema_question_is_rejected(self):
        with self.assertRaises(AssertionError):
            validate_faq(self.document(), [], "fixture")
        with self.assertRaises(AssertionError):
            validate_faq(Document("<p>Nothing here</p>"), self.graph(), "fixture")

    def test_duplicate_schema_question_is_rejected(self):
        with self.assertRaises(AssertionError):
            validate_faq(self.document(), self.graph() * 2, "fixture")

    def test_missing_visible_answer_is_rejected(self):
        with self.assertRaises(AssertionError):
            Document('<div class="faq-list"><article><h3>Question?</h3></article></div>').faq_pairs()

    def test_schema_types_accept_arrays_without_substring_matches(self):
        self.assertTrue(has_type({"@type": ["WebPage", "ContactPage"]}, "WebPage"))
        self.assertFalse(has_type({"@type": "FAQPage"}, "Page"))

    def test_complete_site(self):
        main()

    def test_scope_and_single_item_conditions(self):
        doc = Document((ROOT / "kontakty-i-usloviya.html").read_text())
        faq = dict(doc.faq_pairs())
        self.assertIn("одно изделие", faq["Нужна ли партия из нескольких десятков изделий?"])
        self.assertIn("Нет.", faq["Восстанавливаете ли вы прочность треснувшего унитаза?"])
        bath = faq["Какие работы с ваннами вы выполняете?"]
        self.assertIn("Только локальное устранение сколов на акриловых и керамических ваннах", bath)
        self.assertIn("чугунные и стальные ванны в это направление не входят", bath)
        for name in ("llms.txt", "llms-full.txt"):
            summary = (ROOT / name).read_text()
            self.assertIn("Можно обратиться с одним изделием.", summary)
            self.assertIn("Партия из нескольких десятков единиц не является условием обращения.", summary)
            validate_summary(summary, name)

    def test_summary_scope_regressions_are_rejected(self):
        for name, boundaries in SUMMARY_FACTS.items():
            source = (ROOT / name).read_text()
            mutations = {
                "Можно обратиться с одним изделием.": "Одно изделие не принимаем.",
                "Партия из нескольких десятков единиц не является условием обращения.": "Минимальная партия составляет несколько десятков единиц.",
                boundaries[0]: "Услуга восстанавливает прочность и герметичность треснувшего корпуса.",
                boundaries[-1]: "Выполняем полное обновление покрытия чугунных и стальных ванн.",
            }
            for fact, contradiction in mutations.items():
                with self.subTest(summary=name, fact=fact):
                    self.assertIn(fact, source)
                    with self.assertRaisesRegex(AssertionError, "service fact"):
                        validate_summary(source.replace(fact, contradiction), name)

    def test_targeted_service_sections(self):
        sections = {
            "restavratsiya-rakoviny-spb.html": ["rim-chips"],
            "restavratsiya-unitaza-spb.html": ["cistern-chips", "lid-chips"],
            "remont-skolov-vanny-spb.html": ["local-repair"],
            "vosstanovlenie-glazuri-santehniki.html": ["sink-glaze", "toilet-glaze"],
            "stoimost-restavratsii-santehniki.html": ["cost-by-damage"],
        }
        for name, anchors in sections.items():
            doc = Document((ROOT / name).read_text())
            for anchor in anchors:
                with self.subTest(page=name, anchor=anchor):
                    self.assertEqual(len(doc.select("section", id=anchor)), 1)

    def test_public_business_profile_identity(self):
        profile = "https://yandex.ru/profile/157427855735"
        doc = Document((ROOT / "index.html").read_text())
        graph = json.loads(doc.select("script", type="application/ld+json")[0]["text"])["@graph"]
        business = next(node for node in graph if node.get("@id") == "https://restb2b.fun/#business")
        self.assertEqual(business["sameAs"], [profile])
        self.assertNotIn("priceRange", business)
        self.assertEqual(len(doc.select("a", href=profile)), 1)


if __name__ == "__main__":
    unittest.main()
