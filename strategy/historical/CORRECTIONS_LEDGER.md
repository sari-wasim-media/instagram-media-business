# Corrections Ledger

**Why this file exists.** The recovered strategy documents are not five views of one plan. They are **five
generations of one plan, each correcting the last.** Read in isolation, an earlier generation will hand you a
claim that a later one withdrew — including claims the founders have explicitly instructed this project not to
repeat.

Every recovered document is preserved **verbatim**, so the corrections could not be written into them. This
ledger is where they live.

**If you are about to rely on any statement from a document in `strategy/research/` or
`experiment/historical-48-post-design/`, check it here first.**

---

## The generation chain

| Gen | Document | Location |
|---|---|---|
| **G1** | Initial Strategic Audit | `strategy/research/INITIAL_STRATEGIC_AUDIT.md` |
| **G2** | Phase 1 + Phase 2 Report | `strategy/research/PHASE_1_PHASE_2_REPORT.md` |
| **G3** | Revival Experiment — Final Lock | `experiment/historical-48-post-design/REVIVAL_EXPERIMENT_FINAL_LOCK.md` |
| **G4** | Patch and Freeze (contains the 48-post matrix) | `experiment/historical-48-post-design/PATCH_AND_FREEZE_48_POST_MATRIX.md` |
| **G5** | Final Methodology Patch — Matrix Frozen | `experiment/historical-48-post-design/FINAL_METHODOLOGY_PATCH_MATRIX_FROZEN.md` |
| **G6** | **Founder cadence decision** — 1 feed post/day/account, 84 planned posts | `DECISIONS.md` · `PROJECT_STATE.md` |

**Later beats earlier. G6 is a founder decision and beats all of G1–G5.**

G1–G5 are AI analysis. Where they state a *recommendation*, it is a recommendation — it became project policy
only where the founders adopted it into `DECISIONS.md`.

---

## Priority corrections — the three most likely to cause harm

### ⚠ 1. "One repost resets a 30-day clock and makes the account ineligible" — **WITHDRAWN**

**Where it still appears (verbatim, in a superseded document):** G3 §2 Correction A point 2 — *"The recovery
clock runs from the last unoriginal post. One slip in week 5 resets 30 days and destroys the eligibility
read"*; G3 §7 preamble; G3 §13 — *"Do not post an unoriginal asset 'just this once.' That resets the 30-day
clock and invalidates the eligibility read for the entire remaining test."*

**Corrected by:** G4 §1 Correction 1.

**Current position — two independent mechanisms, do not conflate them:**

- **Account-level eligibility** turns on *repetition*: accounts that repeatedly post content from other users
  they did not create or materially enhance — 10 or more times in the last 30 days — are not shown in
  recommendation surfaces. The recovery mechanism applies **only to accounts that have already crossed that
  threshold**. Both accounts are green, so neither is in a recovery state, and, in G4's words, *"the 30-day
  clock is not something a clean account resets."*
- **Post-level treatment** is separate and independent: an individual unoriginal post may be replaced by the
  original in recommendations, labelled with credit to the first poster, or deprioritised by near-identical
  detection — which judges **the file, not the account** — with no account-level consequence.

**The zero-repost rule survives, on different reasoning.** G4 restates it on five grounds: clean attribution;
a suppressed post wastes a matrix slot; the experiment is partly a test of the team's ability to produce
original content at cadence; reposts create interpretive ambiguity; and zero against a threshold of ten is a
margin of safety. **Not** because one repost makes the account globally ineligible. It does not.

**Downstream:** an unoriginal post is a **protocol violation, not an emergency**. It is not a hard stop, does
not invalidate the test, and does not require pausing the account.

### ⚠ 2. "Living-follower rate" and the 2.3% / 3.7% liveness figures — **WITHDRAWN**

**Where they still appear:** G3 §1 (*"touching roughly 2.3% of the base in a quarter"*, *"the number of US
followers currently reachable is plausibly in the low hundreds"*), G3 §4, G3 §9 (*"Story reach ÷ current
follower count = living-follower rate"*), G3 §10 (Story bands <3% / 3–8% / >8%).

**Corrected by:** G4 §1 Correction 2 and G4 §4–§5.

**Current position:** the figures are invalid on their face — 98.7% and 98.5% of those views came from
**non-followers**, so the numerator is overwhelmingly not followers. Both figures and everything derived from
them are withdrawn. **The active fraction of each follower list is unknown.** "Living-follower rate" is
deleted as a metric and as a concept. Stories move from a threshold gate to a **supporting diagnostic** and
appear in no pass/fail rule and no scenario definition. The Story threshold bands were withdrawn by G4 as
*"internal hypotheses presented with unearned authority."*

### ⚠ 3. Week 4 "double down" and "drop a cell" adaptation — **REMOVED**

**Where it still appears:** G3 §3, G3 §13; and **G4 §6, which still contains the full adaptation rules
including the added balance clause.** G4 is otherwise the most authoritative historical document — this is the
one section of it that a later generation deleted.

**Corrected by:** G5 §1.

**Current position:** all performance-based adaptation is removed. All six weeks are frozen. Week 4 is a
**diagnostic, safety and data-quality checkpoint only — no allocation decision may be taken at it.** G5
explicitly deletes the "double down" rule, the "drop a cell" rule, the Week 4 adaptation gate, the balance
clause, and every reference to Weeks 1–4 as primary or Weeks 5–6 as confirmatory. Prohibited at any point:
extra Reel slots for a leading cell, dropping a cell for weak performance, increasing a format allocation,
reallocating toward the stronger account, changing slots, changing profile variables for weak conversion,
changing an account's editorial role, or chasing a breakout post.

---

## Full ledger

### G1 → corrected by G2

| Claim in G1 | Correction | Current position |
|---|---|---|
| Reels reach 15–40% of followers | G2 §2 | Wrong by 3–5x. Tier interpolates to roughly 6–8% |
| 100–200 original Reels/month required | G2 §2 | Wrong by 5–10x. Market cadence for this tier is 17–20/month |
| Face on camera worth 3–5x CPM | G2 §2 | **Withdrawn — no evidence base.** Also moot under the faceless constraint, but G2 states it should not have been claimed |
| A meaningful portion of the 44.8k followed for replicas | G2 §2 | **Withdrawn** as an untested hypothesis |
| The historical advertiser base operated in replicas | G2 §2 | **Overstated.** Evidence covers two named advertisers across four creatives — a fact about those creatives, not about the advertiser base |
| Renaming `sneakerbong` is near-mandatory | G2 §6 | Downgraded to *"do not rename either account yet"*; see the rename thread below |
| $750/client/month; $10–25 CPM defensible; 0.5–2% view→follow; 20–30 founder-hours/week; geographic CPM factor of five | G2 §2 | All **weakened to scenario inputs or judgement**, not findings. No validated theme-page CPM dataset exists |
| 500k followers is 2–3x optimistic | G2 §2 | *"Now looks generous"* — only 21% of sub-10k accounts grew at all in 2026 |

### G2 → corrected by G3

| Claim in G2 | Correction | Current position |
|---|---|---|
| The originality rule was announced **30 April 2026** | G3 §2 Correction A | Published **30 April 2024**. The April 2026 event was its *extension* from Reels to photos and carousels. G3: *"I collapsed two events into one"* |
| *"10 or more reposts in 30 days"* appears only in low-quality SEO sources; not relying on it | G3 §2 Correction A | **Reversed.** It is real first-party language. There is also an explicit carve-out for publishers holding licensing agreements or creator permission |
| Hypebeast shows ~20%/yr decline — the category ad market is contracting | G3 §2 Correction C | **Rate of decline roughly halved** (FY25 HK$666.5M; TTM ~HK$580M ≈ −13%); management describes deferral, company profitable and paying dividends. Now a **risk hypothesis, not a proven structural collapse** — and G3 states it was *removed from the design* |
| Six revenue models ranked; Model 4 (content production) most plausible; hybrid recommended | G3 §2 Correction D | **Accepted and removed.** G3 contains no revenue-model recommendation. Direct sponsorship open, services model open, **nothing chosen** |
| Reach-rate bands <3% / 3–7% / >7%; non-follower <20% / 20–50% / >50%; medians across weeks 4–6 | G3 §10 | Replaced by per-format bands (Reels <2.0% / 2.0–5.0% / >5.0%) and non-follower <25% / 25–55% / >55%, medians across **weeks 3–6** |
| Four cells: market intelligence · utility/comparison · original meme/commentary · editorial analysis | G3 §5 | **Redefined** so each cell tests a distribution *mechanism*, not a topic → C1–C4. See the content-engine lineage below |

### G3 → corrected by G4

| Claim in G3 | Correction | Current position |
|---|---|---|
| One unoriginal post resets the 30-day clock / invalidates the eligibility read | G4 Correction 1 | **Withdrawn.** See priority correction 1 |
| Follower liveness ≈2.3% (A) / 3.7% (B); "low hundreds" of reachable US followers; living-follower rate | G4 Correction 2 | **Withdrawn.** See priority correction 2 |
| Format allocation per cell: C1 3R/2C/1S · C2 2R/2C/2S · C3 3R/1C/2S · C4 4R/1C/1S | G4 Correction 3 | **The matrix did not control format** — C4 received the most Reels, so "better engine" and "more exposure to the best format" were inseparable. Rebuilt as a complementary two-account design: pooled **6R / 3C / 3S per cell**, and **exactly 3 Reels per cell on every account** |
| Posting slots welded to account (A always 19:00, B always 19:45), justified by overlapping-audience competition | G4 Correction 4 | Slot and account identity were inseparable. Replaced by **two counterbalanced slots**, each account taking exactly 12 Early and 12 Late. The competition justification is **explicitly withdrawn as unevidenced** |
| Story times A 20:15 / B 21:00 | G4 §3 | Both accounts **20:30 GMT+3** |
| Story threshold bands <3% / 3–8% / >8% | G4 §5 | **Withdrawn** as *"internal hypotheses presented with unearned authority"* |
| Account B runs the identical matrix in reverse week order | G4 §2 | Superseded by the explicit per-account matrix in G4 §2, which is not a simple reversal |

### G4 → corrected by G5

| Claim in G4 | Correction | Current position |
|---|---|---|
| G4 §6: Week 4 gate; "double down"; "drop a cell"; weeks 5–6 adaptation with symmetric balance clause; weeks 1–4 as the primary balanced dataset | G5 §1–§2 | **All removed.** See priority correction 3 |
| A post exceeding 50x running median in weeks 5–6 extends the test two weeks | G5 §1, §3 | Breakouts are recorded as ceiling/breakout evidence and **change nothing in the schedule**. No replication attempt until the locked test completes |
| Replacement for an unoriginal post must land within 7 days or the cell is marked missing | G5 §3 | Replace preserving account, cell, format and slot category, **extending the calendar if needed** — *"An extended calendar is preferable to an unbalanced dataset"* |

### G5 → superseded by G6 (the founder decision)

| What G5 closed | Superseded by | Current position |
|---|---|---|
| The 48-post execution matrix, at 4 feed posts/week/account (24/account, 48 total), across 6 posting weeks | **G6** | **SUPERSEDED BEFORE LAUNCH.** The founders decided on 1 feed post/day/account — 7/week/account, 14 combined/week, 6 posting weeks, **84 planned feed posts total**. No revival-experiment post had been published. The balanced 84-post matrix is **not yet designed** |
| G5's gate: *"REVIVAL EXPERIMENT FULLY LOCKED — PROCEED TO WEEK 0"* | **G6** | That gate applied to the 48-post design. It does not authorise launch today — there is no locked matrix at the active cadence |

---

## Two threads worth following end to end

### The `sneakerbong` rename

G1 called it near-mandatory → G2 §6 found **no evidence** Instagram penalises the name, judged the brand-safety
concern real only for large advertisers running formal review (not the realistic near-term buyers), and
recommended *"do not rename either account yet"* (confidence moderate-to-high), principally because a rename
would confound the experiment → G3 §7 froze the username, noting the earlier brand-safety worry *"has no
platform evidence behind it"*, and deferred to week 8 → G3 §14 Scenario C makes the decision live only if B is
the surviving asset, with the criterion being *"does this name describe a media product a business would buy
from"*, **not** the word "bong".

**Current status: DEFERRED by founder decision.** Not renaming before revival evidence exists.

### The content engines

**G2 §10 four cells** — market intelligence (A) · utility/comparison (E) · original meme/commentary (D) ·
editorial analysis (B), drawn from the six-engine map in G2 §9.

**G3 §5 redefined them** so each cell tests a different *distribution mechanism* rather than a topic:

| | Cell | Primary metric |
|---|---|---|
| **C1** | Release & Verdict Desk | non-follower reach share, comments per reach |
| **C2** | Rankings & Tier Lists | saves per reach, profile visits per reach |
| **C3** | Market & Price Intelligence | saves per reach, profile visits per reach |
| **C4** | Original Meme & Commentary | sends per reach |

**C1–C4 are the latest locked definitions** and are what `PROJECT_STATE.md` carries. The G2 naming is their
ancestor, not a competing set. If you see the older four-way naming quoted anywhere, it is the Phase 2
generation.

---

## On voiceover — an analysis position, not a founder decision

G2 §9 and G3 §5 both state: *"faceless does not mean voiceless — voiceover, text-on-screen narration and a
named editorial persona are all available and all count as authorship."*

**That is prior Claude analysis. It has not been locked as a founder decision.**

The founder constraint is that **Sari and Wasim will not appear visually or become public-facing
personalities**. Voiceover is **not prohibited by that constraint**, but neither has it been separately
approved. Prior analysis may be cited as having considered it viable. It must not be presented as settled
policy in either direction — see `DECISIONS.md`.
