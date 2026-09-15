"""Validate the deployed document graph without third-party dependencies."""

import json
import re
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://restb2b.fun/"
NEW_PAGES = {
    "restavratsiya-rakoviny-spb.html",
    "restavratsiya-unitaza-spb.html",
    "remont-skolov-vanny-spb.html",
}
RESOURCE_PAGES = {
    "kak-sfotografirovat-skol-santehniki.html",
    "kontakty-i-usloviya.html",
    "rezultat-i-uhod-posle-restavratsii.html",
}
SUMMARY_FACTS = {
    "llms.txt": (
        "Косметическая реставрация не восстанавливает прочность треснувшего корпуса или герметичность.",
        "Отдельное направление: локальные сколы акриловых и керамических ванн. Полное покрытие, чугунные и стальные ванны в это направление не входят.",
    ),
    "llms-full.txt": (
        "Услуга не восстанавливает прочность треснувшего корпуса.",
        "Косметическое восстановление не применяется, если повреждение может влиять на надежность, монтаж, герметичность или безопасную эксплуатацию.",
        "Ремонт ванн: только локальное устранение сколов на акриловых и керамических ваннах.",
        "Полное обновление покрытия, наливная реставрация всей ванны, чугунные и стальные ванны не входят в заявленное направление.",
    ),
}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.stack = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        node = {"tag": tag, "attrs": dict(attrs), "text": "", "parent": self.stack[-1] if self.stack else None}
        self.nodes.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        for node in self.stack:
            node["text"] += data

    def select(self, tag, **attrs):
        return [n for n in self.nodes if n["tag"] == tag and all(n["attrs"].get(k) == v for k, v in attrs.items())]

    def descendants(self, ancestor, tag):
        found = []
        for node in self.select(tag):
            parent = node["parent"]
            while parent is not None:
                if parent is ancestor:
                    found.append(node)
                    break
                parent = parent["parent"]
        return found

    def faq_pairs(self):
        pairs = []
        for container in self.nodes:
            if not {"faq-list", "service-faq"}.intersection(container["attrs"].get("class", "").split()):
                continue
            for article in self.descendants(container, "article"):
                headings = self.descendants(article, "h3")
                paragraphs = self.descendants(article, "p")
                check(len(headings) == 1 and paragraphs, "FAQ needs one heading and a visible answer")
                pairs.append((normal(headings[0]["text"]), normal(" ".join(p["text"] for p in paragraphs))))
        return pairs


def normal(text):
    return " ".join(text.split())


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def has_type(node, name):
    types = node.get("@type", [])
    return name in (types if isinstance(types, list) else [types])


def is_accessible_image(node):
    parent = node["parent"]
    while parent is not None:
        if parent["attrs"].get("aria-hidden") == "true":
            return False
        parent = parent["parent"]
    return True


def validate_image_alt(node, filename):
    if is_accessible_image(node):
        check(node["attrs"].get("alt", "").strip(), f"missing or empty image alt: {filename}")


def validate_faq(doc, graph, filename):
    visible = doc.faq_pairs()
    marked = [(normal(q["name"]), normal(q["acceptedAnswer"]["text"]))
              for node in graph if has_type(node, "FAQPage") for q in node.get("mainEntity", [])]
    check(len(visible) == len(set(q for q, _ in visible)), f"duplicate visible FAQ: {filename}")
    check(len(marked) == len(visible) and set(marked) == set(visible), f"FAQ answer mismatch: {filename}")


def validate_summary(source, filename):
    # These owner-confirmed boundaries must survive edits to machine-readable summaries.
    required = (
        "Можно обратиться с одним изделием.",
        "Партия из нескольких десятков единиц не является условием обращения.",
        "das05@list.ru",
        "+7 965 767-29-66",
    ) + SUMMARY_FACTS[filename]
    for fact in required:
        check(normal(fact) in normal(source), f"missing or changed service fact in {filename}: {fact}")


def main():
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap = ElementTree.parse(ROOT / "sitemap.xml")
    urls = [n.text for n in sitemap.findall("s:url/s:loc", namespace)]
    check(len(urls) == len(set(urls)), "duplicate sitemap URL")
    files = {url.removeprefix(ORIGIN) or "index.html": url for url in urls}
    for url in urls:
        check(url.startswith(ORIGIN) and not urlsplit(url).query, f"noncanonical sitemap URL: {url}")
    for n in sitemap.findall("s:url/s:lastmod", namespace):
        check(date.fromisoformat(n.text) <= date.today(), f"future lastmod: {n.text}")
    public = {p.name for p in ROOT.glob("*.html") if not p.name.startswith(("google", "yandex_"))}
    check(public == set(files), f"sitemap mismatch: {public ^ set(files)}")
    docs = {f: Document((ROOT / f).read_text()) for f in files}
    titles, descriptions = set(), set()
    inbound = {f: set() for f in files}
    for f, doc in docs.items():
        title = doc.select("title")
        description = doc.select("meta", name="description")
        canonical = doc.select("link", rel="canonical")
        check(len(title) == len(description) == len(canonical) == 1, f"metadata cardinality: {f}")
        t, d = normal(title[0]["text"]), description[0]["attrs"]["content"]
        check(t not in titles and d not in descriptions, f"duplicate title/description: {f}")
        titles.add(t)
        descriptions.add(d)
        check(canonical[0]["attrs"]["href"] == files[f], f"canonical mismatch: {f}")
        check(len(doc.select("h1")) == 1, f"H1 count: {f}")
        robots = doc.select("meta", name="robots")
        check(robots and not re.search(r"noindex|nofollow|nosnippet", robots[0]["attrs"]["content"]), f"blocked indexing: {f}")
        ids = [n["attrs"]["id"] for n in doc.nodes if "id" in n["attrs"]]
        check(len(ids) == len(set(ids)), f"duplicate ID: {f}")
        for node in doc.nodes:
            attrs = node["attrs"]
            for key in ("href", "src", "data-src", "data-gallery"):
                if key not in attrs:
                    continue
                raw = attrs[key]
                url = urlsplit(urljoin(files[f], raw))
                if url.scheme not in ("https", "http") or url.hostname != "restb2b.fun":
                    continue
                target = unquote(url.path).lstrip("/") or "index.html"
                check((ROOT / target).is_file(), f"missing target: {f} -> {raw}")
                if target in docs and node["tag"] == "a":
                    inbound[target].add(f)
                    if url.fragment:
                        check(any(n["attrs"].get("id") == unquote(url.fragment) for n in docs[target].nodes), f"missing anchor: {f} -> {raw}")
            if node["tag"] == "img":
                validate_image_alt(node, f)
        graph = []
        for node in doc.select("script", type="application/ld+json"):
            data = json.loads(node["text"])
            graph.extend(data.get("@graph", [data]))
        check(any(has_type(n, "WebPage") for n in graph), f"missing WebPage: {f}")
        validate_faq(doc, graph, f)
        if f in NEW_PAGES:
            for required in ("Service", "BreadcrumbList", "FAQPage"):
                check(any(n.get("@type") == required for n in graph), f"missing {required}: {f}")
            check(doc.select("p", **{"class": "answer-summary"}), f"missing answer summary: {f}")
            for contact in ("mailto:das05@list.ru", "tel:+79657672966"):
                check(doc.select("a", href=contact), f"missing contact {contact}: {f}")
    for f in NEW_PAGES | RESOURCE_PAGES:
        check("index.html" in inbound[f] and len(inbound[f]) >= 3, f"weak internal discovery: {f}")
        for summary in ("llms.txt", "llms-full.txt"):
            check(files[f] in (ROOT / summary).read_text(), f"missing summary URL: {f} in {summary}")
    robots = (ROOT / "robots.txt").read_text()
    check("Sitemap: " + ORIGIN + "sitemap.xml" in robots, "missing robots sitemap")
    for filename in SUMMARY_FACTS:
        validate_summary((ROOT / filename).read_text(), filename)
    contact_doc = docs["kontakty-i-usloviya.html"]
    check(contact_doc.select("section", id="one-item"), "missing one-item conditions")
    check(contact_doc.select("section", id="scope"), "missing service-scope conditions")
    for f in RESOURCE_PAGES:
        for contact in ("mailto:das05@list.ru", "tel:+79657672966"):
            check(docs[f].select("a", href=contact), f"missing contact {contact}: {f}")
    print(f"PASS: {len(files)} canonical pages; metadata, links, anchors, assets, JSON-LD, visible FAQs and discovery")


if __name__ == "__main__":
    main()
