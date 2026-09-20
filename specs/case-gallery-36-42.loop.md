# SpecLoop state: case-gallery-36-42

- Spec version: 1.0
- Baseline revision: b3b4b8b
- Current phase: REVIEW
- Iteration: 1
- Task-owned paths: `index.html`, `assets/images/gallery/work-36.webp` through
  `work-42.webp`, `scripts/build_before_after_collage.py`,
  `tests/test_case_gallery.py`, and this task's SpecLoop artifacts.
- External publication: explicitly authorized by the user request to publish the
  new photos to the site.
- Review 1: score 9.2/10; P2 opened for incomplete card/JSON-LD coverage.
- Review 2: score 8.3/10; P1 opened for unreproducible HEIC input and P2 opened
  for incomplete WebP contract coverage.
- Repairs: added direct HEIC conversion support, documented it, and strengthened
  regression coverage for per-card markup, matching structured metadata, WebP
  container, and 1600x1600 dimensions.
- Review 3: score 8.8/10; P2 opened for non-behavioral HEIC coverage and an
  incomplete source-pair manifest.
- Repairs: added a behavior test for configured HEIC conversion and a source-pair
  manifest with relative paths, hashes, and output names.
- Implementation checks: 31 unit tests PASS; static site validation PASS; direct
  HEIC rebuild PASS; JSON manifest validation PASS; `git diff --check` PASS.
- Open findings: none pending final independent review.
- Review 4: score 8.7/10; P2 opened for an intermediate-copy provenance mismatch
  for work 38 and incomplete output/source hash coverage.
- Repairs: regenerated work 38 directly from the manifest pair and added manifest
  output hashes plus optional private-source hash verification.
- Implementation checks: 32 unit tests PASS with private source hashes enabled;
  direct work-38 rebuild byte comparison PASS; static validation and JSON manifest
  validation PASS; `git diff --check` PASS.
- Open findings: none pending final acceptance review.
