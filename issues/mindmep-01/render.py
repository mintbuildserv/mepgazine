#!/usr/bin/env python3
"""Render spreads/*.html to review PNGs and assemble the print PDF.

Usage:
  python3 render.py png [spread-globs...]   # review screenshots -> renders/
  python3 render.py pdf                     # assemble mindmep-01.pdf (all spreads in order)
"""
import sys, glob, os, asyncio

BASE = os.path.dirname(os.path.abspath(__file__))
W, H = 1418, 998
PT_W, PT_H = "8.2677in", "5.8268in"  # A5 landscape: 210 x 148 mm

async def main():
    from playwright.async_api import async_playwright
    mode = sys.argv[1] if len(sys.argv) > 1 else "png"
    pats = sys.argv[2:] or ["spread-*.html"]
    files = sorted({f for p in pats for f in glob.glob(os.path.join(BASE, "spreads", p))})
    os.makedirs(os.path.join(BASE, "renders"), exist_ok=True)
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        page = await browser.new_page(viewport={"width": W, "height": H})
        pdfs = []
        for f in files:
            await page.goto("file://" + f)
            await page.wait_for_timeout(150)
            name = os.path.splitext(os.path.basename(f))[0]
            if mode == "png":
                await page.screenshot(path=os.path.join(BASE, "renders", name + ".png"),
                                      clip={"x": 0, "y": 0, "width": W, "height": H})
                print("png", name)
            else:
                out = os.path.join(BASE, "renders", name + ".pdf")
                await page.pdf(path=out, width=PT_W, height=PT_H,
                               print_background=True, page_ranges="1")
                pdfs.append(out); print("pdf", name)
        await browser.close()
    if mode == "pdf":
        import fitz
        doc = fitz.open()
        for p in pdfs: doc.insert_pdf(fitz.open(p))
        doc.save(os.path.join(BASE, "mindmep-01.pdf"), deflate=True, garbage=3)
        print("assembled", len(pdfs), "spreads -> mindmep-01.pdf")

asyncio.run(main())
