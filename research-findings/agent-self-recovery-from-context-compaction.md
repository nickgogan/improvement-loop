---
name: "Agent Self-Recovery from Context Compaction"
summary: "Explicit recovery protocol for agents that lose context mid-task due to compaction: read external state file for current assignments, run `gh pr view` for PR state, re-derive working context from filesystem rather than conversation history. Fills the gap between 'compaction happens' and 'what does the agent do after'."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources: []
related_findings:
  - file: "proactive-compaction-before-intelligence-degradation.md"
    rel: extends
  - file: "two-threshold-compaction-strategy.md"
    rel: extends
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: raw
consumed_by: []
---

## What It Is

A deterministic recovery protocol embedded in agent instructions that specifies exactly what an agent should do when it detects context loss from compaction. The protocol: (1) read the orchestrator state file (`~/.claude/orchestrator-state.json`) to recover current assignment, branch, worktree, and objective; (2) run `gh pr view` to get PR state including review status and CI results; (3) inspect the filesystem (git status, recent commits, test results) to reconstruct working context.

The key insight is that recovery is pre-scripted in the agent's instructions — the agent does not need to figure out what to do after compaction because the recovery steps are already in its system prompt. Context compaction is treated as a known operational event with a defined response, not an unexpected failure.

## Why It Matters

Most compaction discussions focus on when to trigger compaction and how to summarize context. This pattern addresses the neglected downstream question: what happens to the agent's behavior immediately after compaction strips its working memory? Without explicit recovery instructions, a compacted agent may hallucinate its current state, repeat completed work, or enter an undefined behavior mode.

By externalizing critical state to files (state JSON, git history, PR metadata), the pattern ensures that the information the agent needs to resume is never solely in conversation history. The conversation is treated as ephemeral; durable state lives in the filesystem. This is the difference between "compaction-aware" (knowing it happens) and "compaction-resilient" (having a recovery path).

## Why People Are Using It

Observed in [AutoGPT](https://github.com/significant-gravitas/autogpt) v0.5.0 — see [[autogpt-analysis]] for structural details.

The pattern is part of the fleet orchestration skill where multiple agents run long-lived sessions that routinely exceed context limits. Context compaction is not a theoretical risk — it is an expected operational event that happens multiple times per orchestration run. The recovery protocol is battle-tested against real compaction events in production coding workflows.

## Potential Alternatives

- Proactive state checkpointing: agent writes a structured state summary to a file at regular intervals, then reads it back after compaction. More complete than relying on external tools but adds write overhead.
- Session restart with briefing: kill the compacted session and start a fresh one with a pre-built briefing document. Cleaner but loses any in-progress tool state.
- Extended context windows: use models with larger context to avoid compaction entirely. Avoids the problem but does not eliminate it for very long tasks.

## Potential Improvements

- Structured recovery validation: after running the recovery protocol, the agent summarizes what it believes its current state is and compares against the state file — catching recovery errors early.
- Recovery confidence scoring: the agent assesses how confident it is in its recovered context and escalates to the orchestrator if confidence is below threshold.
- Incremental state externalization: rather than recovering all state post-compaction, continuously externalize key decisions to a running log that survives compaction.

## Potential Failure Modes

- **Stale state file**: If the state file was not updated before compaction, the recovered state may be behind the agent's actual progress, causing rework.
- **Recovery instruction loss**: If compaction is aggressive enough to trim the system prompt (unlikely but architecture-dependent), the recovery instructions themselves may be lost.
- **Incomplete recovery**: The filesystem provides facts (what files changed, what PR exists) but not intent (why the agent chose this approach). Post-recovery decisions may diverge from pre-compaction strategy.
- **Recovery loop**: If recovery itself consumes significant context and triggers another compaction, the agent enters a recovery loop without making progress.
