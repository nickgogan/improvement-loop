---
name: ACP Spawn — Cross-Tool Delegation
summary: OpenClaw's Agent Client Protocol enables spawning subprocesses for coding tasks using Claude Code, Codex, OpenCode, or Pi. Background mode with session monitoring. Multi-AI-tool orchestration at
  runtime — the agent delegates to specialized coding tools rather than doing everything itself.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
## What It Is

OpenClaw implements an Agent Client Protocol (ACP) that enables the primary agent to spawn subprocesses using external AI coding tools — Claude Code, Codex, OpenCode, or Pi. These subprocesses run in the background with session monitoring capabilities (poll status, read logs, kill if needed).

Rather than the agent attempting all tasks directly, ACP enables runtime delegation: complex refactoring goes to Claude Code, quick edits go to Codex, and so on. The primary agent acts as an orchestrator that selects the right tool for each sub-task and monitors execution.

This is multi-AI-tool orchestration at runtime — not just supporting multiple tools through static configurations (like BMAD's installer templates), but actively dispatching work to different tools during a single session based on task characteristics.

## Why It Matters

Most agent frameworks assume a single AI tool per agent session. The agent is Claude Code, or it is Codex, or it is Copilot — but not multiple tools simultaneously. This forces the agent to handle all tasks with one tool's strengths and weaknesses.

ACP breaks this assumption. If Claude Code is better at complex refactoring and Codex is faster for simple edits, an ACP-enabled agent can use each tool where it excels. This is the beginning of inter-tool coordination — agents that compose capabilities from multiple AI tools rather than being bound to one.

As AI coding tools specialize (some for speed, some for accuracy, some for specific languages), the ability to delegate across tools becomes a strategic capability.

## Why People Are Using It

Observed in [OpenClaw](https://github.com/openclaw/openclaw) v2026.4.5 — see [[openclaw-analysis]] for structural details.

The protocol includes background mode and session monitoring (poll, log, kill), indicating this is designed for production use, not just proof-of-concept. The support for 4+ external tools suggests active experimentation with multi-tool workflows.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Single-tool deep integration | Optimize for one AI tool and use it for everything | When one tool is sufficient and the complexity of multi-tool orchestration is not justified |
| Human-driven tool selection | User manually switches between tools for different tasks | When task-tool mapping requires human judgment and automated delegation is unreliable |
| MCP-based tool federation | Use Model Context Protocol to expose tools from multiple providers through a unified interface | When the tools can be accessed as MCP tools rather than spawned as subprocesses |
| Pipeline-based handoff | Sequential tool handoff — tool A produces output, tool B refines it | When the workflow is linear rather than parallel |

## Potential Improvements

- Define a task-tool matching heuristic — which characteristics of a task determine which tool should handle it?
- Explore error handling and fallback — if the delegated tool fails, does the primary agent retry with a different tool?
- Measure the overhead of subprocess spawning and monitoring vs. the benefit of tool specialization

## Potential Failure Modes

- **Orchestration overhead**: Spawning, monitoring, and collecting results from subprocesses adds latency and complexity that may exceed the benefit of tool specialization
- **Context loss at delegation boundary**: The spawned tool starts with a fresh context; important context from the primary agent's session may not transfer, leading to suboptimal execution
- **Tool version fragility**: ACP depends on specific tool CLIs and their interfaces; tool updates may break the spawning protocol
- **Cost multiplication**: Running multiple AI tools for a single task multiplies API costs; the orchestrator itself also consumes tokens for dispatch decisions
- **Debugging complexity**: When a delegated task fails, diagnosing whether the failure is in the orchestrator's dispatch decision, the delegation protocol, or the target tool is difficult
- **Security surface expansion**: Spawning external processes with user data creates additional attack surfaces and permission management challenges
