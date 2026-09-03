# Measurement Framework and Operating Rules

The methodology that survives the cadence change. Everything here is **cadence-independent** — see
`CADENCE_DEPENDENCY_MAP.md` for what does not transfer.

**Status:** these are the locked methodological principles carried forward from the 48-post design. They were
adopted by the founders into `../../DECISIONS.md`. The *numbers* sized to 48 posts are not here.

---

## 1. Metric definitions — the discipline that matters most

| Term | Definition | Use |
|---|---|---|
| **Views** | Plays or displays **including repeats**. Not unique. Instagram replaced Plays/Impressions with Views in April 2025 | Recorded for every post. **Never a denominator.** Never divided by follower count |
| **Reach** | "Accounts reached" — unique accounts | **The denominator for every rate metric** |
| **Non-follower reach** | The non-follower portion of accounts reached, as Instagram reports it | Primary discovery metric, expressed as % of reach |
| **Follower reach** | The follower portion, as Instagram reports it | The **only** legitimate basis for any statement about follower-base responsiveness |
| **Story reach** | Accounts reached by a Story | Diagnostic only |

**Standing rule.** No metric may use total followers as a denominator unless its numerator is a
follower-specific figure reported by Instagram. The one deliberate exception is format reach rate, retained
only because the external benchmarks are constructed the same way — and it must be labelled as such.

**"Living-follower rate" does not exist.** It was withdrawn. The active fraction of each follower list is
**unknown**, and any number produced by dividing total Story reach or total viewers by follower count is a
non-follower artefact. See `../../strategy/historical/CORRECTIONS_LEDGER.md`, priority correction 2.

**Do not anchor on the 98.7% / 98.5% non-follower share in the passive baseline.** That is residual surfacing
of dormant content and predicts nothing about new-post distribution.

---

## 2. Snapshot protocol

- **T+7** for every feed post — the primary snapshot.
- **T+14** additionally for every Reel — the tail snapshot.
- **Fixed maturation age is the point.** Never compare a post measured at 40 days against one measured at 5.
- Stories snapshot at T+2.
- Account-level weekly: followers start/end, net change, reach, % non-follower, profile visits, external link
  taps, **Account Status across all five categories**, posts published by format, any Instagram notification.
- Full audience snapshot (countries, cities, age, gender) at the start and end of the test only — comparing
  those two is the only way to detect audience-composition drift.

---

## 3. Statistics

- **Median is the decision statistic.** Distributions here are heavy-tailed; means are misleading.
- **Maximum is reported separately as ceiling evidence** and never moves an account from weak to strong.
- A breakout post is recorded and **changes nothing in the schedule**. No replication attempt until the locked
  test completes.
- Comparative cell rules were built on a small-n design. Any comparative threshold must be re-checked against
  the new sample size before use — see `CADENCE_DEPENDENCY_MAP.md`.

---

## 4. Originality standard

**Zero unoriginal/reposted feed posts during the controlled experiment.**

The rationale, as corrected:

1. **Clean attribution** — a repost measures someone else's content, not the production system.
2. **A suppressed or replaced post wastes a matrix slot** and returns no usable measurement.
3. **The experiment is partly a capability test** — whether two people can produce original content at
   cadence. A repost is a skipped rep.
4. **It removes interpretive ambiguity** — weak reach with reposts in the set cannot be attributed.
5. **Margin of safety** — zero against a threshold of ten means judgment errors about "materially enhanced"
   never accumulate toward the wall.

**Not** because one repost makes the account globally ineligible. **It does not.**

**The two mechanisms, kept separate:**

- **Account-level eligibility** turns on *repetition* — 10 or more unoriginal posts in the last 30 days.
  Recovery applies **only to accounts that have already crossed that threshold**. Both accounts are green;
  neither is in a recovery state; a clean account has no clock to reset.
- **Post-level treatment** is independent — an individual unoriginal post may be replaced by the original in
  recommendations, labelled with credit, or deprioritised by near-identical detection, **which judges the
  file, not the account**, with no account-level consequence.

**Handling a violation:** log it; do **not** panic-delete (deletion is an unrecorded account-state change
mid-measurement); exclude the observation from analysis; replace the slot preserving account, cell, format and
slot category, extending the calendar if needed; do not pause the account; no clock resets. Internal
escalation margin: 3+ on one account within any 30-day window triggers a production-process review.

---

## 5. Frozen variables

**Frozen for the duration of the controlled test**, on both accounts: username · display name · bio · profile
photo · link in bio · pinned posts · highlights · posting times · comment-reply policy · follow/unfollow
activity · editorial role · historical feed.

**Prohibited for the duration:** paid promotion · giveaways · Collabs · advertiser outreach · cross-posting ·
adding or dropping a content cell · moving effort between accounts · replicating a breakout.

**No performance-based adaptation at any point.** All posting weeks are frozen. Specifically prohibited: extra
slots for a leading cell, dropping a cell for weak performance, increasing a format allocation, reallocating
toward the stronger account, changing slots, or changing profile variables because conversion looks weak.

---

## 6. Checkpoints

**Weekly review** — same day and time each week, both founders. Screenshot Account Status on both accounts;
log every post that crossed T+7 and every Reel that crossed T+14; update account-weekly rows; check the
trigger list; confirm next week's pieces are produced and scheduled. **No strategy discussion inside the
weekly review** — the most common failure mode of a controlled test is relitigating the design in week 2 after
one bad post.

**Mid-test checkpoint** — diagnostic, safety and data-quality only. **No allocation decision may be taken.**
Covers: Account Status still green; any IP/removal notice; any Instagram metric change; any unoriginal asset
published; any frozen variable inadvertently changed; any prohibited activity; planned vs actually published;
matrix conformance; posting times inside assigned slots; tracking-sheet completeness; T+14 Reel snapshots
recorded; Reach used as denominator everywhere; post-ID convention applied. Observations about which cells or
account look stronger are **recorded, not acted on**.

**Decision point** — at the end of the measurement tail, on medians from the steady-state window.

---

## 7. Stop, extend and investigate rules

**Hard stop:** any Account Status category leaving green on either account — pause that account, screenshot
the flagged item and the exact guideline named, request review if offered, continue the other account. Any
content-removal notice or IP report — pause both, investigate before resuming.

**Extend rather than unbalance:** missed posts are recovered preserving account, cell, format and slot
category; if recovery falls outside the posting weeks, **extend the calendar**. If production falls below 80%
of plan, extend rather than analyse an incomplete matrix. *An extended calendar is preferable to an unbalanced
dataset.*

**Unpublishable asset:** replace with a different asset in the same account, cell, format and slot category.
The matrix row is preserved; only the creative changes. Log the substitution.

**Investigate but keep posting, change nothing:** zero non-follower reach on all Reels for two consecutive
weeks on one account (verify no unoriginal asset entered the set, verify Reel lengths, check Account Status) ·
one account's reach exceeding the other's by >3x for two consecutive weeks (**this is the account effect being
measured**) · Story reach flat or declining (supporting context only) · a breakout post (ceiling evidence).

**Data failure:** record exactly what is unavailable and from which date, capture whatever substitute
Instagram provides, note the affected rows. **Do not back-fill estimates. Do not change the posting plan.**

---

## 8. What the experiment is designed to isolate

Three effects: **account**, **format**, and **content engine**, plus the account × cell interaction as a guard
against generalising an account-specific result.

The interaction check matters: **if a cell only dominates on one account, it is not an engine effect.**

The design removes confounds; it does not manufacture statistical power. Any matrix built at the active
cadence must state its own residual limitations the way the historical design did.

---

**Sources.** Carried forward from the 48-post design chain in `../historical-48-post-design/`, as corrected —
see `../../strategy/historical/CORRECTIONS_LEDGER.md`. Those documents are **superseded as execution plans**;
the principles above are what survives.
