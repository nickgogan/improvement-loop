---
title: "Multi-Agent Proportional Content Summarization to Obsidian"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "multi-agent-proportional-content-summarization"
extraction_date: "2026-04-20"
identification_report: "2026-04-20-identification-report.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic coding systems that ingest long-form content (video, audio, articles, books) and need persistent, navigable knowledge artifacts"
    - "personal knowledge management workflows using Obsidian or similar vault tools"
    - "multi-agent orchestration pipelines where parallel subagent dispatch is available"
  platform_coupling: "specific:claude-code"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — writes Obsidian notes and entity stub pages to vault; removal requires manual file deletion or vault cleanup tooling"
  auditability: "medium — each output note is a readable artifact with source attribution; entity stub provenance is traceable via back-references; transcript acquisition step is auditable by source URL"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Pattern documented by a practitioner sharing the skill as installable from a URL, suggesting early community adoption; no production deployments known within this system at time of extraction."
contract:
  preconditions: "Claude Code harness is available with subagent dispatch. Target Obsidian vault is accessible and writable. Transcript source is fetchable (yt-dlp for YouTube, Whisper for audio without transcript, readable text for articles). The vault has a stable convention for entity stub pages."
  invariants: "Summary depth is proportional to source length — short content produces concise summaries, long content produces comprehensive artifacts. Every output note carries a TLDR, timestamp index (where applicable), and entity references. Entity stub pages are created once and reused across summaries (no duplicate stubs for the same entity)."
  governance: "Owner: Claude Code user / personal productivity skill. Installed per-user. Vault write access is scoped to a designated summaries folder and the shared entity folder. Does not modify source transcripts."
  recovery: "If transcript fetch fails: surface the failure with the source URL and stop — do not attempt to summarize raw audio without transcription. If a subagent returns a malformed chunk summary: re-dispatch that chunk with a tighter prompt. If entity deduplication fails: create a duplicate stub and flag for manual merge."
tags:
  - "extracted-artifact"
  - "skill"
---

# Multi-Agent Proportional Content Summarization to Obsidian

**Source:** [[multi-agent-proportional-content-summarization]]
**Form:** skill
**Extraction date:** 2026-04-20

## Purpose

Take any long-form content source (YouTube video, podcast, article, book, academic paper) and produce a structured, hyperlinked Obsidian knowledge artifact whose depth scales with source length — collapsing the "too long to summarize, too valuable to skip" problem into a bounded-read reviewable artifact.

## Inputs

- **Source identifier:** URL (YouTube, podcast, article) or local file path (PDF, text, audio).
- **Target vault path:** Obsidian vault root.
- **Summaries folder:** Designated subfolder for summary notes (e.g., `summaries/`).
- **Entity folder:** Shared subfolder for entity stub pages (e.g., `entities/`).
- **Proportionality target (optional):** Target read-time for the summary (e.g., 15 min). Defaults by source length: ≤30 min source → 2-3 min read; 30-90 min → 5-8 min read; 90 min-3 hr → 10-15 min; books/papers → 15-20 min.

## Outputs

A single Obsidian note in the summaries folder, containing:

- **Clickable thumbnail** (video only, via Obsidian plugin).
- **TLDR callout block** — 2-4 sentences summarizing the source's core claim.
- **Timestamped topic index** (video/audio) — each section header links to the timestamp in the original.
- **Key quotes** — verbatim pull-quotes with attribution.
- **People mentioned** — with links to entity stub pages.
- **Concepts mentioned** — with links to concept stub pages.
- **Tools/products mentioned** — with links to tool stub pages.

Plus one entity stub page per newly-mentioned entity in the "mentioned" sections. Existing entity pages receive a new back-reference to this summary.

## Steps

1. **Acquire transcript.**
   - YouTube: `yt-dlp --write-auto-sub --skip-download {url}` (extract captions).
   - Audio without transcript: download audio, run local Whisper.
   - Article/text: fetch and clean (strip boilerplate).
   - If transcript acquisition fails: surface error and stop.

2. **Chunk the transcript.** Split into chunks sized for a single subagent context window with overlap at chunk boundaries (to preserve mid-thought context). Chunk size ≈ 3-5k tokens; overlap ≈ 200-400 tokens.

3. **Dispatch subagents in parallel.** Each subagent receives one chunk plus a shared prompt: produce a structured chunk summary (key claims, quotes, entities mentioned, timestamps if available).

4. **Assemble the note.** Orchestrator concatenates chunk summaries and reduces to the target structure:
   - Synthesize TLDR from chunk-level key claims.
   - Order timestamp index by position in source.
   - Deduplicate entity mentions across chunks.
   - Select top N quotes by salience signal returned by subagents.

5. **Create or update entity stubs.** For each entity in the mentioned sections:
   - Check vault for existing stub (match by canonical name or slug).
   - If present: append back-reference to this summary.
   - If absent: create stub with name, type (person/concept/tool), first-seen source, and back-reference.

6. **Write the summary note.** Place in the summaries folder with a filename derived from the source title (kebab-case, length-capped).

7. **Verify proportionality.** Compare output word count against the target read-time. If off by >50%, flag for manual trim or expansion — do not silently accept.

## Failure Modes

- **Whisper transcription quality degrades on accented or technical speech.** Output reflects transcript noise. Mitigation: when transcript source is Whisper, annotate the TLDR with a confidence qualifier and include a link to the raw audio timestamp for verifying contested claims.
- **Chunk boundaries cut mid-thought.** Overlap reduces but does not eliminate this. Mitigation: subagents are prompted to flag incomplete thoughts at chunk edges; the orchestrator reconciles edge summaries before writing.
- **Entity stub proliferation.** Over time the entities folder accumulates thousands of low-quality stubs, each referenced once. Mitigation: periodic prune pass removes stubs referenced by fewer than N summaries and not linked from any other note.
- **Proportionality calibration drift.** "15-20 min read for a 500-page book" is subjective. Mitigation: define explicit word-count targets per source-length bucket and verify in step 7.
- **Duplicate entity creation.** Different name spellings for the same entity create separate stubs. Mitigation: canonical-name normalization (case-fold, strip punctuation) at stub lookup; periodic manual merge pass for ambiguous cases.

## Contract

### Preconditions
Claude Code harness is available with subagent dispatch. Target Obsidian vault is accessible and writable. Transcript source is fetchable (yt-dlp for YouTube, Whisper for audio without transcript, readable text for articles). The vault has a stable convention for entity stub pages.

### Invariants
Summary depth is proportional to source length — short content produces concise summaries, long content produces comprehensive artifacts. Every output note carries a TLDR, timestamp index (where applicable), and entity references. Entity stub pages are created once and reused across summaries (no duplicate stubs for the same entity).

### Governance
Owner: Claude Code user / personal productivity skill. Installed per-user. Vault write access is scoped to a designated summaries folder and the shared entity folder. Does not modify source transcripts.

### Recovery
If transcript fetch fails: surface the failure with the source URL and stop — do not attempt to summarize raw audio without transcription. If a subagent returns a malformed chunk summary: re-dispatch that chunk with a tighter prompt. If entity deduplication fails: create a duplicate stub and flag for manual merge.
