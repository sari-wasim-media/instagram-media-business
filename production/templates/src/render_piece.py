#!/usr/bin/env python3
"""Render a PRODUCTION piece (feed static, carousel, Reel or Story) in House System v1.

Usage (from the repository root):

    python3 production/templates/src/render_piece.py SPEC.json [--out DIR]

SPEC.json describes one piece:

    {
      "piece_id": "A-2026xx-C1-REEL-01",          # any stable id; used for file names
      "account": "A" | "B",                        # sets the real handle in the top band
      "engine": "C1" | "C2" | "C3" | "C4" | "ST",  # sets the accent
      "format": "REEL" | "CARO" | "STAT" | "STORY",
      "band_left": "RELEASE DESK",                 # optional; defaults to the engine label
      "frames": [
        { "name": "01_hook", "surface": "ink" | "paper", "body": "<div class='content'>…</div>",
          "band_right": "…", "counter": "1/6", "duration": 3.0 }      # duration: Reels only
      ]
    }

Bodies use the house classes in production/house-style/house.css. Any element with class "in" enters with
the house 120 ms slide-up; give it style="--d:0.4s" to delay it inside its beat. Feed frames are 1080 × 1350,
Reels and Stories 1080 × 1920. Carousels, statics and Stories are written as PNGs; Reels additionally as an
H.264 MP4 (1080 × 1920, 30 fps, yuv420p, no audio — the track is added at upload from the platform's
royalty-free library).

Production frames carry no specimen tag and carry the real account handle. Output defaults to
_local/exports/<piece_id>/ (gitignored): finished media is delivered to the founders, never committed.
This is a local production aid (DECISIONS.md, Agile Revival delegated decisions): it reads and writes files
only, and never publishes, schedules or contacts any platform.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
CSS = os.path.join(ROOT, "production", "house-style", "house.css")
DRIVER = os.path.join(HERE, "render_driver.js")
HANDLES = {"A": "@thestreetwearofficial", "B": "@sneakerbong"}
ENGINE_LABEL = {"C1": "Release Desk", "C2": "Rankings", "C3": "Market Desk", "C4": "Commentary", "ST": "Story"}
FPS = 30
ANIM_CSS = """
.in { animation: rise .12s cubic-bezier(.2,.7,.2,1) both; animation-delay: var(--d, 0s); }
.pop { animation: pop .15s cubic-bezier(.2,.7,.2,1) both; animation-delay: var(--d, 0s); }
.draw { stroke-dasharray: var(--len, 3000); animation: draw var(--dur, 3s) linear both; animation-delay: var(--d, 0s); }
@keyframes rise { from { transform: translateY(40px); opacity: 0; } to { transform: none; opacity: 1; } }
@keyframes pop { from { transform: scale(1.15) rotate(-6deg); opacity: 0; } to { transform: rotate(-6deg); opacity: 1; } }
@keyframes draw { from { stroke-dashoffset: var(--len, 3000); } to { stroke-dashoffset: 0; } }
"""


def page(spec, fr, tall):
    eng = spec["engine"]
    left = fr.get("band_left", spec.get("band_left", ENGINE_LABEL[eng]))
    h = 1920 if tall else 1350
    cls = f"frame {fr.get('surface', 'ink')}{' tall' if tall else ''}{' story' if spec['format'] == 'STORY' else ''}"
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{spec['piece_id']} {fr['name']}</title>
<link rel="stylesheet" href="file://{CSS}">
<style>html,body{{width:1080px;height:{h}px;overflow:hidden}}{ANIM_CSS}{spec.get('css', '')}{fr.get('css', '')}</style></head>
<body><div class="{cls}" data-engine="{eng}" id="frame">
  <div class="band-top"><div class="engine">{left}</div><div>{HANDLES[spec['account']]}</div></div>
  {fr['body']}
  <div class="band-bottom"><div>{fr.get('band_right', '')}</div><div>{fr.get('counter', '')}</div></div>
</div></body></html>"""


def anim_end(fr):
    """Seconds until the last entry animation of a beat has finished (delays parsed from --d / --dur)."""
    import re
    body = fr["body"]
    ends = [0.0]
    for m in re.finditer(r"--d:\s*([0-9.]+)s", body):
        ends.append(float(m.group(1)) + 0.15)
    for m in re.finditer(r"--dur:\s*([0-9.]+)s", body):
        ends.append(float(m.group(1)) + 0.05)
    if re.search(r'class="[^"]*\b(in|pop)\b', body) or re.search(r"class='[^']*\b(in|pop)\b", body):
        ends.append(0.15)
    return max(ends)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    spec = json.load(open(a.spec, encoding="utf-8"))
    fmt = spec["format"]
    tall = fmt in ("REEL", "STORY")
    out = a.out or os.path.join(ROOT, "_local", "exports", spec["piece_id"])
    os.makedirs(out, exist_ok=True)
    work = tempfile.mkdtemp(prefix="render_")
    job = {"frames": []}
    plan = []   # (frame, [(png, hold_seconds)])
    for fr in spec["frames"]:
        hpath = os.path.join(work, f"{fr['name']}.html")
        with open(hpath, "w", encoding="utf-8") as fh:
            fh.write(page(spec, fr, tall))
        final_png = os.path.join(out, f"{spec['piece_id']}__{fr['name']}.png")
        shots = []
        seq = []
        if fmt == "REEL":
            end = anim_end(fr)
            n = int(round(end * FPS))
            for i in range(n):
                p = os.path.join(work, f"{fr['name']}__{i:03d}.png")
                shots.append({"t": i / FPS, "png": p})
                seq.append((p, 1.0 / FPS))
            hold = float(fr["duration"]) - n / FPS
            if hold <= 0:
                sys.exit(f"{fr['name']}: duration {fr['duration']} shorter than its entry animation ({end:.2f}s)")
            seq.append((final_png, hold))
        shots.append({"t": 60.0, "png": final_png})   # end state, all animations complete
        job["frames"].append({"html": hpath, "width": 1080, "height": 1920 if tall else 1350, "shots": shots})
        plan.append((fr, seq))
    jpath = os.path.join(work, "job.json")
    json.dump(job, open(jpath, "w"))
    env = dict(os.environ, NODE_PATH=os.environ.get("NODE_PATH", "/opt/node22/lib/node_modules"))
    subprocess.run(["node", DRIVER, jpath], check=True, env=env)
    print(f"{len(spec['frames'])} frame(s) → {os.path.relpath(out, ROOT)}")
    if fmt == "REEL":
        lst = os.path.join(work, "concat.txt")
        total = 0.0
        with open(lst, "w") as fh:
            last = None
            for fr, seq in plan:
                for png, dur in seq:
                    fh.write(f"file '{png}'\nduration {dur:.4f}\n")
                    total += dur
                    last = png
            fh.write(f"file '{last}'\n")   # concat demuxer: the last entry needs repeating
        mp4 = os.path.join(out, f"{spec['piece_id']}.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                        "-vf", f"fps={FPS},format=yuv420p", "-c:v", "libx264", "-preset", "slow", "-crf", "18",
                        "-r", str(FPS), "-movflags", "+faststart", mp4], check=True)
        print(f"Reel → {os.path.relpath(mp4, ROOT)} ({total:.1f} s)")
    shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
