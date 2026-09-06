# Pre-launch runbook — the founders' path from here to a passed pair of gates

Ordered, with rough hours. Everything below is founder execution; the instruments it uses are already in this
directory. **Nothing here publishes anything.** The start Monday is instantiated only at step 9.

| Step | Do | Uses | Hours | Closes |
|---|---|---|---|---|
| 1 | **Review and lock** the 13 items in `FOUNDER_REVIEW_QUEUE.md`; record them in `DECISIONS.md` | the decision blocks in each document | 2 | Sourcing Gate 1, 2, 7; Week-1 Gate 2, 9 (rotation), 10 (wording) |
| 2 | **Inventory** every pair the founders own or can borrow; write C2 themes toward it | `assets/C2_SOURCING_ROUTES.md` (route O), `backlog/IDEA_BANK.md` | 1 | — |
| 3 | **Build the bank**: rig, first shoot (20 pairs × 3 angles), free-stock pass with licences archived, first 8 house silhouettes; record every row; validator clean | `assets/ASSET_PIPELINE.md`, `assets/provenance_register.csv`, `tools/validate_provenance.py` | 12–15 | Sourcing Gate 3, 4 |
| 4 | **Run the C2 sustainability test** — the two C2 reserve pieces, one per founder, timed | `assets/C2_SUSTAINABILITY_TEST.md` | 3–4 | Sourcing Gate 5; two reserve pieces |
| 5 | **Read and clear C3 sources**: brand release notes and published reports (default), then any marketplace whose terms permit; archive the terms; decide the facts-vs-terms posture once | `assets/C3_DATA_SOURCE_TOS_REGISTER.md` | 3 | Sourcing Gate 6 |
| 6 | **Verify the AI tool** (read its current terms; record tool, version, plan, date) and **produce TEST-AI-01** with the nine-item checklist, timed; sign the attestation | `policy/AI_IMAGERY_POLICY_PACK.md` §5–§7 | 3 | Sourcing Gate 9–12 |
| 7 | **Sign off the Sourcing Gate** | `gates/SOURCING_GATE_SCORECARD.md` | 0.5 | Sourcing Gate |
| 8 | **Seed the queue** from the idea bank at real timestamps; set up the daily C1 release watch; run the time-zone check in the scheduling tool; turn off Facebook cross-sharing on both accounts | `backlog/`, `policy/SCHEDULING_AND_PUBLISH_SETTINGS.md` | 2 | Week-1 Gate 5 (partly) |
| 9 | **Pick the candidate Monday** (the first Monday that leaves two clean production weeks after step 7) and instantiate the calendar locally; put the 21 C1 blocks and the weekly review in both calendars | `tools/instantiate_calendar.py --start … --print`, `operations/C1_DEADLINE_LADDER.md` | 1 | Week-1 Gate Layer 2 (capacity) |
| 10 | **P−2 / P−1 production**: Friday check-outs for Week 1 and Week 2; produce the 11 non-C1 Week-1 pieces and the remaining 5 reserve pieces; QA each; schedule at 16:00 UTC with screenshots; produce and schedule the 14 Week-1 Stories; write the 14 Week-2 outlines | `operations/PRODUCTION_RHYTHM.md` §3, `operations/PRE_PUBLISH_QA.md`, the template specs | 28–32 | Week-1 Gate 1, 6, 7, 9 |
| 11 | **Baselines**: Account Status (five categories) and the full audience snapshot on both accounts; confirm the Insights field names per format; fill the W0 rows | `experiment/tracking/tracking_sheet.xlsx` | 1 | Week-1 Gate 11 |
| 12 | **Day 0, 16:00 UTC: the D2 C1 topic lock** for `A-W1-C1-CAR-01` from the watchlist, logged | `backlog/checkout_log.csv`, `tools/validate_backlog.py --start …` | 0.5 | Week-1 Gate 8 |
| 13 | **Sign off the Week-1 Gate**; the start rule instantiates the date as the first Monday after both gates | `gates/WEEK1_GATE_SCORECARD.md` | 0.5 | Week-1 Gate → launch authorised by the founders |

Total: roughly **60 founder-hours** from this commit to a launch-ready state, of which about half is the
one-off bank build and the Week-1 production itself.

## Two rules that hold throughout

- **If a gate cannot be passed, delay launch.** Do not relax the originality rule, do not alter the matrix,
  do not shrink the ranked-item count to fit the bank. Change the route.
- **No date until both gates pass.** Steps 9–12 use a *candidate* Monday for planning; if the candidate slips,
  re-run the calendar script with the next Monday. Never write the date into the repository.
