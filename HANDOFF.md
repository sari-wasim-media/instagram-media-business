# Handoff — Start Here

**For a fresh Claude Code session with no prior chat history, on any account or machine.**

This repository is self-contained. You do not need any Claude.ai conversation to continue this project.

---

## 1. Read these, in this order

1. **`PROJECT_STATE.md`** — what is true right now. The single most important file.
2. **`DECISIONS.md`** — what was decided, and what is still open.
3. **`WORKFLOW.md`** — how work is done here: autonomy, escalation, and the Git flow.
4. **`experiment/active-84-post-plan/README.md`** — the **founder-locked** 84-post design.
5. **`experiment/active-84-post-plan/GATES.md`** — **what still blocks launch.**
6. **`strategy/historical/CORRECTIONS_LEDGER.md`** — **read before citing anything historical.**

That is enough to work. Everything else is depth — and this is a sensible default, not a mandatory checklist:
read whatever else the task needs.

---

## 2. Current state in six lines

- Two dormant Instagram accounts, `thestreetwearofficial` (~23.9K) and `sneakerbong` (~20.8K), being revived
  as a faceless sneaker/streetwear media business by two 50/50 founders, Sari and Wasim.
- Both accounts are **fully green** on all five Account Status categories — latest observed state.
- Week 0 setup is substantially done: 2FA enabled, targeted legacy cleanup executed, a minimal bio edit made
  (follower-goal line removed) and profiles then frozen.
- **The controlled revival experiment has NOT started. Zero posts published.**
- The active cadence is **1 feed post/day/account → 84 feed posts over 6 weeks**, plus **84 Stories**.
- ✅ **The 84-post matrix is designed, validated and FOUNDER-LOCKED** —
  `experiment/active-84-post-plan/matrix_84.csv`.
- ✅ **The creative system and pre-launch instruments are built (2026-09-06) and decided (2026-09-08)** —
  `production/`. The founders delegated production-level authority to Claude on 2026-09-08; the former
  review-queue items are **ACTIVE — delegated production decisions** in `DECISIONS.md` (C2 ranked-item
  count **7**, Wednesday sticker, Firefly, and the rest). Founders may override before Day 1.
- ✅ **The trademark / trade-dress posture is ACCEPTED** (2026-09-08) —
  `production/TRADEMARK_RISK_REVIEW.md`. Photographs of branded sneakers are produced under its §5
  nominative-use operating rule, mandatory on every piece; its §3 re-review triggers stand.
- ⚠ **Locked is not launched.** Launch is blocked on the Sourcing Gate and the Week-1 Gate. Zero Week-1
  pieces exist, by design.

---

## 3. Hard constraints — do not violate

| Constraint | Detail |
|---|---|
| **Faceless** | Neither founder appears on camera, in photographs, in video, or as the public personality behind either account |
| **No voiceover during the test** | Founder-locked. All 48 Reels use a uniform non-voiceover method. **Test-specific, not a permanent business ban** |
| **No link in bio during the test** | Founder-locked. Both bios route business contact through DM |
| **AI imagery only in 6 locked C4 slots** | Founder-locked nested sub-test. Prohibited in C1/C2/C3 and in every other slot. See `experiment/active-84-post-plan/AI_IMAGERY_SUBTEST.md` |
| **Daily Stories, frozen** | 1/day/account, 84 combined. Diagnostic only, outside the matrix, never performance-adaptive |
| **No replica/counterfeit advertisers** | Permanent. Also excludes bot/proxy vendors, follower-growth services, crypto/NFT-adjacent, gambling, dropship arbitrage |
| **Zero reposts during the experiment** | Original or materially enhanced content only |
| **Profile frozen** | Username, display name, bio, photo, link (none), pins, highlights, publish instant — all frozen for the experiment's duration |
| **No paid promotion, giveaways, Collabs or advertiser outreach** | During the controlled test |
| **No performance-based adaptation** | All six weeks are frozen. Outliers change nothing |
| **No monetization commitments** | Not before the experiment produces data |
| **No automation built** | No publishing tooling, dashboards or scrapers. `tools/validate_matrix.py` is a read-only checker of a committed CSV, not automation |

---

## 4. Completed — do not redo

- Strategic audit, and the full Phase 1 + Phase 2 research round → `strategy/research/`
- Account data collection: status, demographics, geography, 90-day passive performance, historical samples
  → `evidence/`
- The revival experiment methodology, designed and locked across four correction generations
- **The balanced 84-post matrix — designed, validated and founder-locked** → `experiment/active-84-post-plan/`
- 2FA on both accounts
- Targeted removal of three UAPLG/counterfeit promotions (documented first)
- The Week 0 profile edit — **minimal by decision**: the follower-goal line was removed from each bio and the
  rest kept substantially unchanged. ⚠ **An earlier draft proposed rewriting both bios; the founders did not
  apply it. Do not treat that rewrite as pending work** — the profile is frozen
- This repository migration
- **The Creative System + Pre-Launch Foundations sprint (2026-09-06)** → `production/`: House System v1,
  the C1–C4 and Story templates with 64 rendered specimens, the asset and rights pipeline with its research
  record, the policy pack, the topic queue, the production rhythm and C1 ladder, the tracking-sheet skeleton,
  the gate scorecards, and four validators/generators in `tools/`. **Decided under delegated authority on
  2026-09-08 — do not rebuild them and do not reopen them unless a founder asks.**

⚠ **Do not re-run market research.** It exists, and much of it was corrected — read the ledger rather than
regenerating it. ⚠ **Do not re-run the rights and terms research either** — it is recorded with access
dates in `production/assets/SOURCING_ROUTES_RESEARCH.md`; re-read a specific page only when a decision
depends on it.

---

## 5. Superseded — do not accidentally reactivate

**The 48-post matrix is not the plan.** It is detailed, balanced, and looks authoritative. It was superseded
before launch. Everything in `experiment/historical-48-post-design/` is historical.

Three specific traps, all live if you read those documents without the ledger:

1. **"One repost resets a 30-day clock and makes the account ineligible."** Appears in the Final Lock.
   **Withdrawn.** Account-level eligibility turns on repetition (10+/30 days) and its recovery applies only to
   accounts that already crossed the threshold. Post-level treatment judges the file, not the account. The
   zero-repost rule still stands — on different reasoning.
2. **"Living-follower rate" and the 2.3% / 3.7% liveness figures.** **Withdrawn** — the numerator was
   overwhelmingly non-followers. The active fraction of each follower list is **unknown**. Stories gate
   nothing.
3. **Week 4 "double down" / "drop a cell" adaptation.** Still present in §6 of the Patch and Freeze document.
   **Removed** by the final methodology patch. All posting weeks are frozen.

Also superseded: the earlier six-model monetization ranking (explicitly retracted — nothing is chosen), the
earlier four-cell naming (redefined as C1–C4), and every count sized to 4 posts/week/account.

**Three further things that were designed during review and then removed before lock. Do not reintroduce them:**

1. **A 1.7× "suggestive" engine-separation band.** Removed as false precision. The rule is **≥2×**, and there
   is **no sub-2× cutoff of any kind**.
2. **A weekly account-level Reach "secondary safeguard"** able to veto a Scenario H conclusion. Removed —
   daily Stories make account-level Reach non-attributable to the feed. It has **no decision authority**.
3. **Early/Late two-slot posting.** Replaced by one fixed instant, 16:00 UTC, for all 84 posts.

**Also superseded: 3 Stories/week.** Stories are now **daily** by founder decision — 84 combined.

---

## 6. Immediate next task

> **The founders verify Adobe Firefly's terms.** Then **execute the Sourcing Gate** along
> `production/PRE_LAUNCH_RUNBOOK.md` (asset bank on the accepted routes, C2 sustainability test, AI test
> piece). Then the Week-1 Gate. Then, and only then, the start date is
> instantiated as the first Monday after both gates pass.

**The design is finished and locked. Do not redesign it. The creative system is built and decided; do not
rebuild it and do not re-open the delegated decisions unless a founder asks.** Read
`experiment/active-84-post-plan/GATES.md` for the exact pass criteria, the scorecards in `production/gates/`
for status, and run `python3 tools/validate_matrix.py` if you want to confirm the matrix is intact.

⚠ **C2 is the binding constraint, and it is different in kind from C3.** A C2 ranking needs one rights-clean
image **per ranked item, in every format** — roughly 85–170 distinct images across its 21 posts. C3's visuals
are self-generated charts; its constraint is research time and data-source terms of service. Older checklists
bundle these as "C2 and C3 sourcing"; they are not the same problem.

**Changing the format mix would not reduce the rights burden** — a C2 ranking needs the same per-item assets
whether it ships as a carousel or a Reel. If the gate cannot be passed, delay launch.

---

## 7. Needs founder approval before you act

**Settled by the Founder Lock — do NOT reopen these:** the format mix · voiceover (none during the test) · the
start rule · link in bio (none) · AI-generated imagery (six locked C4 slots only) · Story cadence (daily) ·
the 84-post matrix itself.

**Delegated to Claude since 2026-09-08 (`WORKFLOW.md` §2a):** production-level decisions — creative
system, visual and production design, sourcing implementation, platform operating details, workflow,
template and content mechanics, operational policies, tooling selection, queue / reserve / scheduling
details. Recorded as **ACTIVE — delegated production decision**; do not send these back to the founders.

**Still requires founder approval:**

- **Publishing anything at all.** Launch is gated; the gates have not passed.
- **Spending money, paid subscriptions or licences, paid stock, or accepting external terms on the
  founders' behalf** (tool selection is delegated; purchase is not).
- **Any monetization, pricing or advertiser contact.**
- **Building automation, dashboards or publishing tooling.**
- **Renaming `sneakerbong`** — deferred until after revival evidence.
- **Git finalization of any task** — add / commit / push / PR / merge. See `WORKFLOW.md` §4.
- **Any change to the locked matrix or the locked methodology.** The lock is a founder decision; only the
  founders can move it.

When in doubt about anything **outside this repository**, this project's default is to **document and ask**,
not to execute. Inside an approved task, in this repository, Claude executes and reports afterwards.

## 8. Working workflow and Git safety

**`WORKFLOW.md` is canonical** on how work is done here — founder roles, Claude's autonomy, the escalation
rule, the branch-per-task Git flow, and the guardrails. The short version:

- **Work on a task branch** cut from an up-to-date `main`; `main` is shared between two founders.
- **Stop before Git finalization.** Summarize the work, then wait for the active founder's explicit approval
  before add / commit / push / PR / merge.
- **Never rewrite history** — no force-push, rebase of pushed commits or amending published commits — without
  explicit founder approval for that specific operation.
- **Never commit secrets** — no passwords, tokens, API keys, session cookies, or **2FA recovery codes**.
  `.gitignore` covers common patterns, but the rule is yours to enforce.

Repository-specific preservation rules:

- **Never modify `archive/raw-migration-source/`.** It is the pristine record. If an organized copy is wrong,
  fix the copy.
- **Never edit recovered historical documents.** They are preserved verbatim. Corrections belong in
  `strategy/historical/CORRECTIONS_LEDGER.md` and adjacent README files.
- `_migration_inbox/` is gitignored because `archive/raw-migration-source/` preserves it byte-for-byte.
  Do not delete it without founder approval.

---

## 9. Where things are

```
PROJECT_STATE.md    current truth          DECISIONS.md     what was decided
ROADMAP.md          phases                 HANDOFF.md       this file
WORKFLOW.md         how we work            CLAUDE.md        Claude Code entry point
strategy/           context + research     experiment/      methodology + the LOCKED matrix + tracking skeleton
evidence/           organized screenshots  archive/         pristine originals
production/         creative system, asset pipeline, policies, queue, rhythm, tooling, gate scorecards (delegated decisions; trademark posture accepted 2026-09-08: TRADEMARK_RISK_REVIEW.md)
tools/              validate_matrix.py · validate_provenance.py · validate_backlog.py · build_tracking_sheet.py · instantiate_calendar.py
experiment/active-84-post-plan/matrix_84.csv  ← the matrix
```

**One-sentence rule:** `evidence/` and the organized documents are the working surface, `archive/` is the
pristine record, root `.md` files are current truth, and every historical document is verbatim with its status
in the README beside it.
