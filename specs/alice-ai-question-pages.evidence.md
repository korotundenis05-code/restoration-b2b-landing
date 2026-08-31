# Alice AI Question Pages Evidence

## Build evidence

- Six unique canonical answer pages were added for the approved customer questions.
- Every answer page contains a direct-answer block, substantive guidance, assessment inputs, limitations, visible FAQ, contacts, and related links.
- Every answer page contains `WebPage`, `Article`, `BreadcrumbList`, and `FAQPage` JSON-LD aligned with the visible FAQ.
- The homepage contains a visible six-link answer section and an `ItemList` describing the same pages.
- Contextual links were added to the four matching service pages.
- `sitemap.xml`, `llms.txt`, `llms-full.txt`, and `README.md` were updated.

## Local validation

- `git diff --check`: pass.
- `npx --yes html-validate` on all 12 public HTML pages: pass.
- Custom metadata, canonical, H1, JSON-LD, local-link, word-count, homepage-discovery, and sitemap-discovery validator: pass for 12 pages.
- All six new pages contain at least 330 words of unique visible content.
- `xmllint --noout sitemap.xml`: pass.
- `node --check assets/js/main.js`: pass.
- Playwright at 390 px: all 12 pages have an H1 and visible FAQ, no horizontal overflow, and the mobile menu opens; all six answer pages expose the direct-answer block.
- Desktop Playwright check at 1440 px: the homepage answer section exposes six links and has no horizontal overflow.
- Local Lighthouse: Accessibility 100, Best Practices 100, SEO 100, Performance 74. The local performance score is treated as diagnostic because the server and font requests run locally; production is checked after publication.

## Visual evidence

- Mobile answer-page screenshot: `/tmp/restb2b-alice-mobile.png`.
- Desktop homepage answer-section screenshot: `/tmp/restb2b-alice-answers-desktop.png`.

## Production evidence

Pending publication and live checks.
