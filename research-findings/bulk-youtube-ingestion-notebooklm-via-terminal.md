---
name: 'Bulk YouTube Channel Ingestion into NotebookLM via Terminal Command'
summary: Use Claude Code to fetch all videos from a YouTube channel, filter by relevance criteria, and bulk-upload 200+ sources to a new NotebookLM notebook in a single terminal command — replacing hours
  of manual link-by-link uploads.
implementation_notes: null
category: Agentic OS
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources:
- notebooklm-claude-code-expert-experiments.md
proposals: []
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
related_findings:
- file: notebooklm-python-api-programmatic-access-beyond.md
  rel: companion
- file: notebooklm-mcp-claude-code-cited-knowledge-layer.md
  rel: companion
pipeline_status: raw
consumed_by: []
---
# Bulk YouTube Channel Ingestion into NotebookLM via Terminal Command

## What It Is

A Claude Code workflow that automates the creation and population of a NotebookLM knowledge base from a YouTube channel:

1. Provide Claude Code with a YouTube channel URL and a topic filter (e.g., "Huberman Lab — health videos only")
2. Claude Code fetches the full video list (~400 videos for a large channel) and presents them for collaborative filtering
3. The user selects a subset (e.g., "most recent 200") in conversation
4. Claude Code creates a new NotebookLM notebook and bulk-uploads all selected YouTube URLs as sources
5. Sources appear in real time in the NotebookLM UI; the process completes without further user interaction

The practitioner shows this completing ~200 sources (two notebooks: "archive" and "recent") in a single session. The alternative — manually copying each YouTube link and pasting into NotebookLM — is characterized as "such a big pain."

## Why It Matters

The volume threshold for useful NotebookLM knowledge bases is high: 50 videos gives partial coverage of an expert's output; 200+ gives near-complete coverage with robust citation breadth. Manual upload at that scale is prohibitive. The terminal workflow removes the bottleneck, making it practical to stand up a complete expert knowledge base for any YouTube channel in one session.

The collaborative filtering step (Claude presents the list, user selects) is important: it keeps the human in control of what enters the KB rather than blindly ingesting everything.

## Why People Are Using It

- Any YouTube channel becomes a queryable expert knowledge base in minutes, not hours
- Works for any domain: health (Huberman), product management (Lenny), programming, finance, etc.
- NotebookLM handles transcript extraction and embedding automatically — no local storage, no Whisper pipeline
- Reusable skill installable from a URL; the same skill works for any channel

## Potential Improvements

Automated relevance filtering (Claude scores each video's relevance to a goal before uploading) would reduce manual selection work. Incremental update mode (only upload videos newer than the last sync date) would keep large knowledge bases current without full re-ingestion.

## Potential Failure Modes

- YouTube API rate limits or changes could block bulk fetching of channel video lists
- NotebookLM source limits per notebook constrain very large channels (500+ videos may require multiple notebooks)
- Filtering entirely by recency ("last 200") may miss older but highly relevant content
- NotebookLM processes YouTube transcripts — channels with poor auto-captions produce low-quality source content
