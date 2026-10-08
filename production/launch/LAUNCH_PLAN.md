# Launch package — first revival posts (target Fri 2026-10-09, 16:00 UTC)

**Status: READY FOR FOUNDER REVIEW** — prepared by Claude under Agile Revival (`DECISIONS.md`, 2026-10-08).
Nothing has been published or scheduled. Media files are delivered to the founders separately (not in Git);
the specs that reproduce them exactly are in `specs/` and render with
`python3 production/templates/src/render_piece.py production/launch/specs/<spec>.json`.

| Account | Post | Story | Why this piece |
|---|---|---|---|
| **A** `thestreetwearofficial` | **Air Jordan 1 High OG "Royal" — verdict Reel (30.5 s), C1** | "Drops tomorrow — the desk says wait. You?" + poll | The week's headline release drops **Sat 10 Oct**; a verdict the day before is peak search and comment interest. A has Reels history. An opinionated **WAIT** on an icon invites debate (comments) and is useful (saves). Facts only, no third-party imagery — zero rights exposure |
| **B** `sneakerbong` | **"Every sneaker group chat, every month" — group-chat Reel (30.6 s), C4** | "Have you ever 'quit' buying sneakers?" + poll | B's best historical posts were relatable collector humour; this is the most sendable format we have (memes travel by DM). It is B's **first-ever Reel**, house-drawn UI, original writing, zero imagery — zero rights exposure |

Two different categories on day 1 give the first comparable read (release verdict vs commentary).

---

## Account A

**File:** `A-LAUNCH-01-C1-REEL.mp4` (1080 × 1920, 30 fps, H.264, 30.5 s, no audio — add audio at upload).
Cover: the hook frame (`A-LAUNCH-01-C1-REEL__01_hook.png`).

⚠ **Fact check before publishing (1 minute, unless Claude confirms it first once network access is on):** open
the Air Jordan 1 High OG "Royal" listing in Nike SNKRS / nike.com and confirm **all four**: release **Sat
10 Oct 2026** · **$185** (adult) · colorway **Black/Game Royal-White** · sold on **SNKRS and Jordan
retailers**. These come from consistent secondary coverage (Sneaker News, Footwear News/WWD, Sneaker Bar
Detroit — leads only under our source posture). If any differs, do not publish; tell Claude and the frame is
corrected and re-rendered in minutes.

**Caption:**

```
Air Jordan 1 High OG 'Royal' drops Saturday, Oct 10.
Retail $185 · Black/Game Royal-White · SNKRS and Jordan retailers.
Verdict: WAIT — buy at retail or not at all. Miss it? Don't pay resale.
Source: Nike SNKRS listing, checked Oct 8, 2026.
#airjordan1 #aj1royal #sneakerrelease #sneakers
```

**Alt text (cover):** "Text graphic: Air Jordan 1 'Royal' — cop, wait, or pass? The Reel lists the release
facts and gives the verdict: wait."

**Verdict basis (rubric, recorded):** value at retail 1 (fair) · wearability 1 (rotation piece) · availability
2 (wide release) · resale outlook 1 ("no published resale data") = **5/8 → WAIT**.

**Story (same day, ~17:30 UTC):** `A-LAUNCH-01-STORY__poll.png`; add a **poll** sticker in the empty area
(placement guide: `…__poll_GUIDE_do_not_post.png`): options **"Cop at retail" / "Wait"**.

## Account B

**File:** `B-LAUNCH-01-C4-REEL.mp4` (1080 × 1920, 30 fps, H.264, 30.6 s, no audio — add audio at upload).
Cover: the hook frame (`B-LAUNCH-01-C4-REEL__01_hook.png`).

**Caption:**

```
Done buying shoes. Day 3: "it's a restock, restocks don't count."
Every group chat has this person. Sometimes it's you.
#sneakerrestock #sneakercollector #sneakermemes #sneakerhead
```

**Alt text (cover):** "Text graphic: every sneaker group chat, every month. A drawn group chat where someone
quits buying shoes, then buys two pairs on a restock three days later."

**Story (same day, ~17:30 UTC):** `B-LAUNCH-01-STORY__poll.png`; add a **poll** sticker in the empty area:
options **"Yes, for 3 days" / "Never"**.

---

## Rights and provenance summary

| Piece | Imagery | Third-party assets | Facts | Provenance rows |
|---|---|---|---|---|
| A Reel + Story | None — typography only | None | 4 release facts, Nike's own listing (to confirm) | None needed (no image assets) |
| B Reel + Story | House-drawn chat UI (original) | None | None (humour) | None needed |

Originality: all writing original; no reposted file, template, screenshot or watermark. Trademark §5:
"Air Jordan 1" appears only as plain-text identification in house type; no logo, Jumpman, brand colours as
framing, @-mention or endorsement language. No AI imagery anywhere. Faceless. No CTA, no link, no location,
no tags of people or brands.

## Upload steps (Instagram app or Meta Business Suite — 5 minutes per account)

1. **Before the first post — baselines (10 minutes, both accounts):** screenshot **Account Status** (all five
   categories) and the **audience** page (top countries, cities, age, gender) and the last-90-days overview.
   Drop them in the chat; Claude files them in `evidence/`.
2. Confirm **Settings → Accounts Center → Sharing across profiles** is **off** for posts, stories and Reels.
3. New **Reel** → select the MP4 → **audio:** add an instrumental track from Instagram's music library at low
   volume (any track you like; no voiceover) → **cover:** the hook frame → paste the caption → **Advanced:**
   alt text as above, *Share to Facebook* off, no location, no tags, **AI label off** (no AI used) → do not
   tap **Trial**.
4. Publish at **16:00 UTC (19:00 Israel)** on Fri 9 Oct, or schedule it for that time. A first, then B, a
   minute apart (the order does not matter).
5. At ~17:30 UTC post each Story with its poll sticker.
6. Tell Claude the actual publish times and the audio track names; Claude fills `production/tracking/agile_posts.csv`.

## Measurement

Reads at ~48 h (Sun 11 Oct) and 7 d (Fri 16 Oct): Reach, Views, non-follower %, likes, comments, saves,
shares/sends, profile visits, follows, average watch time, Story reach and poll taps. A screenshot of each
post's Insights is enough — Claude transcribes. See `production/tracking/LEARNING_LOOP.md`.

## Days 2–4 — already in progress

| Day | Account | Piece | State |
|---|---|---|---|
| 2 (Sat 10 Oct) | A | **THE RECEIPT carousel — "The true cost of a 'free' raffle"** (C4, 5 slides) | **Rendered draft** (`specs/A-D2-DRAFT-C4-CARO.json`) |
| 2 (Sat 10 Oct) | B | **HOT TAKE TICKET Reel — "Your grail is the first pair you couldn't afford at 15"** (C4, 24 s) | **Rendered draft** (`specs/B-D2-DRAFT-C4-REEL.json`) |
| 3–4 | A | Ranking carousel with rights-clean photography (e.g. "7 white sneakers ranked by how well they age") | Needs network access for route F sourcing (CC0 / Pexels / Unsplash, ownership-checked) |
| 3–4 | B | Market-desk data card from a published report (C3) | Needs network access for the source |
| 3–4 | both | Release-desk verdicts on the following week's confirmed drops | Needs network access to confirm facts |

The day-2 drafts are deliberately imagery-free so they ship regardless of sourcing; after the 48-h read,
the mix shifts toward whatever starts distributing.
