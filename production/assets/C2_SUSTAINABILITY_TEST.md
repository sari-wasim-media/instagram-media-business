# C2 sustainability test — protocol and record

**Sourcing Gate item 5:** *two complete C2 pieces produced end-to-end from the chosen route, with elapsed
time and asset count recorded. If two pieces cannot be produced rights-clean inside the declared time budget,
the route fails — the route changes, not the matrix.*

**Status: NOT RUN.** This is founder execution; the protocol below is ready to run.

## Set-up

- **Use the two C2 reserve pieces as the test pieces** (one Reel, one Carousel — see
  `../operations/RESERVE_REGISTER.md`). Their output is needed anyway, and reserve pieces are evergreen by
  definition, so no queue check-out is spent. They enter the reserve only if they pass.
- Ranked-item count as proposed: **7** (or the value the founders lock — the test runs at the locked value).
- Route: the recommended primary **O + F with S as fallback** (`C2_SOURCING_ROUTES.md`). Record every image's
  actual route.
- Declared budgets (`../templates/C2_RANKINGS_AND_TIER_LISTS.md` §8): **Carousel 90 min · Reel 115 min**,
  sourcing included. Pass threshold: each piece within **1.5 ×** its budget (135 / 172 min) **and** all 14
  provenance records complete and valid.
- Two different founders produce one piece each, so the measurement covers both producers.

## Record — piece 1 (Carousel)

| Stage | Started | Finished | Minutes | Notes |
|---|---|---|---|---|
| Theme and item list written (7 items) | | | | |
| Image 1 · route __ · asset ID __ | | | | |
| Image 2 · route __ · asset ID __ | | | | |
| Image 3 · route __ · asset ID __ | | | | |
| Image 4 · route __ · asset ID __ | | | | |
| Image 5 · route __ · asset ID __ | | | | |
| Image 6 · route __ · asset ID __ | | | | |
| Image 7 · route __ · asset ID __ | | | | |
| Provenance rows written | | | | |
| Ranking reasons and chips, sources logged | | | | |
| Layout (9 slides) | | | | |
| Caption, alt text, tags, QA | | | | |
| **Total** | | | **__ / 90 (≤ 135 to pass)** | |

## Record — piece 2 (Reel)

Same table, plus a row for assembly and timing (beats per `C2_RANKINGS_AND_TIER_LISTS.md` §3) and the Reel
duration achieved (target 36.5 s). **Total __ / 115 (≤ 172 to pass).**

## Verdict

| Check | Result |
|---|---|
| Both pieces inside 1.5 × budget | ☐ |
| 14 distinct images, none reused, all in acceptable classes | ☐ (`python3 tools/validate_provenance.py` clean) |
| Route mix observed: O __ · F __ · P __ · X __ · S __ · B __ | |
| Bottleneck stage | |
| Cost incurred | $ |
| **Route passes** | ☐ yes → record in `../gates/SOURCING_GATE_SCORECARD.md` item 5 · ☐ no → change route (`C2_SOURCING_ROUTES.md`, last section), re-run |
| Producers · dates · initials | |

## What the numbers feed

The measured minutes replace the declared budgets in the C2 template and in `../operations/PRODUCTION_RHYTHM.md`;
the observed route mix replaces the planning assumption in `SOURCE_CLASS_DECISION.md` §3; the bottleneck stage
tells the founders where the ≈ 15-hour bank build should spend its next hour.
