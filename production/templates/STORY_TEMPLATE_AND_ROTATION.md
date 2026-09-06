# Story template, 7-day rotation and the interactive-sticker weekday

**Status: PROPOSED — founder review required.** The Story *protocol* is locked
(`../../experiment/methodology/STORY_PROTOCOL.md`): one frame per account per day at 17:30 UTC ± 30 min,
a fixed 7-day rotation predeclared before Week 1 and identical on both accounts, exactly one interactive
sticker per account per week on a fixed weekday, T+2 snapshots, diagnostic only. What was **not** yet
declared — the content classes in the rotation, the sticker weekday and the frame template — is proposed
here. Specimens: `renders/story/`.

---

## 1. The frame

1080 × 1920, ink ground, the house top band placed below the 250 px safe zone reading
`STORY · <WEEKDAY> · <CLASS>` with the account handle, bottom band above the 260 px reply zone reading
`Daily · 17:30 UTC · one frame`. Content in the same components as the feed (kicker, title, rows, plate,
stamp, chip, mosaic). The frame takes the **accent of the engine its class is adjacent to**, so the Story
looks like the desk it came from.

**Nothing links out.** No post-link stickers, no "see feed post" prompts: a Story that drives traffic to a
feed post on a fixed weekday would add a weekday-correlated contribution to that post's reach. Stories stay
self-contained. The one exception is the locked breakout rule — support for a breakout post happens inside
that day's single Story, and is logged.

## 2. The proposed 7-day rotation

| Day | Class | Adjacent engine · accent | What the frame holds | Sticker |
|---|---|---|---|---|
| **Mon** | **DROP CALENDAR** | C1 · blue | This week's *confirmed* drops as rows (day · product · price). Three to five rows | — |
| **Tue** | **PRICE CHECK** | C3 · green | One number: a resale or spread figure with basis and "as of" date | — |
| **Wed** | **THE POLL** | C2 · yellow | A two-option "settle it" question in the house split layout with the **poll sticker** placed in the marked zone | **Poll (or quiz)** |
| **Thu** | **DESK NOTES** | neutral · paper accent | An editorial note: how we rank, a correction, a method line, a reader question answered in text | — |
| **Fri** | **THE VERDICT** | C1 · blue | One stamp — COP / WAIT / PASS — on the weekend's drop, one line of reasoning | — |
| **Sat** | **TWO SHOES** | C4 · pink | The C4 split format, one ruling, two owned/licensed/self-drawn plates | — |
| **Sun** | **THE WEEK** | neutral | A mosaic of the week's own artwork thumbnails (no links) and a one-line "next week" | — |

The rotation repeats unchanged for all six weeks on both accounts. Content differs by account and by week;
class, order, frame and timing never do.

Why this order: the week opens with the calendar the audience needs, closes with a recap, and puts the one
interactive frame mid-week where it neither coincides with the Monday activity peak the evidence shows for
Account B nor with the weekend. Each class costs under 15 minutes to produce, which keeps the 14 Stories a
week inside the ≈ 3 h/week estimate in `GATES.md` §3.

## 3. The interactive-sticker weekday — proposed: Wednesday

Exactly one sticker per account per week (locked). Proposed weekday: **Wednesday**, on THE POLL frame, the
same on both accounts, all six weeks. A poll sticker by default; a quiz sticker is permitted on the same
frame when the question has a factual answer (a price, a year). No other frame in the week carries any
interactive sticker — no question boxes, sliders, link stickers or countdowns. Reactions and replies are
not stickers and need no rule.

Recorded in the tracking sheet's Stories tab as `sticker=Y` on every Wednesday row.

## 4. Production

Batch the coming week's 14 frames in one sitting on the previous Thursday (see
`../operations/PRODUCTION_RHYTHM.md`), from the same house frames. Wednesday's poll question and Friday's
verdict may be finalised later in the week because they depend on C1 and C2 subjects, but the frame is
prepared in the batch. Schedule in Meta Business Suite (desktop or mobile), which schedules Instagram Stories;
if scheduling is unavailable on a given day, post manually at 17:30 UTC within the ± 30 min tolerance and log
the actual time. Never two Stories on one account on one day.

## 5. Anti-duplication and originality

The same rules as the feed: never the same file on both accounts; never the same specific subject on both
accounts within 14 days; different source imagery on every frame; own artwork only in THE WEEK mosaic. Stories
are not reposts of anything, ever — no resharing of other accounts' Stories or posts, no user-generated
content, no screenshots. Story frames are outside the AI sub-test: **no AI imagery in any Story.**

## 6. Measurement fields (from the locked protocol)

T+2 snapshot per Story: viewers (accounts reached) · views · forward taps · back taps · exits · replies ·
sticker interactions (Wednesday only) · actual publish time · deviations. Weekly Story roll-up per account.
Missing data is logged `STORY_DATA_MISSING` and never back-filled. Stories gate nothing.

## 7. Founder decision record

| | |
|---|---|
| Rotation | ☐ as proposed · ☐ amended: ______ |
| Sticker weekday | ☐ Wednesday (proposed) · ☐ other: ______ |
| Sticker type | ☐ poll by default, quiz allowed (proposed) · ☐ poll only |
| Sari / Wasim | ☐ / ☐ · date ______ |
