# C2 sustainability test — the two-piece sourcing stress test (protocol v2, 2026-09-13)

**Sourcing Gate item 5:** *two complete C2 pieces produced end-to-end from the chosen route, with elapsed
time and asset count recorded. If two pieces cannot be produced rights-clean inside the declared time budget,
the route fails — the route changes, not the matrix.*

**Status: PREPARED — NOT RUN.** The package is in `c2_stress_test/`. The founders run the manual part; the
numbers below are blank until they do. **No timing in this repository is estimated, assumed or filled in
ahead of the run.**

**Why v2.** Protocol v1 (2026-09-06) ran on routes O + F and measured only elapsed time per piece. On
2026-09-13 the founders stated that they cannot self-shoot products at scale, so the route stack was
re-ranked (`C2_SOURCING_ROUTES.md`) and this test now has a second job: **to find out whether C2 at seven
items can be sourced repeatedly, rights-clean, without founder-owned inventory** — measuring the real
production burden by stage, not just whether two pieces eventually existed. The pass thresholds of v1 are
kept and extended; the decision rule is pre-declared in §5 so the result cannot be argued into a pass.

**Amended later on 2026-09-13 (founder decision: no permission outreach).** Route X is off the active path,
so the test has no permission-request stage, no passive wait, no seven-day lapse and no `PENDING` state. The
routes under test are F, B, P (hypothetical, `WOULD_USE_P`), S and opportunistic O. The decision rule (§5)
lost exactly one clause — the "permission wait exceeded the 10-day lead" condition, which existed only for
route X — and is otherwise unchanged; see the note under the table.

---

## 1. What the test is, and is not

| It is | It is not |
|---|---|
| Two **non-publishing prototypes**: `TEST-C2-CAR-01` (Carousel, RANKED) and `TEST-C2-REE-01` (Reel, TIER) | Week-1 content — no Week-1 slot is consumed, no queue entry is made, no date is chosen |
| 7 ranked items each → **14 image requirements**, each with a full provenance row before layout | A bank build — the 42-image bank is sized *after* this test, by its numbers |
| A measurement of burden per stage, per item, per route, with rejections counted | A search for "the easiest two lists" — the themes are representative, fixed before sourcing, and item swaps are logged |
| Run by the founders, one piece each, so both producers are measured | Scheduled or published — never; the prototypes may be promoted to reserve later (§6), or discarded |

The pieces are complete when they are laid out in the house template, captioned, alt-texted and QA'd against
`../operations/PRE_PUBLISH_QA.md` — everything short of scheduling.

## 2. Set-up (fixed before the run)

- **Pieces and themes:** `c2_stress_test/TEST_PIECES.md` — two briefs, seven items and two alternates each,
  chosen under delegated production authority to be representative of the C2 engine, not easy: each list
  names a specific colorway per item (the template requires it), mixes icons with long-tail items, includes
  one PUMA item so route B is exercised, and shares no item with the other list (anti-duplication rule 12).
  Neither theme is in the backlog; neither is a Week-1 topic (none are locked).
- **Ranked-item count:** 7 (ACTIVE — delegated production decision).
- **Routes and order:** `C2_SOURCING_ROUTES.md` (revised 2026-09-13) — F → B → (P with approval) → S,
  O only if a pair is at hand; **no route X** (founder decision, 2026-09-13). Inside F, for this test: CC0 /
  public domain → Pexels → Unsplash → other unambiguous free licences; **CC BY not used** (founder
  correction, 2026-09-13). Every candidate goes through the route's checks in order; every candidate,
  cleared or rejected, is a row in the candidate log.
- **Time boxes:** 10 minutes of discovery per item on route F before falling through; route B only for the
  two brands with an archived reading; then S. There is no waiting stage — each piece's sourcing can be
  completed in one sitting, and the whole run needs no more elapsed time than the founders' own schedule.
- **Item swaps:** allowed (the template's rule: the item changes, not the rule), only from the brief's
  alternates, and **every swap is logged** with its reason — the swap count is a metric of how much
  sourcing distorts editorial choice.
- **Chips:** optional. If a founder adds a retail chip, it is verified on the brand's product page
  (`C3_DATA_SOURCE_TOS_REGISTER.md`: product pages confirm only) and the time is logged under `RESEARCH`, so
  research is never mistaken for sourcing.
- **Declared budgets** (`../templates/C2_RANKINGS_AND_TIER_LISTS.md` §8): Carousel 90 min · Reel 115 min,
  sourcing included. **Pass threshold per piece: ≤ 1.5 × its budget in active minutes (135 / 172).**
- **Two different founders produce one piece each.** Claude's discovery pre-scan (if run) is logged with
  `found_by = CLAUDE_PRESCAN` and its minutes are reported separately; it does not count as founder time and
  it clears nothing.
- **No spending.** Route P is logged as "would have used P" unless a founder approves a specific purchase
  first (`../operations/TOOLING.md`, spending register).

## 3. The instruments

| File | Role |
|---|---|
| `c2_stress_test/TEST_PIECES.md` | The two briefs |
| `c2_stress_test/candidates_log.csv` | **One row per candidate image, cleared or not** — route, source, licence as displayed, the three checks, clearance status, rejection reason, asset ID once cleared |
| `c2_stress_test/timing_log.csv` | **One row per stage per item** (or per piece for piece-level stages), minutes, who — every stage is active founder time |
| `provenance_register.csv` (existing) | The clearance record: a **CLEARED** candidate gets the next `AST-nnnn` and a full row under `piece_ref = TEST-C2-…`; nothing else is recorded there |
| `c2_stress_test/FOUNDER_INSTRUCTIONS.md` | The manual run, step by step; what evidence comes back |
| `c2_stress_test/RESULTS.md` | Filled after the run: the measured table, the decision rule applied, the verdict |
| `tools/validate_c2_stress_test.py` | Reads the two logs and the register; refuses a CLEARED row without evidence or with a failed check; prints the burden summary and the decision rule's reading |

## 4. What is measured — every one of these, separately

| Measure | From |
|---|---|
| Discovery / search time, per item and per route | `timing_log` stage `DISCOVERY` |
| Rights-verification time (licence line, ownership plausibility, trademark-rule fit, reverse-image check) | `RIGHTS_VERIFY` |
| Download / asset preparation (crop, plate) | `ASSET_PREP` |
| Provenance logging | `PROVENANCE` |
| Illustration time for any route-S item | `ILLUSTRATION` |
| Research (reasons, chips, sources) — reported, not part of the sourcing number | `RESEARCH` |
| Layout / Reel assembly / caption + alt text + QA | `LAYOUT` · `REEL_ASSEMBLY` · `CAPTION_QA` |
| **Total active minutes per piece** (all stages; every stage is active) — against 135 / 172 | sum |
| Candidates rejected, and the reason histogram | `candidates_log` |
| Item swaps forced by sourcing | `candidates_log` (`SWAPPED_OUT` rows) |
| Routes that produced ≥ 1 cleared asset — "usable routes" | `candidates_log` |
| Cleared route mix per piece: F · X · B · P · S · O | `candidates_log` |
| Items satisfied without paid spend (%) | `candidates_log` |
| Items that *would* have used P | `candidates_log` notes `WOULD_USE_P` |
| Recurring legal / terms ambiguities encountered | `RESULTS.md` §3, free text, one line each |
| Active minutes per **cleared** image, including the time spent on rejected candidates | computed |

## 5. The decision rule — pre-declared

Applied by the validator and written into `RESULTS.md`. **Read top to bottom; the first row that matches is
the verdict.**

| Verdict | Condition | What follows |
|---|---|---|
| **NOT SUSTAINABLE — STOP AND ESCALATE** | Either piece over 1.5 × budget in active minutes; **or** fewer than **4 of 7** items in either piece from the photographic routes (F / B / P / O) — i.e. route S on 4 or more; **or** any item satisfiable only through a source whose rights could not be established; **or** the extrapolated weekly C2 sourcing load (§7) exceeds **6 h**; **or** a terms ambiguity that cannot be resolved without counsel recurs across items | The founders are told exactly what failed and what the options are (delay; approve a paid budget and re-run; accept an illustration-led C2 as a Founder-Lock question; or something else). **Nothing is redesigned in this repository first.** |
| **SUSTAINABLE WITH CONDITIONS** | Both pieces inside 1.5 × budget and 14 / 14 cleared with evidence, **but** route S on exactly **3 of 7** in either piece, **or** ≥ 1 item would have needed P, **or** the extrapolated weekly load is between 4 and 6 h | The conditions are listed for the founders (a paid budget to approve, an S share to accept); the bank build proceeds only once each condition has an answer |
| **SUSTAINABLE** | Both pieces ≤ 1.5 × budget; **≥ 5 of 7** items per piece from photographic routes; 14 / 14 cleared with evidence and `validate_provenance.py` + `validate_c2_stress_test.py` clean; no paid spend needed; extrapolated weekly load ≤ 4 h | Sourcing Gate item 5 passes; the bank build is sized from the measured numbers (`C2_SOURCING_ROUTES.md`, bank section); the measured minutes replace the declared budgets |

Things the rule **cannot** produce, whatever the numbers: a lower item count, AI imagery in C2, a relaxed
originality rule, "cleared because credited", a permission request to anyone, a change to the matrix or the
format mix, a launch date.

*Correction record, 2026-09-13.* The WITH CONDITIONS row originally also read "or a permission wait exceeded
the 10-day check-out lead". That clause existed only because route X had a passive wait; with route X off
the active path it can never fire, so it was removed. No threshold, no other condition and no verdict order
changed.

## 6. After the run — promotion to reserve, or not

`RESERVE_REGISTER.md` (delegated production decision) planned the two C2 reserve pieces to double as the
test pieces. Under v2 the order is reversed: the pieces are **prototypes first**. If the verdict is
SUSTAINABLE (or WITH CONDITIONS, once answered) **and** every one of the 14 assets' licence or clearance
covers a later single publication on either account, **and** the
pieces pass QA, they may be promoted to `RESERVE-C2-CAR-01` / `RESERVE-C2-REE-01` by renaming `piece_ref`
in the register and filling the reserve register — a separate, logged step. If not promoted, the assets are
retired (never reused — rule 4) and the reserve pieces are built fresh. Promotion is never assumed.

## 7. Extrapolation — how the two pieces speak for twenty-one

| Quantity | Formula (from the measured logs) |
|---|---|
| Active sourcing minutes per cleared image, `m` | (DISCOVERY + RIGHTS_VERIFY + ASSET_PREP + PROVENANCE + ILLUSTRATION, all items, both pieces) ÷ 14 |
| Weekly C2 sourcing load | 3.5 pieces/week × 7 × `m` ÷ 60 — compared with the Friday block (4 h for all check-out, research and sourcing, `../operations/PRODUCTION_RHYTHM.md`) |
| 42-image bank | 42 × `m` ÷ 60 (28 × `m` if the prototypes are promoted) |
| 147-image experiment | 147 × `m` ÷ 60 |
| Per-piece production | measured active minutes per piece → replaces the 90 / 115 / 80 budgets in the template and the rhythm |

## 8. Record

Filled by the validator's summary and the founders' notes in `c2_stress_test/RESULTS.md`. Sign-off:

| Item | Result | Sari | Wasim |
|---|---|---|---|
| `TEST-C2-CAR-01` complete, active minutes __ / 90 (≤ 135) | | ☐ | ☐ |
| `TEST-C2-REE-01` complete, active minutes __ / 115 (≤ 172) | | ☐ | ☐ |
| 14 / 14 cleared with evidence; both validators clean | | ☐ | ☐ |
| Verdict per §5 | | ☐ | ☐ |
| Sourcing Gate item 5 | PASSED / NOT PASSED (date) | ☐ | ☐ |
