# Decision Register

Founder decisions and their status. **This file is authoritative on what was decided.**

| Status | Meaning |
|---|---|
| **ACTIVE** | In force now — a founder decision |
| **ACTIVE — delegated production decision** | In force now — decided by Claude under the founders' delegated production authority of 2026-09-08, inside its escalation boundaries. Not a founder-selected value; the founders may override any of them |
| **SUPERSEDED** | Was in force; replaced by a later decision |
| **DEFERRED** | Deliberately not decided yet |
| **OPEN — founder decision pending** | Raised with a recommendation; only the founders can close it |
| **HISTORICAL** | A fact about the past that shapes current constraints |

⚠ **2026-10-08 — AGILE REVIVAL supersedes the 84-post controlled experiment, BEFORE LAUNCH.** Zero posts
had been published under it. Every entry below marked "(Founder Lock)", "FOUNDER-LOCKED" or scoped to "the
controlled experiment / test" is **SUPERSEDED BEFORE LAUNCH** and preserved as historical methodology —
except the rules listed as *retained* in the [Agile Revival section](#agile-revival--founder-decision-2026-10-08).
Read that section first.

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
`tools/validate_backlog.py`, and from 2026-09-13 `tools/validate_c2_stress_test.py`), a generator of the
tracking-sheet skeleton from the matrix
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

### Start rule: begin as soon as the gates pass, on any weekday — **ACTIVE** (Founder Lock, amended 2026-09-11)
**Decided jointly by Sari and Wasim on 2026-09-11**, replacing the first-Monday rule below.

Once every required pre-launch gate has passed and the founders have confirmed the launch-ready state, the
experiment begins immediately: **Day 1 is the earliest calendar day — on any weekday — whose Day-0
requirements are met**: the `A-W1-C1-CAR-01` topic lock executed at Day 0 16:00 UTC (the day before Day 1)
and the 11 non-C1 Week-1 pieces scheduled in-platform on their Day-1–7 dates. **There is no requirement to
wait for a Monday.** No start date is chosen before the gates pass, and none is recorded anywhere in this
repository. Every other gate, lock and launch restriction is unchanged.

**Rationale:** the anti-slip logic of the original rule is preserved in full — the date is still never chosen
ahead of the gates. What is removed is the up-to-six-day idle deferral to the next Monday, which bought
nothing the design needs: every locked balance property is defined on the matrix's day positions, not on
calendar weekdays.

**Corollary, acknowledged by the founders — how the matrix reads under this rule.** `matrix_84.csv` is
**unchanged, byte for byte**. Its `day` / `weekday` columns are **launch-relative positions**: D1 is the first
day of each experiment week and carries the label `Mon`; D7 is the seventh and carries `Sun`. The calendar
weekday of a slot binds only when Day 1 is instantiated, and equals the label only when Day 1 is a Monday.
Because the six weeks are 42 consecutive days, each position D1–D7 maps to one fixed calendar weekday for the
whole experiment, so "every engine exactly once per weekday per account in weeks 3–6" and every other locked
balance property hold in calendar terms under any start weekday. `tools/instantiate_calendar.py` emits both
the matrix label and the real calendar weekday.

**Delegated production decision recorded alongside (Claude, 2026-09-11):** the Story rotation and the
sticker weekday stay **calendar-keyed** — DROP CALENDAR on Monday, THE POLL with the sticker on Wednesday,
THE WEEK on Sunday — because their content is calendar-semantic (`production/templates/STORY_TEMPLATE_AND_ROTATION.md`).
Under a non-Monday Day 1, Week 1's Story sequence simply begins mid-rotation; every experiment week still
carries each class exactly once and exactly one sticker per account. The Stories tab of the tracking
skeleton therefore leaves `weekday` / `rotation_class` / `sticker` / `adjacent_engine` blank until Day 1
exists; they are copied in from the local calendar output.

### Start rule: first Monday after the gates — **SUPERSEDED 2026-09-11**
*Kept for the record; replaced by the entry above.* The experiment starts on the **first Monday after all
required Week-1 and Sourcing Gates have passed**. No start date is chosen in advance, and none is recorded
anywhere in this repository.

**Rationale (still valid, carried forward):** a date chosen before the gates invites starting and slipping,
which the design's own analysis identified as producing a false negative on assets that may not be testable
twice.

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

## Founder decision pulse — 2026-09-08

Five decisions taken by Sari and Wasim after the Creative System + Pre-Launch Foundations sprint, delivered
through the active founder. They change no Founder Lock, no matrix value and no methodology rule.

### Delegated production authority — **ACTIVE** (Founder decision, 2026-09-08)
The founders explicitly delegate **production-level decision authority** for the controlled revival
experiment to Claude. Claude may independently decide and lock professional choices in: the creative system ·
visual design · production design · sourcing implementation · platform operating details · workflow ·
content-production mechanics · template mechanics · operational policies · tooling recommendations · queue,
reserve and scheduling implementation details — without returning small or specialist decisions to the
founders.

**The delegation is bounded.** Claude must still escalate anything that: changes an existing Founder Lock ·
changes the 84-post matrix or the methodology · changes an experimental decision rule · creates a material
new business, legal, platform or account risk · requires spending money · requires accepting a paid
subscription or licence · requires an irreversible external action · requires publishing, scheduling,
outreach or account changes that are not already authorised · creates a genuine contradiction in the canon.
Within those boundaries Claude uses its judgement and does not manufacture founder decisions where expert
implementation judgement is sufficient. Decisions taken under this authority are recorded in this register
as **ACTIVE — delegated production decision**, never as founder-selected values.

**Rationale (founders'):** to remove founder review burden from specialist details — fonts, item counts,
Story weekdays, reply caps, reserve composition, batching, caption mechanics, scheduling toggles — that do
not concern founder preference, material risk, money, irreversible commitment or a Founder Lock.

**Effect on `WORKFLOW.md`:** refines the escalation rule in §3; recorded there as §2a.

### Public brand posture: a faceless, opinionated editorial media desk — **ACTIVE** (Founder decision, 2026-09-08)
During the controlled experiment both accounts operate as a **faceless, opinionated editorial media desk**:
not a founder-personality brand, not a neutral repost page, not a generic news aggregator. The accounts have a
clear editorial voice, issue opinions, rankings and verdicts, may use concepts such as COP / WAIT / PASS where
Claude concludes they are the strongest implementation, and remain inside **one shared professional production
system** on both accounts for experimental control. Claude holds authority to optimise the detailed visual and
editorial implementation of that posture. The frozen profile variables (bio, display name, photo) are
unchanged by this decision. Implementation: `production/house-style/EDITORIAL_VOICE.md`.

### Trademark / trade-dress risk posture — **ACTIVE** (Founder decision, 2026-09-08)
The founders asked for an expert recommendation before choosing the legal posture on depicting real branded
sneakers in editorial content, and reserved the choice; Claude was not permitted to accept the residual risk
on their behalf. Claude's focused review — U.S. and Israeli positions, a calibrated likelihood-and-severity
table, and a single recommendation of **ACCEPT** — is `production/TRADEMARK_RISK_REVIEW.md`.
**The founders ACCEPTED on 2026-09-08.** The experiment runs on an editorial, nominative, non-endorsing
posture: rights-cleared photographs of branded sneakers may be used to identify the product being ranked,
reviewed or reported on, with the review's §5 nominative-use operating rule **mandatory on every piece** and
enforced at pre-publish QA. The §3 re-review triggers stand — any IP notice or brand contact, any
monetisation or sponsorship, any new imagery route, and the rest — and each one stops product photography of
the affected brand until the posture is reviewed again. This is an accepted operational risk position, not
legal advice and not a guarantee of legal immunity.

### Conservative data-source posture — **ACTIVE** (Founder decision, 2026-09-08)
For C3 and any other factual or data sourcing during the controlled experiment: **if the applicable terms of
service or usage terms do not clearly permit the intended use, the source is not used** — a cleared
alternative is chosen instead. A slightly narrower data set is preferred over ambiguous or restrictive source
terms. Claude operationalises this rule and chooses the compliant sources. Operationalised in
`production/assets/C3_DATA_SOURCE_TOS_REGISTER.md` (marketplace listing data excluded; press releases,
published reports and brand release notes are the sources) and in the C1 and C3 templates.

### Tool-selection autonomy without spending authority — **ACTIVE** (Founder decision, 2026-09-08)
Claude may independently choose and recommend the AI generation tool, stock provider, production software,
design workflow, technical utilities, sourcing routes and other production tooling. **Selection is not
purchase authorisation.** Any paid subscription, paid licence, paid stock purchase, external financial
commitment, or irreversible acceptance of external terms on behalf of the founders requires explicit founder
approval before execution. Decisions: `production/operations/TOOLING.md`.

---

## Delegated production decisions — 2026-09-08

Decided by Claude under the delegated production authority above, on the same day, after re-evaluating each
earlier proposal rather than mechanically confirming it. Each is **ACTIVE — delegated production decision**;
each is a held-fixed production variable for the six posting weeks; none is a founder-selected value; the
founders may override any of them before Day 1.

| Decision | Value | Where |
|---|---|---|
| **House System v1** | The house visual and motion language — canvases and safe zones, bands, palette with one accent per engine, Bebas Neue / Inter / IBM Plex Mono, the component set, plate treatment, Reel beat grammar, Sound Collection audio rule — for all 84 posts and 84 Stories on both accounts; only the handle differs between accounts | `production/house-style/HOUSE_STYLE.md` |
| **Editorial voice** | The desk voice implementing the approved brand posture: declarative, sourced, verdict-led, no founder persona, no engagement bait | `production/house-style/EDITORIAL_VOICE.md` |
| **C2 ranked-item count** | **7** items in every C2 piece, every format; 147 images across the experiment, 42 for the gate bank | `production/templates/C2_RANKED_ITEM_COUNT_DECISION.md` |
| **C1 verdict scale and rubric** | COP · WAIT · PASS on four criteria scored 0–2 (6–8 / 3–5 / 0–2), score logged; one-step override with a written reason; resale outlook scored 1 (neutral) and stated as such when no compliant resale data exists | `production/templates/C1_RELEASE_VERDICT_DESK.md` §1 |
| **Story rotation and sticker** | Mon DROP CALENDAR · Tue PRICE CHECK · Wed THE POLL · Thu DESK NOTES · Fri THE VERDICT · Sat TWO SHOES · Sun THE WEEK; sticker weekday **Wednesday**, poll by default, quiz allowed; Wednesday posted manually until scheduler sticker support is proven | `production/templates/STORY_TEMPLATE_AND_ROTATION.md` |
| **AI disclosure line and placement** | "Imagery in this post is AI-generated and illustrative. It does not depict a real product." — verbatim as the last caption line before the hashtags in all six AI posts, platform AI label on; **nothing on the artwork** | `production/policy/AI_IMAGERY_POLICY_PACK.md` §3 |
| **AI generation tool** | **Adobe Firefly** (web), free tier first; alternate Google Gemini. Licence verification, account creation and any paid plan are founder actions (Sourcing Gate item 9; no spending authority) — **licence confirmed by Wasim 2026-10-07, free tier only** (founder decision below) | `production/policy/AI_IMAGERY_POLICY_PACK.md` §5, `production/operations/TOOLING.md` |
| **Source-class priority per engine** | C1: self-generated → owned → licensed → verified press · **C2 (revised 2026-09-13): licensed free → verified press → licensed paid (founder-approved spend) → self-generated illustration → owned (opportunistic only); permissioned is not an active route (founder decision, 2026-09-13: no permission outreach)** · C3: self-generated only · C4: self-generated → owned → licensed → AI in the six slots. Product photography of branded sneakers runs under the accepted trademark posture and its §5 operating rule (2026-09-08). The C2 order is provisional until the two-piece stress test reports | `production/assets/SOURCE_CLASS_DECISION.md` |
| **Compliant data sources** | Press releases, published reports and brand release notes are the sources; marketplace listing pages, aggregators and secondary reporting are not; product pages confirm only | `production/assets/C3_DATA_SOURCE_TOS_REGISTER.md` |
| **Caption and hashtag form** | Hook · body · source line · AI line (six posts) · 3–5 tags (2–3 subject + 1 fixed category + ≤ 1 community; ban list); alt text always; American spelling; no CTA, link, mention, location | `production/policy/CAPTION_AND_HASHTAG_POLICY.md` |
| **Comment-reply policy** | Substantive comments answered within 24 h, ≤ 15 replies per post, like all non-spam, hide spam, no pins, no DM outreach, identical on both accounts | `production/policy/COMMENT_REPLY_POLICY.md` |
| **Scheduling tool and publish settings** | Meta Business Suite (desktop) for feed posts; Reels share-to-feed ON; Facebook sharing OFF; never Trial; no location, people, collaborator or product tags; AI label ON for the six only; Sound Collection audio; Wednesday Story manual | `production/policy/SCHEDULING_AND_PUBLISH_SETTINGS.md` |
| **Reserve composition** | C2 Reel + Carousel · C3 Reel + Carousel + Static · C4 Reel + Carousel; the two C2 reserve pieces may be filled by promoting the stress-test prototypes after a pass (order reversed 2026-09-13: prototypes first) | `production/operations/RESERVE_REGISTER.md` |
| **Queue-rule operational readings** | C1 eligibility window: news broken ≤ 7 days before or release ≤ 10 days after the publish instant; C2 subject = the theme, #1 pick logged as a secondary subject | `production/backlog/README.md` §2, `production/templates/C2_RANKINGS_AND_TIER_LISTS.md` §7 |
| **Producer allocation and rhythm** | Producers alternate by format batch, never by account; Friday check-outs two weeks ahead; Tue Reels, Wed carousels and statics, Thu QA and scheduling, Mon weekly review | `production/operations/PRODUCTION_RHYTHM.md` |
| **Production tooling** | Figma (free) for stills; CapCut desktop (free) for Reel assembly with no CapCut library content; Meta Business Suite; Instagram Sound Collection; the house renderer for frames; free tiers only | `production/operations/TOOLING.md` |

---

---

## Founder operational fact and the sourcing correction — 2026-09-13

### No founder-owned sneaker inventory — **ACTIVE** · HISTORICAL FACT (founder-stated, 2026-09-13)
Sari and Wasim **do not have meaningful access to a large sneaker inventory** and cannot realistically
self-shoot dozens of different products. Self-shot imagery may be available occasionally; it **cannot be
the primary or scalable sourcing route** for the C2 asset bank. This is an operational constraint, not a
preference. It changes no Founder Lock: the matrix, the C2 ranked-item count, the format mix, the AI
sub-test, the originality rule and every other locked value stand.

### C2 sourcing routes re-ranked; the stress test comes before the bank — **ACTIVE — delegated production decision** (2026-09-13)
Under the delegated production authority of 2026-09-08 (sourcing implementation), and because the
2026-09-08 route order rested on an owned inventory that does not exist:

- **C2 source-class order:** `LICENSED_FREE` (for the initial stress test: CC0 / public-domain-equivalent →
  Pexels License → Unsplash License → other clearly licensed-free assets only where the requirements are
  unambiguous and met exactly; **CC BY not used in the initial test** — founder correction on review,
  2026-09-13 — kept in the class as a possible future route pending an attribution check; with an
  ownership-plausibility check per candidate) → `PRESS_VERIFIED` (PUMA on the
  archived reading; any further brand is a trademark-review §3 trigger) → `LICENSED_PAID` (founder approval
  per purchase; none on file) → `SELF_GENERATED` illustration (always-on fallback; its share is reported) →
  `OWNED` (opportunistic only). The six routes are unchanged in kind — none added, none removed — so no
  re-review trigger fires; the trademark review's §5 rule and §6 narrowing apply unchanged.
- **Credit is not permission.** An image that is merely public, on Instagram, on Pinterest, on a retailer
  page, watermarked, reposted elsewhere or "creditable" is not rights-clean; it is logged UNCLEAR / BLOCKED
  and never receives an asset ID. Trademark posture and copyright permission are separate questions.
- **Sequence:** the two-piece C2 sourcing stress test (protocol v2, `production/assets/C2_SUSTAINABILITY_TEST.md`,
  package in `production/assets/c2_stress_test/`) runs **before** the 42-image bank; the bank is sized by
  its measured minutes per image. The two pieces are **non-publishing prototypes** (`TEST-C2-CAR-01`,
  `TEST-C2-REE-01`); they consume no slot, enter no queue, and are promoted to the two C2 reserve pieces only
  after a pass, by a separate logged step. The verdict follows a pre-declared rule (§5 of the protocol); a
  **NOT SUSTAINABLE** verdict is escalated to the founders, not solved by relaxing any rule.
- The earlier bank-build plan (rig, inventory, 20-pair shoot, "≈ 15 h") and the "shift to O + S" failure
  path are **withdrawn**; the earlier "≈ 54 founder-hours to launch-ready" figure is withdrawn with them.

**Rationale:** the founders' stated constraint; the conservative sourcing posture already in force; and the
gate's own rule that the route changes, never the matrix. Founders may override any of this before Day 1.

### No permission outreach to creators or third parties — **ACTIVE** (Founder decision, 2026-09-13)
**Decided by Sari and Wasim.** For the controlled experiment's sourcing, the founders **will not send
permission requests to creators, photographers, Instagram accounts or any other third party** — no DMs, no
e-mails, no waiting for replies, no permission-request queue, no reliance on one-off creator approvals as a
scalable source. **Route X (permissioned creator imagery) is removed from the active sourcing path**, the
permission-request template is withdrawn, and the stress test has no permission stage, no passive wait and
no seven-day lapse.

**What this does not mean.** It is not licence to use anything found online with a credit. Instagram reposts,
Pinterest images, TikTok screenshots, retailer images, random web images and watermarked creator content are
**not** an approved route and are not made one by attribution. **Credit is not permission.** An asset whose
rights basis is not clear under the project's sourcing posture is classified unavailable / rejected. The
`PERMISSIONED` class stays defined in the register schema only because the locked `GATES.md` §1.2 lists it
as an acceptable class; no workflow solicits one, and reopening the route is a founder decision.

**Active C2 route hierarchy after this decision** (`production/assets/C2_SOURCING_ROUTES.md`): F licensed
free (CC0 / public domain → Pexels → Unsplash → other unambiguous free licences; CC BY not used in the initial
test) → B verified brand / press assets where the terms clearly permit the editorial use → P paid stock only
with founder spending approval (`WOULD_USE_P` recorded during the test) → S house illustration → O owned,
opportunistic only. If the 14-image test cannot be completed sustainably on those routes, the verdict is NOT
SUSTAINABLE and the next step is founder escalation — not a weaker route.

**Rationale (founders'):** a deliberate operating decision — the desk does not run outreach, does not wait
days on replies, and does not build its production on approvals it cannot repeat.

## Founder confirmation — Adobe Firefly terms (Sourcing Gate item 9) — 2026-10-07

### Adobe Firefly terms confirmed; free route only — **ACTIVE** (Founder decision, 2026-10-07)
**Confirmed by Wasim (active founder).** Wasim confirmed the Adobe Firefly terms and rules prepared in
`production/assets/FIREFLY_TERMS_VERIFICATION.md`, re-checked against the live Adobe pages, whose dates read
unchanged: Generative AI Product Specific Terms *Effective as of April 23, 2026*; Generative AI User
Guidelines *Last Updated May 15, 2026*; General Terms of Use *Published / Effective October 3, 2025*. Output
is our Content; commercial use is permitted as the memo describes; the Input / prohibited-content rules match
the project guardrails; Content Credentials must not be removed; Adobe's indemnity does **not** apply to the
free / individual route we use. **Sourcing Gate item 9 is PASSED 2026-10-07.**

Conditions confirmed with it:

- **Adobe Firefly on the free route only.** No paid Firefly plan is approved, then or at any earlier point;
  a paid plan remains a separate founder spending decision.
- **No Firefly Gallery / Community use; no Adobe Stock submission.**
- **Content Credentials are never removed or altered.**
- **Prompts never use** brand names, real sneaker model names, logos, real people, or third-party images or
  other protected material without rights.
- **AI stays confined to the six locked C4 slots plus TEST-AI-01**; AI remains prohibited in C1, C2 and C3.

**Recorded with care:** the account is a **pre-existing founder Adobe ID** on which Firefly generation had
already been used; its creation date is **not established from evidence** and is not recorded as a date.
The model is recorded as the **Adobe-native Firefly image model**; the exact in-app version is captured in
`ai_tool_version` at TEST-AI-01, and no partner model inside the Firefly app is part of the route. No lock,
matrix row, methodology rule or decision rule moved.

## Agile Revival — founder decision, 2026-10-08

### Launch Fast-Track — **SUPERSEDED the same day** (Founder decision, 2026-10-08, Wasim)
Earlier on 2026-10-08 Wasim decided that Claude executes all pre-launch work and the C2 stress test that can
reasonably be automated, measuring the real Claude-assisted workflow, with no change to the matrix, Founder
Locks, sourcing/rights rules or gate outputs. Under it, Claude established that the locked T−10 d check-out
rule made Day 1 = 2026-10-09 impossible (earliest 2026-10-18). Before any of that plan was executed it was
superseded by the decision below. Two clarifications Wasim gave under it carry forward: **Claude writes
captions, scripts, alt text and research** (the AI sub-test's "founders' own writing" line was a scope note),
and **work-in-progress commits may be pushed to the task branch** (never to `main` without approval).

### Agile Revival replaces the controlled experiment as the active plan — **ACTIVE** (Founder decision, 2026-10-08, Wasim, active founder)
Because **zero revival posts were published**, the founders superseded the 84-post controlled revival
experiment as the execution plan before Post #1. It was designed, validated and locked, then superseded
before launch; it **neither ran nor failed**. Its documents (`experiment/active-84-post-plan/`,
`experiment/methodology/`) are preserved verbatim as historical methodology.

**The objective now:** launch fast, publish high-quality original content, measure real performance, and
adapt continuously — *publish → measure → learn → adapt → repeat*. Performance data **may** influence future
content. Content need not be predetermined before launch.

**Superseded — no longer binding and never launch blockers:** the 84-row matrix as a publishing schedule;
21 posts per engine; the 4R/2C/1S weekly mix; the T−48 h / T−7 d / T−10 d check-out deadlines and the
FIFO queue rule; the no-performance-driven-adaptation and no-virality-follow-up rules; the fixed 16:00 UTC
instant as a lock; daily Stories as a lock; the six-slot AI sub-test as an experimental treatment; the
Sourcing Gate and Week-1 Gate as launch gates (42-image C2 bank, all 11 non-C1 Week-1 pieces, 14 Week-1
Stories, the 7-piece reserve, 14 Week-2 outlines, the Day-0 lock); the C2 stress test as a precondition of
publishing; the frozen-experiment analysis rules (W3–6 window, ≥2× engine rule). These remain available as
operational tools where useful — they may not delay the first high-quality posts.

**Unlocked but unchanged:** profile variables, link in bio, voiceover and the publish time were frozen only
for the test. Nothing about the profiles changes without a founder decision; the accounts stay faceless.

**Retained — non-negotiable:**

- Original content only; **zero reposted feed content**; no third-party file, watermark or reposted template.
- **Credit is not permission.** No Instagram, Pinterest, TikTok, retailer, random-web or watermarked imagery.
  Every external asset has a defensible rights basis and a provenance row (`production/assets/`).
- The **conservative data-source posture** (2026-09-08) and the C3 data-source register.
- **No permission outreach** (2026-09-13) unless the founders change it.
- **No spending, paid asset, subscription or service** without founder approval.
- **AI imagery:** only clearly illustrative / fictional / commentary creative that cannot be mistaken for a
  real specific product or factual evidence; never a real sneaker model being reviewed, ranked or released;
  never laundering a third-party image; no real-person likeness; disclosed where appropriate (the fixed
  line in `production/policy/AI_IMAGERY_POLICY_PACK.md` §3 plus the platform label). Adobe Firefly on the free
  route stays the confirmed tool (2026-10-07).
- The **trademark / nominative-use posture** and its §5 rule (`production/TRADEMARK_RISK_REVIEW.md`).
- **Account Status monitoring**; any category leaving green stops publishing on that account.
- No replica/counterfeit advertisers, no monetization or advertiser contact, no paid promotion — without a
  founder decision.
- **Quality beats cadence:** a piece that is not good enough is not published.
- Publishing remains a founder action; Claude prepares, the founders publish.

**C1–C4** remain content categories and analysis labels, not quotas. Claude may vary their frequency, add a
strong adjacent angle that fits the brand, pick the strongest format per subject and adapt hooks, pacing,
design and mix from evidence. The house creative system is the starting system and may evolve on evidence.

**Measurement:** a practical learning loop replaces the frozen-experiment analysis — every post tracked
(account, publish time, format, category/angle, topic, Reach, Views, likes, comments, saves, shares, profile
activity, follows, non-follower share), read at fixed ages and reviewed on a rolling basis
(`production/tracking/LEARNING_LOOP.md`).

**Claude's role:** delegated production authority (2026-09-08) now covers topics, formats, angles, workflow
and sequencing, using judgement and observed performance. Claude does everything it reasonably can —
research, sourcing, rights verification, writing, rendering, captions, Stories, analytics structure — and
batches founder-only actions (account access, publishing, screenshots, spending, external terms).

### Delegated production decisions under Agile Revival — **ACTIVE — delegated production decision** (2026-10-08)

| Decision | Value | Where |
|---|---|---|
| Default publish time | **16:00 UTC** (19:00 Israel until 24 Oct, 18:00 after; 12:00 ET) — the evidenced evening window; adjustable on evidence | `production/tracking/LEARNING_LOOP.md` |
| First-post selection | Strongest revival potential (non-follower reach, sends/saves/comments) × rights certainty × production quality; one strong post per account, not a matrix slot | `production/launch/LAUNCH_PLAN.md` |
| Production renderer | House HTML/CSS → Chromium → PNG; ffmpeg → H.264 MP4 Reels (canon-approved alternative to Figma/CapCut) | `production/templates/src/render_piece.py` |
| Learning tracker | One row per post, snapshots at ~48 h and 7 d, weekly rolling review | `production/tracking/` |

## Pending founder decisions and actions

- ~~**AI tool licence verification and account**~~ — **done 2026-10-07** (Wasim; free tier only; Sourcing
  Gate item 9 passed). Any paid Firefly plan still needs founder approval. A confirmed licence does not make
  AI a C2 route.
- ~~**Run the two-piece C2 sourcing stress test**~~ — no longer a launch precondition (Agile Revival,
  2026-10-08); its package stays available as a sourcing-burden instrument.
- **Review the launch package and publish the first posts** — founders (`production/launch/`).
- **Baseline capture** before Post #1: Account Status (five categories) and the audience snapshot on both
  accounts — founders.
- **Any paid stock credits or paid tool** — founder approval before purchase.
- **Git finalization** of the task branch — `WORKFLOW.md` §4.

The experiment Founder Locks above are superseded before launch (Agile Revival, 2026-10-08); the retained
rules listed there are unchanged.
