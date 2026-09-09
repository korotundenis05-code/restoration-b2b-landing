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
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.stack = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        node = {"tag": tag, "attrs": dict(attrs), "text": ""}
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


def normal(text):
    return " ".join(text.split())


def check(condition, message):
    if not condition:
        raise AssertionError(message)


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
                check("alt" in attrs, f"missing image alt: {f}")
        graph = []
        for node in doc.select("script", type="application/ld+json"):
            data = json.loads(node["text"])
            graph.extend(data.get("@graph", [data]))
        check(any(n.get("@type") == "WebPage" for n in graph), f"missing WebPage: {f}")
        questions = [q for n in graph if n.get("@type") == "FAQPage" for q in n["mainEntity"]]
        headings = {normal(n["text"]) for n in doc.select("h3")}
        check(all(normal(q["name"]) in headings for q in questions), f"hidden FAQ question: {f}")
        if f in NEW_PAGES:
            for required in ("Service", "BreadcrumbList", "FAQPage"):
                check(any(n.get("@type") == required for n in graph), f"missing {required}: {f}")
            paragraphs = {normal(n["text"]) for n in doc.select("p")}
            check(all(normal(q["acceptedAnswer"]["text"]) in paragraphs for q in questions), f"FAQ answer mismatch: {f}")
            check(doc.select("p", **{"class": "answer-summary"}), f"missing answer summary: {f}")
            for contact in ("mailto:das05@list.ru", "tel:+79657672966"):
                check(doc.select("a", href=contact), f"missing contact {contact}: {f}")
    for f in NEW_PAGES:
        check("index.html" in inbound[f] and len(inbound[f]) >= 3, f"weak internal discovery: {f}")
        for summary in ("llms.txt", "llms-full.txt"):
            check(files[f] in (ROOT / summary).read_text(), f"missing summary URL: {f} in {summary}")
    robots = (ROOT / "robots.txt").read_text()
    check("Sitemap: " + ORIGIN + "sitemap.xml" in robots, "missing robots sitemap")
    print(f"PASS: {len(files)} canonical pages; metadata, links, anchors, assets, JSON-LD, visible FAQs and discovery")


if __name__ == "__main__":
    main()
