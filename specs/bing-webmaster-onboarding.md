# Bing Webmaster onboarding

Version: 1.1. Date: 2026-09-15. Mode: autonomous.
Baseline: `9bedae9515f0d7c121db0c3b07f29fa0c60f0a24`.

## Objective

Verify `https://restb2b.fun/` in Bing Webmaster Tools, submit the canonical
Sitemap and request discovery of the site's public pages without changing the
confirmed business scope or visible design.

## Requirements

- R1: Publish the account-specific `BingSiteAuth.xml` file unchanged at the
  domain root.
- R2: Protect the verification filename, XML structure and token with a
  regression test.
- R3: Preserve all existing pages, crawler rules, contacts and service
  boundaries. Existing metadata remains unchanged except for a narrowly
  scoped, evidence-backed SEO/GEO repair recorded under R6.
- R4: Deploy through the existing GitHub Pages workflow and verify the live
  file before completing Bing verification.
- R5: Submit `https://restb2b.fun/sitemap.xml` and inspect Bing's indexing
  reports after ownership is confirmed.
- R6: Resolve the actionable homepage image accessibility/SEO notice reported
  by Bing URL Inspection without changing the visible design or service copy;
  keep the validator permissive for intentionally hidden decorative images.

## Acceptance

- Unit tests, site validation, XML parsing and diff checks pass.
- GitHub Pages deploy succeeds.
- The live XML bytes match the reviewed file.
- Bing visibly reports ownership verification success.
- Sitemap submission is visibly accepted by Bing.
- The R6 repair passes local checks and is live-byte verified after deployment.

Indexing, ranking and ChatGPT citation changes are external outcomes and are
not implied by successful verification or submission.
