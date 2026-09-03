# Tracking

**Status: NOT BUILT. Blocked on the 84-post matrix.**

The tracking sheet is built *from* the locked matrix — one row per planned post. Building it before the matrix
exists would bake in the superseded 48-post structure.

**Do not build this until `../active-84-post-plan/` contains a locked matrix.**

---

## What it will need to contain

Carried from the historical design as a requirement, not a template.

**Per-post row:** post ID · account · week · day · cell · format · slot · publish datetime · T+7 snapshot date
· T+14 snapshot date (Reels) · accounts reached · views · % non-follower reach · likes ÷ reach · comments ÷
reach · sends ÷ reach · saves ÷ reach · profile visits · follows attributed · Reel duration (Reels) · slide
count (carousels) · originality status · any protocol deviation.

**Post ID convention:** `A-W3-C2-CAR-01` — account, week, cell, format, sequence. Put the ID in the asset
filename too, so assets and data never separate.

**Second tab:** account-weekly rows — followers start/end · net change · reach (7d) · % non-follower · profile
visits · external link taps · **Account Status across all five categories** · posts published by format · any
Instagram notification received.

**Third tab:** Stories log.

**Rules that govern the sheet:** every rate metric uses **Reach** as denominator — Views is recorded but never
substituted. No blank cells for any post past T+7. See `../methodology/MEASUREMENT_AND_RULES.md`.
