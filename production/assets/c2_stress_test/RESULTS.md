# C2 sourcing stress test — results (filled after the run; blank until then)

**Status: NOT RUN.** Every number below is written by the founders from the two logs, or copied from the
output of `python3 tools/validate_c2_stress_test.py`. **Nothing here is estimated in advance.** If a cell is
blank, the measurement has not been taken.

Run dates: from ____ to ____ · Piece 1 producer: ____ · Piece 2 producer: ____ · QA by the other founder.

## 1. The measured table

| Measure | `TEST-C2-CAR-01` (Carousel) | `TEST-C2-REE-01` (Reel) | Both |
|---|---|---|---|
| Items cleared / 7 | | | / 14 |
| **Active minutes, total** — pass ≤ 135 / ≤ 172 | | | |
| Discovery / search (min) | | | |
| Rights verification (min) | | | |
| Download / asset prep (min) | | | |
| Provenance logging (min) | | | |
| Illustration, route S (min) | | | |
| Research — reasons, chips, sources (min; not sourcing) | | | |
| Layout / Reel assembly (min) | | | |
| Caption, alt text, tags, QA (min) | | | |
| Candidates logged / rejected | | | |
| Rejection reasons (histogram) | | | |
| Item swaps forced by sourcing | | | |
| Cleared route mix — F · X · B · P · S · O | | | |
| Photographic items (F/X/B/P/O) / 7 | | | |
| Route S items / 7 | | | |
| Satisfied without paid spend (%) | | | |
| Items that would have used P | | | |
| Usable routes (≥ 1 cleared asset) | — | — | |
| **Active sourcing minutes per cleared image, `m`** | — | — | |
| Cost incurred ($) | | | |
| Claude pre-scan minutes (reported apart; cleared nothing) | | | |

## 2. Extrapolation (from `m`, per `../C2_SUSTAINABILITY_TEST.md` §7)

| Quantity | Value |
|---|---|
| Weekly C2 sourcing load = 3.5 × 7 × `m` ÷ 60 | ____ h (Friday block 4 h) |
| 42-image bank = 42 × `m` ÷ 60 (28 × `m` if the prototypes are promoted) | ____ h |
| 147-image experiment = 147 × `m` ÷ 60 | ____ h |
| Measured per-piece production → replaces the declared 90 / 115 / 80 budgets | Carousel ____ · Reel ____ · Static (derived) ____ |

## 3. Terms and rights ambiguities met during the run — one line each

Record each one as it happened, whether or not it was resolved. Examples of the kind of thing that belongs
here: a PUMA "media channels" reading · a CC0 file page whose uploader's ownership is doubtful
· an Unsplash image that looked like a brand render.

| # | Item / candidate | The ambiguity | How it was handled | Needs counsel? |
|---|---|---|---|---|
| | | | | |

## 4. Can the same process plausibly sustain all 21 C2 posts? — the producers' own answer

Two or three sentences from each founder, written before reading §5, on whether they would do this 3.5 times
a week for six weeks. Honest. This is evidence, not a decision.

- Sari:
- Wasim:

## 5. Verdict — the pre-declared rule (`../C2_SUSTAINABILITY_TEST.md` §5), first matching row wins

| Verdict | Applies? | Because |
|---|---|---|
| NOT SUSTAINABLE — STOP AND ESCALATE | ☐ | |
| SUSTAINABLE WITH CONDITIONS | ☐ | conditions: |
| SUSTAINABLE | ☐ | |

Validator output pasted here (the decision-rule block):

```
```

## 6. What follows from the verdict

- **NOT SUSTAINABLE:** nothing in the repository is redesigned. The finding goes to the founders with the
  options as `C2_SUSTAINABILITY_TEST.md` §5 lists them (delay; approve a paid budget and re-run; put an
  illustration-led C2 to the founders as a Founder-Lock question; other). The bank build does not start.
- **WITH CONDITIONS:** each condition gets a founder answer (a spend approval in `../../operations/TOOLING.md`,
  an explicit acceptance of the S share) before the bank build starts.
- **SUSTAINABLE:** Sourcing Gate item 5 → PASSED (date) in `../../gates/SOURCING_GATE_SCORECARD.md`; the
  bank build is sized from §2; the measured minutes replace the declared budgets in the C2 template and
  `../../operations/PRODUCTION_RHYTHM.md`; the promotion-to-reserve decision (§6 of the protocol) is taken
  and logged.

## 7. Sign-off

| Item | Sari | Wasim | Date |
|---|---|---|---|
| Both logs complete; `validate_provenance.py` and `validate_c2_stress_test.py` clean | ☐ | ☐ | |
| Verdict recorded in §5 | ☐ | ☐ | |
| Promotion to reserve: ☐ yes ☐ no (reason) | ☐ | ☐ | |
