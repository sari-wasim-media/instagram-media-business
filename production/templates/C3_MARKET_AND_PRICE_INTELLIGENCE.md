# C3 — Market & Price Intelligence · house template

**Engine definition (locked):** original charts and data cards in a consistent visual system — resale price
movement, retail-vs-resale spreads, brand share shifts, which releases trade below retail. Static and carousel
primary, animated-chart Reel secondary. Most research-heavy (~90 min/piece). Key metrics: saves ÷ reach,
profile visits ÷ reach. **Data sourcing rule: manual collection from public pages and published reports;
check terms of service before any collection; no scraper during the experiment.**

**Template status: ACTIVE — delegated production decision (2026-09-08).** Specimens: `renders/c3/`.

C3 carries 21 posts: 12 Reels, 6 Carousels, 3 Statics (A: 6R/3C/1S · B: 6R/3C/2S). Its visuals are
self-generated, so its rights burden is **zero**; its constraints are research time and the terms of the
sources it reads. Under the founders' conservative data-source posture (2026-09-08) the sources are
**published reports and brand release notes only** — live marketplace data is excluded
(`../assets/C3_DATA_SOURCE_TOS_REGISTER.md`). The template is built so every C3 piece can be made from those.

| Chart type | Compliant basis |
|---|---|
| MOVE | A report's price series, or a brand's own price history across its release notes |
| SPREAD | Release-note retail against report-stated resale |
| BELOW RETAIL | Only where a published report states the figures |
| SHARE | Report data (brand share, top sellers) |

---

## 1. Chart grammar — four fixed chart types

| Type | Question it answers | Encoding | Formats |
|---|---|---|---|
| **MOVE** | How has one price moved over time? | Line + 12 % area fill in the C3 accent, dashed grid, start and end value labels, end dot, month axis, headline `+14 %` in the semantic colour | Static · carousel slide · Reel (the line draws over 3.0 s) |
| **SPREAD** | Retail vs resale, item by item | Dumbbell per row: grey retail dot → resale dot in green (above retail) or red (below), % delta at the end | Static · carousel · Reel (rows appear one per 2.5 s beat) |
| **BELOW RETAIL** | Which pairs trade under list price right now | The SPREAD rows filtered to red | Static · carousel |
| **SHARE** | How is the market splitting? | Ranked horizontal bars in accent, muted bars for the rest, % labels | Static · carousel |

Never: pie charts, 3-D, dual axes, truncated axes without a break mark, gradients, more than one accent per
chart. Every chart carries on the frame: the metric definition, the size band, the window, the source
class, and **"Data as of <date>"**. Every number a reader could quote is a factual claim and lives in the
tracking row with its source.

## 2. The piece, as data

| Field | Rule |
|---|---|
| `question` | One sentence the piece answers ("Is resale on X still above retail?") |
| `chart_type` | MOVE / SPREAD / BELOW RETAIL / SHARE |
| `metric` | Exactly what was measured: "median last sale", "list price", "share of top-50 sellers" |
| `basis` | Size band, window, currency, what was excluded |
| `data[]` | The points, each with source, URL or report reference, date collected, collector's initials |
| `headline_number` | The one figure that leads the frame, with its sign and direction |
| `takeaway` | One sentence, plain, not advice |
| `sources[]` | Named; terms checked and recorded in the ToS register |
| `caveats` | Snapshot, sample size, anything a fair reader should know |

**Manual collection means:** a founder opens the published report or release note, reads the figure, types
it into the data sheet with the publisher, title and date. No browser extension, no export, no script, no
bulk download. **If a source's terms do not clearly permit the use, it is not a source** — regardless of how
public the page looks (founder posture, 2026-09-08).

## 3. Static — the data card

Ink. Kicker (what and window) · headline number (Bebas 260, semantic colour) beside a direction chip ·
title (Bebas 88, two lines) · the chart · data foot (mono 26: metric, basis, "Data as of", "Chart is
self-generated"). Asset count: **0 images; 1 dataset.** Specimens: `c3_static_move.png`, `c3_static_spread.png`.

## 4. Carousel — 5 slides

| Slide | Content |
|---|---|
| 1 | Hook: the headline finding as a claim ("Resale is up 14 %. Here is what moved") |
| 2 | The chart (MOVE or SPREAD) with the headline number |
| 3 | The breakdown: rows with per-item change, coloured by direction |
| 4 | The second view (BELOW RETAIL or SHARE) — the actionable cut |
| 5 | Method & sources: DATA · SIZES · WINDOW · METHOD rows + "Numbers are snapshots, not advice" |

Slide 5 is not optional. It is where the content-quality minimum ("every factual claim verified against a
named source") becomes visible to the audience, and it is the slide that earns the save.

## 5. Reel — ~30 s animated chart

| Beat | Frame | Duration |
|---|---|---|
| 1 | Hook: the headline number as the whole frame | 3.0 s |
| 2 | The chart draws left → right (MOVE) or row by row (SPREAD), then holds with the headline number | 3.0 + 2.0 s |
| 3–5 | Three data points, one per beat, each a three-line Bebas headline + one chip | 3 × 2.5 s = 7.5 s |
| 6 | Takeaway + the data foot on screen | 4.0 s |
| 7 | End card | 1.5 s |

Total **21 s**; hold the chart 4 s and run four data points for **26–30 s**. The chart draw is the only
animation beyond text entry. No voiceover; text-on-screen carries the whole argument; the caption repeats
the numbers and the method line.

## 6. Copy rules

- Headlines are findings, not questions: "Four of five trade below retail."
- Every percentage carries a direction sign and the absolute values that produced it ("↑ $212 → $242").
- "Median last sale" not "price"; "list price" not "retail" when the retailer discounts.
- The word **snapshot** appears on every piece. The phrase "not advice" appears in the caption of every piece.
- No predictions. C3 reports what moved; the desk's opinion lives in C1 and C4.

## 7. Research and data discipline

- One data sheet per piece (a tab in the founders' working spreadsheet, not the repository): source · URL or
  report · figure · date · collector. The tracking row links to it by name.
- Allowed sources — the founders' conservative data-source posture (2026-09-08), operationalised in
  `../assets/C3_DATA_SOURCE_TOS_REGISTER.md`: **(1) brand press releases and newsroom release notes** and
  **(2) published market reports and data press releases**. Nothing else. Brand and retailer product pages
  confirm a release-note price but are not cited; **live marketplace pages (StockX, GOAT, Flight Club, Stadium
  Goods, eBay, Grailed, KLEKT, Laced) are not used**, manually or otherwise, because their terms do not
  clearly permit it. A figure that exists only in an excluded source is not used; the piece is written
  without it or the subject changes.
- Sample honesty: state the size band and window; if fewer than 5 sales underlie a median, say so or do not
  publish the number.
- Collect in one sitting per piece and date-stamp the sheet; a piece is not re-collected after check-out.

## 8. Asset count and declared time budgets (Sourcing Gate item 1)

| Format | Rights-clean images | Datasets | Declared budget |
|---|---|---|---|
| Static | 0 | 1 (5–12 points) | 90 min: research 50 · chart 20 · copy, caption, QA 20 |
| Carousel | 0 | 1–2 | 110 min: research 60 · charts 30 · copy and QA 20 |
| Reel | 0 | 1 | 120 min: research 50 · chart and draw 40 · assembly and QA 30 |

C3 never touches the image-rights bank. Its Sourcing Gate item is **item 6, the ToS check**, plus the time
budget above, which replaces the historical ~90 min estimate once measured.

## 9. Caption template

```
<headline finding as one sentence>
<metric>, <basis>, <window>. Data as of <date>.
<takeaway sentence>. Snapshot, not advice.
Source: <named source(s)>.
#<model or brand tag> #sneakerresale #sneakermarket
```
