# Revival Experiment — Patch and Freeze

## 1. Final corrections

### Correction 1 — Originality rule: account-level vs post-level

**What was wrong.** I acknowledged the first-party rule correctly, then operationally treated a single unoriginal post as if it would make the account ineligible and reset a 30-day clock. That conflated two separate mechanisms.

**Corrected interpretation.**

*Account-level eligibility.* The first-party criterion is repetition: accounts that repeatedly post content from other users they didn't create or enhance in a material way — 10 or more times in the last 30 days — are not shown in recommendation surfaces. The recovery mechanism applies **to accounts that have already crossed that threshold**: they become eligible again once 30 days have passed since the last time they posted unoriginal content, and status is visible in Account Status. Both your accounts are currently green, so neither is in a recovery state, and the 30-day clock is not something a clean account "resets."

*Post-level treatment.* Separately and independently, an individual unoriginal post can be replaced by the original in recommendations, labelled with credit to the first poster, or deprioritised by near-identical detection — which judges the file, not the account. This happens without any account-level consequence.

**Exact experiment consequence.** The zero-repost operating rule stands unchanged. The rationale changes:

1. **Clean attribution.** A repost's performance measures someone else's content, not your production system. It answers no question the experiment asks.
2. **Post-level penalty wastes a slot.** A suppressed or replaced post occupies a matrix cell and returns no usable measurement.
3. **The experiment is partly a capability test.** You are finding out whether two people can produce original content at cadence. A repost is a skipped rep.
4. **Removes interpretive ambiguity.** If reach is weak and there were reposts in the set, you cannot tell which caused it.
5. **Margin of safety.** Zero against a threshold of ten means judgment errors about what counts as "materially enhanced" never accumulate toward the wall.

Not because one repost makes the account globally ineligible. It does not.

**Downstream changes:** an unoriginal post is now a **protocol violation, not an emergency**. It is not a hard stop, does not invalidate the test, and does not require pausing. See §6 for the replacement handling rule. All "resets the clock" language is removed.

---

### Correction 2 — Follower liveness

**What was wrong.** I computed 90-day Viewers ÷ followers to claim \~2.3% (A) and \~3.7% (B) follower liveness. That's invalid on its own face: 98.7% and 98.5% of those views came from non-followers, so the numerator is overwhelmingly *not followers*. I then compounded it by deriving a "low hundreds of reachable US followers" figure from it.

**Corrected interpretation.** Both figures are withdrawn, along with every claim built on them. **The active fraction of each follower list is unknown.** The passive data tells you that residual old content gets occasional non-follower surfacing; it tells you nothing about how many followers are still there.

**Exact experiment consequence.**

- "Living-follower rate" is deleted as a metric name and as a concept.
- Replaced by two clearly separated measures in §4.
- Stories move from a threshold gate to a **supporting diagnostic**. They no longer appear in any pass/fail rule.
- Decision tree: Story performance is removed from all scenario definitions. Scenarios A–H were defined on reach rate, non-follower share and follower growth, none of which used the withdrawn figures — so the tree stands as written, with Story data used only as supporting context when reading it.
- Experiment objective is narrowed accordingly: this experiment tests whether the accounts can obtain **distribution**. It gives a partial, not definitive, read on how much of the legacy follower base survives.

---

### Correction 3 — The matrix did not control format

**What was wrong.** My allocation gave C1 3R/2C/1S, C2 2R/2C/2S, C3 3R/1C/2S, C4 4R/1C/1S. C4 received the most Reels — the highest-reach format. If C4 had won, "better engine" and "more exposure to the better format" would have been inseparable. "Every cell appears in every format" is not balance.

**Corrected design.** Rebuilt as a complementary two-account design. Pooled across both accounts, **every cell receives exactly 6 Reels, 3 Carousels and 3 Static** — mathematically perfect balance, no rounding residual.

Per account, integer constraints force asymmetry, resolved complementarily:

| Cell Account A Account B **Pooled**  |              |              |                  |
| ------------------------------------ | ------------ | ------------ | ---------------- |
| C1                                   | 3R / 2C / 1S | 3R / 1C / 2S | **6R / 3C / 3S** |
| C2                                   | 3R / 2C / 1S | 3R / 1C / 2S | **6R / 3C / 3S** |
| C3                                   | 3R / 1C / 2S | 3R / 2C / 1S | **6R / 3C / 3S** |
| C4                                   | 3R / 1C / 2S | 3R / 2C / 1S | **6R / 3C / 3S** |

Note the critical property: **every cell gets exactly 3 Reels on every account.** That makes the Reels subset a fully balanced 2 × 4 design and is what rescues the interaction test (see §2 analysis notes).

---

### Correction 4 — Posting slot was welded to account

**What was wrong.** A permanently at 19:00 and B at 19:45 makes slot and account identity inseparable. My justification — that simultaneous posting would make overlapping audiences compete — was asserted without evidence.

**Corrected design.** Two fixed slots inside the evening window, **counterbalanced**. Each account receives exactly 12 Early and 12 Late. Balance holds within every cell (3E/3L per cell per account) and within every format (Reels 6E/6L, Carousels 3E/3L, Static 3E/3L per account). Time remains a control variable and is not added as an experimental factor. Exact assignment is in the matrix.

---

## 2. FINAL LOCKED 48-POST MATRIX

Four matched publishing events per week (Day 1–4). Both accounts publish on the same four days. Within each event, one account takes Early and the other takes Late.

### Account A — `thestreetwearofficial`

| Wk Day Cell Format Slot  |   |    |          |       |
| ------------------------ | - | -- | -------- | ----- |
| 1                        | 1 | C2 | Reel     | Late  |
| 1                        | 2 | C1 | Carousel | Early |
| 1                        | 3 | C4 | Reel     | Early |
| 1                        | 4 | C3 | Static   | Early |
| 2                        | 1 | C2 | Reel     | Early |
| 2                        | 2 | C1 | Carousel | Late  |
| 2                        | 3 | C3 | Reel     | Early |
| 2                        | 4 | C4 | Static   | Early |
| 3                        | 1 | C1 | Reel     | Late  |
| 3                        | 2 | C2 | Carousel | Late  |
| 3                        | 3 | C4 | Reel     | Late  |
| 3                        | 4 | C3 | Static   | Late  |
| 4                        | 1 | C1 | Reel     | Late  |
| 4                        | 2 | C2 | Carousel | Early |
| 4                        | 3 | C3 | Reel     | Early |
| 4                        | 4 | C4 | Static   | Late  |
| 5                        | 1 | C2 | Reel     | Early |
| 5                        | 2 | C3 | Carousel | Late  |
| 5                        | 3 | C4 | Reel     | Late  |
| 5                        | 4 | C1 | Static   | Early |
| 6                        | 1 | C1 | Reel     | Early |
| 6                        | 2 | C4 | Carousel | Early |
| 6                        | 3 | C3 | Reel     | Late  |
| 6                        | 4 | C2 | Static   | Late  |

### Account B — `sneakerbong`

| Wk Day Cell Format Slot  |   |    |          |       |
| ------------------------ | - | -- | -------- | ----- |
| 1                        | 1 | C2 | Reel     | Early |
| 1                        | 2 | C3 | Carousel | Late  |
| 1                        | 3 | C4 | Reel     | Late  |
| 1                        | 4 | C1 | Static   | Late  |
| 2                        | 1 | C1 | Reel     | Late  |
| 2                        | 2 | C3 | Carousel | Early |
| 2                        | 3 | C4 | Reel     | Late  |
| 2                        | 4 | C2 | Static   | Late  |
| 3                        | 1 | C2 | Reel     | Early |
| 3                        | 2 | C4 | Carousel | Early |
| 3                        | 3 | C3 | Reel     | Early |
| 3                        | 4 | C1 | Static   | Early |
| 4                        | 1 | C1 | Reel     | Early |
| 4                        | 2 | C4 | Carousel | Late  |
| 4                        | 3 | C3 | Reel     | Late  |
| 4                        | 4 | C2 | Static   | Early |
| 5                        | 1 | C2 | Reel     | Late  |
| 5                        | 2 | C1 | Carousel | Early |
| 5                        | 3 | C4 | Reel     | Early |
| 5                        | 4 | C3 | Static   | Late  |
| 6                        | 1 | C1 | Reel     | Late  |
| 6                        | 2 | C2 | Carousel | Late  |
| 6                        | 3 | C3 | Reel     | Early |
| 6                        | 4 | C4 | Static   | Early |

### Balance verification

| Check A B Pooled          |               |               |                 |
| ------------------------- | ------------- | ------------- | --------------- |
| Posts                     | 24            | 24            | 48              |
| Format totals             | 12R / 6C / 6S | 12R / 6C / 6S | 24R / 12C / 12S |
| Posts per cell            | 6 each        | 6 each        | 12 each         |
| Reels per cell            | 3 each        | 3 each        | 6 each          |
| Slot totals               | 12E / 12L     | 12E / 12L     | 24E / 24L       |
| Slot per cell             | 3E / 3L each  | 3E / 3L each  | 6E / 6L each    |
| Cell appearances per week | 1 each        | 1 each        | —               |

### How each effect is estimated

**1. Account effect** — A's 24 posts vs B's 24. Both accounts carry identical format totals, identical cell totals, and identical slot totals. **Cleanly estimable.**

**2. Format effect** — 24 Reels vs 12 Carousels vs 12 Static, pooled. Each format is balanced across cells (every cell contributes 6R/3C/3S), across accounts, and across slots. **Cleanly estimable.**

**3. Content-cell effect** — 12 posts per cell, pooled. Every cell carries an identical format mix, an identical 6/6 account split, and an identical 6E/6L slot split. **Cleanly estimable.** This is the primary analysis and it is the one Correction 3 was needed to make valid.

**4. Account × cell interaction — partially confounded, with a clean workaround.** Within a single account, cell and format are not orthogonal: C1 and C2 carry 2 carousels and 1 static on A but 1 and 2 on B. So an overall interaction test would be contaminated by format. **However, every cell has exactly 3 Reels on every account**, making the Reels subset a fully balanced 2 × 4 design at n = 3. **Run the interaction test on Reels only.** Reels are also the format that matters most for the discovery question.

### Declared residual limitations

- **Within-account cell rankings on carousels and static** carry a one-post format imbalance. Use pooled cell rankings for any conclusion; treat within-account non-Reel rankings as indicative only.
- **Statistical power is low by construction.** 12 posts per cell pooled, 3 per account × cell × Reels. Only differences of roughly 2x or larger are readable above noise. This design removes a confound; it does not manufacture power. The ≥2x comparative rule in §5 exists precisely because of this.
- **Format × slot within a cell** cannot be perfectly balanced with 3 Reels per cell per account (2/1 splits). Third-order given a 45-minute offset; noted, not corrected.
- **Anti-duplication rules are unchanged and remain binding:** never the same file on both accounts; never the same specific subject on both accounts within 14 days; topics checked out to one account and locked for 14 days; different source imagery on every piece.

---

## 3. Final posting-time protocol

**Two slots, both inside the observed evening activity window (18:00–21:00 GMT+3):**

- **Early — 19:00 GMT+3**
- **Late — 19:45 GMT+3**

**Counterbalancing rule.** Each publishing event is matched: both accounts post on the same day, one Early and one Late. Assignment follows the Slot column in the matrix above, which was constructed so that each account receives exactly 12 Early and 12 Late, with 3 Early and 3 Late inside every content cell and balanced within every format. **Neither account owns a slot, and no cell is systematically advantaged.**

**Rationale for keeping the two slots rather than posting simultaneously.** With slot now counterbalanced, the account/slot confound is gone either way. Retaining two slots simply preserves a small hedge against overlapping-audience effects at zero methodological cost. The earlier claim that this competition effect is material is withdrawn — it is unevidenced, and the design no longer depends on it.

**Stories.** Posted daily-window consistent at **20:30 GMT+3 on both accounts**, 3 per week each, identical structure, one interactive sticker per week from week 1. Stories are outside the counterbalanced matrix because they are diagnostic, not part of the primary analysis.

**Frozen.** The two clock times, the four publishing days per week, the Story time, and the slot assignments in the matrix. Time is a control variable. "Best posting time" is not tested in this experiment and is a candidate follow-up only after week 8.

---

## 4. Final metric definitions

Only definitions affected by this patch. Everything else from the previous framework stands.

| Term Definition Use           |                                                                                                                                                                                         |                                                                                                                                                  |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Views**                     | Plays or displays including repeats. Not unique. Instagram replaced Plays/Impressions with Views in April 2025.                                                                         | Recorded for every post. **Never a denominator.** Never divided by follower count.                                                               |
| **Reach**                     | "Accounts reached" — unique accounts.                                                                                                                                                   | **The denominator for every rate metric in this experiment.**                                                                                    |
| **Non-follower reach**        | The non-follower portion of Accounts reached, as reported by Instagram.                                                                                                                 | Primary discovery metric. Expressed as % of reach.                                                                                               |
| **Follower reach**            | The follower portion of Accounts reached, as reported by Instagram.                                                                                                                     | Recorded per post. The only legitimate basis for any statement about follower-base responsiveness.                                               |
| **Story reach**               | Accounts reached by a Story.                                                                                                                                                            | Recorded for all Stories.                                                                                                                        |
| **Story follower-reach rate** | (Story reach from followers) ÷ current follower count. **Only computed if Instagram exposes the follower/non-follower split on Story insights.** Verify in Week 0.                      | Diagnostic. Best available estimate of follower responsiveness — still an estimate, since it measures who was served and viewed, not who exists. |
| **Story reach rate**          | Total Story reach ÷ follower count. Used **only** if the follower split is unavailable.                                                                                                 | Internal engagement baseline for longitudinal comparison. **Explicitly not a percentage of "living followers."** Never quoted as such.           |
| \~\~Living-follower rate\~\~  | **Removed.** Not directly measurable with available instrumentation. Any number produced this way would be a non-follower artefact, which is exactly the error Correction 2 identifies. | —                                                                                                                                                |

**Standing rule:** no metric in this experiment may use total followers as a denominator unless its numerator is a follower-specific figure reported by Instagram. The one deliberate exception is format reach rate (§5), which is retained because the external benchmarks are constructed the same way — and is labelled accordingly.

---

## 5. Final threshold table

### Reach rate by format — Reach ÷ followers, median of weeks 3–6

| Format Benchmark Weak Promising Strong  |                                                                                                                               |        |           |       |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | ----- |
| Reels                                   | \~7.1% *(****External benchmark****, founders' cited Socialinsider 10K–50K figure;* ***not independently verified by me****)* | <2.0%  | 2.0–5.0%  | >5.0% |
| Carousels                               | \~6.4% *(same status)*                                                                                                        | <1.75% | 1.75–4.5% | >4.5% |
| Static                                  | \~5.5% *(same status)*                                                                                                        | <1.5%  | 1.5–4.0%  | >4.0% |

Bands: **Internal decision rule**, set at roughly 30% and 70% of the cited benchmark.
**Hypothesis** behind the discount: an account dormant for years should not be expected to reach active-account benchmark parity within six weeks; requiring parity would produce a false negative and kill a live asset.
*Shape corroboration (****External benchmark****): Socialinsider states Reels lead reach up to 50K followers, above which carousels take over — placing both accounts in the tier where Reels are the reach engine.*

### Non-follower share of Reels reach — median weeks 3–6

| Threshold  |        |
| ---------- | ------ |
| Weak       | <25%   |
| Promising  | 25–55% |
| Strong     | >55%   |

**Internal decision rule.** Loose supporting context (**Hypothesis**, weak source, different denominator): platform-level reporting suggests roughly 55% of Reels views come from non-followers.

**This remains the single most important metric in the experiment.** It is the direct test of whether recommendation distribution is available.

**Reading rule:** do not anchor on the 98.7% / 98.5% non-follower share in the passive data. That is residual surfacing of dead content and predicts nothing about new-post distribution.

### Follower growth

| Threshold  |                                       |
| ---------- | ------------------------------------- |
| Weak       | Still net negative at end of week 6   |
| Promising  | Net positive but <+1%/month           |
| Strong     | >+1%/month sustained across weeks 4–6 |

**Internal decision rule.** Context (**External benchmark**): only 21% of accounts under 10,000 followers grew at all in 2026. Current baseline decay: A ≈ –85/month, B ≈ –63/month.

### Saves per reach and sends per reach

**Internal decision rule, comparative only. No absolute threshold.** A cell wins a metric only if its pooled median is **≥2x the next-best cell**.

Context (**External benchmark**): Socialinsider's measured save rates are 0.05% for carousels, 0.04% for Reels and 0.02% for images — one to two orders of magnitude below commonly quoted targets, with a median of one save per post at this account size. This is why no absolute save threshold is set.

### Stories — **Diagnostic only. No pass/fail gate.**

I did not find a verified Story reach benchmark for the 10K–50K tier. The figures I saw elsewhere (e.g. a \~7.5% Story reach aspiration for smaller brands) come from a top-quartile brand sample, are dated, and are not tier-matched — not a valid comparator, and I'm not adopting it.

My previous <3% / 3–8% / >8% bands were **internal hypotheses presented with unearned authority**. They are withdrawn.

Stories are interpreted three ways only:

1. **Longitudinally within each account** — is Story reach trending up as posting resumes?
2. **Account A vs Account B** — same cadence, same structure, same time.
3. **Weeks 1–2 vs weeks 3–6** — does follower responsiveness recover with consistent posting?

Stories inform the read. They do not gate any decision and appear in no scenario definition.

### Recommendation eligibility

**Binary. Internal decision rule.** Any change from green in any of the five Account Status categories triggers §6.

### Explicitly diagnostic only — no thresholds

**Profile visits per reach** and **follows per profile visit.** No credible benchmark exists. Read directionally: flat profile visits indicates a content problem; profile visits up with follows flat indicates a profile problem.

---

## 6. Corrected early-stop and adaptation rules

Week 4 gate and weeks 5–6 adaptation window are preserved. Only the rules touched by the corrections change.

### Hard stop — any time

- **Account Status changes from green in any category on either account.** Pause that account immediately, screenshot the flagged item and the exact guideline named, request review if offered. Continue the other account; the paused account's series ends at that date.
- **Any content removal notice or IP report.** Pause both, investigate before resuming.

**Removed from hard stop:** a single unoriginal post. It is not an emergency and does not appear here.

### Protocol violation — unoriginal post published *(new, replaces the old hard-stop language)*

1. Log it. Do not delete it in a panic — deletion adds an unrecorded account-state change mid-measurement.
2. **Exclude that post from all analysis.** It measures someone else's content.
3. **Replace the slot** — publish a replacement in the same cell and format within 7 days so the matrix stays balanced. If the replacement would fall outside the six posting weeks, mark that matrix cell as missing and note the resulting imbalance in the final read.
4. Escalation threshold: **3 or more unoriginal posts on one account within any 30-day window** triggers a review of production process and content-selection judgment. This sits well below the first-party threshold of 10 and exists as an early-warning margin, not because 3 carries any platform consequence.
5. Do not pause the account. Do not restart any clock. Neither account is in a recovery state.

### Investigate — keep posting

- **Zero non-follower reach on all Reels for two consecutive weeks on one account.** Verify no unoriginal asset entered the set; verify Reels sit in the 30–60 second band, which produced the highest reach rate at 5.60%, and that none exceed 3 minutes since those are not recommended to non-followers; check Account Status.
- **One account's reach exceeds the other's by >3x for two consecutive weeks.** Note it. Do not act. This is the account effect being measured.
- **Story reach flat or declining across weeks 3–6 on both accounts.** Log as supporting context for the week 8 read. **Not a trigger for any action** — Stories no longer gate anything.

### Week 4 gate — adaptation permitted in weeks 5–6 only

Unchanged in logic, with one balance clause added.

- **Double down:** if a cell's pooled median on its primary metric is ≥2x the next-best cell after week 4, that cell may take one extra Reel slot per account per week, taken from the lowest cell.
- **Drop a cell:** if a cell's pooled median reach rate is <40% of the overall median after week 4, drop it for weeks 5–6.
- **New balance clause.** Any adaptation must be applied **identically and symmetrically to both accounts**, and both weeks 5 and 6 must be adapted the same way. Weeks 1–4 (32 posts, fully balanced) are then analysed as the primary balanced dataset, and weeks 5–6 analysed separately as a confirmatory unbalanced extension. State this split in the final read rather than pooling adapted and unadapted weeks.

### Extend

- Production below 80% of plan → extend posting to week 8 rather than analyse an incomplete matrix.
- A post exceeding 50x the running median reach in weeks 5–6 → extend two weeks to test repeatability. This changes the schedule, never the verdict.

### Never, mid-test

Move effort between accounts · change posting slots or times · change display name, bio, profile photo, pinned posts · add a fifth cell · run paid promotion, giveaways, Collabs, or advertiser outreach · change username.

---

## 7. Final experiment verdict

# REVIVAL EXPERIMENT LOCKED — READY FOR WEEK 0

**No further strategic or research round is required before Week 0 setup.**

All four methodological issues are corrected and propagated. The 48-post matrix is fully specified and balanced: cell effect and format effect are now genuinely orthogonal in the pooled analysis, account × cell interaction is cleanly estimable within the Reels subset, and posting slot is counterbalanced against account, format and cell. The originality rule is stated at first-party precision with post-level and account-level mechanics separated. The invalid liveness inference and everything derived from it are withdrawn, and Stories are demoted to a supporting diagnostic with no gating power.

Everything preserved from the previous lock — six posting weeks plus measurement tail, T+7 primary and T+14 Reel snapshots, medians as the decision statistic, Views separated from Reach, both accounts running simultaneously, four faceless content engines, weekly Account Status checks, the frozen-variable list, targeted legacy-counterfeit cleanup before Post #1, the Week 4 gate and Week 8 decision, and the Week 0 checklist — stands unchanged.

Two things I am not going to soften on the way out. The design now removes confounds but does not add statistical power; at 12 posts per cell only large differences are readable, which is why every cell comparison runs through the ≥2x rule. And the binding risk remains execution, not methodology: 48 original pieces in six weeks from a team that has not produced original content at volume. If week 1's eight pieces are not finished and scheduled before week 1 begins, cut to 3 posts per account per week and rebuild the matrix at that cadence rather than starting and slipping.

Next action is Week 0 setup. Nothing further to plan.