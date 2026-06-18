---
name: Event Bus Observability — Three Architectural Approaches
summary: Four repos implement typed event systems for agent observability via three distinct approaches — dedicated bus (CrewAI, DeepTutor), event sourcing (Letta, ADK-Python), and extension hooks (Pi Agent).
  All enable external monitoring without modifying core logic. Key design tension is bus (simple pub/sub) vs event-sourcing (events ARE state, enables replay) vs hooks (minimal coupling).
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: structured-streaming-events-observability.md
  rel: extends
- file: event-to-llm-context-orchestration.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: raw
consumed_by: []
---

## What It Is

Three distinct architectural approaches to agent observability via typed events, observed across 4+ repos:

1. **Dedicated event bus** (CrewAI: singleton `crewai_event_bus` with 17+ typed events + OpenTelemetry; DeepTutor: StreamBus with fan-out) — publish/subscribe with typed event schemas. Simple, decoupled, but events are ephemeral notifications.

2. **Event sourcing** (Letta: events as ground truth + EventActions; ADK-Python: Plugin system with callbacks) — events ARE the authoritative state record. Enables replay, time-travel debugging, and derived views. Most powerful but most complex.

3. **Extension hooks** (Pi Agent: EventBus for inter-extension communication with 30+ event types) — minimal coupling via hook points. Extensions register interest in specific lifecycle events. Lightest-weight but least structured.

## Why It Matters

Agent observability is converging as a requirement but the implementation approach carries significant architectural consequences. Bus-based is simplest (add subscriber, get notifications) but loses events when no one is listening. Event-sourcing is most powerful (full audit trail, replay, time-travel) but adds storage and complexity overhead. Hooks are lightest but require extensions to understand the event schema. The choice cascades into debugging capabilities, audit compliance, and system evolution.

## Why People Are Using It

Observed across 4+ repos in the cross-repo structural comparison — see [[cross-repo-comparison]] for details. The convergence signals that as agent systems grow in complexity, printf-debugging and log files become insufficient. Typed events provide the structured observability layer needed for production monitoring, debugging, and compliance.

## Potential Alternatives

| Alternative | When to Prefer |
|---|---|
| Structured logging (JSON lines) | Simple systems where grep-ability matters more than type safety |
| Distributed tracing (OpenTelemetry) | When integrating with existing APM infrastructure |
| No observability | Prototypes and single-turn agents without persistence |

## Potential Improvements

- Assess whether event sourcing could be layered on top of a simple bus (bus for real-time, event store for persistence)
- Identify minimum viable event schema for agent observability (what events are always useful vs. domain-specific)

## Potential Failure Modes

- Event schema becoming a coupling point (changing event shape breaks all subscribers)
- Event volume overwhelming storage in high-throughput multi-agent systems
- Event sourcing complexity not justified for simple agents that don't need replay
