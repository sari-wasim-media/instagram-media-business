# Active 84-Post Plan — FOUNDER-LOCKED

# ✅ THE 84-POST MATRIX IS DESIGNED, VALIDATED AND FOUNDER-LOCKED.

Approved jointly by Sari and Wasim. This directory holds the active, locked execution design for the
controlled revival experiment.

⚠ **Locked is not launched. Publishing is NOT authorized.** Both gates in `GATES.md` must pass first, and
zero revival posts have been published.

---

## What is here

| File | What it is | Status |
|---|---|---|
| **`matrix_84.csv`** | **The canonical machine-readable matrix. The single source of truth.** 84 rows, one per feed post | **LOCKED** |
| `MATRIX_84.md` | The same 84 rows, human-readable, plus the full balance audit. Derived from the CSV | **LOCKED** |
| `LOCK_SPECIFICATION.md` | Exactly what is frozen and what is deliberately late-bound; timing definition; statistical honesty | **LOCKED** |
| `AI_IMAGERY_SUBTEST.md` | The six-slot nested AI-imagery sub-test: scope, prohibitions, disclosure, analysis rule | **LOCKED** |
| `ANTI_DUPLICATION_AND_TOPIC_SELECTION.md` | Contamination rules and the blind-to-performance topic check-out queue | **LOCKED** |
| `EXCEPTION_PROTOCOL.md` | Pre-declared failure, recovery and hard-stop handling | **LOCKED** |
| `GATES.md` | **The Sourcing Gate and the two-layer Week-1 Gate. Launch is gated here** | **BINDING — NOT PASSED** |

Validate the matrix at any time with `python3 tools/validate_matrix.py` from the repository root.

---

## The locked design in one table

| | |
|---|---|
| Accounts | 2 — `thestreetwearofficial` (A) and `sneakerbong` (B), tested concurrently, identical structure |
| Cadence | **1 feed post/day/account** · 7/week/account · 14 combined/week |
| Duration | **6 posting weeks** + measurement tail |
| Total | **84 feed posts — 42 per account** |
| Format mix | **4 Reels + 2 Carousels + 1 Static** per account per week — **LOCKED** |
| Engines | C1 Release & Verdict · C2 Rankings & Tier Lists · C3 Market & Price Intelligence · C4 Original Meme & Commentary |
| Publish instant | **16:00 UTC**, both accounts, all 84 posts (= 19:00 at UTC+3). Held fixed, not tested |
| Blocks | W1–2 warm-up · **W3–6 primary analysis window** |
| Stories | **1/day/account** — 42/account, 84 combined. Diagnostic only, outside the matrix |
| AI imagery | **Exactly 6 posts, C4 only**, 3 per account, 1 Reel + 1 Carousel + 1 Static each |
| Voiceover | **None** for the duration of the test |
| Link in bio | **None** for the duration of the test |
| Start date | **Not chosen.** The first Monday after both gates pass |

---

## Why this design

**The primary analysis window is balanced in itself, not merely as part of a balanced whole.** Weeks 3–6 give
28 posts per account: 28 ÷ 4 engines = 7 exactly, and 4R/2C/1S per week × 4 weeks = 16R/8C/4S, which divides
by 4 engines into exactly **4 Reels + 2 Carousels + 1 Static per engine per account.** Zero residual anywhere
in the window that decides go/no-go.

**The unavoidable imbalance is quarantined.** 42 ÷ 4 = 10.5, so exact per-account engine equality is
impossible. The residual is one post per engine, it is **complementary across accounts** (pooled totals are
exactly 21 each), it lives **only in the Static format**, and it lives **only in the warm-up block**.

**Format is exactly orthogonal to engine.** Pooled, every engine carries 12 Reels, 6 Carousels and 3 Statics.
Per account, every engine carries exactly 6 Reels and 3 Carousels. "This engine won" and "this engine got more
Reels" are separable.

**Reels cadence sits at market norm.** 4 Reels/week/account ≈ 17/month, inside the 17–20/month tier band. The
superseded 48-post design ran ~8.7/month and openly accepted that "insufficient Reels volume" would remain a
live alternative explanation for a negative result. **That hole is closed.**

---

## What still blocks launch

1. **Sourcing Gate** — including the AI arm. See `GATES.md` §1.
2. **Week-1 Gate** — 11 non-C1 Week-1 pieces finished and scheduled, the D2 C1 topic locked, templates, Story
   readiness, reserve, backlog, tracking sheet. See `GATES.md` §2.
3. Then, and only then, the start date is instantiated as the **first Monday** after both gates pass.

---

## Superseded

The 48-post execution matrix is **historical methodology only** and must never be executed. See
`../historical-48-post-design/`. Every count in it is sized to 4 posts/week/account.
