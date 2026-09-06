# C1 deadline ladder — all 21 slots, relative to launch day

**Locked rule (`GATES.md` §2.3):** measured from each slot's 16:00 UTC publish instant — **T−48 h topic lock** (irreversible, from the queue, logged) · **T−24 h production complete** (every factual claim verified, QA passed) · **T−12 h scheduled** in-platform. Identical for all 21 C1 slots, all six weeks. A slot that misses T−24 h is a Miss and recovers by the exception protocol; it is never converted to evergreen.

This table is generated from `matrix_84.csv` in **launch-relative days** (Day 1 = the Week-1 Monday, Day 0 = the Sunday before launch). No calendar date is recorded here — run `python3 tools/instantiate_calendar.py --start YYYY-MM-DD --print` locally once the start Monday exists to get absolute datetimes.

| # | Slot | Wk | Day | Weekday | Format | Publish | Topic lock (T−48 h) | Production complete (T−24 h) | Scheduled by (T−12 h) | Production block (declared budget) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `A-W1-C1-CAR-01` | 1 | 2 | Tue | CARO | Day 2 16:00 UTC | Day 0 16:00 UTC | Day 1 16:00 UTC | Day 2 04:00 UTC | Day 1, between 16:00 UTC lock+0 and 16:00 UTC — 65 min |
| 2 | `A-W1-C1-STA-01` | 1 | 6 | Sat | STAT | Day 6 16:00 UTC | Day 4 16:00 UTC | Day 5 16:00 UTC | Day 6 04:00 UTC | Day 5, between 16:00 UTC lock+0 and 16:00 UTC — 55 min |
| 3 | `B-W1-C1-REE-01` | 1 | 7 | Sun | REEL | Day 7 16:00 UTC | Day 5 16:00 UTC | Day 6 16:00 UTC | Day 7 04:00 UTC | Day 6, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 4 | `A-W2-C1-REE-01` | 2 | 8 | Mon | REEL | Day 8 16:00 UTC | Day 6 16:00 UTC | Day 7 16:00 UTC | Day 8 04:00 UTC | Day 7, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 5 | `B-W2-C1-CAR-01` | 2 | 9 | Tue | CARO | Day 9 16:00 UTC | Day 7 16:00 UTC | Day 8 16:00 UTC | Day 9 04:00 UTC | Day 8, between 16:00 UTC lock+0 and 16:00 UTC — 65 min |
| 6 | `A-W2-C1-REE-02` | 2 | 12 | Fri | REEL | Day 12 16:00 UTC | Day 10 16:00 UTC | Day 11 16:00 UTC | Day 12 04:00 UTC | Day 11, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 7 | `B-W2-C1-REE-01` | 2 | 13 | Sat | REEL | Day 13 16:00 UTC | Day 11 16:00 UTC | Day 12 16:00 UTC | Day 13 04:00 UTC | Day 12, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 8 | `B-W3-C1-REE-01` | 3 | 15 | Mon | REEL | Day 15 16:00 UTC | Day 13 16:00 UTC | Day 14 16:00 UTC | Day 15 04:00 UTC | Day 14, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 9 | `B-W3-C1-STA-01` | 3 | 19 | Fri | STAT | Day 19 16:00 UTC | Day 17 16:00 UTC | Day 18 16:00 UTC | Day 19 04:00 UTC | Day 18, between 16:00 UTC lock+0 and 16:00 UTC — 55 min |
| 10 | `A-W3-C1-REE-01` | 3 | 20 | Sat | REEL | Day 20 16:00 UTC | Day 18 16:00 UTC | Day 19 16:00 UTC | Day 20 04:00 UTC | Day 19, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 11 | `A-W3-C1-REE-02` | 3 | 21 | Sun | REEL | Day 21 16:00 UTC | Day 19 16:00 UTC | Day 20 16:00 UTC | Day 21 04:00 UTC | Day 20, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 12 | `B-W4-C1-REE-01` | 4 | 23 | Tue | REEL | Day 23 16:00 UTC | Day 21 16:00 UTC | Day 22 16:00 UTC | Day 23 04:00 UTC | Day 22, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 13 | `A-W4-C1-REE-01` | 4 | 24 | Wed | REEL | Day 24 16:00 UTC | Day 22 16:00 UTC | Day 23 16:00 UTC | Day 24 04:00 UTC | Day 23, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 14 | `A-W4-C1-CAR-01` | 4 | 26 | Fri | CARO | Day 26 16:00 UTC | Day 24 16:00 UTC | Day 25 16:00 UTC | Day 26 04:00 UTC | Day 25, between 16:00 UTC lock+0 and 16:00 UTC — 65 min |
| 15 | `B-W4-C1-REE-02` | 4 | 28 | Sun | REEL | Day 28 16:00 UTC | Day 26 16:00 UTC | Day 27 16:00 UTC | Day 28 04:00 UTC | Day 27, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 16 | `A-W5-C1-STA-01` | 5 | 30 | Tue | STAT | Day 30 16:00 UTC | Day 28 16:00 UTC | Day 29 16:00 UTC | Day 30 04:00 UTC | Day 29, between 16:00 UTC lock+0 and 16:00 UTC — 55 min |
| 17 | `B-W5-C1-REE-01` | 5 | 31 | Wed | REEL | Day 31 16:00 UTC | Day 29 16:00 UTC | Day 30 16:00 UTC | Day 31 04:00 UTC | Day 30, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 18 | `B-W5-C1-CAR-01` | 5 | 32 | Thu | CARO | Day 32 16:00 UTC | Day 30 16:00 UTC | Day 31 16:00 UTC | Day 32 04:00 UTC | Day 31, between 16:00 UTC lock+0 and 16:00 UTC — 65 min |
| 19 | `A-W6-C1-CAR-01` | 6 | 36 | Mon | CARO | Day 36 16:00 UTC | Day 34 16:00 UTC | Day 35 16:00 UTC | Day 36 04:00 UTC | Day 35, between 16:00 UTC lock+0 and 16:00 UTC — 65 min |
| 20 | `A-W6-C1-REE-01` | 6 | 39 | Thu | REEL | Day 39 16:00 UTC | Day 37 16:00 UTC | Day 38 16:00 UTC | Day 39 04:00 UTC | Day 38, between 16:00 UTC lock+0 and 16:00 UTC — 80 min |
| 21 | `B-W6-C1-CAR-01` | 6 | 41 | Sat | CARO | Day 41 16:00 UTC | Day 39 16:00 UTC | Day 40 16:00 UTC | Day 41 04:00 UTC | Day 40, between 16:00 UTC lock+0 and 16:00 UTC — 65 min |

## Reading the table

- **`A-W1-C1-CAR-01` locks on Day 0 — the Sunday before launch.** That is why the D2 topic lock is a Layer-1 Week-1 Gate item: it must be executed before Day 1 exists.
- Nine C1 slots publish on a weekend day; their production blocks fall on Friday or Saturday. The matrix fixes the publication day, not the production day, but the ladder's T−24 h deadline does fix the latest production day. Plan the founders' weekend availability against this table.
- Two C1 pressure-point pairs sit on consecutive days on Account A (`A-W3-C1-REE-01` Sat → `A-W3-C1-REE-02` Sun): two topic locks on Days 18 and 19, two production blocks on Days 19 and 20, and the anti-duplication check recorded in both rows.
- **Capacity reservation (Week-1 Gate Layer 2):** for every row, a named, calendared block of the declared budget sits inside the window between the lock and the scheduling deadline, in each founder's calendar, alternating producers. The tracking row's `producer` field names who held the block.

## The C1 production block, step by step (from `../templates/C1_RELEASE_VERDICT_DESK.md` §7)

| Offset | Step |
|---|---|
| T−48 h | Draw the top eligible item from the C1 queue (nearest confirmed release/news date inside the slot window, ties by entry timestamp); log slot · timestamp · item · rule · queue position · `performance_data_referenced = NO`; fill the research sheet; log the sources |
| T−36 h | Verify every fact against the logged sources; score the rubric; write the three reasons; source the image or choose the no-image layout |
| T−28 h | Layout in the template |
| T−24 h | **Production complete** — QA against the content-quality minimum; caption, alt text, tags |
| T−12 h | **Scheduled** at 16:00 UTC; screenshot of the scheduled state in the tracking row |
