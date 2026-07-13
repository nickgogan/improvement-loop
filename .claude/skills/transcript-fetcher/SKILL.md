---
name: transcript-fetcher
description: >-
  Fetch YouTube video transcripts as full-text markdown files for research-loop
  Pass 2 deep extraction. Wraps the Python transcript fetcher tool. Use when the
  research-loop needs full transcript text for a high-value video source, or when
  the user provides YouTube URLs and wants transcripts fetched.
user-invocable: true
allowed-tools: Bash Read Write
argument-hint: "<url1> [url2] [url3] ..."
---

# Transcript Fetcher

Fetch YouTube video transcripts and save them as full-text markdown files for downstream research-loop processing.

## When to Use This Skill

- The research-loop needs a transcript for Pass 2 deep extraction
- The user provides YouTube URLs and wants transcripts fetched
- Batch fetching transcripts for multiple videos before a research session

## Prerequisites

The Python tool requires `youtube-transcript-api`. If not installed:

```bash
pip install youtube-transcript-api
```

The `browser` fallback backend (step 4 in the chain) additionally requires Playwright
plus **Google Chrome** (the backend launches `channel="chrome"` — bundled Chromium does
not satisfy it). If missing:

```bash
pip install playwright && playwright install chrome
```

## Tool Location

The fetcher script lives at:
```
systems/improvement-loop/app/transcript-fetcher/fetch.py
```

Transcripts are saved to:
```
systems/improvement-loop/app/transcript-fetcher/transcripts/
```

Each transcript is named by video ID (e.g., `5ztI_dbj6ek.md`).

## Procedure

### Step 0: Probe the Batch (recommended for 2+ URLs)

Before fetching, probe metadata to size the batch — duration, upload date, and an
estimated transcript token cost per video:

```bash
python systems/improvement-loop/app/transcript-fetcher/fetch.py --probe --urls "URL1" "URL2"
```

Output includes per-video `[fetched]`/`[new]` status and a batch total (runtime +
estimated tokens). When invoked from the research-loop's batch gate, this output is
what gets presented to the user to decide how many videos to process. Add `--json`
to also write `transcripts/probe.json` for programmatic use.

### Step 1: Deduplication (automatic)

The tool deduplicates for you:

- **URL normalization** — video IDs are extracted via URL parsing, so timestamp
  (`&t=520s`) and playlist params never produce duplicates. Transcript files always
  record the canonical `watch?v=ID` URL.
- **In-batch dedup** — the same video ID appearing twice in one batch is fetched once.
- **Already-fetched skip** — videos with an existing `transcripts/<id>.md` are skipped
  and reported as cached. Pass `--force` to re-fetch.

No manual `ls` check is needed, though you can still list
`systems/improvement-loop/app/transcript-fetcher/transcripts/` to see what exists.

### Step 2: Fetch Transcripts

Use `Bash` to run the fetcher:

```bash
# Single URL
python systems/improvement-loop/app/transcript-fetcher/fetch.py --urls "https://www.youtube.com/watch?v=VIDEO_ID"

# Multiple URLs
python systems/improvement-loop/app/transcript-fetcher/fetch.py --urls "URL1" "URL2" "URL3"

# From a file containing URLs (one per line)
python systems/improvement-loop/app/transcript-fetcher/fetch.py --input /path/to/urls.txt
```

The tool accepts various YouTube URL formats:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`
- Raw video IDs (11 characters)

### Step 3: Verify Output

After fetching, verify the transcript files were created:

```bash
ls -la systems/improvement-loop/app/transcript-fetcher/transcripts/
```

Each transcript file contains:
- A metadata header (title, channel, duration, upload date, segment count)
- Full concatenated text

### Step 3b: Fallback Chain

Transcripts must always be obtained if possible. Work down this chain in order —
each step only when the previous one failed:

1. **`api` backend** — youtube-transcript-api (fastest; often IP-blocked). Default `--backend auto` tries this first.
2. **`playwright` backend** — automated browser pull; `--backend auto` falls back to this automatically, or force with `--backend playwright`
3. **`ytdlp` backend** — subtitle download via `--backend ytdlp` (prefers the Homebrew yt-dlp build; the pip 3.9 build is stale and rejected by YouTube)
4. **`browser` backend — Playwright browser-assisted HTML pull** — for IP-level blocks (HTTP 429 / IpBlocked) that defeat steps 1–3: `--backend browser` drives a real headed Chrome with a persistent profile (`.playwright/chrome-profile/`, gitignored) via Playwright, opens the transcript panel, captures its HTML, and parses it through the same code path as `--from-html`. On parse failure the captured HTML is saved to `.playwright/html/<id>.html` for manual `--from-html` retry.
5. **Manual HTML paste** — ask the user to copy the transcript panel HTML themselves, then parse with `--from-html`
6. **Flag as blocked** — only when steps 1–5 are exhausted (see Step 4)

#### Parse from Saved HTML

If the automated fetch fails (no captions) but transcript panel HTML is available
(from step 4 or 5 above), parse it directly:

```bash
# From an HTML file — video ID inferred from filename or provided explicitly
python systems/improvement-loop/app/transcript-fetcher/fetch.py --from-html /path/to/transcript.html --video-id VIDEO_ID
```

The parser handles both YouTube DOM formats:
- **Old:** `ytd-transcript-segment-renderer` with `.segment-timestamp` / `.segment-text`
- **New:** `transcript-segment-view-model` with `.ytwTranscriptSegmentViewModelTimestamp`

The `parse_transcript_html(html, video_id)` function is also importable for programmatic use.

### Step 4: Report Results and Flag Blocked Videos

Report which transcripts were fetched successfully and which failed. Common failure reasons:
- Video has no captions/subtitles
- Video is private or age-restricted
- Network connectivity issues

For any video where the full fallback chain (Step 3b) is exhausted:

1. If a research-source entry exists for the video, set its `status` to `"Blocked"` and
   note the reason in `key_takeaways` (e.g., "Blocked: no captions, HTML pull failed").
2. If no source entry exists yet, report the URL and failure reason to the caller so the
   research-loop can record it.

Blocked sources form the retry backlog — find them anytime with (quote-tolerant, since
existing sources mix quoted and unquoted status values):

```bash
rg -l 'status: "?Blocked"?' systems/improvement-loop/research-sources/
```

## Boundary Conditions

- **Safety posture:** This skill is write-capable but low-risk by design. Its writes are
  (a) additive transcript files in `transcripts/` (never overwritten without `--force`)
  and (b) the Step 4 `status: "Blocked"` flag on research-source entries. The Blocked
  flag is applied autonomously — it is additive metadata, reversible via git, inside the
  Researcher write boundary (DD-30), and always surfaced in the session's delta report
  under "Blocked" for human review. It never deletes or rewrites source content.
- **Out of scope:** modifying findings, authorities, system configs, or skill files;
  audio transcription; downloading video/audio media.
- **Termination:** the skill ends when every requested video has either a transcript
  file or a Blocked flag with a recorded reason. Do not loop retrying a backend that
  has already failed for the same video in the same session.

## Integration with Research Loop

This skill is called by the research-loop during Pass 2:

1. Research-loop identifies a high-value source (P1/P2 triage)
2. Research-loop checks for existing transcript
3. If missing, research-loop invokes this skill to fetch it
4. Research-loop reads the transcript for deep extraction

## Transcript File Format

Output files are markdown with this structure:

```markdown
# Transcript: [Video Title, or VIDEO_ID if metadata probe failed]

**URL:** https://www.youtube.com/watch?v=VIDEO_ID
**Segments:** [count]
**Channel:** [channel name]
**Duration:** [H:MM:SS]
**Uploaded:** [YYYY-MM-DD]

---

## Full Text

[Complete concatenated transcript text]
```

Full text only — no timestamped-segments section. Downstream consumers read for
content; no finding has ever cited a timestamp, and the section tripled file
size (ruled 2026-07-13). Timestamps remain available at fetch time if a
citation need ever materializes.

## Limitations

- Only fetches auto-generated or manual captions — no audio transcription
- English captions by default (use `--languages` flag for others)
- Metadata enrichment (title, channel, duration, upload date) requires yt-dlp; when
  the probe fails the header falls back to the bare video ID. Transcripts fetched
  before 2026-07-12 predate enrichment and carry ID-only headers.
- Token estimates are duration-based (~220 tokens/video-minute) — approximate, not a count
- IP-level YouTube blocks (HTTP 429 / IpBlocked) can span sessions within the same
  calendar day and are not solved by cookies. During a block, attempt step 4 (browser
  backend) once — a real browser session may pass where API clients are blocked. If
  step 4 also fails, stop: the ≥1-calendar-day retry spacing applies to the whole
  chain, including step 4.
