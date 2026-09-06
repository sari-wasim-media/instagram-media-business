# Decision Register

Founder decisions and their status. **This file is authoritative on what was decided.**

| Status | Meaning |
|---|---|
| **ACTIVE** | In force now |
| **SUPERSEDED** | Was in force; replaced by a later decision |
| **DEFERRED** | Deliberately not decided yet |
| **HISTORICAL** | A fact about the past that shapes current constraints |

⚠ **Historical AI analysis is not a decision.** The recovered strategy documents contain recommendations.
A recommendation appears here only where the founders adopted it. Where a decision originated as an advisory
recommendation, that is stated.

---

## Business constraints

### Founders remain faceless — **ACTIVE** · FIXED CONSTRAINT
Neither Sari nor Wasim will appear on camera, appear in published photographs or video, become the public
personality behind either account, or rely on founder-as-influencer positioning. The business must work as a
faceless media brand.

**Rationale:** founder preference, stated as non-negotiable from the outset.

**Scope limit — read this before extending the rule.** The constraint covers visual appearance and
public-personality positioning. It does **not** by itself prohibit voiceover. See the separate entry below.

### No voiceover during the controlled experiment — **ACTIVE** (Founder Lock)
**Decided jointly by Sari and Wasim.** No content piece in the 84-post experiment uses voiceover. All 48 Reels
run a uniform non-voiceover production method: text-on-screen with licensed or royalty-free audio. AI-generated
voice is prohibited for the same reason and separately by the AI sub-test rules.

**Rationale:** holds production method constant across all 48 Reels. A mixed method would be an uncontrolled
variable correlated with whoever produced the piece.

⚠ **Test-specific, not a permanent business prohibition.** This settles the experiment, not the business
question. Voiceover, text-on-screen narration and a named editorial persona remain compatible with the faceless
constraint, and voiceover may be revisited after the decision point. Prior analysis
(`strategy/research/PHASE_1_PHASE_2_REPORT.md` §9, `experiment/historical-48-post-design/REVIVAL_EXPERIMENT_FINAL_LOCK.md` §5)
considered it viable — *"faceless does not mean voiceless"* — and that analysis is unaffected.

### Replica / counterfeit / UA advertisers permanently excluded — **ACTIVE** · FIXED CONSTRAINT
A standing exclusion, not a per-deal judgement. Extended by research to also exclude bot and proxy vendors for
sneaker copping, follower-growth and engagement services, crypto/NFT-adjacent, gambling, dropship arbitrage,
and anything paying above market rate — that premium is itself a risk signal.

**Rationale:** IP-enforcement exposure (repeat infringement can disable an account), audience trust, and the
historical exposure this business is deliberately leaving behind.

### No reckless automation — **ACTIVE** · FIXED CONSTRAINT
Official Meta/Instagram-compatible methods only. No grey automation, private APIs, mass-spam behaviour or
botting. Advertiser vetting, brand-safety judgement, pricing, negotiation, contract terms and account access
remain permanently manual.

### No business implementation through Claude Code yet — **ACTIVE**
Claude Code's authorised scope to date is **documentation and repository migration only**. No automation, no
dashboards, no tracking software, no publishing tooling has been built or authorised.

*Clarification, 2026-09-06.* The founder-approved Creative System sprint authorised, and produced,
**in-repository production aids**: read-only validators of committed CSVs (`tools/validate_provenance.py`,
`tools/validate_backlog.py`), a generator of the tracking-sheet skeleton from the matrix
(`tools/build_tracking_sheet.py`), a local calendar printer (`tools/instantiate_calendar.py`) and a specimen
renderer (`production/templates/src/render_frames.py`). They are of the same kind as
`tools/validate_matrix.py`: they read and write files in this repository and print. **They are not publishing
tooling, dashboards, scrapers or automation, which remain unauthorised.** The tracking sheet itself is a
manual spreadsheet.

---

## Platform and content policy

### The historical repost-heavy model is not the future model — **ACTIVE**
Future content is original or materially enhanced, and rights-safe.

### Zero unoriginal/reposted feed posts during the controlled experiment — **ACTIVE**
**Rationale, as corrected:** clean attribution; a suppressed post wastes a matrix slot; the experiment is
partly a test of whether the team can produce original content at cadence; reposts create interpretive
ambiguity; and zero against a threshold of ten is a margin of safety.

⚠ **Not** because one repost makes the account globally ineligible — it does not. Account-level eligibility
turns on repetition (10+ in 30 days) with recovery applying only to accounts that already crossed the
threshold; post-level treatment is independent and judges the file. An earlier project document states this
wrongly — see `strategy/historical/CORRECTIONS_LEDGER.md`.

**Handling:** an unoriginal post is a protocol violation, not an emergency. Log, exclude from analysis,
replace the slot, do not pause, no clock resets.

### No mass deletion of the historical feed — **ACTIVE**
**Rationale:** originality is assessed on a rolling recent window, so old posts have no effect on
recommendation eligibility. Deleting them would destroy engagement history and social proof to fix a problem
that does not exist.

### Targeted UAPLG / counterfeit cleanup — **ACTIVE** (executed) · HISTORICAL FACT
Three specific promotional posts meeting both removal criteria were documented (post **and** Insights
screenshots) and removed before Post #1. Highlights were checked afterwards and found clean of the identified
material. Both accounts remained green.

⚠ **Targeted, not general.** This does not support any claim that all historical content was cleaned.

### 2FA enabled on both accounts — **ACTIVE** (executed) · HISTORICAL FACT
Week 0 security task complete. **Recovery codes must never be stored in this repository.**

---

## Profile

### Minimal bio edit before Post #1 — **ACTIVE** (executed, founder-confirmed)
**The follower-target / follower-goal line was removed from the bio on both accounts.** The rest of each bio
was kept substantially unchanged, and no other material bio rewrite was made. No username changes.

**Rationale:** the founders chose a deliberately minimal edit over a rewrite.

**Evidence status:** the surrounding profile state is screenshot-evidenced pre-change
(`evidence/profile-baseline/`); the removal itself is founder-confirmed but not separately screenshot-verified
after the edit. A post-change capture is an optional improvement, not a blocker.

### Proposed full bio rewrite — **SUPERSEDED** (never applied)
An earlier draft proposed replacing both bios and display names with rewritten versions. **The founders did
not apply them.** They are recorded here only so they are not mistaken for the current state or revived as an
outstanding task. See `PROJECT_STATE.md`.

### Display names unchanged — **ACTIVE** (founder-confirmed)
Neither display name was changed: *"streetwear life"* on `thestreetwearofficial`, *"Sneakerbong"* on
`sneakerbong`, as shown in `evidence/profile-baseline/`. The proposed replacement display names belonged to
the rewrite that was never applied and are **not** canonical. Display names are a frozen profile variable for
the duration of the controlled experiment.

### Usernames unchanged during the initial test — **ACTIVE**
**Rationale:** renaming mid-test makes any reach change unattributable. No evidence was found that Instagram
penalises either name.

### Profile variables frozen during the controlled experiment — **ACTIVE**
Username, display name, bio, profile photo, link in bio (**none**), pinned posts, highlights, publish instant,
comment-reply policy and follow/unfollow activity are all frozen for the duration.

**Rationale:** every one of them is an unmeasured variable that would contaminate the profile-visit → follow
read. Any change belongs before Post #1 or after the decision point, never mid-measurement.

### No link in bio during the controlled experiment — **ACTIVE** (Founder Lock)
**Decided jointly by Sari and Wasim: no link in bio for the duration of the test.** Both bios already route
business contact through DM; bio link taps read zero across the 90-day dormant baseline; and adding one would
change a frozen profile variable and introduce a metric outside the primary read.

This closes the historical Week 0 checklist item, which is now **decided, not deferred**. See
`evidence/WEEK_0_CHECKLIST_STATUS.md`. Revisit after the decision point if wanted.

### `sneakerbong` rename — **DEFERRED**
Not renaming before revival evidence exists.

**Rationale:** a rename now would confound the experiment. No evidence Instagram penalises the name; the
brand-safety concern applies mainly to large advertisers running formal review, who are not the realistic
near-term buyers. If revisited, the criterion should be whether the name describes a media product a business
would buy from — not the word "bong".

---

## Experiment

### Both accounts tested concurrently; no winner chosen in advance — **ACTIVE**
Same cells, same structure, different topics and assets. **Editorial roles are an output of the experiment,
not an input** — assigning roles now would destroy the account comparison.

### Six posting weeks plus measurement tail — **ACTIVE**

### The 48-post matrix — **SUPERSEDED BEFORE LAUNCH**
Fully designed, corrected across four generations, balanced and locked at 4 feed posts/week/account (24 per
account, 48 total). **Never launched. Zero posts published under it.**

**Superseded by:** the cadence decision below. Preserved as historical methodology at
`experiment/historical-48-post-design/`.

### Current cadence: 1 feed post/day/account — **ACTIVE**
7 feed posts/week/account · 14 combined/week · 6 posting weeks · **84 feed posts total** (42 per account).

**This is the decision that superseded the 48-post matrix**, taken after that design was locked and before any
post was published.

### Weekly feed-format mix: 4 Reels + 2 Carousels + 1 Static — **ACTIVE** (Founder Lock)
Per account per week. 24 Reels / 12 Carousels / 6 Statics per account; 48 / 24 / 12 pooled. **Locked**, no
longer "intended".

**Rationale:** it is the only mix that keeps Reels and Carousels exactly divisible per engine per account, so
the unavoidable integer residual falls on Static — the smallest, cheapest, least distribution-relevant arm. It
also puts Reels cadence at ~17/month, inside the market band for this tier, which closes the "insufficient
Reels volume" alternative explanation that the 48-post design openly accepted.

### The balanced 84-post matrix — **ACTIVE · FOUNDER-LOCKED**
Designed, validated and locked jointly by Sari and Wasim. **Canonical source of truth:
`experiment/active-84-post-plan/matrix_84.csv`** (84 rows). Human-readable form and full balance audit:
`experiment/active-84-post-plan/MATRIX_84.md`. Validate with `python3 tools/validate_matrix.py`.

Key locked properties: 42 posts/account · 21 pooled per engine · 24R/12C/6S per account · pooled engine ×
format exactly 12R/6C/3S · **weeks 3–6 exactly 7 posts per account per engine at exactly 4R/2C/1S** · every
engine exactly once per weekday per account in weeks 3–6 · A and B never publish the same engine on the same
date. The full frozen surface is `experiment/active-84-post-plan/LOCK_SPECIFICATION.md`.

⚠ **Locked is not launched.** Nothing may be published until both gates in
`experiment/active-84-post-plan/GATES.md` pass.

### Fixed publish instant: 16:00 UTC — **ACTIVE** (Founder Lock)
All 84 feed posts, both accounts, one absolute instant (= 19:00 at UTC+3). Posting time is a **held-fixed
control, not an experimental factor**; "best posting time" is not tested here.

**Rationale:** a constant cannot confound anything, which fixes the historical account/slot welding more
completely than the superseded two-slot Early/Late scheme did. Anchored to UTC rather than local wall-clock so
the frozen variable stays frozen across any daylight-saving transition. **Early/Late is not part of this
design.**

### Start rule: no arbitrary calendar date — **ACTIVE** (Founder Lock)
The experiment starts on the **first Monday after all required Week-1 and Sourcing Gates have passed**. No
start date is chosen in advance, and none is recorded anywhere in this repository.

**Rationale:** a date chosen before the gates invites starting and slipping, which the design's own analysis
identified as producing a false negative on assets that may not be testable twice.

### AI-generated imagery: permitted in exactly six C4 slots — **ACTIVE** (Founder Lock)
AI-generated imagery is **not categorically prohibited**. The founders want long-term evidence about it. It is
permitted **only** through a predeclared, counterbalanced, logged nested sub-test:

**exactly 6 of the 84 feed posts · C4 only · 3 per account · 1 Reel + 1 Carousel + 1 Static per account.**
The six slot IDs are frozen in `matrix_84.csv` and may not be swapped after Day 1. **Prohibited in C1, C2 and
C3** — those engines cover real, specific products and factual claims.

Binding safety rules, prohibited-use list, disclosure and provenance requirements, the mandatory sensitivity
analysis and the flip rule: **`experiment/active-84-post-plan/AI_IMAGERY_SUBTEST.md`**. AI results are
exploratory and directional; **the sub-test is not independently powered** and may not declare that AI imagery
works or does not work. Using AI imagery in any other slot is a protocol violation.

### Daily Stories — **ACTIVE** (Founder Lock)
**1 Story per day per account** — 7/week/account, 42/account, **84 combined** over six weeks. Identical
cadence, timing and structure on both accounts; frozen for the whole test; **diagnostic and supporting only**;
outside the 84-post feed matrix; never performance-adaptive. Protocol:
`experiment/methodology/STORY_PROTOCOL.md`.

This supersedes the historical 3-Stories-per-week figure, which came from the superseded 48-post design and was
never a founder decision.

### The weekly account-level Reach safeguard — **SUPERSEDED before it was ever used**
A "secondary safeguard" comparing weekly account-level Reach and non-follower Reach against a Week-0 dormant
baseline was designed during review and **removed before lock**. With daily Stories, weekly account-level Reach
aggregates 42 Stories and 42 feed posts per account against a baseline containing neither, so the increase is
not attributable to the feed. **It has no decision authority.** The per-post read is the sole decision
authority. See Rule S in `experiment/methodology/MEASUREMENT_AND_RULES.md` §4.

### Engine-win rule: ≥2×, with no sub-2× cutoff — **ACTIVE**
A declared engine win requires a pooled median **≥2× the next-best engine** in weeks 3–6 **and** the same
direction on both accounts. Sub-2× separations are reported descriptively with **no cutoff of any kind**.

⚠ **A proposed 1.7× "suggestive" band was removed before lock** as false precision — √n scaling governs the
standard error of a mean, not the median of a heavy-tailed distribution.

### No performance-based adaptation mid-test — **ACTIVE**
The full matrix is frozen for all posting weeks. No extra slots for a leading cell, no dropping a cell for
weak performance, no reallocating toward the stronger account, no changing slots or profile variables in
response to results.

**Provenance:** originated as a methodology correction (removing an earlier Week-4 adaptation gate) and
adopted by the founders.

### No extra feed post triggered by virality — **ACTIVE**
The founders initially proposed posting an additional feed post on a day when a post goes viral. Advisory
review identified this as adaptive-selection bias; the founders adopted the restriction.

A breakout post is **documented and may be supported via Story and comments**; any follow-up stays within the
next planned slot. Outliers are ceiling evidence and change nothing in the schedule.

### No paid promotion, giveaways, Collabs, cross-posting or advertiser outreach during the controlled test — **ACTIVE**
Scope-limited to the experiment window. Giveaways and collaborations remain acceptable in principle
afterwards, subject to a later decision — this is a scope limit, not a permanent ban.

### Weekly Account Status checks — **ACTIVE**
All five categories, both accounts, every week. Any category leaving green is a hard stop for that account.

---

## Monetization

### Monetization model unresolved — **DEFERRED**
Direct Instagram sponsorship remains open. A content-production/services model remains open. **Nothing is
chosen.**

### Content-services model considered but not selected — **DEFERRED**
An earlier research round ranked six revenue structures and favoured a productised content service. That
ranking was **explicitly retracted** by the next generation, which contains no revenue-model recommendation.
It is an option under consideration, not an adopted plan.

**Open founder question, deliberately unresolved:** do you want a media asset, or a business that reaches
$6,000/month? A services model is roughly linear in labour and therefore in tension with the 10%-involvement
goal. These may be different businesses.

### Controlled revival required before monetization conclusions — **ACTIVE**
No pricing, packaging, outreach or monetization commitment before the experiment produces distribution data.

**Rationale:** every revenue model depends on reach and audience data that did not exist when the models were
first sketched, and the first sold campaigns are the only real price discovery available — no validated CPM
for a faceless sneaker page at this scale exists publicly.

---

## Infrastructure

### Shared private GitHub repository — **ACTIVE** · HISTORICAL FACT
Organization `sari-wasim-media`, repository `instagram-media-business`, private. Owners `sarimichael` and
`wasimkhoury11`; member `wasimkhoury3-lang`. Git, `gh` and Claude Code installed on Sari's Windows machine;
write access verified by a test commit.

### This repository is the canonical source of truth — **ACTIVE**
Project state no longer depends on Claude.ai chat history. Any future session — any account, any machine —
starts from `HANDOFF.md`.

### Workflow V1 — the canonical working workflow — **ACTIVE**
How the founders and Claude Code work in this repository is codified in **`WORKFLOW.md`**. In summary: Sari
and Wasim are equal founders and a task handed to Claude is already agreed between them; one founder normally
works at a time; each task gets its own branch from an up-to-date `main`; Auto Mode is the default; Claude has
broad execution autonomy **inside** an approved task and escalates anything that changes scope, contradicts a
locked decision, creates significant risk, requires an irreversible external action, or is otherwise a
founder-level call; and **Claude stops before Git finalization**, gives the active founder a review summary,
and waits for explicit approval before add / commit / push / PR / merge — with merge to `main` as the default
after approval.

**Scope limit.** Workflow V1 governs work *inside this repository only*. It does not authorise publishing,
automation, monetization or any other action restricted by an ACTIVE decision above, and it does not change
any business, experiment or platform decision in this register.

⚠ **Clarified, not changed:** `CLAUDE.md`'s "documents and asks — it does not execute" always meant execution
*outside* the repository — publishing, automation, monetization. It was reworded to say so explicitly, because
Workflow V1 makes Claude's in-repository execution autonomy explicit.

---

## Pending founder review — proposals, not decisions

The Creative System + Pre-Launch Foundations sprint (2026-09-06) proposed values for everything the Founder
Lock left to be fixed at template lock or before Day 1: House System v1 (the house templates) · the **C2
ranked-item count (proposed 7)** · the C1 verdict scale and rubric · the Story rotation and sticker weekday
(proposed Wednesday) · the fixed AI disclosure wording · the AI tool candidate · the source-class priority
per engine and the residual-risk acceptance · the caption and hashtag operating form · the comment-reply
policy · the scheduling tool and publish settings · the reserve composition · two operational readings of
locked rules · producer alternation by format batch.

**None of these is in force.** Each becomes an ACTIVE entry in this register only when Sari and Wasim record
it. The queue, with recommendations and the reasoning behind each, is `production/FOUNDER_REVIEW_QUEUE.md`.
Every locked decision above is unchanged by the sprint.
