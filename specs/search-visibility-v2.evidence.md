# Search Visibility V2 Evidence

## Build evidence

- Homepage title and H1 identify sanitary-ceramics restoration and Saint Petersburg.
- Visible homepage copy retains the B2B reclamation and warehouse-goods outcome.
- `stoimost-restavratsii-santehniki.html` contains cost factors, the assessment process, exclusions, FAQ, contacts, and a non-offer qualification for the 10% reference.
- The five service pages contain WebPage, Service, BreadcrumbList, and FAQPage JSON-LD aligned with visible copy.
- Homepage gallery has descriptive alt text and ImageObject captions for the initially visible examples.
- `robots.txt` allows standard search crawlers and named answer-engine crawlers while retaining `User-agent: *` access.
- `llms.txt` is Russian-first and links to `llms-full.txt` for a detailed factual summary.
- `sitemap.xml` lists all six canonical HTML pages with `2026-08-21` modification dates.
- Google Fonts are discovered in document head with preconnect and only the four weights used by the design.
- Mobile navigation is available on every service page.

## Static verification

- `html-validate`: pass on all six HTML pages.
- JSON-LD parse, canonical metadata, H1, and local HTML link check: pass on all six HTML pages.
- `node --check assets/js/main.js`: pass.
- `xmllint --noout sitemap.xml`: pass.
- `git diff --check`: pass.
- Local HTTP: 200 for all public pages and discovery files.
- Mobile viewport: document width equals viewport width; no overflowing elements detected; menu opens successfully.

## Pre-release production baseline

- URL: `https://restb2b.fun/`
- Lighthouse: Performance 90, Accessibility 100, Best Practices 100, SEO 100.
- FCP 2.8 s, LCP 2.8 s, TBT 0 ms, CLS 0, Speed Index 4.0 s.
- Lighthouse results vary between runs; the hard regression threshold remains Performance 77 and SEO 100.

## Publication evidence

- Production revision: `5505ff7` on `origin/main`.
- Live HTTP: 200 for all six canonical HTML pages, `robots.txt`, `sitemap.xml`, `llms.txt`, and `llms-full.txt`.
- Live DOM: expected H1 and FAQ present on all six pages; mobile menus open; no horizontal overflow at 390 px.
- Post-release Lighthouse: Performance 91, Accessibility 100, Best Practices 100, SEO 100.
- FCP 2.8 s, LCP 2.8 s, TBT 0 ms, CLS 0.014, Speed Index 3.2 s.
- IndexNow submission: HTTP 200 for all six canonical URLs.
- R1-R8: pass.
