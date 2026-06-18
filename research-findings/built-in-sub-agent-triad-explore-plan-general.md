---
name: "Built-In Sub-Agent Triad (Explore, Plan, General Purpose)"
summary: "Claude Code ships with three implicit sub-agents that activate automatically without user instruction: Explore (Haiku, read-only, fast/cheap scouting), Plan (read-only, activates in plan mode), and General Purpose (Sonnet, full read-write, complex multi-step tasks). Each runs in its own context window to prevent main conversation bloat. Claude decides when to use them based on task complexity."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "five-agentic-patterns-claude-code.md"
related_findings:
  - file: "model-tier-routing-expensive-orchestrator-cheap-s.md"
    rel: "same-problem"
  - file: "boris-chernys-explore-plan-implement-commit-workf.md"
    rel: "same-problem"
  - file: "sub-agent-context-isolation-for-parallel-complex.md"
    rel: "same-problem"
  - file: "progressive-skill-loading.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - agent-design-patterns.md
tags:
  - "session-95-reextract"
---

## What It Is

Claude Code has three built-in sub-agents that operate automatically, without explicit user instruction:

1. **Explore** — Runs on Haiku (cheapest/fastest model). Read-only: can search files, inspect folder structures, but cannot modify anything. Activates when Claude needs to understand codebase context (e.g., "how does authentication work in this project?"). Returns a summary to the main conversation.

2. **Plan** — Activates specifically when the user enters plan mode (`/plan` or Shift+Tab twice). Read-only. Researches the codebase before presenting a strategy. Separate context window.

3. **General Purpose** — Runs on Sonnet. Full tool access (read and write). Handles complex multi-step tasks that require both exploring code and making changes across multiple files.

The key architectural properties:
- **Automatic dispatch**: Claude decides when to spin up each sub-agent based on task complexity. The user doesn't need to request it.
- **Context isolation**: Each sub-agent runs in its own context window. The main conversation only receives the summary/result, preventing context bloat from file reading and searching.
- **Model tiering**: Cheap model (Haiku) for scouting tasks, medium model (Sonnet) for implementation tasks, with the implicit assumption that the main orchestrator runs on the premium model.

## Why It Matters

This is a production implementation of the model-tier-routing pattern built directly into the tool, not a custom harness. It demonstrates that even "simple" single-conversation usage of Claude Code is already multi-agent under the hood. Understanding this changes how users think about their sessions — they're always working with a team, not a single model.

For harness builders, the triad is a reference architecture: scout agents should be cheap and read-only, planning agents should be isolated from implementation context, and implementation agents need full tool access but should report results rather than dumping raw context back to the orchestrator.

## Why People Are Using It

Users don't choose to use it — it activates automatically. But understanding its existence changes behavior: knowing that Explore offloads file reading to a separate context window explains why the main conversation stays clean during codebase research. Knowing that Plan uses a separate window explains why plan mode produces better strategies than ad-hoc planning within a conversation.

## Potential Improvements

- Make the sub-agent dispatch visible and configurable (which model for each tier, when to activate)
- Allow users to define custom implicit sub-agents beyond the three built-in ones
- Add telemetry showing when sub-agents were invoked and their context usage

## Potential Failure Modes

- Users unaware of the triad may duplicate work by manually doing what the sub-agents already handle
- The Explore sub-agent running on Haiku may miss nuances that a more capable model would catch
- Automatic dispatch heuristics may not match the user's intent — Claude might spin up Explore when the user wanted to see the raw file content in their main context
