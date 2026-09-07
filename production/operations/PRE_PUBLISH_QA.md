# Pre-publish QA — the checklist every piece passes before it is scheduled

Built from the locked **content-quality minimum** (`GATES.md` §4), the anti-duplication rules, the AI
sub-test, the policy pack and the templates. **If a piece fails any item and cannot be fixed before its
deadline, publish nothing** — a Miss is better than a substandard piece (locked). QA is done by the founder
who did **not** produce the piece.

## A. Every piece

☐ **Original.** No third-party file, no watermark, no reposted template, no screenshot of another account.
Every pixel traces to "us", "licensed — archived", "permitted — archived" or "AI, in one of the six slots".
☐ **Provenance.** Every image has an `AST-nnnn` row; the ID is in the filename and the tracking row; no ID
used on any other piece; `python3 tools/validate_provenance.py` is clean.
☐ **Facts.** Every price, date, name and figure verified against a named source recorded in the tracking row.
No number without a source; no source, no number.
☐ **Template.** The correct house template, engine accent, bands, handle for the right account; nothing
below 24 px; safe zones respected (Reel/Story rulers in `../templates/renders/diagnostics/`).
☐ **Check-out.** The subject was checked out by the queue rule, inside its deadline, logged with
`performance_data_referenced = NO`; `python3 tools/validate_backlog.py` is clean.
☐ **Anti-duplication.** Not the same file, subject, thesis, source image or hook as anything on the other
account within 14 days or on this account within the within-account windows; consecutive same-format pieces
use disjoint subject sets.
☐ **Caption** per `../policy/CAPTION_AND_HASHTAG_POLICY.md`: hook ≤ 100 chars · body · source line where
required · 3–5 tags from the policy · no CTA, no link, no mention, no location · alt text on every image.
☐ **No engagement bait** on artwork or caption; no giveaway, contest, sponsor, retailer or affiliate language.
☐ **Faceless.** No founder, no face, no identifying personal detail anywhere in the frame or caption.
☐ **Publish settings** per `../policy/SCHEDULING_AND_PUBLISH_SETTINGS.md`: 16:00 UTC · Facebook share OFF ·
no Trial · location none · tags none · AI label OFF (ON only for the six) · Reels "share to feed" ON.

## B. Reels

☐ Duration **20–59 s**, target 30–45 s (C2: 36.5 s at house pacing), never over 90 s.
☐ Cuts only; text holds ≥ 2.5 s; hook frame is the cover; cover title inside the 4:5 grid crop.
☐ No voiceover, no AI voice; audio is a Sound Collection track added at upload and logged in
`../assets/audio_ledger.csv` (not on both accounts within 14 days; not reused on one account within 14 days).
☐ Key on-screen claims also in the caption.

## C. Carousels

☐ **5–10 slides**; one orientation (4:5) throughout; slide counter correct; summary slide present.
☐ C2: exactly 7 items, countdown on item slides, ascending on the summary; C3: method-and-sources slide present.

## D. Statics

☐ 1080 × 1350; essential content inside the 1:1 crop; C2: hero + 6 with all 7 images.

## E. Engine-specific

☐ **C1:** four facts present; rubric scored and recorded; verdict is COP / WAIT / PASS; release date is
confirmed, not rumoured; source line names the release note or product page; the ladder's T−24 h met.
☐ **C2:** ranked-item count = the locked value; `ranked_by` stated; chips only where verified; #1 logged as
a secondary subject; pressure-point pair check recorded where required (`A-W5-C2-REE-01/02`).
☐ **C3:** metric, basis, window and "Data as of" on the frame; source class is a CLEARED register row;
"snapshot" on the frame and "not advice" in the caption; n ≥ 5 behind any median.
☐ **C4:** one of the seven house formats; no brand-bashing by name, no replica jokes, no named private person,
no sexual/political/drug reference; imagery self-drawn / owned / licensed.
☐ **AI slot (six only):** the nine prohibited-use items clear; the fixed disclosure line verbatim in the
caption; **no disclosure element on the artwork** (the frame is an ordinary C4 frame); AI label ON; AI
provenance fields complete; reviewed by the other founder; `ai_platform_label_observed` to be filled at T+7.

## F. Stories

☐ One frame; house Story template; the day's rotation class; sticker only on the fixed weekday; no post
links, no reshares, no AI imagery; 17:30 UTC ± 30 min; logged.

## G. Sign-off

| Piece | Producer | QA by | Date | Result |
|---|---|---|---|---|
| | | | | PASS / FAIL (reason) |

Record the sign-off in the tracking row (`status = QA_PASSED`) before scheduling.
