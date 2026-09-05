# Exception and Recovery Protocol — FOUNDER-LOCKED

**Status: ACTIVE.** Pre-declared so that no judgement call is invented after data starts arriving.

**Governing principle, carried forward from the locked methodology:**
*An extended calendar is preferable to an unbalanced dataset.*

---

| Event | Rule |
|---|---|
| **Scheduled topic becomes obsolete / release delayed or cancelled** | Release the subject back to the backlog marked `INVALID`. Draw the next eligible item by the queue rule. **Slot ID, account, engine, format, weekday and instant unchanged.** If under 24 h remain, fill from the evergreen reserve for the **same engine and format**; if none exists, the slot becomes a Miss. Log the substitution |
| **Platform upload failure** | Retry immediately. If published the same calendar day, mark `LATE` with the actual timestamp and continue. If it cannot publish that day, treat as a **Miss**. **Never publish two feed posts on one account on one day** — daily cadence is a held-fixed variable |
| **Post publishes late (<24 h, same day)** | Mark `LATE`, record the actual timestamp. The row stays in analysis. More than 3 `LATE` rows on one account triggers a scheduling-process review at the weekly review |
| **Miss — slot not published on its date** | Recover at the **end of the schedule, on the same weekday and the same instant**, so weekday and time balance are preserved exactly and only block membership changes. Mark `RECOVERED`. A recovered W3–6 slot is **excluded from the W3–6 window analysis** (declared in the final read) and included in the all-weeks pooled analysis. **Never shift the rest of the calendar** |
| **An AI-treated slot Misses** | Recovered by the same path, **retaining its AI treatment**. No reserve piece may be AI-treated |
| **Instagram removes or restricts a post** | Screenshot the notice and the exact guideline named. Mark `REMOVED`, exclude from all analysis, recover the slot at end of schedule preserving engine/format/weekday/instant. If it is an **IP report or content-removal notice** → **hard stop: pause both accounts and investigate before resuming** |
| **Account Status leaves green (any of five categories)** | **Hard stop for that account.** Screenshot the flagged item and the guideline named; request review if offered. That account's series ends at that date; its remaining rows are marked `INCOMPLETE`. **The other account continues.** If the trigger followed an AI-treated post, log the AI treatment as a candidate cause |
| **An account temporarily loses a feature** (cannot post Reels, audio unavailable, scheduling disabled) | **Do not substitute a different format** — that would break format balance. Mark the slot `BLOCKED`, publish nothing on that account that day, recover at end of schedule. If the block persists more than 7 days, escalate to the founders as a partial hard stop |
| **T+7 data unavailable** | Capture at the earliest available time and **record the actual age in days**. If actual age deviates from 7 days by more than 48 h, mark `AGE_DEVIATION` and exclude from the primary median, retaining it in a sensitivity read. **Never back-fill estimates** |
| **T+14 Reel data unavailable** | Same handling, flagged. T+7 remains primary, so the row survives |
| **T+2 Story data unavailable** | Log `STORY_DATA_MISSING`. No back-fill. Stories gate nothing, so no further action |
| **Founder misses a production deadline / bank falls below 7** | Fill from the evergreen reserve for the **same engine and format**. If the reserve holds no matching piece, the slot becomes a **Miss**. **Never** fill with an off-matrix piece, a different engine, a different format, or a repost |
| **A C1 slot misses its T−24 h production deadline** | It becomes a **Miss** and flows through the recovery path above. It is **never** converted to evergreen content — that contradicts the C1 engine definition — and is never replaced by an off-matrix post. **C1 has no evergreen reserve piece for exactly this reason; the reserve is 7 pieces, not 8** |
| **Slot cannot meet the content-quality minimum in time** | Publish nothing. Treat as a Miss. A substandard piece contaminates its engine's median more than a missing row does |
| **Unoriginal asset published** | **Protocol violation, not an emergency.** Log it; do **not** panic-delete (deletion is an unrecorded account-state change mid-measurement); exclude the observation; replace preserving account, engine, format, weekday and instant, extending the calendar if needed; **do not pause the account; no clock resets.** Escalate at 3+ on one account within any 30-day window → production-process review |
| **Cumulative published below 80% of plan at any checkpoint** | **Extend the calendar to complete all 84 posts.** Do not shrink the matrix to fit the calendar |
| **Analytics change, metric removed, or Insights layout changes** | Record exactly what is unavailable and from which date; capture whatever substitute Instagram provides; note the affected rows. Do not back-fill. **Do not change the posting plan** |
| **Breakout post** | Record as ceiling/breakout evidence. Story and comment support permitted inside that day's single scheduled Story. **Nothing in the schedule changes.** No replication until the locked test completes |
| **One account's reach exceeds the other's by >3× for two consecutive weeks** | Note it and continue. **This is the account effect being measured** |
| **Zero non-follower reach on all Reels for two consecutive weeks on one account** | Verify no unoriginal asset entered the set, verify Reel durations are in band, check Account Status. **No allocation change** |

---

## Never, during the six posting weeks

Move effort between accounts · alter engine, format or slot allocation · change the publish instant · change
display name, bio, profile photo, pinned posts or link in bio · change username · add or drop an engine · run
paid promotion, giveaways, Collabs or advertiser outreach · cross-post · attempt to replicate a breakout ·
use AI imagery outside the six locked slots · change Story cadence.
