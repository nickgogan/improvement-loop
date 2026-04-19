---
name: Memory Bank Isolation (Per-Agent, Per-Project)
summary: Long-term memory systems should support dynamic bank IDs that isolate memories by agent identity, project, or session. A Telegram bot agent and a coding agent sharing a memory bank will pollute
  each other's recall. Hindsight supports bankId configuration and channel-based isolation (HINDSIGHT_CHANNEL_ID, HINDSIGHT_USER_ID) as first-class primitives.
implementation_notes: If MetaSystem adopts semantic memory, ensure separate memory banks per system boundary (Improvement Loop, Household OS, Claude Build). Cross-system recall should be opt-in, not default.
  This maps directly to the existing system scope boundaries (DD-55, DD-56, DD-59).
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- openclaude-build-a-claude-code-agent-with-long-ter.md
related_findings:
- file: memorymd-cross-session-preference-persistence.md
  rel: same-problem
- file: compounding-knowledge-loop-internal-data.md
  rel: same-problem
- file: memory-cross-layer-promotion-governance.md
  rel: same-problem
- file: agent-memory-architecture-multi-agent-layered.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
- file: claude-code-long-term-memory-via-pre-prompt-recall.md
  rel: same-problem
- file: biomimetic-memory-auto-recall-over-tool-based.md
  rel: same-problem
- file: multi-client-context-isolation-with-shared-skills.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---
## What It Is

A memory architecture principle demonstrated in Hindsight's Claude Code integration: memory banks should be scoped and isolated to prevent cross-contamination.

Configuration primitives:
- **bankId** (default: "claude_code"): Names the memory bank. Change to isolate memory per agent, per project, or per workspace.
- **bankMission**: Tells the memory engine who this agent is, improving fact extraction relevance.
- **retainMission**: Guides what the memory engine should remember from conversations.
- **HINDSIGHT_CHANNEL_ID**: Isolates memories per messaging channel (e.g., separate Telegram groups).
- **HINDSIGHT_USER_ID**: Isolates memories per user in multi-user scenarios.

The always-on agent pattern (Okhlopkov's architecture) demonstrates a two-tier memory system: hot memory (operational context in a Docker volume) and long-term memory (an Obsidian vault in git), with agent-memory as a third layer of topic-specific notes and corrections.

## Why It Matters

Without isolation, a memory system that works well for one agent becomes a liability in multi-agent or multi-project deployments. Memories from Project A pollute recall for Project B, creating confusion and contradictions. This is the memory equivalent of the context file bloat problem -- more memories aren't better if they're irrelevant.

## Why People Are Using It

The Hindsight plugin supports per-agent, per-project, and per-session isolation out of the box. The always-on agent community (running Claude Code on servers 24/7 via Telegram) has independently converged on separate memory tiers because compaction in long sessions erases critical rules -- forcing them to separate "must survive compaction" rules (in CLAUDE.md) from "useful but not critical" context (in memory files).

## Potential Improvements

Cross-bank queries: allow explicit opt-in to search memories from other banks when the agent detects a cross-project dependency. This would enable MetaSystem's cross-system reference pattern while preserving isolation by default.

## Potential Failure Modes

Over-isolation creates knowledge silos. Lessons learned in one project that would benefit another are invisible. The isolation boundaries need to match the actual knowledge boundaries, which may not align with organizational boundaries.
