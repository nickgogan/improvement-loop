---
notion_id: 32b1e08b-9b34-812f-ae55-e88f1ca5b53b
name: 'NotebookLM Python API: Programmatic Access Beyond the Web UI'
summary: The NotebookLM CLI uses browser automation to give Claude Code programmatic access to NotebookLM's video analysis capabilities — enabling YouTube-to-analysis pipelines that run on Google's tokens
  rather than the user's Claude API credits.
implementation_notes: null
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- 10-cli-tools-that-make-claude-code-unstoppable.md
- claude-code-works-better-when-you-do-this.md
- notebooklm-py-unofficial-python-api-skill-for-note.md
- notebooklm-claude-code-expert-experiments.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-05-24'
pipeline_status: "classified"
consumed_by: []
---
# NotebookLM Python API: Programmatic Access Beyond the Web UI

## What It Is
notebooklm-py is an unofficial Python API and CLI that provides full programmatic access to Google NotebookLM — including capabilities the web UI doesn't expose. Three interfaces: Python async API (for application integration and custom pipelines), CLI (for shell scripts and CI/CD), and agent integration (ships SKILL.md for Claude Code, AGENTS.md for Codex, installable via `npx skills add` or `notebooklm skill install`). Covers the complete NotebookLM surface: notebooks (CRUD), sources (URLs, YouTube, PDFs, Google Drive, pasted text), chat (questions, history, custom personas), research (web and Drive agents with fast/deep modes and auto-import), and sharing (permissions, view levels). Content generation spans all Studio types: Audio Overview (4 formats, 3 lengths, 50+ languages), Video Overview (3 formats, 9 visual styles), Slide Deck (with individual slide revision), Infographic, Quiz, Flashcards, Report, Data Table, and Mind Map.

## Why It Matters
Unlike the previous browser-automation approach, this library uses undocumented Google APIs directly — making it faster, more reliable, and scriptable. It exposes features unavailable in the web UI: batch downloads, quiz/flashcard export (JSON/Markdown/HTML), mind map JSON extraction, PPTX slide deck downloads, individual slide revision via natural language, data table CSV export, source fulltext access, and programmatic sharing. For research workflows, this means building repeatable pipelines that import sources, generate analysis artifacts, and export structured data — all without browser fragility.

## Why People Are Using It
Zero-cost video/document analysis on Google's infrastructure. CLI and Python API enable automation at scale. Agent skill integration means Claude Code can invoke NotebookLM as a tool naturally. Content generation (podcasts, videos, quizzes, flashcards, mind maps) adds value beyond raw analysis. Batch operations replace manual copy-paste from the web interface. The research agent feature (web and Drive search with auto-import) enables automated source discovery.

## Potential Alternatives
yt-dlp + Whisper + Claude text analysis (local, consumes Claude tokens). Paid video analysis APIs (Twelve Labs, Google Video AI). YouTube transcript extraction (text only). Browser automation approach (the original NotebookLM CLI mentioned in "10 CLI Tools" video — more fragile). Google's official NotebookLM API (if/when released).

### Brain/Executor Architecture (2026-04-07)

New practitioner evidence positions NotebookLM in a broader architectural pattern: **"NotebookLM as brain, Claude as executor."** In this model:

- **NotebookLM (the brain):** Ingests and indexes all research sources -- YouTube videos, Google Drive documents, PRDs, web sources, design docs, meeting notes
- **Claude Code (the executor):** Receives only a lean initial context; queries NotebookLM via API when it needs specific knowledge during execution
- **System prompt query instruction:** A `.md` file in the Claude Code project stores the NotebookLM query instruction, teaching Claude how and when to fetch from the KB

The key distinction is **on-demand knowledge retrieval vs. upfront context dump**. Rather than pasting all research into the initial context (bloating the window before work begins), knowledge lives outside the conversation and is fetched only when relevant. This is effectively a RAG pattern applied at the Claude Code workflow level without custom infrastructure.

## Potential Improvements
Official Google API would eliminate reliance on undocumented endpoints. MCP server wrapping the Python API for direct tool-use by agents. Streaming generation status for long-running artifact creation. Cross-notebook search and analysis.

## Potential Failure Modes
Uses undocumented Google APIs that can break without notice — explicitly "not affiliated with Google." Rate limiting under heavy automated usage. Auth relies on browser-based Google login and cookie storage. No stability guarantees — best for prototypes, research, and personal projects per the authors' own warning. Google could intentionally block programmatic access.
