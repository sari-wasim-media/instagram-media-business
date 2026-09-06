# Sourcing Gate — scorecard

Canonical criteria: `../../experiment/active-84-post-plan/GATES.md` §1. **Gate status: NOT PASSED.** This
scorecard records what the Creative System sprint built for each item and exactly what remains, which is
founder execution in every case. Update the status column as items close; the gate passes when all twelve
read PASSED.

| # | Gate item | Status after the sprint | What exists | What remains (founder execution) |
|---|---|---|---|---|
| 1 | Templates built and measured first; **C2 ranked-item count fixed** | **BUILT — AWAITING TEMPLATE LOCK** | Four house systems + Story as specs, 64 specimen frames, a motion reference, the asset-count table (`../templates/README.md`), the count **proposed at 7** with the full comparison (`../templates/C2_RANKED_ITEM_COUNT_DECISION.md`) | Founders review and lock House System v1 and the count (`../FOUNDER_REVIEW_QUEUE.md` items 1–2). Optionally rebuild the masters in Canva/Figma from the specs |
| 2 | Asset-class decision recorded per engine, in priority order | **RECORDED — AWAITING CONFIRMATION** | `../assets/SOURCE_CLASS_DECISION.md` with the research behind it | Confirm the order; sign the residual-risk acceptance (§4) |
| 3 | The bank covers 22 pieces at the measured per-piece counts | **NOT STARTED — PLAN READY** | The requirement is quantified: **42 C2 images**, ≈ 6–12 C4, 0–3 C1, 1–2 AI illustrations; the 15-hour bank build in `../assets/C2_SOURCING_ROUTES.md`; tracking table in `../assets/ASSET_PIPELINE.md` | Inventory the pairs at hand, set up the rig, shoot, run the free-stock pass, build the first silhouettes, record every row |
| 4 | Provenance record for every asset | **INSTRUMENT BUILT — 0 ASSETS RECORDED** | `../assets/provenance_register.csv` (schema), worked example, `tools/validate_provenance.py` (passes on the example) | Populate as assets land; validator clean before any piece is scheduled |
| 5 | C2 sustainability test: two complete pieces end-to-end, timed | **NOT RUN — PROTOCOL READY** | `../assets/C2_SUSTAINABILITY_TEST.md` with pass thresholds (1.5 × the declared budgets: 135 / 172 min); the two test pieces double as the C2 reserve pieces | Run it; record times, route mix and verdict; if it fails, shift the route (O + S) and re-run |
| 6 | C3 data-source ToS check per source; no scraper | **REGISTER BUILT — 0 ROWS CLEARED** ⚠ | `../assets/C3_DATA_SOURCE_TOS_REGISTER.md` with the 2026-09-05 research: **most marketplaces' terms restrict even manual copying**; two default source classes (reports, release notes) identified | Read and archive each source's current terms; fill the conclusion column; decide the facts-vs-terms posture once; plan BELOW RETAIL pieces only against CLEARED rows |
| 7 | C4 imagery source confirmed; never-a-reposted-template rule in the production checklist | **RECORDED** | `SOURCE_CLASS_DECISION.md` §2 (self-drawn → owned → licensed → AI in six slots); the rule in `../operations/PRE_PUBLISH_QA.md` §A and §E; seven originated house formats replace any template | Confirm |
| 8 | No gate item requires reposting, Collabs or relaxing the originality rule | **CONFIRMED BY CONSTRUCTION** | Every route in the stack is owned, licensed, permissioned or self-generated; route X forbids on-post promotion of the grantor | — |
| 9 | AI generation tool(s) named; output licence confirmed to permit commercial use | **CANDIDATE NAMED — NOT VERIFIED** | Adobe Firefly recommended (states commercial safety, attaches Content Credentials), Gemini alternate; findings and the pages that could not be fetched in `../assets/SOURCING_ROUTES_RESEARCH.md` §6 | **The founders read the tool's current terms themselves**, record tool + version + plan + date (`../policy/AI_IMAGERY_POLICY_PACK.md` §5) |
| 10 | One complete AI-treated C4 piece produced end-to-end, timed | **NOT PRODUCED — PROTOCOL READY** | `../policy/AI_IMAGERY_POLICY_PACK.md` §7 (TEST-AI-01, a Reel in the shape of `B-W2-C4-REE-01`) | Produce it; log generation, review and production minutes |
| 11 | That piece verified against the prohibited-use list, carrying the fixed disclosure, label observed | **NOT DONE — CHECKLIST AND WORDING READY** | Nine-item checklist (§4); disclosure wording proposed (§3) | Founders lock the wording; run the checklist on TEST-AI-01; observe the label |
| 12 | No AI asset reconstructs a third-party image; none in C1/C2/C3 | **ENFORCED BY INSTRUMENT — ATTESTATION PENDING** | Validator refuses AI assets outside the six slots or in C1–C3; attestation field mandatory | Sign the attestation on TEST-AI-01 and on each of the six real assets |

## Reading the scorecard

- **Nothing in the gate can pass without founder execution**, and nothing in it is blocked on design any
  more. The binding sequence is: lock templates and count → build the 42-image bank → run the sustainability
  test → fill the ToS register → verify the AI tool and produce the test piece.
- **Two findings the founders should read before starting** (neither reopens a locked decision):
  1. Brand press imagery is **not** a default source for C1 or C2 — the terms read grant personal,
     non-commercial use only (PUMA's media hub is the one editorial clearance found). C1 was designed so
     imagery is optional; C2 relies on owned photography, free-licence stock and the illustration route.
  2. "Manual collection from public marketplace pages" for C3 is **not automatically clean** — StockX- and
     Flight-Club-style terms reach manual copying; Stadium Goods restricts to personal use. The locked rule
     already said "check terms first"; the register is where that check is recorded.
- Estimated founder effort to pass: **≈ 25–30 hours** (bank build ≈ 15 h, sustainability test ≈ 4 h, ToS
  reading ≈ 3 h, AI verification and test piece ≈ 3 h, reviews ≈ 2 h).

## Sign-off

| Item | Passed (date) | Sari | Wasim |
|---|---|---|---|
| 1–8 (imagery arm) | | ☐ | ☐ |
| 9–12 (AI arm) | | ☐ | ☐ |
| **Sourcing Gate PASSED** | | ☐ | ☐ |
