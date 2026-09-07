#!/usr/bin/env python3
"""Build the tracking-sheet skeleton from the locked matrix.

Usage:  python3 tools/build_tracking_sheet.py

Reads  experiment/active-84-post-plan/matrix_84.csv  (never retyped — imported)
       production/templates/template_constants.json  (Story rotation, sticker weekday)
Writes experiment/tracking/posts.csv           84 rows, one per feed post, measurement columns blank
       experiment/tracking/account_weekly.csv  2 accounts x 9 weeks (W0 baseline, W1-W6, W7-W8 tail)
       experiment/tracking/stories.csv         84 rows, one per Story
       experiment/tracking/tracking_sheet.xlsx the same three tabs plus a README tab, with the per-reach
                                               rate columns as formulas that divide by Reach

The sheet is a manual instrument. Founders fill it by hand from Instagram Insights at T+7 / T+14 / T+2.
No date is instantiated here: publish_date stays blank until the founders run tools/instantiate_calendar.py
locally and copy the dates in. Re-running this script regenerates the SKELETON only — it never overwrites a
sheet that already carries data (it refuses if any measurement cell is filled).
"""
import csv, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATRIX = os.path.join(ROOT, "experiment", "active-84-post-plan", "matrix_84.csv")
CONSTANTS = os.path.join(ROOT, "production", "templates", "template_constants.json")
OUT = os.path.join(ROOT, "experiment", "tracking")

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

POST_COLS = [
    # identity — imported from the matrix, never edited
    "slot_id", "account", "account_handle", "week", "day", "weekday", "engine", "format", "block", "pair", "ai_overlay", "publish_utc",
    # instantiated locally
    "publish_date",
    # production
    "status", "producer", "checkout_id", "subject", "secondary_subjects", "thesis", "house_format_or_variant",
    "asset_ids", "audio_track_id", "sources", "c1_rubric_score", "caption_final", "alt_text_done", "hashtags",
    "reel_duration_s", "slide_count", "scheduled_at_utc", "schedule_screenshot_ref", "actual_publish_utc",
    "originality_status", "pressure_point_check",
    # T+7 primary snapshot — Reach (unique accounts) is the denominator for every rate
    "t7_snapshot_date", "t7_age_days", "t7_reach", "t7_views", "t7_follower_reach", "t7_nonfollower_reach",
    "t7_pct_nonfollower_reach", "t7_likes", "t7_comments", "t7_sends_shares", "t7_saves", "t7_profile_visits", "t7_follows",
    "t7_avg_watch_time_s", "t7_total_watch_time_s", "t7_replays",
    "t7_likes_per_reach", "t7_comments_per_reach", "t7_sends_per_reach", "t7_saves_per_reach", "t7_profile_visits_per_reach",
    # T+14 tail snapshot — Reels only
    "t14_snapshot_date", "t14_age_days", "t14_reach", "t14_views", "t14_nonfollower_reach", "t14_pct_nonfollower_reach",
    "t14_likes", "t14_comments", "t14_sends_shares", "t14_saves", "t14_sends_per_reach", "t14_saves_per_reach",
    # community and compliance
    "replies_made", "corrections_acknowledged", "spam_hidden", "ai_platform_label_observed",
    "protocol_deviation", "notes",
]
WEEKLY_COLS = [
    "account", "account_handle", "week", "week_label", "week_start_date", "week_end_date",
    "followers_start", "followers_end", "net_change", "reach_7d_descriptive_only", "pct_nonfollower_reach_7d_descriptive_only",
    "profile_visits", "external_link_taps", "status_features", "status_content_removals", "status_recommendation_eligibility",
    "status_under_18", "status_monetization", "all_five_green", "status_screenshot_ref",
    "posts_published_reel", "posts_published_caro", "posts_published_stat", "stories_published", "late_rows", "buffer_pieces_banked",
    "reserve_pieces_remaining", "instagram_notifications", "reviewed_by", "review_date", "notes",
]
STORY_COLS = [
    "story_id", "account", "account_handle", "week", "day", "weekday", "rotation_class", "sticker", "adjacent_engine",
    "scheduled_utc", "publish_date", "actual_publish_utc", "status", "producer", "asset_ids",
    "t2_snapshot_date", "t2_age_days", "t2_reach", "t2_views", "t2_forward_taps", "t2_back_taps", "t2_exits",
    "t2_replies", "t2_sticker_interactions", "breakout_support_used", "deviation", "notes",
]
ROTATION_ENGINE = {"DROP CALENDAR": "C1", "PRICE CHECK": "C3", "THE POLL": "C2", "DESK NOTES": "", "THE VERDICT": "C1",
                   "TWO SHOES": "C4", "THE WEEK": ""}
STATUS_VALUES = ["PLANNED", "CHECKED_OUT", "IN_PRODUCTION", "QA_PASSED", "SCHEDULED", "PUBLISHED", "LATE", "MISS",
                 "RECOVERED", "REMOVED", "BLOCKED", "INCOMPLETE"]
ORIGINALITY_VALUES = ["ORIGINAL", "VIOLATION_LOGGED"]


def read_matrix():
    with open(MATRIX, newline="") as fh:
        return list(csv.DictReader(fh))


def build_rows(matrix, consts):
    posts = []
    for r in matrix:
        row = {c: "" for c in POST_COLS}
        for c in ("slot_id", "account", "account_handle", "week", "day", "weekday", "engine", "format", "block", "pair",
                  "ai_overlay", "publish_utc"):
            row[c] = r[c]
        row["status"] = "PLANNED"
        row["originality_status"] = "ORIGINAL"
        if r["slot_id"] in ("A-W3-C1-REE-01", "A-W3-C1-REE-02", "A-W5-C2-REE-01", "A-W5-C2-REE-02"):
            row["pressure_point_check"] = "REQUIRED"
        if r["format"] != "REEL":
            row["t14_snapshot_date"] = "n/a"
        posts.append(row)

    handles = {"A": "thestreetwearofficial", "B": "sneakerbong"}
    weekly = []
    labels = {0: "W0 baseline (pre-launch)", 7: "W7 measurement tail", 8: "W8 tail / decision point"}
    for acct in ("A", "B"):
        for w in range(0, 9):
            row = {c: "" for c in WEEKLY_COLS}
            row.update({"account": acct, "account_handle": handles[acct], "week": w,
                        "week_label": labels.get(w, f"W{w} posting week ({'WARM' if w <= 2 else 'STEADY'})"),
                        "external_link_taps": "0 expected (no link in bio)"})
            weekly.append(row)

    rotation = consts["story_rotation"]; sticker_day = consts["story_sticker_weekday"]
    stories = []
    for acct in ("A", "B"):
        for w in range(1, 7):
            for d in range(1, 8):
                cls = rotation[d - 1]; wd = WEEKDAYS[d - 1]
                row = {c: "" for c in STORY_COLS}
                row.update({"story_id": f"{acct}-W{w}-D{d}-ST", "account": acct, "account_handle": handles[acct], "week": w,
                            "day": f"D{d}", "weekday": wd, "rotation_class": cls, "sticker": "Y" if wd == sticker_day else "",
                            "adjacent_engine": ROTATION_ENGINE.get(cls, ""), "scheduled_utc": "17:30", "status": "PLANNED"})
                stories.append(row)
    return posts, weekly, stories


def refuse_if_data_present(path, id_col, skeleton_cols):
    """Never regenerate over a sheet that carries measurements."""
    if not os.path.exists(path):
        return
    with open(path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        for c in skeleton_cols:
            if c.startswith(("t7_", "t14_", "t2_", "followers_", "actual_publish")) and r.get(c, "").strip() not in ("", "n/a"):
                sys.exit(f"REFUSING to overwrite {os.path.relpath(path, ROOT)}: row {r.get(id_col)} already holds data in '{c}'. "
                         "Back it up and delete it first if you really mean to regenerate the skeleton.")


def write_csv(path, cols, rows):
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader(); w.writerows(rows)


def write_xlsx(path, posts, weekly, stories):
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill, Alignment
        from openpyxl.utils import get_column_letter
        from openpyxl.worksheet.datavalidation import DataValidation
    except ImportError:
        print("openpyxl not installed — CSVs written, XLSX skipped (pip install openpyxl)"); return
    wb = Workbook()
    readme = wb.active; readme.title = "README"
    lines = [
        "TRACKING SHEET — 84-post controlled revival experiment (skeleton generated from matrix_84.csv)",
        "",
        "RULES THAT GOVERN THIS SHEET",
        "1. Reach is the denominator for every rate metric. Reach = the unique-accounts figure Instagram reports for the post (record it in *_reach). The UI label for that figure (Accounts reached / Viewers) is UNVERIFIED until observed per format on both real accounts at the Week-0 baseline; the label does not change the rule. Views (plays incl. repeats) is recorded but is never a denominator and is never divided by follower count.",
        "2. Snapshots at fixed ages: T+7 for every feed post, T+14 additionally for every Reel, T+2 for every Story. Record the actual age in days; if it deviates from the target by more than 48 h, mark AGE_DEVIATION in protocol_deviation.",
        "3. No blank measurement cells for any post past T+7. Never back-fill estimates.",
        "4. Weekly account-level Reach and non-follower Reach (account_weekly tab) are descriptive context only — no decision authority (Rule S).",
        "5. Medians on weeks 3–6 are the decision statistic; maximums are ceiling evidence. Nothing in this sheet triggers any change to the schedule.",
        "6. status values: " + ", ".join(STATUS_VALUES) + ".  originality_status: " + ", ".join(ORIGINALITY_VALUES) + ".",
        "7. The identity columns (slot_id … publish_utc) are imported from the locked matrix and are never edited. publish_date is filled from tools/instantiate_calendar.py once the start Monday exists.",
        "8. Every asset ID in asset_ids must exist in production/assets/provenance_register.csv; every checkout_id in production/backlog/checkout_log.csv.",
        "9. The six AI slots carry ai_overlay = AI; ai_platform_label_observed is filled at T+7 for those six only.",
        "10. Account Status is checked weekly on both accounts (account_weekly tab); any category leaving green is a hard stop for that account.",
        "",
        "Rate columns in the posts tab are formulas: =IF(reach>0, metric/reach, \"\"). They divide by Reach and nothing else.",
    ]
    for i, t in enumerate(lines, 1):
        readme.cell(row=i, column=1, value=t)
    readme.column_dimensions["A"].width = 160

    hdr_font = Font(bold=True, color="FFFFFF"); hdr_fill = PatternFill("solid", fgColor="0F1013")
    id_fill = PatternFill("solid", fgColor="E6E1D6"); rate_fill = PatternFill("solid", fgColor="FFF6CC")

    def add_sheet(title, cols, rows, id_cols_n, rate_formulas=None, validations=None):
        ws = wb.create_sheet(title)
        ws.append(cols)
        for c in range(1, len(cols) + 1):
            cell = ws.cell(row=1, column=c); cell.font = hdr_font; cell.fill = hdr_fill
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            ws.column_dimensions[get_column_letter(c)].width = max(12, min(28, len(cols[c - 1]) + 2))
        for r in rows:
            ws.append([r[c] for c in cols])
        for rr in range(2, len(rows) + 2):
            for c in range(1, id_cols_n + 1):
                ws.cell(row=rr, column=c).fill = id_fill
        if rate_formulas:
            col_idx = {c: i + 1 for i, c in enumerate(cols)}
            for target, (num, den) in rate_formulas.items():
                tc, nc, dc = col_idx[target], get_column_letter(col_idx[num]), get_column_letter(col_idx[den])
                for rr in range(2, len(rows) + 2):
                    cell = ws.cell(row=rr, column=tc)
                    cell.value = f'=IF(AND(ISNUMBER({dc}{rr}),{dc}{rr}>0,ISNUMBER({nc}{rr})),{nc}{rr}/{dc}{rr},"")'
                    cell.fill = rate_fill
        if validations:
            col_idx = {c: i + 1 for i, c in enumerate(cols)}
            for col, values in validations.items():
                dv = DataValidation(type="list", formula1='"' + ",".join(values) + '"', allow_blank=True)
                ws.add_data_validation(dv)
                L = get_column_letter(col_idx[col]); dv.add(f"{L}2:{L}{len(rows) + 1}")
        ws.freeze_panes = "B2"
        ws.auto_filter.ref = f"A1:{get_column_letter(len(cols))}{len(rows) + 1}"
        return ws

    add_sheet("posts", POST_COLS, posts, 12,
              rate_formulas={"t7_pct_nonfollower_reach": ("t7_nonfollower_reach", "t7_reach"),
                             "t7_likes_per_reach": ("t7_likes", "t7_reach"),
                             "t7_comments_per_reach": ("t7_comments", "t7_reach"),
                             "t7_sends_per_reach": ("t7_sends_shares", "t7_reach"),
                             "t7_saves_per_reach": ("t7_saves", "t7_reach"),
                             "t7_profile_visits_per_reach": ("t7_profile_visits", "t7_reach"),
                             "t14_pct_nonfollower_reach": ("t14_nonfollower_reach", "t14_reach"),
                             "t14_sends_per_reach": ("t14_sends_shares", "t14_reach"),
                             "t14_saves_per_reach": ("t14_saves", "t14_reach")},
              validations={"status": STATUS_VALUES, "originality_status": ORIGINALITY_VALUES,
                           "ai_platform_label_observed": ["Y", "N", "n/a"], "alt_text_done": ["Y", "N"], "caption_final": ["Y", "N"]})
    add_sheet("account_weekly", WEEKLY_COLS, weekly, 4,
              validations={c: ["GREEN", "NOT GREEN"] for c in ("status_features", "status_content_removals",
                                                               "status_recommendation_eligibility", "status_under_18", "status_monetization")}
              | {"all_five_green": ["Y", "N"]})
    add_sheet("stories", STORY_COLS, stories, 10,
              validations={"status": ["PLANNED", "SCHEDULED", "PUBLISHED", "LATE", "MISSED", "STORY_DATA_MISSING"],
                           "sticker": ["Y", ""], "breakout_support_used": ["Y", ""]})
    wb.save(path)


def main():
    consts = json.load(open(CONSTANTS))
    matrix = read_matrix()
    if len(matrix) != 84:
        sys.exit("matrix_84.csv does not have 84 rows — run tools/validate_matrix.py first")
    os.makedirs(OUT, exist_ok=True)
    p_csv, w_csv, s_csv = (os.path.join(OUT, n) for n in ("posts.csv", "account_weekly.csv", "stories.csv"))
    refuse_if_data_present(p_csv, "slot_id", POST_COLS)
    refuse_if_data_present(w_csv, "week", WEEKLY_COLS)
    refuse_if_data_present(s_csv, "story_id", STORY_COLS)
    posts, weekly, stories = build_rows(matrix, consts)
    write_csv(p_csv, POST_COLS, posts); write_csv(w_csv, WEEKLY_COLS, weekly); write_csv(s_csv, STORY_COLS, stories)
    write_xlsx(os.path.join(OUT, "tracking_sheet.xlsx"), posts, weekly, stories)
    ai = sum(1 for p in posts if p["ai_overlay"] == "AI"); st = sum(1 for s in stories if s["sticker"] == "Y")
    print(f"posts.csv: {len(posts)} rows ({ai} AI slots) · account_weekly.csv: {len(weekly)} rows · stories.csv: {len(stories)} rows "
          f"({st} sticker days) · tracking_sheet.xlsx written to {os.path.relpath(OUT, ROOT)}/")


if __name__ == "__main__":
    main()
