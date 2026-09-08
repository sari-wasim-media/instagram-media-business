# C1 — Release & Verdict Desk · house template

**Engine definition (locked):** original graphics and short Reels reacting to actual releases within 24–48 h
of news breaking — price and sizing breakdowns in the house layout, ranked "this week's drops", "worth it /
wait for the sale" verdicts. Reel primary, static secondary, carousel occasional. Key metrics: non-follower
reach share, comments ÷ reach. Production target ~40 min per piece once templated.

**Template status: ACTIVE — delegated production decision (2026-09-08).** The verdict scale and rubric in
§1 are decided under that authority; the founders' brand-posture decision names COP / WAIT / PASS as usable
where Claude concludes it is the strongest implementation, and it is. Specimens: `renders/c1/`.

C1 carries 21 posts: 12 Reels, 6 Carousels, 3 Statics (A: 6R/3C/2S · B: 6R/3C/1S). Every C1 slot runs the
locked deadline ladder — topic lock T−48 h, production complete T−24 h, scheduled T−12 h — so the template's
first job is to be **producible in under an hour from a filled research sheet**, and its second job is to be
**never blocked by imagery**.

---

## 1. The two design decisions that make C1 fast and safe

**Imagery is a slot, not a requirement.** A C1 piece is a data-and-verdict object. The product plate is
present when a rights-clean image exists (owned photograph, licensed stock, a brand asset whose terms were
verified and logged — see `../assets/SOURCE_CLASS_DECISION.md`) and **absent otherwise**; the no-image
variant is a first-class layout (`renders/c1/c1_static_verdict_card_no_image.png`), not a degraded one.
Research found that most brand newsrooms do **not** grant social-media use of press imagery, so the desk
cannot depend on it. A release post without the shoe still carries the facts the audience is deciding on.

**The verdict is a fixed three-value scale with a rubric.** COP · WAIT · PASS, scored on four criteria so two
founders produce the same verdict from the same facts and so the piece can be written at T−36 h without
deliberation.

| Criterion (0–2 each) | 0 | 1 | 2 |
|---|---|---|---|
| Value at retail | Overpriced for materials and make | Fair | Under-priced for what it is |
| Wearability | Costume | Rotation piece | Daily driver |
| Availability | Raffle-only, tiny run | Limited but gettable | General release / restocks |
| Resale outlook (from C3 data or the last comparable release) | Below retail expected | Around retail | Above retail expected |

Total **6–8 → COP** · **3–5 → WAIT** (wait for the sale, the restock or the resale dip) · **0–2 → PASS**. The
score is recorded in the tracking row. A founder may override the arithmetic by one step with a one-line
reason in the row; never by two. **When no compliant resale data exists for the comparable** (the usual case
under the conservative data-source posture), score resale outlook **1** and write "no published resale data"
in the row — the verdict then rests on the three criteria the desk can verify.

## 2. The piece, as data — the research sheet

Filled at topic lock (T−48 h) from the sources named in the row; every field below is a factual claim and is
verified against a named source before production completes (T−24 h).

| Field | Rule |
|---|---|
| `product` | Model + ‘colorway’ as the brand writes it |
| `release_date` | Confirmed date (and local time if published). Rumoured dates are not eligible — the queue orders on confirmed dates |
| `retail` | Adult list price; grade-school / kids tiers if published |
| `sizes` | Published run |
| `where` | Retailer / app / raffle / in-store, as published |
| `materials` | Two facts from the product page |
| `comparable` | Last comparable release and what it did at resale (C3 rules apply to any number) |
| `verdict` | COP / WAIT / PASS with the four scores |
| `reasons[3]` | One sentence each, ≤ 60 characters |
| `sources[]` | Brand release note / product page / retailer listing, with date accessed |
| `asset_id` (optional) | Provenance record for the product image, if any |

Source checklist for the row (conservative data-source posture, 2026-09-08 —
`../assets/C3_DATA_SOURCE_TOS_REGISTER.md`): the brand's release note or press release for name, date, price,
sizes, materials and where sold; the seller's own public announcement for raffle mechanics; a product page
only to confirm that the release-note price still stands; published reports for resale comparables. Never a
marketplace listing, never a rumour account, never another account's post as a source (a lead at most).

## 3. Static — the verdict card

Paper (with image) or ink (without). Kicker `VERDICT · DROPS <weekday>` · title (Bebas 104 / 136) · plate
936 × 400 when present · facts grid (RELEASE · RETAIL · SIZES · WHERE) beside the stamp (Bebas 140–168,
rotated −6°, semantic colour) · one reason line · bottom band `Source: <source> <date> · verified in tracking
row`. Asset count: **0–1**.

## 4. Reel — ~30 s single-release verdict (primary)

| Beat | Frame | Duration |
|---|---|---|
| 1 | Hook (ink): "<product> drops <weekday>" + "Cop, wait, or pass? 30 seconds." Plate 936 × 430 if an image exists; otherwise the hook fills the frame. Cover frame | 3.0 s |
| 2 | Facts block: the four facts, revealed one at a time | 8.0 s (2.0 s each) |
| 3 | Verdict: stamp reveal (scale 1.15 → 1.0 in 150 ms), one-line ruling | 3.0 s |
| 4–6 | Reasons, one per beat, Bebas 136 three-line headline + one sentence | 3 × 2.5 s = 7.5 s |
| 7 | Docket (summary rows: WHEN · COST · HOW · CALL) | 4.0 s |
| 8 | End card: "Next drop, same desk" | 1.5 s |

Total **27.0 s**; extend beat 2 to 10 s (2.5 s per fact) when the facts need it → **29–30 s**. Never pad past
45 s. Asset count: **0–1** (the same image reused across beats within the piece is one asset).

**Weekly docket variant** ("this week's drops, ranked"): hook · three releases, each facts (4 s) + stamp (2 s)
· docket ranking the three · end card ≈ 3 + 18 + 4 + 1.5 = **26.5 s**; stretch facts to 5 s for 29.5 s. Asset
count **0–3**. Use when the queue delivers a multi-release week; the three releases are one check-out
("the week of <date>") and each release is logged as a secondary subject for the anti-duplication checks.

## 5. Carousel — 6 slides

| Slide | Ground | Content |
|---|---|---|
| 1 | Ink | Hook: product, drop day, "verdict inside" |
| 2 | Paper | The pair: plate 936 × 700 (or the facts block if no image), two materials facts |
| 3 | Ink | The facts grid, up to six facts (adds grade-school price, restock status) |
| 4 | Ink | The verdict stamp, large, one-line ruling |
| 5 | Ink | Three reasons as rows + the rubric line ("value 2 · wearability 2 · availability 1 · resale 2 → 7/8") |
| 6 | Ink | Docket: WHEN · COST · HOW · CALL |

Weekly docket variant: hook · 3 × (facts + stamp) · ranked docket = 8 slides. Asset count **0–1** (or 0–3).

## 6. Copy rules

- Hooks state the product and the day; verdict Reels promise the verdict, never tease it ("you won't believe").
- Facts are typeset, not narrated: numbers in mono, dates as `Sat 14 Sep`, prices as `$185`, sizes as `US 7–14`.
- Reasons are the desk's opinion, one sentence, no hedging words ("might", "maybe").
- Rulings: "Buy at retail. Do not pay resale." / "Wait for the restock." / "Pass. The 2024 pair is the same shoe."
- No retailer links, no "link in bio" (locked: no link in bio), no affiliate language, no raffle codes.
- Caption repeats the four facts and the verdict in text, then the source line and 3–5 tags.

## 7. The ladder, applied to the template

| Deadline | Template step | Time |
|---|---|---|
| T−48 h | Topic lock from the queue; research sheet filled; sources logged | 20 min |
| T−36 h | Facts verified against sources; rubric scored; reasons written; image sourced or the no-image variant chosen | 20 min |
| T−28 h | Layout in the template (static 10 min · carousel 20 min · Reel 30 min) | 10–30 min |
| T−24 h | **Production complete**: QA against the content-quality minimum; caption, alt text, tags | 10 min |
| T−12 h | **Scheduled** at 16:00 UTC; screenshot of the scheduled state in the row | 5 min |

Declared per-piece budgets: **static 55 min · carousel 65 min · Reel 80 min**, to be replaced by measured
times after the first three C1 pieces. If a slot cannot meet T−24 h it becomes a Miss and recovers by the
exception protocol; it is never converted into an evergreen piece.

## 8. Asset count (Sourcing Gate item 1)

| Format | Distinct rights-clean images | Notes |
|---|---|---|
| Static | 0–1 | Optional plate |
| Reel | 0–1 (docket variant 0–3) | One image reused across beats counts once |
| Carousel | 0–1 (docket variant 0–3) | |

Whole experiment: **0 required, ≤ ~30 optional** across 21 posts. C1 never fails the Sourcing Gate on
imagery; it can only fail on research time, which the ladder budgets.

## 9. Caption template

```
<product> ‘<colorway>’ drops <weekday> <date>.
Retail $<price> · sizes <run> · <where>.
Verdict: <COP/WAIT/PASS> — <ruling sentence>.
Source: <brand release note / product page>, <date accessed>.
#<model tag> #<brand tag> #sneakerrelease
```
