---
name: Hook-Based Transparent Memory Injection
summary: Three-hook lifecycle (SessionStart→bootstrap, UserPromptSubmit→auto-recall, Stop→auto-capture) enables transparent memory without agent awareness. Memory is injected and captured via hooks — the
  agent never explicitly manages memory.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: hook-based-enforcement-for-agent-outputs.md
  rel: extends
- file: claude-code-long-term-memory-via-pre-prompt-recall.md
  rel: enables
- file: automatic-fact-extraction.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: cross-session-learnings-jsonl.md
  rel: same-problem
- file: gsd-global-learnings-store-cross-session-persistence.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
---

## What It Is

A three-hook pattern that makes memory fully transparent to the agent: (1) `SessionStart` hook bootstraps runtime state and cold-starts the memory system, (2) `UserPromptSubmit` hook auto-recalls relevant memories and injects them as a `systemMessage` before every turn — the agent sees memories as context but never explicitly calls a recall function, (3) `Stop` hook auto-captures the conversation transcript, parses it, and extracts memories for persistence. The agent operates as if it naturally "remembers" and "learns" without any explicit memory management tools.

## Why It Matters

The existing KB covers hook-based enforcement (PostToolUse) and long-term memory via pre-prompt recall as separate concepts. This pattern unifies them into a complete lifecycle: capture → store → recall, all via hooks, all transparent. The agent's cognitive load is reduced — it doesn't need to decide when to save or what to recall. The hook layer handles that based on semantic relevance scoring.

## Why People Are Using It

Observed in [OpenViking](https://github.com/volcengine/OpenViking) — see [[openviking-analysis]] for structural details. OpenViking's Claude Code plugin implements this via `hooks.json` with three hooks (`bootstrap-runtime.mjs`, `auto-recall.mjs`, `auto-capture.mjs`). The `systemMessage` output channel enables transparent injection without modifying the user's prompt.

## Potential Alternatives

- Explicit memory tools (agent calls `memory_store`/`memory_recall` as tools)
- CLAUDE.md-based memory (auto-memory, MetaSystem's current approach)
- Conversation-level context carry (no persistent memory)

## Potential Improvements

Could be combined with the two-threshold compaction pattern to trigger memory extraction at compaction boundaries rather than only at session end.

## Potential Failure Modes

- Hook execution adds latency to every turn (recall) and session end (capture)
- Transparent injection may confuse the agent if injected memories conflict with current context
- Memory extraction quality depends on the extraction prompt
