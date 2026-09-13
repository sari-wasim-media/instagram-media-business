#!/usr/bin/env python3
"""Validate the two-piece C2 sourcing stress test and print its burden summary and decision-rule reading.

Usage:  python3 tools/validate_c2_stress_test.py [--example]

Reads production/assets/c2_stress_test/candidates_log.csv and timing_log.csv (the _EXAMPLE files with
--example), production/assets/provenance_register.csv and production/templates/template_constants.json.
Checks (from C2_SUSTAINABILITY_TEST.md v2 and C2_SOURCING_ROUTES.md, revised 2026-09-13):

  * every candidate has an id, a known piece, an item number 1..N, a route and a known clearance status;
  * a CLEARED candidate passed all three checks (trademark-rule fit, ownership plausibility, licence), carries
    an asset ID that exists in the provenance register under the same piece with the class its route implies,
    and — for routes F / X / B / P — has its evidence archived; a route X clearance has both permission dates;
  * "credited" is never "cleared": a CLEARED row with a licence/ownership check blank or N fails;
  * a REJECTED / LAPSED / SWAPPED_OUT row states its reason; at most one CLEARED candidate per item;
  * timing rows use the fixed stage list; PERMISSION_WAIT is passive and nothing else is; minutes are numbers;
  * summary: active minutes per piece and per stage, passive wait, cleared route mix, S share, rejections by
    reason, swaps, usable routes, share satisfied without paid spend, would-have-used-P count, minutes per
    cleared image, and the extrapolation formulas of C2_SUSTAINABILITY_TEST.md §7;
  * the pre-declared decision rule (§5) is read out when both pieces are complete; otherwise INCOMPLETE.

A passing run means the logs are complete and internally consistent. It does not mean a founder verified a
licence — that judgement is recorded, not computed — and it never fills in a number that was not measured.
"""
import argparse, csv, json, os, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_DIR = os.path.join(ROOT, "production", "assets", "c2_stress_test")
REGISTER = os.path.join(ROOT, "production", "assets", "provenance_register.csv")
CONSTANTS = os.path.join(ROOT, "production", "templates", "template_constants.json")

CAND_COLS = ["candidate_id", "piece_ref", "item_no", "item_name", "colorway", "route", "source_name",
             "source_url_or_ref", "licence_as_displayed", "creator_or_rightsholder", "found_by", "date_checked",
             "tm_rule_fit", "ownership_plausible", "licence_ok", "attribution_required", "clearance_status",
             "rejection_reason", "permission_requested_date", "permission_reply_date", "asset_id",
             "evidence_archived_at", "notes"]
TIME_COLS = ["entry_id", "piece_ref", "item_no", "stage", "active_or_passive", "started_utc", "finished_utc",
             "minutes", "who", "notes"]

ROUTES = {"F": "LICENSED_FREE", "X": "PERMISSIONED", "B": "PRESS_VERIFIED", "P": "LICENSED_PAID",
          "S": "SELF_GENERATED", "O": "OWNED"}
PHOTOGRAPHIC = {"F", "X", "B", "P", "O"}
EVIDENCE_REQUIRED = {"F", "X", "B", "P"}
STATUSES = {"CANDIDATE", "CLEARED", "REJECTED", "PENDING", "UNCLEAR", "BLOCKED", "LAPSED", "SWAPPED_OUT"}
REASONS = {"PEOPLE", "CONTEXT", "LICENCE", "LAUNDERED", "WATERMARK", "WRONG_ITEM", "QUALITY",
           "COUNTERFEIT_RISK", "DUPLICATE", "NO_REPLY", "DECLINED", "NOT_FOUND", "UNCLEAR_RIGHTS", "OTHER"}
STAGES = ["THEME", "DISCOVERY", "RIGHTS_VERIFY", "PERMISSION_REQUEST", "PERMISSION_WAIT", "ASSET_PREP",
          "PROVENANCE", "ILLUSTRATION", "RESEARCH", "LAYOUT", "REEL_ASSEMBLY", "CAPTION_QA"]
SOURCING_STAGES = {"DISCOVERY", "RIGHTS_VERIFY", "PERMISSION_REQUEST", "ASSET_PREP", "PROVENANCE", "ILLUSTRATION"}
PIECES = {"TEST-C2-CAR-01": ("Carousel", 90), "TEST-C2-REE-01": ("Reel", 115)}
PASS_FACTOR = 1.5
PIECES_PER_WEEK = 21 / 6.0

failures, warnings = [], []


def fail(msg): failures.append(msg); print(f"[FAIL] {msg}")
def warn(msg): warnings.append(msg); print(f"[WARN] {msg}")
def ok(msg): print(f"[PASS] {msg}")


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as fh:
        rd = csv.DictReader(fh)
        return rd.fieldnames or [], list(rd)


def yes(v): return v.strip().upper() in ("Y", "YES")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--example", action="store_true", help="validate the _EXAMPLE logs instead of the live ones")
    a = ap.parse_args()
    suffix = "_EXAMPLE" if a.example else ""
    cand_path = os.path.join(TEST_DIR, f"candidates_log{suffix}.csv")
    time_path = os.path.join(TEST_DIR, f"timing_log{suffix}.csv")
    n_items = int(json.load(open(CONSTANTS))["c2_ranked_item_count"])

    # ---- register (asset IDs the cleared candidates must point at)
    _, reg_rows = read_csv(REGISTER)
    register = {r["asset_id"].strip(): r for r in reg_rows if r.get("asset_id", "").strip()}

    # ---- candidates
    header, cands = read_csv(cand_path)
    print(f"=== CANDIDATE LOG: {os.path.relpath(cand_path, ROOT)} ({len(cands)} rows) ===")
    missing = [c for c in CAND_COLS if c not in header]
    if missing: fail(f"candidate log missing columns: {missing}")
    else: ok("candidate log columns present")
    ids = Counter(r["candidate_id"].strip() for r in cands)
    dup = [k for k, v in ids.items() if v > 1]
    if dup: fail(f"duplicate candidate_id: {dup}")

    cleared = defaultdict(dict)           # piece -> item_no -> row
    rejected = Counter(); swaps = Counter(); pending = Counter(); unclear = Counter()
    routes_used = defaultdict(Counter)    # piece -> route -> cleared count
    would_use_p = Counter()
    prescan = 0
    for r in cands:
        cid = r.get("candidate_id", "").strip() or "<no id>"
        piece = r.get("piece_ref", "").strip()
        status = r.get("clearance_status", "").strip().upper()
        route = r.get("route", "").strip().upper()
        try:
            item = int(r.get("item_no", "").strip())
        except ValueError:
            item = None
        if not (piece.startswith("TEST-C2-") or piece.startswith("RESERVE-C2-")):
            fail(f"{cid}: piece_ref '{piece}' is not a TEST-C2-* / RESERVE-C2-* piece")
        if item is None or not (1 <= item <= n_items):
            fail(f"{cid}: item_no must be 1..{n_items}")
        if status not in STATUSES:
            fail(f"{cid}: unknown clearance_status '{status}'"); continue
        if status != "SWAPPED_OUT" and route not in ROUTES:
            fail(f"{cid}: unknown route '{route}' (F X B P S O)")
        if r.get("found_by", "").strip().upper() == "CLAUDE_PRESCAN":
            prescan += 1
        if "WOULD_USE_P" in r.get("notes", "").upper():
            would_use_p[piece] += 1

        if status == "CLEARED":
            for chk in ("tm_rule_fit", "ownership_plausible", "licence_ok"):
                if not yes(r.get(chk, "")):
                    fail(f"{cid}: CLEARED but {chk} is not Y — a credited or unverified image is not a cleared image")
            aid = r.get("asset_id", "").strip()
            if not aid:
                fail(f"{cid}: CLEARED without an asset_id (write the provenance row first)")
            elif a.example:
                pass  # the example log points at illustrative asset IDs; the register cross-check is skipped
            elif aid not in register:
                fail(f"{cid}: asset_id {aid} not found in provenance_register.csv")
            else:
                reg = register[aid]
                reg_piece = reg.get("slot_id", "").strip() or reg.get("piece_ref", "").strip()
                if reg_piece != piece:
                    fail(f"{cid}: {aid} is recorded under '{reg_piece}' in the register, not '{piece}'")
                if route in ROUTES and reg.get("class", "").strip() != ROUTES[route]:
                    fail(f"{cid}: route {route} implies class {ROUTES[route]} but the register says '{reg.get('class')}'")
            if route in EVIDENCE_REQUIRED and not r.get("evidence_archived_at", "").strip():
                fail(f"{cid}: route {route} CLEARED without evidence_archived_at (licence / permission / terms archived)")
            if route == "X" and not (r.get("permission_requested_date", "").strip() and r.get("permission_reply_date", "").strip()):
                fail(f"{cid}: route X CLEARED needs both permission_requested_date and permission_reply_date")
            if item in cleared[piece]:
                fail(f"{cid}: item {item} of {piece} already has a CLEARED candidate ({cleared[piece][item]['candidate_id']})")
            else:
                cleared[piece][item] = r
                routes_used[piece][route] += 1
        elif status in ("REJECTED", "LAPSED", "SWAPPED_OUT"):
            reason = r.get("rejection_reason", "").strip().upper()
            if reason not in REASONS:
                fail(f"{cid}: {status} needs a rejection_reason from {sorted(REASONS)}")
            if status == "SWAPPED_OUT": swaps[piece] += 1
            else: rejected[reason] += 1
        elif status == "PENDING":
            pending[piece] += 1
            if not r.get("permission_requested_date", "").strip():
                fail(f"{cid}: PENDING without permission_requested_date")
        elif status in ("UNCLEAR", "BLOCKED"):
            unclear[piece] += 1
    ok("candidate rows checked")

    # ---- timing
    header, times = read_csv(time_path)
    print(f"\n=== TIMING LOG: {os.path.relpath(time_path, ROOT)} ({len(times)} rows) ===")
    missing = [c for c in TIME_COLS if c not in header]
    if missing: fail(f"timing log missing columns: {missing}")
    else: ok("timing log columns present")
    tids = Counter(r["entry_id"].strip() for r in times)
    dup = [k for k, v in tids.items() if v > 1]
    if dup: fail(f"duplicate entry_id: {dup}")
    active = defaultdict(lambda: defaultdict(float))   # piece -> stage -> minutes
    passive = defaultdict(float)
    for r in times:
        tid = r.get("entry_id", "").strip() or "<no id>"
        piece = r.get("piece_ref", "").strip()
        stage = r.get("stage", "").strip().upper()
        mode = r.get("active_or_passive", "").strip().upper()
        if not (piece.startswith("TEST-C2-") or piece.startswith("RESERVE-C2-")):
            fail(f"{tid}: piece_ref '{piece}' is not a TEST-C2-* / RESERVE-C2-* piece")
        if stage not in STAGES:
            fail(f"{tid}: unknown stage '{stage}' ({', '.join(STAGES)})"); continue
        if stage == "PERMISSION_WAIT" and mode != "PASSIVE":
            fail(f"{tid}: PERMISSION_WAIT must be PASSIVE")
        if stage != "PERMISSION_WAIT" and mode != "ACTIVE":
            fail(f"{tid}: {stage} must be ACTIVE (only PERMISSION_WAIT is passive)")
        try:
            m = float(r.get("minutes", "").strip())
            if m < 0: raise ValueError
        except ValueError:
            fail(f"{tid}: minutes must be a non-negative number"); continue
        if mode == "PASSIVE": passive[piece] += m
        else: active[piece][stage] += m
    ok("timing rows checked")

    # ---- summary
    print("\n=== BURDEN SUMMARY (measured rows only — nothing is estimated) ===")
    total_cleared = 0; total_sourcing = 0.0; photographic_ok = {}; s_share = {}
    complete = {}
    for piece, (fmt, budget) in PIECES.items():
        c = cleared.get(piece, {})
        n = len(c); total_cleared += n
        complete[piece] = (n == n_items)
        act = active.get(piece, {})
        tot = sum(act.values())
        sourcing = sum(v for k, v in act.items() if k in SOURCING_STAGES)
        total_sourcing += sourcing
        photo = sum(v for k, v in routes_used[piece].items() if k in PHOTOGRAPHIC)
        s_n = routes_used[piece].get("S", 0)
        photographic_ok[piece] = photo; s_share[piece] = s_n
        limit = budget * PASS_FACTOR
        print(f"\n{piece} ({fmt}) — cleared {n}/{n_items}"
              + (" COMPLETE" if complete[piece] else " INCOMPLETE")
              + f"; pending {pending.get(piece, 0)}; unclear/blocked {unclear.get(piece, 0)}; swaps {swaps.get(piece, 0)}")
        print(f"  active minutes: {tot:.0f} / budget {budget} (pass <= {limit:.0f})"
              + ("" if tot <= limit else "  ** OVER **"))
        print("  by stage: " + ", ".join(f"{k} {act[k]:.0f}" for k in STAGES if k in act))
        print(f"  sourcing minutes (discovery+verify+request+prep+provenance+illustration): {sourcing:.0f}")
        print(f"  passive permission wait: {passive.get(piece, 0):.0f} min")
        mix = ", ".join(f"{k} {v}" for k, v in sorted(routes_used[piece].items()))
        print(f"  cleared route mix: {mix or '—'}   photographic {photo}/{n}   S {s_n}/{n}")
        paid = routes_used[piece].get("P", 0)
        if n: print(f"  satisfied without paid spend: {100.0 * (n - paid) / n:.0f} %   would-have-used-P: {would_use_p.get(piece, 0)}")
    print(f"\nrejections by reason: {dict(rejected) or '—'}")
    usable = sorted({k for p in routes_used.values() for k, v in p.items() if v > 0})
    print(f"usable routes (>= 1 cleared asset): {usable or '—'}")
    if prescan: print(f"rows found by CLAUDE_PRESCAN (reported separately, cleared nothing): {prescan}")
    if total_cleared:
        m = total_sourcing / total_cleared
        weekly = PIECES_PER_WEEK * n_items * m / 60.0
        print(f"\nactive sourcing minutes per cleared image, m = {m:.1f}")
        print(f"extrapolated weekly C2 sourcing load = {PIECES_PER_WEEK:.1f} pieces x {n_items} x m / 60 = {weekly:.1f} h  (Friday block 4 h; conditions 4-6 h; stop > 6 h)")
        print(f"42-image bank = {42 * m / 60:.1f} h (28 x m = {28 * m / 60:.1f} h if the prototypes are promoted); 147 images = {147 * m / 60:.1f} h")
    else:
        weekly = None
        print("\nno cleared images yet — no per-image figure, no extrapolation")

    # ---- decision rule (§5), read top to bottom
    print("\n=== DECISION RULE (C2_SUSTAINABILITY_TEST.md §5) ===")
    if not all(complete.values()):
        print(f"INCOMPLETE — {total_cleared}/{2 * n_items} items cleared; the rule is not read until both pieces are complete")
    else:
        stop, cond = [], []
        for piece, (fmt, budget) in PIECES.items():
            tot = sum(active.get(piece, {}).values())
            if tot > budget * PASS_FACTOR: stop.append(f"{piece} over 1.5x budget ({tot:.0f} > {budget * PASS_FACTOR:.0f})")
            if photographic_ok[piece] < 4: stop.append(f"{piece}: only {photographic_ok[piece]}/{n_items} photographic — illustration-led")
            elif photographic_ok[piece] == 4: cond.append(f"{piece}: route S on 3/{n_items}")
            if unclear.get(piece, 0): stop.append(f"{piece}: {unclear[piece]} UNCLEAR/BLOCKED candidate(s) on record — founders confirm none was needed")
            if would_use_p.get(piece, 0): cond.append(f"{piece}: {would_use_p[piece]} item(s) would have used P (a spend decision)")
            if passive.get(piece, 0) > 10 * 24 * 60: cond.append(f"{piece}: a permission wait exceeded the 10-day check-out lead")
        if weekly is not None:
            if weekly > 6: stop.append(f"extrapolated weekly load {weekly:.1f} h > 6 h")
            elif weekly > 4: cond.append(f"extrapolated weekly load {weekly:.1f} h is between 4 and 6 h")
        if stop:
            print("NOT SUSTAINABLE — STOP AND ESCALATE:"); [print("  - " + s) for s in stop]
        elif cond:
            print("SUSTAINABLE WITH CONDITIONS:"); [print("  - " + s) for s in cond]
        else:
            print("SUSTAINABLE (by the numbers; the founders confirm no terms ambiguity needs counsel, RESULTS.md §3)")
        print("Two conditions are founder judgements the validator cannot compute: a rights basis that could not be\n"
              "established for a needed item, and a recurring terms ambiguity that needs counsel. Record both in RESULTS.md.")

    print("\n" + "=" * 60)
    if failures:
        print(f"VALIDATION FAILED — {len(failures)} failure(s), {len(warnings)} warning(s)")
        return 1
    print(f"ALL CHECKS PASSED — {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
