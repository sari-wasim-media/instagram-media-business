# House templates — C1 · C2 · C3 · C4 · Story

**Status: ACTIVE — delegated production decisions (2026-09-08).** House System v1, the C2 ranked-item count
of 7, the C1 verdict scale, the Story rotation with the Wednesday sticker and the AI disclosure line are
decided under the founders' delegated production authority and are frozen for the six posting weeks; the
founders may override any of them before Day 1. Nothing here alters the matrix or the methodology.

| File | What it is |
|---|---|
| `C1_RELEASE_VERDICT_DESK.md` | Verdict card, Reel, carousel; the COP / WAIT / PASS rubric; the research sheet; the ladder applied |
| `C2_RANKINGS_AND_TIER_LISTS.md` | The ranking carousel, Reel and static; copy and imagery rules; anti-duplication handling |
| `C2_RANKED_ITEM_COUNT_DECISION.md` | The decided value (7) with the full comparison that produced it |
| `C3_MARKET_AND_PRICE_INTELLIGENCE.md` | Four chart types, the data card, carousel, animated-chart Reel, research discipline |
| `C4_ORIGINAL_MEME_AND_COMMENTARY.md` | Seven named originated formats; the AI-slot treatment |
| `STORY_TEMPLATE_AND_ROTATION.md` | The Story frame, the proposed 7-day rotation, the proposed sticker weekday |
| `template_constants.json` | The numbers the validators read (item count, bands, slots) |
| `src/render_frames.py` | Generates every specimen frame (HTML → PNG) and the C2 Reel pacing reference |
| `src/html/` | The generated HTML for each frame — open any file in a browser |
| `renders/` | 64 specimen PNGs by engine, the two safe-zone rulers, and `c2/C2_REEL_pacing_reference_36s.webm` |

Every specimen carries a red **SPECIMEN · PLACEHOLDER FACTS** tag and uses fictional products, prices and
data. None of them is publishable. The generic sneaker silhouette is a stand-in for the rights-cleared image.

---

## Asset counts — Sourcing Gate item 1, measured from the templates

"Templates built and measured first: the number of distinct assets each consumes is recorded." Counts are
distinct rights-clean **photographic** images per piece; charts, typography, house UI and illustrations are
self-generated and rights-free by construction.

| Engine | Static | Carousel | Reel | Per-piece rule | 21-post total | Week-1 pieces | Reserve pieces | Gate bank |
|---|---|---|---|---|---|---|---|---|
| C1 | 0–1 | 0–1 (docket 0–3) | 0–1 (docket 0–3) | Image is optional; the no-image layout is first-class | 0 required, ≤ ~30 optional | 3 (0–3) | 0 (no C1 reserve) | 0–3 |
| **C2** | **7** | **7** | **7** | Exactly the ranked-item count, every format | **147** | 4 → **28** | 2 → **14** | **42** |
| C3 | 0 | 0 | 0 | Self-generated charts; 1 dataset per piece | 0 | 3 → 0 | 3 → 0 | 0 |
| C4 | 0–2 | 0–2 | 0–2 | Three of seven formats need no imagery | ≈ 20–30, of which 8–12 AI illustrations in the six slots | 4 → ≈ 4–8 | 2 → ≈ 2–4 | ≈ 6–12 |
| Story | 0–2 | — | — | Owned / self-drawn only; no AI | ≈ 12 (Saturday frames) | 14 → ≈ 2 | — | — |
| AI route test | — | — | — | One non-matrix C4 piece | 1–2 AI illustrations | — | — | 1–2 |

**The Sourcing Gate bank therefore needs roughly 50–60 provenance-recorded assets, of which 42 are C2
product images.** C2 remains the whole problem, exactly as `GATES.md` says; C1 was designed so imagery can
never block it, and C3 needs none.

Reserve composition assumed above: 3 Reels (C2, C3, C4) + 3 Carousels (C2, C3, C4) + 1 Static (C3) — see
`../operations/RESERVE_REGISTER.md`. Week-1 slots from the matrix: C1 ×3 (A CAR, A STA, B REE), C2 ×4
(A REE ×2, B CAR, B REE), C3 ×3 (A CAR, B REE, B STA), C4 ×4 (A REE ×2, B CAR, B REE).

## Declared time budgets (to be replaced by measured times)

| Engine | Static | Carousel | Reel |
|---|---|---|---|
| C1 | 55 min | 65 min | 80 min |
| C2 | 80 min | 90 min | 115 min |
| C3 | 90 min | 110 min | 120 min |
| C4 | 45 min | 60 min | 70 min (+ 30 min in AI slots) |

A Week-1 production of 11 non-C1 pieces + 7 reserve pieces + 14 Stories sums to roughly 26–30 hours by these
budgets, before the C1 pieces on the ladder. This is consistent with the ≈ 23 h/week estimate in `GATES.md`
§3 spread over the two pre-launch production weeks.

## Rendering the specimens yourself

```
python3 production/templates/src/render_frames.py            # HTML + PNG for all 64 frames
python3 production/templates/src/render_frames.py --html-only # no browser needed
python3 production/templates/src/render_frames.py --motion    # also rebuild the C2 Reel pacing reference
```

Needs a Chromium: the script finds Playwright's `headless_shell` (exact viewport) or any Chrome (it then
compensates for new-headless's hidden 87 px toolbar; set `CHROME_VIEWPORT_OFFSET` if your build differs).
The motion reference needs `ffmpeg` and Pillow. This is a local production aid, not automation.
