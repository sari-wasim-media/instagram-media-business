# Tracking

**Status: NOT BUILT — but no longer blocked.** The matrix is locked, so the sheet can now be built.

Build it directly from **`../active-84-post-plan/matrix_84.csv`**, which already carries all 84 rows with
slot ID, account, week, day, weekday, engine, format, publish instant, block, publishing pair and the AI
overlay flag. Do not retype the matrix — import it.

Building the tracking sheet is a **Week-1 Gate item** (`../active-84-post-plan/GATES.md` §2.1 item 4).

---

## What it must contain

Carried from the historical design as a requirement, not a template.

**Per-post row:** post ID · account · week · day · weekday · engine · format · **AI overlay flag** · publish datetime · T+7 snapshot date
· T+14 snapshot date (Reels) · accounts reached · views · % non-follower reach · likes ÷ reach · comments ÷
reach · sends ÷ reach · saves ÷ reach · profile visits · follows attributed · Reel duration (Reels) · slide
count (carousels) · originality status · any protocol deviation.

**Post ID convention:** `A-W3-C2-CAR-01` — account, week, engine, format, sequence. `REE` Reel · `CAR`
Carousel · `STA` Static. Put the ID in the asset filename too, so assets and data never separate. All 84 IDs
are already assigned in `matrix_84.csv`.

**Second tab:** account-weekly rows — followers start/end · net change · reach (7d) · % non-follower · profile
visits · external link taps · **Account Status across all five categories** · posts published by format · any
Instagram notification received.

**Third tab:** Stories log — **84 rows** (1/day/account × 42 days), with the T+2 snapshot fields from
`../methodology/STORY_PROTOCOL.md` and a flag for the one interactive sticker per account per week.

**Rules that govern the sheet:** every rate metric uses **Reach** as denominator — Views is recorded but never
substituted, and never divided by follower count. No blank cells for any post past T+7. Weekly account-level
Reach and non-follower Reach are recorded as **descriptive context only** and carry no decision authority —
see Rule S in `../methodology/MEASUREMENT_AND_RULES.md` §4.
