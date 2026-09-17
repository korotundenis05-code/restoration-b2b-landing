"""Keep the illustrative economics calculation separate from a service quote."""

import unittest

from scripts.validate_site import ROOT, Document, normal


class PricingClarityTests(unittest.TestCase):
    def test_homepage_does_not_advertise_percentage_tariff(self):
        document = Document((ROOT / "index.html").read_text())
        proof = document.select("aside", **{"class": "hero-proof"})[0]
        self.assertNotIn("10%", proof["text"])
        self.assertIn("По фото", proof["text"])
        economics = document.select("section", id="economics")[0]
        text = normal(economics["text"])
        self.assertIn("Цена рассчитывается индивидуально", text)
        self.assertIn("Единого тарифа в процентах нет", text)

    def test_numeric_example_carries_its_own_qualification(self):
        document = Document((ROOT / "index.html").read_text())
        example = document.select("div", **{"class": "calc-card"})[0]
        text = normal(example["text"])
        for phrase in ("Условный пример экономики, не предложение цены",
                       "Допустим, затраты на восстановление", "100 000 ₽",
                       "10 000 ₽", "Это не тариф и не смета"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_summaries_do_not_present_example_as_price(self):
        for filename in ("llms.txt", "llms-full.txt"):
            with self.subTest(filename=filename):
                text = (ROOT / filename).read_text()
                self.assertIn("Цена рассчитывается индивидуально", text)
                self.assertIn("Единого тарифа в процентах нет", text)
                self.assertIn("условный пример экономики", text)


if __name__ == "__main__":
    unittest.main()
