# C2 sourcing stress test — the package

**Sourcing Gate item 5, protocol v2 (2026-09-13). Status: PREPARED — NOT RUN. Zero timings recorded.**

Two non-publishing C2 prototypes, seven ranked items each, fourteen image requirements, sourced without
founder-owned inventory, timed by stage, every candidate logged — to find out whether the locked C2 design
can be produced repeatedly and rights-clean on the routes that actually exist. No Week-1 slot is consumed,
nothing is scheduled or published, no date is chosen. The protocol and the pre-declared decision rule are in
`../C2_SUSTAINABILITY_TEST.md`.

| File | Role | Filled by |
|---|---|---|
| `TEST_PIECES.md` | The two briefs: themes, 7 items + 2 alternates each, formats, budgets | Claude (done) |
| `FOUNDER_INSTRUCTIONS.md` | The manual run — A (prepared) / B (founders do) / C (evidence back) — including the Firefly confirmation and the route B checks | Claude (done); founders execute |
| `PERMISSION_REQUEST_TEMPLATE.md` | Route X: the message, the reply that counts, the record | Claude (done); founders send |
| `candidates_log.csv` | One row per candidate image, cleared or rejected; the three checks; clearance status; reasons | Founders (Claude pre-scan rows possible, marked) |
| `timing_log.csv` | One row per stage per item; active vs passive | Founders |
| `RESULTS.md` | The measured table, extrapolation, ambiguities, verdict, sign-off | Founders, then Claude |
| `PRESCAN_NOTES.md` | Claude's read-only discovery pre-scan of 2026-09-13: per-item coverage of the free-licence pool, its own minutes, four leads logged as `CANDIDATE` — clears nothing | Claude (done) |
| `*_EXAMPLE.csv` | Filled examples of both logs (fictional) | — |
| `../provenance_register.csv` | The clearance record — cleared assets only, existing schema, `piece_ref = TEST-C2-…` | Founders |
| `../../../tools/validate_c2_stress_test.py` | Consistency checks, burden summary, the decision rule read out | — |

```
python3 tools/validate_c2_stress_test.py            # live logs
python3 tools/validate_c2_stress_test.py --example  # the filled examples
python3 tools/validate_provenance.py                # the register, as always
```

**Route F in this test** (founder correction, 2026-09-13): CC0 / public domain → Pexels → Unsplash → other
unambiguous free licences; **CC BY is not used**.

**Clearance statuses:** `CANDIDATE` (found, unverified) · `CLEARED` (three checks Y, evidence archived,
asset ID) · `REJECTED` (reason) · `PENDING` (permission asked) · `LAPSED` (no reply in 7 days) · `UNCLEAR` /
`BLOCKED` (rights not established — never used) · `SWAPPED_OUT` (item replaced by an alternate, reason).
**Rejection reasons:** `PEOPLE` · `CONTEXT` · `LICENCE` · `LAUNDERED` · `WATERMARK` · `WRONG_ITEM` ·
`QUALITY` · `COUNTERFEIT_RISK` · `DUPLICATE` · `NO_REPLY` · `DECLINED` · `NOT_FOUND` · `UNCLEAR_RIGHTS` · `OTHER`.
**Stages:** `THEME` · `DISCOVERY` · `RIGHTS_VERIFY` · `PERMISSION_REQUEST` · `PERMISSION_WAIT` (the only
passive one) · `ASSET_PREP` · `PROVENANCE` · `ILLUSTRATION` · `RESEARCH` · `LAYOUT` · `REEL_ASSEMBLY` · `CAPTION_QA`.
