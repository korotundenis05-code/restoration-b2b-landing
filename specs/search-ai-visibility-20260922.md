# Search and AI visibility, 2026-09-22

## Objective

Improve discovery and factual usefulness of restb2b.fun, publish the reviewed change, and measure the actual state in owner dashboards. Search positions and AI citations are external outcomes, not a software acceptance gate.

## Baseline

- Yandex Webmaster: 7 pages in search, 11 excluded as low-value or low-demand; tracked query `реставрация керамики спб` has 2 impressions and 0 clicks. Alice AI report says insufficient data.
- Google Search Console: 1 indexed page, 0 excluded; no sitemap had been submitted in this property. Submitted `sitemap.xml` on 2026-09-22, initial receipt confirmed; processing pending.
- Bing Webmaster: sitemap succeeds with 18 discovered URLs; Site Explorer shows 2 indexed URLs, 0 search impressions, and AI Performance 0 citations. URL Inspection independently reports the main ceramics service page indexed.
- Public crawler access and 18 canonical HTML pages already exist. Existing sitemap and JSON-LD modification dates predate real content edits from 2026-09-20.

## Requirements

- R1: Keep all public pages, canonical URLs, verification files, and service boundaries intact. Do not invent outcomes, credentials, address, reviews, or prices.
- R2: Align sitemap `lastmod` and structured-data `dateModified` with genuine page edits; update tests to prevent inconsistency.
- R3: Make the main ceramics service and the toilet-chip answer more useful with original before/after evidence and precise, visually supported context. Expose gallery image URLs directly in HTML while keeping native lazy loading and the existing expand/collapse behavior.
- R4: Fix verifiable wording or metadata defects, then run unit tests and the site validator before deployment.
- R5: Publish to the authorized GitHub Pages production site, verify the live payload, and request recrawl for materially changed URLs.
- R6: Report dashboard observations and remaining external constraints without claiming top-three ranks or universal AI recommendations.

## Checks

- Required: `python3 -m unittest discover -s tests -v`, `python3 scripts/validate_site.py`, GitHub Actions success, `python3 scripts/verify_live.py`.
- Relevant: responsive browser inspection, live HTTP headers, Yandex/Google/Bing owner dashboards, IndexNow receipt.

## Definition of done

R1-R6 have direct evidence; code and production match. Ranking and citations remain monitored outcomes rather than promises.
