# AI pricing clarity

Version: 1.0. Autonomous execution authorized by the user.
Baseline: fed20c5a49b514a0ddb5f7b009cf5b69d474be37.

## Objective and evidence

An actual Alice answer to the unbranded price query on 2026-09-16,
read on 2026-09-17, recommends the business but describes 10% of retail
value as its price. The homepage hero and economics paragraph present
that number prominently, although the detailed price pages qualify it.
Conversation: https://alice.yandex.ru/chat/01a0aa6d-92ce-436e-ab60-9b12ff56b9fe/

## Requirements

- R1: The homepage must present individual photo-based assessment, not 10%,
  as the service's pricing condition. Keep 10,000 / 100,000 only as an
  explicitly hypothetical economics example, not a quote or tariff.
- R2: The machine-readable summaries must make the same distinction.
- R3: Preserve services, contacts, gallery behavior, URLs, verification
  files and service limitations. Update homepage modification dates only.
- R4: Publish through the existing GitHub Pages workflow and verify public
  payloads against the checkout. Do not claim that this guarantees ranking.

## Scope and constraints

In scope: homepage copy, llms summaries, affected dates and focused tests.
Out of scope: new prices, guarantees, address, reviews, new services,
paid promotion, bulk pages, or a promise of AI inclusion/top-three ranking.
The original 10% is an illustration, not an independently verified tariff.
No personal data or browser account information belongs in the repository.

## Acceptance and checks

R1-R3: unittest regression checks, site validator, diff inspection,
desktop/mobile visual inspection of the changed text.
R4: successful Pages deployment and scripts/verify_live.py PASS.
Required: python3 -m unittest discover -s tests -v;
python3 scripts/validate_site.py; git diff --check;
python3 scripts/verify_live.py after deployment.

Done means required checks pass and the release is visible at restb2b.fun.
AI visibility observations are a separate dated report, not a release gate.
