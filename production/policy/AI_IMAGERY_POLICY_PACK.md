# AI-imagery policy pack

**Week-1 Gate item 10:** *definition, prohibited-use list, fixed disclosure wording, provenance fields, and
the six locked slot IDs recorded in the tracking sheet.* The sub-test itself is founder-locked
(`../../experiment/active-84-post-plan/AI_IMAGERY_SUBTEST.md`); this pack operationalises it. **The disclosure
wording and placement (§3) and the tool selection (§5) are decided under the founders' delegated production
authority (2026-09-08), which completes the pack.** What stays with the founders: verifying the tool's
current terms, creating the account, and approving any paid plan (Sourcing Gate item 9; no spending
authority). **Item 9 closed 2026-10-07:** Wasim confirmed Firefly's terms, free tier only, no paid plan
(`../assets/FIREFLY_TERMS_VERIFICATION.md` §5).

## 1. Definition (locked, restated for the production desk)

**AI-generated imagery** is any raster or vector element in the published creative whose pixels were produced
or materially altered by a generative model: text-to-image, image-to-image, generative fill or expand,
generative object addition or removal, generative upscaling that invents detail.

**Not AI imagery:** chart rendering, non-generative photo adjustment (crop, exposure, colour balance,
sharpening), template layout, typography. Captions, scripts and research are always the founders' own
writing; this pack is about imagery only.

## 2. The six slots — and nowhere else

| Slot | Account | Week | Format |
|---|---|---|---|
| `B-W2-C4-REE-01` | B | 2 | Reel |
| `A-W2-C4-CAR-01` | A | 2 | Carousel |
| `B-W2-C4-STA-01` | B | 2 | Static |
| `A-W4-C4-REE-01` | A | 4 | Reel |
| `B-W5-C4-CAR-01` | B | 5 | Carousel |
| `A-W6-C4-STA-01` | A | 6 | Static |

Recorded in `matrix_84.csv` (`ai_overlay = AI`), in the tracking sheet's `ai_overlay` column, in
`../templates/template_constants.json`, and enforced by `tools/validate_matrix.py` and
`tools/validate_provenance.py`. **Zero AI imagery in Week 1, in C1/C2/C3, in any other C4 slot, in any Story,
and in any reserve piece.**

## 3. The fixed disclosure line — decided (delegated production decision, 2026-09-08)

> **Imagery in this post is AI-generated and illustrative. It does not depict a real product.**

- Appears **verbatim** as the last caption line before the hashtags in all six posts. Never abbreviated,
  never paraphrased, never moved to a comment. The line is part of the treatment being measured, so it must be
  identical six times.
- In addition: the in-app AI label is switched **on** when posting each of the six ("Add AI label" in the
  composer, as documented for Meta surfaces; the Instagram composer's exact label is to be confirmed at the
  AI test), and any label Meta applies automatically is left in place. Never strip or alter metadata to
  avoid a label.
- **Nothing on the artwork.** The locked sub-test requires exactly these two disclosures — the fixed caption
  line and the preserved platform label. A visible disclosure element on the frame would add a second visual
  difference between AI and non-AI C4 posts on top of the imagery itself, so it is not part of the treatment.
  The AI-slot specimen (`../templates/renders/c4/c4_ai_slot_static_expectation_reality.png`) is therefore an
  ordinary C4 frame.

| Decision record | |
|---|---|
| Wording | the line above, verbatim, six times |
| Placement | caption line + platform label only (per the locked sub-test; no on-artwork element) |
| Decided | 2026-09-08 — delegated production decision (Claude); inside the locked sub-test, which requires an identical fixed caption line and a preserved platform label. Founders may override the wording before Day 1 |

## 4. Prohibited — even inside the six slots (locked, as a checklist)

☐ No depiction readable as a photograph of a real, specific, identifiable product — no generated shoe that
purports to be an actual model or colorway.
☐ No generated image supporting a factual claim — price, date, colorway, materials, availability, sizing,
market data.
☐ No brand marks or trademarks (Swoosh, Jumpman, three stripes, wordmarks) or brand-identifying design elements.
☐ No likeness of a real person — athletes, designers, celebrities, anyone.
☐ No generative video, no generative interpolation, no AI voice. Still images only, inside the house motion template.
☐ Nothing generated in C1, C2, C3 or any slot outside the six.
☐ No mimicry of an identifiable creator's style; no reproduction of a recognisable existing work.
☐ No use of generation to reconstruct or "clean up" a third-party image.
☐ No attempt to strip, obscure or evade a platform AI label.

## 5. Generation guardrails — how the founders stay inside the list

- **Prompts** name no brand, no model, no athlete, no artist. They ask for *illustration*, *flat* or
  *abstract* styles, and include the clauses "unbranded", "no logos", "no text", "no people". The idea is a
  scene or an object of the meme (a mountain of shoeboxes, a shoe-shaped cloud, a receipt the length of a
  street), never a product.
- **Review** by the *other* founder before use: inspect for accidental swoosh-like curves, stripe patterns,
  wordmark-like text, recognisable silhouettes of a specific model, and faces. Anything doubtful is
  regenerated; nothing is "fixed" by generative editing of a real photograph.
- **Tool — decided: Adobe Firefly** (web), on its free tier first (delegated production decision under the
  founders' tool-selection autonomy, 2026-09-08). Adobe states its models are "commercially safe" and
  attaches Content Credentials (C2PA), which is what lets Instagram's "AI info" label appear automatically —
  the disclosed version of the treatment the sub-test wants measured. Alternate if Firefly's free allowance
  or output proves unsuitable at the test piece: Google Gemini (SynthID; C2PA on its pro image model).
  Rejected: Midjourney (no provenance metadata, paid only), Ideogram and Leonardo free tiers (images public
  or rights retained). **Selection is not purchase and not verification:** `GATES.md` §1.4 item 9 requires
  the founders themselves to read the tool's current output-licence terms, create the account, and record
  tool + version + plan + date in `../assets/SOURCING_ROUTES_RESEARCH.md` §6 and in every asset row; a paid
  plan needs founder approval (`../operations/TOOLING.md`). **Confirmed 2026-10-07 (Wasim):** free tier only;
  Adobe-native Firefly image model — the exact in-app version goes in `ai_tool_version` from TEST-AI-01 on;
  partner models offered inside the Firefly app are not part of the route; no Gallery / Community, no Adobe
  Stock submission; Content Credentials never removed or altered.
- **Never** feed a third-party photograph, a brand image or another account's post into a generator.

## 6. Provenance fields for every AI asset (locked list, as register columns)

`ai_tool_version` · `ai_prompt` (full text of every prompt) · `ai_seed_params` (seed and parameters where
available) · `ai_attestation_no_product_brand_person` (Y) · `ai_reviewer` (the other founder's initials) ·
`ai_disclosure_present` (Y) · `ai_platform_label_observed` (Y/N, filled at T+7) — alongside the standard
provenance columns in `../assets/provenance_register.csv`. `tools/validate_provenance.py` refuses an
AI asset with any of the first six blank.

## 7. The AI-route test piece — Sourcing Gate items 10–12

Produce **one complete AI-treated C4 piece end-to-end**, as a non-matrix test piece (`TEST-AI-01`, never
published, never used as a reserve), in one of the seven house formats, in the format of the earliest AI slot
(a Reel, so `B-W2-C4-REE-01`'s shape is proven). Record:

| Measure | Value |
|---|---|
| Tool, version, plan | |
| Generations attempted / kept | |
| Generation time | min |
| Compliance review time (§4 checklist, by the other founder) | min |
| Production time (layout, beats, caption with the fixed line) | min |
| Prohibited-use checklist: all nine clear | ☐ |
| Content Credentials present in the file (check with a C2PA verifier) | ☐ |
| Attestation: no third-party image was used or reconstructed | ☐ |
| Producer / reviewer / date | |

Items 11–12 pass when the checklist is clear and the attestation is signed; item 10 records the times, which
set the "+30 min" AI budget in `../templates/C4_ORIGINAL_MEME_AND_COMMENTARY.md` §7.

## 8. Handling during the experiment (locked, restated)

An AI slot that Misses is recovered at the end of the schedule **retaining its AI treatment**; no reserve
piece is AI-treated; if either account's Account Status changes after an AI post, the standard hard stop
applies and the AI treatment is logged as a candidate cause; the platform label state is observed and
recorded at T+7 and never evaded. Analysis reads C4 three ways (full, AI-excluded, AI-only) and applies the
flip rule — that is the analysts' job, not the production desk's, but the desk makes it possible by keeping
the six rows clean.
