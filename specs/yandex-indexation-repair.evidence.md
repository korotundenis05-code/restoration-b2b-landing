# Yandex indexation repair evidence

Date: 2026-09-14. Production commit: `1afd283e817ab6ce04ea7f2224baf7212a4adfad`.

## Requirement evidence

- R1-R2: `vosstanovlenie-skolov-santehniki.html` now provides a direct
  answer, assessment criteria, supported products, exclusions, single-item
  and batch workflow, photo requirements, cost factors and next steps.
- R2 factual boundary: metadata, visible copy and Service JSON-LD consistently
  limit bath work to local chips on acrylic and ceramic baths. Structural
  repair, leaks, fittings, full coatings, cast iron and steel baths remain
  excluded. Exact-value and mutation tests reject contradictory claims.
- R3: existing first-party `case-transport-chip.webp` is used at its verified
  821 by 1100 dimensions with lazy loading and descriptive before/after alt.
- R4: five visible FAQ answers exactly match the five FAQPage JSON-LD answers.
- R5: page `dateModified` and its sole Sitemap `lastmod` are `2026-09-14`.
- R6: contacts, service boundaries, existing navigation and styles are
  preserved. No new capability, price, guarantee, address or visit model was
  introduced.

## Validation evidence

- `python3 -m unittest discover -s tests -v`: PASS, 20 tests.
- `python3 scripts/validate_site.py`: PASS, 18 canonical pages.
- `html-validate` on all 18 canonical HTML pages: PASS.
- `git diff --check`: PASS.
- Browser QA at 1440 px and 390 px: PASS for all 18 pages, 36 cases; no
  overflow, broken images, menu failure or console error.
- GitHub Pages workflow `34851205437`: PASS; deploy job completed in 15 s.
- `python3 scripts/verify_live.py`: PASS; 18 production pages and six
  supporting files match the reviewed checkout byte-for-byte. Crawler access
  passes for YandexBot, Googlebot, Bingbot and OAI-SearchBot.
- Production browser QA at 1440 px and 390 px: PASS for all 36 cases.
- Yandex IndexNow submission for the changed canonical URL: HTTP 202 with
  `{"success":true}` after the page and hosted key were verified live.

## Webmaster evidence

- Yandex Webmaster identified this page as the only explicit
  `Малоценная или маловостребованная страница` exclusion.
- The outdated six-URL Sitemap snapshot was resent on 2026-09-14, and all 18
  canonical URLs were added to the reindex queue.
- Region change to Saint Petersburg is pending Yandex review for up to seven
  days.
- The measured query `реставрация керамики спб` had one impression, zero
  clicks and average position 12 before this release.
- Alice AI currently reports insufficient data. Yandex Webmaster also reports
  no detected external links.

## External uncertainty

The evidence proves technical readiness, publication and crawler
notification. It does not prove that Yandex has already reprocessed the page,
changed its rank or selected it for Alice AI answers. Those outcomes depend on
crawl/indexing latency, relevance, competition and external authority.
