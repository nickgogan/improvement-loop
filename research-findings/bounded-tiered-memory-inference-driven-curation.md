---
name: Bounded Tiered Memory with Inference-Driven Curation
summary: Memory files have hard character ceilings enforced by the agent loop (MEMORY.md ≤2,200 chars, USER.md ≤1,375 chars). Writes are triggered by conversation-pattern inference, not explicit commands.
  Timestamps are embedded. A 'Curator' step consolidates/evicts on overflow, resolving conflicts in favor of most-recent high-confidence facts. The combination of fixed ceilings + inference-driven writes
  + LLM curation produces a self-maintaining user model that degrades gracefully rather than growing unbounded.
implementation_notes: MetaSystem's MEMORY.md has no hard ceiling and relies on file-level conventions. This finding suggests enforcing a character limit and adding a curator step when the limit is exceeded.
  The inference-driven write trigger (agent decides what to persist based on conversation patterns, not explicit user commands) is distinct from MetaSystem's current approach where memory saves are explicit.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- hermes-agent-nousresearch-analysis.md
- rebuilt-hermes-memory-in-claude-code.md
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-07-13'
related_findings:
- file: four-tier-agent-memory-model-with-write-policy.md
  rel: extends
- file: typed-relationship-memory-graph.md
  rel: same-problem
- file: verbatim-storage-thesis-for-memory.md
  rel: contradicts
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
- file: ace-delta-updates-over-monolithic-rewrites.md
  rel: same-problem
- file: agent-memory-architecture-multi-agent-layered.md
  rel: same-problem
- file: background-hooks-as-token-economy.md
  rel: same-problem
- file: biomimetic-memory-auto-recall-over-tool-based.md
  rel: same-problem
- file: catastrophic-context-collapse-risk-during-claudemd.md
  rel: same-problem
- file: claude-code-context-management-decision-matrix-five-tools.md
  rel: same-problem
- file: claude-code-hooks-for-automatic-session-memory.md
  rel: same-problem
- file: claude-code-long-term-memory-via-pre-prompt-recall.md
  rel: same-problem
- file: content-derived-temporal-expiration-contradiction-resolution.md
  rel: same-problem
- file: context-file-instruction-bloat-eth-zurich.md
  rel: same-problem
- file: cross-session-learnings-jsonl.md
  rel: same-problem
- file: localized-memory-maintenance-over-global-reorganization.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
- defending-agent-context.md
- templates/tiered-memory-file-architecture.md
- rules/apply-hard-ceilings-to-agent-memory-files.md
tags:
- context-engineering
- memory
- agent-design
---

# Bounded Tiered Memory with Inference-Driven Curation

## What It Is

A memory architecture with three tiers and hard boundaries:

- **Hot** (always-injected): SOUL.md (identity), MEMORY.md (≤2,200 chars, environment facts), USER.md (≤1,375 chars, user preferences). Loaded verbatim into system prompt each session.
- **Warm** (retrieved): FTS5 full-text search over SQLite state.db surfaces relevant prior-session snippets, which are LLM-summarized before injection.
- **Cold** (archival): Raw JSONL transcripts in sessions/.

## Why It Matters

The key innovations are: (1) hard character ceilings on always-loaded memory, preventing unbounded growth; (2) inference-driven writes — the agent decides what to persist based on conversation patterns, not just explicit "remember this" commands; (3) a Curator step that consolidates and evicts entries when ceilings are exceeded, resolving conflicts in favor of most-recent high-confidence facts. This produces a self-maintaining user model that degrades gracefully.

## Practitioner Rebuild in Claude Code (2026-07)

Simon Scrapes rebuilt the pattern inside Claude Code as portable local markdown
(`rebuilt-hermes-memory-in-claude-code.md`), confirming the architecture transfers off
the Hermes runtime: a size-capped curated snapshot (memory.md, max 2,500 chars, silently
injected every session alongside profile and today's memories), inference-driven writes
via a **post-turn hook** that decides after every turn whether anything is worth
promoting as a durable fact (decisions, price changes, preferences), dedup-then-replace
favoring most-recent/most-relevant on overflow, and — his addition — **user-editable
promotion rules** in a readable "meta memory-write skill," so the curation policy is
owned by the operator rather than baked into the loop. He also surfaces the failure
evidence for unbounded curation: Hermes' self-rewriting loop has multiple reports of the
agent overwriting good information when editing its own memory/skills, and its hard
caps compressing away standing instructions (one user built a plugin solely to stop his
instructions being forgotten). Corroborates the ruled IB-176 memory design
(`project-management/design-notes/2026-07-13-memory-system-design.md` §1) point-for-point:
append-only capture + size-capped curated distillate, gated promotion, files-over-runtime.

## How It Could Fail

Hard ceilings cause information loss — the curator may evict entries that turn out to be important later. Inference-driven writes may persist irrelevant observations. The curation quality depends on the LLM's judgment, which may not align with user priorities.
