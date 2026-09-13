# C2 sourcing routes — how 147 rights-clean product images actually get made

C2 needs one rights-clean image per ranked item, per piece, in every format, never reused: **7 × 21 = 147**,
of which **42** must exist before the Sourcing Gate can pass (four Week-1 pieces + two C2 reserve pieces).
This document turns the class priority in `SOURCE_CLASS_DECISION.md` into routes with steps, costs and
throughput, so the founders can run the sustainability test against a real procedure.

**Revised 2026-09-13 (ACTIVE — delegated production decision).** The founders stated an operational fact:
**Sari and Wasim do not have meaningful access to a sneaker inventory and cannot self-shoot dozens of
products.** The earlier primary — "O + F", built on a rig and a 20-pair shoot — assumed they could. That
assumption is withdrawn. Owned photography (route O) remains an acceptable class (`GATES.md` §1.2 is locked
and lists it) but is now **opportunistic only: used when a pair happens to be at hand, never planned
against, never the base of the bank.** The routes are the same six routes the trademark review narrowed on
2026-09-08 — none added, none removed — so no §3 re-review trigger fires; only their order and the
assumed volume per route changed. The earlier order is kept at the end of this file for the record.

**Second founder decision, 2026-09-13 (ACTIVE — founder decision): no permission outreach.** Sari and Wasim
will **not** send permission requests to creators, photographers, Instagram accounts or any other third
party in order to source content — no DMs, no e-mails, no waiting for replies, no request queue, no reliance
on one-off approvals. **Route X (permissioned creator imagery) is removed from the active sourcing path.**
It is not replaced by anything weaker: an image without a clear licence or an archived brand clearance is
rejected, whatever credit could be given. The `PERMISSIONED` class stays in the register schema only because
`GATES.md` §1.2 (locked) lists it as an acceptable class; nothing in this workflow solicits one.

## The route stack — priority order (revised 2026-09-13)

| Priority | Route | Class | Per-image cost | Per-image time (planning figure — replaced by the stress test) | Throughput ceiling | Covers |
|---|---|---|---|---|---|---|
| **1** | **F · Free-licence stock** | `LICENSED_FREE` | $0 | 6–12 min (search, ownership-plausibility check, licence archive, download, plate) | CC0 / public domain on Wikimedia Commons and Flickr, then Pexels and Unsplash (CC BY not used in the initial test); **specific colorways patchy** | Icons, general releases, common colorways |
| **2** | **B · Brand press, verified per brand** | `PRESS_VERIFIED` | $0 | 10 min first time per brand (read and archive the terms), 3 min per asset after | Only brands whose archived terms grant editorial use in a way that covers a social post — **PUMA** on the terms read 2026-09-05; every other brand read grants personal / non-commercial use only | New releases from those brands |
| **3** | **P · Paid stock** | `LICENSED_PAID` | ~$3 per image on a 10-credit plan — **founder approval per purchase; no approval is on file** | 5 min | Budget-limited: a gap-filler, never a route | Specific models missing from F |
| **4** | **S · Self-generated illustration** | `SELF_GENERATED` | $0 | 3–5 min per colorway once the silhouette library exists (≈ 5 h to build 15 silhouettes) | Unlimited | Any colorway — as a recognisable colour-blocked silhouette. The always-on fallback; its **share** is a finding the stress test reports |
| **5** | **O · Owned photography** | `OWNED` | ~$0 | 4–6 min per photograph with a phone and a plain backdrop | **Whatever pair is physically at hand on the day — not a planning input** | Occasional |

**Primary for the experiment (revised 2026-09-13, second revision the same day): F, with B per brand where
terms are archived, S as the always-on fallback, P only inside a founder-approved budget, O whenever a pair
is actually at hand. No route X.**
Routes F, B, P and O all produce photographs of branded sneakers and therefore run **under the accepted
trademark posture and its §5 operating rule** (`../TRADEMARK_RISK_REVIEW.md`, ACCEPTED 2026-09-08); route S
is unaffected by it. **The two-piece stress test (`C2_SUSTAINABILITY_TEST.md`) decides whether this primary
holds** — it is not assumed to.

**Fall-through, per item.** Take the first route that can supply the item; if it cannot inside the item's
time box, move to the next. With no paid budget on file the practical order is **F → B → S**; the stress
test records how many items *would have* used P, so the founders can decide whether a small paid budget is
worth approving. An item that reaches S is a valid item; a piece that reaches S on more than two of seven
items is a valid piece **and** a finding to report (see the test's decision rule).

## What is never a source — the rule that credit is not permission

Public visibility is not a licence. **None of the following clears an image**, and no amount of crediting
turns it into a cleared image:

- it is on Instagram, Pinterest, TikTok, a forum, a blog or a retailer's product page;
- it carries a watermark (its own or someone else's);
- other pages repost it;
- the creator "can be credited", "was credited", or "probably wouldn't mind";
- it was "found online".

An image whose rights are not established is logged as **UNCLEAR / BLOCKED** in the candidate log and is
never given an asset ID. The only ways an image becomes an asset are the five active routes above, each with
its evidence archived (`SOURCE_CLASS_DECISION.md` §1). Trademark posture and copyright permission are separate
questions: the accepted trademark posture does not grant copyright permission to any photograph.

---

## Route F — free-licence stock, the discipline

Free licences clear the *photographer's copyright* for commercial use; none clears the trademark in frame,
which the accepted posture handles. The discipline that makes route F defensible:

**Where to look, and which licence line to require**

| Source | Accept only | Never | Notes |
|---|---|---|---|
| Unsplash | Images under the **Unsplash License** | **Unsplash+** images (a separate paid licence) | Read the licence line on the photo page, not the search result |
| Pexels | Images under the **Pexels License** | — | Same |
| Wikimedia Commons | **CC0**, **public domain** | **CC BY-SA** (share-alike attaches to the whole slide), "fair use" uploads, anything with a deletion or copyright-review tag; **CC BY — not used in the initial test** (see below) | Read the licence box on the file page |
| Flickr | **CC0**, Public Domain Mark | BY-SA, BY-NC, BY-ND, "All rights reserved"; **CC BY — not used in the initial test** (see below) | Check the "Some rights reserved" line on the photo page; the search filter is not proof |
| Openverse (openverse.org) | — | — | A **discovery** aid across the CC sources above; filter to CC0 / PDM; the licence is verified on the source page, never on Openverse |

**Priority inside route F for the initial stress test (founder correction, 2026-09-13):** CC0 / public-
domain-equivalent imagery where applicable → Pexels assets whose current licence permits the use → Unsplash
assets whose current licence permits the use → any other clearly licensed-free asset **only** where its usage
requirements are unambiguous and can be satisfied exactly. **CC BY is NOT USED IN THE INITIAL TEST.** It
stays documented as a possible future route (it is inside the `LICENSED_FREE` class as recorded in
`SOURCE_CLASS_DECISION.md` §1) and may be reopened only once its attribution requirements have been checked
and the intended Instagram implementation shown to satisfy them cleanly. A CC BY image found during the test
is logged `REJECTED`, reason `LICENCE`, note "CC BY — not used in the initial test". The Commons / Flickr /
Openverse surface remains a widening of *where the founders search* for the class, not a new class or route.
Pixabay stays excluded for any branded product.

**Per candidate — in this order**

1. **Trademark §6 narrowing** (`../TRADEMARK_RISK_REVIEW.md`): the product is the subject in a neutral
   context; no brand advertising imagery, no store or event scene with brand signage as the subject, nothing
   that could depict counterfeit product, **no people, hands or faces**. Most lifestyle and on-feet
   photographs fail here; that is expected.
2. **Ownership plausibility** — the check that catches "licence laundering" (an uploader publishing a
   brand's render or someone else's photograph under a free licence they cannot grant). Reject if: the image
   looks like a brand render, catalogue or press shot (perfect studio cut-out, 3D render, the brand's own
   angle and lighting); a quick reverse-image search shows it earlier elsewhere under a different name or
   as a brand asset; the uploader's profile is an aggregation or repost account rather than a photographer's;
   the image carries any watermark or third-party overlay. Reject **on doubt** — a licence that the
   uploader could not grant is worthless, and this is exactly the residual the trademark review flagged as
   "a mis-read or mis-recorded licence".
3. **Licence line** read on the photo's own page and matching the accept column above.
4. **Archive**: the photo page (screenshot with the licence line, photographer name and date visible) and the
   licence text (PDF or screenshot, dated) into the local asset store; record both in the provenance row.
5. **Attribution.** Unsplash, Pexels, CC0, public domain: not required (a plain-text credit is still good
   provenance culture when space allows). No asset in the initial test carries a mandatory attribution.
   *For the record, not for this test:* CC BY would require attribution, and the only form the caption policy
   could carry is a plain-text line (`Photo: <author>, CC BY <version>, via <Commons|Flickr>, cropped` — no
   URL, no @-mention) that cannot include the licence link the licence prefers. That unresolved ambiguity is
   why CC BY is excluded from the initial test; reopening it needs that check done first.
6. **Time-box** each item at 10 minutes of search before falling through to route B (if the brand qualifies)
   or route S. Log the minutes.

## Route X — permissioned creator imagery: NOT ACTIVE (founder decision, 2026-09-13)

The founders will not solicit permissions from creators, photographers, Instagram accounts or other third
parties, and will not run a request queue or wait on replies. **No candidate is logged as pending a
permission; no permission-request message exists in this repository** (the earlier template was withdrawn
the same day it was written, before any request was sent). An image that would only be usable with a
permission the founders are not going to ask for is logged `REJECTED`, reason `UNCLEAR_RIGHTS` (or
`LICENCE`), and the item falls through to route B or S. Credit is not permission, and this decision does not
make it one. The `PERMISSIONED` class remains defined in `SOURCE_CLASS_DECISION.md` §1 only because
`GATES.md` §1.2 (locked) lists it; reopening the route would be a founder decision.

## Route B — brand press assets, per brand only

Read the newsroom terms, archive them, and only proceed if the text grants editorial or media use in a way
that covers a social post. Log the clause in the provenance row. On the terms read on 2026-09-05 this is
**PUMA** (Media Hub: "cleared for editorial and news use across media channels" — **the founders confirm on
the day that the wording still stands and that "media channels" is read to include Instagram**, then archive
the page) and **Amer Sports** press material with a source credit. Everything else read is personal /
non-commercial only (`SOURCING_ROUTES_RESEARCH.md` §1). **Any brand beyond the archived PUMA clearance is a
§3 re-review trigger of the trademark review — escalate before use, do not read-and-proceed.** Re-read PUMA's
page before each new batch.

## Route P — paid stock (gap-filler, founder approval per purchase)

Adobe Stock Standard (never an "editorial use only" asset), single credits. **No spending is authorised;
route P is taken only after a founder approves a specific purchase or a small budget in
`../operations/TOOLING.md` (spending register).** The stress test logs every item that *would* have used P
so the decision can be taken on a number, not a guess.

## Route S — the house silhouette library

A colour-blocked illustration of the silhouette (upper, quarter panel, sole, laces, collar) in the house
plate. Recognisable as "a Court 1 High in Deep Royal" without claiming to be a photograph, and carrying no
brand mark. Build a library of the ~15 silhouettes the rankings will keep returning to, each as a vector with
named colour regions; recolouring per colorway then takes minutes. The specimen shoe in every rendered frame
(`../templates/src/render_frames.py`, `shoe()`) is the starting point of that library.

Rules: no Swoosh, Jumpman, stripes, wordmarks or any brand-identifying device; the silhouette is generic to
the model family, the colour blocking carries the colorway; the plate label reads "Illustration". A piece may
mix photographs and illustrations. **A ranking that is mostly illustration is the fallback that keeps a slot
alive, not the house look** — which is why the stress test reports the S share per piece and treats a high
share as a finding for the founders rather than quietly normalising it.

## Route O — owned photography, opportunistic

When a pair is actually at hand — a founder's own, a friend's for an afternoon — shoot it: it is the cleanest
asset there is (no third-party copyright at all; the same trademark residual as every photograph). Shoot with
the plate discipline in the appendix so it matches the other routes. **Do not inventory, do not build a rig
budget, do not write a theme toward pairs that are not in the room.** Owned images are never reused across
pieces (anti-duplication rule 4): a pair that ranks again later is a second photograph with a second ID.

---

## Building the 42-image gate bank — after the stress test, sized by it

The bank is built **only after `C2_SUSTAINABILITY_TEST.md` returns SUSTAINABLE or SUSTAINABLE WITH
CONDITIONS**, and its plan is sized by the measured minutes per cleared image, not by the planning figures
above. Until then the plan is a shape, not a schedule:

| Step | Output | Time |
|---|---|---|
| 1 | Idea-bank themes checked against what the test showed is findable (`../backlog/IDEA_BANK.md`) | 1 h |
| 2 | Route F pass for the items the next four themes need, ownership-plausibility checks done, licences archived | (measured min/image) × N |
| 3 | Route B: PUMA page re-read and archived if a PUMA item is in scope | 10 min |
| 4 | Silhouette library: the 8 models the themes use most | 3 h |
| 5 | Provenance rows for all of the above; `python3 tools/validate_provenance.py` clean | 1 h |

The 42 comprise 28 for the four Week-1 C2 pieces and 14 for the two C2 reserve pieces; the stress test's 14
assets count toward the 42 **only if** the prototypes are promoted to reserve (`C2_SUSTAINABILITY_TEST.md`
§6). The earlier "≈ 15 hours" figure — most of it a rig and a 20-pair shoot — is withdrawn; the replacement
figure is computed in `c2_stress_test/RESULTS.md` from measured times.

## What would make the route fail, and what changes

The pre-declared decision rule is in `C2_SUSTAINABILITY_TEST.md` §5. In short: if the two pieces cannot be
produced rights-clean inside 1.5 × their declared budgets, or if fewer than 5 of 7 items per piece can be
sourced from the photographic routes (F / B / P / O) so that C2 becomes an illustration-led engine, or if
the extrapolation to 21 pieces does not fit the weekly rhythm, **the finding is escalated to the founders —
it is not solved by relaxing a rule, by reducing the item count, by admitting AI to C2, or by treating a
credited image as cleared.** The idea bank may change (rankings are written toward what the test showed is
findable); the count and the matrix may not.

---

## Appendix — the plate discipline for any photograph, and the shoot checklist if a pair is at hand

*Kept from the 2026-09-06 version. It is no longer a bank-build step; it is what to do on the day a pair
happens to be in the room, and the framing standard every route's plate is cropped to.*

Faceless product photography needs no face: the founders never appear. A plain seamless backdrop (a roll of
white or light-grey paper, or a large white foam board), a window, a phone, a lens cloth. Shoot every pair the
same way so the plates match across a piece:

1. Side profile, toe pointing left, laced, insole flat, on the backdrop, camera at shoe height, 1–1.5 m away.
2. Fill the frame 80 %, leave paper around it; expose for the white (slightly over), no flash.
3. Shoot the angles once: profile, three-quarter, top-down. Profile is the C2 default.
4. Name the file with the provenance ID at import; log the record (`provenance_register.csv`) the same day.

- [ ] **Trademark §5 rule at the lens** (`../TRADEMARK_RISK_REVIEW.md`): the product is the subject in a
      neutral context — no brand advertising material, packaging, store or event signage as the subject; no
      person, hand or face; no counterfeit product, ever.
- [ ] Import the same day into `assets/shoots/YYYY-MM-DD/`. Assign the next `AST-nnnn` per photograph and
      rename the raw to `BANK__AST-nnnn.<ext>`. One photograph = one asset ID = one future piece.
- [ ] Append one row per photograph to `provenance_register.csv`: `class=OWNED`, `engine=C2`, `slot_id` blank,
      `source_name=Founder photograph`, `source_url_or_ref=local://shoots/YYYY-MM-DD/<raw>`,
      `licence_or_permission=Owned by the founders`, `date_obtained`, `permitted_use=Any use by the accounts`,
      `file_name=BANK__AST-nnnn.<ext>`, `obtained_by=<initials>`.
- [ ] `python3 tools/validate_provenance.py` clean before leaving the session.

Every other route crops its plate to the same standard: side profile where the source allows, toe left,
product at 80–90 % of plate width, on the house plate (`../templates/C2_RANKINGS_AND_TIER_LISTS.md` §6).

## Record — the order this revision replaced

*2026-09-06 → 2026-09-13, for the record only.* Primary "O + F, S as fallback, X/B gap-fillers, P with
approval"; a 15-hour bank build beginning with a pair inventory, a rig and a 20-pair × 3-angle shoot; failure
path "shift to O + S". Withdrawn on the founders' statement of 2026-09-13 that no such inventory exists. The
classes, the evidence rules and the trademark narrowing are unchanged.

*Later on 2026-09-13.* The first revision of that day made "F + X" the primary and ran route X on a
seven-day permission window with a passive wait. Withdrawn the same day by the founders' decision not to
solicit permissions; route X is no longer on the active path and the wait stage is gone from the test.
