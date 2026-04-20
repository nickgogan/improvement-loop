---
name: Structured Streaming Events for System Observability
summary: Typed streaming events (message_start, command_match, tool_match, crash with reason) that communicate agent system state to external consumers for real-time observability and post-mortem analysis.
implementation_notes: ''
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropics-2-5-billion-leak-12-critical-pieces.md
- multi-agent-orchestration-production-playbook-nick.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
related_findings:
- file: system-event-logging-actions-not-words.md
  rel: same-problem
- file: unified-tracing-opentelemetry-for-agents.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---
# Structured Streaming Events for System Observability

## What It Is
Instead of treating streaming purely as token output, the system emits typed events: message_start, command_match, tool_match, and crash events (with a reason field). These events communicate system state to external consumers. Crash events include a reason field, functioning as a "black box" for post-mortem analysis.

## Why It Matters
Without structured events, debugging agent systems requires reading raw conversation logs. Typed events enable real-time dashboards, automated alerting, and structured post-mortems.

## Why People Are Using It
Anthropic's production Claude Code. The crash event with reason field is particularly valuable for diagnosing failures.

## Potential Alternatives
Unstructured logging with post-hoc parsing. Application Performance Monitoring (APM) tools. Manual observation.

## Potential Improvements
Custom event types for domain-specific monitoring. Event aggregation for multi-agent systems. Event-driven triggers (auto-retry on specific crash types).

## Potential Failure Modes
Event flood in verbose mode. Storage costs for high-volume event streams. Observer effect — monitoring overhead affecting performance.
