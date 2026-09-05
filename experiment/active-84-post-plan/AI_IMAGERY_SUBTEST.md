# AI-Imagery Sub-Test — FOUNDER-LOCKED

**Status: ACTIVE and LOCKED.** Approved jointly by Sari and Wasim as part of the Founder Lock.

The founders decided that AI-generated imagery is **not categorically prohibited** and that they want
evidence about it for the long-term business. This document is the complete, predeclared design that
delivers that evidence **without corrupting the primary 84-post experiment**.

---

## 1. Status of the sub-test

**A logged nested sub-test. NOT a formal secondary experimental factor.**

Making AI a real factor would require balancing it against account × engine × format × week, which at 84
posts fragments cells to n = 1–2 and destroys the primary design. As a nested, predeclared, counterbalanced
subset inside **one engine only**, it costs the primary design one engine's purity and nothing else.

**It is explicitly not statistically powered** (6 AI posts against 15 non-AI posts within C4). It may not
declare that AI imagery works or does not work. Its three deliverables are:

1. a **production-cost and rights-burden measurement**,
2. a **compliance observation** — platform labelling behaviour, Account Status, comment sentiment,
3. a **directional note** carrying no decision authority.

---

## 2. Confined to C4 — and why

This follows from the founders' safety requirement, not from convenience.

| Engine | AI imagery | Reason |
|---|---|---|
| C1 Release & Verdict | **PROHIBITED** | Content is about specific real releases with real prices and sizing. Generated imagery would misrepresent a real, specific product |
| C2 Rankings & Tier Lists | **PROHIBITED** | Ranks specific real products, one item per slide. Precisely the failure mode the founders named |
| C3 Market & Price Intelligence | **PROHIBITED** | Visuals sit adjacent to factual price, spread and availability claims |
| **C4 Original Meme & Commentary** | **PERMITTED — 6 slots** | Canonically "originated formats using owned or licensed imagery and original writing" — inherently stylized and non-documentary. The only engine where generated imagery is neither misleading nor factually load-bearing |

---

## 3. The six locked slots

**6 is the smallest subset that covers both accounts in all three formats exactly once.** Fewer drops a
format; 3 cannot split across two accounts.

| Slot ID | Account | Week | Weekday | Format | Block |
|---|---|---|---|---|---|
| `B-W2-C4-REE-01` | B | 2 | Mon | REEL | WARM |
| `A-W2-C4-CAR-01` | A | 2 | Wed | CARO | WARM |
| `B-W2-C4-STA-01` | B | 2 | Sun | STAT | WARM |
| `A-W4-C4-REE-01` | A | 4 | Tue | REEL | STEADY |
| `B-W5-C4-CAR-01` | B | 5 | Fri | CARO | STEADY |
| `A-W6-C4-STA-01` | A | 6 | Sun | STAT | STEADY |

These slot IDs are **frozen at lock**, are recorded in `matrix_84.csv` as the `ai_overlay` column, and are
verified by `tools/validate_matrix.py` (run from the repository root).

### Balance

| Dimension | Result |
|---|---|
| Account | A 3 · B 3 |
| Format | REEL 2 · CARO 2 · STAT 2 |
| Account × format | A: 1 Reel, 1 Carousel, 1 Static · B: 1 Reel, 1 Carousel, 1 Static |
| Block | WARM 3 · STEADY 3 |
| Format × block | REEL 1W/1S · CARO 1W/1S · STAT 1W/1S |
| Account × block | A 1W/2S · B 2W/1S (complementary) |
| Engine | 6 of 6 in C4. C1, C2, C3 contain **zero** AI posts in every window |
| Week | W1 **0** · W2 3 · W3 0 · W4 1 · W5 1 · W6 1 |
| Date collisions | None — no two AI posts share a publishing date |

**Contamination of the primary window: 3 of C4's 14 steady-block posts (21%).**
**Week 1 carries zero AI posts by design**, so the launch week's gate is unaffected.

### Declared limitations

- All three warm-up AI posts fall in Week 2, so the W1-vs-W2 comparison inside C4's warm-up is confounded
  with treatment. That comparison is not used for any decision.
- Account A holds only one C4 Static in the entire experiment and it is AI-treated, so there is no non-AI
  A/C4 static comparator.
- **Placement constraint, for the record:** A has no C4 Static in the warm-up block (its single C4 Static is
  `A-W6-C4-STA-01`), which is why account × block is 1W/2S versus 2W/1S rather than even. This is the best
  available balance without moving a row, and no row was moved.

---

## 4. What qualifies as AI-generated imagery

**In scope:** any raster or vector element in the published creative whose pixels were produced or materially
altered by a generative model — text-to-image, image-to-image, generative fill or expand, generative object
addition or removal, generative upscaling that hallucinates detail.

**Not in scope:** algorithmic chart rendering · non-generative photo adjustment (crop, exposure, colour
balance, sharpening) · template layout · typography.

**Explicitly outside this decision:** captions, scripts and research remain the founders' own writing, per the
engine definitions. This sub-test is about **imagery only**.

---

## 5. Prohibited — even inside the six permitted slots

1. Any depiction readable as a photograph of a **real, specific, identifiable product**. No generated sneaker
   purporting to be an actual model or colorway.
2. Any generated image supporting a **factual claim** — price, release date, colorway, materials,
   availability, sizing, market data.
3. Generated **brand marks or trademarks** (Swoosh, Jumpman, three stripes, wordmarks) or brand-identifying
   design elements.
4. Generated **likenesses of real people** — athletes, designers, celebrities.
5. **Generative video, generative interpolation, and AI voice.** Still imagery only, placed inside the house
   motion template, so the treatment is identical across all three formats. *(AI voice is doubly prohibited:
   the Founder Lock bars voiceover outright for the duration of the test.)*
6. Any generated element in **C1, C2 or C3**, or in any slot outside the six listed above.
7. Imagery mimicking an identifiable creator's style or reproducing a recognisable existing work.
8. Using generation to reconstruct or "clean up" a third-party image the project lacks rights to. That
   launders a rights problem; it does not solve one.
9. Any attempt to strip, obscure or evade a platform AI label.

---

## 6. Disclosure

All six AI-treated posts carry an **identical, fixed in-caption disclosure line**, and any platform AI label
is left intact.

The disclosure is **part of the treatment being measured** — "disclosed AI imagery" is the only version the
business could actually operate, so it is the version worth measuring.

⚠ **The exact disclosure wording is pre-launch work and is NOT yet written.** See `GATES.md`.

---

## 7. Analysis rule

- **Primary account / engine / format conclusions are computed on all 84 posts.** Excluding the AI posts
  would leave C4 with a smaller n than the other engines and break the balance the whole design rests on.
- **Mandatory predeclared sensitivity analysis.** Report C4's median on its primary metric **three ways** —
  full set, AI-excluded, AI-only — for both the primary window and all weeks.
- **Flip rule.** If C4's rank among the four engines, or its ≥2× status against the next-best engine,
  **differs** between the full-set and AI-excluded computations, the C4 engine conclusion is declared
  **UNRESOLVED** and is carried into no Phase 3 decision. C1, C2 and C3 conclusions are unaffected — they
  contain no AI posts.
- **No performance-driven selection.** The six slot IDs are frozen at lock and recorded before any data
  exists. They may not be swapped after Day 1. No slot outside the six may use AI imagery.
- **Failure handling.** An AI slot that Misses is recovered through the standard end-of-schedule path
  **retaining its AI treatment**. No reserve piece may be AI-treated — an unplanned AI substitution would
  break the predeclared subset.
- **Safety trigger.** If either account's Account Status changes after an AI post publishes, the standard hard
  stop applies and the AI treatment is logged as a candidate cause.

---

## 8. Provenance fields required for every AI asset

Recorded alongside the standard asset provenance record:

tool and version · full prompt(s) · seed and parameters where available · attestation that the output contains
**no real specific product, no brand mark and no real person** · reviewer name · disclosure line present (y) ·
platform AI label observed (y/n).
