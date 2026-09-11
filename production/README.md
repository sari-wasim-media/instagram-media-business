# Production — the creative system and pre-launch operating surface

**What this directory is.** Everything the founders need to turn the founder-locked 84-post design into
posts: the house creative system for C1–C4 and Stories, the asset and rights pipeline, the policy pack of
held-fixed production variables, the topic queue, the operating rhythm, and the two gate scorecards. It was
built in the Creative System + Pre-Launch Foundations sprint (2026-09-05/06) and **stops before Week-1
production and launch**.

**What it is not.** It changes nothing that is locked. The matrix, the format mix, the engines, the publish
instant, the analysis windows, the measurement rules, the AI sub-test, daily Stories and the start rule all
stand exactly as `experiment/active-84-post-plan/` states them. Where this surface fixes a value the lock
left open (templates, the C2 count, the Story rotation, the disclosure wording, the publish settings), it now
does so as an **ACTIVE — delegated production decision** under the founders' delegation of 2026-09-08
(`DECISIONS.md`); the founders may override any of them before Day 1.

**The trademark / trade-dress posture was ACCEPTED by the founders on 2026-09-08** —
`TRADEMARK_RISK_REVIEW.md`. Photographs of branded sneakers are produced under its §5 nominative-use
operating rule, mandatory on every piece and checked at QA.

## Map

| Path | Holds | Status |
|---|---|---|
| **`TRADEMARK_RISK_REVIEW.md`** | The focused risk review, the accepted posture and the §5 operating rule | **ACCEPTED 2026-09-08** |
| `FOUNDER_REVIEW_QUEUE.md` | The former queue, resolved: 13 items decided under delegated authority; the founder-only items listed | Resolved 2026-09-08 |
| **`PRE_LAUNCH_RUNBOOK.md`** | The ordered founder path from here to both gates passed (≈ 60 h) | Ready |
| `house-style/` | House System v1: `HOUSE_STYLE.md`, `EDITORIAL_VOICE.md`, `tokens.json`, `house.css`, vendored OFL fonts | Decided 2026-09-08 |
| `templates/` | C1 · C2 (+ the ranked-item count decision) · C3 · C4 · Story specs; `template_constants.json`; the specimen renderer; **64 rendered frames** and a 36.5 s Reel pacing reference | Decided 2026-09-08 |
| `assets/` | Source-class decision, C2 route stack, sustainability-test protocol, the compliant data-source register, research record, provenance register + audio ledger (empty, with examples) | Order and sources decided; trademark acceptance open; founder execution pending |
| `policy/` | AI-imagery policy pack, caption/hashtag, comment-reply, the originality rule card, scheduling and publish settings | Decided 2026-09-08 |
| `backlog/` | The topic queue, the check-out log, examples, the idea bank | Instrument built; empty |
| `operations/` | Production rhythm, the C1 deadline ladder (21 slots, launch-relative), the reserve register, the pre-publish QA checklist, `TOOLING.md` | Decided 2026-09-08 |
| `gates/` | Sourcing Gate and Week-1 Gate scorecards — item-by-item status | Sourcing 5 of 12 passed; Week-1 Layer 1 2 of 11 passed |

Related, outside this directory: `experiment/tracking/` (the tracking sheet skeleton: 84 post rows, 18
account-weekly rows, 84 Story rows, XLSX with Reach-denominated formulas) and `tools/` (the validators and
generators below).

## The pipeline in one line

> idea bank → queue entry (timestamp) → **check-out by the queue rule** (Friday, two weeks ahead; C1 at
> T−48 h) → research sheet + sources → **assets with provenance IDs** → layout in the house template →
> caption, alt text, tags → **QA by the other founder** → scheduled at 16:00 UTC with a screenshot →
> T+7 / T+14 / T+2 rows → weekly review (no strategy talk).

## Tools

| Command | What it does |
|---|---|
| `python3 tools/validate_matrix.py` | Unchanged — the locked matrix's own checker |
| `python3 tools/build_tracking_sheet.py` | Regenerates the tracking skeleton from the matrix (refuses to overwrite data) |
| `python3 tools/validate_provenance.py` | Provenance register + audio ledger against the rights and 14-day rules |
| `python3 tools/validate_backlog.py [--start YYYY-MM-DD]` | Queue rule, deadlines, anti-duplication, blind attestation |
| `python3 tools/instantiate_calendar.py --start YYYY-MM-DD --print` | Local calendar (writes to `_local/`, never the repo): every instant, the C1 ladder, snapshots, DST notes |
| `python3 production/templates/src/render_frames.py [--motion]` | Re-renders the specimen frames (needs a Chromium) |

None of this is publishing automation, a dashboard or a scraper: the scripts read and write files in this
repository and print. Publishing, Insights capture and data collection stay manual (locked).

## Who decided what — the short version

| Founder-locked (do not touch) | Delegated production decisions (Claude, 2026-09-08; founders may override before Day 1) | Open — founders only |
|---|---|---|
| The 84 rows · 4R/2C/1S · C1–C4 · 16:00 UTC · six weeks · W1–2 / W3–6 · no voiceover · no link · six AI slots · daily Stories at 17:30 UTC with one sticker per week · no adaptation · zero reposts · frozen profile · start rule (as amended 2026-09-11: begin as soon as the gates pass, any weekday) · **and from 2026-09-08:** the delegation itself · the editorial-desk brand posture · the conservative data-source posture · tool autonomy without spending | House System v1 + editorial voice · C2 count = 7 · verdict scale · Story rotation + Wednesday sticker · disclosure line and placement · AI tool (Firefly) · source-class order · compliant data sources · caption/hashtag form · comment policy · scheduling tool + settings · reserve composition · queue-rule readings · producer allocation · production tooling | Firefly licence confirmation (the reading is prepared in `assets/FIREFLY_TERMS_VERIFICATION.md`), account and any paid plan · any paid stock · Git finalization (the trademark posture was answered on 2026-09-08: ACCEPT) |
