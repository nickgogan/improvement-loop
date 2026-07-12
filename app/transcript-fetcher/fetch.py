"""
Transcript Fetcher — YouTube transcript extraction for the research-loop.

Reads YouTube URLs from a queue file (or stdin), fetches transcripts via
youtube-transcript-api, and writes markdown files ready for research-loop
processing. Falls back to yt-dlp or Playwright when the primary API is IP-blocked.

Usage:
    python fetch.py                              # reads queue.md
    python fetch.py --input /path/to/Links       # reads URLs from any file
    python fetch.py --urls "URL1" "URL2"         # direct URL args
    python fetch.py --output ./transcripts       # custom output dir
    python fetch.py --backend playwright         # force Playwright backend
    python fetch.py --backend ytdlp              # force yt-dlp backend
    python fetch.py --backend browser            # browser-assisted HTML pull (persistent profile)
    python fetch.py --cookies ~/cookies.txt      # use browser cookies (yt-dlp)
    python fetch.py --probe --urls "URL1"        # metadata + token estimate only, no fetch
    python fetch.py --force --urls "URL1"        # re-fetch even if transcript exists

Backends:
    api         - youtube-transcript-api (fastest, but IP-blocked by YouTube)
    ytdlp       - yt-dlp subtitle download (needs cookies, also often blocked)
    playwright  - Playwright + system Chrome (most reliable, slower)
    browser     - Playwright persistent-profile Chrome; captures the transcript
                  panel HTML and parses it via the --from-html code path.
                  The rung for IP-level blocks (HTTP 429 / IpBlocked) that
                  defeat api/ytdlp — presents as a real, returning browser.
    auto        - try api → playwright fallback
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi

# Speech averages ~165 words/min; ~1.33 tokens/word → ~220 tokens per video-minute.
TOKENS_PER_MINUTE = 220

try:
    from html.parser import HTMLParser
except ImportError:
    pass  # stdlib, always available


def extract_video_id(url: str) -> str:
    """Extract YouTube video ID from various URL formats."""
    url = url.strip()

    if re.fullmatch(r"[\w-]{11}", url):
        return url

    parsed = urlparse(url)

    if parsed.netloc in {"youtu.be", "www.youtu.be"}:
        return parsed.path.lstrip("/").split("/")[0]

    if "youtube.com" in parsed.netloc:
        if parsed.path == "/watch":
            ids = parse_qs(parsed.query).get("v", [None])
            if ids and ids[0]:
                return ids[0]
        if parsed.path.startswith("/shorts/"):
            return parsed.path.split("/")[2]
        if parsed.path.startswith("/embed/"):
            return parsed.path.split("/")[2]

    raise ValueError(f"Could not extract video ID from: {url}")


def canonical_url(video_id: str) -> str:
    """Canonical watch URL — timestamp/playlist params stripped."""
    return f"https://www.youtube.com/watch?v={video_id}"


def ytdlp_bin() -> str | None:
    """Locate yt-dlp, preferring the Homebrew build.

    The pip-installed yt-dlp is pinned to Python 3.9 and stuck on 2025.10.14,
    which YouTube's anti-bot check rejects ("The page needs to be reloaded").
    """
    brew = Path("/opt/homebrew/bin/yt-dlp")
    if brew.exists():
        return str(brew)
    return shutil.which("yt-dlp")


def probe_video(url: str, timeout: int = 30) -> dict:
    """Fetch video metadata (no transcript) via yt-dlp.

    Returns dict with: video_id, title, channel, duration (sec),
    upload_date (YYYY-MM-DD or None), est_tokens.
    Raises RuntimeError if yt-dlp is unavailable or the probe fails.
    """
    ytdlp = ytdlp_bin()
    if not ytdlp:
        raise RuntimeError("yt-dlp not found — cannot probe metadata")

    video_id = extract_video_id(url)
    result = subprocess.run(
        [ytdlp, "-J", "--skip-download", "--no-warnings", canonical_url(video_id)],
        capture_output=True, text=True, timeout=timeout,
    )
    if result.returncode != 0:
        # Report the last stderr line — the first lines are often
        # environment warnings, not the actual error.
        err_lines = [l for l in result.stderr.strip().splitlines() if l.strip()]
        raise RuntimeError(f"yt-dlp probe failed: {err_lines[-1][:200] if err_lines else 'unknown'}")

    info = json.loads(result.stdout)
    duration = info.get("duration") or 0
    raw_date = info.get("upload_date")  # YYYYMMDD
    upload_date = (
        f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}" if raw_date else None
    )
    return {
        "video_id": video_id,
        "title": info.get("title"),
        "channel": info.get("channel") or info.get("uploader"),
        "duration": duration,
        "upload_date": upload_date,
        "est_tokens": int(duration / 60 * TOKENS_PER_MINUTE),
    }


def fetch_transcript(url: str, languages=("en",)):
    """Fetch transcript for a single YouTube URL using youtube-transcript-api."""
    video_id = extract_video_id(url)
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=list(languages))
    return {
        "video_id": video_id,
        "text": " ".join(snippet.text for snippet in transcript),
        "segments": [
            {
                "text": snippet.text,
                "start": snippet.start,
                "duration": snippet.duration,
            }
            for snippet in transcript
        ],
    }


def _parse_vtt_time(ts: str) -> float:
    """Convert VTT timestamp (HH:MM:SS.mmm) to seconds."""
    parts = ts.split(":")
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h = "0"
        m, s = parts
    else:
        return 0.0
    return int(h) * 3600 + int(m) * 60 + float(s)


def _parse_vtt(vtt_text: str) -> list[dict]:
    """Parse VTT subtitle content into segments."""
    segments = []
    lines = vtt_text.strip().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Look for timestamp lines: "00:00:01.000 --> 00:00:04.000"
        if "-->" in line:
            times = line.split("-->")
            start = _parse_vtt_time(times[0].strip().split()[0])
            # Collect text lines until blank line or next timestamp
            text_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() and "-->" not in lines[i]:
                text_lines.append(lines[i].strip())
                i += 1
            text = " ".join(text_lines)
            # Strip VTT tags like <c> </c>
            text = re.sub(r"<[^>]+>", "", text)
            if text:
                segments.append({"text": text, "start": start, "duration": 0.0})
        else:
            i += 1
    # Deduplicate consecutive identical segments (common in auto-subs)
    deduped = []
    for seg in segments:
        if not deduped or seg["text"] != deduped[-1]["text"]:
            deduped.append(seg)
    return deduped


def fetch_transcript_ytdlp(url: str, languages=("en",), cookies=None, cookies_from_browser=None):
    """Fetch transcript using yt-dlp as backend."""
    video_id = extract_video_id(url)

    with tempfile.TemporaryDirectory() as tmpdir:
        out_template = str(Path(tmpdir) / "%(id)s")
        cmd = [
            ytdlp_bin() or "yt-dlp",
            "--write-auto-sub",
            "--sub-lang", ",".join(languages),
            "--skip-download",
            "--sub-format", "vtt",
            "-o", out_template,
            url,
        ]
        if cookies_from_browser:
            cmd.extend(["--cookies-from-browser", cookies_from_browser])
        elif cookies:
            cmd.extend(["--cookies", str(cookies)])

        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=60
        )

        if result.returncode != 0:
            raise RuntimeError(
                f"yt-dlp failed (exit {result.returncode}): {result.stderr.strip()}"
            )

        # Find the subtitle file — yt-dlp names it <id>.<lang>.vtt
        vtt_files = list(Path(tmpdir).glob("*.vtt"))
        if not vtt_files:
            raise RuntimeError(
                f"yt-dlp produced no subtitle files. stdout: {result.stdout.strip()}"
            )

        vtt_text = vtt_files[0].read_text(encoding="utf-8")
        segments = _parse_vtt(vtt_text)

        return {
            "video_id": video_id,
            "text": " ".join(seg["text"] for seg in segments),
            "segments": segments,
        }


def _parse_yt_timestamp(ts: str) -> float:
    """Convert YouTube transcript timestamp (e.g., '1:23' or '1:02:03') to seconds."""
    parts = ts.strip().split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    elif len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    return 0.0


def parse_transcript_html(html: str, video_id: str = "unknown") -> dict:
    """Parse YouTube transcript panel HTML into the standard transcript dict.

    Handles two YouTube DOM formats:
      - Old: <ytd-transcript-segment-renderer> with .segment-timestamp / .segment-text
      - New: <transcript-segment-view-model> with .ytwTranscriptSegmentViewModelTimestamp
             and <span class="ytAttributedStringHost ...">

    Args:
        html: Raw HTML string (from the transcript engagement panel or full page).
        video_id: YouTube video ID to embed in the result.

    Returns:
        Dict with keys: video_id, text, segments (same shape as fetch_transcript).
    """
    segments = []

    # --- Strategy 1: new DOM (transcript-segment-view-model) ---
    # Timestamp lives in a div with class containing "Timestamp", text in a sibling span.
    new_ts_pattern = re.compile(
        r'class="ytwTranscriptSegmentViewModelTimestamp[^"]*"[^>]*>'
        r'\s*([0-9]+:[0-9:]+)\s*</div>',
        re.DOTALL,
    )
    new_text_pattern = re.compile(
        r'class="ytAttributedStringHost[^"]*"[^>]*role="text"[^>]*>'
        r'\s*(.*?)\s*</span>',
        re.DOTALL,
    )

    ts_matches = list(new_ts_pattern.finditer(html))
    text_matches = list(new_text_pattern.finditer(html))

    if ts_matches and text_matches and len(ts_matches) == len(text_matches):
        for ts_m, txt_m in zip(ts_matches, text_matches):
            timestamp_str = ts_m.group(1).strip()
            raw_text = txt_m.group(1).strip()
            # Strip any residual HTML tags
            clean_text = re.sub(r"<[^>]+>", "", raw_text).strip()
            if clean_text:
                segments.append({
                    "text": clean_text,
                    "start": _parse_yt_timestamp(timestamp_str),
                    "duration": 0.0,
                })

    # --- Strategy 2: old DOM (ytd-transcript-segment-renderer) ---
    if not segments:
        old_ts_pattern = re.compile(
            r'class="segment-timestamp[^"]*"[^>]*>\s*([0-9]+:[0-9:]+)\s*<',
            re.DOTALL,
        )
        old_text_pattern = re.compile(
            r'class="segment-text[^"]*"[^>]*>\s*(.*?)\s*</',
            re.DOTALL,
        )
        ts_matches = list(old_ts_pattern.finditer(html))
        text_matches = list(old_text_pattern.finditer(html))

        if ts_matches and text_matches:
            for ts_m, txt_m in zip(ts_matches, text_matches):
                timestamp_str = ts_m.group(1).strip()
                raw_text = txt_m.group(1).strip()
                clean_text = re.sub(r"<[^>]+>", "", raw_text).strip()
                if clean_text:
                    segments.append({
                        "text": clean_text,
                        "start": _parse_yt_timestamp(timestamp_str),
                        "duration": 0.0,
                    })

    if not segments:
        raise RuntimeError(
            "Could not extract transcript segments from HTML. "
            "Neither new (transcript-segment-view-model) nor old "
            "(ytd-transcript-segment-renderer) DOM format found."
        )

    return {
        "video_id": video_id,
        "text": " ".join(seg["text"] for seg in segments),
        "segments": segments,
    }


def fetch_transcript_playwright(url: str, pw_browser=None):
    """Fetch transcript using Playwright with system Chrome.

    If pw_browser is provided, reuses it (for batch efficiency).
    Otherwise launches and closes its own browser.
    """
    from playwright.sync_api import sync_playwright

    video_id = extract_video_id(url)
    own_browser = pw_browser is None

    pw_context = None
    if own_browser:
        pw_context = sync_playwright().start()
        pw_browser = pw_context.chromium.launch(
            channel="chrome",
            headless=False,
            args=[
                "--window-position=-2000,-2000",
                "--disable-blink-features=AutomationControlled",
            ],
        )

    try:
        ctx = pw_browser.new_context(viewport={"width": 1280, "height": 900})
        page = ctx.new_page()
        page.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
        )

        page.goto(url, wait_until="networkidle", timeout=30000)

        # Dismiss cookie consent
        try:
            page.locator('button:has-text("Accept all")').first.click(timeout=3000)
            page.wait_for_timeout(2000)
        except Exception:
            pass

        page.wait_for_timeout(2000)
        page.evaluate("window.scrollBy(0, 400)")
        page.wait_for_timeout(1000)

        # Expand description
        try:
            page.locator("tp-yt-paper-button#expand").first.click(timeout=5000)
        except Exception:
            pass
        page.wait_for_timeout(1000)

        # Click Show transcript
        page.evaluate(
            'document.querySelector("button[aria-label=\\"Show transcript\\"]")?.click()'
        )
        page.wait_for_timeout(3000)

        # Click Transcript tab (if chapters tab is shown first)
        page.evaluate(
            """() => {
            const panel = document.querySelector(
                'ytd-engagement-panel-section-list-renderer[target-id="engagement-panel-searchable-transcript"]'
            );
            if (panel) {
                const btns = panel.querySelectorAll('button');
                for (const b of btns) {
                    if (b.textContent.trim() === 'Transcript') b.click();
                }
            }
        }"""
        )
        page.wait_for_timeout(5000)

        # Extract all segments
        result = page.evaluate(
            """() => {
            const segs = document.querySelectorAll('ytd-transcript-segment-renderer');
            return [...segs].map(s => ({
                t: s.querySelector('.segment-timestamp')?.textContent?.trim() || '0:00',
                s: s.querySelector('.segment-text')?.textContent?.trim() || ''
            }));
        }"""
        )

        ctx.close()

        if not result:
            raise RuntimeError(f"No transcript segments found for {video_id}")

        segments = [
            {
                "text": seg["s"],
                "start": _parse_yt_timestamp(seg["t"]),
                "duration": 0.0,
            }
            for seg in result
            if seg["s"]
        ]

        return {
            "video_id": video_id,
            "text": " ".join(seg["text"] for seg in segments),
            "segments": segments,
        }
    finally:
        if own_browser:
            pw_browser.close()
            if pw_context:
                pw_context.stop()


def launch_browser_context(pw):
    """Launch a persistent-profile Chrome context for the 'browser' backend.

    The persistent user-data-dir (gitignored under .playwright/) makes the
    session present as a real, returning browser — cookies, storage, and
    fingerprint persist across runs, unlike the throwaway contexts the
    'playwright' backend uses.
    """
    profile_dir = Path(__file__).parent / ".playwright" / "chrome-profile"
    profile_dir.mkdir(parents=True, exist_ok=True)
    return pw.chromium.launch_persistent_context(
        str(profile_dir),
        channel="chrome",
        headless=False,
        viewport={"width": 1280, "height": 900},
        args=[
            "--window-position=-2000,-2000",
            "--disable-blink-features=AutomationControlled",
        ],
    )


def fetch_transcript_browser(url: str, pw_ctx=None):
    """Browser-assisted HTML pull: drive a real Chrome session via Playwright,
    open the transcript panel, capture its HTML, and parse it through
    parse_transcript_html — the same code path as --from-html.

    Distinct from fetch_transcript_playwright in two ways: (1) persistent
    profile context (real-browser presentation, for IP-level 429/IpBlocked
    situations), and (2) HTML-capture-then-parse, so both old and new YouTube
    DOM formats are handled. On parse failure the captured HTML is saved under
    .playwright/html/ for manual inspection or --from-html retry.

    If pw_ctx (a persistent BrowserContext) is provided, reuses it for batch
    efficiency. Otherwise launches and closes its own.
    """
    from playwright.sync_api import sync_playwright

    video_id = extract_video_id(url)
    own_ctx = pw_ctx is None

    pw = None
    if own_ctx:
        pw = sync_playwright().start()
        pw_ctx = launch_browser_context(pw)

    try:
        page = pw_ctx.new_page()
        page.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
        )
        try:
            page.goto(canonical_url(video_id), wait_until="networkidle", timeout=30000)

            # Dismiss cookie consent
            try:
                page.locator('button:has-text("Accept all")').first.click(timeout=3000)
                page.wait_for_timeout(2000)
            except Exception:
                pass

            page.wait_for_timeout(2000)
            page.evaluate("window.scrollBy(0, 400)")
            page.wait_for_timeout(1000)

            # Expand description
            try:
                page.locator("tp-yt-paper-button#expand").first.click(timeout=5000)
            except Exception:
                pass
            page.wait_for_timeout(1000)

            # Click Show transcript
            page.evaluate(
                'document.querySelector("button[aria-label=\\"Show transcript\\"]")?.click()'
            )
            page.wait_for_timeout(5000)

            # Capture the transcript panel HTML (fall back to the full page)
            html = page.evaluate(
                """() => {
                const panel = document.querySelector(
                    'ytd-engagement-panel-section-list-renderer[target-id="engagement-panel-searchable-transcript"]'
                );
                return panel ? panel.outerHTML : document.documentElement.outerHTML;
            }"""
            )
        finally:
            page.close()

        try:
            return parse_transcript_html(html, video_id=video_id)
        except RuntimeError:
            # Save the captured HTML for manual inspection / --from-html retry
            html_dir = Path(__file__).parent / ".playwright" / "html"
            html_dir.mkdir(parents=True, exist_ok=True)
            html_path = html_dir / f"{video_id}.html"
            html_path.write_text(html, encoding="utf-8")
            raise RuntimeError(
                f"Browser pull got no transcript segments for {video_id}; "
                f"captured HTML saved to {html_path}"
            )
    finally:
        if own_ctx:
            pw_ctx.close()
            if pw:
                pw.stop()


def format_timestamp(seconds: float) -> str:
    """Convert seconds to HH:MM:SS format."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def write_transcript_markdown(result: dict, output_dir: Path, meta: dict = None):
    """Write a single transcript result as a markdown file.

    If meta (from probe_video) is provided, the header is enriched with
    title, channel, duration, and upload date — upload date feeds the
    research-loop's recency weighting.
    """
    video_id = result["video_id"]
    slug = video_id
    filepath = output_dir / f"{slug}.md"

    title = (meta or {}).get("title") or video_id
    lines = [
        f"# Transcript: {title}",
        "",
        f"**URL:** {canonical_url(video_id)}",
        f"**Segments:** {len(result['segments'])}",
    ]
    if meta:
        if meta.get("channel"):
            lines.append(f"**Channel:** {meta['channel']}")
        if meta.get("duration"):
            lines.append(f"**Duration:** {format_timestamp(meta['duration'])}")
        if meta.get("upload_date"):
            lines.append(f"**Uploaded:** {meta['upload_date']}")
    lines += [
        "",
        "---",
        "",
        "## Full Text",
        "",
        result["text"],
        "",
        "---",
        "",
        "## Timestamped Segments",
        "",
    ]

    for seg in result["segments"]:
        ts = format_timestamp(seg["start"])
        lines.append(f"**[{ts}]** {seg['text']}")
        lines.append("")

    filepath.write_text("\n".join(lines), encoding="utf-8")
    return filepath


def read_urls_from_file(filepath: Path) -> list[str]:
    """Read URLs from a file, one per line. Skips blank lines and comments."""
    urls = []
    for line in filepath.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Handle lines that might have other content — extract URLs
        if "youtube.com" in line or "youtu.be" in line:
            # Extract URL if line contains other text
            match = re.search(r"https?://[^\s]+", line)
            if match:
                urls.append(match.group(0))
            else:
                urls.append(line)
    return urls


def main():
    parser = argparse.ArgumentParser(
        description="Fetch YouTube transcripts for research-loop processing"
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=None,
        help="File containing YouTube URLs (default: queue.md in script dir)",
    )
    parser.add_argument(
        "--urls",
        nargs="+",
        help="YouTube URLs to process directly",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output directory for transcript files (default: transcripts/ in script dir)",
    )
    parser.add_argument(
        "--languages",
        nargs="+",
        default=["en"],
        help="Language preferences for transcripts (default: en)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Also write a combined JSON results file",
    )
    parser.add_argument(
        "--backend",
        choices=["api", "ytdlp", "playwright", "browser", "auto"],
        default="auto",
        help="Backend: 'api' (youtube-transcript-api), 'ytdlp' (yt-dlp), "
        "'playwright' (browser scrape), 'browser' (persistent-profile Chrome "
        "HTML pull — for IP-level 429 blocks), 'auto' (try api, fall back to playwright)",
    )
    parser.add_argument(
        "--cookies",
        type=Path,
        default=None,
        help="Path to cookies.txt file for yt-dlp (Netscape format)",
    )
    parser.add_argument(
        "--cookies-from-browser",
        default=None,
        help="Browser to extract cookies from for yt-dlp (e.g., 'chrome', 'firefox', 'brave')",
    )
    parser.add_argument(
        "--from-html",
        type=Path,
        default=None,
        help="Parse transcript from saved YouTube HTML file instead of fetching. "
        "Video ID is inferred from the filename unless --video-id is given.",
    )
    parser.add_argument(
        "--video-id",
        default=None,
        help="Video ID to use when parsing from HTML (used for output filename)",
    )
    parser.add_argument(
        "--probe",
        action="store_true",
        help="Probe metadata only (title, duration, upload date, token estimate) — no transcript fetch",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-fetch transcripts even if a transcript file already exists",
    )

    args = parser.parse_args()

    script_dir = Path(__file__).parent

    # Handle --from-html mode: parse saved HTML instead of fetching
    if args.from_html:
        if not args.from_html.exists():
            print(f"HTML file not found: {args.from_html}")
            sys.exit(1)
        vid = args.video_id or args.from_html.stem
        html_content = args.from_html.read_text(encoding="utf-8")
        output_dir = args.output or script_dir / "transcripts"
        output_dir.mkdir(parents=True, exist_ok=True)
        try:
            data = parse_transcript_html(html_content, video_id=vid)
            filepath = write_transcript_markdown(data, output_dir)
            print(
                f"Parsed {len(data['segments'])} segments from HTML → {filepath.name}"
            )
        except Exception as exc:
            print(f"FAILED to parse HTML: {exc}")
            sys.exit(1)
        sys.exit(0)

    # Determine URLs to process
    if args.urls:
        urls = args.urls
    elif args.input:
        urls = read_urls_from_file(args.input)
    else:
        queue_file = script_dir / "queue.md"
        if queue_file.exists():
            urls = read_urls_from_file(queue_file)
        else:
            print("No URLs provided. Use --urls, --input, or create queue.md")
            sys.exit(1)

    if not urls:
        print("No YouTube URLs found in input.")
        sys.exit(1)

    # Determine output directory
    output_dir = args.output or script_dir / "transcripts"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Dedup within the batch by video ID (strips timestamp/playlist params)
    seen_ids = set()
    deduped_urls = []
    for url in urls:
        try:
            vid = extract_video_id(url)
        except ValueError:
            deduped_urls.append(url)  # let the fetch loop report the bad URL
            continue
        if vid in seen_ids:
            print(f"Skipping duplicate in batch: {url} ({vid})")
            continue
        seen_ids.add(vid)
        deduped_urls.append(url)
    urls = deduped_urls

    # Probe mode: metadata + token estimates only, no transcript fetch
    if args.probe:
        print(f"Probing {len(urls)} videos...\n")
        total_tokens = 0
        total_duration = 0
        rows = []
        for url in urls:
            try:
                meta = probe_video(url)
                have = (output_dir / f"{meta['video_id']}.md").exists()
                total_tokens += meta["est_tokens"]
                total_duration += meta["duration"]
                rows.append(meta | {"fetched": have})
                print(
                    f"  {meta['video_id']}  {format_timestamp(meta['duration']):>8}  "
                    f"~{meta['est_tokens']:>6,} tok  {meta['upload_date'] or '????-??-??'}  "
                    f"{'[fetched]' if have else '[new]':>9}  {meta['title']}"
                )
            except Exception as exc:
                rows.append({"url": url, "error": str(exc)})
                print(f"  PROBE FAILED: {url}: {exc}")
        print(
            f"\nTotal: {len(urls)} videos, {format_timestamp(total_duration)} runtime, "
            f"~{total_tokens:,} estimated transcript tokens"
        )
        if args.json:
            json_path = output_dir / "probe.json"
            json_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
            print(f"JSON results: {json_path}")
        sys.exit(0)

    print(f"Processing {len(urls)} URLs...")
    print(f"Output: {output_dir}")
    print()

    results = []
    succeeded = 0
    failed = 0
    backend = args.backend

    # For playwright/browser backends, launch browser once and reuse across URLs
    pw_context = None
    pw_browser = None
    pw_persistent = None
    if backend == "browser":
        try:
            from playwright.sync_api import sync_playwright

            pw_context = sync_playwright().start()
            pw_persistent = launch_browser_context(pw_context)
            print("Persistent-profile Chrome launched (reusing for all URLs)")
        except Exception as pw_init_exc:
            print(f"Browser backend init failed: {pw_init_exc}")
            sys.exit(1)
    elif backend in ("playwright", "auto"):
        try:
            from playwright.sync_api import sync_playwright

            pw_context = sync_playwright().start()
            pw_browser = pw_context.chromium.launch(
                channel="chrome",
                headless=False,
                args=[
                    "--window-position=-2000,-2000",
                    "--disable-blink-features=AutomationControlled",
                ],
            )
            print(f"Playwright browser launched (reusing for all URLs)")
        except Exception as pw_init_exc:
            print(f"Playwright init failed: {pw_init_exc}")
            if backend == "playwright":
                sys.exit(1)

    try:
        for i, url in enumerate(urls, 1):
            try:
                video_id = extract_video_id(url)

                existing = output_dir / f"{video_id}.md"
                if existing.exists() and not args.force:
                    print(
                        f"[{i}/{len(urls)}] {video_id} already fetched → {existing.name} "
                        "(use --force to re-fetch)"
                    )
                    results.append(
                        {"url": url, "ok": True, "backend": "cached",
                         "video_id": video_id, "skipped": True}
                    )
                    succeeded += 1
                    continue

                print(f"[{i}/{len(urls)}] Fetching {video_id}...", end=" ")

                data = None
                used_backend = None

                if backend in ("api", "auto"):
                    try:
                        data = fetch_transcript(url, languages=tuple(args.languages))
                        used_backend = "api"
                    except Exception as api_exc:
                        if backend == "api":
                            raise
                        print(
                            f"api failed ({type(api_exc).__name__}), trying playwright...",
                            end=" ",
                        )

                if data is None and backend in ("playwright", "auto") and pw_browser:
                    data = fetch_transcript_playwright(url, pw_browser=pw_browser)
                    used_backend = "playwright"

                if data is None and backend == "browser":
                    data = fetch_transcript_browser(url, pw_ctx=pw_persistent)
                    used_backend = "browser"

                if data is None and backend in ("ytdlp",):
                    data = fetch_transcript_ytdlp(
                        url,
                        languages=tuple(args.languages),
                        cookies=args.cookies,
                        cookies_from_browser=args.cookies_from_browser,
                    )
                    used_backend = "ytdlp"

                # Best-effort metadata enrichment (title/duration/upload date)
                meta = None
                try:
                    meta = probe_video(url)
                except Exception:
                    pass

                filepath = write_transcript_markdown(data, output_dir, meta=meta)
                print(
                    f"OK via {used_backend} ({len(data['segments'])} segments) → {filepath.name}"
                )
                results.append(
                    {"url": url, "ok": True, "backend": used_backend, **data}
                )
                succeeded += 1
            except Exception as exc:
                print(f"FAILED: {exc}")
                results.append({"url": url, "ok": False, "error": str(exc)})
                failed += 1
    finally:
        if pw_browser:
            pw_browser.close()
        if pw_persistent:
            pw_persistent.close()
        if pw_context:
            pw_context.stop()

    # Summary
    print()
    print(f"Done: {succeeded} succeeded, {failed} failed out of {len(urls)} total")

    if failed > 0:
        print("\nFailed URLs:")
        for r in results:
            if not r["ok"]:
                print(f"  - {r['url']}: {r['error']}")

    # Optional JSON output
    if args.json:
        json_path = output_dir / "results.json"
        # Strip full text from JSON to keep it manageable
        json_results = []
        for r in results:
            entry = {k: v for k, v in r.items() if k != "segments"}
            if r.get("ok") and "segments" in r:
                entry["segment_count"] = len(r["segments"])
            json_results.append(entry)
        json_path.write_text(
            json.dumps(json_results, indent=2), encoding="utf-8"
        )
        print(f"\nJSON results: {json_path}")


if __name__ == "__main__":
    main()
