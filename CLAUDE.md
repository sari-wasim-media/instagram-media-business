# Claude Code — project entry point

**Read `HANDOFF.md` first.** It contains current state, hard constraints, completed work, superseded work,
the next task, and git safety rules.

**`WORKFLOW.md` is the canonical working workflow** — founder roles, Claude's execution autonomy, the
escalation rule, the Git flow and its finalization gate, and the safety guardrails. Read it before doing
work. Two things it settles that matter every session:

- Claude has **broad execution autonomy inside an approved task** — read, edit, refactor, script, test,
  research, and decide implementation details without asking.
- **Stop before Git finalization.** Give the active founder the review summary and wait for explicit
  approval before add / commit / push / PR / merge.

Four things that are easy to get wrong here:

1. **The 84-post matrix is FOUNDER-LOCKED and lives at `experiment/active-84-post-plan/matrix_84.csv`.**
   That CSV is the single source of truth. Validate it with `python3 tools/validate_matrix.py`. Do not
   regenerate, re-solve or "improve" it — it is a founder decision, not a design in progress.
2. **The 48-post matrix in `experiment/historical-48-post-design/` is SUPERSEDED.** It is detailed and looks
   authoritative. It was replaced before launch by a 1-post/day/account cadence. Every count in it is sized to
   4 posts/week/account. Never execute it.
3. **Check `strategy/historical/CORRECTIONS_LEDGER.md` before citing any historical document.** They correct
   each other across five generations; several confident claims in the earlier ones were withdrawn.
4. **This project documents and asks — it does not execute outside the repository.** No publishing, no
   automation built, no monetization, and no Git finalization without explicit founder approval. Inside an
   approved task, in this repository, Claude executes freely — see `WORKFLOW.md`.

**Locked is not launched.** The design is complete; publishing is blocked on two operational gates in
`experiment/active-84-post-plan/GATES.md`. Zero revival posts have been published.
