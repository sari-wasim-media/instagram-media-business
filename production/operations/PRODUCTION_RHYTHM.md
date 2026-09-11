# Production rhythm — how 14 feed posts and 14 Stories a week get made, on time, by two people

**Status: ACTIVE — delegated production decision (2026-09-08).** It implements the locked constraints —
one post per account per day at 16:00 UTC, the check-out deadlines, the C1 ladder, the ≥ 7-piece buffer, the
7-piece reserve, the weekly review with no strategy discussion — and changes none of them. Estimates come
from the declared budgets in `../templates/README.md`; replace them with measured times after Week 1.

## 1. The two clocks

| Clock | Governs | Lead |
|---|---|---|
| **Evergreen clock** (C2, C3, C4 — 63 of 84 posts) | Check out on **Friday** every slot whose publish date falls 10–16 days ahead; produce it the following week; schedule it on the Thursday before its publish date | ≥ 7 days finished before publish → the buffer |
| **News clock** (C1 — 21 posts) | The ladder: lock T−48 h, produce by T−24 h, schedule by T−12 h. Roughly one C1 slot every two days | 48 hours |

Publication days are fixed by the matrix; **production days are not.** Weekend posts are produced by
Thursday and scheduled; only C1's ladder ever forces weekend production (see `C1_DEADLINE_LADDER.md`).

**"Next week" in this document means the next seven publish days** — the 14 feed slots (both accounts) and
14 Stories whose publish dates fall in the seven calendar days after the coming Thursday scheduling block.
The matrix's posting weeks are launch-relative (Day 1 may fall on any weekday — start rule as amended
2026-09-11) and need not align with calendar weeks; the grid below is a calendar-week rhythm that works
against publish dates from the instantiated calendar, never against matrix week numbers. The Story rotation
is calendar-keyed, so Monday is always DROP CALENDAR and Wednesday always carries the sticker, whatever the
matrix day label says.

## 2. The standard week (posting weeks 1–6)

| Day | Block | What happens | Approx. hours (both founders) |
|---|---|---|---|
| **Mon** | Weekly review (fixed hour, both founders) | Account Status screenshots both accounts · T+7 / T+14 / T+2 rows logged · account-weekly rows · buffer ≥ 7 confirmed · the next seven publish days' pieces confirmed scheduled · deviations logged. **No strategy discussion.** | 1.0 |
| Mon | C1 watch | Release-calendar scan (15 min, daily); any C1 lock due today | 0.5 + ladder |
| **Tue** | Reels batch | The next seven publish days' Reels (4 per account = 8) assembled from finished layouts; audio chosen from Sound Collection at upload time and logged | 5.0 |
| **Wed** | Carousels + Statics batch | The next seven publish days' 4 carousels and 2 statics; alt text and captions | 4.5 |
| **Thu** | QA + scheduling + Stories | QA every piece against `PRE_PUBLISH_QA.md`; schedule the next seven publish days' non-C1 slots at 16:00 UTC; batch the 14 Story frames (classes from the instantiated calendar); schedule the non-sticker frames where the Week-0 test proved it, otherwise post manually at 17:30 UTC | 3.5 |
| **Wed** (every week) | Sticker Story, manual | Post THE POLL frame manually on both accounts at 17:30 UTC ± 30 min, adding the sticker in the app (scheduler support unverified — not assumed) | 0.3 |
| **Fri** | Check-out + research | Check out every C2/C3/C4 slot publishing 10–16 days ahead (log); C3 data collection for those pieces; C2 sourcing and provenance rows; idea bank → backlog entries | 4.0 |
| Sat–Sun | C1 ladder only | Only the C1 slots whose ladder lands on the weekend (see ladder table) | ladder |
| Daily | Community | Replies within 24 h per `../policy/COMMENT_REPLY_POLICY.md`; C1 watch | 0.5 |

≈ 19–21 h/week plus the C1 ladder (≈ 21 pieces × ~65 min ≈ 3.8 h/week), consistent with the ≈ 23 h/week
estimate recorded in `GATES.md` §3. The founders' estimate is a band, not a measurement; log actual minutes
in the tracking row (`producer` + notes) for the first two weeks and re-plan on the numbers.

## 3. The two pre-launch production weeks (P−2, P−1)

| Week | Output | Gate item |
|---|---|---|
| **P−2** | Templates confirmed (founder lock) · asset bank build (`../assets/C2_SOURCING_ROUTES.md`, ≈ 15 h) · sustainability test (2 C2 reserve pieces) · AI-route test piece · ToS register rows read · backlog seeded · Week-1 check-outs logged (C2/C3/C4 by the Friday ≥ 10 days before Day 1) | Sourcing Gate 1–12 |
| **P−1** | The 11 non-C1 Week-1 pieces produced, QA'd, **scheduled**; the remaining 5 reserve pieces; Week-1's 14 Stories produced and scheduled; Week-2 outlines (14); Week-0 baselines captured; tracking sheet live; **Day-0 C1 topic lock** (`A-W1-C1-CAR-01`, the day before Day 1, 16:00 UTC) | Week-1 Gate Layer 1 |

Day 1 is instantiated only after both gates pass — on any weekday — so P−2 and P−1 are counted backwards
from a *candidate* Day 1 that is chosen *when* the work above is done, not before. That is the start rule
(as amended 2026-09-11) working as intended: no date, no slipping, and no idle days waiting for a Monday.

## 4. Producers and the account/producer separation

"Which founder produces which piece" is late-bound and logged. The one constraint: **never weld a producer to
an account.** Sari-does-A / Wasim-does-B would make the account effect partly a producer effect. Alternate
by **format batch** instead: one founder takes the Reels batch one week and the carousel/static batch the
next; C1 slots alternate by slot number. The tracking row's `producer` field is the record; the mid-test
checkpoint reads the producer × account split and expects it near 50/50.

## 5. Buffer and reserve

- **Buffer:** ≥ 7 finished, QA'd, rights-clean pieces banked at all times, i.e. the next seven publish days'
  non-C1 pieces done by Thursday. Below 7 at any weekly review → the Friday block goes to production before research.
- **Reserve:** 7 evergreen pieces (`RESERVE_REGISTER.md`), never C1, never AI-treated, used only through the
  exception protocol for the *same engine and format*, and refilled the following week.

## 6. The weekly review — agenda (locked content, fixed form)

1. Account Status, both accounts, all five categories — screenshot into the evidence store; any non-green →
   hard stop for that account, per protocol.
2. Every post past T+7 logged; every Reel past T+14 logged; every Story past T+2 logged; no blank cells.
3. Account-weekly rows completed (descriptive only).
4. Planned vs published; `LATE` count; deviations and their protocol handling.
5. Buffer ≥ 7? Reserve intact? Next week scheduled? C1 ladder blocks calendared?
6. Provenance and backlog validators run clean (`tools/validate_provenance.py`, `tools/validate_backlog.py`).
7. **Nothing else.** No "what's working". No allocation talk. Observations about strength are written into
   the notes column and not discussed.

## 7. The daily 15 minutes

C1 release-calendar scan (brand release notes, retailer calendars, the sources in the C3 register row 1);
new confirmed dates entered into `backlog.csv` at that moment; any T−48 h lock due today executed and logged.
