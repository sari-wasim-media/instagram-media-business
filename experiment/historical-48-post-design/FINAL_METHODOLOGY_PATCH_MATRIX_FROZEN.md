# Final Methodology Patch — Matrix Frozen

## 1. Final correction

**What is changing.** All performance-based adaptation is removed from the experiment. The Week 4 checkpoint becomes diagnostic and safety only.

**Why.** The previous split — Weeks 1–4 as the primary balanced dataset, Weeks 5–6 as an adaptive extension — was a patch on a flaw rather than a fix. Weeks 1–4 were never independently balanced across every controlled variable: the 32-post subset does not carry the same cell × format × slot balance that the full 48-post design does, so treating it as the primary dataset would have discarded the orthogonality that the balancing correction existed to create. Adapting Weeks 5–6 on interim results would also introduce adaptive-selection bias into the comparison the experiment is built to make. Freezing all six weeks is cleaner.

**No longer allowed at any point during the six posting weeks:**

- Extra Reel slots for a leading cell
- Dropping a cell for weak performance
- Increasing any format allocation because it appears stronger
- Reallocating effort toward the apparently stronger account
- Changing posting slots because one appears stronger
- Changing bio, display name, profile photo or pinned posts because conversion looks weak
- Changing either account's editorial role
- Replicating or chasing a breakout post

**Language removed from the plan.** The "double down" rule, the "drop a cell" rule, the Week 4 adaptation gate, the balance clause governing symmetric adaptation, and every reference to Weeks 1–4 as primary or Weeks 5–6 as confirmatory. The final analysis uses the complete locked dataset: all six weeks, all 48 planned posts, excluding only documented protocol-invalid observations, with medians as already specified.

**Outliers.** A breakout post is recorded separately as ceiling / breakout evidence and changes nothing in the schedule. No replication attempt until the locked test is complete.

---

## 2. Corrected Week 4 protocol

**Week 4 Diagnostic, Safety and Data-Quality Checkpoint.** Not an optimisation gate. No allocation decision may be taken at this meeting.

### Safety and platform

1. Account Status screenshot, both accounts, all five categories — confirm still green, and specifically confirm recommendation eligibility.
2. Any IP notice, content-removal notice, or Instagram warning received since Week 0.
3. Any Instagram change to available metrics, metric definitions, or Insights layout.

### Protocol integrity

4. Any unoriginal or reposted asset published to date — logged, excluded from analysis, replacement scheduled per disruption rules.
5. Any frozen variable inadvertently changed (bio, display name, profile photo, pinned posts, posting slots, link in bio).
6. Any prohibited activity: paid promotion, giveaway, Collab, advertiser outreach, cross-posting, follow/unfollow.

### Execution

7. Planned vs actually published, per account: 16 posts each by end of Week 4. Any missed post identified with its account, cell, format and slot category for recovery.
8. Every published post matches its locked matrix row (cell, format, slot). Any deviation logged.
9. Posting times landed inside the assigned slot.
10. Stories: 12 published per account, at the assigned time, one interactive sticker per week.

### Data quality

11. Tracking sheet complete for every post that has crossed T+7. No blank cells.
12. T+14 Reel snapshots recorded for Reels published in Weeks 1–2.
13. Every rate metric uses Reach as denominator. No instance where Views was substituted.
14. Story insights: confirm whether Instagram is exposing the follower/non-follower split, so it is settled by Week 8 which Story metric is in use.
15. Post ID convention applied consistently and asset files still matched to IDs.

### Observation only — record, do not act

16. Which cells appear strongest. Which account appears stronger. Notable outliers. Apparent format differences.

**Record these in a dated Week 4 observation note and close the meeting.** No decision follows from item 16 until Week 8.

---

## 3. Corrected early-stop and disruption rules

Only genuine safety, platform, execution or data failures. Nothing performance-driven.

### Hard stop

- **Account Status changes from green in any category on either account.** Pause that account immediately. Screenshot the flagged item and the exact guideline named. Request review if offered. Continue the other account; the paused account's series ends at that date and its remaining matrix rows are marked incomplete.
- **Any content-removal notice or IP report.** Pause both accounts, investigate before resuming.

### Unpublishable asset

If a planned asset cannot legally or safely be published (rights problem, factual error discovered, sensitive news event), replace it with a different asset in the **same account, same cell, same format, same slot category**. The matrix row is preserved; only the creative changes. Log the substitution.

### Missed post

Recover it while preserving account, cell, format and slot category. Publish the recovery as soon as production allows. If recovery would fall outside the six posting weeks, **extend the calendar to complete the matrix** rather than leaving the row empty. An extended calendar is preferable to an unbalanced dataset.

### Protocol violation — unoriginal post published

1. Log it. Do not delete in a panic; deletion is an unrecorded account-state change mid-measurement.
2. Exclude that observation from all analysis.
3. Replace the slot with an original asset in the same account, cell, format and slot category, extending the calendar if needed.
4. Escalation: 3 or more unoriginal posts on one account within any 30-day window triggers a production-process review. This is an internal early-warning margin well below the first-party threshold of 10 and carries no platform consequence in itself.
5. Do not pause the account. No clock resets. Neither account is in a recovery state.

### Production failure

If cumulative published posts fall below 80% of plan at any checkpoint, **extend the calendar to complete all 48 posts** rather than analysing an incomplete matrix. Do not reduce the matrix to fit the calendar.

### Data failure

If analytics are missing, corrupted, or a metric is removed by Instagram: record exactly what is unavailable and from which date, capture whatever substitute Instagram provides, and note the affected rows. Do not back-fill estimates. Do not change the posting plan.

### Investigate — keep posting, change nothing

- Zero non-follower reach on all Reels for two consecutive weeks on one account: verify no unoriginal asset entered the set, verify Reel lengths, check Account Status. **No allocation change.**
- One account's reach exceeding the other's by >3x for two consecutive weeks: note it. This is the account effect being measured.
- Story reach flat or declining: record as supporting context. No action.
- Breakout post: record as ceiling / breakout evidence. Continue exactly as scheduled.

### Never, during the six posting weeks

Move effort between accounts · alter cell, format or slot allocation · change posting times · change display name, bio, profile photo, pinned posts or link in bio · change username · add or drop a cell · run paid promotion, giveaways, Collabs or advertiser outreach · attempt to replicate a breakout.

---

## 4. Confirmation of frozen matrix

**The 48-post matrix published in the previous response is unchanged and was intended to be executed in full across all six posting weeks.**

Confirmed intact at that stage:

- 24 posts per account, 48 total
- Per account: 12 Reels, 6 Carousels, 6 Static
- Per account: 6 posts per cell, of which exactly 3 Reels per cell
- Pooled per cell: 6 Reels, 3 Carousels, 3 Static
- Per account: 12 Early, 12 Late, with 3 Early and 3 Late in every cell
- Complementary A/B allocation producing exact pooled format balance
- Anti-duplication rules unchanged: no shared file, no shared subject within 14 days, 14-day topic check-out, distinct source imagery

Also unchanged at that stage: six posting weeks plus measurement tail, T+7 primary snapshots, T+14 Reel tail snapshots, medians as the principal decision statistic, Views separated from Reach, both accounts running simultaneously, four faceless content engines, weekly Account Status checks, the frozen-variable list, targeted legacy-counterfeit cleanup before Post #1, Week 8 as the decision point, the threshold table, the Scenario A–H decision tree, and the Week 0 checklist.

**Historical-status warning:** this methodology patch closed the 48-post experiment design at the time. The founders later superseded the 48-post execution matrix before launch by deciding on one feed post per day per account (84 posts over six weeks). Preserve this artifact as historical methodology; do not reactivate the 48-post matrix as the current plan.

---

## 5. Final gate at the time

# REVIVAL EXPERIMENT FULLY LOCKED — PROCEED TO WEEK 0

At that point no further methodology, strategy, or research round was required before Week 0 setup.

**Later supersession:** before the controlled experiment launched, the founders changed cadence to 1 feed post/day/account, making the 48-post execution matrix historical/superseded and leaving the 84-post matrix not yet designed.
