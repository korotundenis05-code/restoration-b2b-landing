# Bing Webmaster onboarding evidence

Date: 2026-09-15. Site: `https://restb2b.fun/`.

## Requirement evidence

### R1 - ownership file

- `BingSiteAuth.xml` is present at the repository root with token
  `9F43905F2BE154A8D51F956CFDE8BCE2`.
- Production byte comparison passed for
  `https://restb2b.fun/BingSiteAuth.xml`.
- Bing Webmaster Tools visibly reported:
  `Congratulations! Site addition successful` and confirmed that
  `https://restb2b.fun` was added.

### R2 - regression protection

- `tests/test_bing_webmaster.py` enforces the exact XML bytes, element
  structure, empty attribute sets and account token.
- Mutation coverage rejects altered attributes, an extra element, a changed
  token and CRLF-normalized content.

### R3 - existing site behavior

- The 18-page canonical set, contacts and confirmed service boundaries remain
  covered by the complete test suite and `scripts/validate_site.py`.
- No visible layout, service, contact or crawler-policy change was introduced
  by the verification file.
- A later Bing URL inspection notice identified the homepage hero image as
  missing useful alt text. The image now has an accurate description, is no
  longer hidden from accessibility APIs, and the validator rejects empty image
  alt values across the canonical set.

### R4 - production deployment

- Commit `6fad73a6a520106522e0a125823dd64ffacd273f` was pushed to `main`.
- GitHub Pages workflow run `34971578165` completed successfully.
- `python3 scripts/verify_live.py` reported that all 18 canonical pages and 7
  supporting files matched the checkout, including `BingSiteAuth.xml`.
- Final deployment evidence for the homepage alt repair is recorded in the
  final review after the follow-up release completes.

### R6 - Bing notice repair

- The homepage hero image now exposes an accurate alt description for the
  before/after ceramic repair example and is no longer hidden from
  accessibility APIs.
- The validator requires meaningful alt text for accessible images while
  allowing intentionally decorative images inside an `aria-hidden="true"`
  subtree.
- Regression coverage checks the hero DOM structure, both JSON-LD modified
  dates, the homepage sitemap entry and the validator's decorative-image
  branch.
- Local verification is complete. Live-byte verification of the follow-up
  release remains pending while the GitHub Pages deployment finishes.

### R5 - Bing discovery and reports

- Bing accepted `https://restb2b.fun/sitemap.xml` for processing on
  2026-09-15. The Sitemaps report showed 1 known sitemap, 0 errors and 0
  warnings; its immediate state was `Processing` with 0 URLs discovered.
- Bing URL Submission accepted all 18 canonical URLs. The report showed
  `18 URLs submitted Successfully`, 18 submitted today and 82 daily quota
  remaining.
- URL Inspection reported the homepage as `Indexed successfully` and
  `URL can appear on Bing`.
- Search Performance displayed `Please check back in 48 hours while we prepare
  the data for your site`.
- AI Performance for the three-month view showed 0 citations, 0 cited pages
  and no grounding-query rows. This is the measured baseline, not a claim of
  AI visibility.
- Recommendations had no data available immediately after onboarding.

## ChatGPT discovery evidence

- In a fresh ChatGPT web-search chat, a broad unbranded restoration query did
  not cite `restb2b.fun`.
- A precise Saint Petersburg query for local repair of chips on ceramic sinks
  and toilets also did not cite `restb2b.fun`; it cited competitors instead.
- A direct-domain request successfully opened, summarized and cited
  `https://restb2b.fun/` as the source. The summary correctly reflected the
  products, local-repair scope, limitations and pricing caveat.
- Therefore the site is readable and citable when named. Unbranded discovery
  and authority remain external, lagging outcomes.

## Automated checks

- `python3 -m unittest discover -s tests -v`: PASS, 25 tests.
- `python3 scripts/validate_site.py`: PASS, 18 canonical pages.
- `xmllint --noout sitemap.xml BingSiteAuth.xml`: PASS.
- `git diff --check`: PASS.

## External uncertainty

Bing crawl timing, search position, Microsoft Copilot/partner citations and
ChatGPT citations are controlled by external systems. Verification, sitemap
submission and URL submission do not guarantee a ranking or citation and are
not represented as doing so.
