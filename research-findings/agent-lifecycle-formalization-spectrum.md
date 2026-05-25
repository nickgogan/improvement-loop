---
name: Agent Lifecycle Formalization Spectrum
summary: 'Four repos formalize agent lifecycle beyond running/done: Beads (state machine + Witness), Paperclip (heartbeat cycle), OpenClaw (Dreaming phases), DeerFlow (middleware lifecycle). Each formalizes
  a different facet: liveness, work cycles, memory consolidation, resource management.'
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: agent-state-machine-with-witness-monitoring.md
  rel: extends
- file: identity-depth-correlates-with-persistence.md
  rel: extends
- file: heartbeat-execution-model.md
  rel: extends
- file: dreaming-memory-consolidation.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: work-disavowal-failure-mode-context-limit-cheating.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-20'
pipeline_status: synthesized
consumed_by:
  - agent-design-patterns.md
---

## What It Is

A cross-repo comparison finding: four repos formalize agent lifecycle beyond simple binary state (running or not), each addressing a different facet:

1. **State machine + Witness** (Beads) — Formal FSM (idle→spawning→running→done/stuck/dead/stopped) with an external Witness monitor that tracks heartbeats and can declare agents dead. Focuses on liveness monitoring and state transitions.

2. **Heartbeat cycle** (Paperclip) — Wake→check→work→exit cycle with CEO delegation model. Focuses on periodic work execution and organizational structure.

3. **Dreaming phases** (OpenClaw) — Light→Deep→REM phases for memory consolidation during agent idle time. Focuses on memory management between active sessions.

4. **Middleware lifecycle** (DeerFlow) — SandboxMiddleware acquires/releases resources per turn; MemoryMiddleware queues/summarizes post-agent. Focuses on resource management and cleanup.

## Why It Matters

Most agent systems have implicit lifecycle (process alive or not). Production agent systems need richer models because agents can get stuck (Beads), need periodic maintenance (Paperclip), accumulate memory debt (OpenClaw), or leak resources (DeerFlow). The four facets are complementary — a complete lifecycle model would address all of them.

## Why People Are Using It

Cross-repo observation across 14 analyzed repos — see [[cross-repo-comparison]] for structural details. Observed in [Beads](https://github.com/gastownhall/beads), [Paperclip](https://github.com/nicholasgriffintn/paperclip), [OpenClaw](https://github.com/openclaw/openclaw), and [DeerFlow](https://github.com/bytedance/deer-flow).

## Potential Alternatives

- Binary lifecycle (running or not — simplest, fragile)
- Process-level monitoring (OS PID/health checks — no semantic awareness)
- Supervisor patterns (Erlang/OTP — heavy infrastructure)

## Potential Improvements

Combine all four facets: state machine for transitions (Beads) + periodic work cycles (Paperclip) + idle-time memory consolidation (OpenClaw) + per-turn resource management (DeerFlow). MetaSystem's agents currently have no formal lifecycle model.

## Potential Failure Modes

- Over-formalization adds complexity without benefit for simple agents
- State machine transitions can be hard to debug
- External monitors (Witness) add infrastructure requirements
