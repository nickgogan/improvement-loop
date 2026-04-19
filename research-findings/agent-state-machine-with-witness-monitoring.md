---
name: Agent State Machine with Witness Monitoring
summary: Formal state machine for agent lifecycle (idle→spawning→running→done/stuck/dead/stopped) with an external Witness monitor that tracks heartbeats and can set terminal states. Agents cannot declare
  themselves dead — separation of monitoring from execution.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
---

## What It Is

A formal state machine for agent lifecycle management with clearly defined states (idle, spawning, running/working, done, stuck, dead, stopped) and an external Witness system that monitors agent heartbeats. The key design decision: agents can set most of their own states (running, stuck, stopped, done) but **cannot** set themselves to `dead` — only the Witness can do that via heartbeat timeout detection. This creates a separation between execution and monitoring.

## Why It Matters

Most agent systems have implicit lifecycle states (running or not running). A formal state machine enables: (1) explicit handling of stuck/dead states, (2) external monitoring without agent cooperation, (3) recovery workflows triggered by specific state transitions, (4) audit trails of agent lifecycle events. The Witness pattern specifically addresses the problem of agents that hang or crash silently.

## Why People Are Using It

Observed in [Beads](https://github.com/gastownhall/beads) v1.0.2 — see [[beads-analysis]] for structural details. Beads implements agent beads as first-class issue types with state machine semantics. The Witness monitors heartbeats and can set `dead` state. Role beads define agent capabilities, referenced by agent beads via a `role` slot.

## Potential Alternatives

- Simple process monitoring (is the process alive or not)
- Health check endpoints (HTTP-based liveness probes)
- Supervisor processes (Erlang/OTP style)

## Potential Improvements

Could be extended with state transition hooks (trigger actions on specific transitions) and state history for post-mortem analysis.

## Potential Failure Modes

- Heartbeat timeout too aggressive → premature `dead` declarations
- Heartbeat timeout too lenient → slow detection of stuck agents
- State machine complexity grows with new states
