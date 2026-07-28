# MINDMEP — Mint Editorial Design System

Governing document for the MINDMEP magazine redesign. Every spread must comply.
Source of truth extracted from `MINDMEP_2_Azz_optimised.pdf` (50 spreads, A5 landscape
spread format) and refined per editorial-craft review.

## Canvas

- One HTML file per **spread** (two facing A5 portrait pages side by side).
- Canvas: **1418 × 998 px** (708.66 × 498.9 pt at 2 px/pt). `data-document-role="page"` on the spread root.
- Safe margins: 60 px outer edges, 90 px top for running elements, gutter at x = 709 (avoid placing body text across it; images MAY bleed across).
- Full-bleed imagery allowed and encouraged (the original uses full-bleed photo spreads as section breathers).

## Colour (Mint brand palette — identity preserved, never reinvent)

| Token | Hex | Role |
|---|---|---|
| `--ink` | `#0F222E` | Deep navy. Dominant surface (covers, contents, openers) and text on light |
| `--paper` | `#FFFFFF` | Page ground for body/editorial pages |
| `--mint` | `#4CBC8E` | Brand green. Logo underline, 01 COMPANY section, drop caps, highlights |
| `--coral` | `#F1583A` | 04 FEATURES section marker, hot accents |
| `--sky` | `#9BD9E5` | 03 PEOPLE section marker, cool accents (`#C8E9F2` tint) |
| `--lilac` | `#9F89C0` | 02 PROJECTS section marker |
| `--peach` | `#FFE2CB` | Occasional warm panel tint (sparing) |
| `--ink-90` | `rgba(15,34,46,.9)` | Scrim panels over photography |

Section colour-coding is systematic: every section carries its swatch as a short
underline bar beside the section number. New TECHNOLOGY pieces use `--mint` family
unless told otherwise (they sit in the Company/capability narrative).

Contrast rules (non-negotiable): body text on white is `--ink` (not grey);
text on navy is pure white ≥ 4.5:1; captions on navy use `#C8E9F2`, never mid-grey.

## Typography

Fonts: **Roboto** (display/headings, variable) + **Space Grotesk** (body/editorial, variable).
Local files in `fonts/` — never substitute.

| Style | Font | Size (px @2px/pt) | Notes |
|---|---|---|---|
| Giant display (openers, cover) | Roboto Bold/Black | 190–310 | Tight leading (0.92), letter-spacing ≥ -0.03em, `text-wrap: balance`. Exception: when the longest word cannot reach 190 without crossing the gutter on a single A5 page, size to the largest fit (floor 130) — the no-gutter-crossing rule always wins |
| Headline (article title on body pages) | Roboto Bold | 64–96 | |
| Section number (contents) | Roboto Bold | 190 | White on navy |
| Section name | Roboto Medium Italic | 48–56 | Tracked +0.18em, caps |
| Kicker / running label | Roboto ExtraBold | 15 | Caps, +0.35em tracking, section colour. Used ONLY as the magazine's section wayfinding system (e.g. `01 COMPANY`), never as decorative eyebrows on every block |
| Standfirst / deck | Space Grotesk Medium | 40 | Max 26 words |
| Pull quote | Space Grotesk Medium | 40–44 | With 6 px section-colour rule above (not a side stripe) |
| Subhead | Roboto Bold | 28 | Sentence case |
| Body | Space Grotesk Regular | 18 | Line-height 1.5, columns ~284 px wide (matches the original 10pt/120pt measure); 17 permitted on the densest spreads; justify OFF (rag right) |
| Caption / credit | Space Grotesk Regular | 15 | |
| Contact card | Roboto Bold 20 / Space Grotesk 17 | | White on navy rounded panel, 24 px radius |
| Drop cap | Space Grotesk Bold | 200, `--mint` | 4-line drop, opener paragraph only, one per article |
| Folio | Space Grotesk Medium | 15 | Page number + `MINDMEP` at outer bottom corners of editorial pages |

## Layout grammar (page archetypes)

1. **Cover** — navy field, giant MINDꟺEP wordmark (white, the ꟺ is flipped with a
   `--mint` underline bar), full-width hero photo panel, "IN THIS ISSUE" glass scrim
   card (right third, `backdrop blur` + `--ink-90`) with kicker-labelled entries.
2. **Full-bleed photo spread** — single image across the spread, no text. Used as
   pacing between sections.
3. **Contents** — navy ground, `Contents` in Roboto Bold 96, two photo cards each
   with giant section number + italic tracked name + swatch bar + story list
   (bold title + 2-line description).
4. **Section opener** — full-bleed photo or textured navy; kicker top-left with
   swatch bar; giant stacked display headline (white), max 3 lines per page;
   standfirst on the facing page or lower third.
5. **Editorial body** — white ground, 3 columns per A5 page (two used for text, one
   free for images/quotes is common), drop cap on opening paragraph, subheads in
   Roboto Bold, images squared to the column grid, captions beneath. Folio strip.
6. **Project spotlight** — kicker `ONGOING`/`COMPLETED`, project name Roboto Bold 40,
   country + key stat row (stat in Space Grotesk Bold 40), 2-col description,
   photo(s) filling remaining grid cells.
7. **Profile opener (People)** — duotone/blueprint-textured navy photo ground, cutout
   portrait right page, kicker `03 PEOPLE`, giant stacked headline.
8. **Contact card** — navy rounded panel: circular headshot 150 px, name Roboto Bold,
   role + email + phone Space Grotesk, optional `Got a project…?` lead-in with
   section-colour bold phrase.
9. **Back cover** — navy, tracked country labels (`S I N G A P O R E`), address blocks,
   logo.

## Craft rules (redesign, not just replication)

- Spacing rhythm on an 8 px scale; section spacing tiers 32/56/96 px.
- Never letter-space lowercase body text. Tracked caps only for kickers/section names.
- No gradient-fill display text (the original's "NEW" iridescent fill fails contrast —
  replace with solid white or section colour).
- Text never crosses the spread gutter; images may.
- Every image squared to the grid; no orphan slivers.
- Max one drop cap per article; drop caps never on continuation spreads.
- Body measure 60–68 ch; widows/orphans killed (`text-wrap: pretty`).
- Photography: use extracted originals in `assets/` (named `p<spread>-x<xref>.jpg` by
  source spread). Treat photos as full-bleed blocks or clean grid rectangles — never
  tilted, never framed, no drop shadows on images.
- Panels over photos use `--ink-90` scrim (or blur glass on cover only), text white.
- No decorative card grids, no side-stripe borders; accents are underline bars,
  colour blocks, and giant numerals — the Mint grammar.

## Issue map (redesigned flatplan)

Copy sources: `S##` = original copy from `copy/spread-##.json` (replicate, tightened);
`A1/A3/A4/A41` = refined articles in `articles/` (authoritative where present).

| New spread | Archetype | Content | Copy |
|---|---|---|---|
| 01 | Cover | MINDMEP cover, hero photo, In-this-issue card (update entries to refined stories) | S01 + new TOC entries |
| 02 | Photo | Full-bleed opener | — |
| 03 | Contents | 01 COMPANY / 02 PROJECTS | S04, updated story lists |
| 04 | Contents | 03 PEOPLE / 04 FEATURES + 05 TECHNOLOGY entry | S05, updated |
| 05 | Editorial | Editor's letter (left) + issue mockup photo & colophon (right) | S06 + S04 colophon |
| 06 | Editorial | Managing Director's note | S07 |
| 07 | Section opener | 01 COMPANY — "BEYOND THE ACRONYMS" | A1 |
| 08 | Editorial | Beyond the Acronyms body 1 | A1 |
| 09 | Editorial | Beyond the Acronyms body 2 | A1 |
| 10 | Editorial | Beyond the Acronyms body 3 + Mint-in-Thailand sidebar & Nuno contact card | A1 + S08/S09 condensed |
| 11 | Project spotlight | 02 PROJECTS — Ongoing: heritage shophouse | S10 |
| 12 | Project spotlight | Completed: The Laurus | S11 |
| 13 | Project spotlight | Completed: Coriander Leaf | S12 |
| 14 | Project spotlight | Completed: YETI APAC | S13 |
| 15 | Profile opener | 03 PEOPLE — Shan Nathan "FROM PROJECT FLOOR…" | S14 |
| 16 | Editorial | Shan standfirst spread ("…TO STRATEGY ROOM") | S15 |
| 17 | Editorial | Shan profile body 1 | S16 |
| 18 | Editorial | Shan profile body 2 + photo | S17–S18 |
| 19 | Profile opener | Jaymee Recto "MIND OVER MONEY" | S19 |
| 20 | Editorial | Jaymee body 1 | S20 |
| 21 | Editorial | Jaymee body 2 | S21 |
| 22 | Profile opener | Nuno Rio Tinto "LINE BY LINE, PIPE BY PIPE" | S22–S23 |
| 23 | Editorial | Nuno body 1 | S24 |
| 24 | Editorial | Nuno body 2 | S25 |
| 25 | Section opener | 04 FEATURES — "OLD BONES, NEW BEATS" | A4 |
| 26 | Editorial | Old Bones standfirst + intro | A4 |
| 27 | Editorial | Old Bones body (toolbox / space & structure) | A4 |
| 28 | Editorial | Old Bones body (performance / ghosts in walls) | A4 |
| 29 | Editorial | Old Bones close + full-bleed photo | A4 |
| 30 | Section opener | Feature: "21 KEPPEL: STRIPPED BACK, POWERED FORWARD" | A41 |
| 31 | Editorial | 21 Keppel body 1 | A41 |
| 32 | Editorial | 21 Keppel body 2 | A41 |
| 33 | Editorial | 21 Keppel close + Project Sherlock bridge | A41 + S38 |
| 34 | Editorial | Project Sherlock (China Square) | S38, S40–41 |
| 35 | Section opener | 05 TECHNOLOGY — "LOW VOLTAGE, HIGH STAKES" | A3 |
| 36 | Editorial | Low Voltage body 1 | A3 |
| 37 | Editorial | Low Voltage body 2 | A3 |
| 38 | Section opener | Feature: Curtin Singapore "THREE YEARS, FIVE PHASES" | S42–S44 |
| 39 | Editorial | Curtin body 1 | S45 |
| 40 | Editorial | Curtin body 2 | S46–S47 |
| 41 | Editorial | Curtin body 3 (what good looks like) | S48–S49 |
| 42 | Back cover | Addresses SG / MY / TH, logo | S50 |

TECHNOLOGY is a new 05 section: swatch `--sky` deepened to `#5FB7C9` family if `--sky`
clashes with PEOPLE — final call: TECHNOLOGY uses **`--peach` bar on navy** to stay
distinct. Keep folios sequential (A5 page numbers 1–84).
