# Organic Search Growth Evidence

## R1: Custom-domain indexing signals

- Updated `index.html`, `robots.txt`, `sitemap.xml`, and `llms.txt` to use `https://restb2b.fun/`.
- Static scan: no old GitHub Pages address in shipped root files.

## R2 and R3: Service pages

- Added four public pages:
  - `restavratsiya-santehnicheskoy-keramiki.html`
  - `vosstanovlenie-skolov-santehniki.html`
  - `vosstanovlenie-glazuri-santehniki.html`
  - `restavratsiya-reklamatsionnyh-partiy.html`
- Each page has a unique title, description, canonical URL, H1, Service JSON-LD, contacts, FAQ, and related-service links.

## R4 and R5: Discovery and internal linking

- Added all service URLs to `sitemap.xml` and `llms.txt`.
- Added crawlable service links to `index.html`.

## R6: JavaScript compatibility

- Added null guards in `assets/js/main.js` so optional landing-page components do not throw errors on service pages.

## Checks

- `node --check assets/js/main.js`: PASS.
- `xmllint --noout sitemap.xml`: PASS.
- Node SEO validation: PASS for title, canonical, H1, and parseable JSON-LD on all five pages.
- Node local link/asset validation: PASS.
- Local HTTP checks on five pages plus `robots.txt`, `sitemap.xml`, and `llms.txt`: all `200`.
- `git diff --check`: PASS.

## Remaining uncertainty

- Search engines and LLMs control their own crawl schedule and ranking. The new URLs will be submitted through IndexNow after deployment, but organic position cannot be guaranteed.
