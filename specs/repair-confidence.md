# Repair confidence and search content

Version: 1.0. Date: 2026-09-11. Mode: autonomous.
Baseline: fea26cdbaaa5bf03f0c6433bcf8f3001257cf4c4.

## Objective and current state

Adapt useful customer-answer patterns from Surface Master to Restoration B2B,
then publish on the existing restb2b.fun GitHub Pages site. The user clarified
that "FB" means AI systems, not Facebook. Existing 17 static pages cover products,
chips, glaze, price and assessment, but do not explain finish expectations or care.

## Scope and requirements

- R1: Add one distinct, original Russian resource about appearance after local
  repair, acceptance, use and care. Include a real existing photo and concise FAQ.
- R2: Broaden the ceramics page's heading and customer questions without inventing
  artistic ceramic services or nationwide operations. Add visible homepage answers
  and contextual links from relevant service/conditions pages to the new resource.
- R3: Make enquiry preparation clearer with a prefilled email draft and existing
  plain email/phone fallback. No form backend, automatic sending, data collection
  or false submission-success state. The draft must not claim photos are attached.
- R4: Keep FAQ JSON-LD identical to visible answers; add canonical metadata,
  sitemap and machine-summary discovery for the new resource. Summaries remain
  optional descriptions, not a claimed AI inclusion mechanism.
- R5: Preserve owner-confirmed cosmetic-only scope, bath materials, one-item
  acceptance, contacts, gallery behavior, fonts and effects. No competitor text,
  photographs, reviews, credentials, savings, warranty or durability promises.
- R6: Publish the validated revision without force pushes; verify actual live
  bytes and browser behavior. Synchronize the owner's original project, ZIP and
  UPLOAD_TO_GITHUB with tracked source, excluding temporary files.

## Constraints, assumptions and exclusions

The business works in Saint Petersburg. Baths: local acrylic/ceramic chips only.
No structural/hermetic repair, cast iron/steel baths, full recoating, antiques or
ceramic dishes. No confirmed warranty duration, universal cure time or home visits.
Care copy asks clients to obtain material-specific instructions, not generic
chemical/temperature directions. Preserve unrelated untracked files.
No new accounts, external publications, purchased links, hosting migration,
tracking scripts, social integrations or guarantees of top-three/AI citations.

## Acceptance and required checks

- R1/R2/R5: Read the rendered content and diff; new content visible without JS;
  real image loads; contextual links from homepage plus at least two other pages.
- R3: Parse mailto recipient, subject/body; verify fallback contacts and no form
  or network submission. Do not open an email client or send a real message.
- R4/R5: Run `python3 -m unittest discover -s tests -v`, the site validator and
  HTML validation on all canonical pages. Add focused regression tests.
- R1-R5: Headless Chrome checks across desktop/mobile, existing gallery/menu,
  image rendering, no horizontal overflow; inspect changed-page screenshots.
- R6: Successful GitHub deployment, `python3 scripts/verify_live.py`, browser
  smoke test on production, exact tracked-file archive/export comparison.
- Independent read-only review with evidence; minimum 9.5/10 and no failed
  requirements before final PASS. Production evidence may complete after review.

## Failure and completion

Do not publish failed validation. If remote advanced, reconcile without overwriting
user changes. A mailto draft needs a configured email app; visible email/phone work
as fallbacks. IndexNow receipt, if submitted, is not indexing or ranking evidence.
Done means R1-R6 verified and remaining search/AI uncertainty stated honestly.
