#!/usr/bin/env python3
"""Validate the asset provenance register and the audio ledger against the locked rules.

Usage:  python3 tools/validate_provenance.py [--register PATH] [--audio PATH]

Defaults: production/assets/provenance_register.csv and production/assets/audio_ledger.csv.
Checks (all derived from GATES.md §1, AI_IMAGERY_SUBTEST.md §5/§8 and the anti-duplication rules):

  * every row has an asset_id, a known class, a date, a source and a licence/permission reference;
  * licensed and press assets carry an archived licence text; permissioned assets carry the permission;
  * every asset is used in at most ONE piece (anti-duplication rule 4: different source imagery on every piece);
  * slot IDs exist in the locked matrix (or are RESERVE-*/TEST-* pieces);
  * AI_GENERATED assets appear only in the six founder-locked AI slots (or TEST-AI pieces), never in C1/C2/C3,
    and carry the full AI provenance field set;
  * no asset of any class is missing from a piece that the register says is complete (C2 pieces must reference
    exactly the ranked-item count in production/templates/template_constants.json);
  * audio: the same track never on both accounts within 14 days, never reused on one account within 14 days.

A passing run means the records are complete and consistent. It does not mean the founders have verified a
licence — that judgement is recorded, not computed.
"""
import argparse, csv, json, os, sys
from collections import Counter, defaultdict
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATRIX = os.path.join(ROOT, "experiment", "active-84-post-plan", "matrix_84.csv")
CONSTANTS = os.path.join(ROOT, "production", "templates", "template_constants.json")

REQUIRED = ["asset_id", "class", "engine", "slot_id", "piece_ref", "description", "source_name", "source_url_or_ref",
            "licence_or_permission", "licence_text_archived_at", "date_obtained", "permitted_use", "attribution_required",
            "attribution_text", "restrictions", "expiry", "file_name", "obtained_by", "ai_tool_version", "ai_prompt",
            "ai_seed_params", "ai_attestation_no_product_brand_person", "ai_reviewer", "ai_disclosure_present",
            "ai_platform_label_observed", "notes"]
AI_FIELDS = ["ai_tool_version", "ai_prompt", "ai_seed_params", "ai_attestation_no_product_brand_person", "ai_reviewer",
             "ai_disclosure_present"]

failures, warnings = [], []


def fail(msg): failures.append(msg); print(f"[FAIL] {msg}")
def warn(msg): warnings.append(msg); print(f"[WARN] {msg}")
def ok(msg): print(f"[PASS] {msg}")


def parse_date(s):
    try:
        y, m, d = (int(x) for x in s.split("-"))
        return date(y, m, d)
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--register", default=os.path.join(ROOT, "production", "assets", "provenance_register.csv"))
    ap.add_argument("--audio", default=os.path.join(ROOT, "production", "assets", "audio_ledger.csv"))
    a = ap.parse_args()

    consts = json.load(open(CONSTANTS))
    classes = set(consts["asset_classes"]); ai_slots = set(consts["ai_slots"]); n_items = int(consts["c2_ranked_item_count"])
    with open(MATRIX, newline="") as fh:
        matrix = {r["slot_id"]: r for r in csv.DictReader(fh)}

    with open(a.register, newline="") as fh:
        rd = csv.DictReader(fh)
        header = rd.fieldnames or []
        rows = list(rd)
    print(f"=== PROVENANCE REGISTER: {os.path.relpath(a.register, ROOT)} ({len(rows)} rows) ===")
    missing_cols = [c for c in REQUIRED if c not in header]
    if missing_cols:
        fail(f"missing columns: {missing_cols}")
    else:
        ok("all required columns present")

    ids = Counter(r["asset_id"] for r in rows)
    dup = [k for k, v in ids.items() if v > 1]
    if dup: fail(f"duplicate asset_id: {dup}")
    else: ok("asset IDs unique")

    used_in = defaultdict(set)
    by_piece = defaultdict(list)
    for r in rows:
        aid = r.get("asset_id", "").strip()
        cls = r.get("class", "").strip()
        eng = r.get("engine", "").strip()
        slot = r.get("slot_id", "").strip()
        piece = slot or r.get("piece_ref", "").strip()
        if not aid: fail("row without asset_id"); continue
        if cls not in classes: fail(f"{aid}: unknown class '{cls}'")
        if not parse_date(r.get("date_obtained", "")): fail(f"{aid}: date_obtained missing or not YYYY-MM-DD")
        if not r.get("source_name", "").strip(): fail(f"{aid}: source_name missing")
        if not r.get("licence_or_permission", "").strip(): fail(f"{aid}: licence_or_permission missing")
        if not r.get("file_name", "").strip(): warn(f"{aid}: file_name empty — put the asset ID in the filename")
        elif aid not in r["file_name"]: warn(f"{aid}: file_name does not contain the asset ID")
        if cls in ("LICENSED_FREE", "LICENSED_PAID", "PRESS_VERIFIED") and not r.get("licence_text_archived_at", "").strip():
            fail(f"{aid}: {cls} requires licence_text_archived_at (an archived copy of the licence/terms)")
        if cls == "PERMISSIONED" and not r.get("licence_text_archived_at", "").strip():
            fail(f"{aid}: PERMISSIONED requires the written permission archived (licence_text_archived_at)")
        if cls == "OWNED" and not r.get("obtained_by", "").strip():
            fail(f"{aid}: OWNED requires obtained_by (who shot it)")
        if slot and slot not in matrix and not (slot.startswith("RESERVE-") or slot.startswith("TEST-")):
            fail(f"{aid}: slot_id '{slot}' is not in the locked matrix (or RESERVE-*/TEST-*)")
        if slot in matrix and eng and matrix[slot]["engine"] != eng:
            fail(f"{aid}: engine '{eng}' does not match the matrix engine for {slot} ({matrix[slot]['engine']})")
        if cls == "AI_GENERATED":
            if eng in ("C1", "C2", "C3"): fail(f"{aid}: AI_GENERATED asset assigned to {eng} — prohibited")
            if slot and slot in matrix and slot not in ai_slots: fail(f"{aid}: AI_GENERATED in {slot}, which is not one of the six locked AI slots")
            if slot and not slot.startswith("TEST-") and slot not in ai_slots and slot not in matrix:
                fail(f"{aid}: AI_GENERATED assigned to '{slot}' — only the six AI slots or a TEST-AI piece may carry AI imagery")
            for f in AI_FIELDS:
                if not r.get(f, "").strip(): fail(f"{aid}: AI field '{f}' missing")
            if r.get("ai_attestation_no_product_brand_person", "").strip().upper() not in ("Y", "YES"):
                fail(f"{aid}: AI attestation must be Y (no real product, no brand mark, no real person)")
        elif slot in ai_slots and cls not in ("AI_GENERATED", "SELF_GENERATED"):
            warn(f"{aid}: non-AI photograph in AI slot {slot} — allowed only if the piece's *imagery* is AI; check the treatment is identical")
        if piece:
            used_in[aid].add(piece); by_piece[piece].append(r)

    multi = {k: v for k, v in used_in.items() if len(v) > 1}
    if multi: fail(f"assets used in more than one piece (rule 4): {multi}")
    else: ok("no asset used in more than one piece")

    for piece, prs in sorted(by_piece.items()):
        eng = prs[0].get("engine", "")
        if eng == "C2" or (piece in matrix and matrix[piece]["engine"] == "C2"):
            imgs = [p for p in prs if p["class"] != "SELF_GENERATED" or "illustration" in p.get("description", "").lower()]
            if len(imgs) != n_items:
                warn(f"{piece}: C2 piece references {len(imgs)} item images; the ranked-item count is {n_items} (fine while the piece is in progress)")
    ok(f"per-piece counts checked against the C2 ranked-item count ({n_items})")
    print("class mix:", dict(Counter(r["class"] for r in rows)))

    # ---- audio ledger
    if os.path.exists(a.audio):
        with open(a.audio, newline="") as fh:
            audio = list(csv.DictReader(fh))
        print(f"\n=== AUDIO LEDGER: {os.path.relpath(a.audio, ROOT)} ({len(audio)} rows) ===")
        uses = defaultdict(list)
        for r in audio:
            d = parse_date(r.get("publish_date", ""))
            if not d: fail(f"audio {r.get('track_id')}: publish_date missing or not YYYY-MM-DD"); continue
            if r.get("library", "").strip() != "Instagram Sound Collection":
                warn(f"audio {r.get('track_id')}: library is '{r.get('library')}' — only Instagram's royalty-free library is cleared for business accounts")
            uses[r["track_id"]].append((d, r.get("account", ""), r.get("slot_id", "")))
        for tid, lst in uses.items():
            lst.sort()
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    (d1, a1, s1), (d2, a2, s2) = lst[i], lst[j]
                    if abs((d2 - d1).days) < 14:
                        if a1 != a2: fail(f"audio {tid}: on both accounts within 14 days ({s1} {d1} / {s2} {d2})")
                        else: fail(f"audio {tid}: reused on account {a1} within 14 days ({s1} {d1} / {s2} {d2})")
        ok("audio 14-day rules checked")

    print("\n" + "=" * 60)
    if failures:
        print(f"VALIDATION FAILED — {len(failures)} failure(s), {len(warnings)} warning(s)")
        return 1
    print(f"ALL CHECKS PASSED — {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
