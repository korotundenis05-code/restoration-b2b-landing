# Organic Search Growth

## Objective

Improve the technical indexing signals and topical relevance of `https://restb2b.fun/` for B2B sanitary-ceramics restoration queries in Saint Petersburg.

## Current behavior

The live site is a single landing page. Its canonical URLs, structured data, `robots.txt`, `sitemap.xml`, and `llms.txt` still refer to the previous GitHub Pages address.

## Desired behavior

The custom domain is the only declared public URL and the site contains useful, crawlable pages for its principal B2B services.

## In scope

- Correct custom-domain canonical and discovery URLs.
- Add four static service pages with unique Russian B2B content.
- Link pages together and add them to sitemap and LLM discovery text.
- Preserve existing visual language and all user-provided gallery content.
- Publish the reviewed change to the existing GitHub repository.

## Out of scope

- Guaranteed top-three organic position.
- Paid advertising, review manipulation, and third-party directory profiles which require account ownership.
- Claims about licences, addresses, prices, or guarantees not supplied by the owner.

## Assumptions

- The service area is Saint Petersburg and contacts remain `das05@list.ru` and `+7 965 767-29-66`.
- The user explicitly authorized publishing to the existing repository and deployment.

## Requirements

R1. Every canonical, Open Graph, structured-data and discovery URL uses `https://restb2b.fun/`.

R2. Add separate, indexable pages for: sanitary ceramics restoration, chip restoration, glaze restoration, and B2B reclamation batches.

R3. Each page includes an accurate title, description, canonical, clear H1, unique service information, internal links, contacts, and Service structured data.

R4. The sitemap and `llms.txt` list every public page on the custom domain.

R5. The existing landing page includes crawlable links to the four service pages.

R6. JavaScript continues to work on the main landing page and does not throw errors on service pages.

## Acceptance criteria and checks

- R1, R4: static URL scan and live HTTP check after deployment.
- R2, R3, R5: HTML parser check for pages, metadata, headings, internal links, and JSON-LD.
- R6: browser console and interaction check on the main page, plus console check on every service page.

## Definition of done

All requirements pass, the change is reviewed, committed, pushed to `origin/main`, GitHub Pages serves the new files, and IndexNow receives the updated URLs.
