# LLM/SEO Adaptation Spec

Version: 2026-08-20.1

## Objective
Make the static Restoration B2B landing page easier for search engines and LLM search systems to crawl, understand, cite, and display for relevant queries about B2B restoration of sanitary ceramics in Saint Petersburg.

## Current Behavior
The site has a public one-page landing page with useful service text and images, but lacks robots.txt, sitemap.xml, structured data, dedicated FAQ content, canonical/Open Graph metadata, and an LLM-friendly summary file.

## Desired Behavior
The site should expose crawl-friendly metadata and visible content that clearly states the service, location, audience, contact methods, and common questions.

## Requirements
R1. Add robots.txt that allows general search crawlers and known AI/search crawlers, and points to sitemap.xml.
R2. Add sitemap.xml for the public GitHub Pages URL.
R3. Add llms.txt with concise service facts, contact details, URL, location, and allowed use guidance for LLM/search summarization.
R4. Improve index.html head metadata: title, description, canonical URL, robots directive, keywords, Open Graph, Twitter card, and theme color.
R5. Add Schema.org JSON-LD describing the business/service, website, image gallery, and FAQ.
R6. Add a visible FAQ section with concise answers relevant to LLM and search queries.
R7. Preserve current visual design and existing gallery/contact behavior.
R8. Prepare all changed files in UPLOAD_TO_GITHUB and attempt direct git publication if credentials allow.
R9. Add an IndexNow verification key and submit public URLs through IndexNow after the key is live.

## Out of Scope
Guaranteeing that ChatGPT, Grok, Yandex Alice, DeepSeek, Google, Bing, or Yandex will immediately cite the site. Indexing and LLM answer inclusion are controlled by external systems.

## Checks
C1. Static file existence and content checks for robots.txt, sitemap.xml, llms.txt.
C2. Parse JSON-LD from index.html as valid JSON.
C3. Confirm key SEO/LLM strings exist in index.html.
C4. Verify no obvious broken local file references for added metadata assets.
C5. If publishing succeeds, fetch live files and confirm updated content; otherwise mark publication as requiring manual upload.
C6. Confirm IndexNow key file is live and IndexNow API accepts the submitted URLs.

## Definition of Done
All files are implemented, locally validated, copied to UPLOAD_TO_GITHUB, and either pushed to GitHub or ready for manual upload with exact file list.
