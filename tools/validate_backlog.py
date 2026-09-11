#!/usr/bin/env python3
"""Validate the topic backlog and the check-out log against the locked queue and anti-duplication rules.

Usage:  python3 tools/validate_backlog.py [--start YYYY-MM-DD]

Reads production/backlog/backlog.csv and production/backlog/checkout_log.csv.
--start is Day 1 (any weekday), used ONLY to check check-out deadlines against absolute publish instants.
It is never written anywhere; without it the deadline checks are skipped and everything else still runs.

Checks (ANTI_DUPLICATION_AND_TOPIC_SELECTION.md §2, §3, §5):
  * every check-out references an existing OPEN/CHECKED_OUT/USED entry of the same engine and a valid slot;
  * the queue rule: FIFO for C2/C3/C4 (earliest entry_timestamp among eligible), nearest confirmed date for C1
    inside the slot window, ties by entry timestamp — the taken item must be the top eligible item;
  * check-out deadlines: C1 T-48h, C3 T-7d, C2/C4 T-10d (needs --start);
  * cross-account: never the same subject_key within 14 days; never the same thesis within 14 days;
  * within-account: same subject_key at most twice per account and never within 10 days; same thesis once;
  * the blind-to-performance attestation (performance_data_referenced == NO) on every check-out;
  * the logged queue position equals the computed one.
"""
import argparse, csv, os, sys
from collections import defaultdict
from datetime import datetime, date, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATRIX = os.path.join(ROOT, "experiment", "active-84-post-plan", "matrix_84.csv")
BACKLOG = os.path.join(ROOT, "production", "backlog", "backlog.csv")
LOG = os.path.join(ROOT, "production", "backlog", "checkout_log.csv")

ENGINES = {"C1", "C2", "C3", "C4"}
DEADLINE_H = {"C1": 48, "C2": 240, "C3": 168, "C4": 240}
C1_WINDOW_BEFORE_D, C1_WINDOW_AFTER_D = 7, 10   # proposed operational window, see production/backlog/README.md
failures, warnings = [], []


def fail(m): failures.append(m); print(f"[FAIL] {m}")
def warn(m): warnings.append(m); print(f"[WARN] {m}")
def ok(m): print(f"[PASS] {m}")


def ts(s):
    s = s.strip()
    if not s: return None
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%MZ", "%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M"):
        try: return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError: pass
    return None


def d(s):
    s = s.strip()
    if not s: return None
    try: y, m, dd = (int(x) for x in s.split("-")); return date(y, m, dd)
    except Exception: return None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--start", default=None); a = ap.parse_args()
    start = d(a.start) if a.start else None
    if a.start and not start:
        sys.exit("--start must be Day 1 in YYYY-MM-DD form (any weekday)")
    with open(MATRIX, newline="") as fh:
        matrix = {r["slot_id"]: r for r in csv.DictReader(fh)}
    dayidx = {s: (int(r["week"]) - 1) * 7 + int(r["day"][1:]) for s, r in matrix.items()}   # 1..42

    def publish_dt(slot):
        if not start: return None
        return datetime.combine(start + timedelta(days=dayidx[slot] - 1), datetime.min.time(), tzinfo=timezone.utc) + timedelta(hours=16)

    with open(BACKLOG, newline="") as fh: backlog = list(csv.DictReader(fh))
    with open(LOG, newline="") as fh: log = list(csv.DictReader(fh))
    print(f"=== BACKLOG {len(backlog)} entries · CHECK-OUT LOG {len(log)} rows{' · start ' + a.start if start else ' · no --start: deadline checks skipped'} ===")

    entries = {}
    for e in backlog:
        eid = e.get("entry_id", "").strip()
        if not eid: fail("backlog entry without entry_id"); continue
        if eid in entries: fail(f"duplicate entry_id {eid}")
        entries[eid] = e
        if e.get("engine", "").strip() not in ENGINES: fail(f"{eid}: engine '{e.get('engine')}' invalid")
        if not ts(e.get("entry_timestamp_utc", "")): fail(f"{eid}: entry_timestamp_utc missing or not ISO (YYYY-MM-DDTHH:MMZ)")
        if not e.get("subject_key", "").strip(): fail(f"{eid}: subject_key missing (colorway/model-level key)")
        if e.get("engine", "").strip() == "C1":
            if not d(e.get("news_or_release_date", "")): fail(f"{eid}: C1 entry needs a confirmed news_or_release_date")
            if not e.get("source_of_date", "").strip(): fail(f"{eid}: C1 entry needs source_of_date")
        if e.get("status", "").strip() not in ("OPEN", "CHECKED_OUT", "USED", "INVALID", "EXPIRED"):
            fail(f"{eid}: status '{e.get('status')}' invalid")
    ok("backlog entries well-formed") if not failures else None

    # check-outs in chronological order
    log_sorted = sorted(log, key=lambda r: ts(r.get("checkout_timestamp_utc", "")) or datetime.max.replace(tzinfo=timezone.utc))
    taken_before = defaultdict(set)   # engine -> entry ids checked out before the current one
    slot_used = {}
    placements = []                   # (slot, account, dayidx, subject_key, secondary keys, thesis)
    for r in log_sorted:
        cid, slot, eid = r.get("checkout_id", "").strip(), r.get("slot_id", "").strip(), r.get("entry_id", "").strip()
        t = ts(r.get("checkout_timestamp_utc", ""))
        if not t: fail(f"{cid}: checkout_timestamp_utc missing or not ISO"); continue
        if slot not in matrix: fail(f"{cid}: slot_id '{slot}' not in the locked matrix"); continue
        if slot in slot_used: fail(f"{cid}: slot {slot} already checked out by {slot_used[slot]}")
        slot_used[slot] = cid
        m = matrix[slot]; eng = m["engine"]
        if r.get("account", "").strip() != m["account"]: fail(f"{cid}: account '{r.get('account')}' does not match the matrix ({m['account']}) for {slot}")
        if r.get("engine", "").strip() != eng: fail(f"{cid}: engine '{r.get('engine')}' does not match the matrix ({eng}) for {slot}")
        if r.get("performance_data_referenced", "").strip().upper() != "NO":
            fail(f"{cid}: performance_data_referenced must be NO (blind-to-performance rule §5.3)")
        e = entries.get(eid)
        if not e: fail(f"{cid}: entry {eid} not in the backlog"); continue
        if e.get("engine", "").strip() != eng: fail(f"{cid}: entry {eid} is {e.get('engine')} but slot {slot} is {eng}")
        # eligible set at check-out time
        elig = [x for k, x in entries.items() if x.get("engine", "").strip() == eng and (ts(x.get("entry_timestamp_utc", "")) or datetime.max.replace(tzinfo=timezone.utc)) <= t
                and x.get("status", "").strip() not in ("INVALID", "EXPIRED") and k not in taken_before[eng]]
        pub = publish_dt(slot)
        if eng == "C1":
            if pub:
                lo, hi = pub.date() - timedelta(days=C1_WINDOW_BEFORE_D), pub.date() + timedelta(days=C1_WINDOW_AFTER_D)
                elig = [x for x in elig if d(x.get("news_or_release_date", "")) and lo <= d(x["news_or_release_date"]) <= hi]
                elig.sort(key=lambda x: (abs((d(x["news_or_release_date"]) - pub.date()).days), ts(x["entry_timestamp_utc"])))
            else:
                elig.sort(key=lambda x: (d(x.get("news_or_release_date", "")) or date.max, ts(x["entry_timestamp_utc"])))
                warn(f"{cid}: C1 window not applied (no --start); ordering checked by date only")
            rule = "C1_NEAREST_CONFIRMED_DATE"
        else:
            elig.sort(key=lambda x: ts(x["entry_timestamp_utc"]))
            rule = "FIFO"
        if r.get("rule_applied", "").strip() != rule: warn(f"{cid}: rule_applied '{r.get('rule_applied')}' — expected {rule}")
        pos = next((i + 1 for i, x in enumerate(elig) if x["entry_id"] == eid), None)
        if pos is None: fail(f"{cid}: entry {eid} was not eligible at check-out time (timestamp, status, window)")
        elif pos != 1: fail(f"{cid}: DEVIATION — took queue position {pos}, top eligible item was {elig[0]['entry_id']}")
        logged = r.get("queue_position_at_checkout", "").strip()
        if pos is not None and logged and logged != str(pos): fail(f"{cid}: logged queue position {logged} ≠ computed {pos}")
        if pub:
            deadline = pub - timedelta(hours=DEADLINE_H[eng])
            if t > deadline: fail(f"{cid}: checked out at {t:%Y-%m-%d %H:%M}Z, after the T−{DEADLINE_H[eng]}h deadline {deadline:%Y-%m-%d %H:%M}Z")
        taken_before[eng].add(eid)
        sec = [s.strip() for s in e.get("secondary_subjects", "").split(";") if s.strip()]
        placements.append((slot, m["account"], dayidx[slot], e.get("subject_key", "").strip(), sec, e.get("thesis", "").strip().lower()))

    # anti-duplication across placements (day-index arithmetic needs no calendar)
    for i in range(len(placements)):
        for j in range(i + 1, len(placements)):
            s1, a1, d1, k1, sec1, th1 = placements[i]; s2, a2, d2, k2, sec2, th2 = placements[j]
            gap = abs(d1 - d2)
            keys1, keys2 = {k1} | set(sec1), {k2} | set(sec2)
            shared = keys1 & keys2 - {""}
            if shared:
                if a1 != a2 and gap < 14: fail(f"{s1} / {s2}: same subject {shared} on both accounts within 14 days (gap {gap})")
                if a1 == a2 and gap < 10: fail(f"{s1} / {s2}: same subject {shared} on one account within 10 days (gap {gap})")
            if th1 and th1 == th2:
                if a1 == a2: fail(f"{s1} / {s2}: same thesis twice on account {a1}")
                elif gap < 14: fail(f"{s1} / {s2}: same thesis on both accounts within 14 days (gap {gap})")
    per_acct = defaultdict(int)
    for s, acct, _, k, _, _ in placements:
        if k: per_acct[(acct, k)] += 1
    for (acct, k), n in per_acct.items():
        if n > 2: fail(f"subject {k} anchors {n} posts on account {acct} (max 2)")
    ok("queue rule, deadlines (where checkable) and anti-duplication rules evaluated")

    print("\n" + "=" * 60)
    if failures:
        print(f"VALIDATION FAILED — {len(failures)} failure(s), {len(warnings)} warning(s)"); return 1
    print(f"ALL CHECKS PASSED — {len(warnings)} warning(s)"); return 0


if __name__ == "__main__":
    sys.exit(main())
