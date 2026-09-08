# C2 sourcing routes — how 147 rights-clean product images actually get made

C2 needs one rights-clean image per ranked item, per piece, in every format, never reused: **7 × 21 = 147**,
of which **42** must exist before the Sourcing Gate can pass (four Week-1 pieces + two C2 reserve pieces).
This document turns the class priority in `SOURCE_CLASS_DECISION.md` into routes with steps, costs and
throughput, so the founders can run the sustainability test against a real procedure.

## The route stack

| Route | Class | Per-image cost | Per-image time | Throughput ceiling | Covers |
|---|---|---|---|---|---|
| **O · Owned photography** | `OWNED` | ~$0 after a one-off setup (backdrop, tape, phone) | 4–6 min once the rig exists | The pairs the founders and their circle own or can borrow — build the inventory list first | Any colorway physically at hand |
| **F · Free-licence stock** | `LICENSED_FREE` | $0 | 5–8 min (search, licence archive, download, plate) | Thousands of sneaker photos on Unsplash/Pexels; specific colorways patchy | Icons, general releases, lifestyle shots |
| **P · Paid stock** | `LICENSED_PAID` | ~$3 per image on a 10-credit plan — **founder approval per purchase** | 5 min | Budget-limited: use for ≤ 10 gaps | Specific models missing from F |
| **X · Permissioned** | `PERMISSIONED` | $0; a message and a wait | 15 min + the reply | Slow; ask early, in batches | Niche colorways owned by collectors |
| **S · Self-generated illustration** | `SELF_GENERATED` | $0 | 3–5 min per colorway once the silhouette library exists (≈ 5 h to build 15 silhouettes) | Unlimited | Any colorway — as a recognisable colour-blocked silhouette |
| **B · Brand press, verified** | `PRESS_VERIFIED` | $0 | 10 min first time per brand (read and archive terms), 3 min per asset after | Only brands with permissive, archived terms (PUMA so far) | New releases from those brands |

**Primary for the experiment (ACTIVE — delegated production decision, 2026-09-08): O + F, with S as the
always-on fallback and X/B as gap-fillers; P only with founder approval per purchase.** Routes O, F, X, P
and B all produce photographs of branded sneakers and therefore run **under the accepted trademark posture
and its §5 operating rule** (`../TRADEMARK_RISK_REVIEW.md`, ACCEPTED 2026-09-08); route S is unaffected by it. The sustainability test decides whether the primary holds.

## Route O — owned photography, the rig

Faceless product photography needs no face: the founders never appear. One-off setup for well under the $300
budget: a plain seamless backdrop (a roll of white or light-grey paper, or a large white foam board), a
window or two cheap LED panels, a phone on a small tripod, a lens cloth. Shoot every pair the same way so the
plates match across a piece:

1. Side profile, toe pointing left, laced, insole flat, on the backdrop, camera at shoe height, 1–1.5 m away.
2. Fill the frame 80 %, leave paper around it; expose for the white (slightly over), no flash.
3. Shoot both pairs' angles once: profile, three-quarter, top-down. Profile is the C2 default.
4. Name the file with the provenance ID at import; log the record (`provenance_register.csv`) the same day.

Owned images may be re-cropped but not reused across pieces: shoot enough angles that a later piece can use a
different frame if the same pair ever ranks again (allowed within the anti-duplication rules only after
10 days on one account and 14 days across accounts, and only as a different photograph).

**Inventory step (do first):** list every pair the founders own or can borrow, by model and colorway. That
list is the real ceiling of route O and the input to the idea bank — rankings should be written toward pairs
that can be photographed.

## Route F — free-licence stock, the discipline

Unsplash and Pexels licences permit commercial use and exclude the trademark in frame; Unsplash's own
guidance says positive, non-endorsing, editorial use is likely fine. The discipline that makes route F
defensible:

1. Search by model and colorway; take only frames in which **the product is the subject in a neutral
   context**: no brand advertising imagery, no store or event scenes with brand signage as the subject,
   nothing that could depict counterfeit product, no people at all (the account is faceless and model releases
   cannot be relied on). The trademark review narrows this route to exactly these frames
   (`../TRADEMARK_RISK_REVIEW.md` §6).
2. **Archive the licence**: save the licence page as PDF/screenshot with the date, and the photo's own page
   URL, into the local asset store; record both in the provenance row.
3. Record the photographer's name and, although not required by either licence, credit in the caption when
   space allows — it is cheap goodwill and part of the desk's provenance culture.
4. Never Pixabay for a branded shoe (its licence bars it); never an image that is itself a brand advert or
   a screenshot; never an image with a watermark.

## Route S — the house silhouette library

A colour-blocked illustration of the silhouette (upper, quarter panel, sole, laces, collar) in the house
plate. Recognisable as "a Court 1 High in Deep Royal" without claiming to be a photograph, and carrying no
brand mark. Build a library of the ~15 silhouettes the rankings will keep returning to, each as a vector with
named colour regions; recolouring per colorway then takes minutes. The specimen shoe in every rendered frame
(`../templates/src/render_frames.py`, `shoe()`) is the starting point of that library.

Rules: no Swoosh, Jumpman, stripes, wordmarks or any brand-identifying device; the silhouette is generic to
the model family, the colour blocking carries the colorway; the plate label reads "Illustration". A piece may
mix photographs and illustrations, but a ranking that is *all* illustration should be the exception — it is
the fallback that keeps a slot alive, not the house look.

## Route X — permissioned images

Message collectors and sneaker photographers in the founders' network: what image, where it will be used
(a ranking post on the named account), that it will be credited, that it is not sponsorship. Keep the reply.
Scope the permission to "one Instagram post, either account, within 60 days". During the experiment no
grantor is promoted, tagged as a Collab or offered anything — that would breach the locked no-Collab,
no-advertiser-outreach rule.

## Route B — brand press assets, per brand only

Read the newsroom terms, archive them, and only proceed if the text grants editorial or media use in a way
that covers a social post. Log the clause in the provenance row. On the terms read on 2026-09-05 this is
**PUMA** (Media Hub: "cleared for editorial and news use across media channels" — founders to confirm that
"media channels" is read to include Instagram) and **Amer Sports** press material with a source credit.
Everything else read is personal / non-commercial only. Re-read before each new brand.

## Building the 42-image gate bank

| Step | Output | Time |
|---|---|---|
| 1 | Inventory of pairs at hand (route O ceiling) | 1 h |
| 2 | Rig set up; first 20 pairs shot in one session, 3 angles each | 3 h |
| 3 | Idea bank themes written toward the inventory (`../backlog/IDEA_BANK.md`) | 1 h |
| 4 | Route F pass for the 20 most likely non-owned items, licences archived | 2.5 h |
| 5 | Silhouette library: 8 silhouettes first (the models the idea bank uses most) | 3 h |
| 6 | Provenance rows for all of the above; `python3 tools/validate_provenance.py` clean | 1 h |
| 7 | The sustainability test: two C2 pieces end-to-end from the bank (`C2_SUSTAINABILITY_TEST.md`) | 3–4 h |

Roughly **15 hours** to a passable C2 arm of the Sourcing Gate, most of it one-off.

## What would make the route fail, and what changes

If the sustainability test shows that fewer than 5 of 7 items per piece can be sourced from O + F within the
time budget, shift the primary to **O + S** (photograph what you own, illustrate the rest) and re-run the
test. If owned inventory is too thin for the idea bank, the idea bank changes — rankings are written toward
what can be shown — not the count, not the matrix.
