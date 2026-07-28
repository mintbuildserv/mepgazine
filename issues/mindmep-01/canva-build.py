#!/usr/bin/env python3
"""Build the single-file Canva import HTML from spreads/*.html.

Canva's HTML importer flattens CSS pseudo-elements and does not fetch @font-face
files, so this build:
  - drops @font-face and uses bare family names ("Roboto", "Space Grotesk") that
    exist in Canva's font library;
  - converts .dropcap ::first-letter caps into an explicit flex row (giant mint
    glyph + remainder of the paragraph);
  - converts .pullquote ::before rules into a real bar element;
  - scopes each page's local <style> under its page id;
  - rewrites relative asset paths to absolute raw.githubusercontent URLs.
Output: mindmep-01-canva.html (42 divs annotated data-document-role="page").
"""
import re, glob

RAW = ('https://raw.githubusercontent.com/mintbuildserv/mepgazine/'
       'claude/mint-magazine-redesign-7370nr/issues/mindmep-01/')

base = open('spreads/base.css').read()
base = re.sub(r'@font-face \{[^}]*\}\n', '', base)
base = base.replace("'Roboto VF'", "'Roboto'").replace("'Space Grotesk VF'", "'Space Grotesk'")
base = re.sub(r'\.dropcap::first-letter \{[^}]*\}\n', '', base)
base = re.sub(r'\.pullquote::before \{[^}]*\}\n', '', base)

BAR = ('<span style="display:block;width:96px;height:8px;'
       'background:var(--rule, var(--mint));margin-bottom:24px"></span>')

def transform_dropcap(m):
    attrs, inner = m.group(1), m.group(2)
    attrs = attrs.replace('dropcap', '').replace('class=" ', 'class="')
    inner = inner.strip()
    cap, rest = inner[0], inner[1:]
    return (f'<div{attrs}><div style="display:flex;align-items:flex-start;gap:22px">'
            f'<div style="flex:0 0 auto;font-family:\'Space Grotesk\';font-weight:700;'
            f'color:var(--mint);font-size:190px;line-height:.75">{cap}</div>'
            f'<div style="flex:1">{rest}</div></div></div>')

pages, scoped = [], []
for f in sorted(glob.glob('spreads/spread-*.html')):
    n = int(re.search(r'(\d+)', f).group(1))
    pid = f'pg{n:02d}'
    src = open(f).read()
    for m in re.findall(r'<style>(.*?)</style>', src, re.S):
        rules = re.sub(r'/\*.*?\*/', '', m, flags=re.S)
        rules = re.sub(r'([^{}]+)\{', lambda mm: ','.join(
            f'#{pid} {s.strip()}' for s in mm.group(1).split(',')) + '{', rules)
        scoped.append(rules)
    dm = re.search(r'(<div class="spread[^"]*"[^>]*>.*)</div>\s*$', src, re.S)
    div = dm.group(1) + '</div>'
    div = div.replace('<div class="spread', f'<div id="{pid}" class="spread', 1)
    # dropcap paragraphs (p or div, class anywhere in the attr list)
    div = re.sub(r'<(?:p|div)([^>]*class="[^"]*dropcap[^"]*"[^>]*)>(.*?)</(?:p|div)>',
                 transform_dropcap, div, flags=re.S)
    # pullquotes: inject explicit bar as first child
    div = re.sub(r'(<[a-z]+[^>]*class="[^"]*pullquote[^"]*"[^>]*>)', r'\1' + BAR, div)
    div = div.replace('src="../assets/', f'src="{RAW}assets/')
    div = div.replace("url('../assets/", f"url('{RAW}assets/")
    div = div.replace('url("../assets/', f'url("{RAW}assets/')
    pages.append(div)

html = ('<!doctype html><html><head><meta charset="utf-8">'
        '<title>MINDMEP Issue 01</title><style>\n' + base + '\n' + '\n'.join(scoped) +
        '\n.spread { margin: 0 auto 24px; }\n</style></head><body>\n'
        + '\n'.join(pages) + '\n</body></html>')
open('mindmep-01-canva.html', 'w').write(html)
print('built mindmep-01-canva.html |', len(pages), 'pages |', len(scoped), 'scoped styles')
