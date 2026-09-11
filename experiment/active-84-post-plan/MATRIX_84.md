# The Locked 84-Post Execution Matrix

**Status: FOUNDER-LOCKED.** Approved jointly by Sari and Wasim. Frozen for the duration of the controlled
revival experiment. No row may be added, removed, reassigned or reordered.

**`matrix_84.csv` in this directory is the canonical machine-readable source of truth.** This document is
derived from it. If the two ever disagree, the CSV wins and this file must be regenerated.
Run `python3 tools/validate_matrix.py` after any change to the CSV.

---

## Reading the matrix

| Column | Meaning |
|---|---|
| **Slot ID** | `account-week-engine-format-sequence`, the adopted convention. `REE` Reel · `CAR` Carousel · `STA` Static. Put the slot ID in the asset filename so assets and data never separate |
| **Acct** | A = `thestreetwearofficial` · B = `sneakerbong` |
| **Wk / Day / Weekday** | **Launch-relative positions.** D1 is the first day of each experiment week and is labelled `Mon`; D7 is the seventh, labelled `Sun`. Day 1 may fall on any calendar weekday (start rule as amended 2026-09-11); the calendar weekday of every slot binds when Day 1 is instantiated and equals the label only when Day 1 is a Monday. Each position maps to one fixed calendar weekday for all six weeks, so the weekday balances below hold in calendar terms — see `LOCK_SPECIFICATION.md` §3 |
| **Engine** | C1 Release & Verdict · C2 Rankings & Tier Lists · C3 Market & Price Intelligence · C4 Original Meme & Commentary |
| **Format** | REEL · CARO (carousel) · STAT (static) |
| **Time** | **16:00 UTC** for all 84 posts (= 19:00 at UTC+3). A fixed instant, not a local wall-clock time |
| **Block** | WARM = weeks 1–2 (warm-up, excluded from the primary read) · STEADY = weeks 3–6 (the primary analysis window) |
| **Pair** | The publishing date. The two rows sharing a Pair ID publish on the same date and never carry the same engine |
| **AI** | `AI` marks one of the six founder-locked AI-imagery sub-test slots. See `AI_IMAGERY_SUBTEST.md` |

---

## The 84 rows

| Slot ID | Acct | Wk | Day | Weekday | Engine | Format | Time (UTC) | Block | Pair | AI |
|---|---|---|---|---|---|---|---|---|---|---|
| `A-W1-C2-REE-01` | A | 1 | D1 | Mon | C2 | REEL | 16:00 | WARM | E01 |  |
| `B-W1-C3-REE-01` | B | 1 | D1 | Mon | C3 | REEL | 16:00 | WARM | E01 |  |
| `A-W1-C1-CAR-01` | A | 1 | D2 | Tue | C1 | CARO | 16:00 | WARM | E02 |  |
| `B-W1-C2-CAR-01` | B | 1 | D2 | Tue | C2 | CARO | 16:00 | WARM | E02 |  |
| `A-W1-C3-CAR-01` | A | 1 | D3 | Wed | C3 | CARO | 16:00 | WARM | E03 |  |
| `B-W1-C4-CAR-01` | B | 1 | D3 | Wed | C4 | CARO | 16:00 | WARM | E03 |  |
| `A-W1-C4-REE-01` | A | 1 | D4 | Thu | C4 | REEL | 16:00 | WARM | E04 |  |
| `B-W1-C2-REE-01` | B | 1 | D4 | Thu | C2 | REEL | 16:00 | WARM | E04 |  |
| `A-W1-C2-REE-02` | A | 1 | D5 | Fri | C2 | REEL | 16:00 | WARM | E05 |  |
| `B-W1-C4-REE-01` | B | 1 | D5 | Fri | C4 | REEL | 16:00 | WARM | E05 |  |
| `A-W1-C1-STA-01` | A | 1 | D6 | Sat | C1 | STAT | 16:00 | WARM | E06 |  |
| `B-W1-C3-STA-01` | B | 1 | D6 | Sat | C3 | STAT | 16:00 | WARM | E06 |  |
| `A-W1-C4-REE-02` | A | 1 | D7 | Sun | C4 | REEL | 16:00 | WARM | E07 |  |
| `B-W1-C1-REE-01` | B | 1 | D7 | Sun | C1 | REEL | 16:00 | WARM | E07 |  |
| `A-W2-C1-REE-01` | A | 2 | D1 | Mon | C1 | REEL | 16:00 | WARM | E08 |  |
| `B-W2-C4-REE-01` | B | 2 | D1 | Mon | C4 | REEL | 16:00 | WARM | E08 | AI |
| `A-W2-C3-REE-01` | A | 2 | D2 | Tue | C3 | REEL | 16:00 | WARM | E09 |  |
| `B-W2-C1-CAR-01` | B | 2 | D2 | Tue | C1 | CARO | 16:00 | WARM | E09 |  |
| `A-W2-C4-CAR-01` | A | 2 | D3 | Wed | C4 | CARO | 16:00 | WARM | E10 | AI |
| `B-W2-C2-REE-01` | B | 2 | D3 | Wed | C2 | REEL | 16:00 | WARM | E10 |  |
| `A-W2-C2-STA-01` | A | 2 | D4 | Thu | C2 | STAT | 16:00 | WARM | E11 |  |
| `B-W2-C3-REE-01` | B | 2 | D4 | Thu | C3 | REEL | 16:00 | WARM | E11 |  |
| `A-W2-C1-REE-02` | A | 2 | D5 | Fri | C1 | REEL | 16:00 | WARM | E12 |  |
| `B-W2-C3-CAR-01` | B | 2 | D5 | Fri | C3 | CARO | 16:00 | WARM | E12 |  |
| `A-W2-C2-CAR-01` | A | 2 | D6 | Sat | C2 | CARO | 16:00 | WARM | E13 |  |
| `B-W2-C1-REE-01` | B | 2 | D6 | Sat | C1 | REEL | 16:00 | WARM | E13 |  |
| `A-W2-C3-REE-02` | A | 2 | D7 | Sun | C3 | REEL | 16:00 | WARM | E14 |  |
| `B-W2-C4-STA-01` | B | 2 | D7 | Sun | C4 | STAT | 16:00 | WARM | E14 | AI |
| `A-W3-C2-REE-01` | A | 3 | D1 | Mon | C2 | REEL | 16:00 | STEADY | E15 |  |
| `B-W3-C1-REE-01` | B | 3 | D1 | Mon | C1 | REEL | 16:00 | STEADY | E15 |  |
| `A-W3-C3-REE-01` | A | 3 | D2 | Tue | C3 | REEL | 16:00 | STEADY | E16 |  |
| `B-W3-C2-REE-01` | B | 3 | D2 | Tue | C2 | REEL | 16:00 | STEADY | E16 |  |
| `A-W3-C2-STA-01` | A | 3 | D3 | Wed | C2 | STAT | 16:00 | STEADY | E17 |  |
| `B-W3-C3-REE-01` | B | 3 | D3 | Wed | C3 | REEL | 16:00 | STEADY | E17 |  |
| `A-W3-C4-CAR-01` | A | 3 | D4 | Thu | C4 | CARO | 16:00 | STEADY | E18 |  |
| `B-W3-C2-CAR-01` | B | 3 | D4 | Thu | C2 | CARO | 16:00 | STEADY | E18 |  |
| `A-W3-C3-CAR-01` | A | 3 | D5 | Fri | C3 | CARO | 16:00 | STEADY | E19 |  |
| `B-W3-C1-STA-01` | B | 3 | D5 | Fri | C1 | STAT | 16:00 | STEADY | E19 |  |
| `A-W3-C1-REE-01` | A | 3 | D6 | Sat | C1 | REEL | 16:00 | STEADY | E20 |  |
| `B-W3-C4-REE-01` | B | 3 | D6 | Sat | C4 | REEL | 16:00 | STEADY | E20 |  |
| `A-W3-C1-REE-02` | A | 3 | D7 | Sun | C1 | REEL | 16:00 | STEADY | E21 |  |
| `B-W3-C3-CAR-01` | B | 3 | D7 | Sun | C3 | CARO | 16:00 | STEADY | E21 |  |
| `A-W4-C3-STA-01` | A | 4 | D1 | Mon | C3 | STAT | 16:00 | STEADY | E22 |  |
| `B-W4-C4-REE-01` | B | 4 | D1 | Mon | C4 | REEL | 16:00 | STEADY | E22 |  |
| `A-W4-C4-REE-01` | A | 4 | D2 | Tue | C4 | REEL | 16:00 | STEADY | E23 | AI |
| `B-W4-C1-REE-01` | B | 4 | D2 | Tue | C1 | REEL | 16:00 | STEADY | E23 |  |
| `A-W4-C1-REE-01` | A | 4 | D3 | Wed | C1 | REEL | 16:00 | STEADY | E24 |  |
| `B-W4-C4-CAR-01` | B | 4 | D3 | Wed | C4 | CARO | 16:00 | STEADY | E24 |  |
| `A-W4-C2-REE-01` | A | 4 | D4 | Thu | C2 | REEL | 16:00 | STEADY | E25 |  |
| `B-W4-C3-STA-01` | B | 4 | D4 | Thu | C3 | STAT | 16:00 | STEADY | E25 |  |
| `A-W4-C1-CAR-01` | A | 4 | D5 | Fri | C1 | CARO | 16:00 | STEADY | E26 |  |
| `B-W4-C2-REE-01` | B | 4 | D5 | Fri | C2 | REEL | 16:00 | STEADY | E26 |  |
| `A-W4-C4-REE-02` | A | 4 | D6 | Sat | C4 | REEL | 16:00 | STEADY | E27 |  |
| `B-W4-C2-CAR-01` | B | 4 | D6 | Sat | C2 | CARO | 16:00 | STEADY | E27 |  |
| `A-W4-C2-CAR-01` | A | 4 | D7 | Sun | C2 | CARO | 16:00 | STEADY | E28 |  |
| `B-W4-C1-REE-02` | B | 4 | D7 | Sun | C1 | REEL | 16:00 | STEADY | E28 |  |
| `A-W5-C4-CAR-01` | A | 5 | D1 | Mon | C4 | CARO | 16:00 | STEADY | E29 |  |
| `B-W5-C2-STA-01` | B | 5 | D1 | Mon | C2 | STAT | 16:00 | STEADY | E29 |  |
| `A-W5-C1-STA-01` | A | 5 | D2 | Tue | C1 | STAT | 16:00 | STEADY | E30 |  |
| `B-W5-C3-REE-01` | B | 5 | D2 | Tue | C3 | REEL | 16:00 | STEADY | E30 |  |
| `A-W5-C4-REE-01` | A | 5 | D3 | Wed | C4 | REEL | 16:00 | STEADY | E31 |  |
| `B-W5-C1-REE-01` | B | 5 | D3 | Wed | C1 | REEL | 16:00 | STEADY | E31 |  |
| `A-W5-C3-CAR-01` | A | 5 | D4 | Thu | C3 | CARO | 16:00 | STEADY | E32 |  |
| `B-W5-C1-CAR-01` | B | 5 | D4 | Thu | C1 | CARO | 16:00 | STEADY | E32 |  |
| `A-W5-C2-REE-01` | A | 5 | D5 | Fri | C2 | REEL | 16:00 | STEADY | E33 |  |
| `B-W5-C4-CAR-01` | B | 5 | D5 | Fri | C4 | CARO | 16:00 | STEADY | E33 | AI |
| `A-W5-C2-REE-02` | A | 5 | D6 | Sat | C2 | REEL | 16:00 | STEADY | E34 |  |
| `B-W5-C3-REE-02` | B | 5 | D6 | Sat | C3 | REEL | 16:00 | STEADY | E34 |  |
| `A-W5-C3-REE-01` | A | 5 | D7 | Sun | C3 | REEL | 16:00 | STEADY | E35 |  |
| `B-W5-C4-REE-01` | B | 5 | D7 | Sun | C4 | REEL | 16:00 | STEADY | E35 |  |
| `A-W6-C1-CAR-01` | A | 6 | D1 | Mon | C1 | CARO | 16:00 | STEADY | E36 |  |
| `B-W6-C3-CAR-01` | B | 6 | D1 | Mon | C3 | CARO | 16:00 | STEADY | E36 |  |
| `A-W6-C2-CAR-01` | A | 6 | D2 | Tue | C2 | CARO | 16:00 | STEADY | E37 |  |
| `B-W6-C4-STA-01` | B | 6 | D2 | Tue | C4 | STAT | 16:00 | STEADY | E37 |  |
| `A-W6-C3-REE-01` | A | 6 | D3 | Wed | C3 | REEL | 16:00 | STEADY | E38 |  |
| `B-W6-C2-REE-01` | B | 6 | D3 | Wed | C2 | REEL | 16:00 | STEADY | E38 |  |
| `A-W6-C1-REE-01` | A | 6 | D4 | Thu | C1 | REEL | 16:00 | STEADY | E39 |  |
| `B-W6-C4-REE-01` | B | 6 | D4 | Thu | C4 | REEL | 16:00 | STEADY | E39 |  |
| `A-W6-C4-REE-01` | A | 6 | D5 | Fri | C4 | REEL | 16:00 | STEADY | E40 |  |
| `B-W6-C3-REE-01` | B | 6 | D5 | Fri | C3 | REEL | 16:00 | STEADY | E40 |  |
| `A-W6-C3-REE-02` | A | 6 | D6 | Sat | C3 | REEL | 16:00 | STEADY | E41 |  |
| `B-W6-C1-CAR-01` | B | 6 | D6 | Sat | C1 | CARO | 16:00 | STEADY | E41 |  |
| `A-W6-C4-STA-01` | A | 6 | D7 | Sun | C4 | STAT | 16:00 | STEADY | E42 | AI |
| `B-W6-C2-REE-02` | B | 6 | D7 | Sun | C2 | REEL | 16:00 | STEADY | E42 |  |

---

## Balance audit

Every table below is computed from the 84 rows above, not from design targets.
`tools/validate_matrix.py` re-derives all of them and fails if any drifts.

### Account × Engine — all six weeks

42 ÷ 4 engines = 10.5, so exact per-account equality is impossible. The residual is 1 post, split complementarily so the **pooled** total is exactly 21 per engine.

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **A** | 11 | 11 | 10 | 10 | **42** |
| **B** | 10 | 10 | 11 | 11 | **42** |
| **Total** | **21** | **21** | **21** | **21** | **84** |

### Account × Engine — W3–6 primary window

**Zero residual.** The entire per-account engine imbalance is confined to the warm-up block.

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **A** | 7 | 7 | 7 | 7 | **28** |
| **B** | 7 | 7 | 7 | 7 | **28** |
| **Total** | **14** | **14** | **14** | **14** | **56** |

### Account × Engine — W1–2 warm-up

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **A** | 4 | 4 | 3 | 3 | **14** |
| **B** | 3 | 3 | 4 | 4 | **14** |
| **Total** | **7** | **7** | **7** | **7** | **28** |

### Account × Format — all six weeks

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **A** | 24 | 12 | 6 | **42** |
| **B** | 24 | 12 | 6 | **42** |
| **Total** | **48** | **24** | **12** | **84** |

### Account × Format — W3–6

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **A** | 16 | 8 | 4 | **28** |
| **B** | 16 | 8 | 4 | **28** |
| **Total** | **32** | **16** | **8** | **56** |

### Engine × Format — pooled, all six weeks

Perfect. Every engine carries an identical format mix, so "this engine won" and "this engine got more Reels" are separable.

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **C1** | 12 | 6 | 3 | **21** |
| **C2** | 12 | 6 | 3 | **21** |
| **C3** | 12 | 6 | 3 | **21** |
| **C4** | 12 | 6 | 3 | **21** |
| **Total** | **48** | **24** | **12** | **84** |

### Engine × Format — Account A

Exactly 6 Reels and 3 Carousels per engine. The only per-account residual in the whole design is the Static column.

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **C1** | 6 | 3 | 2 | **11** |
| **C2** | 6 | 3 | 2 | **11** |
| **C3** | 6 | 3 | 1 | **10** |
| **C4** | 6 | 3 | 1 | **10** |
| **Total** | **24** | **12** | **6** | **42** |

### Engine × Format — Account B

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **C1** | 6 | 3 | 1 | **10** |
| **C2** | 6 | 3 | 1 | **10** |
| **C3** | 6 | 3 | 2 | **11** |
| **C4** | 6 | 3 | 2 | **11** |
| **Total** | **24** | **12** | **6** | **42** |

### Engine × Format — Account A, W3–6

**Zero residual.** A complete 4R / 2C / 1S per engine.

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **C1** | 4 | 2 | 1 | **7** |
| **C2** | 4 | 2 | 1 | **7** |
| **C3** | 4 | 2 | 1 | **7** |
| **C4** | 4 | 2 | 1 | **7** |
| **Total** | **16** | **8** | **4** | **28** |

### Engine × Format — Account B, W3–6

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **C1** | 4 | 2 | 1 | **7** |
| **C2** | 4 | 2 | 1 | **7** |
| **C3** | 4 | 2 | 1 | **7** |
| **C4** | 4 | 2 | 1 | **7** |
| **Total** | **16** | **8** | **4** | **28** |

### Week × Engine — pooled

Every engine appears in every week on both accounts, so week-level shocks and the production learning curve hit all engines rather than concentrating on one.

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **1** | 3 | 4 | 3 | 4 | **14** |
| **2** | 4 | 3 | 4 | 3 | **14** |
| **3** | 4 | 4 | 4 | 2 | **14** |
| **4** | 4 | 4 | 2 | 4 | **14** |
| **5** | 3 | 3 | 4 | 4 | **14** |
| **6** | 3 | 3 | 4 | 4 | **14** |
| **Total** | **21** | **21** | **21** | **21** | **84** |

### Week × Engine — Account A

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **1** | 2 | 2 | 1 | 2 | **7** |
| **2** | 2 | 2 | 2 | 1 | **7** |
| **3** | 2 | 2 | 2 | 1 | **7** |
| **4** | 2 | 2 | 1 | 2 | **7** |
| **5** | 1 | 2 | 2 | 2 | **7** |
| **6** | 2 | 1 | 2 | 2 | **7** |
| **Total** | **11** | **11** | **10** | **10** | **42** |

### Week × Engine — Account B

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **1** | 1 | 2 | 2 | 2 | **7** |
| **2** | 2 | 1 | 2 | 2 | **7** |
| **3** | 2 | 2 | 2 | 1 | **7** |
| **4** | 2 | 2 | 1 | 2 | **7** |
| **5** | 2 | 1 | 2 | 2 | **7** |
| **6** | 1 | 2 | 2 | 2 | **7** |
| **Total** | **10** | **10** | **11** | **11** | **42** |

### Week × Format — Account A

Identical every week on both accounts: the locked 4R / 2C / 1S mix.

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **1** | 4 | 2 | 1 | **7** |
| **2** | 4 | 2 | 1 | **7** |
| **3** | 4 | 2 | 1 | **7** |
| **4** | 4 | 2 | 1 | **7** |
| **5** | 4 | 2 | 1 | **7** |
| **6** | 4 | 2 | 1 | **7** |
| **Total** | **24** | **12** | **6** | **42** |

### Week × Format — Account B

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **1** | 4 | 2 | 1 | **7** |
| **2** | 4 | 2 | 1 | **7** |
| **3** | 4 | 2 | 1 | **7** |
| **4** | 4 | 2 | 1 | **7** |
| **5** | 4 | 2 | 1 | **7** |
| **6** | 4 | 2 | 1 | **7** |
| **Total** | **24** | **12** | **6** | **42** |

### Weekday × Engine — Account A, W3–6

**Every engine appears exactly once on every weekday.** In the primary window, engine is perfectly orthogonal to weekday.

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **Mon** | 1 | 1 | 1 | 1 | **4** |
| **Tue** | 1 | 1 | 1 | 1 | **4** |
| **Wed** | 1 | 1 | 1 | 1 | **4** |
| **Thu** | 1 | 1 | 1 | 1 | **4** |
| **Fri** | 1 | 1 | 1 | 1 | **4** |
| **Sat** | 1 | 1 | 1 | 1 | **4** |
| **Sun** | 1 | 1 | 1 | 1 | **4** |
| **Total** | **7** | **7** | **7** | **7** | **28** |

### Weekday × Engine — Account B, W3–6

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **Mon** | 1 | 1 | 1 | 1 | **4** |
| **Tue** | 1 | 1 | 1 | 1 | **4** |
| **Wed** | 1 | 1 | 1 | 1 | **4** |
| **Thu** | 1 | 1 | 1 | 1 | **4** |
| **Fri** | 1 | 1 | 1 | 1 | **4** |
| **Sat** | 1 | 1 | 1 | 1 | **4** |
| **Sun** | 1 | 1 | 1 | 1 | **4** |
| **Total** | **7** | **7** | **7** | **7** | **28** |

### Weekday × Engine — Account A, all six weeks

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **Mon** | 2 | 2 | 1 | 1 | **6** |
| **Tue** | 2 | 1 | 2 | 1 | **6** |
| **Wed** | 1 | 1 | 2 | 2 | **6** |
| **Thu** | 1 | 2 | 1 | 2 | **6** |
| **Fri** | 2 | 2 | 1 | 1 | **6** |
| **Sat** | 2 | 2 | 1 | 1 | **6** |
| **Sun** | 1 | 1 | 2 | 2 | **6** |
| **Total** | **11** | **11** | **10** | **10** | **42** |

### Weekday × Engine — Account B, all six weeks

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **Mon** | 1 | 1 | 2 | 2 | **6** |
| **Tue** | 2 | 2 | 1 | 1 | **6** |
| **Wed** | 1 | 2 | 1 | 2 | **6** |
| **Thu** | 1 | 2 | 2 | 1 | **6** |
| **Fri** | 1 | 1 | 2 | 2 | **6** |
| **Sat** | 2 | 1 | 2 | 1 | **6** |
| **Sun** | 2 | 1 | 1 | 2 | **6** |
| **Total** | **10** | **10** | **11** | **11** | **42** |

### Weekday × Format — Account A

**The one imbalance that cannot be removed:** 24 Reels do not divide into 7 weekdays. Constrained to 3–4 Reels, 1–2 Carousels, 0–1 Static per weekday, with the two accounts' zero-Static weekdays deliberately offset (A: Friday · B: Wednesday).

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **Mon** | 3 | 2 | 1 | **6** |
| **Tue** | 3 | 2 | 1 | **6** |
| **Wed** | 3 | 2 | 1 | **6** |
| **Thu** | 3 | 2 | 1 | **6** |
| **Fri** | 4 | 2 | 0 | **6** |
| **Sat** | 4 | 1 | 1 | **6** |
| **Sun** | 4 | 1 | 1 | **6** |
| **Total** | **24** | **12** | **6** | **42** |

### Weekday × Format — Account B

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **Mon** | 4 | 1 | 1 | **6** |
| **Tue** | 3 | 2 | 1 | **6** |
| **Wed** | 4 | 2 | 0 | **6** |
| **Thu** | 3 | 2 | 1 | **6** |
| **Fri** | 3 | 2 | 1 | **6** |
| **Sat** | 3 | 2 | 1 | **6** |
| **Sun** | 4 | 1 | 1 | **6** |
| **Total** | **24** | **12** | **6** | **42** |

### Weekday × Account

| | A | B | Total |
|---|---|---|---|
| **Mon** | 6 | 6 | **12** |
| **Tue** | 6 | 6 | **12** |
| **Wed** | 6 | 6 | **12** |
| **Thu** | 6 | 6 | **12** |
| **Fri** | 6 | 6 | **12** |
| **Sat** | 6 | 6 | **12** |
| **Sun** | 6 | 6 | **12** |
| **Total** | **42** | **42** | **84** |

### Block × Engine — pooled

| | C1 | C2 | C3 | C4 | Total |
|---|---|---|---|---|---|
| **WARM** | 7 | 7 | 7 | 7 | **28** |
| **STEADY** | 14 | 14 | 14 | 14 | **56** |
| **Total** | **21** | **21** | **21** | **21** | **84** |

### Block × Format — pooled

| | REEL | CARO | STAT | Total |
|---|---|---|---|---|
| **WARM** | 16 | 8 | 4 | **28** |
| **STEADY** | 32 | 16 | 8 | **56** |
| **Total** | **48** | **24** | **12** | **84** |

### Contamination structure

| Check | Value |
|---|---|
| Publishing dates (pairs) | 42, two rows each |
| Dates where both accounts publish the **same engine** | **0** — structural, by design |
| Dates where both accounts publish the same **format** | 21 — unavoidable, 4+4 Reels in 7 days |

### AI-imagery sub-test overlay

| Slot ID | Acct | Wk | Weekday | Format | Block |
|---|---|---|---|---|---|
| `B-W2-C4-REE-01` | B | 2 | Mon | REEL | WARM |
| `A-W2-C4-CAR-01` | A | 2 | Wed | CARO | WARM |
| `B-W2-C4-STA-01` | B | 2 | Sun | STAT | WARM |
| `A-W4-C4-REE-01` | A | 4 | Tue | REEL | STEADY |
| `B-W5-C4-CAR-01` | B | 5 | Fri | CARO | STEADY |
| `A-W6-C4-STA-01` | A | 6 | Sun | STAT | STEADY |

Account 3/3 · format 2/2/2 · one Reel + one Carousel + one Static per account · 3 WARM / 3 STEADY ·
every format 1 WARM / 1 STEADY · all six in C4 · **zero AI slots in Week 1** · no two on the same date.
C1, C2 and C3 contain no AI-treated posts in any window. Full specification: `AI_IMAGERY_SUBTEST.md`.

