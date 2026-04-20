---
name: Agent Teams — Shared Communication Channel Between Sub-Agents
summary: Extension of isolated sub-agent model adding a shared communication channel. Sub-agents can coordinate directly (e.g., frontend agent ↔ backend agent on API contracts) instead of routing all coordination
  through the orchestrator. Reduces orchestrator bottleneck.
implementation_notes: Design work needed on implementation mechanism (shared file vs message bus vs shared context). Dedicated tutorial video exists for implementation details.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- claude-code-works-better-when-you-do-this.md
- five-claude-code-agent-patterns.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
devil_advocate_role: 'Explicitly named role in agent team: one agent continuously challenges decisions made by all other sub-agents, acting as a senior/staff engineer. Practical example: review team of 4 specialized reviewers + 1 devil's advocate for PR review.'
related_findings:
- file: competitive-module-development-parallel-teams.md
  rel: same-problem
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: same-problem
- file: database-as-shared-memory-coordination.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
---
## What It Is

Agent Teams is an extension of the basic sub-agent orchestration pattern that adds a **shared communication channel** between agents that would otherwise operate in isolation. In the standard sub-agent model, each sub-agent has its own fresh context and communicates only with the orchestrator. In the Agent Teams model, sub-agents can also communicate with each other directly.

**Example:** A frontend agent building a UI component can communicate directly with the backend agent responsible for the API endpoint that component depends on — rather than routing all coordination through the orchestrator.

This is positioned as a step up from isolated sub-agents, enabling tighter cross-domain coordination on projects where multiple agents have interdependencies.

## Why It Matters

The isolated sub-agent model (each agent works independently, results merged by orchestrator) breaks down when agents have real-time interdependencies. Frontend and backend development, for example, requires constant negotiation over API contracts. Forcing all of this coordination through an orchestrator creates a bottleneck and risks the orchestrator losing track of the current state of each agent's work.

A shared communication channel allows agents to resolve interdependencies directly, reducing orchestrator load and keeping coordination closer to the actual work.

## Why People Are Using It

- Mentioned as a distinct tip in source-002 (Eric Tech), separate from basic sub-agents
- Framed as "extending" sub-agents — implies the speaker has used both models and found this to be an upgrade
- Dedicated tutorial video exists on the Eric Tech channel, suggesting enough practitioner interest to warrant standalone content

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Isolated sub-agents + orchestrator merge | Standard pattern; orchestrator handles all coordination | For tasks with clear, non-overlapping domain boundaries |
| gstack sequential data flow | Sequential handoffs between specialist roles | When coordination is linear and doesn't require real-time cross-agent negotiation |
| Shared state file (MD/JSON) | Agents communicate via a shared file rather than a channel | Simpler to implement; less real-time but lower complexity |

## Potential Improvements

- Define a standard message schema for the shared communication channel
- Explore whether the channel can be implemented as a shared MD file (low-tech) vs. a dedicated message bus (higher-complexity)
- Determine how the orchestrator monitors the channel and intervenes when agent communication breaks down

## Potential Failure Modes

- **Channel noise**: Agents communicating freely may generate irrelevant cross-talk that consumes tokens without adding value
- **Circular dependencies**: Agent A waiting on Agent B waiting on Agent A — deadlock risk in loosely coupled systems
- **Channel as context bloat**: If the shared channel is loaded into each agent's context, it may accelerate context degradation
- **Coordination overhead**: More complex than isolated sub-agents; may not be worth it for tasks with clear domain separation
- **Implementation opacity**: The source video is high-level; the actual implementation mechanism is unclear without the dedicated tutorial
