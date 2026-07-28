# Executor Brief — MINDMEP spread production

You are producing redesigned magazine spreads for MINDMEP (Mint Building Services).
Work from `/home/user/mepgazine/issues/mindmep-01/`.

## Read first, in this order
1. `DESIGN-SYSTEM.md` — tokens, type scale, archetypes, craft rules, and the flatplan
   (which copy source feeds each new spread). BINDING.
2. `spreads/base.css` — use its classes/tokens; add per-spread inline or `<style>` only
   for layout geometry. Never fork or override token values.
3. The ORIGINAL spread render(s) for your copy sources:
   `/tmp/claude-0/-home-user/c2357ef3-7775-5f83-aff3-41e2792e4a74/scratchpad/pages/spread-NN.png`
   (NN = OLD spread number from the flatplan). View them with the Read tool — you are
   redesigning these layouts, so know what they looked like.
4. Copy: `copy/spread-NN.json` (styled text dump of old spread NN: spans with font,
   size, colour, bbox) and/or the refined article in `/home/user/mepgazine/articles/`.
   Refined article text is AUTHORITATIVE where the flatplan says A1/A3/A4/A41 —
   use it verbatim (trim only to fit, cutting whole paragraphs from the end of a
   section, never rewriting). Strip tracked-changes artefacts like "Not yet finished" /
   "Not Yet Reviewed" — those are review notes, not copy.

## Produce
One HTML file per assigned spread: `spreads/spread-XX.html` (XX = NEW spread number,
zero-padded). Template:

```html
<!doctype html>
<meta charset="utf-8">
<link rel="stylesheet" href="base.css">
<div class="spread" data-document-role="page" data-label="SHORT LABEL">
  ...
</div>
```

- Canvas is exactly 1418×998. Absolute positioning is fine and encouraged; this is a
  fixed print canvas, not responsive web.
- Images: relative paths `../assets/pNN-xK.jpg` (NN = OLD spread the asset came from —
  use assets from your spread's copy-source spreads, or a neighbouring one if it fits
  better). Check an image's aspect before sizing; crop with `object-fit: cover`.
- `data-label` example: "07 — Company opener".

## Verify (mandatory, every spread)
Render and LOOK at your work:
```bash
cd /home/user/mepgazine/issues/mindmep-01 && python3 render.py png spread-XX.html
```
Then Read `renders/spread-XX.png`. Iterate until:
- No text overflow, no text crossing the centre gutter (x=709), no orphan slivers.
- Type sizes/roles match the design system table; body ≤ 68ch measure.
- Contrast: ink-on-white body, pure white on navy; no grey body text.
- Section colour coding correct (COMPANY mint / PROJECTS lilac / PEOPLE sky /
  FEATURES coral / TECHNOLOGY peach).
- Folios on editorial/body pages only (not covers, not full-bleed photo spreads, not
  section openers): spread XX holds A5 pages (2·XX−2) left and (2·XX−1) right.
  Format: `<num>` + `MINDMEP` per `.folio` classes, outer corners.
- It should look like a designed magazine page a human art director shipped: committed
  hierarchy, one clear focal point, generous whitespace, no filler decoration.

## Report
Return a short list: spread number → one-line description + any judgement calls or
copy cuts you made. Do NOT run git. Do NOT edit base.css or DESIGN-SYSTEM.md.
