# Sourcing Gate — scorecard

Canonical criteria: `../../experiment/active-84-post-plan/GATES.md` §1. **Gate status: NOT PASSED.** This
scorecard records what the Creative System sprint built for each item and exactly what remains, which is
founder execution in every case. Update the status column as items close; the gate passes when all twelve
read PASSED.

| # | Gate item | Status after the sprint | What exists | What remains (founder execution) |
|---|---|---|---|---|
| 1 | Templates built and measured first; **C2 ranked-item count fixed** | **PASSED 2026-09-08** | Four house systems + Story as specs, 64 specimen frames, a motion reference, the asset-count table (`../templates/README.md`); House System v1 and the count **fixed at 7** as delegated production decisions (`DECISIONS.md`) | — (the founders may override before Day 1; rebuild the masters in Figma from the specs) |
| 2 | Asset-class decision recorded per engine, in priority order | **PASSED 2026-09-08** | `../assets/SOURCE_CLASS_DECISION.md` — priority order decided under delegated authority, narrowed per the trademark review, and the residual **accepted by the founders on 2026-09-08** (`../TRADEMARK_RISK_REVIEW.md`) | — (the review's §5 rule is mandatory at QA; a §3 re-review trigger reopens the posture, not the gate item) |
| 3 | The bank covers 22 pieces at the measured per-piece counts | **NOT STARTED — PLAN READY** | The requirement is quantified: **42 C2 images**, ≈ 6–12 C4, 0–3 C1, 1–2 AI illustrations; the 15-hour bank build in `../assets/C2_SOURCING_ROUTES.md`; tracking table in `../assets/ASSET_PIPELINE.md` | Inventory the pairs at hand, set up the rig, shoot, run the free-stock pass, build the first silhouettes, record every row |
| 4 | Provenance record for every asset | **INSTRUMENT BUILT — 0 ASSETS RECORDED** | `../assets/provenance_register.csv` (schema), worked example, `tools/validate_provenance.py` (passes on the example) | Populate as assets land; validator clean before any piece is scheduled |
| 5 | C2 sustainability test: two complete pieces end-to-end, timed | **NOT RUN — PROTOCOL READY** | `../assets/C2_SUSTAINABILITY_TEST.md` with pass thresholds (1.5 × the declared budgets: 135 / 172 min); the two test pieces double as the C2 reserve pieces | Run it; record times, route mix and verdict; if it fails, shift the route (O + S) and re-run |
| 6 | C3 data-source ToS check per source; no scraper | **PASSED 2026-09-08** | `../assets/C3_DATA_SOURCE_TOS_REGISTER.md` operationalised under the founders' conservative data-source posture: press releases, published reports and release notes are the sources; every marketplace is excluded because its terms do not clearly permit the use; product pages confirm only | — (a row reopens only if a source publishes explicit permission) |
| 7 | C4 imagery source confirmed; never-a-reposted-template rule in the production checklist | **PASSED 2026-09-08** | `SOURCE_CLASS_DECISION.md` §2 (self-drawn → owned → licensed → AI in six slots) as a delegated production decision; the rule in `../operations/PRE_PUBLISH_QA.md` §A and §E; seven originated house formats replace any template | Photographs of branded sneakers in C4 wait on the same ACCEPT as item 2 |
| 8 | No gate item requires reposting, Collabs or relaxing the originality rule | **CONFIRMED BY CONSTRUCTION** | Every route in the stack is owned, licensed, permissioned or self-generated; route X forbids on-post promotion of the grantor | — |
| 9 | AI generation tool(s) named; output licence confirmed to permit commercial use | **TOOL DECIDED — LICENCE VERIFICATION OPEN (founder)** | **Adobe Firefly** selected as a delegated production decision (states commercial safety, attaches Content Credentials), Gemini alternate; findings in `../assets/SOURCING_ROUTES_RESEARCH.md` §6 | **The founders read the tool's current terms themselves**, create the account, record tool + version + plan + date (`../policy/AI_IMAGERY_POLICY_PACK.md` §5); any paid plan is a founder approval |
| 10 | One complete AI-treated C4 piece produced end-to-end, timed | **NOT PRODUCED — PROTOCOL READY** | `../policy/AI_IMAGERY_POLICY_PACK.md` §7 (TEST-AI-01, a Reel in the shape of `B-W2-C4-REE-01`) | Produce it; log generation, review and production minutes |
| 11 | That piece verified against the prohibited-use list, carrying the fixed disclosure, label observed | **NOT DONE — CHECKLIST AND WORDING READY** | Nine-item checklist (§4); disclosure wording proposed (§3) | Founders lock the wording; run the checklist on TEST-AI-01; observe the label |
| 12 | No AI asset reconstructs a third-party image; none in C1/C2/C3 | **ENFORCED BY INSTRUMENT — ATTESTATION PENDING** | Validator refuses AI assets outside the six slots or in C1–C3; attestation field mandatory | Sign the attestation on TEST-AI-01 and on each of the six real assets |

## Reading the scorecard

- **Passed on 2026-09-08:** items 1, 2, 6, 7 and 8 (five of twelve) — item 2 closed by the founders'
  acceptance of the trademark posture (`../TRADEMARK_RISK_REVIEW.md`). **Founder execution:** items 3, 4, 5 (the bank,
  the provenance rows, the sustainability test), 9 (licence verification), 10, 11, 12 (the AI test piece).
- The binding sequence is now: **build the 42-image bank** on routes O and F under the accepted posture →
  run the sustainability test → founders verify Firefly's terms → produce and check the AI test piece →
  sign off.
- Estimated founder effort to pass: **≈ 22–26 hours** (bank build ≈ 15 h, sustainability test ≈ 4 h, AI
  verification and test piece ≈ 3 h; the ToS reading is no longer needed).

## Sign-off

| Item | Passed (date) | Sari | Wasim |
|---|---|---|---|
| 1–8 (imagery arm) | | ☐ | ☐ |
| 9–12 (AI arm) | | ☐ | ☐ |
| **Sourcing Gate PASSED** | | ☐ | ☐ |
