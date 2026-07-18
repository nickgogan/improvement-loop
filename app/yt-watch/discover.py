#!/usr/bin/env python3
"""yt-watch v0 — watch-history discovery pass for /watch-youtube (IB-179).

Deterministic core only: fetch Nick's YouTube watch history via yt-dlp's
InnerTube path (:ythistory, Chrome cookies, read-only), dedup candidate video
IDs against the live corpus, and emit a compact candidate table. Relevance
judgment is model-side (the orchestrating skill), not code-side.

Raw history lands in state/ (gitignored — personal data). The high-water
watermark also lives there once the full skill ships.

Usage:
  discover.py --fetch N          # fetch newest N history entries -> state/history.json + TSV to stdout
  discover.py --dedup            # mark history entries already known to the corpus
  discover.py --fetch N --dedup  # both
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

TOOL_DIR = Path(__file__).resolve().parent
ENGINE_DIR = TOOL_DIR.parent.parent  # systems/improvement-loop/
STATE = TOOL_DIR / "state"
HISTORY_JSON = STATE / "history.json"
YTDLP = "/opt/homebrew/bin/yt-dlp"

LINKS_MD = ENGINE_DIR / "LINKS.md"
SOURCES_DIR = ENGINE_DIR / "research-sources"
TRANSCRIPTS_DIR = ENGINE_DIR / "app" / "transcript-fetcher" / "transcripts"

VIDEO_ID_RE = re.compile(r"(?:v=|youtu\.be/|/shorts/)([A-Za-z0-9_-]{11})")


def fetch_history(n: int) -> list[dict]:
    """One yt-dlp invocation; continuations handled internally by yt-dlp."""
    cmd = [
        YTDLP, "--cookies-from-browser", "chrome",
        "--flat-playlist", "--playlist-items", f"1:{n}",
        "--dump-json", ":ythistory",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    entries = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        entries.append({
            "position": e.get("playlist_index"),
            "id": e.get("id"),
            "title": e.get("title"),
            "duration": e.get("duration"),
            "duration_string": e.get("duration_string"),
            "channel": e.get("channel") or e.get("uploader"),  # null in flat mode; probe fills later
        })
    if not entries:
        sys.stderr.write(proc.stderr[-2000:] + "\n")
        raise SystemExit("history fetch returned no entries (cookies stale? yt-dlp drift?)")
    STATE.mkdir(exist_ok=True)
    HISTORY_JSON.write_text(json.dumps(entries, indent=1))
    return entries


def known_ids() -> dict[str, str]:
    """video_id -> evidence, from the live corpus: LINKS.md, research-sources URLs, transcript cache."""
    known: dict[str, str] = {}
    if TRANSCRIPTS_DIR.is_dir():
        for f in TRANSCRIPTS_DIR.glob("*.md"):
            known.setdefault(f.stem, f"transcript:{f.name}")
    if SOURCES_DIR.is_dir():
        for f in SOURCES_DIR.glob("*.md"):
            for vid in VIDEO_ID_RE.findall(f.read_text(errors="ignore")):
                known.setdefault(vid, f"source:{f.name}")
    if LINKS_MD.is_file():
        for vid in VIDEO_ID_RE.findall(LINKS_MD.read_text(errors="ignore")):
            known.setdefault(vid, "links.md")
    return known


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", type=int, metavar="N")
    ap.add_argument("--dedup", action="store_true")
    args = ap.parse_args()
    if not args.fetch and not args.dedup:
        ap.error("nothing to do")

    if args.fetch:
        entries = fetch_history(args.fetch)
    else:
        entries = json.loads(HISTORY_JSON.read_text())

    corpus = known_ids() if args.dedup else {}
    for e in entries:
        mark = corpus.get(e["id"], "") if args.dedup else ""
        print(f"{e['position']}\t{e['id']}\t{e['duration_string'] or '?'}\t{mark}\t{e['title']}")
    sys.stderr.write(f"{len(entries)} entries\n")


if __name__ == "__main__":
    main()
