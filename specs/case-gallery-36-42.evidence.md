# Evidence: case-gallery-36-42

## Implementation evidence

| Requirement | Changed paths | Evidence |
| --- | --- | --- |
| R1 | `assets/images/gallery/work-36.webp` through `work-42.webp`; `scripts/build_before_after_collage.py` | Seven source-derived two-panel collages generated at 1600x1600. Visual inspection confirms white canvas, rounded vertical panels, no labels or added artwork. |
| R2 | `index.html`; `tests/test_case_gallery.py` | The seven cases use existing deferred `data-src` markup and existing `data-gallery-toggle` behavior. |
| R3 | `index.html` | Descriptive Russian alt text and seven `ImageObject` entries added to the existing `ImageGallery` JSON-LD. |
| R4 | `tests/test_case_gallery.py` | Test verifies all seven deferred cards, lightbox target URLs, alt text, source files, and a minimum non-empty asset size. |
| R5 | Pending | Publication and public checks run after review and push. |

## Local checks

- `python3 -m unittest discover -s tests -v`: PASS, 29 tests.
- `python3 scripts/validate_site.py`: PASS, 18 canonical pages.
- Square WebP check for `work-36.webp` through `work-42.webp`: PASS, each is 1600x1600.
- `git diff --check`: PASS.

## Repair iteration 3

- Reviewer finding P2 closed: `work-38.webp` was regenerated directly from its
  two manifest-listed source JPEGs rather than from intermediate copies.
- Reviewer finding P2 closed: the manifest now records output SHA-256 values;
  tests validate strict hash syntax and each committed WebP's hash. When the
  private source root is supplied through `CASE_GALLERY_SOURCE_ROOT`, the same
  test suite verifies every listed source file against its manifest hash.
- Direct rebuild of work 38: PASS. `cmp` confirmed an exact byte match with the
  committed asset.
- `CASE_GALLERY_SOURCE_ROOT=... python3 -m unittest discover -s tests -v`:
  PASS, 32 tests, including all private-source hash checks.
- `python3 scripts/validate_site.py`: PASS, 18 canonical pages.
- `python3 -m json.tool scripts/case-gallery-36-42-manifest.json`: PASS.
- `git diff --check`: PASS.

## Repair iteration 2

- Reviewer finding P2 closed: a Pillow-backed behavioral test now simulates a
  configured HEIC converter and verifies that the builder emits a 1600x1600 WebP.
  The test is skipped only where Pillow, an optional local authoring dependency,
  is unavailable.
- Reviewer finding P2 closed: `scripts/case-gallery-36-42-manifest.json` records
  the selected relative input paths, SHA-256 values, and exact output names. It
  uses an environment variable rather than committing a local filesystem path.
- `python3 -m unittest discover -s tests -v`: PASS, 31 tests.
- `python3 scripts/validate_site.py`: PASS, 18 canonical pages.
- `python3 -m json.tool scripts/case-gallery-36-42-manifest.json`: PASS.
- `git diff --check`: PASS.
- Direct HEIC rebuild: PASS. The collage builder generated a 1600x1600 WebP from
  source folder 36 after `HEIF_CONVERT` was set to the available `heif-convert`
  executable.

## Repair iteration 1

- Reviewer finding P1 closed: the collage builder now has an explicit HEIC/HEIF
  conversion path using `HEIF_CONVERT` or a PATH-discoverable `heif-convert`.
- Reviewer finding P2 closed: the regression test now parses WebP RIFF dimensions
  with the standard library and validates card containment, placeholder source,
  deferred source, alt text, and matching structured-image caption.
- `python3 -m unittest discover -s tests -v`: PASS, 30 tests.
- `python3 scripts/validate_site.py`: PASS, 18 canonical pages.
- `git diff --check`: PASS.

## Remaining verification

- Independent read-only review.
- GitHub Pages workflow result.
- Public byte comparison and browser interaction after deployment.
