# Search Visibility V2

## Objective

Strengthen the live site for its primary commercial search intents and make its factual content easier for search engines and answer engines to crawl, understand, and cite.

## Current behavior

The custom domain is crawlable and has focused service pages, but the homepage H1 leads with an operational outcome rather than the primary service, no dedicated cost page exists, service-page structured data is minimal, and `llms.txt` is primarily English despite a Russian audience.

## Desired behavior

The homepage clearly identifies the primary service and city, visitors can find transparent pricing criteria, every public page has useful machine-readable context, and current search/answer crawlers are explicitly allowed.

## In scope

- Improve homepage title, H1, navigation, service links, and visible pricing context.
- Add one substantive cost and assessment page.
- Add richer Service, WebPage, BreadcrumbList, and FAQ structured data where matching visible content exists.
- Expand Russian-language LLM discovery content and current crawler directives.
- Improve font loading without changing the selected Inter/Inter Tight typefaces.
- Update sitemap and publish to the existing GitHub Pages production site.

## Out of scope

- Guaranteed top-three rankings or guaranteed inclusion in every LLM response.
- Fabricated reviews, guarantees, certifications, legal data, address, or business history.
- Creation of external business profiles or backlinks requiring third-party account ownership.
- Paid advertising.

## Assumptions

- Service area and contacts remain Saint Petersburg, `das05@list.ru`, and `+7 965 767-29-66`.
- The existing 10% figure is an indicative restoration-cost reference, not a binding quote.
- The user has explicitly authorized immediate production publication.

## Requirements

R1. Homepage title and H1 name sanitary-ceramics restoration and Saint Petersburg while retaining the B2B reclamation outcome in visible supporting copy.

R2. A dedicated cost page explains the indicative 10% reference, pricing factors, evaluation process, exclusions, and contacts without presenting a fixed public offer.

R3. All public service pages expose valid, visible-content-aligned structured data for the page, service, breadcrumbs, and FAQ.

R4. `robots.txt` explicitly allows current search and answer-engine user agents already covered by the general allow rule, without reducing access for standard crawlers.

R5. `llms.txt` is primarily Russian, lists every canonical public page, states verifiable facts and limitations, and links to a detailed `llms-full.txt` summary.

R6. Sitemap and homepage internal links include the cost page, use the custom domain, and carry the current modification date.

R7. Font loading is initiated in document head with preconnect and uses only the weights required by the design; Lighthouse SEO must remain 100 and performance must not regress from the 77 baseline.

R8. The reviewed changes are published to `origin/main`, return HTTP 200 on the live domain, and all canonical URLs are submitted to IndexNow.

## Required checks

- Static HTML metadata, H1, local-link, JSON-LD, and canonical validation.
- XML validation for sitemap.
- JavaScript syntax validation.
- Lighthouse production audit before and after publication.
- Live HTTP and content verification for all public pages and discovery files.
- IndexNow response inspection.

## Definition of done

All requirements and checks pass, the reviewed commit is on `origin/main`, the production pages are live, and the remaining external ranking uncertainty is documented.
