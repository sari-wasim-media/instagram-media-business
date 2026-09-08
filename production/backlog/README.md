# Topic backlog and the blind-to-performance check-out queue

**Week-1 Gate item 5:** *topic backlog live, queue rule operating, C1 release-calendar watchlist populated
for the Week-1 window.* The mechanism is founder-locked
(`../../experiment/active-84-post-plan/ANTI_DUPLICATION_AND_TOPIC_SELECTION.md` §5). This directory is the
instrument that runs it. **Status: BUILT, EMPTY.** The founders populate it; the Week-1 C1 watchlist can only
be populated once the start Monday is known.

| File | What it is |
|---|---|
| `backlog.csv` | **The queue.** One row per candidate subject, entered at its timestamp. Empty until the founders add the first item |
| `checkout_log.csv` | **The audit trail.** One row per check-out: slot · timestamp · item · rule · queue position · the blind attestation |
| `backlog_EXAMPLE.csv` · `checkout_log_EXAMPLE.csv` | Filled examples of both (fictional subjects) |
| `IDEA_BANK.md` | Candidate subjects **not yet in the queue** — a founder moves one into `backlog.csv` at the moment they decide it is a real candidate, at that moment's timestamp |
| `../../tools/validate_backlog.py` | Checks every check-out against the queue rule, the deadlines and the anti-duplication rules |

## The rules, as the instrument enforces them

1. **Entry.** A subject enters `backlog.csv` with its UTC timestamp, engine, a `subject_key` at the locked
   "specific subject" level (`model:court-1-high/deep-royal`, `theme:under-200-looks-expensive`,
   `person:…`, `event:…`, `claim:…`), any secondary subjects (a ranking's #1 pick; a docket's three releases),
   the thesis in one sentence, and for C1 a **confirmed** news or release date with its source. Rumoured dates
   do not enter the C1 queue.
2. **Check-out.** The founder filling a slot takes the **top eligible item** — no choosing:
   - **C2, C3, C4: strict FIFO** by entry timestamp among OPEN items of that engine.
   - **C1: nearest confirmed date** to the slot's publish instant among items whose date falls inside the
     slot's window, ties by entry timestamp. *Operational window (ACTIVE — delegated production decision,
     2026-09-08): news broken up to 7 days before publish, or a release up to 10 days after.* This makes
     "eligible" testable without changing the locked rule.
3. **Deadlines**, from the slot's 16:00 UTC instant: C1 T−48 h · C3 T−7 d · C2 and C4 T−10 d. Earlier is
   always allowed.
4. **Log** every check-out: `checkout_id · timestamp · slot · account · engine · entry_id · rule ·
   queue_position_at_checkout · eligible_count · performance_data_referenced = NO · who`. The attestation is
   the blind-to-performance rule made loggable: a check-out that referenced any published post's performance
   is a protocol violation.
5. **Lock.** A checked-out subject is locked to that account for 14 days. The same `subject_key` may never
   appear on both accounts within 14 days, may anchor at most 2 of one account's 42 posts and never within
   10 days; the same thesis at most once per account and never on both accounts within 14 days. The
   validator computes all of this from slot day-indices, so it works before any calendar date exists.
6. **Obsolescence.** If a subject dies (release delayed or cancelled), mark the entry `INVALID`, draw the next
   eligible item, keep every slot attribute unchanged, log the substitution (exception protocol).
7. **Audit.** At the mid-test checkpoint, run the validator and confirm every check-out took the top eligible
   item; any deviation is logged as such.

## Operating rhythm

Every **Friday** (see `../operations/PRODUCTION_RHYTHM.md`) the founders check out all C2, C3 and C4 slots of
the week after next — 10–16 days ahead, inside every deadline — and add new candidates to the queue as they
occur, at the moment they occur. C1 check-outs happen slot by slot at T−48 h from the release watchlist,
which is simply the C1 rows of `backlog.csv` ordered by date.

## Running the validator

```
python3 tools/validate_backlog.py                       # queue rule + anti-duplication (day-index based)
python3 tools/validate_backlog.py --start YYYY-MM-DD    # also checks the absolute check-out deadlines; the date is not stored
```
