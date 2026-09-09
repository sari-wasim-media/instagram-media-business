# Workflow V1 — how Sari and Wasim work in this repository

**Status: ACTIVE.** This is the canonical working workflow for this project. It governs *how work is done in
this repository* — founder roles, Claude Code's autonomy, the escalation rule, the Git flow, and the safety
guardrails.

It does **not** change any business, experiment or platform decision. Those live in `DECISIONS.md` and remain
in force exactly as written. See [§9](#9-what-this-workflow-does-not-change).

---

## 1. Core working model

- **Sari and Wasim are equal founders.** Neither outranks the other.
- **A task that has been handed to Claude is already agreed.** Before beginning or continuing a task, assume
  the two founders have discussed and approved it. Claude does not re-open the question of whether the task
  should be done.
- **One founder normally works at a time.** Simultaneous work is uncommon. The founder running the current
  session is the **active founder** — the person Claude reports to, asks, and takes approval from.
- **GitHub is the canonical shared source of truth.** Not chat history, not a local machine.
- **Each task normally gets its own branch**, created from an up-to-date `main`.
- **Auto Mode is the default operating mode** for Claude Code on this project.

## 2. Claude's autonomy

Within an approved task, Claude has **broad execution autonomy**. Claude may:

- read any repository context it considers useful;
- create, edit, move, refactor or delete files as the task requires;
- install packages, write scripts, run tests, change configuration, use the GitHub CLI;
- perform whatever research the execution needs;
- make reasonable technical, editorial and product **implementation** decisions in service of the founders'
  goals and vision.

**Use best judgment rather than interrupting.** Routine and low-risk decisions are Claude's to make and to
report afterwards, not to ask about first.

## 2a. Delegated production authority (founder decision, 2026-09-08)

For the controlled revival experiment the founders have delegated **production-level decision authority** to
Claude: the creative system, visual and production design, sourcing implementation, platform operating
details, workflow, content-production and template mechanics, operational policies, tooling recommendations,
and queue / reserve / scheduling implementation details. Claude decides these itself, records each as
**ACTIVE — delegated production decision** in `DECISIONS.md`, and does not return specialist details to the
founders.

The delegation is bounded by §3 below, sharpened as follows. Claude must still escalate anything that changes
an existing Founder Lock, the 84-post matrix, the methodology or an experimental decision rule; creates a
material new business, legal, platform or account risk; requires spending money or accepting a paid
subscription or licence; requires an irreversible external action; requires publishing, scheduling, outreach
or account changes not already authorised; or creates a genuine contradiction in the canon. Tool *selection*
is delegated; *purchase* and the acceptance of external terms on the founders' behalf are not.

## 3. Escalation rule

Solve low-risk problems independently. **Stop and inform the active founder before proceeding** if something
discovered during the work would:

| Trigger | Example |
|---|---|
| Materially change project scope or direction | The task turns out to require redesigning the experiment |
| Contradict a locked founder decision | A cleaner solution would break a `DECISIONS.md` **ACTIVE** entry |
| Create significant risk | Account risk, legal risk, loss of evidence or provenance |
| Require an irreversible external action | Publishing, deleting content, anything outside this repository |
| Otherwise be a substantive decision the founders should make | A business, strategy or monetization call |

When the trigger fires, surface it with the options and a recommendation. Do not quietly pick one.

## 4. Git workflow

```
sync main  →  task branch  →  work (Auto Mode)  →  validate  →  REVIEW SUMMARY  →  ⛔ approval  →  finalize
```

1. **Start from current `main`** and pull/sync before creating the branch.
2. **Create the task branch** from that up-to-date `main`. Suggested shape: `founder/short-task-name`
   (e.g. `wasim/workflow-v1`, `sari/84-post-matrix`).
3. **Do the work on the task branch.** Claude executes freely here in Auto Mode.
4. **Validate** when the substantive work is complete — test, review or check it in whatever way fits the
   change.
5. **Stop before Git finalization** and give the active founder a concise summary of:
   1. what was completed,
   2. important files and areas changed,
   3. validation / tests performed,
   4. notable decisions, risks, or remaining items.
6. ⛔ **Do not add, commit, push, open a PR or merge until the active founder explicitly approves
   finalization.** This gate is the one hard stop in the normal flow.
7. **After approval**, Claude performs the complete finalization flow as appropriate: `add`, `commit`, push the
   branch, open or update the PR, and merge.

**Merge to `main` is the default after approval**, unless the founder explicitly says otherwise.

## 5. Canonical documentation

- **Update the canonical state documents whenever the project state actually changes** — `PROJECT_STATE.md`,
  `HANDOFF.md`, `DECISIONS.md`, `ROADMAP.md`, `README.md` and the relevant `README.md` inside a subdirectory.
- **Do not generate noisy updates for trivial changes.** A typo fix is not a state change.
- **Tell the founder which canonical documents were updated**, as part of the review summary.
- At the end of meaningful finalized work, leave the repository **clear and synchronized** — ready for the
  other founder, or a fresh Claude session, to continue without reconstruction.

## 6. Safety and Git-history guardrails

**Never commit sensitive material.** No secrets, credentials, API keys, access tokens, passwords, 2FA codes,
recovery codes, session cookies, or anything similar. `.gitignore` catches common patterns; the rule is
enforced by judgment, not by the file.

**Never perform destructive or history-rewriting Git operations automatically.** Each of the following
requires the active founder's explicit approval **for that specific operation**:

- `git push --force` (and `--force-with-lease`)
- destructive `git reset`
- rewriting or rebasing already-published history
- amending a pushed commit
- any equivalent destructive or history-rewriting operation

**Preserved material — never modify:**

- `archive/raw-migration-source/` — the pristine record. If an organized copy is wrong, fix the copy.
- Recovered historical documents, which are preserved verbatim. Corrections belong in
  `strategy/historical/CORRECTIONS_LEDGER.md` and in the README files beside them.

## 7. Parallel work

Simultaneous work is uncommon, so this stays lightweight:

- If both founders do work at the same time, each uses a **separate task branch**.
- Avoid working the same task or the same files without coordinating first.
- If a meaningful merge conflict occurs, **do not silently pick a business or strategy outcome.** Where the
  conflict is between two founder-approved states, surface it and let the founders decide. Mechanical
  conflicts (formatting, ordering, unrelated hunks) are Claude's to resolve.

## 8. Session behavior

There is **no fixed reading checklist**. Claude inspects whatever repository context the task needs, and may
read more whenever it is useful. `CLAUDE.md` and `HANDOFF.md` are the natural entry points because they carry
the traps worth knowing early — not because every session is required to read a set list.

## 9. What this workflow does not change

Workflow V1 is about *how work happens in this repository*. It grants no authority outside it. Unchanged, and
still binding:

- **Nothing is published** to either Instagram account without founder approval.
- **No automation, dashboards, tracking software or publishing tooling** is built without founder approval.
- **No monetization, pricing or advertiser contact** without founder approval.
- Every **ACTIVE** entry in `DECISIONS.md`, including the standing business and experiment constraints, and
  the hard constraints in `HANDOFF.md` §3.

Broad execution autonomy inside an approved task is not authority to widen the task.
