# Sourcing Gate — scorecard

Canonical criteria: `../../experiment/active-84-post-plan/GATES.md` §1. **Gate status: NOT PASSED.** This
scorecard records what the Creative System sprint built for each item and exactly what remains, which is
founder execution in every case. Update the status column as items close; the gate passes when all twelve
read PASSED.

| # | Gate item | Status after the sprint | What exists | What remains (founder execution) |
|---|---|---|---|---|
| 1 | Templates built and measured first; **C2 ranked-item count fixed** | **PASSED 2026-09-08** | Four house systems + Story as specs, 64 specimen frames, a motion reference, the asset-count table (`../templates/README.md`); House System v1 and the count **fixed at 7** as delegated production decisions (`DECISIONS.md`) | — (the founders may override before Day 1; rebuild the masters in Figma from the specs) |
| 2 | Asset-class decision recorded per engine, in priority order | **PASSED 2026-09-08** | `../assets/SOURCE_CLASS_DECISION.md` — priority order decided under delegated authority, narrowed per the trademark review, and the residual **accepted by the founders on 2026-09-08** (`../TRADEMARK_RISK_REVIEW.md`) | — (the review's §5 rule is mandatory at QA; a §3 re-review trigger reopens the posture, not the gate item) |
| 3 | The bank covers 22 pieces at the measured per-piece counts | **NOT STARTED — WAITS ON ITEM 5** (2026-09-13) | The requirement is quantified: **42 C2 images**, ≈ 6–12 C4, 0–3 C1, 1–2 AI illustrations; the bank plan in `../assets/C2_SOURCING_ROUTES.md` is now sized by the stress test's measured minutes per image, on routes F + X (+ B per brand, S fallback) — the earlier 15-hour rig-and-shoot build is withdrawn because the founders have no owned inventory | Run item 5 first; then the route F pass, the route X batch, the silhouette library; record every row |
| 4 | Provenance record for every asset | **INSTRUMENT BUILT — 0 ASSETS RECORDED** | `../assets/provenance_register.csv` (schema), worked example, `tools/validate_provenance.py` (passes on the example) | Populate as assets land; validator clean before any piece is scheduled |
| 5 | C2 sustainability test: two complete pieces end-to-end, timed | **NOT RUN — PACKAGE PREPARED (protocol v2, 2026-09-13)** | `../assets/C2_SUSTAINABILITY_TEST.md` (v2: burden by stage, candidates and rejections logged, pre-declared decision rule) and the package in `../assets/c2_stress_test/` — two briefs, logs, permission template, founder instructions, results template, `tools/validate_c2_stress_test.py`; pass thresholds kept (≤ 1.5 × budget: 135 / 172 active min) and extended (≥ 5 of 7 photographic per piece; weekly extrapolation ≤ 4 h); the pieces are **non-publishing prototypes**, promoted to reserve only after a pass | Run it per `../assets/c2_stress_test/FOUNDER_INSTRUCTIONS.md`; bring back the two logs, the register rows and `RESULTS.md`. **NOT SUSTAINABLE → STOP and escalate**; nothing is redesigned to pass |
| 6 | C3 data-source ToS check per source; no scraper | **PASSED 2026-09-08** | `../assets/C3_DATA_SOURCE_TOS_REGISTER.md` operationalised under the founders' conservative data-source posture: press releases, published reports and release notes are the sources; every marketplace is excluded because its terms do not clearly permit the use; product pages confirm only | — (a row reopens only if a source publishes explicit permission) |
| 7 | C4 imagery source confirmed; never-a-reposted-template rule in the production checklist | **PASSED 2026-09-08** | `SOURCE_CLASS_DECISION.md` §2 (self-drawn → owned → licensed → AI in six slots) as a delegated production decision; the rule in `../operations/PRE_PUBLISH_QA.md` §A and §E; seven originated house formats replace any template | Photographs of branded sneakers in C4 wait on the same ACCEPT as item 2 |
| 8 | No gate item requires reposting, Collabs or relaxing the originality rule | **CONFIRMED BY CONSTRUCTION** | Every active route in the stack is owned, licensed, verified-press or self-generated; no permission outreach at all (founder decision, 2026-09-13) — so no grantor exists to promote | — |
| 9 | AI generation tool(s) named; output licence confirmed to permit commercial use | **PASSED 2026-10-07** | **Adobe Firefly** selected as a delegated production decision (Gemini alternate); the current terms read and mapped to our use on 2026-09-11 in `../assets/FIREFLY_TERMS_VERIFICATION.md` (dates re-checked 2026-09-13); **confirmed by Wasim on 2026-10-07** against the live pages — ownership, commercial use, Input/prohibited-content rules, Content Credentials, the indemnity's non-applicability to our route — and recorded in the memo §5: **free tier only, no paid plan**; Adobe-native Firefly image model (exact version logged at TEST-AI-01); pre-existing Adobe ID, creation date not established; no Gallery/Community, no Adobe Stock | — (a paid plan would be a separate founder spending approval; the confirmed licence changes nothing for C2: AI stays in the six C4 slots plus TEST-AI-01) |
| 10 | One complete AI-treated C4 piece produced end-to-end, timed | **NOT PRODUCED — PROTOCOL READY** | `../policy/AI_IMAGERY_POLICY_PACK.md` §7 (TEST-AI-01, a Reel in the shape of `B-W2-C4-REE-01`) | Produce it; log generation, review and production minutes |
| 11 | That piece verified against the prohibited-use list, carrying the fixed disclosure, label observed | **NOT DONE — CHECKLIST AND WORDING READY** | Nine-item checklist (§4); disclosure wording proposed (§3) | Founders lock the wording; run the checklist on TEST-AI-01; observe the label |
| 12 | No AI asset reconstructs a third-party image; none in C1/C2/C3 | **ENFORCED BY INSTRUMENT — ATTESTATION PENDING** | Validator refuses AI assets outside the six slots or in C1–C3; attestation field mandatory | Sign the attestation on TEST-AI-01 and on each of the six real assets |

## Reading the scorecard

- **Passed on 2026-09-08:** items 1, 2, 6, 7 and 8 — item 2 closed by the founders'
  acceptance of the trademark posture (`../TRADEMARK_RISK_REVIEW.md`). **Passed on 2026-10-07:** item 9
  (Firefly licence confirmed by Wasim; free tier only). **Six of twelve passed. Founder execution remaining:**
  items 3, 4, 5 (the bank, the provenance rows, the sustainability test), 10, 11, 12 (the AI test piece).
- The binding sequence (revised 2026-09-13, after the founders stated they have no owned inventory): ~~founders
  confirm Firefly's terms~~ (**done 2026-10-07**) → **run the two-piece stress test on routes F, B
  and S (P as `WOULD_USE_P` only; no route X — the founders do not solicit permissions)** → read the
  pre-declared verdict → **only if it sustains**, build the 42-image bank sized by the
  measured minutes per image → produce and check the AI test piece → sign off. **If the test returns NOT
  SUSTAINABLE, the gate stops there and the finding is escalated** — the design is not adjusted to pass.
- Estimated founder effort to pass: **no longer estimated in advance.** The stress test measures it; the
  test piece (≈ 2 h) stands. The AI confirmation is done.

## Sign-off

| Item | Passed (date) | Sari | Wasim |
|---|---|---|---|
| 1–8 (imagery arm) | | ☐ | ☐ |
| 9–12 (AI arm) | | ☐ | ☐ |
| **Sourcing Gate PASSED** | | ☐ | ☐ |
