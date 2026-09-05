# Story Protocol — FOUNDER-LOCKED

**Status: ACTIVE.** Daily Stories are a Founder Lock decision, taken jointly by Sari and Wasim.

Stories are **diagnostic and supporting**. They gate nothing, appear in no scenario definition, and sit
**outside** the 84-slot feed matrix.

---

## 1. The locked protocol

| | |
|---|---|
| **Cadence** | **1 Story per day per account** — 7/week/account · **42/account · 84 combined** over six weeks |
| **Timing** | **17:30 UTC daily**, both accounts (= 20:30 at UTC+3), 90 minutes after the 16:00 UTC feed post. ±30 min tolerance; the actual time is logged |
| **Structure** | Exactly **one frame** per account per day, in the house Story template. Frame content follows a **fixed 7-day rotation, predeclared before Week 1, identical on both accounts, repeated unchanged in all six weeks** |
| **Interactive sticker** | Exactly **one per account per week**, on a fixed weekday, the same weekday on both accounts, all six weeks — 6 per account, 12 total. Sticker frequency is a constant, not a variable |
| **Measurement** | **T+2 snapshot for every Story**: accounts reached · forward taps · back taps · exits · replies · sticker interactions where present. Plus a weekly Story roll-up per account |
| **Missing data** | Log `STORY_DATA_MISSING`. **Never back-fill.** Stories gate nothing, so no further action follows |
| **Production** | Batched weekly and scheduled where the platform permits; otherwise posted manually at the fixed instant within tolerance |

**Frozen for the duration:** cadence · clock instant · rotation · sticker weekday · frame count · structure.

**Not performance-adaptive.** No extra Story for a well-performing post, no Story volume change for any reason.

---

## 2. Why the cadence must be identical and frozen

Beyond the general no-adaptation rule, Story cadence is now **load-bearing**: account-level weekly Reach
aggregates Stories alongside feed posts. Holding Stories at a fixed, identical daily rate on both accounts
means their contribution is a **constant** across accounts and weeks. Any variation between accounts or across
weeks would make account-level figures uninterpretable.

---

## 3. Reconciliation with the breakout rule

Canonical methodology permits supporting a breakout post via Story. Under a fixed daily rotation that support
must fit **inside that day's single Story**. It may **never** add an extra Story, because Story volume is a
frozen variable.

---

## 4. What Stories are NOT

- **Not** a second experiment. There is no Story factorial, no Story arm of the matrix, no Story treatment.
- **Not** a gate. No pass/fail rule, no scenario definition and no decision depends on any Story metric.
- **Not** a follower-liveness instrument. *"Living-follower rate" was withdrawn and stays withdrawn.* The
  active fraction of each follower list is **unknown**, and no metric may divide Story reach by follower count
  and present the result as a share of living followers. See
  `../../strategy/historical/CORRECTIONS_LEDGER.md`, priority correction 2.

Stories are read three ways only: longitudinally within each account · Account A versus Account B on identical
cadence and structure · weeks 1–2 versus weeks 3–6.

---

## 5. Pre-launch work — NOT done

⚠ The **content classes making up the 7-day rotation** must be declared before Week 1. Designing them is
content work and is part of the Week-1 Gate, not part of the locked methodology. See
`../active-84-post-plan/GATES.md` §2.1 item 9.
