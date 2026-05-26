# mepgazine

Production repository for the MEP magazine — articles, layouts, assets, and source files for the print edition.

## Repository structure

```
.
├── issues/         # Per-issue working folders (e.g. issues/2026-q2/)
├── articles/       # Manuscripts, drafts, and edited copy
├── layouts/        # InDesign files (.indd) and exported PDFs
├── assets/         # Photography, illustrations, logos, fonts
└── archive/        # Final, shipped issues (read-only after release)
```

> Folders are created as needed — empty placeholders are not committed.

## Workflow

1. **Draft** — copy lands in `articles/<issue>/<slug>.md` (or `.docx`).
2. **Edit** — revisions tracked via commits; reviewers comment on PRs.
3. **Layout** — designer pulls approved copy into InDesign under `layouts/<issue>/`.
4. **Assets** — supporting photography and graphics live in `assets/<issue>/`.
5. **Release** — finalized issue moves to `archive/<issue>/` and is tagged (e.g. `v2026.q2`).

## Branching

- `main` — canonical, release-ready state.
- `claude/*` — automation / AI-assisted edits.
- `issue/<slug>` — per-issue working branches; merged to `main` on sign-off.

## Large files

Binary design files (InDesign, high-res TIFF/PSD, raw video) should be tracked with **Git LFS**. Initialize before adding:

```bash
git lfs install
git lfs track "*.indd" "*.psd" "*.tiff" "*.ai"
git add .gitattributes
```

## Conventions

- File names: lowercase, hyphenated (`feature-headline.md`, not `Feature Headline.md`).
- Commit messages: short, present-tense (`add Q2 cover draft`, `revise editor's letter`).
- One PR per editorial change so reviewers can comment cleanly.
