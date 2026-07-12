---
name: "Austin Marchese — How to Build A Self-Improving System with Claude"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Five-step build framework for a self-improving Claude Code system: base (Karpathy-style
  raw/ + wiki/ knowledge base + utility skills), upload (bulk-ingest historical data —
  session history is called the most relevant training data you will ever have), inflow
  (skill-driven data pipelines: sync-claude-sessions, sync-ecosystem-data, sync-curated-
  content), loop (an improve-system skill that reads sessions, finds patterns, and
  proposes changes tiered into three buckets — auto-approve to a changelog, need-sign-off
  to a dated checkbox review file with approve / reject / approve-and-don't-ask-again,
  more-context-required to the same file), and drive (run it, don't over-engineer it).
  Explicitly frames the three-bucket tiering as the middle of a spectrum between full
  automation (system drift risk) and review-everything (abandonment risk), with the human
  kept as tastemaker.
relevance: "High"
added_by: "Nick"
tags:
  - "claude-code"
  - "session-management"
  - "skills"
  - "context-engineering"
  - "vault-architecture"
url: "https://www.youtube.com/watch?v=2fc0NX9vIJ8"
authority:
  - "austin-marchese.md"
findings:
  - "three-bucket-change-approval-tiering.md"
  - "session-history-mining-for-skill-discovery.md"
date_added: "2026-07-12"
date_processed: "2026-07-12"
date_published: "2026-06-28"
---

Session-136 Pass 2 deep extraction (link-intake wave 2, loops/self-improvement cluster).
Transcript: `app/transcript-fetcher/transcripts/2fc0NX9vIJ8.md`. Processed as a pair with
`8-claude-loops-to-build-10x-faster.md` (same author) — the three-bucket change-approval
pattern is extracted once, citing both. The raw/wiki knowledge-base and data-pipeline
material overlaps existing Karpathy-LLM-wiki and agentic-OS findings and was not
re-extracted.
