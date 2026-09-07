# House System v1 — the visual and motion language for all 84 posts

**Status: PROPOSED TEMPLATE-LOCK VALUES — founder review required before Day 1.** House templates are a
held-fixed production variable (`LOCK_SPECIFICATION.md` §1 item 17), so once the founders confirm this system
it is frozen for the six posting weeks. Nothing here changes the matrix, the methodology or any locked decision.

**One system, both accounts.** `ANTI_DUPLICATION_AND_TOPIC_SELECTION.md` §4 *requires* the identical house
template, palette and typography on both accounts. The only variable that differs between accounts is the
handle in the top band. Everything else is constant, because the experiment measures accounts, engines and
formats — not two art directions.

Files in this directory: `tokens.json` (the numbers) · `house.css` (the same numbers as a stylesheet, used by
the specimen renderer) · `fonts/` (vendored under the SIL Open Font License). Specimens of every frame type:
`../templates/renders/`.

---

## 1. Five principles

1. **A desk, not a persona.** The accounts speak as an editorial desk: Release Desk, Rankings, Market Desk,
   Commentary. No face, no first-person "I", no founder name. Authority comes from the format, the sources
   and the consistency.
2. **Paper for photographs, Ink for words.** Product images sit on a white plate on a warm paper ground;
   hooks, verdicts, summaries, data and commentary sit on near-black ink. This gives every carousel and Reel a
   built-in rhythm (ink → paper → ink) and, practically, lets product images that arrive on white be placed
   without cut-outs.
3. **One accent per engine, nothing else coloured.** Blue for C1, yellow for C2, green for C3, pink for C4.
   Semantic green/amber/red is reserved for verdicts and price direction. Product photography supplies all
   other colour.
4. **Data is typeset, not decorated.** Prices, dates, sizes and sources are set in the mono face, tabular,
   with the source and "data as of" date on the frame. No 3-D, no gradients on charts, no icons for their own sake.
5. **Cuts, not effects.** Reels are cut-based text-on-screen over still frames. No dissolves over 200 ms, no
   generative motion, no voiceover, no AI voice. Motion is timing.

---

## 2. Canvases and safe zones

| Use | Canvas | Ratio | Notes |
|---|---|---|---|
| Feed static, carousel slide | **1080 × 1350** | 4:5 | The largest feed footprint. Keep essential content inside y = 135…1215 (the 1:1 crop) |
| Reel | **1080 × 1920** | 9:16 | 30 fps. UI safe zones: top 250 px, bottom 420 px, right 130 px, left 60 px |
| Reel cover | the hook frame | — | The profile grid shows a 4:5 crop of the cover: keep the cover title inside y = 285…1635 |
| Story | **1080 × 1920** | 9:16 | Safe zones: top 250 px, bottom 260 px, sides 60 px. One frame per day |

Two ruler frames show these zones: `../templates/renders/diagnostics/`.

---

## 3. Colour

| Token | Hex | Role |
|---|---|---|
| `ink` | `#0F1013` | Ground for hook, verdict, summary, data and commentary frames; Reel and Story ground |
| `ink-2` / `ink-3` | `#1B1C21` / `#2A2B33` | Raised surfaces, rules, chart grid on ink |
| `paper` | `#F3EFE6` | Ground for frames that carry a photograph |
| `paper-2` | `#E6E1D6` | Rules and plate borders on paper |
| `white` | `#FFFFFF` | The image plate |
| text on ink | `#F3EFE6` / `#9A9AA3` | Primary / secondary |
| text on paper | `#0F1013` / `#5E5E66` | Primary / secondary |
| **C1 accent** | `#3D7BFF` | Release Desk blue |
| **C2 accent** | `#FFD23F` | Rankings yellow |
| **C3 accent** | `#21D07A` | Market green |
| **C4 accent** | `#FF3E9B` | Commentary pink |
| `up` / `cop` | `#21D07A` | Price up, verdict COP |
| `hold` / `wait` | `#FFB020` | Verdict WAIT |
| `down` / `pass` | `#FF3B30` | Price down, verdict PASS |

Contrast: every text/ground pair above clears 7:1 except secondary-on-ink (≈5.5:1), which is used only at
≥ 26 px. The C2 yellow and the semantic amber are deliberately different hues so a WAIT stamp never reads as
a Rankings element.

---

## 4. Typography

| Role | Face | Licence | Use |
|---|---|---|---|
| Display | **Bebas Neue** | SIL OFL 1.1 | Hooks, titles, item names, rank numbers, stamps. **Caps only.** |
| Body | **Inter** (variable) | SIL OFL 1.1 | Reasons, subtitles, body copy. Sentence case. Weights 400–700 |
| Mono | **IBM Plex Mono** | SIL OFL 1.1 | Kickers, prices, dates, sizes, chips, source lines, counters, handles |

Scale on a 1080-wide canvas (px): display 240 / 168 / 120 / 88 / 64 · body 44 / 36 / 30 / 26 · mono 34 / 30 / 26.
Line height: display 0.92 · body 1.25 · mono 1.3. Mono kickers are caps with 0.12 em tracking.

Rules: nothing below **24 px**; hooks ≤ 4 lines and ≤ 5 words per line; a reason line is one sentence,
≤ 60 characters; numbers are always mono and tabular; never letter-space Bebas beyond 0.02 em; never fake-bold.

All three faces are free on Google Fonts and available inside Canva and Figma, so the founders can rebuild the
templates in either tool without licensing work. The vendored files in `fonts/` carry their `OFL.txt`.

---

## 5. Grid and bands — the constants on every frame

- **Outer margin 72 px, gutter 24 px, base unit 8 px.** Cards radius 24 px, pills fully round, rules 4 px.
- **Top band (96 px):** left, the engine label in mono caps with a 18 px accent square — `RELEASE DESK` ·
  `RANKINGS` · `MARKET DESK` · `COMMENTARY` (Stories: `STORY · <weekday> · <class>`); right, the account
  handle. On Reels and Stories the band sits below the 250 px safe zone.
- **Bottom band (72 px):** left, the source line or ranking basis in mono; right, the slide counter
  (`3/9`), `STATIC`, or the beat note on Reel storyboards. On Reels the band sits above the 420 px caption zone.
- **Specimen tag.** Every frame in `renders/` carries a red `SPECIMEN · PLACEHOLDER FACTS` tag. Production
  frames do not.

---

## 6. Components

| Component | Where | Spec |
|---|---|---|
| **Kicker** | every frame | Mono 30 px caps, accent colour. Names the frame's job: "Verdict · drops Saturday", "The list" |
| **Hook** | slide 1 / beat 1 | Bebas 168 px (200 px on Reels), ≤ 4 lines, ink ground, accent arrow bottom-right on carousels |
| **Plate** | any frame with a photograph | White, 2 px paper-2 border, radius 24, padding 32/40/60. Product centred, `object-fit: contain`. No shadow, no filter, no background removal required |
| **Rank** | C2 item slides | Bebas 240 px in accent, with a 64 px `/7` at 55 % opacity |
| **Chip** | data | Mono 30 px in a 2 px pill; solid accent variant for emphasis; semantic colour for up/down |
| **Rows** | summaries, dockets, breakdowns | Mono number column (92 px) + Bebas 72 px title + mono value; 1 px rules |
| **Stamp** | C1 | Bebas 168 px, 10 px border, radius 16, rotated −6°. COP green · WAIT amber · PASS red |
| **Facts grid** | C1 | 2 columns; mono 24 px key, Bebas 72 px value (mono 44 px for prices and sizes) |
| **Chart** | C3 | Inline SVG. Grid dashed ink-3, line 8 px accent, area 12 % accent, end dot with value label, months on the axis. Dumbbell for retail-vs-resale (grey retail dot → green/red resale dot) |
| **Receipt / Chat / Ticket / Split** | C4 | Original, house-drawn UI. Never a screenshot of any real app, receipt or ticket |
| **Sticker zone** | Story, Wednesday | Dashed accent box marking where the one interactive sticker is placed in-app |
| **Mosaic** | Story, Sunday | Own artwork thumbnails only — no post links, no stickers |

There is deliberately **no AI-disclosure component**: the six AI-treated posts are disclosed in the fixed
caption line and by the platform's AI label, never on the artwork, so their frames are visually identical to
the other C4 frames.

---

## 7. Imagery treatment

- Every photograph sits on a plate. Side profile, toe pointing the same direction on every item in a piece,
  product filling 80–90 % of the plate width.
- Permitted adjustments: crop, exposure, white balance, sharpening. **Not permitted:** generative fill or
  expand, background replacement by a generative tool, style filters, adding or removing objects.
- Product images never carry the accent colour; the accent lives in type and rules only.
- Every image carries a provenance ID in the tracking row (`../assets/ASSET_PIPELINE.md`). No ID, no publish.
- In the six AI slots the plate holds an AI-generated **illustration** that depicts no real product, no brand
  mark and no real person. Everything else about the frame is identical to a non-AI C4 frame; disclosure is
  in the caption and the platform label only.

---

## 8. Motion — the Reel grammar

| Beat | Duration | Rule |
|---|---|---|
| Hook | 3.0 s | The hook frame; also the cover |
| Item / fact / data beat | 4.0 s (C2) · 2.0 s per fact (C1) · 2.5 s (C3 data points, C4 say/think pairs) | Text is fully legible for ≥ 2.5 s |
| Rank reveal | 0.4 s number-only frame before each C2 item | The "stamp" rhythm |
| Stamp reveal (C1) | 3.0 s | Stamp scales 1.15 → 1.0 over 150 ms, then holds |
| Chart draw (C3) | 3.0 s draw + 2.0 s hold | Line draws left to right |
| Summary | 4.0 s | The list / the docket / the takeaway |
| End card | 1.5 s | "Next week" — no call to action, no ask |

Hard rules: cuts only; text enters with a 120 ms slide-up, nothing else animates; **20–59 s, target 30–45 s,
never over 90 s** (locked); the hook frame is the cover; key claims that appear on screen also appear in the
caption; no on-screen asks for likes, follows, saves or comments.

Reference pacing: `../templates/renders/c2/C2_REEL_pacing_reference_36s.*` — hook 3.0 + 7 × (0.4 + 3.6) +
summary 4.0 + end 1.5 = **36.5 s**.

---

## 9. Audio

No voiceover and no AI voice (locked). Music comes only from the **Instagram in-app royalty-free library
(Meta Sound Collection)**, chosen at upload, because it is the one library Meta states is cleared for
business accounts and commercial use — the licensed "popular music" library is not available to business
accounts, and CapCut's "commercial" sounds are cleared only for CapCut and TikTok. Every track is logged in
`../assets/audio_ledger.csv`. Never the same track on both accounts within 14 days; never reused on one account
within 14 days. Keep ≥ 24 distinct tracks in rotation. Full research: `../assets/SOURCING_ROUTES_RESEARCH.md`.

---

## 10. Accessibility and legibility

Alt text on every image and slide (one sentence, descriptive, no hashtags). Nothing below 24 px. Text-on-screen
holds ≥ 2.5 s. Every number on a frame has a source and a date on the same frame or in the caption. Colour is
never the only carrier of meaning: an up/down chip always carries an arrow and a sign.

---

## 11. What is fixed and what is free

**Fixed for all 84 posts and 84 Stories:** canvases · bands · palette · faces and scale · plate treatment ·
component set · beat durations · Reel duration band · audio source rule · alt-text rule · the C2 ranked-item
count (see `../templates/C2_RANKED_ITEM_COUNT_DECISION.md`) · the Story frame.

**Free at production (late-bound by rule):** the subject · the copy · the photographs · the chart data ·
the verdict · which named C4 format is used · the specific royalty-free track.

---

## 12. Rebuilding the templates in your own tool

The specs in `../templates/` give sizes in pixels on the canvases above. Load Bebas Neue, Inter and IBM Plex
Mono from Google Fonts (all three exist in Canva's and Figma's font pickers). Build one master per frame type,
duplicate per piece. Or edit `../templates/src/render_frames.py` and render frames directly with a headless
Chrome — see `../templates/README.md`.
