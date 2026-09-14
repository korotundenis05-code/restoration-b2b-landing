# Yandex indexation repair

Version: 1.0. Date: 2026-09-14. Mode: autonomous.
Baseline: ea3a1ae5df61d38c1d1784cdd6e708c0b68dad37.

## Objective and current state

Improve the only URL that Yandex Webmaster currently classifies as a
"low-value or low-demand page": `vosstanovlenie-skolov-santehniki.html`.
Yandex currently has seven canonical pages in search, sees an outdated
six-URL Sitemap snapshot, and reports one impression for the query
"реставрация керамики спб" at average position 12.

## Scope and requirements

- R1: Make the affected page a distinct practical answer for local cosmetic
  chip repair, rather than a shorter duplicate of the general ceramics page.
- R2: State concrete assessment criteria, supported products, exclusions and
  the photo-assessment workflow without inventing guarantees or capabilities.
- R3: Add one existing first-party before/after image with descriptive alt text.
- R4: Expand the visible FAQ to five useful questions and keep FAQ JSON-LD
  exactly synchronized with the visible answers.
- R5: Update `dateModified` and the Sitemap `lastmod` only for the changed page.
- R6: Preserve confirmed business scope, contacts, navigation, design and all
  unrelated pages. Publish through the existing GitHub Pages workflow and
  verify the live result.

## Constraints and exclusions

The service covers cosmetic defects on sanitary ceramics and local chips on
acrylic or ceramic baths. It does not restore structural strength, leaks,
fittings, full bath coatings, cast iron or steel baths. No fixed price,
warranty duration, universal turnaround, home visit or nationwide coverage is
introduced. No new CSS or image files are required.

## Acceptance and checks

- A1 (R1-R2): The page has a direct answer summary and distinct sections for
  assessment, supported cases, exclusions, batch handling and next steps.
- A2 (R3): `case-transport-chip.webp` is visible in the page and has accurate
  dimensions, lazy loading and descriptive alt text.
- A3 (R4): Five visible FAQ pairs exactly match the page FAQ JSON-LD.
- A4 (R5): WebPage `dateModified` and Sitemap `lastmod` are `2026-09-14`.
- A5 (R6): Site validator, unit tests and HTML validation pass; browser checks
  show no overflow or broken assets on desktop and mobile.
- A6 (R6): GitHub Pages deploy succeeds and production bytes/checks pass.

## Required check plan

- `python3 -m unittest discover -s tests -v`
- `python3 scripts/validate_site.py`
- HTML validation for all canonical HTML pages
- Local browser checks for the changed page at desktop and mobile widths
- Successful GitHub Pages workflow and `python3 scripts/verify_live.py`

## Definition of done

All requirements and acceptance criteria pass, review score is at least 9.5,
the production page matches the reviewed source, and remaining ranking/indexing
latency is reported as external uncertainty rather than implementation success.
