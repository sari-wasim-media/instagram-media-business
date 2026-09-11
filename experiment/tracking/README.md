# Tracking

**Status: SKELETON BUILT (2026-09-06) — not yet live.** The three tabs exist with every row pre-populated
from the locked matrix and every measurement cell empty. "Live" (Week-1 Gate item 4) means the founders have
adopted it as their working sheet and filled the Week-0 baseline rows.

Built directly from **`../active-84-post-plan/matrix_84.csv`** by `tools/build_tracking_sheet.py` — the
matrix is imported, never retyped. The script refuses to regenerate over a sheet that already holds data.

| File | Rows | What it is |
|---|---|---|
| `posts.csv` | 84 | One row per feed post: identity columns imported from the matrix (never edited) · production fields · T+7 snapshot · T+14 snapshot (Reels) · community and compliance · deviations |
| `account_weekly.csv` | 18 | Two accounts × W0 (baseline), W1–W6, W7–W8 (measurement tail): followers, weekly Reach (descriptive only), profile visits, **Account Status across all five categories**, published counts, buffer, notifications |
| `stories.csv` | 84 | One row per Story (1/day/account × 42 days) with the rotation class, the sticker flag on the fixed weekday, and the T+2 fields |
| `tracking_sheet.xlsx` | — | The same three tabs plus a README tab, with the per-reach rate columns as formulas that divide by Reach and nothing else, drop-down statuses, frozen headers |

Post-ID convention `A-W3-C2-CAR-01` (account · week · engine · format · sequence; `REE` / `CAR` / `STA`) is
carried from the matrix; Story IDs are `A-W1-D1-ST`. Put the slot ID and the asset ID in every filename so
assets and data never separate (`../../production/assets/ASSET_PIPELINE.md`).

## Rules that govern the sheet (locked)

- **Reach is the denominator for every rate metric.** Reach is the unique-accounts figure Instagram reports
  for the post; record it in the `*_reach` columns. **The label the Insights UI puts on that figure
  ("Accounts reached" or "Viewers") is unverified until observed per format on both real accounts** at the
  Week-0 baseline; the label does not change the rule. **Views** (plays including repeats) is recorded but is
  never a denominator and is never divided by follower count.
- **T+7** for every feed post · **T+14** additionally for every Reel · **T+2** for every Story. Record the
  actual age in days; a deviation of more than 48 h is flagged `AGE_DEVIATION` and excluded from the primary
  median. **Never back-fill estimates.**
- No blank measurement cells for any post past T+7.
- Weekly account-level Reach and non-follower Reach are **descriptive context only** — Rule S,
  `../methodology/MEASUREMENT_AND_RULES.md` §4.
- The six AI slots carry `ai_overlay = AI`; `ai_platform_label_observed` is filled at T+7 for those six only.
- `publish_date` stays empty until Day 1 exists; fill it from the local output of
  `tools/instantiate_calendar.py`. The date is never committed to the repository.
- Every `asset_ids` entry must exist in `production/assets/provenance_register.csv`; every `checkout_id` in
  `production/backlog/checkout_log.csv`.

## Week-0 verification still needed

Before Day 1, record on both accounts, per format, the exact Insights field names shown for unique accounts
(Reach), for plays (Views) and for the follower / non-follower split, so the columns map to real fields.
Write the observed names into the README tab of the XLSX. If a field is unavailable, record exactly what is
unavailable and from which date (exception protocol) — do not substitute.
