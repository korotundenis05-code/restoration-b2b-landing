# Bing Webmaster onboarding

Version: 1.0. Date: 2026-09-15. Mode: autonomous.
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
- R3: Preserve all existing pages, crawler rules, metadata, contacts and
  service boundaries.
- R4: Deploy through the existing GitHub Pages workflow and verify the live
  file before completing Bing verification.
- R5: Submit `https://restb2b.fun/sitemap.xml` and inspect Bing's indexing
  reports after ownership is confirmed.

## Acceptance

- Unit tests, site validation, XML parsing and diff checks pass.
- GitHub Pages deploy succeeds.
- The live XML bytes match the reviewed file.
- Bing visibly reports ownership verification success.
- Sitemap submission is visibly accepted by Bing.

Indexing, ranking and ChatGPT citation changes are external outcomes and are
not implied by successful verification or submission.
