#!/usr/bin/env python3
"""Instantiate the locked matrix onto real dates from a start Monday — LOCALLY, never into the repository.

Usage:  python3 tools/instantiate_calendar.py --start YYYY-MM-DD [--out PATH] [--print]

The start date is NOT chosen and must never be recorded in this repository (LOCK_SPECIFICATION.md §1, item 2;
the start rule: first Monday after both gates pass). This script takes the date as an argument and writes to
_local/ (gitignored) by default. Run it only once the gates have passed, or with a hypothetical Monday to see
the shape of the calendar.

For every one of the 84 slots it emits: publish datetime (16:00 UTC), local conversions, the check-out deadline
(C1 T-48h · C3 T-7d · C2/C4 T-10d), the C1 ladder (T-48h lock · T-24h production complete · T-12h scheduled),
the T+7 snapshot instant and T+14 for Reels, and the production week. Then the 84 Stories (17:30 UTC, rotation
class, sticker day), the weekly reviews, the mid-test checkpoint, the tail snapshots and the decision point,
and a daylight-saving straddle check for the EU/UK (25 Oct 2026) and US (1 Nov 2026) transitions.
"""
import argparse, csv, json, os, sys
from datetime import datetime, date, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATRIX = os.path.join(ROOT, "experiment", "active-84-post-plan", "matrix_84.csv")
CONSTANTS = os.path.join(ROOT, "production", "templates", "template_constants.json")
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
CHECKOUT_H = {"C1": 48, "C2": 240, "C3": 168, "C4": 240}
DST = [("EU/UK clocks change", date(2026, 10, 25)), ("US/Canada clocks change", date(2026, 11, 1))]


def fmt(dt): return dt.strftime("%Y-%m-%d %H:%M UTC")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="Week-1 Monday, YYYY-MM-DD")
    ap.add_argument("--out", default=None, help="CSV path (default _local/calendar_<start>.csv)")
    ap.add_argument("--print", action="store_true", help="print the summary and the C1 ladder")
    a = ap.parse_args()
    try:
        y, m, d = (int(x) for x in a.start.split("-")); start = date(y, m, d)
    except Exception:
        sys.exit("--start must be YYYY-MM-DD")
    if start.weekday() != 0:
        sys.exit(f"{start} is a {WEEKDAYS[start.weekday()]}; the experiment starts on a Monday")
    consts = json.load(open(CONSTANTS))
    with open(MATRIX, newline="") as fh:
        matrix = list(csv.DictReader(fh))
    out = a.out or os.path.join(ROOT, "_local", f"calendar_{start.isoformat()}.csv")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.commonpath([os.path.abspath(out), ROOT]) == ROOT and "_local" not in os.path.abspath(out).split(os.sep):
        sys.exit("Refusing to write an instantiated calendar inside the tracked repository tree. Use _local/ or a path outside the repo.")

    rows = []
    end = start + timedelta(days=41)
    for r in matrix:
        D = (int(r["week"]) - 1) * 7 + int(r["day"][1:])
        pub_date = start + timedelta(days=D - 1)
        pub = datetime.combine(pub_date, datetime.min.time(), tzinfo=timezone.utc) + timedelta(hours=16)
        eng, fmt_ = r["engine"], r["format"]
        row = {
            "type": "FEED", "slot_id": r["slot_id"], "account": r["account"], "handle": r["account_handle"], "week": r["week"],
            "day_index": D, "weekday": r["weekday"], "engine": eng, "format": fmt_, "block": r["block"], "ai_overlay": r["ai_overlay"],
            "publish_date": pub_date.isoformat(), "publish_utc": fmt(pub),
            "publish_local_utc+3": (pub + timedelta(hours=3)).strftime("%H:%M"), "publish_local_utc+2": (pub + timedelta(hours=2)).strftime("%H:%M"),
            "checkout_deadline_utc": fmt(pub - timedelta(hours=CHECKOUT_H[eng])),
            "c1_topic_lock_utc": fmt(pub - timedelta(hours=48)) if eng == "C1" else "",
            "c1_production_complete_utc": fmt(pub - timedelta(hours=24)) if eng == "C1" else "",
            "c1_scheduled_by_utc": fmt(pub - timedelta(hours=12)) if eng == "C1" else "",
            "production_week": "P-1 (before launch)" if int(r["week"]) == 1 else f"posting week {int(r['week']) - 1}",
            "t7_snapshot_utc": fmt(pub + timedelta(days=7)), "t14_snapshot_utc": fmt(pub + timedelta(days=14)) if fmt_ == "REEL" else "",
            "rotation_class": "", "sticker": "",
        }
        rows.append(row)
    rotation, sticker_day = consts["story_rotation"], consts["story_sticker_weekday"]
    for acct, handle in (("A", "thestreetwearofficial"), ("B", "sneakerbong")):
        for D in range(1, 43):
            pd = start + timedelta(days=D - 1); wd = WEEKDAYS[pd.weekday()]
            st = datetime.combine(pd, datetime.min.time(), tzinfo=timezone.utc) + timedelta(hours=17, minutes=30)
            rows.append({"type": "STORY", "slot_id": f"{acct}-W{(D - 1) // 7 + 1}-D{(D - 1) % 7 + 1}-ST", "account": acct, "handle": handle,
                         "week": (D - 1) // 7 + 1, "day_index": D, "weekday": wd, "engine": "", "format": "STORY", "block": "", "ai_overlay": "",
                         "publish_date": pd.isoformat(), "publish_utc": fmt(st), "publish_local_utc+3": "20:30", "publish_local_utc+2": "19:30",
                         "checkout_deadline_utc": "", "c1_topic_lock_utc": "", "c1_production_complete_utc": "", "c1_scheduled_by_utc": "",
                         "production_week": "batched the Thursday before", "t7_snapshot_utc": "", "t14_snapshot_utc": "",
                         "rotation_class": rotation[pd.weekday()], "sticker": "Y" if wd == sticker_day else ""})
    # milestones
    ms = [("MILESTONE", "DAY-0 · C1 topic lock for A-W1-C1-CAR-01 (16:00 UTC, before launch)", start - timedelta(days=1)),
          ("MILESTONE", "WEEK-1 GATE Layer 1 must be complete (all 11 non-C1 pieces scheduled)", start - timedelta(days=1))]
    for w in range(1, 7):
        ms.append(("MILESTONE", f"Weekly review · after posting week {w} (same day/time each week; founders fix it)", start + timedelta(days=7 * w)))
    ms.append(("MILESTONE", "Mid-test checkpoint · diagnostic, safety, data-quality only — NO allocation authority", start + timedelta(days=21)))
    ms.append(("MILESTONE", "Last feed post (Day 42)", end))
    ms.append(("MILESTONE", "Last T+7 snapshot due", end + timedelta(days=7)))
    ms.append(("MILESTONE", "Last T+14 Reel snapshot due · end of measurement tail · decision point on W3–6 medians", end + timedelta(days=14)))
    for typ, label, dt in ms:
        rows.append({k: "" for k in rows[0]} | {"type": typ, "slot_id": label, "publish_date": dt.isoformat()})
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    straddle = [(n, dd) for n, dd in DST if start <= dd <= end + timedelta(days=14)]
    print(f"Start Monday {start} · last post {end} · last Reel snapshot {end + timedelta(days=14)}")
    print(f"Written: {os.path.relpath(out, ROOT) if out.startswith(ROOT) else out}  ({len(rows)} rows: 84 feed, 84 Story, {len(ms)} milestones)")
    if straddle:
        for n, dd in straddle:
            print(f"DST NOTE: {n} on {dd} falls inside the posting weeks or the tail. The 16:00 UTC instant does not move; local wall-clock does. Log it as a known event; do not chase it.")
    else:
        print("DST: no EU/UK or US transition inside the posting weeks or the measurement tail.")
    if a.print:
        print("\nC1 deadline ladder (all 21 slots):")
        for r in rows:
            if r["type"] == "FEED" and r["engine"] == "C1":
                print(f"  {r['slot_id']:16s} {r['weekday']} {r['publish_date']}  lock {r['c1_topic_lock_utc'][:16]}  prod {r['c1_production_complete_utc'][:16]}  sched {r['c1_scheduled_by_utc'][:16]}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        pass
