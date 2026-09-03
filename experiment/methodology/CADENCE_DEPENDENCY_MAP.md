# Cadence Dependency Map

**Purpose.** The locked methodology was built at **4 feed posts/week/account** (24/account, 48 total). The
active decision is **7/week/account** (42/account, 84 total). This file records which parts transfer unchanged
and which are arithmetically tied to the old cadence and must be re-derived.

**This is documentation of existing material, not a new design.** No replacement numbers are proposed here —
deriving them is the 84-post matrix task.

---

## Carries forward unchanged — cadence-independent

These are principles and definitions. Nothing about them depends on how many posts per week.

| Item | Source |
|---|---|
| **Reach is the denominator for every rate metric.** Views is recorded but never a denominator, and never divided by follower count | G4 §4 |
| Views ≠ Reach; never silently substitute one for the other | G3 §9, G4 §4 |
| **T+7 snapshot for every feed post; T+14 additional snapshot for Reels.** Fixed maturation age — never compare a week-1 post at 40 days to a week-6 post at 5 days | G3 §3, §9 |
| **Medians are the decision statistic.** Maximum reported separately as ceiling evidence | G3 §9 |
| Breakout/viral posts are ceiling evidence, recorded, and change nothing in the schedule. No replication attempt until the test completes | G5 §1 |
| **Zero unoriginal/reposted feed posts**, on the five corrected rationales | G4 §1 Correction 1 |
| An unoriginal post is a **protocol violation, not an emergency** — log, exclude from analysis, replace preserving account/cell/format/slot, do not pause, no clock resets | G5 §3 |
| Internal escalation margin: 3+ unoriginal posts on one account in any 30-day window triggers a production-process review (well below the first-party threshold of 10) | G4 §1, G5 §3 |
| **Anti-duplication rules:** never the same file on both accounts; never the same specific subject on both within 14 days; topics checked out to one account and locked 14 days; different source imagery on every piece | G3 §6, G4 §2 |
| **Frozen-variable list:** username, profile photo, bio, display name, pinned posts, link in bio, posting times, highlights, comment-reply policy, follow/unfollow | G3 §7, G5 §1 |
| No paid promotion, giveaways, Collabs, cross-posting or advertiser outreach during the controlled test | G3 §7 |
| **No performance-based adaptation at any point.** All posting weeks frozen | G5 §1 |
| Week 4 = diagnostic, safety and data-quality checkpoint only, with **no allocation authority**. Week 8 = the decision point | G5 §2 |
| Weekly Account Status check, all five categories, both accounts | G3 §12 |
| Hard stops: any Account Status category leaving green; any content-removal notice or IP report | G5 §3 |
| Both accounts run concurrently with identical structure; editorial roles are an **output** of the experiment, not an input | G3 §6 |
| Stories are a **supporting diagnostic** and gate nothing. No "living-follower rate" | G4 §1 Correction 2 |
| Missed posts and unpublishable assets are recovered preserving account/cell/format/slot; **extend the calendar rather than leave the matrix unbalanced** | G5 §3 |
| Production below 80% of plan → extend the calendar to complete the matrix; do not shrink the matrix to fit | G5 §3 |
| Data failures: record what is unavailable and from which date; do not back-fill estimates | G5 §3 |

---

## Must be re-derived for 84 posts — cadence-dependent

Every item below contains a number that only holds at 4 posts/week/account. **Do not carry any of these
forward as-is.**

| Item | Value at 48 | Why it breaks |
|---|---|---|
| **The matrix itself** | 4 matched publishing events/week (Day 1–4), 24 rows per account | 7 posts/week/account means 7 events; the whole row structure is rebuilt |
| **Per-cell format allocation** | Pooled 6R / 3C / 3S per cell; 3 Reels per cell per account | Derived from 12 posts/cell pooled. At 84 the per-cell totals change |
| **Slot counterbalancing** | 12 Early / 12 Late per account; 3E/3L in every cell | Derived from 24 posts/account. Needs rebuilding for 42, and daily posting may not support two evening slots the same way |
| **Posts per cell / statistical power** | 12 pooled per cell; 6 per account; 3 per account×cell×Reels | The **≥2x readability rule** exists *because* n was this small. New n → re-examine, do not assume the rule transfers unchanged |
| **Analysis windows** | Go/no-go on median of weeks 3–6 = 16 posts/account | Post counts per window change |
| **Scenario A–H thresholds** | Calibrated against the old n and the old weeks-3–6 window | The tree's logic may survive; its sample sizes do not |
| **Weekly format mix** | 2 Reels + 1 Carousel + 1 Static per account | Working intent at 84 is ~4 Reels + 2 Carousels + 1 Static — **not yet locked** |
| **Week-1 production gate** | 8 pieces (4/account) before week 1 begins | Becomes **14 pieces** (7/account) |
| **Story volume** | 3/week/account (18 over 6 weeks) | Not yet decided at the new cadence |
| **Week 4 checkpoint counts** | "16 posts each by end of Week 4"; "12 Stories per account" | Arithmetic of the old cadence |
| **Total production load** | 8 feed posts + 6 Stories/week combined | Becomes 14 feed posts/week combined |

---

## Open design questions the 84-post matrix must answer

Recorded as questions, not answered here.

1. Can perfect pooled format balance per cell be achieved at 42 posts/account with the intended 4/2/1 weekly
   mix, or does an integer residual have to be declared as a limitation the way G4 declared its own?
2. With daily posting, is the Early/Late two-slot counterbalance still the right instrument, or does one fixed
   daily slot per account better control time?
3. Does the cell count stay at four? The 4/2/1 weekly mix gives 7 posts across 4 cells — which does not divide
   evenly within a week.
4. What is the new n per cell, and does the ≥2x comparative rule still hold at that n?
5. Do the Scenario A–H thresholds need recalibration, and does the weeks-3–6 analysis window still apply?
6. Story cadence at daily feed posting.

---

**Source key.** G3 = `../historical-48-post-design/REVIVAL_EXPERIMENT_FINAL_LOCK.md` ·
G4 = `../historical-48-post-design/PATCH_AND_FREEZE_48_POST_MATRIX.md` ·
G5 = `../historical-48-post-design/FINAL_METHODOLOGY_PATCH_MATRIX_FROZEN.md`.
All are **superseded as execution plans** — see `../../strategy/historical/CORRECTIONS_LEDGER.md`.
