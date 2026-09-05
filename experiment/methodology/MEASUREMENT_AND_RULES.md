# Measurement Framework and Operating Rules — FOUNDER-LOCKED

**Status: ACTIVE.** These are the locked methodological principles for the 84-post controlled revival
experiment, as approved jointly by Sari and Wasim at Founder Lock.

The execution matrix they govern is `../active-84-post-plan/matrix_84.csv`.

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
**unknown**. See `../../strategy/historical/CORRECTIONS_LEDGER.md`, priority correction 2.

**Do not anchor on the 98.7% / 98.5% non-follower share in the passive baseline.** That is residual surfacing
of dormant content and predicts nothing about new-post distribution.

---

## 2. Snapshot protocol

- **T+7** for every feed post — the primary snapshot.
- **T+14** additionally for every Reel — the tail snapshot.
- **T+2** for every Story.
- **Fixed maturation age is the point.** Never compare a post measured at 40 days against one measured at 5.
- Account-level weekly: followers start/end · net change · reach · % non-follower · profile visits · external
  link taps · **Account Status across all five categories** · posts published by format · any Instagram
  notification.
- Full audience snapshot (countries, cities, age, gender) at Week 0 and at the decision point only — comparing
  those two is the only way to detect audience-composition drift.

---

## 3. Decision authority — PRIMARY read, and nothing else

**The PRIMARY READ is the sole decision authority for this experiment:** per-post, Reach-denominated medians
on **weeks 3–6**. It is the only basis for every account, engine, format and account × engine conclusion, and
the only input to the scenario tree.

- **Median is the decision statistic.** Distributions here are heavy-tailed; means are misleading.
- **Maximum is reported separately as ceiling evidence** and never moves an account from weak to strong.
- A breakout post is recorded and **changes nothing in the schedule.** No replication attempt until the
  locked test completes.

### The engine-win rule

- **Declared engine win:** the engine's pooled median on its primary metric is **≥ 2× the next-best engine**,
  evaluated in the weeks 3–6 window (n = 14 per engine), **and** the same direction holds on both accounts.
- **An engine that dominates on only one account is an account × engine result, not an engine effect**, and is
  never generalised.
- **Sub-2× separations are reported descriptively, with no cutoff of any kind.** Report all four engines'
  pooled medians, their per-account medians, the min/median/max spread, the rank order and the exact ratio to
  the next-best engine. Any separation below 2× is labelled **not declared** and carries **no decision
  authority** — it may inform what to test after the decision point, never what to conclude at it.

⚠ **There is no 1.7× threshold and no other sub-2× cutoff.** An earlier draft proposed one derived by √n
scaling; it was **removed before lock**. That scaling governs the standard error of a *mean* under regularity
conditions, not the median of a heavy-tailed distribution, and compounding it with an already-uncalibrated 2×
judgement produced false precision. The increase in n from 12 to 21 pooled raises confidence *in* the 2× rule;
it does not license a lower one.

### The same discipline applies to format comparisons.

---

## 4. Rule S — the weekly account-level safeguard is REMOVED

An earlier draft proposed a "secondary safeguard": weekly account-level Reach and non-follower Reach compared
against a Week-0 dormant baseline, able to veto a Scenario H conclusion. **It was removed before lock.**

1. **The weekly account-level Reach / non-follower Reach safeguard has no decision authority of any kind.** It
   cannot veto, create, upgrade, downgrade, qualify or delay any verdict. Weekly account-level Reach and
   non-follower Reach are still **recorded** in the account-weekly rows and appear in the final report as
   descriptive context only.

   **Why removed:** with 1 Story per day per account, weekly account-level Reach aggregates 42 Stories and 42
   feed posts per account against a dormant baseline containing neither. The increase is not attributable to
   the feed, and no defensible attribution rule exists with the available instrumentation. Inventing a
   numerical correction for Story contribution was explicitly rejected.

2. **Scenario H remains as canonically defined** — both accounts Weak on all reach thresholds, **and** no
   engine separation ≥2×, **and** non-follower share below the Weak boundary — and may be declared **only**
   when all three conditions hold on the primary per-post data for weeks 3–6. The non-follower-share condition
   is evaluated on its own terms and is never inferred from the reach-rate bands.

3. **Scenario H is already cadence-robust, which is why no safeguard is needed.** Its non-follower-share
   condition is **Reach-denominated**. Publishing more posts divides the same audience appetite across more
   posts and lowers reach *per post*; it does not mechanically lower the *fraction* of each post's reach that
   comes from non-followers. *(Structural argument, not an empirical finding — labelled as such.)*

4. **Mandatory dilution note — a recording rule, not a decision rule.** If an account is Weak on the format
   reach-rate bands but its weeks 3–6 median non-follower share of Reels reach is **not** Weak, the final read
   must contain this sentence: *"The per-post reach-rate bands were imported from a 4-post/week/account design
   and are not calibrated for 7/week; this account fails the rate bands but not the discovery metric."* No
   threshold, no verdict change.

5. **Residual-case rule.** If an account's results satisfy no scenario definition exactly, it is reported as
   **unclassified** with the observed values. **Scenario H may never be used as a default bucket** for results
   that do not meet its definition.

6. The Week-0 weekly account Reach / non-follower Reach baseline is still **captured** — it is cheap and
   useful descriptive context — but it is **not a launch-gate blocker**, because no decision depends on it.

---

## 5. Originality standard

**Zero unoriginal/reposted feed posts during the controlled experiment.** The rationale, as corrected:

1. **Clean attribution** — a repost measures someone else's content, not the production system.
2. **A suppressed or replaced post wastes a matrix slot** and returns no usable measurement.
3. **The experiment is partly a capability test** — whether two people can produce original content at
   cadence. A repost is a skipped rep.
4. **It removes interpretive ambiguity.**
5. **Margin of safety** — zero against a threshold of ten means judgement errors about "materially enhanced"
   never accumulate toward the wall.

**Not** because one repost makes the account globally ineligible. **It does not.** Account-level eligibility
turns on *repetition* (10+ unoriginal posts in 30 days) with recovery applying only to accounts that already
crossed that threshold; post-level treatment is independent and judges the file. See the corrections ledger.

**Handling a violation** and every other failure case: `../active-84-post-plan/EXCEPTION_PROTOCOL.md`.

**AI-generated imagery is not a repost** and is permitted only in the six locked C4 slots, under
`../active-84-post-plan/AI_IMAGERY_SUBTEST.md`. Anywhere else it is a protocol violation.

---

## 6. Frozen variables

**Frozen for the duration**, on both accounts: username · display name · bio · profile photo · **link in bio
(none)** · pinned posts · highlights · **publish instant** · comment-reply policy · follow/unfollow activity ·
editorial role · historical feed · hashtag policy · Reel duration band · carousel slide-count band · C2
ranked-item count · house templates · **Story cadence, timing and structure**.

**Prohibited for the duration:** paid promotion · giveaways · Collabs · advertiser outreach · cross-posting ·
**voiceover** · AI imagery outside the six locked slots · adding or dropping an engine · moving effort between
accounts · replicating a breakout.

**No performance-based adaptation at any point.** All six posting weeks are frozen. The full list is in
`../active-84-post-plan/LOCK_SPECIFICATION.md` §1.

---

## 7. Checkpoints

**Weekly review** — same day and time each week, both founders. Screenshot Account Status on both accounts;
log every post that crossed T+7 and every Reel that crossed T+14; update account-weekly rows; confirm the
buffer holds ≥7 finished pieces; confirm next week's pieces are produced and scheduled. **No strategy
discussion inside the weekly review.**

**Mid-test checkpoint** — diagnostic, safety and data-quality only. **No allocation decision may be taken.**
Covers Account Status; any IP or removal notice; any Instagram metric change; any unoriginal asset published;
any frozen variable inadvertently changed; any prohibited activity; planned versus actually published; matrix
conformance; publish times; tracking-sheet completeness; T+14 Reel snapshots; Reach used as denominator
everywhere; post-ID convention; **that every topic check-out took the top eligible item**; and **that AI
imagery appears only in the six locked slots**. Observations about which engines or account look stronger are
**recorded, not acted on**.

**Decision point** — at the end of the measurement tail, on medians from weeks 3–6.

---

## 8. Stop, extend and investigate rules

Full table: `../active-84-post-plan/EXCEPTION_PROTOCOL.md`. The hard stops:

- **Any Account Status category leaving green on either account** — pause that account, screenshot the flagged
  item and the exact guideline named, request review if offered, continue the other account.
- **Any content-removal notice or IP report** — pause both, investigate before resuming.

**Extend rather than unbalance.** Missed posts are recovered preserving account, engine, format, weekday and
instant; if recovery falls outside the posting weeks, **extend the calendar**. Production below 80% of plan →
extend rather than analyse an incomplete matrix. *An extended calendar is preferable to an unbalanced dataset.*

**Data failure:** record exactly what is unavailable and from which date, capture whatever substitute
Instagram provides, note the affected rows. **Do not back-fill estimates. Do not change the posting plan.**

---

## 9. What the experiment is designed to isolate

Three effects: **account**, **format** and **content engine**, plus the **account × engine interaction** as a
guard against generalising an account-specific result.

**If an engine only dominates on one account, it is not an engine effect.**

The design removes confounds; **it does not manufacture statistical power.** Sample sizes, residual confounds
and the cadence caveat on the absolute threshold bands are stated in
`../active-84-post-plan/LOCK_SPECIFICATION.md` §5–§6.

---

**Stories** are governed entirely by `STORY_PROTOCOL.md`. They are diagnostic, gate nothing, and appear in no
scenario definition.
