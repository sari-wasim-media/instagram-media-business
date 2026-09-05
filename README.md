# Instagram Media Business — Sari & Wasim

Canonical shared source of truth for the revival of two dormant sneaker/streetwear Instagram accounts into a
faceless media business.

**This repository replaces Claude.ai chat history as the project record.** Any future session — any account,
any machine — can continue from here without reconstructing anything.

---

## The two assets

| Account | Followers | Posts | Last active | Status |
|---|---|---|---|---|
| `thestreetwearofficial` | ~23.9K | 1,265 | into late 2023 | All five Account Status categories green |
| `sneakerbong` | ~20.8K | 1,033 | 2021 | All five Account Status categories green |

Both are Professional accounts and recommendation-eligible as last observed. Founders Sari and Wasim are equal
50/50 partners.

## What this project is

Reviving two dormant accounts as a **faceless** media business — neither founder appears on camera or becomes
the public personality behind the accounts. The immediate goal is not revenue. It is a single testable
question:

> **Can either account obtain recommendation distribution to non-followers, with original content, in 2026?**

A controlled revival experiment is designed to answer that before any monetization decision is made.

## Current phase — pre-launch, design complete and locked

**The experiment has not started. Zero revival posts published. Launch is gated and not authorized.**

✅ **The balanced 84-post matrix is designed, validated and FOUNDER-LOCKED** —
`experiment/active-84-post-plan/matrix_84.csv`.

| | |
|---|---|
| Cadence | 1 feed post/day/account · 7/week/account · 14 combined/week · 6 weeks · **84 feed posts** |
| Format mix | **4 Reels + 2 Carousels + 1 Static** per account per week |
| Publish instant | **16:00 UTC**, both accounts, all 84 posts. Held fixed, not tested |
| Stories | **1/day/account** — 84 combined. Diagnostic only, outside the matrix |
| AI imagery | **Exactly 6 posts, C4 only** — a logged nested sub-test |
| Start date | **Not chosen.** The first Monday after both launch gates pass |

**What still blocks launch:** the Sourcing Gate (imagery rights for C2 at volume, plus the AI arm) and the
two-layer Week-1 Gate. See `experiment/active-84-post-plan/GATES.md`.

An earlier 48-post matrix was fully designed and locked, then **superseded before launch** when the founders
increased cadence. It is preserved as historical methodology and must not be executed.

---

## Canonical documents

| File | What it is |
|---|---|
| **`HANDOFF.md`** | **Start here if you are a fresh Claude Code session** |
| **`experiment/active-84-post-plan/`** | **The founder-locked 84-post design, and the gates that block launch** |
| `PROJECT_STATE.md` | Current state as of 2026-09-05 — the operational source of truth |
| `DECISIONS.md` | Decision register: ACTIVE / SUPERSEDED / DEFERRED / HISTORICAL |
| `WORKFLOW.md` | Workflow V1 — how the founders and Claude Code work: autonomy, escalation, Git flow |
| `ROADMAP.md` | Completed · Current · Next · Later |

## Directory map

| Path | What it holds |
|---|---|
| `experiment/active-84-post-plan/` | **The locked matrix (`matrix_84.csv`), lock spec, AI sub-test, gates** |
| `experiment/` | Methodology, content engines, tracking, and the superseded 48-post design |
| `tools/` | `validate_matrix.py` — re-derives every locked balance property from the matrix |
| `strategy/` | Business context and the recovered research chain |
| `evidence/` | 42 organized screenshots — account status, demographics, performance, cleanup, profiles |
| `archive/raw-migration-source/` | Both migration packages, pristine and unmodified |

## Where raw evidence lives

`evidence/` holds organized, renamed copies with a full index at `evidence/README.md`.
`archive/raw-migration-source/` holds the two delivered packages byte-for-byte, with checksums and provenance.
**The archive is never modified** — if an organized copy is ever wrong, the archive settles it.

Recovered historical documents are preserved **verbatim**. Their status, lineage and corrections live in
adjacent README files and in `strategy/historical/CORRECTIONS_LEDGER.md`.

---

## What to read next

**Continuing the work?** → `HANDOFF.md`

**About to do work in this repository?** → `WORKFLOW.md`

**Want the current state?** → `PROJECT_STATE.md`

**Wondering whether something was decided?** → `DECISIONS.md`

**About to cite a historical document?** → `strategy/historical/CORRECTIONS_LEDGER.md` first. Those documents
correct each other across five generations, and several confident-sounding claims in the earlier ones were
withdrawn by the later ones.

---

## Working rules

The full working workflow is `WORKFLOW.md`. The rules that never move:

- **Nothing is published** to either Instagram account without founder approval. Launch is gated.
- **The locked matrix and methodology do not move.** Only the founders can change a founder-locked decision.
- **Nothing is committed, pushed or merged** without the active founder's explicit approval of finalization.
- **No secrets in this repository** — no passwords, tokens, API keys, or 2FA recovery codes.
- **Never rewrite git history** without explicit founder approval for that specific operation.
- **Never edit `archive/raw-migration-source/` or the recovered historical documents.**
