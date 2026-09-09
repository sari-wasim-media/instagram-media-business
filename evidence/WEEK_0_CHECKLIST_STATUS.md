# Week 0 Checklist — Status

The 26-item pre-launch checklist comes from §15 of `REVIVAL_EXPERIMENT_FINAL_LOCK.md`, which belongs to the
**superseded 48-post design**.

## ⚠ Read this before using the table

**An uncompleted item here is not automatically an open task.** Three different things can make an item
not-done, and they have opposite implications:

- a later founder decision **superseded** it,
- it is **not yet applicable** because it depends on a matrix that does not exist,
- or it is genuinely **outstanding**.

Reading this as a flat to-do list would manufacture false tasks and quietly reactivate 48-post assumptions.

| Status | Meaning |
|---|---|
| **DONE** | Completed. Evidence in this directory or founder-reported |
| **NOT DONE** | Genuinely outstanding |
| **UNVERIFIED** | May be complete; no evidence either way in the source packages |
| **SUPERSEDED BY LATER DECISION** | A later founder decision removed or replaced the requirement |
| **NOT YET APPLICABLE** | Depended on the 84-post matrix — now unblocked; see the note below |
| **DECIDED BY FOUNDER LOCK** | Settled by the 2026-09-05 Founder Lock |

---

## Security and access

| # | Item | Status | Notes |
|---|---|---|---|
| 1 | Both founders have working logins to both accounts | **UNVERIFIED** | Not evidenced in either package |
| 2 | Enable 2FA on both accounts, recovery codes stored reachably | **DONE** (2FA) · **UNVERIFIED** (code storage) | 2FA confirmed enabled on both. Where the recovery codes are stored is not recorded — and **must never be recorded in this repository** |
| 3 | Confirm both accounts are Professional so full Insights are available | **DONE** | Professional dashboard visible on both profile screenshots |

## Baseline capture

| # | Item | Status | Notes |
|---|---|---|---|
| 4 | Screenshot Account Status, all five categories, both accounts | **DONE** | `account-a-…/01`, `account-b-…/06` |
| 5 | Screenshot full audience data both accounts | **DONE** | Countries, cities, age, gender, active times — both accounts |
| 6 | Screenshot 90-day account Insights both accounts | **DONE** | Views, viewers, splits, interactions, profile visits, link taps, net followers |
| 7 | Screenshot first 18 grid tiles of each account | **DONE** | `profile-baseline/01`, `02` |
| 8 | Record the exact date of the last published post on each account | **PARTIAL** | Inferable but not explicitly recorded: A active into late 2023 (2.6M Reel dated 2023-10-29), B last posted 2021. Worth confirming exactly |
| 9 | Capture post-level Insights for the last 9 pre-dormancy posts on each | **PARTIAL** | 12 samples captured across both accounts rather than 9 per account. Sufficient for the medians; short of the letter of the item |

## Legacy content

| # | Item | Status | Notes |
|---|---|---|---|
| 10 | Inspect full feed of both accounts, list posts meeting both removal criteria | **DONE** | Produced the three-post list |
| 11 | Screenshot each identified post **and its Insights** before touching it | **DONE** | `legacy-cleanup/`, 4 files |
| 12 | Remove that subset. Remove nothing else | **DONE** | Three UAPLG posts removed. Nothing else deleted — this was deliberate |
| 13 | Check Story Highlights and the bio link destination for the same category | **DONE** (Highlights) · **UNVERIFIED** (bio link destination) | Highlights checked and found clean |

## Account setup

| # | Item | Status | Notes |
|---|---|---|---|
| 14 | Set the display name on both accounts | **SUPERSEDED BY LATER DECISION** | **Founder-confirmed: neither display name was changed.** They remain "streetwear life" and "Sneakerbong". The founders chose a minimal edit over a rewrite. Not an outstanding task — display names are now a frozen variable |
| 15 | Rewrite the bio on both accounts | **SUPERSEDED BY LATER DECISION** — a minimal edit was made instead | **The founders deliberately did not rewrite the bios.** They removed the follower-goal line from each and kept the rest substantially unchanged. Founder-confirmed; not separately screenshot-verified after the edit |
| 16 | Set one link in bio on each account | **DECIDED BY FOUNDER LOCK — no link** | Sari and Wasim decided jointly: **no link in bio for the duration of the controlled test.** No longer deferred, no longer an open question. See `../DECISIONS.md` |
| 17 | Unpin all pinned posts on both accounts | **UNVERIFIED** | No evidence either way |
| 18 | Screenshot the final Week 0 profile state of both accounts | **NOT DONE — optional, not blocking** | The packages hold only pre-change screenshots. Because the actual edit was minimal (one line removed per bio), those screenshots still document the surrounding state; a post-change capture would upgrade the removal from founder-confirmed to screenshot-evidenced |

### On item 16 — link in bio

The historical rationale was that bio link taps read zero over 90 days and the figure was uninterpretable
without knowing whether a link existed; a link was called "the only instrument you have for commercial
intent."

**Why it is recorded as superseded rather than outstanding:** the founders' profile-freeze decision
deliberately settled the profile state before the experiment, and both bios already route business contact
through DM — `📩 | DM for promo` on Account A, `Dm for business/promotion 📩` on Account B — rather than
through a link. The absence of a link is a plausible deliberate outcome of that decision, not an overlooked
task. Adding a link now would also change a frozen profile variable.

*(The founders' bio edit was minimal: only the follower-goal line was removed. Both DM lines are visible in
the pre-change screenshots and are understood to remain in place.)*

**Worth a founder yes/no at review — not blocking.** If the founders intend a link, it must be set **before**
Post #1, never mid-experiment.

## Experiment infrastructure

| # | Item | Status | Notes |
|---|---|---|---|
| 19 | Build the tracking sheet | **SKELETON BUILT (2026-09-06)** — not yet live | Generated from `../experiment/active-84-post-plan/matrix_84.csv` by `tools/build_tracking_sheet.py`: `experiment/tracking/posts.csv`, `account_weekly.csv`, `stories.csv`, `tracking_sheet.xlsx`. "Live" = adopted by the founders with the W0 baseline rows filled. Week-1 Gate item |
| 20 | Adopt the post ID convention `A-W3-C2-CAR-01` | **DONE** | All 84 IDs are assigned in `matrix_84.csv` |
| 21 | Second tab account-weekly, third tab Stories log | **SKELETON BUILT (2026-09-06)** | Account-weekly: 18 rows (W0–W8 × 2). Stories log: **84 rows** with the rotation class and the sticker flag. Part of the tracking sheet |
| 22 | Build the shared topic backlog with the 14-day check-out lock | **INSTRUMENT BUILT — EMPTY (2026-09-06)** | `production/backlog/` (queue, check-out log, idea bank) with `tools/validate_backlog.py` enforcing the queue rule, the 14-day / 10-day locks and the blind attestation. Populating it is founder work. Week-1 Gate item |

## Content readiness

| # | Item | Status | Notes |
|---|---|---|---|
| 23 | Produce and schedule all Week-1 pieces before Week 1 starts | **NOT YET APPLICABLE** + count **SUPERSEDED** | The item says **8 pieces** (4/account). At the active cadence Week 1 requires **14** (7/account). Blocked on the matrix |
| 24 | Build reusable templates (chart, ranking carousel, verdict card, meme layout) | **DONE (2026-09-08)** — delegated production decisions | `production/templates/` — all four house systems plus the Story frame, as specs with 64 rendered specimens and a Reel pacing reference; C2 ranked-item count 7. Recorded in `DECISIONS.md`; founders may override before Day 1 |
| 25 | Resolve imagery sourcing for C2 and C3 | **DECIDED; EXECUTION NOT STARTED (2026-09-08)** | Source-class order per engine and the C2 route stack are decided (`production/assets/`); C3 sources are settled under the conservative data-source posture (published reports and release notes only); the trademark posture was **accepted on 2026-09-08** (`production/TRADEMARK_RISK_REVIEW.md`), so product photography runs under its §5 rule. The asset bank (42 C2 images for the gate) and the C2 sustainability test remain founder work. Still the binding constraint |
| 26 | Write the originality rule where both founders can see it: **zero unoriginal posts** | **DONE (2026-09-06)** | `production/policy/ORIGINALITY_RULE.md` — the one-page rule card |

---

## Summary

**Status after the Creative System sprint (2026-09-06) and the decision pulse (2026-09-08):** items 19 and
21 have a built skeleton; item 22 has its instrument (empty); item 24 is done (delegated production
decisions); item 25 is decided except the founders' trademark answer, with its execution (the asset bank,
the sustainability test) outstanding — **still the binding constraint**; item 26 is done. **Genuinely
outstanding:** item 23 (Week-1 production — deliberately not started) and the execution halves of 22 and 25.
All are tracked item by item in `../production/gates/`.

**New pre-launch items not in the historical 26**, created by the Founder Lock: declare the 7-day Story
rotation and fix the sticker weekday · write the fixed AI disclosure wording · verify the AI tool's
commercial-use licence · build the 7-piece evergreen reserve · capture the Week-0 baselines. All are in
`../experiment/active-84-post-plan/GATES.md`.

**Optional evidence improvement (1):** item 18 — a post-change profile capture. Not blocking.

**Unverified (4):** items 1, 2 (code storage), 13 (bio link destination), 17 · plus partials at 8 and 9.

**Superseded or decided (3):** items 14 and 15 — the founders chose a **minimal bio edit** (removing the
follower-goal line) over the proposed rewrite — and item 16, now **decided by Founder Lock: no link in bio**.
The piece-count inside item 23 is superseded by the locked cadence.

⚠ **Do not reopen items 14 or 15 as work.** The proposed bio rewrite was deliberately not applied. Listing it
as outstanding would push the founders toward a change they decided against, and toward altering a **frozen**
profile variable.

**No longer "not yet applicable".** The 84-post matrix is locked, so items 19–24 are unblocked and are now
ordinary pre-launch work.

**The go/no-go that still binds:** item 23's principle survives its arithmetic. Week 1's pieces must be
produced and scheduled **before** Week 1 begins. The historical design was explicit that starting and slipping
produces a false negative on assets that may not be testable twice. The current form of that gate is the
two-layer Week-1 Gate in `../experiment/active-84-post-plan/GATES.md` §2 — and the correct response to a
failed gate is to **delay launch**, never to alter the locked matrix.
