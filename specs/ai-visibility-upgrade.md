# AI visibility upgrade

Version: 1. Autonomous implementation and public deployment authorized by the owner on 2026-09-10.

## Objective and baseline

Improve useful, crawlable information for the actual restoration services based on the 2026-09-10 AI audit. Baseline commit: a58289d99d1e3553a1beb8e369a368efeeaca245. Static GitHub Pages site, 15 canonical pages. Existing validator passes. The original checkout has only pre-existing untracked exports and .DS_Store files; preserve them until exports are intentionally refreshed.

Audit: Alice mentioned the business in three B2B answers, only two with links; two results were contextual. ChatGPT did not mention it in 38 checked phrases. Perplexity and Claude each had nine completed negative observations, then access/completion limitations. This does not establish a causal technical defect or a ranking guarantee.

## Scope

Improve existing product, glaze, price and B2B pages rather than multiplying synonymous landing pages. Add two distinct useful resources: a photo-assessment guide and a factual contacts/conditions page. Maintain the existing visual language, gallery, effects, navigation and contact channels.

Out of scope: guaranteed rankings/citations, fabricated reviews/prices/credentials/addresses, new accounts, paid services, new restoration materials, complete bath coating, structural crack repair, deleting existing public URLs, changing hosting provider, and redesigning the gallery.

## Requirements

- R1: Expand existing service content for ceramic sink rims, cistern/lid chips, glaze defects and cost factors. Add meaningful heading anchors and links to the exact service/assessment resource. Do not repeat keyword lists or create doorway pages.
- R2: Publish `kak-sfotografirovat-skol-santehniki.html` with a practical photo checklist, an existing real example, material/model information, and explicit limits of remote assessment. Publish `kontakty-i-usloviya.html` with the actual business name, city, email/phone, one-item/batch eligibility, material/scope limits and arrangement of handover. Neither page invents business facts.
- R3: State clearly in visible content and matching machine-readable descriptions that one item may be assessed; a batch of dozens is not required. Baths: local chips on acrylic and ceramic only. No coating of the whole bath, steel/cast iron service or structural repair claims. Review vague claims about restored functional properties and remove unsupported implications.
- R4: New pages have unique metadata, canonical URLs, WebPage/appropriate schema, visible matching FAQs, internal inbound links and sitemap entries. Update dates only for materially changed pages. Keep crawler access open and keep llms summaries consistent without claiming a special ranking effect.
- R5: Preserve all existing URLs, photos, gallery collapse/expand/lightbox, menu, fonts/effects and working email/phone links. Content must fit at desktop and mobile widths with no horizontal overflow.
- R6: Validate before publication; publish the exact reviewed change to the existing GitHub Pages site after verifying the remote baseline. Verify HTTP 200 and byte equality of canonical pages and shared assets on https://restb2b.fun/. Submit changed/new URLs through existing IndexNow only after the key file and published pages are confirmed. A submission receipt is not indexing evidence.
- R7: Synchronize the original Mac project checkout, ZIP and UPLOAD_TO_GITHUB export to the published revision without untracked temporary files. Preserve unrelated data. Record deployment and checks, plus remaining uncertainty.

## Required acceptance checks

- R1-R4: HTML/content assertions, strengthened `scripts/validate_site.py`, focused regression tests, metadata and FAQ equality checks for all canonical pages, sitemap dates and internal discovery.
- R3: Explicit one-item and bath-scope assertions across visible content and structured summaries; no invented tariffs, guarantees, location or minimum quantities.
- R4-R5: HTML validation, JavaScript syntax check and git diff whitespace check.
- R5: Browser verification at 1440 and 390 pixels of the home page, new resources and changed service layouts; menu, gallery and contact actions; images rendered. Browser screenshots inspected. A static server may be used for testing and stopped at completion.
- R6: Actual remote commit, deployment status and live payload verification; no reliance on cache-busting URLs as a substitute for the normal public URLs.
- R7: File manifest and byte comparison of the checkout, ZIP and export, excluding only git metadata and known local export containers.

## Review and completion

Use an independent read-only reviewer when available, as prescribed by SpecLoop. All requirements and checks must pass; publish only the validated source. If an external operation is unavailable, record the affected gate honestly rather than claiming a release. Final evidence must distinguish implementation completion from unproven search/AI visibility gains.

## Sources checked

- https://yandex.ru/support/webmaster/ru/service/alice-answers: visibility is tied to useful, relevant search content; the report does not control inclusion.
- https://developers.google.com/search/docs/appearance/ai-features: standard SEO, index eligibility, crawlable internal links, text content and matching structured data; no special AI schema requirement.
- https://developers.openai.com/api/docs/bots: OAI-SearchBot is the search crawler; crawler access is not proof of citation.
