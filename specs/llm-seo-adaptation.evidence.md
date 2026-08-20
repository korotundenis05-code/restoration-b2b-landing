# LLM/SEO Adaptation Evidence

Spec version: 2026-08-20.1

## Implementation Evidence

- R1: `robots.txt` added with allow rules for general crawlers, Googlebot, Bingbot, Yandex, OAI-SearchBot, GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot and Google-Extended. Sitemap directive included.
- R2: `sitemap.xml` added for `https://korotundenis05-code.github.io/restoration-b2b-landing/`.
- R3: `llms.txt` added with canonical URL, service summary, relevant Russian queries, audience, workflow, contacts and recommended citation summary.
- R4: `index.html` head updated with title, description, keywords, robots, author, theme color, canonical URL, Open Graph, Twitter card and favicon.
- R5: `index.html` includes valid Schema.org JSON-LD graph for `WebSite`, `LocalBusiness`/`ProfessionalService`, `ImageGallery` and `FAQPage`.
- R6: Visible FAQ section added with four user-facing questions and answers.
- R7: Existing contact links and gallery behavior preserved; CSS changes are additive for FAQ and prior gallery styling.
- R8: Changed publish files copied to `UPLOAD_TO_GITHUB`; direct git push succeeded for main SEO/LLM commit.
- R9: IndexNow verification key file `653524955ebf60c17f8f10b0e570502614f7c51a1d54e0c459165426ee205137.txt` added and published.

## Checks

- Local JSON-LD parse: PASS.
- Local sitemap XML parse: PASS.
- Local `robots.txt`, `sitemap.xml`, `llms.txt` HTTP check on `127.0.0.1:8081`: PASS.
- Local browser preview at `http://127.0.0.1:8081/#faq`: PASS.
- Git push of commit `09bd9cd Add LLM and SEO metadata`: PASS.
- GitHub Pages deployment status after push: PASS.
- Live `robots.txt`: PASS.
- Live `sitemap.xml`: PASS.
- Live `llms.txt`: PASS.
- Live home page contains canonical, FAQPage JSON-LD and FAQ section: PASS.
- Live JSON-LD parse from public URL: PASS.
- Live IndexNow key file: PASS.
- IndexNow API submission: PASS, returned `202 Accepted`.

## External Limitations

Search engine and LLM answer inclusion cannot be guaranteed or forced immediately from code. The site is technically ready for crawling and has been submitted through IndexNow; Google Search Console, Bing Webmaster Tools and Yandex Webmaster account ownership setup still requires a logged-in owner account.
