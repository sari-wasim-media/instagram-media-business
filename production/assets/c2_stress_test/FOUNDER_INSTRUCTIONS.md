# Founder instructions — the manual part of the Sourcing Gate, split three ways

Everything in this file is divided into **A. what Claude prepared (done)**, **B. what Sari and Wasim must
actually do**, and **C. what evidence comes back into the repository**. Nothing in B publishes, schedules,
spends, or touches either Instagram account.

---

## A. Prepared by Claude — done, in this repository

| Item | Where |
|---|---|
| The route stack re-ranked for a desk with no owned inventory **and no permission outreach** (both founder decisions, 2026-09-13); credit-is-not-permission rule; route F discipline with the ownership-plausibility check; route X off the active path | `../C2_SOURCING_ROUTES.md`, `../SOURCE_CLASS_DECISION.md` §2 |
| The stress-test protocol v2 with the pre-declared decision rule | `../C2_SUSTAINABILITY_TEST.md` |
| The two briefs — 7 items + 2 alternates each, disjoint, one PUMA and one Amer Sports item | `TEST_PIECES.md` |
| The candidate log and the timing log (headers) with filled examples | `candidates_log.csv`, `timing_log.csv`, `*_EXAMPLE.csv` |
| The results template with the extrapolation and the verdict table | `RESULTS.md` |
| A validator that refuses "cleared because credited", refuses any route X candidate, and prints the burden summary and the rule's reading | `tools/validate_c2_stress_test.py` |
| Firefly: the three governing documents re-checked on 2026-09-13 — the dates the memo recorded on 2026-09-11 are unchanged | `../FIREFLY_TERMS_VERIFICATION.md` §1, §4 |
| A Claude discovery **pre-scan** of the 14 items on the free-licence pool (done 2026-09-13, ≈ 6 min): four leads logged as `CANDIDATE` with `found_by = CLAUDE_PRESCAN` — all from one Wikimedia Commons CC0 contributor, two matching the brief's colorway — and ten items with nothing at model level in the CC pool. It clears nothing; the founders re-verify every lead | `PRESCAN_NOTES.md`, `candidates_log.csv` rows CND-0001–0004 |

## B. What Sari and Wasim must do — in this order

### B1. Firefly terms confirmation (≈ 30 min, one founder) — Sourcing Gate item 9 — ✅ DONE 2026-10-07

**Closed:** Wasim confirmed the memo on 2026-10-07 — free tier only, no paid plan; the record is
`../FIREFLY_TERMS_VERIFICATION.md` §5. Nothing below remains to do for B1; it is kept as the record of the step.

Follow `../FIREFLY_TERMS_VERIFICATION.md` §4 exactly. In short: open the three documents (§1) on the day;
check each "effective" / "last updated" line against §1 (as of 2026-09-13 they read *April 23, 2026* ·
*May 15, 2026* · *October 3, 2025*); confirm §2.1, §2.2, §2.3, §2.5 read as quoted; create the Adobe ID
yourself (this is an acceptance of external terms — Claude cannot do it); do not join the Firefly gallery
or submit anything to Adobe Stock; stay on the free tier (any paid plan is a founder spending decision);
fill the confirmation record in §5.

**Boundaries that do not move:** AI imagery stays in the six C4 slots plus `TEST-AI-01`. Even a fully
confirmed Firefly licence does **not** make AI a route for C2 — that would need the founders to reopen a
Founder Lock, which this test cannot do.

### B2. Before sourcing starts (≈ 20 min, both)

1. Read `TEST_PIECES.md`. Decide who produces which piece (one each) and who QA's. Log initials.
2. Set up the local asset store (`../ASSET_PIPELINE.md`, "The local asset store") with `licences/`,
   `permissions/`, `illustration/`, `exports/TEST-C2-CAR-01/`, `exports/TEST-C2-REE-01/`. Not in Git.
3. Open `candidates_log.csv` and `timing_log.csv` in a spreadsheet; keep a stopwatch. **Every stage gets a
   timing row; every candidate — including the ones you reject in ten seconds — gets a candidate row.**
   Untimed work does not exist for this test.
4. If a Claude pre-scan left `CANDIDATE` rows, treat them as leads: **re-verify every one yourself** (the
   three checks) and log your verification minutes under `RIGHTS_VERIFY`. A pre-scan row never becomes
   CLEARED without a founder's check.

### B3. Sourcing — one sitting per piece (per item; both founders on their own piece)

There is nothing to wait for: no permission request is sent to anyone, so each piece's sourcing can be done
start to finish in one sitting. For each of your 7 items, in this order, time-boxed:

1. **DISCOVERY (≤ 10 min per item on F).** In route F's priority for the initial test: Openverse filtered
   to CC0 / public domain (Commons / Flickr) → Pexels → Unsplash. Search by model, then model + colorway,
   then model family. Log each candidate with the licence line **as displayed on the photo's own page**.
   **CC BY images are not used in this test** — log one you meet as `REJECTED`, reason `LICENCE`.
2. **RIGHTS_VERIFY** for each candidate you want: (a) trademark §6 fit — product is the subject, neutral
   context, **no people, hands or faces**; (b) ownership plausibility — not a brand render / catalogue shot,
   a quick reverse-image search (Google Lens or TinEye) shows no earlier brand or third-party origin, the
   uploader is a photographer not an aggregator, no watermark; (c) licence line in the accept column of
   `../C2_SOURCING_ROUTES.md` route F (never Unsplash+, never BY-SA / NC / ND, and no CC BY in this test).
   Reject on doubt; log the reason.
3. If F yields nothing inside the box, **do not contact anyone.** No DM, no e-mail, no "would you mind if".
   An image that would only be usable with a permission is logged `REJECTED`, reason `UNCLEAR_RIGHTS`, and
   the item goes to route B (if the brand qualifies) or route S — or to a logged swap.
4. PUMA item (`TEST-C2-REE-01` item 6) and Salomon item (`TEST-C2-CAR-01` item 7) — **route B check**: open
   the PUMA Media Hub terms and the Amer Sports newsroom / site terms on the day; confirm the wording recorded
   in `../SOURCING_ROUTES_RESEARCH.md` §1 still stands; decide and write down whether you read PUMA's
   "media channels" to include Instagram; screenshot both pages with the date into `licences/`. If either
   reading no longer holds, route B is closed for that brand — log `BLOCKED`, reason `LICENCE`, and fall
   through. **Any brand other than these two is a re-review trigger — do not read-and-proceed.**
5. **ASSET_PREP** for each cleared photograph: download, crop to the plate, name the file
   `<piece_ref>__AST-nnnn.<ext>`. (Only download what you have cleared.)
6. **PROVENANCE**: the `provenance_register.csv` row (`piece_ref` = the piece, `slot_id` blank, `engine = C2`,
   class per route, evidence path), then `asset_id` and `CLEARED` on the candidate row. Run
   `python3 tools/validate_provenance.py` and `python3 tools/validate_c2_stress_test.py` before you stop.

### B4. Illustration, swaps, the routes that need a founder's word

- An item that F and B could not supply goes to route S — or, if you judge an illustration inadequate for
  that item, swap to an alternate (`SWAPPED_OUT`, reason).
- **ILLUSTRATION** (route S): the house silhouette recoloured to the colorway, no brand device, plate label
  "Illustration"; a `SELF_GENERATED` provenance row. Time it.
- Route P: **do not buy anything.** If an item would clearly have been solved by a $3 stock credit, write
  `WOULD_USE_P` in the candidate row's notes and carry on. The count goes to the founders as a spend question.
- Route O: if a pair on either list is physically in front of you, shoot it per the appendix in
  `../C2_SOURCING_ROUTES.md` and log it `OWNED`. Do not go looking for pairs.

### B5. Producing the two pieces (each founder, own piece)

- **RESEARCH**: order or tier the seven, write the reasons (≤ 60 chars, desk voice), verify each colorway name
  on the brand product page; chips optional. Time it.
- **LAYOUT** (Figma, from the house masters — `../../templates/C2_RANKINGS_AND_TIER_LISTS.md` §2 / §4) or
  **REEL_ASSEMBLY** (CapCut desktop with no library content, or the house renderer + ffmpeg — §3, 36.5 s).
  No audio baked in; no upload, so no Sound Collection track and no audio-ledger row.
- **CAPTION_QA**: caption to the §9 skeleton, alt text on every slide / cover, 3–5 tags per policy; then the
  other founder QA's against `../../operations/PRE_PUBLISH_QA.md` §A–§C and §E (C2), including the
  nominative-use rule. Sign the row in `RESULTS.md` §7.
- **Do not schedule. Do not post. Do not enter either theme in the backlog.**

### B6. Closing the run (≈ 30 min, both)

1. Run both validators; paste the decision-rule block into `RESULTS.md` §5.
2. Fill `RESULTS.md` §1–§4 from the logs and the validator's summary. Write your own §4 answer **before**
   reading the verdict.
3. Tick the verdict row. Then §6 says what happens next — **if it is NOT SUSTAINABLE, stop there and hand it
   back**; nothing gets redesigned to make it pass.

## C. What must come back into the repository

| Evidence | File |
|---|---|
| Every candidate, cleared or not, with the three checks and a reason for every rejection | `candidates_log.csv` |
| Every stage timed, per item where the stage is per item — all of it active founder time | `timing_log.csv` |
| A provenance row for each of the (up to) 14 cleared assets, evidence paths pointing into the local store | `../provenance_register.csv` |
| The Firefly confirmation record | `../FIREFLY_TERMS_VERIFICATION.md` §5; `../SOURCING_ROUTES_RESEARCH.md` §6 Firefly row |
| The PUMA / Amer Sports readings on the day (wording confirmed? "media channels" read to include Instagram?) | `RESULTS.md` §3 and the candidate rows |
| The filled results, ambiguities, producers' answers, verdict, sign-off | `RESULTS.md` |
| Two validator runs, clean | pasted into `RESULTS.md` §5 |

**Not** into the repository: the images, the licence PDFs, the Adobe login — all of that lives in the local
asset store; the repository holds the record.

## What Claude does after the evidence is back

Reads the logs, re-runs the validators, writes the Phase D decision into the canonical documents
(scorecard item 5, the bank plan sized from `m`, the budgets in the template and the rhythm, the promotion-
to-reserve decision) — or, if the verdict is NOT SUSTAINABLE, writes the escalation with the options and
**stops**.
