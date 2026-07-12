---
name: "Scene-Detection Frame Sampling for Agent Video Watching"
summary: |-
  A Claude Code skill makes video a first-class agent input by pairing the transcript
  (yt-dlp captions, Whisper/Grok fallback for Loom/Zoom) with FFmpeg scene-detection
  frame extraction — one frame per actual scene change instead of N frames on a timer —
  so the agent sees demos, diagrams, and edits rather than random screenshots. Ends with
  a human-gated ingest step into a linked knowledge base (Obsidian second brain).
implementation_notes: |-
  Timer sampling fails at scale: 100 frames over a 1-hour video = one frame per 36s; over
  10 hours = one per 6 minutes. Scene detection allocates frames where visual information
  actually changes. Pipeline: URL → captions via yt-dlp (free when present) → Whisper/Grok
  transcription fallback → FFmpeg scene-detect frames → agent analysis → "ingest into KB?"
  gate. Origin: a skill by "Brad", fixed/extended by Taoufik (GitHub repo referenced in
  video description — not yet chased).
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented, working demo)"
adoption_status: "Not Yet Started"
priority: "P2"
applicability:
  - "IL (transcript-fetcher redesign)"
  - "General"
adopted_in: []
sources:
  - "this-claude-skill-watches-videos-so-you-dont-have-to.md"
related_findings:
  - file: "ffmpeg-cli-multimedia-manipulation-for-claude-cod.md"
    rel: "extends"
  - file: "dual-path-rag-ingestion-text-vs-multimodal.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A video is two streams — frames and transcript — and agent tooling that ingests only the
transcript is blind to half the content. This skill extracts the transcript cheaply
(yt-dlp captions when available; Whisper or Grok transcription when not, which also covers
Loom recordings and Zoom calls) and solves the frame problem with **FFmpeg scene
detection**: instead of sampling frames on a fixed timer, it grabs one frame each time the
scene actually changes. The agent then "watches" the video — text plus visually-informative
frames — and closes with a human-gated question: ingest this analysis into the knowledge
base? Ingested notes land linked to existing context (the creator uses an Obsidian second
brain).

## Why It Matters for Us

Our `/transcript-fetcher` is transcript-only — this finding names our exact capability gap
and is the primary design input for its redesign (session-133 directive, restructure
program Phase 1). Three separable ideas: (1) scene-detection sampling makes the visual
channel tractable at any video length; (2) transcription fallback extends intake beyond
YouTube to meetings and screen recordings; (3) the watch → analyze → **gated ingest** →
linked-KB loop is our own pipeline's human-gate pattern (DD-29) applied to video intake.

## Caveats

Single practitioner demo; no benchmark of scene-detection threshold quality or token cost
of frame analysis. The upstream GitHub repo is referenced but not yet analyzed — chase it
before building (reuse before invention).
