---
name: Multi-Agent Proportional Content Summarization to Obsidian
summary: Claude Code downloads a video/podcast/article transcript, splits it into chunks, dispatches sub-agents to summarize each chunk, and assembles a structured Obsidian note proportional in depth to
  the content length. For long content (2-3 hour podcast), the result is a Wikipedia-like article with TLDR callout, timestamps, top quotes, and entity pages for people and concepts mentioned.
implementation_notes: 'Workflow steps: (1) Download transcript via yt-dlp or equivalent; if no transcript, download video and run Whisper transcription locally. (2) Split transcript into segments. (3) Sub-agents
  summarize individual segments. (4) Assemble into structured Obsidian note with: video thumbnail (via Obsidian plugin), TLDR callout block, timestamped topic index, key quotes section, people/concepts
  mentioned section. (5) For each entity mentioned, create a stub page in the vault. Summary depth is proportional: 500-page book → 15-20 min read summary. Implemented as a Claude Code skill installable
  from a URL.'
category: Agentic OS
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- claude-code-for-life-daily-briefs-obsidian-memory.md
related_findings:
- file: bulk-youtube-ingestion-notebooklm-via-terminal.md
  rel: same-problem
- file: obsidian-as-transparent-frontend-vs-rag-black-box.md
  rel: companion
- file: claude-code-as-vault-query-engine-project-assistant.md
  rel: companion
- file: subagent-exploration-mode-parallel-codebase-mappi.md
  rel: same-technique
- file: cited-health-interview-pattern-parallelized-kb-qa.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-04-20'
pipeline_status: extracted
consumed_by:
  - skills/multi-agent-proportional-content-summarization.md
---
# Multi-Agent Proportional Content Summarization to Obsidian

## What It Is
A Claude Code skill that takes any long-form content source (YouTube video, podcast, article, book, academic paper) and produces a structured, hyperlinked Obsidian knowledge artifact:

**Input:** URL or file path  
**Process:**
1. Download transcript (yt-dlp for YouTube; Whisper transcription as fallback when no transcript exists)
2. Split into chunks sized for individual sub-agent context windows
3. Sub-agents summarize individual chunks in parallel
4. Orchestrator assembles chunk summaries into a structured note

**Output note structure:**
- Video thumbnail (clickable, via Obsidian plugin)
- TLDR callout block (2-4 sentences)
- Timestamped topic index (each section links to the timestamp in the original video)
- Key quotes section
- People/concepts/tools mentioned section
- Each entity in the "mentioned" section links to a stub page in the vault

**Proportionality rule:** Summary depth scales with content length. A 15-minute video gets a concise overview; a 500-page book gets a 15-20 minute read. This is explicitly contrast-positioned against ChatGPT/Gemini direct summaries, which are limited by context window and produce generic overviews of long content.

The entity page creation is the key differentiation from flat summarization: as the vault accumulates summaries, entities (people, concepts, tools) accumulate cross-references. A person mentioned in 10 different podcasts has an entity page linking all 10 sources.

## Why It Matters
Standard AI chatbot summarization fails on long-form content (2-3 hour podcasts, books) because the full transcript doesn't fit in a single context window. The multi-agent chunking approach solves this architecturally. The Obsidian storage makes the result a persistent, hyperlinked, navigable knowledge artifact rather than a one-time output. The entity page pattern transforms isolated summaries into a growing interconnected knowledge base where repeated exposure to the same people/concepts builds up a profile organically.

## Why People Are Using It
Practitioner uses it to evaluate whether a long podcast contains novel information before committing to listening — the timestamped topic index provides this in seconds. Also used to understand dense technical papers by having Claude Code create prerequisite concept pages and explain the paper at the appropriate level. The skill is shared/installable, suggesting broader community adoption of the pattern.

## Potential Improvements
- **Incremental entity enrichment** — when a new summary mentions an entity already in the vault, append the new reference rather than creating a duplicate stub
- **Novelty detection** — compare new podcast summary against existing summaries of the same speaker to flag repeated talking points vs. novel content
- **Reading-level personalization** — the user explicitly values summaries at their comprehension level; this could be captured as a vault-level preference that all summaries inherit

## Potential Failure Modes
- Whisper transcription quality varies significantly by audio quality; heavily accented or technical speech produces noisy transcripts that degrade summary quality
- Sub-agent chunk boundaries may cut mid-thought; naive splitting (by word count) can produce incoherent chunk summaries at boundaries
- Entity page proliferation at scale — a large vault accumulates thousands of stub pages that become noise; without curation, discoverability degrades
- The proportionality heuristic requires calibration — what counts as "15-20 minute read" depth for a 500-page book needs explicit token/word targets

## Extraction Note — 2026-04-20
Extracted as **skill**: [[multi-agent-proportional-content-summarization]] in `extracts/skills/`
