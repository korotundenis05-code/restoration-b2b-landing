# Search follow-up, 2026-09-23

## Objective

Correct verifiable business-identity markup after publication of the official Yandex Business profile, deploy the change, and report actual search visibility without promising rankings or AI citations.

## Baseline

- Production revision: `6360103f17ca5bc8d8b6e1ab185a291b0b81f2a1`.
- Yandex Business profile `https://yandex.ru/profile/157427855735` is public. The restoration-of-ceramics attribute is approved; the text publication is visible in the owner interface. The owner declined uploading work photos to this profile and confirmed that there is no customer walk-in location.
- Yandex Webmaster lists 11 excluded URLs as low-value or low-demand, with last crawl on 2026-09-14, before the 2026-09-22 content update. Three priority recrawl requests from 2026-09-22 are processed.
- Google Search Console reports that it could not process `sitemap.xml` on 2026-09-22, while the public URL returns HTTP 200 with `application/xml`; a text sitemap fallback is also submitted.
- The home-page `LocalBusiness` markup uses `priceRange` for a quotation process rather than a price range and does not link to the verified public profile.

## Requirements

- R1: Preserve accurate service scope and the owner's privacy choices: no invented address, fixed price, opening hours, review, or photo upload.
- R2: Remove the misleading `priceRange` value, add the official Yandex profile to the business entity's `sameAs`, and offer a visible profile link on the home page.
- R3: Update the home-page modification date and sitemap date truthfully; add regression coverage for R2 and R3.
- R4: Run tests and validator, publish to the authorized GitHub Pages site, and verify that production matches the checkout.
- R5: Report owner-dashboard status and remaining external indexing/ranking limitations accurately. Do not treat search rank or AI citation as a software acceptance gate.

## Checks

- Required: `python3 -m unittest discover -s tests -v`, `python3 scripts/validate_site.py`, GitHub Pages workflow success, `python3 scripts/verify_live.py`.
- Relevant: live HTTP response for sitemap, Yandex Business and Webmaster, Google Search Console, Bing Webmaster, real AI answer sample.

## Out of scope

- Rewriting pages that Yandex has not recrawled since the last update; fake reviews, prices, claims, or backlinks; adding a public physical address or opening hours without owner facts; uploading photos to Yandex Business.

## Definition of done

R1-R5 have direct evidence, production matches the verified code, and any unresolved external indexing or ranking state is explicit.
