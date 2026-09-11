"""Customer-answer and enquiry regression checks."""

import unittest
from urllib.parse import parse_qs, urlsplit

from scripts.validate_site import ROOT, Document


class RepairConfidenceTests(unittest.TestCase):
    def test_resource_answers_are_visible_without_javascript(self):
        doc = Document((ROOT / "rezultat-i-uhod-posle-restavratsii.html").read_text())
        for anchor in ("appearance", "acceptance", "care", "replacement", "faq"):
            self.assertEqual(len(doc.select("section", id=anchor)), 1)
        answers = dict(doc.faq_pairs())
        self.assertEqual(len(answers), 5)
        self.assertTrue(answers["Можно ли гарантировать незаметный ремонт по фотографии?"].startswith("Нет."))
        self.assertIn("Универсальный срок для всех сколов на сайте не установлен", answers["Через сколько можно пользоваться раковиной или ванной после реставрации?"])
        self.assertIn("не восстанавливает прочность треснувшего корпуса или герметичность", answers["Можно ли пользоваться треснувшим унитазом после косметического ремонта?"])
        self.assertEqual(len(doc.select("img", src="assets/images/case-panel.webp")), 1)

    def test_email_is_only_a_draft_with_plain_contact_fallbacks(self):
        doc = Document((ROOT / "kontakty-i-usloviya.html").read_text())
        links = [n for n in doc.select("a") if "data-enquiry-draft" in n["attrs"]]
        self.assertEqual(len(links), 1)
        target = urlsplit(links[0]["attrs"]["href"])
        self.assertEqual((target.scheme, target.path), ("mailto", "das05@list.ru"))
        fields = parse_qs(target.query)
        self.assertEqual(set(fields), {"subject", "body"})
        self.assertEqual(fields["subject"], ["Оценка скола сантехники"])
        for phrase in ("Изделие и модель:", "Материал (если известен):", "Количество изделий:", "Признаки трещины или течи", "Фотографии добавлю к письму отдельно."):
            self.assertIn(phrase, fields["body"][0])
        self.assertFalse(doc.select("form"))
        self.assertTrue(doc.select("a", href="mailto:das05@list.ru"))
        self.assertTrue(doc.select("a", href="tel:+79657672966"))

    def test_primary_topic_still_qualifies_the_actual_service(self):
        doc = Document((ROOT / "restavratsiya-santehnicheskoy-keramiki.html").read_text())
        self.assertIn("Реставрация керамики:", doc.select("h1")[0]["text"])
        self.assertIn("сантехника", doc.select("h1")[0]["text"])
        self.assertIn("Санкт-Петербурге", doc.select("p", **{"class": "answer-summary"})[0]["text"])
        self.assertTrue(any("Реставрация посуды, статуэток, антиквариата" in p["text"] for p in doc.select("p")))

    def test_each_relevant_product_links_to_result_resource(self):
        for name in ("index.html", "restavratsiya-santehnicheskoy-keramiki.html", "restavratsiya-rakoviny-spb.html", "restavratsiya-unitaza-spb.html", "remont-skolov-vanny-spb.html", "vosstanovlenie-glazuri-santehniki.html", "kontakty-i-usloviya.html"):
            doc = Document((ROOT / name).read_text())
            with self.subTest(page=name):
                self.assertTrue(any(urlsplit(n["attrs"].get("href", "")).path == "rezultat-i-uhod-posle-restavratsii.html" for n in doc.select("a")))


if __name__ == "__main__":
    unittest.main()
