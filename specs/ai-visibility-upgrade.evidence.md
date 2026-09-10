# AI visibility upgrade evidence

Date: 2026-09-10. Spec version 1. Baseline a58289d99d1e3553a1beb8e369a368efeeaca245.

## Pre-release verification

- R1: Existing sink, toilet/cistern/lid, bath, glaze, cost and B2B pages expanded. Targeted section anchors covered by regression tests. Existing public URLs retained; two new resources serve different practical needs rather than duplicate service landing pages.
- R2: Photo guide and contacts/conditions page have real existing images, visible answers, unique canonical metadata, entity references and internal links. No invented address, business hours, tariffs, reviews or credentials.
- R3: One-item eligibility and cosmetic-only scope appear in homepage FAQ, conditions, service content and llms summaries. Baths remain local chips on acrylic/ceramic only. Unsupported homepage functional-properties wording removed. Scope assertions and visible/schema equality tests pass.
- R4: All 17 canonical pages have matching visible and machine-readable FAQ answers, unique metadata, valid links/anchors and sitemap entries. Dates changed only for modified pages. Original robots, CNAME and provider verification files retained.
- R5: Chrome browser checks completed on all 17 pages at 1440x960 and 390x960. No document or checked text/control horizontal overflow; contact hrefs and all service images checked. Mobile menus open and close with Escape. Home gallery shows 8 desktop / 4 mobile items, expands, opens an image, closes with Escape and collapses. No page JavaScript errors. Screenshots of home, FAQ, new resources and toilet page inspected. Existing stylesheet, gallery photographs and main JavaScript unchanged.

## Commands

- `python3 -m unittest discover -s tests -v`: exit 0, 10 tests, including contradictory-summary mutation fixtures for minimum quantity, single-item eligibility, bath materials/coating and structural repair.
- `python3 scripts/validate_site.py`: included in regression suite; PASS 17 pages.
- html-validate 11.11.0 using existing `.htmlvalidate.json`: exit 0 for all 17 canonical HTML pages. Google/Yandex ownership files are excluded because they are provider-issued verification responses, retained verbatim. The Yandex response lacks title/lang by provider format.
- `node --check assets/js/main.js`: exit 0.
- `git diff --check`: exit 0.
- Chrome Playwright script stored outside publication at `/Users/macbook/Documents/New project/restb2b-browser-check.cjs`: exit 0, 34 page/viewport cases. Screenshots at `/Users/macbook/Documents/New project/restb2b-release-qa/`.

## Release gates

Independent read-only review identified F1: summary-scope tests used overly weak substring checks. Repaired with explicit factual boundaries checked by the main validator and negative fixtures for both summary files. No visible content or CSS changed during this repair.

- R6: Pending publication and public byte equality. GitHub API confirms both legacy Pages and repository workflow previously deployed the same push. The release will use GitHub Actions as the single source so validation failures prevent publication. Domain and repository remain unchanged.
- R7: Pending original checkout, ZIP and upload export synchronization after release.

## Limits

These checks prove content and technical readiness, not indexing, top-three search positions or future AI citations. The earlier audit was a limited set of observations, partly contextual, with login/region limitations on several platforms. No new cross-platform ranking claim is made. IndexNow acceptance, when obtained, is only a notification receipt.
