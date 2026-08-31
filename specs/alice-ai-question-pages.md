# Alice AI Question Pages

## Objective

Add six substantive Russian-language question pages that answer common customer intents and provide search engines and Alice AI with clear, factual, citable content.

## Current behavior

The site has commercial service pages and FAQ blocks, but no dedicated pages for the six customer questions identified in the visibility audit.

## Desired behavior

Each question has a unique canonical page with a direct answer, decision criteria, limitations, next steps, visible FAQ, structured data, and internal links. All pages are discoverable from the homepage, sitemap, and LLM summaries.

## In scope

- Six static HTML pages for the approved questions.
- Homepage resource section linking all six pages.
- Contextual links from existing service pages.
- Article, WebPage, BreadcrumbList, and FAQPage JSON-LD aligned with visible content.
- Sitemap, `llms.txt`, and `llms-full.txt` updates.
- Production publication, live verification, IndexNow resubmission, and local archive refresh.

## Out of scope

- Invented guarantees, reviews, certifications, fixed prices, addresses, or repair methods.
- Claims that every defect is repairable or safe.
- Guaranteed rankings or guaranteed Alice AI citation.
- New business accounts or paid promotion.

## Assumptions

- Geography and contacts remain Saint Petersburg, `das05@list.ru`, and `+7 965 767-29-66`.
- The service concerns cosmetic restoration after assessment; structural, installation, and safety defects are excluded.
- The 10% figure is an indicative economic reference, not a tariff or public offer.
- Immediate production publication remains authorized by the user.

## Requirements

R1. Add six unique canonical pages for the exact approved customer questions.

R2. Every page must provide a concise direct answer near the top, substantive unique guidance, assessment inputs, service limitations, a visible FAQ, and contacts.

R3. Every page must include valid WebPage, Article, BreadcrumbList, and FAQPage JSON-LD matching visible content.

R4. The homepage must expose a visible internal-link section to all six pages without disturbing existing workflows or responsive layout.

R5. Existing relevant service pages must link contextually to the matching question pages.

R6. Sitemap and Russian LLM discovery files must list all six pages with current factual descriptions.

R7. Existing crawler access, analytics verification files, gallery behavior, and contacts must remain unchanged.

R8. All pages must pass HTML, JSON-LD, local-link, JavaScript, XML, responsive overflow, and live HTTP checks.

R9. Reviewed changes must be published to `origin/main`, submitted to IndexNow, and included in the local ZIP and `UPLOAD_TO_GITHUB` copy.

## Required checks

- `html-validate` on all twelve public HTML pages.
- JSON-LD parse, metadata, H1, canonical, unique-title, and local-link validation.
- `node --check assets/js/main.js`.
- `xmllint --noout sitemap.xml`.
- `git diff --check`.
- Desktop and 390 px responsive DOM checks.
- Live HTTP and content verification after deployment.
- IndexNow response inspection.
- Archive and upload-copy manifest/content comparison against tracked files.

## Definition of done

R1-R9 pass, no blocking review findings remain, production and local artifacts contain the same reviewed version, and external ranking uncertainty is stated honestly.
