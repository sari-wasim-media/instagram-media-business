# Scheduling procedure and publish settings — held fixed for all 84 posts and 84 Stories

**Status: ACTIVE — delegated production decision (2026-09-08).** The publish instant (16:00 UTC), the
scheduling rule (all posts scheduled in advance) and the manual-fallback alternation are founder-locked
(`LOCK_SPECIFICATION.md` §3). The per-post settings below are the composer toggles that would otherwise vary
silently; they are declared once here, under the founders' delegated production authority, so they are
identical on both accounts for every post.

## 1. The publish settings — every feed post

| Setting | Value | Why |
|---|---|---|
| Schedule time | **16:00 UTC** exactly (19:00 at UTC+3 · 18:00 at UTC+2 · 12:00 EDT / 11:00 EST · 09:00 PDT / 08:00 PST) | Locked |
| Reels: "Also share to feed" | **ON** | Reels are feed posts in the locked 1/day cadence and must appear in the grid |
| Reels: Trial | **Never tap Trial** | Trial reels change distribution; the feature is opt-in per reel |
| Reels: allow remix / allow download | Platform defaults, left unchanged on both accounts | Constants, not variables |
| Reel cover | The hook frame, from the file, no custom crop beyond the 4:5 grid crop | House rule |
| Audio | A track from Instagram's Sound Collection, chosen at upload, logged in `../assets/audio_ledger.csv` | Only library cleared for business accounts; 14-day rules |
| Caption | Full caption in the caption field, hashtags last line; nothing in a first comment | `CAPTION_AND_HASHTAG_POLICY.md` |
| Alt text | Written for every image / slide / cover | Policy |
| Share to Facebook (per post "Also share on…") | **OFF** | No cross-posting (locked) |
| Accounts Center → Sharing across profiles (posts, stories, reels) | **OFF** on both accounts, verified at Week 0 | No cross-posting (locked) |
| Recommend reel on Facebook | OFF | Same |
| Location tag | **None** | A location is an unmeasured variable |
| Tag people / collaborator / product (shopping) tags | **None** | No Collabs, no advertiser adjacency (locked) |
| Hide like counts | OFF | Constant |
| Comments | ON | `COMMENT_REPLY_POLICY.md` |
| "Add AI label" | **ON for the six AI slots only; OFF everywhere else** | `AI_IMAGERY_POLICY_PACK.md` |
| Boost / promote | **Never** | No paid promotion (locked) |
| Pinned posts, highlights | Unchanged for the duration | Frozen profile variables |

## 2. Scheduling procedure — feed posts

1. **Where.** Instagram's in-app scheduler (public professional accounts: reels, photos and carousels; up
   to 25 a day, **up to 30 days ahead**) or Meta Business Suite (desktop or mobile). One tool for both
   accounts for the whole test; proposed: **Business Suite on desktop** because Meta documents Story
   scheduling there (sticker preservation unverified — see §4).
2. **Time-zone check, once per account before Week 1.** Business Suite displays times in the connected
   Page's time zone; the app uses the device's. Schedule a test post for a known UTC instant, read it back in
   the scheduled-content list, and confirm the displayed time converts to 16:00 UTC. Record the offset used.
3. **When.** All 11 non-C1 Week-1 posts are scheduled before Day 0 (Layer 1). Later weeks are scheduled as
   pieces pass QA, always ≥ 12 h before the instant; C1 posts by their **T−12 h** deadline.
4. **Proof.** Screenshot the scheduled-content entry (date, time, account) and note it in the tracking row
   (`scheduled_at_utc`). This is the artefact the Week-1 Gate asks for ("scheduled in-platform").
5. **Verify after publish.** Within the day, record `actual_publish_utc` from the post's own timestamp. A
   post that publishes the same day but late is marked `LATE`; more than three `LATE` rows on one account
   triggers the scheduling-process review at the weekly review.

## 3. Manual fallback (locked rule, restated)

If a post must be published by hand, the account published first alternates by pair number — **A first on
odd pairs, B first on even** — so a few minutes' lag never correlates with account. Both actual timestamps
are logged. Never publish two feed posts on one account on one day.

## 4. Stories

One frame per account per day at **17:30 UTC** (± 30 min tolerance, actual time logged). Meta's help pages
describe Story scheduling in Business Suite (desktop and mobile); **whether a scheduled Story keeps an
interactive poll or quiz sticker is unverified** and is not assumed.

- **Non-sticker days (six per week):** schedule in Business Suite where the Week-0 test (§2 step 2, repeated
  for a Story) shows the frame publishes intact at the instant; otherwise post manually inside the tolerance.
- **Wednesday, the sticker day: post manually** at 17:30 UTC ± 30 min, adding the poll or quiz sticker in the
  Instagram app at posting time, on both accounts, all six weeks — unless a test on the real account, recorded
  in the Stories tab notes, proves the chosen scheduler preserves the sticker exactly. Until that record
  exists, manual is the procedure.
- Never two Stories on one account on one day. No Facebook cross-share of Stories.

## 5. Daylight-saving note

The instant is UTC and does not move. Local wall-clock conversions change on **25 Oct 2026** (EU/UK) and
**1 Nov 2026** (US); the founders' own zone is unnamed in the repository and may or may not shift. Re-run
the time-zone check (§2 step 2) in the week of any transition. `tools/instantiate_calendar.py` flags whether
the six weeks straddle either date once a start Monday is given.

## 6. Decision record

| | |
|---|---|
| Scheduling tool | Meta Business Suite, desktop (Instagram in-app scheduling as the fallback) |
| Settings table | as above |
| Decided | 2026-09-08 — delegated production decision (Claude); founders may override before Day 1 |
