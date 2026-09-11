# Pre-launch runbook — the founders' path from here to a passed pair of gates

Ordered, with rough hours. Everything below is founder execution; the instruments it uses are already in this
directory. **Nothing here publishes anything.** A *candidate* Day 1 is used from step 9; the real Day 1 is
instantiated only at step 13 — the earliest day, on any weekday, whose Day-0 requirements are met (start rule
as amended 2026-09-11).

| Step | Do | Uses | Hours | Closes |
|---|---|---|---|---|
| 1 | **Confirm Adobe Firefly's current terms** — the reading is prepared for you in `assets/FIREFLY_TERMS_VERIFICATION.md` (clauses quoted, mapped to our use, with the checklist); re-open the live pages, confirm each line, create the account and record tool · version · plan · date (a paid plan needs your approval). The trademark posture was accepted on 2026-09-08, so nothing else in the former review queue is waiting on you | `assets/FIREFLY_TERMS_VERIFICATION.md`; `policy/AI_IMAGERY_POLICY_PACK.md` §5; `TRADEMARK_RISK_REVIEW.md` §5 for the rule now binding at QA | 0.5 | Sourcing Gate 9 (items 1, 2, 6, 7, 8 and Week-1 Gate 2, 10 already passed) |
| 2 | **Inventory** every pair the founders own or can borrow; write C2 themes toward it | `assets/C2_SOURCING_ROUTES.md` (route O), `backlog/IDEA_BANK.md` | 1 | — |
| 3 | **Build the bank**: rig, first shoot (20 pairs × 3 angles), free-stock pass with licences archived, first 8 house silhouettes; record every row; validator clean | `assets/ASSET_PIPELINE.md`, `assets/provenance_register.csv`, `tools/validate_provenance.py` | 12–15 | Sourcing Gate 3, 4 |
| 4 | **Run the C2 sustainability test** — the two C2 reserve pieces, one per founder, timed | `assets/C2_SUSTAINABILITY_TEST.md` | 3–4 | Sourcing Gate 5; two reserve pieces |
| 5 | **C3 sources are settled** (press releases, published reports, release notes only — the conservative posture); build the first C3 data sheets from them | `assets/C3_DATA_SOURCE_TOS_REGISTER.md` | 1 | (Sourcing Gate 6 already passed) |
| 6 | **Produce TEST-AI-01** in Firefly with the nine-item checklist, timed; sign the attestation | `policy/AI_IMAGERY_POLICY_PACK.md` §5–§7 | 2 | Sourcing Gate 10–12 |
| 7 | **Sign off the Sourcing Gate** | `gates/SOURCING_GATE_SCORECARD.md` | 0.5 | Sourcing Gate |
| 8 | **Seed the queue** from the idea bank at real timestamps; set up the daily C1 release watch; run the time-zone check in the scheduling tool; turn off Facebook cross-sharing on both accounts | `backlog/`, `policy/SCHEDULING_AND_PUBLISH_SETTINGS.md` | 2 | Week-1 Gate 5 (partly) |
| 9 | **Pick the candidate Day 1** — any weekday; the earliest date that leaves two clean production weeks after step 7 — and instantiate the calendar locally; put the 21 C1 blocks and the weekly review in both calendars. The script prints the real calendar weekday of every slot and the Story rotation for that start | `tools/instantiate_calendar.py --start … --print`, `operations/C1_DEADLINE_LADDER.md` | 1 | Week-1 Gate Layer 2 (capacity) |
| 10 | **P−2 / P−1 production**: Friday check-outs for Week 1 and Week 2 (≥ 10 days before each C2/C4 slot's publish instant); produce the 11 non-C1 Week-1 pieces and the remaining 5 reserve pieces; QA each; schedule at 16:00 UTC with screenshots; produce and schedule the 14 Week-1 Stories (rotation classes from the instantiated calendar); write the 14 Week-2 outlines | `operations/PRODUCTION_RHYTHM.md` §3, `operations/PRE_PUBLISH_QA.md`, the template specs | 28–32 | Week-1 Gate 1, 6, 7, 9 |
| 11 | **Baselines**: Account Status (five categories) and the full audience snapshot on both accounts; confirm the Insights field names per format; fill the W0 rows | `experiment/tracking/tracking_sheet.xlsx` | 1 | Week-1 Gate 11 |
| 12 | **Day 0 (the day before Day 1), 16:00 UTC: the D2 C1 topic lock** for `A-W1-C1-CAR-01` from the watchlist, logged. This is the step that fixes Day 1: once the lock is executed against a date, that date is Day 1 | `backlog/checkout_log.csv`, `tools/validate_backlog.py --start …` | 0.5 | Week-1 Gate 8 |
| 13 | **Sign off the Week-1 Gate and confirm launch-ready**; the start rule instantiates Day 1 as the day after the Day-0 lock — any weekday, no Monday deferral | `gates/WEEK1_GATE_SCORECARD.md` | 0.5 | Week-1 Gate → launch authorised by the founders |

Total: roughly **54 founder-hours** from here to a launch-ready state, of which about half is the one-off
bank build and the Week-1 production itself. Step 1 is short and unblocks the AI arm; the bank build in
step 3 can start immediately, since the trademark posture was accepted on 2026-09-08.

## Two rules that hold throughout

- **If a gate cannot be passed, delay launch.** Do not relax the originality rule, do not alter the matrix,
  do not shrink the ranked-item count to fit the bank. Change the route.
- **No date until both gates pass.** Steps 9–12 use a *candidate* Day 1 for planning; if the candidate slips,
  re-run the calendar script with the next feasible day — not the next Monday. Never write the date into the
  repository.
