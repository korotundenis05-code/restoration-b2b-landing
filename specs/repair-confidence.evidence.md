# Verification evidence

Spec: repair-confidence.md v1.0. Baseline: fea26cd.

## Sources and adaptation

- Surface Master FAQ: https://www.surfacemaster.co.uk/faq (read 2026-09-11).
  Adapted topics, not text: visibility of repairs, acceptance, care, quote preparation.
  Excluded their warranty, no-fix-no-fee terms, savings, response/cure times,
  nationwide/onsite implications, structural repairs, photos and testimonials.
- Google guidance: https://developers.google.com/search/docs/appearance/ai-features
  Accessible text, internal discovery and matching structured data help eligibility;
  no special AI markup or guaranteed indexing/citation. Existing llms summaries
  updated for consistency only, not represented as a ranking mechanism.
- User clarified AI rather than Facebook. No social integration was introduced.

## Requirement mapping

- R1: rezultat-i-uhod-posle-restavratsii.html; five visible FAQs, existing photo,
  sections appearance/acceptance/care/replacement. Original cautious copy.
- R2: Homepage/category answers and links from seven relevant pages. Ceramics
  heading covers the general topic but visible text retains sanitary-only scope
  and Saint Petersburg. No duplicate product pages added.
- R3: kontakty-i-usloviya.html#enquiry; native mailto draft with recipient and
  percent-encoded subject/body, manual photo attachment, plain email/phone fallback.
  No form, backend, JavaScript changes, telemetry or automatic sending.
- R4: Sitemap, JSON-LD and both llms descriptions updated. New resource added to
  discovery validation. Visible FAQ text is the exact source of structured answers.
- R5: Existing boundary regression tests retained, four new tests added.
  Photos, styling, scripts, gallery and contacts are unchanged.
- R6: Published content revision 239d838a69c91125f356d348310e6a2697757d85.
  GitHub Pages workflow 34561480104 succeeded. Original project was fast-forwarded
  without overwriting untracked files; original, ZIP and UPLOAD_TO_GITHUB contained
  the same 115 tracked files with exact bytes. Final report-only revision will
  repeat deployment and full tracked-manifest export verification before handoff.

## Completed checks

- `python3 -m unittest discover -s tests -v`: exit 0, 14 tests.
- Integrated site validator: PASS for 18 canonical pages, links, assets, metadata,
  FAQ agreement, anchors, internal discovery and factual summary boundaries.
- html-validate 11.11.0, all 18 canonical HTML files: exit 0.
  Google/Yandex ownership verification files excluded, preserved verbatim.
- `git diff --check`: exit 0.
- Chrome desktop/mobile checks: exit 0; all 18 pages at 1440x960 and 390x960,
  36 cases. Contacts, headings, page/text overflow, menu/Escape, images, gallery
  expand/collapse/lightbox and email draft parsing pass; no JavaScript errors.
- Visual inspection: new resource desktop/mobile, homepage FAQ desktop and
  enquiry mobile, all consistent with existing design and without overlap.
  Screenshots: sibling directory restb2b-confidence-qa, not published.
- Additional Chrome check with JavaScript disabled at 320x800: new resource,
  category and conditions page answers visible, no horizontal overflow; exit 0.
- Independent review found no actionable defects. The same read-only reviewer
  accepted direct production/export evidence, closed R6 and returned SPECLOOP PASS,
  9.8/10. Full result: repair-confidence.review.md.

## Production checks

- `python3 scripts/verify_live.py`: exit 0; all 18 canonical pages and six supporting
  files HTTP 200, correct final URLs and exact bytes matching the content revision.
  No noindex/nosnippet response headers; robots permits YandexBot, Googlebot,
  Bingbot and OAI-SearchBot on every canonical page.
- Chrome against https://restb2b.fun/: exit 0, all 36 desktop/mobile cases passed,
  including new content, images, enquiry draft, navigation and gallery behavior.
  Live screenshots in sibling directory restb2b-confidence-live-qa, not published.
- IndexNow: eight changed/new canonical pages submitted to Yandex after the live
  key file was verified. HTTP 200 with `success: true`, 2026-09-11.
  This confirms receipt, not crawling, indexing, ranking or inclusion in AI answers.
- Provider verification files, domain, hosting settings and robots preserved.

No result here demonstrates a search position or an AI citation.
