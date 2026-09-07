#!/usr/bin/env python3
"""Render the House System v1 specimen frames.

Every frame below is a SPECIMEN: placeholder facts, fictional product names,
illustrative data. Nothing here is publishable. The frames exist so the founders
can see exactly what a C1 / C2 / C3 / C4 post and a Story look like in the
house system, and rebuild them in whatever tool they produce with (Figma, Canva,
CapCut, or this script).

Usage (from the repository root):

    python3 production/templates/src/render_frames.py            # HTML + PNG
    python3 production/templates/src/render_frames.py --html-only
    python3 production/templates/src/render_frames.py --only c2_  # filter by prefix
    python3 production/templates/src/render_frames.py --motion    # also build the C2 Reel pacing reference

Rendering needs a Chromium/Chrome binary. Set CHROME=/path/to/chrome if it is not
found automatically. This is a local production aid, not automation: it writes
files into the repository and touches nothing outside it.
"""
import argparse, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(HERE, "html")
RENDER_DIR = os.path.normpath(os.path.join(HERE, "..", "renders"))
CSS_REL = "../../../house-style/house.css"   # from src/html/ to production/house-style/

ENGINE_LABEL = {"C1": "Release Desk", "C2": "Rankings", "C3": "Market Desk", "C4": "Commentary", "ST": "Story"}
HANDLE_A = "@thestreetwearofficial"
HANDLE_B = "@sneakerbong"
SPECIMEN = "Specimen · placeholder facts"

# --------------------------------------------------------------------------- helpers

def shoe(fill="#14151A", fill2="#3A3B44", sole="#C9C6BC", lace="#F3EFE6"):
    """A generic, brand-neutral sneaker silhouette. Deliberately NOT any real model and
    carrying no brand mark. Stands in for the rights-cleared product image."""
    return f'''<svg class="shoe" viewBox="0 0 480 250" xmlns="http://www.w3.org/2000/svg">
  <path d="M28 190 H452 a22 22 0 0 1 0 44 H28 a22 22 0 0 1 0 -44 Z" fill="{sole}"/>
  <path d="M30 196 C 18 196, 12 176, 28 166 L 130 148 C 176 140, 196 104, 246 94 L 332 78 C 366 72, 386 56, 408 62 C 436 70, 448 108, 452 150 C 456 176, 448 196, 432 196 Z" fill="{fill}"/>
  <path d="M246 94 C 262 130, 300 160, 360 176 L 432 196 C 448 196, 456 176, 452 150 C 448 108, 436 70, 408 62 C 386 56, 366 72, 332 78 Z" fill="{fill2}"/>
  <circle cx="200" cy="128" r="7" fill="{lace}"/><circle cx="232" cy="116" r="7" fill="{lace}"/>
  <circle cx="264" cy="106" r="7" fill="{lace}"/><circle cx="296" cy="98" r="7" fill="{lace}"/>
  <path d="M340 80 C 372 66, 396 66, 416 78" stroke="{lace}" stroke-width="6" fill="none" stroke-linecap="round"/>
</svg>'''

PALETTES = [
    ("#14151A", "#3A3B44", "#C9C6BC"), ("#1D3A8A", "#2F5BD6", "#E8E4DA"), ("#7A1F1F", "#B23A3A", "#E8E4DA"),
    ("#2B4A2E", "#4E8A55", "#E8E4DA"), ("#5B4A2B", "#8C7345", "#E8E4DA"), ("#3B3B3B", "#8A8A8A", "#F0EDE4"),
    ("#0F2E3D", "#2A7A9A", "#E8E4DA"), ("#4A2B5B", "#7B4E9A", "#E8E4DA"),
]

def plate(i=0, w=936, h=600, label="Rights-cleared image goes here · provenance ID", extra_style=""):
    f, f2, s = PALETTES[i % len(PALETTES)]
    return (f'<div class="plate" style="width:{w}px;height:{h}px;{extra_style}">{shoe(f, f2, s)}'
            f'<div class="label">{label}</div></div>')

def doc(name, body, *, size="feed", engine="C2", surface="ink", handle=HANDLE_A, band_left=None,
        band_right="", counter="", specimen=True, story=False):
    tall = size in ("reel", "story")
    cls = f"frame {surface}{' tall' if tall else ''}{' story' if story else ''}"
    h = 1920 if tall else 1350
    left = band_left if band_left is not None else ENGINE_LABEL[engine]
    spec = f'<div class="specimen">{SPECIMEN}</div>' if specimen else ""
    return f'''<!doctype html>
<html><head><meta charset="utf-8"><title>{name}</title>
<link rel="stylesheet" href="{CSS_REL}">
<style>html,body{{width:1080px;height:{h}px;overflow:hidden}}</style></head>
<body><div class="{cls}" data-engine="{engine}" id="frame">
  <div class="band-top"><div class="engine">{left}</div><div>{handle}</div></div>
  {spec}
  {body}
  <div class="band-bottom"><div>{band_right}</div><div>{counter}</div></div>
</div></body></html>'''

FRAMES = []   # (name, size, html)

def frame(name, size, html):
    FRAMES.append((name, size, html))

# --------------------------------------------------------------------------- C2 — Rankings & Tier Lists (N = 7)

C2_ITEMS = [  # rank, name, colorway, reason, data chip — all fictional
    (1, "Runner 550", "Sea Salt", "Wears with everything, still under retail on resale.", "RETAIL $110 · RESALE $95"),
    (2, "Court 1 High", "Deep Royal", "The one high-top that never goes out of rotation.", "RETAIL $180 · RESALE $210"),
    (3, "Aero 90", "Chalk", "Comfort per dollar is unmatched at this price.", "RETAIL $140 · RESALE $120"),
    (4, "Trail XT", "Moss", "Built for weather; looks better scuffed.", "RETAIL $170 · RESALE $150"),
    (5, "Classic 77", "Cream", "Cheapest entry on the list, hardest to beat.", "RETAIL $70 · RESALE $65"),
    (6, "Gel 2160", "Silver", "Tech-runner shape without the tech-runner price.", "RETAIL $150 · RESALE $140"),
    (7, "Low Cut", "Bone", "Everyone owns it. That is the problem.", "RETAIL $115 · RESALE $105"),
]
C2_TITLE = "7 sneakers under $200 that still look expensive"
C2_SHORT = "Under $200, looks expensive"      # running head on item slides: ≤ 28 characters
C2_RANKED_BY = "Ranked by: looks-per-dollar · resale checked 2026-08 (illustrative)"

def c2_hook(size="feed"):
    body = f'''<div class="content">
  <div class="kicker">Rankings · 7 items · swipe</div>
  <h1 class="hook">7 sneakers<br>under $200<br>that still<br>look expensive</h1>
  <div class="sub">Ranked by looks-per-dollar. Resale checked, retail confirmed.</div>
  <div class="arrow abs" style="right:0;bottom:0">→</div>
</div>'''
    return doc("c2 hook", body, size=size, engine="C2", surface="ink", band_right=C2_RANKED_BY, counter="1/9")

def c2_method():
    body = '''<div class="content">
  <div class="kicker">How we ranked</div>
  <h2 class="title" style="margin-top:24px">Three tests,<br>no vibes</h2>
  <div class="rows" style="margin-top:56px">
    <div class="row"><div class="n">01</div><div class="t s">Under $200 at retail, right now</div></div>
    <div class="row"><div class="n">02</div><div class="t s">Resale within 20% of retail</div></div>
    <div class="row"><div class="n">03</div><div class="t s">Would we wear it in 2028</div></div>
  </div>
  <div class="sub" style="margin-top:56px">Prices are retail list prices; resale is the recent median last sale in common sizes.</div>
</div>'''
    return doc("c2 method", body, engine="C2", surface="ink", band_right="Optional slide · use when the ranking basis needs a sentence", counter="2/9")

def c2_item(rank, name, cw, reason, chip, size="feed", counter="", number_only=False):
    tall = size == "reel"
    ph = 560 if not tall else 500
    rank_px = 240 if not tall else 176
    number = f'<div class="rank" style="font-size:{rank_px}px">{rank}<span class="of">/7</span></div>'
    if number_only:
        body = f'''<div class="content" style="display:flex;align-items:center;justify-content:center">
  <div class="rank" style="font-size:420px">{rank}</div></div>'''
    else:
        body = f'''<div class="content">
  <div class="head" style="display:flex;align-items:flex-end;justify-content:space-between">{number}<div class="kicker" style="color:var(--t-paper-2)">{C2_SHORT}</div></div>
  <div style="margin-top:16px">{plate(rank, 936, ph)}</div>
  <h2 class="item-name" style="font-family:var(--display);font-size:{104 if not tall else 96}px;line-height:.92;text-transform:uppercase;margin:{36 if not tall else 28}px 0 0">{name} <span style="color:var(--t-paper-2)">‘{cw}’</span></h2>
  <div class="reason" style="margin-top:{20 if not tall else 14}px">{reason}</div>
  <div class="chips" style="margin-top:{28 if not tall else 20}px"><span class="chip">{chip}</span></div>
</div>'''
    return doc(f"c2 item {rank}", body, size=size, engine="C2", surface="paper", band_right=C2_RANKED_BY, counter=counter)

def c2_summary(size="feed", counter="9/9"):
    rows = "".join(f'<div class="row"><div class="n">{r:02d}</div><div class="t">{n} <span style="opacity:.55">‘{c}’</span></div><div class="v">{d.split("·")[0].replace("RETAIL ","")}</div></div>'
                   for r, n, c, _, d in C2_ITEMS)
    body = f'''<div class="content">
  <div class="kicker">The list</div>
  <h2 class="title" style="margin-top:16px">Under $200,<br>looks expensive</h2>
  <div class="rows" style="margin-top:40px">{rows}</div>
</div>'''
    return doc("c2 summary", body, size=size, engine="C2", surface="ink", band_right=C2_RANKED_BY, counter=counter)

def c2_static():
    grid = "".join(f'''<div class="cell" style="display:flex;flex-direction:column;gap:8px">{plate(r, 300, 200, label="")}
      <div style="display:flex;gap:12px;align-items:baseline"><span class="mono accent" style="font-size:34px;font-weight:700">{r:02d}</span>
      <span style="font-family:var(--display);font-size:44px;text-transform:uppercase;line-height:1">{n}</span></div></div>'''
                   for r, n, c, _, d in C2_ITEMS[1:])
    r, n, c, reason, d = C2_ITEMS[0]
    body = f'''<div class="content">
  <div style="display:flex;justify-content:space-between;align-items:flex-end">
    <h1 class="title" style="font-size:96px">7 sneakers under $200<br>that still look expensive</h1>
  </div>
  <div style="display:grid;grid-template-columns:420px 1fr;gap:24px;margin-top:32px;align-items:stretch">
    {plate(0, 420, 300, label="")}
    <div style="display:flex;flex-direction:column;justify-content:center;gap:8px">
      <div class="rank small" style="font-size:150px">1<span class="of">/7</span></div>
      <div style="font-family:var(--display);font-size:64px;text-transform:uppercase;line-height:.95">{n} ‘{c}’</div>
      <div class="small muted">{reason}</div>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px 18px;margin-top:28px">{grid}</div>
</div>'''
    return doc("c2 static", body, engine="C2", surface="paper", band_right=C2_RANKED_BY, counter="STATIC")

frame("c2_car_01_hook", "feed", c2_hook())
frame("c2_car_02_method_optional", "feed", c2_method())
r, n, c, re_, d = C2_ITEMS[6]; frame("c2_car_03_item_07", "feed", c2_item(r, n, c, re_, d, counter="3/9"))
r, n, c, re_, d = C2_ITEMS[0]; frame("c2_car_09_item_01", "feed", c2_item(r, n, c, re_, d, counter="9/10"))
frame("c2_car_10_summary", "feed", c2_summary())
frame("c2_static_hero_plus_6", "feed", c2_static())
frame("c2_reel_01_hook", "reel", c2_hook(size="reel"))
for r, n, c, re_, d in C2_ITEMS[::-1]:
    frame(f"c2_reel_item_{r:02d}_number", "reel", c2_item(r, n, c, re_, d, size="reel", counter=f"{r}/7", number_only=True))
    frame(f"c2_reel_item_{r:02d}", "reel", c2_item(r, n, c, re_, d, size="reel", counter=f"{r}/7"))
frame("c2_reel_summary", "reel", c2_summary(size="reel", counter="THE LIST"))
frame("c2_reel_end", "reel", doc("c2 end", '''<div class="content" style="display:flex;flex-direction:column;justify-content:center">
  <div class="kicker">Next week</div><h2 class="title">Another list,<br>same rules</h2>
  <div class="sub">Rankings every week. Retail confirmed, resale checked, no sponsors in the list.</div></div>''',
  size="reel", engine="C2", surface="ink", band_right="End card · 1.5 s", counter=""))

# --------------------------------------------------------------------------- C1 — Release & Verdict Desk

C1_FACTS = [("Release", "Sat 14 Sep"), ("Retail", "$185"), ("Sizes", "US 7–14"), ("Where", "App raffle")]
C1_PRODUCT = ("Court 1 High", "Deep Royal")

def facts_grid(items, mono_keys=("Retail", "Sizes")):
    return '<div class="facts">' + "".join(
        f'<div class="fact"><div class="k">{k}</div><div class="v{" mono" if k in mono_keys else ""}">{v}</div></div>' for k, v in items) + "</div>"

def c1_verdict_card(with_image=True):
    n, cw = C1_PRODUCT
    surface = "paper" if with_image else "ink"
    img = plate(1, 936, 400, label="Licensed / owned image · provenance ID") if with_image else ""
    body = f'''<div class="content">
  <div class="kicker">Verdict · drops Saturday</div>
  <h1 class="title" style="margin-top:12px;font-size:{'104' if with_image else '136'}px">{n} ‘{cw}’</h1>
  <div style="margin-top:{'20' if with_image else '48'}px">{img}</div>
  <div style="display:grid;grid-template-columns:1fr 340px;gap:24px;align-items:center;margin-top:{'20' if with_image else '64'}px">
    <div style="--fact-size:{'56' if with_image else '72'}px">{facts_grid(C1_FACTS).replace('class="v"', 'class="v" style="font-size:var(--fact-size)"').replace('class="v mono"', 'class="v mono" style="font-size:40px"')}</div>
    <div style="text-align:center"><span class="stamp cop" style="font-size:{'140' if with_image else '168'}px">COP</span></div>
  </div>
  <div class="reason" style="margin-top:{'24' if with_image else '64'}px">Retail is fair for the materials, sizes run full, and last year’s pair still resells above retail.</div>
</div>'''
    return doc("c1 verdict card", body, engine="C1", surface=surface,
               band_right="Source: brand release note 2026-09-08 · verified in tracking row", counter="STATIC")

def c1_car():
    n, cw = C1_PRODUCT
    hook = doc("c1 hook", f'''<div class="content">
  <div class="kicker">Release desk · verdict inside</div>
  <h1 class="hook">{n}<br>‘{cw}’<br>drops<br>Saturday</h1>
  <div class="sub">Price, sizes, where, and whether it is worth your money.</div>
  <div class="arrow abs" style="right:0;bottom:0">→</div></div>''',
        engine="C1", surface="ink", band_right="Source: brand release note 2026-09-08", counter="1/6")
    look = doc("c1 look", f'''<div class="content">
  <div class="kicker">The pair</div>
  <div style="margin-top:24px">{plate(1, 936, 700, label="Licensed / owned image · provenance ID")}</div>
  <h2 class="title m" style="margin-top:36px">{n} ‘{cw}’</h2>
  <div class="reason" style="margin-top:16px">Leather upper, padded collar, the original 1985-style cut. Two colourways at launch.</div></div>''',
        engine="C1", surface="paper", band_right="Materials from the brand product page · verified", counter="2/6")
    facts = doc("c1 facts", f'''<div class="content">
  <div class="kicker">The facts</div>
  <h2 class="title m" style="margin-top:16px">Price · sizes · where</h2>
  <div style="margin-top:48px">{facts_grid(C1_FACTS + [("Grade school", "$140"), ("Restock", "None announced")], mono_keys=("Retail","Sizes","Grade school"))}</div></div>''',
        engine="C1", surface="ink", band_right="Every figure verified against the logged source", counter="3/6")
    verdict = doc("c1 verdict", f'''<div class="content" style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:48px">
  <div class="kicker">The verdict</div>
  <span class="stamp cop" style="font-size:280px;border-width:14px">COP</span>
  <div class="sub" style="text-align:center;max-width:820px">Buy at retail. Do not pay resale.</div></div>''',
        engine="C1", surface="ink", band_right="Verdict scale: COP · WAIT · PASS", counter="4/6")
    why = doc("c1 why", '''<div class="content">
  <div class="kicker">Why</div>
  <h2 class="title m" style="margin-top:16px">Three reasons</h2>
  <div class="rows" style="margin-top:40px">
    <div class="row"><div class="n">01</div><div class="t s">Materials justify $185</div></div>
    <div class="row"><div class="n">02</div><div class="t s">Sizes run full · order true to size</div></div>
    <div class="row"><div class="n">03</div><div class="t s">Last year’s pair still resells above retail</div></div>
  </div>
  <div class="sub" style="margin-top:48px">Rubric: value 2 · wearability 2 · availability 1 · resale 2 → 7/8 → COP</div></div>''',
        engine="C1", surface="ink", band_right="Rubric scored in the tracking row", counter="5/6")
    docket = doc("c1 docket", f'''<div class="content">
  <div class="kicker">Docket</div>
  <h2 class="title m" style="margin-top:16px">{n} ‘{cw}’</h2>
  <div class="rows" style="margin-top:40px">
    <div class="row"><div class="n">WHEN</div><div class="t s">Saturday 14 September</div><div class="v">10:00 local</div></div>
    <div class="row"><div class="n">COST</div><div class="t s">$185 adult</div><div class="v">$140 GS</div></div>
    <div class="row"><div class="n">HOW</div><div class="t s">Retail app raffle · select stores</div><div class="v"></div></div>
    <div class="row"><div class="n">CALL</div><div class="t s up">COP at retail</div><div class="v"></div></div>
  </div></div>''',
        engine="C1", surface="ink", band_right="Source: brand release note 2026-09-08", counter="6/6")
    return [("c1_car_01_hook", hook), ("c1_car_02_the_pair", look), ("c1_car_03_facts", facts),
            ("c1_car_04_verdict", verdict), ("c1_car_05_why", why), ("c1_car_06_docket", docket)]

def c1_reel():
    n, cw = C1_PRODUCT
    hook = doc("c1 reel hook", f'''<div class="content">
  <div class="kicker">Drops Saturday</div>
  <h1 class="hook xl">{n}<br>‘{cw}’</h1>
  <div class="sub">Cop, wait, or pass? 30 seconds.</div>
  <div style="margin-top:40px">{plate(1, 936, 430, label="Licensed / owned image · provenance ID")}</div></div>''',
        size="reel", engine="C1", surface="ink", band_right="Beat 1 · 3.0 s", counter="")
    facts = doc("c1 reel facts", f'''<div class="content">
  <div class="kicker">The facts</div>
  <div style="margin-top:40px">{facts_grid(C1_FACTS, mono_keys=("Retail","Sizes"))}</div>
  <div style="margin-top:48px">{plate(1, 936, 420, label="Licensed / owned image · provenance ID")}</div></div>''',
        size="reel", engine="C1", surface="ink", band_right="Beat 2 · facts block · 8.0 s (2 s per fact)", counter="")
    verdict = doc("c1 reel verdict", '''<div class="content" style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:56px">
  <div class="kicker">The verdict</div><span class="stamp cop" style="font-size:320px;border-width:16px">COP</span>
  <div class="sub" style="text-align:center">Buy at retail.<br>Do not pay resale.</div></div>''',
        size="reel", engine="C1", surface="ink", band_right="Beat 3 · stamp reveal · 3.0 s", counter="")
    reason = doc("c1 reel reason", '''<div class="content">
  <div class="kicker">Why · 1 of 3</div>
  <h2 class="hook l" style="margin-top:24px">Materials<br>justify<br>$185</h2>
  <div class="sub">Full-grain leather, padded collar. Nothing at this price feels like it.</div></div>''',
        size="reel", engine="C1", surface="ink", band_right="Beats 4–6 · one reason each · 2.5 s", counter="")
    return [("c1_reel_01_hook", hook), ("c1_reel_02_facts", facts), ("c1_reel_03_verdict", verdict), ("c1_reel_04_reason", reason)]

frame("c1_static_verdict_card", "feed", c1_verdict_card(True))
frame("c1_static_verdict_card_no_image", "feed", c1_verdict_card(False))
for nm, html in c1_car(): frame(nm, "feed", html)
for nm, html in c1_reel(): frame(nm, "reel", html)

# --------------------------------------------------------------------------- C3 — Market & Price Intelligence

def line_chart(values, w=936, h=420, labels=None, unit="$"):
    n = len(values); lo, hi = min(values), max(values); pad = (hi - lo) * 0.18 or 1
    lo -= pad; hi += pad
    x = lambda i: 40 + i * (w - 80) / (n - 1)
    y = lambda v: 30 + (hi - v) * (h - 90) / (hi - lo)
    pts = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(values))
    area = f"M{x(0):.1f},{h-60} L" + " L".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(values)) + f" L{x(n-1):.1f},{h-60} Z"
    grid = "".join(f'<line class="grid" x1="40" x2="{w-40}" y1="{30 + k*(h-90)/4:.1f}" y2="{30 + k*(h-90)/4:.1f}"/>' for k in range(5))
    lab = ""
    if labels:
        lab = "".join(f'<text x="{x(i):.1f}" y="{h-18}" text-anchor="middle">{t}</text>' for i, t in enumerate(labels) if t)
    end = f'<circle class="dot" cx="{x(n-1):.1f}" cy="{y(values[-1]):.1f}" r="16"/><text class="lbl strong" x="{x(n-1)-20:.1f}" y="{y(values[-1])-30:.1f}" text-anchor="end">{unit}{values[-1]}</text>'
    start = f'<text class="lbl" x="{x(0):.1f}" y="{y(values[0])-24:.1f}">{unit}{values[0]}</text>'
    return f'<svg class="chart" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{grid}<path class="area" d="{area}"/><polyline class="line" points="{pts}"/>{start}{end}{lab}</svg>'

def spread_chart(rows, w=936, rowh=92):
    """rows: (name, retail, resale). Dumbbell from retail to resale; green if above retail, red if below."""
    h = rowh * len(rows) + 40
    mx = max(max(r[1], r[2]) for r in rows) * 1.15
    x = lambda v: 300 + v * (w - 340) / mx
    out = []
    for i, (name, ret, res) in enumerate(rows):
        cy = 40 + i * rowh + rowh / 2
        col = "var(--up)" if res >= ret else "var(--down)"
        out.append(f'<text class="lbl" x="0" y="{cy+10}">{name}</text>'
                   f'<line x1="{x(ret):.1f}" x2="{x(res):.1f}" y1="{cy}" y2="{cy}" stroke="{col}" stroke-width="10" stroke-linecap="round"/>'
                   f'<circle cx="{x(ret):.1f}" cy="{cy}" r="14" fill="var(--t-ink-2)"/><circle cx="{x(res):.1f}" cy="{cy}" r="16" fill="{col}"/>'
                   f'<text x="{x(max(ret,res))+28:.1f}" y="{cy+10}" class="lbl">{("+" if res>=ret else "−")}{abs(res-ret)*100//ret}%</text>')
    legend = '<circle cx="0" cy="14" r="10" fill="var(--t-ink-2)"/><text x="20" y="22">retail</text><circle cx="150" cy="14" r="10" fill="var(--up)"/><text x="170" y="22">resale</text>'
    return f'<svg class="chart" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg"><g transform="translate(0,0)">{legend}</g>{"".join(out)}</svg>'

MOVE = [212, 218, 209, 205, 214, 226, 231, 224, 219, 228, 236, 242]
MOVE_LABELS = ["Sep", "", "Nov", "", "Jan", "", "Mar", "", "May", "", "Jul", "Aug"]
SPREAD = [("Court 1 High", 180, 210), ("Runner 550", 110, 95), ("Aero 90", 140, 120), ("Trail XT", 170, 150), ("Gel 2160", 150, 140)]
C3_SRC = "Data: median last sale, common sizes, public listing pages · manual · as of 31 Aug 2026 (illustrative)"

def c3_static_move():
    body = f'''<div class="content">
  <div class="kicker">Resale · 12 months</div>
  <div style="display:flex;align-items:baseline;gap:32px;margin-top:8px"><div class="big-number up">+14%</div><div class="chip up">↑ $212 → $242</div></div>
  <h2 class="title m" style="margin-top:8px">Court 1 High resale,<br>Sep 2025 – Aug 2026</h2>
  <div style="margin-top:40px">{line_chart(MOVE, labels=MOVE_LABELS)}</div>
  <div class="data-foot" style="margin-top:32px">Median last sale, sizes US 8–11, public listing pages, manual collection. Data as of 31 Aug 2026. Chart is self-generated.</div>
</div>'''
    return doc("c3 move", body, engine="C3", surface="ink", band_right=C3_SRC, counter="STATIC")

def c3_static_spread():
    body = f'''<div class="content">
  <div class="kicker">Retail vs resale · this week</div>
  <h2 class="title" style="margin-top:12px;font-size:104px">Four of five<br>trade below retail</h2>
  <div style="margin-top:40px">{spread_chart(SPREAD)}</div>
  <div class="data-foot" style="margin-top:40px">Retail = list price. Resale = median last sale, sizes US 8–11, past 30 days. Manual collection from public listing pages. Data as of 31 Aug 2026.</div>
</div>'''
    return doc("c3 spread", body, engine="C3", surface="ink", band_right=C3_SRC, counter="STATIC")

def c3_car():
    hook = doc("c3 hook", '''<div class="content">
  <div class="kicker">Market desk</div>
  <h1 class="hook">Resale<br>is up 14%.<br>Here is<br>what moved</h1>
  <div class="sub">One silhouette, twelve months, public data, no guesses.</div>
  <div class="arrow abs" style="right:0;bottom:0">→</div></div>''',
        engine="C3", surface="ink", band_right=C3_SRC, counter="1/5")
    chart = doc("c3 chart", f'''<div class="content">
  <div class="kicker">The move</div>
  <div style="display:flex;align-items:baseline;gap:32px;margin-top:8px"><div class="big-number m up">+14%</div><div class="chip up">↑ $212 → $242</div></div>
  <div style="margin-top:40px">{line_chart(MOVE, labels=MOVE_LABELS)}</div>
  <div class="data-foot" style="margin-top:32px">Median last sale, US 8–11. Data as of 31 Aug 2026.</div></div>''',
        engine="C3", surface="ink", band_right=C3_SRC, counter="2/5")
    rows = "".join(f'<div class="row"><div class="n">{i+1:02d}</div><div class="t s">{n}</div><div class="v {"up" if b>=a else "down"}">{"+" if b>=a else "−"}{abs(b-a)*100//a}%</div></div>' for i, (n, a, b) in enumerate(SPREAD))
    brk = doc("c3 breakdown", f'''<div class="content">
  <div class="kicker">The breakdown</div>
  <h2 class="title m" style="margin-top:16px">Where the money went</h2>
  <div class="rows" style="margin-top:40px">{rows}</div>
  <div class="data-foot" style="margin-top:40px">Change in median last sale vs retail, past 30 days.</div></div>''',
        engine="C3", surface="ink", band_right=C3_SRC, counter="3/5")
    below = doc("c3 below retail", f'''<div class="content">
  <div class="kicker">Below retail right now</div>
  <h2 class="title m" style="margin-top:16px">Buy resale,<br>not retail</h2>
  <div style="margin-top:40px">{spread_chart([r for r in SPREAD if r[2] < r[1]])}</div>
  <div class="data-foot" style="margin-top:40px">Pairs where the resale median sits under list price. Sizes US 8–11.</div></div>''',
        engine="C3", surface="ink", band_right=C3_SRC, counter="4/5")
    method = doc("c3 method", '''<div class="content">
  <div class="kicker">Method &amp; sources</div>
  <h2 class="title m" style="margin-top:16px">How this was made</h2>
  <div class="rows" style="margin-top:40px">
    <div class="row"><div class="n">DATA</div><div class="t s">Median last sale, public listing pages</div></div>
    <div class="row"><div class="n">SIZES</div><div class="t s">US 8–11, pooled</div></div>
    <div class="row"><div class="n">WINDOW</div><div class="t s">1–31 Aug 2026</div></div>
    <div class="row"><div class="n">METHOD</div><div class="t s">Manual collection · no scraper · charts self-generated</div></div>
  </div>
  <div class="sub" style="margin-top:48px">Numbers are snapshots, not advice. Prices move.</div></div>''',
        engine="C3", surface="ink", band_right=C3_SRC, counter="5/5")
    return [("c3_car_01_hook", hook), ("c3_car_02_chart", chart), ("c3_car_03_breakdown", brk), ("c3_car_04_below_retail", below), ("c3_car_05_method_sources", method)]

def c3_reel():
    hook = doc("c3 reel hook", '''<div class="content">
  <div class="kicker">Market desk</div>
  <h1 class="hook xl">Resale<br>is up<br>14%</h1>
  <div class="sub">Twelve months, one silhouette. Watch the line.</div></div>''',
        size="reel", engine="C3", surface="ink", band_right="Beat 1 · 3.0 s", counter="")
    draw = doc("c3 reel draw", f'''<div class="content">
  <div class="kicker">Sep 2025 → Aug 2026</div>
  <div style="margin-top:40px">{line_chart(MOVE, h=520, labels=MOVE_LABELS)}</div>
  <div style="display:flex;align-items:baseline;gap:32px;margin-top:40px"><div class="big-number m up">+14%</div><div class="chip up">$212 → $242</div></div></div>''',
        size="reel", engine="C3", surface="ink", band_right="Beat 2 · line draws left→right over 3.0 s, then holds 2.0 s", counter="")
    point = doc("c3 reel point", '''<div class="content">
  <div class="kicker">Data point · 2 of 3</div>
  <h2 class="hook l" style="margin-top:24px">The dip<br>in December<br>was the<br>buy window</h2>
  <div class="chip down" style="margin-top:40px">↓ $205 · lowest of the year</div></div>''',
        size="reel", engine="C3", surface="ink", band_right="Beats 3–5 · one data point each · 2.5 s", counter="")
    take = doc("c3 reel take", '''<div class="content">
  <div class="kicker">Takeaway</div>
  <h2 class="hook l" style="margin-top:24px">Retail<br>is still<br>the deal</h2>
  <div class="data-foot" style="margin-top:56px">Median last sale, US 8–11, public listing pages, manual collection. Data as of 31 Aug 2026. Not advice.</div></div>''',
        size="reel", engine="C3", surface="ink", band_right="Beat 6 · 4.0 s · source line on screen", counter="")
    return [("c3_reel_01_hook", hook), ("c3_reel_02_chart_draw", draw), ("c3_reel_03_data_point", point), ("c3_reel_04_takeaway", take)]

frame("c3_static_move", "feed", c3_static_move())
frame("c3_static_spread", "feed", c3_static_spread())
for nm, html in c3_car(): frame(nm, "feed", html)
for nm, html in c3_reel(): frame(nm, "reel", html)

# --------------------------------------------------------------------------- C4 — Original Meme & Commentary

def c4_two_shoes():
    body = f'''<div class="content">
  <div class="kicker">Two shoes, one verdict</div>
  <h1 class="title" style="margin-top:12px;font-size:96px">Same $180.<br>One of these is a mistake.</h1>
  <div style="position:relative;margin-top:36px">
    <div class="split">
      <div class="cell"><div class="lab">A · the hyped one</div>{plate(2, 456, 360, label="Owned / licensed image")}</div>
      <div class="cell"><div class="lab">B · the boring one</div>{plate(0, 456, 360, label="Owned / licensed image")}</div>
    </div>
    <div class="vs" style="top:50%;">VS</div>
  </div>
  <div style="margin-top:40px;padding:32px 40px;background:var(--ink);color:var(--t-ink);border-radius:24px">
    <div class="kicker">Ruling</div>
    <div style="font-family:var(--display);font-size:80px;line-height:.95;text-transform:uppercase;margin-top:8px">B. You will wear it 200 times. A, twice.</div>
  </div></div>'''
    return doc("c4 two shoes", body, engine="C4", surface="paper", band_right="Format: TWO SHOES, ONE VERDICT · owned or licensed imagery only", counter="STATIC")

def c4_receipt():
    body = '''<div class="content" style="display:flex;flex-direction:column;justify-content:center">
  <div class="kicker" style="text-align:center;margin-bottom:32px">The receipt</div>
  <div class="receipt">
    <h3>SNEAKERHEAD LEDGER</h3>
    <div class="fine" style="margin:0 0 20px">2026 · one collector · rounded to the L</div>
    <div class="line"><span>Pairs bought “for resale”</span><span>9</span></div>
    <div class="line"><span>Pairs actually resold</span><span>2</span></div>
    <div class="line"><span>Profit on those two</span><span>$41.00</span></div>
    <div class="line"><span>Shipping, fees, tax</span><span>$236.50</span></div>
    <div class="line"><span>“Investment pieces” now worn</span><span>7</span></div>
    <div class="line total"><span>NET RESULT</span><span>A SHOE COLLECTION</span></div>
    <div class="fine">THANK YOU FOR PLAYING · NO REFUNDS ON TASTE</div>
  </div></div>'''
    return doc("c4 receipt", body, engine="C4", surface="ink", band_right="Format: THE RECEIPT · typographic · zero imagery", counter="STATIC")

def c4_hot_take():
    body = '''<div class="content" style="display:flex;flex-direction:column;justify-content:center">
  <div class="kicker" style="margin-bottom:24px">Hot take ticket · no. 014</div>
  <div class="ticket">
    <div style="display:flex;justify-content:space-between;font-family:var(--mono);font-size:26px;letter-spacing:.1em;text-transform:uppercase;color:var(--t-paper-2)"><span>Admit one opinion</span><span>Row C · Seat 4</span></div>
    <div class="tear"></div>
    <div style="font-family:var(--display);font-size:120px;line-height:.92;text-transform:uppercase;margin-top:88px">Your “grail” is just the first pair you couldn’t afford at 15.</div>
    <div class="body" style="margin-top:40px;color:var(--t-paper-2)">Nostalgia is a pricing model. The shoe did not get better; you got older.</div>
    <div style="display:flex;justify-content:space-between;margin-top:48px;font-family:var(--mono);font-size:26px;letter-spacing:.1em;text-transform:uppercase;color:var(--t-paper-2)"><span>Valid: forever</span><span>Non-transferable</span></div>
  </div></div>'''
    return doc("c4 hot take", body, engine="C4", surface="ink", band_right="Format: HOT TAKE TICKET · typographic · zero imagery", counter="STATIC")

def c4_math():
    body = f'''<div class="content">
  <div class="kicker">Sneakerhead math</div>
  <h1 class="title" style="margin-top:12px;font-size:96px">How a $110 shoe<br>costs $600</h1>
  <div style="display:grid;grid-template-columns:1fr 80px 1fr 80px 1fr;align-items:center;gap:8px;margin-top:48px;text-align:center">
    <div>{plate(0, 280, 190, label="")}<div class="mono" style="margin-top:12px;font-size:30px">1 pair · $110</div></div>
    <div style="font-family:var(--display);font-size:120px;color:var(--accent)">+</div>
    <div>{plate(3, 280, 190, label="")}<div class="mono" style="margin-top:12px;font-size:30px">“backup pair” · $110</div></div>
    <div style="font-family:var(--display);font-size:120px;color:var(--accent)">+</div>
    <div>{plate(5, 280, 190, label="")}<div class="mono" style="margin-top:12px;font-size:30px">“one to wear” · $110</div></div>
  </div>
  <div style="margin-top:40px;border-top:6px solid var(--ink);padding-top:28px;display:flex;justify-content:space-between;align-items:baseline">
    <div style="font-family:var(--display);font-size:88px;text-transform:uppercase">= three of the same shoe</div>
    <div class="mono" style="font-size:44px;font-weight:700">$330 + fees + shame</div>
  </div>
  <div class="reason" style="margin-top:32px;color:var(--t-paper-2)">The $600 is the pair you then buy so the three do not look sad.</div></div>'''
    return doc("c4 math", body, engine="C4", surface="paper", band_right="Format: SNEAKERHEAD MATH · owned/licensed/self-drawn imagery", counter="STATIC")

def c4_chat():
    s1 = doc("c4 chat 1", '''<div class="content">
  <div class="kicker">Group chat · 11:48 pm</div>
  <h2 class="title m" style="margin-top:16px">“It’s an investment”</h2>
  <div class="chat" style="margin-top:48px">
    <div class="bubble them"><span class="who">Dan</span>bought the pair. for resale obviously</div>
    <div class="bubble me"><span class="who">You</span>obviously</div>
    <div class="bubble them"><span class="who">Dan</span>just gonna wear them once to see</div>
    <div class="bubble me"><span class="who">You</span>see what</div>
    <div class="bubble them"><span class="who">Dan</span>the fit</div>
  </div></div>''', engine="C4", surface="ink", band_right="Format: GROUP CHAT · original UI drawn in the house system · never a screenshot", counter="1/2")
    s2 = doc("c4 chat 2", '''<div class="content">
  <div class="kicker">Group chat · 3 weeks later</div>
  <div class="chat" style="margin-top:48px">
    <div class="bubble them"><span class="who">Dan</span>ok they’re not for sale anymore</div>
    <div class="bubble me"><span class="who">You</span>investment matured?</div>
    <div class="bubble them"><span class="who">Dan</span>emotionally yes</div>
  </div>
  <div style="margin-top:72px;padding-top:40px;border-top:1px solid var(--ink-3)">
    <div style="font-family:var(--display);font-size:104px;line-height:.92;text-transform:uppercase">Every resale pair<br>is one wear from<br>a personal pair</div>
  </div></div>''', engine="C4", surface="ink", band_right="Format: GROUP CHAT · original UI · never a screenshot", counter="2/2")
    return [("c4_car_group_chat_01", s1), ("c4_car_group_chat_02_punchline", s2)]

def c4_reel():
    hook = doc("c4 reel hook", f'''<div class="content">
  <div class="kicker">Inner monologue</div>
  <h1 class="hook l">What I say<br>vs what<br>I think<br>at a drop</h1>
  <div style="margin-top:40px">{plate(6, 936, 400, label="Owned / licensed / self-drawn hero image")}</div></div>''',
        size="reel", engine="C4", surface="ink", band_right="Beat 1 · 3.0 s · kinetic text over one hero image", counter="")
    beat = doc("c4 reel beat", f'''<div class="content">
  <div class="kicker">Say</div>
  <h2 class="title" style="margin-top:8px;font-size:92px">“I’m just here<br>to look.”</h2>
  <div class="rule-line" style="margin:24px 0"></div>
  <div class="kicker" style="color:var(--t-ink-2)">Think</div>
  <h2 class="title" style="margin-top:8px;font-size:92px;color:var(--accent)">Size 10.<br>Two if they<br>have them.</h2>
  <div style="margin-top:36px">{plate(6, 936, 300, label="Same hero image holds through every beat")}</div></div>''',
        size="reel", engine="C4", surface="ink", band_right="Beats 2–7 · say/think pairs · 3.5 s each · 6 pairs ≈ 24 s + hook + end = 30 s", counter="")
    return [("c4_reel_01_inner_monologue_hook", hook), ("c4_reel_02_inner_monologue_beat", beat)]

def c4_ai_static():
    """AI-slot specimen. The frame is the ordinary EXPECTATION / REALITY layout: nothing on the artwork marks it
    as AI-treated. Disclosure lives in the fixed caption line and the platform AI label only, so the artwork
    treatment stays identical to the non-AI C4 posts. The plate labels are specimen annotations, as on every
    other frame, and are not part of the production design."""
    body = f'''<div class="content">
  <div class="kicker">Expectation / reality</div>
  <h1 class="title" style="margin-top:12px;font-size:96px">The shoe rack<br>you planned vs<br>the one you have</h1>
  <div style="position:relative;margin-top:36px">
    <div class="split">
      <div class="cell"><div class="lab">Expectation</div><div class="plate" style="width:456px;height:420px;background:linear-gradient(160deg,#243b6b,#5b7fd6)"><div class="label" style="color:#fff">Specimen: AI illustration goes here · no real product · no brand mark</div></div></div>
      <div class="cell"><div class="lab">Reality</div><div class="plate" style="width:456px;height:420px;background:linear-gradient(160deg,#6b2433,#d65b7f)"><div class="label" style="color:#fff">Specimen: AI illustration goes here · no real product · no brand mark</div></div></div>
    </div>
  </div>
  <div class="reason" style="margin-top:44px;color:var(--t-ink-2)">Disclosure is in the caption (fixed line) and the platform AI label — never on the artwork.</div>
</div>'''
    return doc("c4 ai static", body, engine="C4", surface="ink", band_right="AI slot specimen · identical artwork treatment to non-AI C4", counter="STATIC")

frame("c4_static_two_shoes_one_verdict", "feed", c4_two_shoes())
frame("c4_static_the_receipt", "feed", c4_receipt())
frame("c4_static_hot_take_ticket", "feed", c4_hot_take())
frame("c4_static_sneakerhead_math", "feed", c4_math())
for nm, html in c4_chat(): frame(nm, "feed", html)
for nm, html in c4_reel(): frame(nm, "reel", html)
frame("c4_ai_slot_static_expectation_reality", "feed", c4_ai_static())

# --------------------------------------------------------------------------- Stories — 7-day rotation

def story(name, cls_label, body, handle=HANDLE_A, engine="ST", accent_engine=None):
    d = doc(name, body, size="story", engine=engine, surface="ink", handle=handle, band_left=f"Story · {cls_label}",
            band_right="Daily · 17:30 UTC · one frame", counter="", story=True)
    if accent_engine:
        d = d.replace(f'data-engine="{engine}"', f'data-engine="{accent_engine}"')
    return d

frame("st_mon_drop_calendar", "story", story("st mon", "Mon · Drop calendar", '''<div class="content">
  <div class="kicker">This week’s confirmed drops</div>
  <div class="rows" style="margin-top:40px">
    <div class="row"><div class="n">TUE</div><div class="t s">Aero 90 ‘Chalk’</div><div class="v">$140</div></div>
    <div class="row"><div class="n">THU</div><div class="t s">Gel 2160 ‘Silver’</div><div class="v">$150</div></div>
    <div class="row"><div class="n">SAT</div><div class="t s">Court 1 High ‘Deep Royal’</div><div class="v">$185</div></div>
  </div>
  <div class="sub" style="margin-top:64px">Confirmed dates only. Verdicts on the feed as they land.</div></div>''', accent_engine="C1"))
frame("st_tue_price_check", "story", story("st tue", "Tue · Price check", '''<div class="content">
  <div class="kicker">One number</div>
  <div class="big-number up" style="margin-top:24px">$95</div>
  <h2 class="title m">Runner 550 ‘Sea Salt’<br>resale, this week</h2>
  <div class="chip down" style="margin-top:40px">↓ $15 under retail</div>
  <div class="data-foot" style="margin-top:56px">Median last sale, US 8–11, public listing pages, manual. As of yesterday.</div></div>''', accent_engine="C3"))
frame("st_wed_the_poll_sticker_day", "story", story("st wed", "Wed · The poll", '''<div class="content">
  <div class="kicker">Settle it</div>
  <h2 class="hook l" style="margin-top:16px">Same $180.<br>Which one?</h2>
  <div class="split" style="margin-top:48px">
    <div class="cell"><div class="lab">A</div><div style="font-family:var(--display);font-size:64px;text-transform:uppercase">Court 1 High</div></div>
    <div class="cell"><div class="lab">B</div><div style="font-family:var(--display);font-size:64px;text-transform:uppercase">Trail XT</div></div>
  </div>
  <div class="sticker-zone" style="margin-top:80px;padding:80px 32px">Poll sticker goes here<br>the ONE interactive sticker of the week</div></div>''', accent_engine="C2"))
frame("st_thu_desk_notes", "story", story("st thu", "Thu · Desk notes", '''<div class="content">
  <div class="kicker">From the desk</div>
  <h2 class="title m" style="margin-top:16px">How we rank</h2>
  <div class="body" style="margin-top:40px;color:var(--t-ink-2)">Three tests, every list: under the price cap at retail, resale within 20% of retail, and would we wear it in two years. No sponsors in any list during this run. Corrections get posted here.</div></div>'''))
frame("st_fri_the_verdict", "story", story("st fri", "Fri · The verdict", '''<div class="content" style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:48px">
  <div class="kicker">Saturday’s drop</div>
  <h2 class="title m" style="text-align:center">Court 1 High<br>‘Deep Royal’</h2>
  <span class="stamp cop" style="font-size:260px;border-width:14px">COP</span>
  <div class="sub" style="text-align:center">At retail. Not at resale.</div></div>''', accent_engine="C1"))
frame("st_sat_two_shoes", "story", story("st sat", "Sat · Two shoes", f'''<div class="content">
  <div class="kicker">Two shoes, one verdict</div>
  <h2 class="title m" style="margin-top:16px">Hyped vs boring</h2>
  <div class="split" style="margin-top:40px">
    <div class="cell">{plate(2, 456, 320, label="Owned / licensed")}</div>
    <div class="cell">{plate(0, 456, 320, label="Owned / licensed")}</div>
  </div>
  <div style="margin-top:56px;font-family:var(--display);font-size:88px;line-height:.95;text-transform:uppercase;color:var(--accent)">Boring wins. It always does.</div></div>''', accent_engine="C4"))
frame("st_sun_the_week", "story", story("st sun", "Sun · The week", '''<div class="content">
  <div class="kicker">This week on the feed</div>
  <div class="mosaic" style="margin-top:32px;grid-template-columns:repeat(4,1fr)">
    <div class="tile c2">Mon · ranking</div><div class="tile c1">Tue · verdict</div><div class="tile c3">Wed · market</div>
    <div class="tile c4">Thu · commentary</div><div class="tile c2">Fri · ranking</div><div class="tile c1">Sat · verdict</div>
    <div class="tile c4">Sun · commentary</div>
  </div>
  <div class="sub" style="margin-top:48px">Own artwork thumbnails only. No post links, no stickers.</div></div>'''))

# --------------------------------------------------------------------------- Diagnostics — safe zones

frame("diag_reel_safe_zones", "reel", doc("diag reel", '''
  <div class="safe" style="top:250px"><span>top 250 px · Instagram UI · keep clear</span></div>
  <div class="safe" style="top:285px;border-color:rgba(255,210,63,.6)"><span style="color:var(--c2);top:-34px">grid 4:5 crop of the cover starts (y = 285)</span></div>
  <div class="safe" style="top:1635px;border-color:rgba(255,210,63,.6)"><span style="color:var(--c2)">grid 4:5 crop of the cover ends (y = 1635)</span></div>
  <div class="safe" style="top:1500px"><span>bottom 420 px · caption, handle, audio · keep clear</span></div>
  <div class="abs" style="top:0;bottom:0;right:0;width:130px;border-left:3px dashed rgba(255,59,48,.75)"></div>
  <div class="content"><div class="kicker">Reel canvas 1080 × 1920</div><h1 class="hook l">Content<br>lives<br>here</h1>
  <div class="sub">Right 130 px: like / comment / share column. Cover title inside the yellow band.</div></div>''',
  size="reel", engine="ST", surface="ink", band_left="Diagnostic · safe zones", band_right="Not a template · a ruler", specimen=False))
frame("diag_feed_safe_zones", "feed", doc("diag feed", '''
  <div class="safe" style="top:135px;border-color:rgba(255,210,63,.6)"><span style="color:var(--c2)">1:1 crop starts (y = 135)</span></div>
  <div class="safe" style="top:1215px;border-color:rgba(255,210,63,.6)"><span style="color:var(--c2);top:-34px">1:1 crop ends (y = 1215)</span></div>
  <div class="content"><div class="kicker">Feed canvas 1080 × 1350</div><h1 class="hook l">Essential<br>content in<br>the square</h1>
  <div class="sub">Bands and margins are fixed. 72 px outer margin, 24 px gutter, 8 px unit.</div></div>''',
  engine="ST", surface="ink", band_left="Diagnostic · safe zones", band_right="Not a template · a ruler", specimen=False))

# --------------------------------------------------------------------------- render

def find_chrome():
    """Prefer Playwright's headless shell: its window size is exactly the viewport. The full
    Chrome binary in --headless=new mode keeps ~87 px for an invisible toolbar, which would cut
    the bottom band off every frame; render() compensates for that case."""
    base = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    cands = [os.environ.get("CHROME")]
    if os.path.isdir(base):
        for d in sorted(os.listdir(base), reverse=True):
            for rel in (("chrome-linux", "headless_shell"), ("chrome-linux", "chrome-headless-shell"),
                        ("chrome-win", "headless_shell.exe"), ("chrome-win", "chrome-headless-shell.exe"),
                        ("chrome-mac", "headless_shell"), ("chrome-linux", "chrome"), ("chrome-win", "chrome.exe")):
                cands.append(os.path.join(base, d, *rel))
    cands += [shutil.which("chrome-headless-shell"), shutil.which("chromium"), shutil.which("chromium-browser"),
              shutil.which("google-chrome"), shutil.which("chrome"),
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              r"C:\Program Files\Google\Chrome\Application\chrome.exe"]
    for c in cands:
        if c and os.path.exists(c):
            return c
    return None

def is_headless_shell(binary):
    return "headless" in os.path.basename(binary).lower()

def render(name, size, html, chrome, html_only):
    os.makedirs(HTML_DIR, exist_ok=True)
    out_dir = os.path.join(RENDER_DIR, name.split("_")[0] if not name.startswith(("st_", "diag_")) else ("story" if name.startswith("st_") else "diagnostics"))
    os.makedirs(out_dir, exist_ok=True)
    hpath = os.path.join(HTML_DIR, f"{name}.html")
    with open(hpath, "w", encoding="utf-8") as fh:
        fh.write(html)
    if html_only:
        return None
    h = 1920 if size in ("reel", "story") else 1350
    png = os.path.join(out_dir, f"{name}.png")
    shell = is_headless_shell(chrome)
    offset = 0 if shell else int(os.environ.get("CHROME_VIEWPORT_OFFSET", "87"))
    cmd = [chrome, "--headless" if shell else "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
           "--allow-file-access-from-files", "--force-device-scale-factor=1",
           f"--window-size=1080,{h + offset}", f"--screenshot={png}", "file://" + hpath]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    if offset:
        try:
            from PIL import Image
            im = Image.open(png)
            if im.size[1] > h:
                im.crop((0, 0, 1080, h)).save(png)
        except ImportError:
            print("  note: full Chrome used without Pillow; frame may carry extra rows at the bottom. "
                  "Install Pillow or point CHROME at a headless_shell binary.")
    return png

def build_motion(chrome):
    """C2 Reel pacing reference: hook 3.0 s · per item: number 0.4 s + card 3.6 s · summary 4.0 s · end 1.5 s = 36.5 s.
    Built as a 10 fps frame sequence (every frame hard-linked N times) so it needs no concat demuxer.
    Encoded as WebM (VP8) because that is the only video encoder Playwright's ffmpeg carries; any browser plays it.
    No audio by design: the track is added at upload from the Instagram royalty-free library."""
    ff = os.environ.get("FFMPEG") or shutil.which("ffmpeg") or "/opt/pw-browsers/ffmpeg-1011/ffmpeg-linux"
    if not os.path.exists(ff):
        print("ffmpeg not found; skipping motion reference"); return
    reel_dir = os.path.join(RENDER_DIR, "c2")
    seq = [("c2_reel_01_hook", 3.0)]
    for r in range(7, 0, -1):
        seq += [(f"c2_reel_item_{r:02d}_number", 0.4), (f"c2_reel_item_{r:02d}", 3.6)]
    seq += [("c2_reel_summary", 4.0), ("c2_reel_end", 1.5)]
    try:
        from PIL import Image
    except ImportError:
        print("Pillow not installed; skipping motion reference (pip install Pillow)"); return
    fps = 10
    enc = subprocess.run([ff, "-hide_banner", "-encoders"], capture_output=True, text=True).stdout
    if "libx264" in enc:
        codec, ext = ["-c:v", "libx264", "-crf", "26", "-preset", "medium", "-movflags", "+faststart"], "mp4"
    else:
        codec, ext = ["-c:v", "libvpx", "-b:v", "700k", "-auto-alt-ref", "0"], "webm"
    out = os.path.join(RENDER_DIR, "c2", f"C2_REEL_pacing_reference_36s.{ext}")
    # An MJPEG stream file read through image2pipe: the one input route that works on every ffmpeg build
    # tried, including Playwright's minimal one (no PNG decoder, no rawvideo demuxer, no pipe protocol).
    # The stream lives in a system temp directory and is removed whatever happens — never in the repository.
    import io, tempfile
    with tempfile.TemporaryDirectory(prefix="c2reel_") as tmp:
        stream = os.path.join(tmp, "frames.mjpeg")
        with open(stream, "wb") as fh:
            for nm, dur in seq:
                buf = io.BytesIO()
                Image.open(os.path.join(reel_dir, nm + ".png")).convert("RGB").save(buf, "JPEG", quality=92)
                fh.write(buf.getvalue() * int(round(dur * fps)))
        cmd = [ff, "-y", "-loglevel", "error", "-f", "image2pipe", "-c:v", "mjpeg", "-r", str(fps), "-i", stream,
               "-pix_fmt", "yuv420p", *codec, "-r", str(fps), out]
        subprocess.run(cmd, check=True)
    total = sum(d for _, d in seq)
    print(f"motion reference written: {out} ({total:.1f} s, {os.path.getsize(out)//1024} KB)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html-only", action="store_true")
    ap.add_argument("--only", default="")
    ap.add_argument("--motion", action="store_true", help="also build the C2 Reel pacing reference from the rendered frames")
    ap.add_argument("--motion-only", action="store_true", help="skip rendering; rebuild the motion reference from existing PNGs")
    a = ap.parse_args()
    if a.motion_only:
        build_motion(None); return
    chrome = None if a.html_only else find_chrome()
    if not a.html_only and not chrome:
        sys.exit("No Chrome/Chromium found. Set CHROME=/path/to/chrome or use --html-only.")
    n = 0
    for name, size, html in FRAMES:
        if a.only and not name.startswith(a.only):
            continue
        out = render(name, size, html, chrome, a.html_only)
        n += 1
        print(f"  {name:48s} {size:5s} {'html' if a.html_only else os.path.relpath(out)}")
    print(f"{n} frame(s) {'written' if a.html_only else 'rendered'}")
    if a.motion and not a.html_only:
        build_motion(chrome)

if __name__ == "__main__":
    main()
