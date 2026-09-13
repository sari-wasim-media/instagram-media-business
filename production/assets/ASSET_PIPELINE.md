# Asset pipeline — from an idea to a provenance-recorded, rights-clean image in a named file

**Purpose.** The Sourcing Gate turns on four things: a source-class decision per engine, a bank of assets
that covers 22 pieces, a provenance record for every asset, and a C2 route proven end-to-end. This directory
holds the instruments for all four. The pipeline below is the operating procedure the founders run.

| File | What it is | Gate item |
|---|---|---|
| `SOURCE_CLASS_DECISION.md` | Which classes supply each engine, in priority order; the accepted trademark residual (2026-09-08) | 2 |
| `C2_SOURCING_ROUTES.md` | Routes F · X · B · P · S · O (order revised 2026-09-13 — no owned inventory) with steps, costs, throughput; the bank build, sized by the stress test | 3, 5 |
| `C2_SUSTAINABILITY_TEST.md` | The two-piece sourcing stress test — protocol v2 with the pre-declared decision rule | 5 |
| `c2_stress_test/` | The stress-test package: briefs, candidate and timing logs, founder instructions, results | 5 |
| `C3_DATA_SOURCE_TOS_REGISTER.md` | Per-source terms verification register | 6 |
| `SOURCING_ROUTES_RESEARCH.md` | The research record behind all of the above (accessed 2026-09-05) | — |
| `provenance_register.csv` | **The register. One row per asset. Empty until the founders source the first asset** | 4 |
| `provenance_register_EXAMPLE.csv` | Six example rows showing every class filled in correctly | — |
| `audio_ledger.csv` (+ `_EXAMPLE`) | One row per track use; enforces the 14-day audio rules | — |
| `../../tools/validate_provenance.py` | Validates both CSVs against the locked rules | 4 |
| `../../tools/validate_c2_stress_test.py` | Validates the stress-test logs against the register; prints the burden summary and the decision rule's reading | 5 |

## The rule that governs everything here

> **No asset without a provenance record may be used in any of the 84 posts** (`GATES.md` §1.3 item 4).
> The record is written **before** layout, not after publishing.

**And one rule on top of it:** every photograph of a branded sneaker — owned, licensed or permissioned —
carries the trademark residual the founders accepted on 2026-09-08, so every such piece is produced under the
review's §5 nominative-use operating rule (`../TRADEMARK_RISK_REVIEW.md`) and checked against it at QA.
Illustration, charts, typography and house UI are unaffected.

## The flow, per asset

1. **Need** — a piece in production (or the bank build) needs an image of item X.
2. **Route** — take the first route in the engine's priority order (`SOURCE_CLASS_DECISION.md` §2) that can
   supply X; fall through in order (C2 since 2026-09-13: F → B → P with approval → S; O only when a pair is
   at hand; no permission outreach — route X is not active). C2 always ends at route S (illustration), so no C2 slot fails for want of an image — but a
   piece that is mostly illustration is reported as such, never silently normalised. **Credit is not
   permission**: an image whose rights are not established is logged in the candidate log as UNCLEAR /
   BLOCKED and never receives an asset ID.
3. **Obtain** — shoot / download / draw / generate. For licensed and press assets, **archive the licence or
   terms text** (PDF or screenshot with date) at the same moment.
4. **Record** — append a row to `provenance_register.csv` with the next `AST-nnnn` ID: class, engine, slot or
   piece, source, licence reference, archived-text location, date, permitted use, restrictions, who obtained
   it. AI assets add tool, prompt, seed, attestation, reviewer, disclosure.
5. **Name** — save the file as `<slot_id>__AST-nnnn.<ext>` (reserve pieces: `RESERVE-C2-CAR-01__AST-nnnn`;
   the AI test piece: `TEST-AI-01__AST-nnnn`). The asset ID travels in the filename, the register and the
   tracking row, so assets and data never separate.
6. **Validate** — `python3 tools/validate_provenance.py` must pass before the piece is scheduled.
7. **Use once** — an asset ID belongs to exactly one piece, ever (anti-duplication rule 4). A second use of
   the same pair is a second photograph with a second ID.

## The local asset store (not in this repository)

Image files, licence archives and AI generations live on the founders' shared drive, never in Git — this
repository holds the register, not the media. Suggested layout, mirrored on both founders' machines:

```
assets/
  shoots/YYYY-MM-DD/            owned photographs, raw and plate-ready
  stock/                        licensed downloads, one folder per source
  licences/                     archived licence and terms texts, dated
  illustration/                 the house silhouette library (SVG) and exports
  ai/YYYY-MM-DD/                generations with their prompt logs
  exports/<slot_id>/            the final frames and video per slot, named with asset IDs
```

The register's `source_url_or_ref` and `licence_text_archived_at` columns use `local://…` paths into this
store. `_local/` in the repository is gitignored and may hold a working copy of the register while a batch
is in progress; the committed register is the truth once the batch is done.

## The bank, tracked

| Bank | Needed for the Sourcing Gate | Recorded | Validated |
|---|---|---|---|
| C2 stress-test prototypes (`TEST-C2-CAR-01`, `TEST-C2-REE-01`) | **14** — non-publishing; count toward the 42 only if promoted to reserve | 0 | — |
| C2 product images | **42** (4 Week-1 pieces + 2 reserve pieces × 7) | 0 | — |
| C4 imagery (non-AI) | ≈ 6–12 | 0 | — |
| C1 optional imagery | 0–3 | 0 | — |
| AI test piece illustrations | 1–2 | 0 | — |
| Story Saturday plates (Week 1) | ≈ 2 | 0 | — |

Update the "Recorded" column as rows land; the gate scorecard (`../gates/SOURCING_GATE_SCORECARD.md`) reads
from here.

## Audio

Music is added at upload from Instagram's Sound Collection (the one library Meta states is cleared for
business accounts). Each use is a row in `audio_ledger.csv`: track, slot, account, publish date. The validator
enforces the two locked 14-day rules. Keep at least 24 tracks in rotation. Never bake music from CapCut or
Canva into an export.
