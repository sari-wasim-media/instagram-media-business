# Pre-Launch Lock Specification — FOUNDER-LOCKED

**Status: ACTIVE.** Approved jointly by Sari and Wasim. This document states exactly what is immutable for the
duration of the controlled revival experiment, and what is deliberately left late-bound.

⚠ **The lock does not authorise launch.** Launch is gated separately — see `GATES.md`.

---

## 1. Frozen — immutable from lock until the decision point

### Matrix and schedule
1. **All 84 slot rows** exactly as in `matrix_84.csv`: slot ID, account, week, weekday, engine, format, block,
   publishing pair. No row may be added, removed, reassigned or reordered.
2. **The start date**, once instantiated, and therefore the calendar date of every slot.
3. **Publish instant: 16:00 UTC** for all 84 posts, both accounts.
4. **The weekly format mix 4 Reels + 2 Carousels + 1 Static** per account per week, and the per-engine format
   totals it produces.
5. **Block definitions and analysis windows**: W1–2 warm-up · W3–6 primary window.
6. **Daily cadence**: exactly one feed post per account per day. Never two on one account on one day.

### Measurement
7. **T+7** snapshot for every feed post · **T+14** additionally for every Reel · **T+2** for every Story ·
   account-weekly rows · full audience snapshot at Week 0 and at the decision point.
8. **Reach is the denominator for every rate metric.** Views is recorded but is never a denominator and is
   never substituted for Reach. No metric uses total followers as a denominator unless its numerator is a
   follower-specific figure reported by Instagram.
9. **Medians are the primary comparative statistic.** Maximum reported separately as ceiling evidence.
10. **The ≥2× declared engine-win rule**, plus the requirement that the same direction hold on both accounts.
    **There is no sub-2× cutoff of any kind** — sub-2× separations are reported descriptively with no decision
    authority.
11. **The account × engine interpretation rule**: an engine that dominates on only one account is an
    account-specific result and is never generalised.
12. **Rule S** — the per-post read is the sole decision authority; the former weekly account-level Reach
    safeguard is removed. See `../methodology/MEASUREMENT_AND_RULES.md`.

### Content and behaviour
13. **Zero unoriginal / reposted feed posts.**
14. **No voiceover** for the duration of the test (Founder Lock; test-specific, not a permanent business ban).
15. **AI-generated imagery only in the six locked C4 slots**, under `AI_IMAGERY_SUBTEST.md` in full.
16. **Frozen profile variables**: username · display name · bio · profile photo · **no link in bio** · pinned
    posts · highlights · posting times · comment-reply policy · follow/unfollow · editorial role · historical
    feed.
17. **Held-fixed production variables**: hashtag policy (one policy, both accounts, all 84 posts — 3–5
    topically specific tags in the caption, no follow-bait or generic reach tags) · comment-reply policy (one
    declared policy applied identically) · **Reel duration 20–59 s**, target 30–45 s, never over 90 s ·
    **carousel 5–10 slides** · **C2 ranked-item count** fixed at template lock · aspect ratios · house
    templates · no boosting · no cross-posting · no trial reels · no Collabs · no paid promotion · no
    giveaways · no advertiser outreach.
18. **Story protocol** — daily, both accounts, per `../methodology/STORY_PROTOCOL.md`.
19. **Anti-duplication rules and the topic check-out mechanism** — `ANTI_DUPLICATION_AND_TOPIC_SELECTION.md`.
20. **The content-quality minimum** — `GATES.md` §4.
21. **The exception and recovery protocol** — `EXCEPTION_PROTOCOL.md`.
22. **Post-ID convention and tracking-sheet schema** — `../tracking/README.md`.
23. **The production-buffer policy**: ≥7 finished pieces banked at all times · the **7-piece evergreen
    reserve** (no C1 reserve) · no reserve piece may be AI-treated.

### No adaptation, at any point
24. **All six posting weeks are frozen.** Specifically prohibited: extra slots for a leading engine · dropping
    an engine for weak performance · increasing a format allocation · reallocating toward the stronger
    account · changing the publish instant · changing a profile variable because conversion looks weak ·
    changing an account's editorial role · replicating or chasing a breakout · adding or dropping an engine ·
    moving effort between accounts.
25. **Virality changes nothing.** A breakout is recorded as ceiling/breakout evidence, may be supported inside
    that day's single scheduled Story and in comments, and triggers no schedule change and no replication
    until the locked test completes.
26. **The mid-test checkpoint has no allocation authority.** It is a diagnostic, safety and data-quality
    review only. Observations about which engines or account look stronger are recorded, not acted on.

---

## 2. Deliberately NOT frozen — late-bound by rule

| Item | Bound when | Governed by |
|---|---|---|
| The **specific subject** of every slot | At check-out, by queue rule — never six weeks ahead | `ANTI_DUPLICATION_AND_TOPIC_SELECTION.md` |
| **C1 subjects** specifically | T−48 h, by the release-date queue rule | same |
| Creative execution inside the house template | At production | — |
| Exact hook and caption wording | At production | — |
| Which founder produces which piece | At production; logged | — |
| Audio selection | At production, subject to the duplication rules | same |
| Story frame content | At production, inside the fixed rotation | `../methodology/STORY_PROTOCOL.md` |
| Week 7+ recovery dates | Only if the exception protocol fires | `EXCEPTION_PROTOCOL.md` |
| Everything after the decision point | After results exist | — |

---

## 3. Timing definition — read this before instantiating dates

**The locked value is an absolute instant: 16:00 UTC.** It is recorded as "19:00 local at UTC+3", but the UTC
instant is what binds.

**Why UTC and not local wall-clock.** The repository records only that the founder device time zone reads
GMT+3, without naming a location. Some UTC+3 zones are permanent; others are UTC+3 only in summer. Anchoring
to UTC makes the frozen variable actually frozen: it is immune to any transition in the founders' local zone,
it produces the fewest discontinuities in audience-facing time, and it remains inside the evidenced 18:00–21:00
local activity window under either local offset (at UTC+2, 16:00 UTC = 18:00 local).

**Conversions for the intended launch period** (US DST in force until **Sunday 1 November 2026**):

| | US Eastern | US Pacific |
|---|---|---|
| Sept–Oct 2026 (DST) | **12:00 noon EDT** | **09:00 PDT** |
| After 1 Nov 2026 | 11:00 EST | 08:00 PST |

**DST provision.** Record at instantiation whether the six posting weeks straddle a DST transition in either
zone. Under the start rule as amended on 2026-09-11 (begin as soon as the gates pass, any weekday) the date is
set by readiness, not chosen for the calendar: any Day 1 on or after 2026-09-21 straddles the 1 November US
change, and the gates cannot realistically pass before then. So **log the transition date as a known event
and do not chase it** — changing the instant mid-test would breach the frozen-variable rule.
`tools/instantiate_calendar.py` prints the straddle check.

**Weekday provision.** The matrix's `day` / `weekday` columns are launch-relative positions (D1 labelled
`Mon` … D7 labelled `Sun`). Day 1 may fall on any weekday; each position then maps to one fixed calendar
weekday for all six weeks, so every balance property in §1 holds in calendar terms. The calendar script
emits both the label and the real weekday.

**Operational rule.** All 84 posts are **scheduled in advance**, not published manually. If a post must be
published manually, the account published first alternates by pair number (A first on odd pairs, B first on
even) so any few-minute lag never correlates with account. Actual publish timestamps are logged for all 84.

---

## 4. Why posting time is held fixed rather than counterbalanced

The historical 48-post design used two counterbalanced clock times (19:00 / 19:45) to fix a real flaw: slot was
welded to account. **A single identical instant for both accounts fixes that flaw completely — a constant
cannot confound anything.** The competition rationale that justified two slots was explicitly withdrawn as
unevidenced in the same historical document, and at daily cadence a two-slot scheme could not be balanced
exactly against format *and* engine *and* weekday *and* week for both accounts simultaneously.

**Posting time is therefore a held-fixed control, not an experimental factor.** "Best posting time" is not
tested here and is a candidate follow-up only after the decision point. **Early/Late is not part of this
design.**

---

## 5. Statistical honesty — what this design does and does not buy

| Effect | n, all weeks | n, W3–6 | Status |
|---|---|---|---|
| Account | 42 vs 42 | 28 vs 28 | Cleanly estimable **as a composite**, not as a cause |
| Format | 48 / 24 / 12 | 32 / 16 / 8 | Cleanly estimable |
| Engine | 21 each | 14 each | Cleanly estimable — the primary analysis |
| Account × engine | 11 / 10 per cell | **7 per cell, fully balanced** | Cleanly estimable across all formats in the primary window |
| Account × engine, Reels only | 6 per cell | 4 per cell | Fully balanced in both windows |

**The design removes confounds; it does not manufacture statistical power.** Only large differences are
readable, which is why the ≥2× rule exists. Static conclusions are weak by construction (12 pooled, 3 per
engine). The account effect bundles follower count, audience composition, dormancy depth, historical feed and
**Account B never having published a Reel** — it is never to be read as a claim about any one of those.

Medians measure the middle, not the tail, and theme-page economics are tail-driven. **Absence of a viral hit
is not evidence that breakouts are impossible.**

---

## 6. The cadence caveat, recorded before any data exists

The absolute per-post reach-rate bands were derived for a design publishing 4 posts/week/account and are
applied here at 7/week/account. They are kept unchanged — altering them without evidence would be arbitrary —
but they bias toward a false negative on per-post rates.

**Scenario H is nonetheless cadence-robust**, because its third condition (non-follower share <25%) is
Reach-denominated: publishing more posts lowers reach *per post*, but does not mechanically lower the
*fraction* of each post's reach that comes from non-followers. Full rule, including the mandatory dilution
note and the residual-case rule, is in `../methodology/MEASUREMENT_AND_RULES.md`.
