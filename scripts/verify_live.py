#!/usr/bin/env python3
"""Compare public site payloads with this checkout after deployment."""

import hashlib
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://restb2b.fun/"
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [item.text for item in ET.parse(ROOT / "sitemap.xml").findall("s:url/s:loc", NS)]
paths = [urlsplit(url).path.lstrip("/") or "index.html" for url in urls]
supporting_paths = [
    "assets/css/styles.css",
    "assets/js/main.js",
    "sitemap.xml",
    "robots.txt",
    "llms.txt",
    "llms-full.txt",
    "BingSiteAuth.xml",
]
paths += supporting_paths
failures = []

for path in paths:
    url = BASE if path == "index.html" else BASE + path
    try:
        request = Request(url, headers={"User-Agent": "RestorationB2B-release-check/1.0", "Cache-Control": "no-cache"})
        with urlopen(request, timeout=30) as response:
            body = response.read()
            assert response.status == 200, f"HTTP {response.status}"
            assert response.url == url, f"unexpected redirect: {response.url}"
            restrictions = response.headers.get("X-Robots-Tag", "").lower()
            assert not any(rule in restrictions for rule in ("noindex", "none", "nosnippet")), restrictions
            if path.endswith(".html"):
                assert response.headers.get_content_type() == "text/html", "incorrect HTML MIME type"
        assert body == (ROOT / path).read_bytes(), "published bytes differ from local file"
        print(f"PASS {url} sha256={hashlib.sha256(body).hexdigest()[:16]}", flush=True)
    except Exception as error:
        failures.append(f"{url}: {error}")
        print(f"FAIL {failures[-1]}", flush=True)

robots = RobotFileParser()
robots.parse((ROOT / "robots.txt").read_text().splitlines())
for agent in ("YandexBot", "Googlebot", "Bingbot", "OAI-SearchBot"):
    blocked = [url for url in urls if not robots.can_fetch(agent, url)]
    if blocked:
        failures.append(f"robots.txt blocks {agent}: {blocked}")
    else:
        print(f"PASS robots.txt allows {agent} for all {len(urls)} canonical pages")

if failures:
    raise SystemExit("\n".join(failures))
print(f"PASS production: {len(urls)} pages and {len(supporting_paths)} supporting files match this checkout")
