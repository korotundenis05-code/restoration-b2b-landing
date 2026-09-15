# Bing Webmaster onboarding loop

- Current phase: VERIFY
- Spec version: 1.1
- Baseline revision: 9bedae9515f0d7c121db0c3b07f29fa0c60f0a24
- Iteration: 5
- Findings opened: live checker omission; exact-byte test gap; metadata-scope gap; brittle hero test; decorative-alt validator scope; stale loop bookkeeping; follow-up live verification pending
- Findings closed: Bing XML added to live comparison; exact-byte and mutation tests added; R6 authorizes the evidence-backed SEO repair; hero and date tests are structural; decorative images are handled separately; spec and evidence counts updated
- Checks run: 25 unit tests; site validator; XML parser; diff check; independent pre-deployment reviews; Bing ownership, sitemap and 18 URL submissions recorded
- Latest local revision: `0e560f5` (`Fix Bing-reported homepage image metadata`)
- Pre-deployment review: no implementation findings; score capped at 9.3/10 because live verification is pending
- Remaining blockers: GitHub Pages completion and direct live-byte verification of the follow-up revision; external browser/API access is temporarily unavailable due the environment usage limit
- Final verdict: pending external verification
