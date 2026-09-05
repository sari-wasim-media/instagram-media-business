#!/usr/bin/env python3
"""Validate the locked 84-post revival matrix against every founder-locked invariant.

Usage:  python3 tools/validate_matrix.py

Reads experiment/active-84-post-plan/matrix_84.csv and fails loudly if any
locked property of the design has drifted. Run this after ANY edit to the
matrix file. A passing run is not permission to change the matrix -- the matrix
is founder-locked and frozen for the duration of the controlled experiment.
"""
import csv, os, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "experiment", "active-84-post-plan", "matrix_84.csv")

ACCOUNTS = ["A", "B"]
ENGINES = ["C1", "C2", "C3", "C4"]
FORMATS = ["REEL", "CARO", "STAT"]
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# The six founder-locked AI-imagery sub-test slots. C4 only, 3 per account,
# one Reel + one Carousel + one Static per account.
AI_SLOTS = {
    "B-W2-C4-REE-01", "A-W2-C4-CAR-01", "B-W2-C4-STA-01",
    "A-W4-C4-REE-01", "B-W5-C4-CAR-01", "A-W6-C4-STA-01",
}

failures = []


def check(label, ok, detail=""):
    (print if ok else print)(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" -- {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(label + (f" -- {detail}" if detail else ""))


def main():
    with open(CSV_PATH, newline="") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        r["week"] = int(r["week"])

    steady = [r for r in rows if r["block"] == "STEADY"]
    warm = [r for r in rows if r["block"] == "WARM"]

    print("=== STRUCTURE ===")
    check("84 rows", len(rows) == 84, f"got {len(rows)}")
    check("84 unique slot IDs", len({r["slot_id"] for r in rows}) == 84)
    check("84 unique (account, week, day)",
          len({(r["account"], r["week"], r["day"]) for r in rows}) == 84)
    check("42 rows per account",
          all(sum(1 for r in rows if r["account"] == a) == 42 for a in ACCOUNTS))
    per_aw = Counter((r["account"], r["week"]) for r in rows)
    check("7 rows per account per week", all(v == 7 for v in per_aw.values()) and len(per_aw) == 12)
    per_w = Counter(r["week"] for r in rows)
    check("14 rows per week combined", all(per_w[w] == 14 for w in range(1, 7)))
    check("6 weeks only", set(per_w) == set(range(1, 7)))
    check("blocks: 28 WARM (W1-2) / 56 STEADY (W3-6)",
          len(warm) == 28 and len(steady) == 56
          and all(r["week"] <= 2 for r in warm) and all(r["week"] >= 3 for r in steady))
    check("every row has one account/week/day/engine/format/time",
          all(r["account"] in ACCOUNTS and r["engine"] in ENGINES and r["format"] in FORMATS
              and r["weekday"] in WEEKDAYS and r["publish_utc"] == "16:00" for r in rows))
    check("single fixed publish instant 16:00 UTC on all 84 rows",
          {r["publish_utc"] for r in rows} == {"16:00"})

    print("\n=== ENGINE BALANCE ===")
    eng = Counter(r["engine"] for r in rows)
    check("21 pooled posts per engine", all(eng[e] == 21 for e in ENGINES), dict(eng))
    ae = Counter((r["account"], r["engine"]) for r in rows)
    check("account x engine = A:11/11/10/10, B:10/10/11/11",
          [ae[("A", e)] for e in ENGINES] == [11, 11, 10, 10]
          and [ae[("B", e)] for e in ENGINES] == [10, 10, 11, 11])
    ae_s = Counter((r["account"], r["engine"]) for r in steady)
    check("W3-6: exactly 7 posts per account per engine",
          all(ae_s[(a, e)] == 7 for a in ACCOUNTS for e in ENGINES))

    print("\n=== FORMAT BALANCE ===")
    af = Counter((r["account"], r["format"]) for r in rows)
    check("24R / 12C / 6S per account",
          all([af[(a, f)] for f in FORMATS] == [24, 12, 6] for a in ACCOUNTS))
    fmt = Counter(r["format"] for r in rows)
    check("48R / 24C / 12S pooled", [fmt[f] for f in FORMATS] == [48, 24, 12])
    wf = Counter((r["account"], r["week"], r["format"]) for r in rows)
    check("4R / 2C / 1S per account per week",
          all([wf[(a, w, f)] for f in FORMATS] == [4, 2, 1]
              for a in ACCOUNTS for w in range(1, 7)))

    print("\n=== ENGINE x FORMAT ===")
    ef = Counter((r["engine"], r["format"]) for r in rows)
    check("pooled engine x format = 12R / 6C / 3S per engine",
          all([ef[(e, f)] for f in FORMATS] == [12, 6, 3] for e in ENGINES))
    aef = Counter((r["account"], r["engine"], r["format"]) for r in rows)
    check("per account: exactly 6 Reels and 3 Carousels per engine",
          all(aef[(a, e, "REEL")] == 6 and aef[(a, e, "CARO")] == 3
              for a in ACCOUNTS for e in ENGINES))
    check("per-account residual confined to STAT (A:2,2,1,1 / B:1,1,2,2)",
          [aef[("A", e, "STAT")] for e in ENGINES] == [2, 2, 1, 1]
          and [aef[("B", e, "STAT")] for e in ENGINES] == [1, 1, 2, 2])
    aef_s = Counter((r["account"], r["engine"], r["format"]) for r in steady)
    check("W3-6: engine x format = exactly 4R / 2C / 1S per account per engine",
          all([aef_s[(a, e, f)] for f in FORMATS] == [4, 2, 1]
              for a in ACCOUNTS for e in ENGINES))

    print("\n=== WEEKDAY BALANCE ===")
    awd = Counter((r["account"], r["weekday"]) for r in rows)
    check("6 posts per weekday per account",
          all(awd[(a, d)] == 6 for a in ACCOUNTS for d in WEEKDAYS))
    awde_s = Counter((r["account"], r["weekday"], r["engine"]) for r in steady)
    check("W3-6: every engine appears exactly once per weekday per account",
          all(awde_s[(a, d, e)] == 1 for a in ACCOUNTS for d in WEEKDAYS for e in ENGINES))
    awdf = Counter((r["account"], r["weekday"], r["format"]) for r in rows)
    check("weekday x format inside declared band (3-4R / 1-2C / 0-1S per account)",
          all(3 <= awdf[(a, d, "REEL")] <= 4 and 1 <= awdf[(a, d, "CARO")] <= 2
              and 0 <= awdf[(a, d, "STAT")] <= 1 for a in ACCOUNTS for d in WEEKDAYS))

    print("\n=== CONTAMINATION STRUCTURE ===")
    by_pair = defaultdict(list)
    for r in rows:
        by_pair[r["pair"]].append(r)
    check("42 publishing pairs, 2 rows each",
          len(by_pair) == 42 and all(len(v) == 2 for v in by_pair.values()))
    check("A and B never publish the same engine on the same date",
          all(v[0]["engine"] != v[1]["engine"] for v in by_pair.values()))

    print("\n=== AI-IMAGERY SUB-TEST OVERLAY ===")
    ai = [r for r in rows if r["ai_overlay"] == "AI"]
    check("exactly 6 AI slots", len(ai) == 6, f"got {len(ai)}")
    check("AI slots are exactly the founder-locked six",
          {r["slot_id"] for r in ai} == AI_SLOTS,
          str({r["slot_id"] for r in ai} ^ AI_SLOTS))
    check("all AI slots are C4", all(r["engine"] == "C4" for r in ai))
    check("no AI overlay in C1/C2/C3",
          not any(r["ai_overlay"] == "AI" and r["engine"] in ("C1", "C2", "C3") for r in rows))
    check("AI: 3 per account", Counter(r["account"] for r in ai) == Counter({"A": 3, "B": 3}))
    check("AI: 1 Reel + 1 Carousel + 1 Static per account",
          all(Counter(r["format"] for r in ai if r["account"] == a)
              == Counter({"REEL": 1, "CARO": 1, "STAT": 1}) for a in ACCOUNTS))
    check("AI: 2 per format overall",
          Counter(r["format"] for r in ai) == Counter({"REEL": 2, "CARO": 2, "STAT": 2}))
    check("AI: 3 WARM / 3 STEADY", Counter(r["block"] for r in ai) == Counter({"WARM": 3, "STEADY": 3}))
    check("AI: format x block is 1 WARM / 1 STEADY for each format",
          all(Counter(r["block"] for r in ai if r["format"] == f)
              == Counter({"WARM": 1, "STEADY": 1}) for f in FORMATS))
    check("AI: zero AI slots in Week 1 (launch week protected)",
          not any(r["week"] == 1 for r in ai))
    check("AI: no two AI slots share a publishing pair",
          len({r["pair"] for r in ai}) == 6)
    ai_steady_c4 = sum(1 for r in steady if r["engine"] == "C4" and r["ai_overlay"] == "AI")
    c4_steady = sum(1 for r in steady if r["engine"] == "C4")
    check("AI contamination of C4 in W3-6 is 3 of 14",
          ai_steady_c4 == 3 and c4_steady == 14, f"{ai_steady_c4}/{c4_steady}")

    print("\n=== STORY PROTOCOL ARITHMETIC (locked constants) ===")
    stories_per_day, days = 1, 42
    check("1 Story/day/account -> 7/week/account", stories_per_day * 7 == 7)
    check("42 Stories per account over 6 weeks", stories_per_day * days == 42)
    check("84 Stories combined", stories_per_day * days * 2 == 84)
    check("6 interactive stickers per account (1/week)", 1 * 6 == 6)

    print("\n" + "=" * 60)
    if failures:
        print(f"VALIDATION FAILED -- {len(failures)} check(s):")
        for f in failures:
            print("  -", f)
        return 1
    print("ALL CHECKS PASSED -- matrix conforms to the Founder Lock.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
