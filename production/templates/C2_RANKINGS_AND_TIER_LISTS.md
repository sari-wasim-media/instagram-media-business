# C2 — Rankings & Tier Lists · house template

**Engine definition (locked):** original ranked carousels in a fixed house layout — slide 1 hook, one item per
slide, summary slide. Carousel primary, Reel secondary. Distribution thesis: saves and repeat views. Key
metrics: saves ÷ reach, profile visits ÷ reach. Binding constraint: imagery rights.

**Template status: ACTIVE — delegated production decision (2026-09-08).** Ranked-item count: **7**
(`C2_RANKED_ITEM_COUNT_DECISION.md`). Product photographs of branded sneakers are produced under
the accepted trademark posture and its §5 operating rule (`../TRADEMARK_RISK_REVIEW.md`). Specimens: `renders/c2/`.

C2 carries 21 posts: 12 Reels, 6 Carousels, 3 Statics. Per account: 6 Reels, 3 Carousels; A holds 2 Statics,
B holds 1. Every one of them ranks exactly 7 items and consumes exactly 7 rights-clean images.

---

## 1. The piece, as data

Every C2 piece is fully described by this record. Fill it in the tracking row before layout starts.

| Field | Rule |
|---|---|
| `title` | The hook. Formula: "7 [things] that/under/for [claim]" or "[Set] ranked by [criterion]". ≤ 9 words |
| `running_head` | ≤ 28 characters; appears on every item slide |
| `variant` | `RANKED` (1–7) or `TIER` (7 items in ≤ 4 tiers S/A/B/C) |
| `ranked_by` | The criterion in ≤ 8 words **plus** the data basis and date when a number is involved ("resale median, US 8–11, Aug 2026") |
| `items[7]` | For each: `rank` or `tier` · `name` (model, ≤ 3 words) · `colorway` (≤ 3 words, in quotes) · `reason` (one sentence, ≤ 60 characters) · `chip` (optional: retail / resale / year; only if verified) · `asset_id` (provenance record) |
| `summary` | Generated from the items: rank · name ‘colorway’ · one value |
| `method` (optional) | Three tests in ≤ 8 words each; used only when the ranking basis needs it |
| `sources` | A named source per factual chip; none required for opinion-only lists |

Reasons are the voice of the desk: declarative, specific, one idea. "Wears with everything, still under
retail on resale." Not "Great shoe!" Opinion is allowed and expected — a ranking is an argument — but a
**number** on a chip is a factual claim and must be verified against the logged source.

---

## 2. Carousel (canonical) — 9 slides, optional 10th

| Slide | Ground | Content |
|---|---|---|
| 1 | Ink | Kicker `RANKINGS · 7 ITEMS · SWIPE` · hook (Bebas 168) · one-line subtitle stating the basis · accent arrow |
| 2 | Ink (optional) | `HOW WE RANKED` — three tests as rows. Use when `ranked_by` needs explaining; otherwise omit and renumber |
| 2–8 (or 3–9) | Paper | Item slides, **counting down 7 → 1**: rank (Bebas 240, accent) with `/7` · running head · plate 936 × 560 · name + ‘colorway’ (Bebas 104, colorway in secondary) · reason (Inter 38) · chip |
| 9 (or 10) | Ink | `THE LIST` — title (Bebas 120) · seven rows 1 → 7 with one value each. The save slide |

Bottom band: left `Ranked by: …` on every slide; right the counter `n/9`. The countdown order gives the
carousel a reason to be swiped to the end; the summary gives it a reason to be saved.

**Tier variant:** slide 1 hook states the tiers; item slides carry a tier badge (solid accent chip `S TIER`)
in place of the rank number, ordered S → C; the summary is the tier board (rows grouped under tier labels).

## 3. Reel — 36.5 s at house pacing

| Beat | Frame | Duration |
|---|---|---|
| 1 | Hook (ink, tall) — also the cover | 3.0 s |
| 2–15 | For each item 7 → 1: number-only frame (paper, Bebas 420) **0.4 s**, then the item card (paper: rank, running head, plate 936 × 500, name, reason, chip) **3.6 s** | 7 × 4.0 s = 28.0 s |
| 16 | Summary (ink) — the same seven rows | 4.0 s |
| 17 | End card — "Next week: another list, same rules" | 1.5 s |

Text enters with a 120 ms slide-up; every cut is hard. Audio from the Instagram royalty-free library, logged.
Total **36.5 s** — inside 30–45 s with margin. Cover = beat 1. Caption carries the full list in text.

The motion reference `renders/c2/C2_REEL_pacing_reference_36s.*` is this storyboard at these durations.

## 4. Static — hero + 6

Paper ground. Title (Bebas 96, two lines) · hero block: plate 420 × 300 for #1 beside rank `1/7`, name and
reason · a 3 × 2 grid of plates 300 × 200 for #2–#7 with rank and name under each. All 7 images present.
Bottom band carries `Ranked by`. The caption carries the list in text.

## 5. Copy rules

- The hook names the count and the promise. No question hooks ("Which is best?"), no clickbait gaps ("You
  won't believe #3").
- Reasons: one sentence, ≤ 60 characters, present tense, no exclamation marks, no emoji.
- Names are the model and colorway as the brand writes them; no nicknames unless in quotes.
- Chips are facts: retail = list price from the brand or retailer page on the date logged; resale = the C3
  rules (median last sale, size band, window, source). If a chip cannot be verified, drop the chip — never
  round a guess into a number.
- No sponsor, retailer or affiliate mention inside a list during the experiment.

## 6. Imagery rules

- **Seven rights-clean images per piece, one per item, never reused across pieces** (anti-duplication rule 4).
  Source classes and the route stack: `../assets/SOURCE_CLASS_DECISION.md` and `../assets/C2_SOURCING_ROUTES.md`.
- Side profile, same toe direction across the piece, product at 80–90 % of plate width, on the white plate.
- No brand-mark crops that make the logo the subject; the product is the subject.
- If an item's image cannot be sourced rights-clean, the **item changes**, not the rule. The fallback for a
  specific colorway is the self-generated illustration route (`C2_SOURCING_ROUTES.md` route S), which is always
  available. Credit is not permission: an image found online and credited is not rights-clean.
- Every image has a provenance record before layout; the asset ID goes in the filename and the tracking row.

## 7. Anti-duplication handling specific to C2 (operationalisation — ACTIVE, delegated production decision 2026-09-08)

- The **subject** checked out for a C2 piece is its theme (e.g. "under-$200 sneakers that look expensive").
  The **#1 item** is additionally logged as a secondary subject so the 14-day cross-account subject rule can be
  checked against it.
- Consecutive C2 pieces on one account use disjoint item sets (rule 12). Two lists may share a brand or
  silhouette family, never an item at colorway level within 10 days.
- Named pressure point: `A-W5-C2-REE-01` (Fri) → `A-W5-C2-REE-02` (Sat) — different theme, disjoint items,
  different images, different hooks, recorded in both tracking rows.

## 8. Asset count and declared time budgets (Sourcing Gate item 1)

| Format | Distinct rights-clean images | Self-generated elements | Declared budget (to be replaced by measured times) |
|---|---|---|---|
| Carousel | **7** | hook, optional method, summary | 90 min: sourcing 7 × 6 = 42 · ranking and reasons 15 · layout 18 · caption, alt text, QA 15 |
| Reel | **7** | hook, 7 number frames, summary, end card | 115 min: as carousel + 25 for assembly and timing |
| Static | **7** | title block | 80 min: sourcing 42 · ranking 15 · layout 10 · caption and QA 13 |

Whole experiment: 21 × 7 = **147 images**. Sourcing Gate bank (4 Week-1 pieces + 2 reserve pieces): **42**.
The two-piece sourcing stress test in `../assets/C2_SUSTAINABILITY_TEST.md` (protocol v2, 2026-09-13 — run
without founder-owned inventory) measures these budgets by stage; if either piece cannot be produced
rights-clean inside 1.5 × its budget, or C2 turns out to be illustration-led, the finding is escalated to
the founders — the count, the matrix and the originality rule do not move.

## 9. Caption template

```
<hook line, ≤ 100 characters>

1. <name> ‘<colorway>’ — <value>
2. …
7. …

Ranked by <criterion>. <Data basis and date, if any number appears.>
#<subject tag> #<subject tag> #<category tag>   (3–5 tags, see ../policy/CAPTION_AND_HASHTAG_POLICY.md)
```

Alt text (every slide): "Slide n of 9: <name> ‘<colorway>’ ranked number <rank> — <reason>."

## 10. QA before scheduling

Content-quality minimum (`GATES.md` §4) plus: exactly 7 items · 7 provenance IDs, none used before · countdown
order on item slides, ascending on the summary · every chip traceable · running head ≤ 28 characters · Reel
20–59 s (target 36.5 s) · cover = hook · caption list matches the slides · hashtags 3–5 and policy-clean ·
no CTA on artwork · pressure-point check if applicable. Full checklist: `../operations/PRE_PUBLISH_QA.md`.
