---
name: transcript-fetcher
description: >-
  Fetch YouTube video transcripts as timestamped markdown files for research-loop
  Pass 2 deep extraction. Wraps the Python transcript fetcher tool. Use when the
  research-loop needs full transcript text for a high-value video source, or when
  the user provides YouTube URLs and wants transcripts fetched.
user-invocable: true
allowed-tools: Bash Read Write
argument-hint: "<url1> [url2] [url3] ..."
---

# Transcript Fetcher

Fetch YouTube video transcripts and save them as timestamped markdown files for downstream research-loop processing.

## When to Use This Skill

- The research-loop needs a transcript for Pass 2 deep extraction
- The user provides YouTube URLs and wants transcripts fetched
- Batch fetching transcripts for multiple videos before a research session

## Prerequisites

The Python tool requires `youtube-transcript-api`. If not installed:

```bash
pip install youtube-transcript-api
```

## Tool Location

The fetcher script lives at:
```
incubator/claude-build/app/transcript-fetcher/fetch.py
```

Transcripts are saved to:
```
incubator/claude-build/app/transcript-fetcher/transcripts/
```

Each transcript is named by video ID (e.g., `5ztI_dbj6ek.md`).

## Procedure

### Step 1: Check for Existing Transcripts

Before fetching, check if transcripts already exist:

```bash
ls incubator/claude-build/app/transcript-fetcher/transcripts/
```

If a transcript for the requested video ID already exists, skip fetching and report it as available.

### Step 2: Fetch Transcripts

Use `Bash` to run the fetcher:

```bash
# Single URL
python incubator/claude-build/app/transcript-fetcher/fetch.py --urls "https://www.youtube.com/watch?v=VIDEO_ID"

# Multiple URLs
python incubator/claude-build/app/transcript-fetcher/fetch.py --urls "URL1" "URL2" "URL3"

# From a file containing URLs (one per line)
python incubator/claude-build/app/transcript-fetcher/fetch.py --input /path/to/urls.txt
```

The tool accepts various YouTube URL formats:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`
- Raw video IDs (11 characters)

### Step 3: Verify Output

After fetching, verify the transcript files were created:

```bash
ls -la incubator/claude-build/app/transcript-fetcher/transcripts/
```

Each transcript file contains:
- Full concatenated text (for quick reading)
- Timestamped segments (for precise citation)

### Step 4: Report Results

Report which transcripts were fetched successfully and which failed. Common failure reasons:
- Video has no captions/subtitles
- Video is private or age-restricted
- Network connectivity issues

## Integration with Research Loop

This skill is called by the research-loop during Pass 2:

1. Research-loop identifies a high-value source (P1/P2 triage)
2. Research-loop checks for existing transcript
3. If missing, research-loop invokes this skill to fetch it
4. Research-loop reads the transcript for deep extraction

## Transcript File Format

Output files are markdown with this structure:

```markdown
# Transcript: VIDEO_ID

**URL:** https://www.youtube.com/watch?v=VIDEO_ID
**Segments:** [count]

---

## Full Text

[Complete concatenated transcript text]

---

## Timestamped Segments

**[0:00]** First segment text

**[0:15]** Next segment text

...
```

## Limitations

- Only fetches auto-generated or manual captions — no audio transcription
- English captions by default (use `--languages` flag for others)
- No title/metadata enrichment — the video ID is the only identifier in the file
