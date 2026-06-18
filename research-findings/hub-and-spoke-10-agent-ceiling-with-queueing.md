---
name: "Hub-and-Spoke Sub-Agent Ceiling (10 Concurrent, Queued Beyond)"
summary: "Claude Code's sub-agent topology is strictly hub-and-spoke: sub-agents report only to the main agent and cannot communicate with each other. Hard limit of 10 concurrent sub-agents; additional tasks are queued. This creates a known bottleneck for tasks requiring inter-agent coordination, which is the explicit escalation trigger for agent teams."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "five-agentic-patterns-claude-code.md"
related_findings:
  - file: "sub-agent-context-isolation-for-parallel-complex.md"
    rel: "extends"
  - file: "builder-validator-chain-pattern.md"
    rel: "enables"
  - file: "agent-teams-shared-communication-channel.md"
    rel: "same-problem"
  - file: "five-pattern-complexity-escalation-ladder.md"
    rel: "enables"
  - file: "orchestrated-competition-n-sub-agents-solve-same.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

## What It Is

Claude Code's split-and-merge pattern enforces a strict hub-and-spoke topology with two hard constraints:

1. **No peer communication**: Sub-agents can only report back to the main agent. Sub-agent 1 and sub-agent 3 have no idea what each other are doing. All coordination must route through the main agent hub.

2. **10-agent concurrency ceiling**: Maximum 10 sub-agents run simultaneously. Any tasks beyond 10 are queued and dispatched as slots free up. Boris Cherny (Claude Code creator) has mentioned spinning up 15 sub-agents at a time, but only 10 execute concurrently.

The main agent acts as both dispatcher and aggregator: it analyzes a task, decomposes it into independent pieces, fans out to sub-agents, and merges results when they return. The user sees this as a single conversation — the parallelization is internal.

## Why It Matters

The 10-agent ceiling and no-peer-communication constraint together define the operational envelope for sub-agent architectures. For harness builders, these constraints matter for:

- **Work decomposition**: Tasks must be decomposable into pieces that can execute independently without cross-coordination. If pieces need to share state mid-execution, the hub-and-spoke model forces that state through the main agent, creating a bottleneck.
- **Batch sizing**: Tasks requiring more than 10 parallel units need to account for queuing latency.
- **Pattern selection**: When tasks genuinely require inter-agent communication, the hub-and-spoke ceiling is the explicit trigger for escalating to agent teams (which adds 4-7x token cost).

The builder-validator chain pattern works within this topology because it's sequential (build, relay through hub, validate) rather than concurrent coordination.

## Why People Are Using It

Split-and-merge is the sweet spot for most parallelizable tasks: cheaper than agent teams, more capable than manual operator coordination, and fully automatic. Common use cases include parallel research (one sub-agent per topic), parallel code review (one per file), and batch processing (one per input item).

## Potential Improvements

- Allow sub-agents to write to a shared scratchpad that other sub-agents can read (limited peer awareness without full communication)
- Expose the queue depth and estimated completion time to the user
- Dynamic ceiling based on available compute/token budget

## Potential Failure Modes

- Decomposing interdependent work into "independent" pieces leads to inconsistent outputs that the main agent must reconcile
- The main agent's merge step can itself consume significant context if 10 sub-agents each return large results
- Queued tasks beyond the 10-agent ceiling may become stale if earlier sub-agents' results change the relevant context
