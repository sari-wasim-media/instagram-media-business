# Handoff — Start Here

**For a fresh Claude Code session with no prior chat history, on any account or machine.**

This repository is self-contained. You do not need any Claude.ai conversation to continue this project.

---

## 1. Read these, in this order

1. **`PROJECT_STATE.md`** — what is true right now. The single most important file.
2. **`DECISIONS.md`** — what was decided, and what is still open.
3. **`WORKFLOW.md`** — how work is done here: autonomy, escalation, and the Git flow.
4. **`experiment/README.md`** — experiment status at a glance.
5. **`strategy/historical/CORRECTIONS_LEDGER.md`** — **read before citing anything historical.**

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
- The active cadence is **1 feed post/day/account → 84 planned posts over 6 weeks**.
- **The 84-post matrix does not exist yet.** Creating it is the next task.

---

## 3. Hard constraints — do not violate

| Constraint | Detail |
|---|---|
| **Faceless** | Neither founder appears on camera, in photographs, in video, or as the public personality behind either account. **Voiceover is not prohibited by this but is NOT approved — it needs founder sign-off** |
| **No replica/counterfeit advertisers** | Permanent. Also excludes bot/proxy vendors, follower-growth services, crypto/NFT-adjacent, gambling, dropship arbitrage |
| **Zero reposts during the experiment** | Original or materially enhanced content only |
| **Profile frozen** | Username, display name, bio, photo, link, pins, highlights, posting times — all frozen for the experiment's duration |
| **No paid promotion, giveaways, Collabs or advertiser outreach** | During the controlled test |
| **No performance-based adaptation** | The matrix is frozen once started. Outliers change nothing |
| **No monetization commitments** | Not before the experiment produces data |
| **No automation built** | Claude Code's authorised scope so far is documentation only |

---

## 4. Completed — do not redo

- Strategic audit, and the full Phase 1 + Phase 2 research round → `strategy/research/`
- Account data collection: status, demographics, geography, 90-day passive performance, historical samples
  → `evidence/`
- The revival experiment methodology, designed and locked across four correction generations
- 2FA on both accounts
- Targeted removal of three UAPLG/counterfeit promotions (documented first)
- The Week 0 profile edit — **minimal by decision**: the follower-goal line was removed from each bio and the
  rest kept substantially unchanged. ⚠ **An earlier draft proposed rewriting both bios; the founders did not
  apply it. Do not treat that rewrite as pending work** — the profile is frozen
- This repository migration

⚠ **Do not re-run market research.** It exists, and much of it was corrected — read the ledger rather than
regenerating it.

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

---

## 6. Immediate next task

> **Create and lock a balanced 84-post matrix** — 7 feed posts/week/account, 6 posting weeks, 42 per account,
> 84 total, controlling account × format × content-cell × posting-slot as far as integer constraints allow.

**Before you start:**
- Read `experiment/active-84-post-plan/README.md` — the requirements.
- Read `experiment/methodology/CADENCE_DEPENDENCY_MAP.md` — what carries forward and what must be re-derived.
- Use `experiment/historical-48-post-design/PATCH_AND_FREEZE_48_POST_MATRIX.md` §2 as a **model of method**.
  **Copy the method, not the numbers.**

Then, in order: tracking sheet → topic backlog → imagery sourcing → produce all 14 Week-1 pieces and schedule
them → launch.

---

## 7. Needs founder approval before you act

- **Designing the 84-post matrix** — approved as the next task in principle, but confirm before generating it.
- **Locking the weekly format mix** (~4 Reels + 2 Carousels + 1 Static is intended, not locked).
- **Any voiceover use** — not covered by an existing decision.
- **Setting a link in bio** — deferred; if wanted, it must happen before Post #1.
- **Publishing anything at all.**
- **Any monetization, pricing or advertiser contact.**
- **Building automation, dashboards or tracking software.**
- **Renaming `sneakerbong`** — deferred until after revival evidence.
- **Git finalization of any task** — add / commit / push / PR / merge. See `WORKFLOW.md` §4.

When in doubt about anything **outside this repository**, this project's default is to **document and ask**,
not to execute. Inside an approved task, in this repository, Claude executes and reports afterwards.

---

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
strategy/           context + research     experiment/      methodology + plans
evidence/           organized screenshots  archive/         pristine originals
```

**One-sentence rule:** `evidence/` and the organized documents are the working surface, `archive/` is the
pristine record, root `.md` files are current truth, and every historical document is verbatim with its status
in the README beside it.
