# Case gallery 36-42

## Objective

Publish one clean before/after collage for each source folder 36 through 42 in the
existing `До / После` gallery on the live Restoration B2B site.

## Baseline

- Repository: `restb2b-ai-upgrade-20260910`
- Baseline revision: `b3b4b8b`
- Current gallery has `work-01.webp` through `work-38.webp`.
- Source images are kept outside the repository in the user's Desktop folder.
- `scripts/case-gallery-36-42-manifest.json` records the selected relative source
  paths, SHA-256 values, and output filenames without publishing the photos or a
  local filesystem path.

## Scope

In scope:

- Replace gallery assets 36-38 and add assets 39-42.
- Build square WebP collages matching the visual pattern of source folder 35:
  white canvas, two vertical rounded photo panels, no text or synthetic retouching.
- Add the seven cases to the existing collapsed gallery and update their accessible
  descriptions and structured image metadata.
- Add a regression check, run site validation, deploy to GitHub Pages, and verify
  the public site.

Out of scope:

- Editing, moving, or deleting any original source photo.
- Changing the gallery layout, the initial eight-card view, or unrelated site copy.
- Claiming visual repair beyond what the supplied before/after photos show.

## Assumptions

- In every folder the photo with the visible defect is shown first and the cleaner
  result second. Folder 42 uses the marked defect detail as the before image and
  the clean follow-up image as the after image.
- Reusing the matching folder number for the gallery filename is intentional:
  folders 36-42 map to `work-36.webp` through `work-42.webp`.

## Requirements

### R1. Faithful source collages

Create seven 1600x1600 WebP images from the source pairs. Each must preserve the
photo pixels except for EXIF orientation correction, cover cropping, rounded panel
masking, and WebP compression. No labels, logos, generated artwork, or retouching
may be added.

### R2. Gallery publication

The home-page gallery must reference every `work-36.webp` through `work-42.webp`.
They must use the existing deferred loading and `Показать больше` behavior so the
first-screen gallery size does not grow.

### R3. Discoverability and accessibility

Every new image must have a useful Russian alt description and be represented in
the page's existing `ImageObject` structured data without unsupported claims.

### R4. Regression safety

Add an automated check that confirms all seven assets and deferred gallery cards
exist. Existing validation and unit tests must pass.

### R5. Publication

Commit and push the approved changes to the configured GitHub repository, wait for
the GitHub Pages deployment, and verify the images on `https://restb2b.fun/`.

## Acceptance criteria

- AC1 (R1): assets `work-36.webp` through `work-42.webp` exist, are square WebP,
  and visibly use the two-panel white composition.
- AC2 (R2): clicking `Показать больше` reveals the seven new cards and their
  lightbox targets load.
- AC3 (R3): the seven image elements have non-empty descriptive Russian alt text;
  structured data has matching image URLs.
- AC4 (R4): `python3 -m unittest discover -s tests -v`,
  `python3 scripts/validate_site.py`, and `git diff --check` pass.
- AC5 (R5): the Pages workflow succeeds and public asset bytes match the committed
  files.

## Check plan

| Requirement | Verification |
| --- | --- |
| R1 | Local image inspection, square-dimension check, and asset file check |
| R2 | Automated gallery regression test and browser interaction on production |
| R3 | Automated gallery regression test and static site validator |
| R4 | Unit tests, validator, and whitespace diff check |
| R5 | GitHub Actions result, HTTP byte comparison, and browser check |
