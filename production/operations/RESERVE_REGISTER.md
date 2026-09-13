# The 7-piece evergreen reserve — composition and register

**Locked:** ≥ 7 finished pieces banked at all times; a **7-piece evergreen reserve**; **no C1 reserve**
(C1 is never converted to evergreen — the reserve is 7 pieces, not 8); **no reserve piece may be AI-treated**;
a reserve piece fills a slot only for the **same engine and format**, via the exception protocol, and never
an off-matrix slot. Building the reserve is Week-1 Gate Layer 1 item 6.

**Composition — ACTIVE, delegated production decision (2026-09-08)**, chosen so the reserve can answer the
most likely Miss in each non-C1 engine and format, weighted toward Reels (4 of every 7 slots). The three C3
pieces are built from published reports and release notes (the compliant sources), which suit dateless,
evergreen charts:

| # | Reserve ID | Engine | Format | Why this one | Doubles as |
|---|---|---|---|---|---|
| 1 | `RESERVE-C2-REE-01` | C2 | Reel | 12 C2 Reels in the matrix — the most exposed cell | May be filled by promoting stress-test prototype `TEST-C2-REE-01` **after** a pass (see note) |
| 2 | `RESERVE-C2-CAR-01` | C2 | Carousel | 6 C2 carousels; the format most likely to be blocked on imagery | May be filled by promoting stress-test prototype `TEST-C2-CAR-01` **after** a pass (see note) |
| 3 | `RESERVE-C3-REE-01` | C3 | Reel | 12 C3 Reels; research-heavy, most likely to miss a deadline | — |
| 4 | `RESERVE-C3-CAR-01` | C3 | Carousel | 6 C3 carousels | — |
| 5 | `RESERVE-C3-STA-01` | C3 | Static | The one Static in the reserve: cheapest to make, and Statics are the least distribution-relevant arm | — |
| 6 | `RESERVE-C4-REE-01` | C4 | Reel | 12 C4 Reels; a rights-free format (INNER MONOLOGUE with a self-drawn hero, or HOT TAKE TICKET) | — |
| 7 | `RESERVE-C4-CAR-01` | C4 | Carousel | 6 C4 carousels (GROUP CHAT — zero imagery) | — |

Not covered: C2 Static (3 in the matrix), C4 Static (3). If either Misses with no reserve match, the slot
becomes a Miss and recovers at the end of the schedule — the locked path.

**Note (2026-09-13, delegated production decision — order reversed).** The 2026-09-08 composition had the two
C2 reserve pieces *double as* the sustainability-test pieces. Under protocol v2 the two test pieces are
**non-publishing prototypes first**; they become these two reserve pieces only if the test's verdict allows
it, every asset's licence or permission scope covers a later single publication, and QA passes — a separate,
logged promotion step (`../assets/C2_SUSTAINABILITY_TEST.md` §6). If they are not promoted, both reserve
pieces are built fresh and the prototypes' assets are retired. Composition unchanged.

## Rules that travel with every reserve piece

- Fully produced, captioned, alt-texted, rights-cleared and QA'd **before Day 1**; provenance rows under
  the `RESERVE-…` piece reference; validator clean.
- **Evergreen means dateless:** no "this week", no release dates, no current prices unless the caption can
  carry a "data as of" line that will still be honest in six weeks (C3 reserve pieces use MOVE charts over a
  closed window, or SHARE from a published report).
- Subjects obey the anti-duplication rules **at deployment**: before a reserve piece fills a slot, check its
  `subject_key` and thesis against the log (`tools/validate_backlog.py` after logging the substitution as a
  check-out with `rule_applied = RESERVE`). If it collides, it cannot be used there.
- When used, it is **refilled the following week** with a new piece of the same engine and format, so the
  reserve is always 7.
- Never AI-treated; never C1; never used to "improve" a slot — only through the exception protocol
  (production deadline missed, buffer below 7, obsolete subject under 24 h).

## Register

| Reserve ID | Subject (`subject_key`) | Producer | Produced (date) | QA passed | Provenance validated | Used for slot | Refilled by |
|---|---|---|---|---|---|---|---|
| `RESERVE-C2-REE-01` | | | | ☐ | ☐ | | |
| `RESERVE-C2-CAR-01` | | | | ☐ | ☐ | | |
| `RESERVE-C3-REE-01` | | | | ☐ | ☐ | | |
| `RESERVE-C3-CAR-01` | | | | ☐ | ☐ | | |
| `RESERVE-C3-STA-01` | | | | ☐ | ☐ | | |
| `RESERVE-C4-REE-01` | | | | ☐ | ☐ | | |
| `RESERVE-C4-CAR-01` | | | | ☐ | ☐ | | |

## Decision record

| | |
|---|---|
| Composition | as above |
| Decided | 2026-09-08 — delegated production decision (Claude); founders may override before Day 1 |
