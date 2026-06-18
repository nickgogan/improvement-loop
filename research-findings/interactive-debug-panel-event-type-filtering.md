---
name: "Interactive Debug Panel with Event-Type Filtering"
summary: "Agent testing interfaces that provide a dual-panel view (conversation transcript + debug log) with filterable event types (agent thinking, agent messages, tool calls, model start/stop, idle states). Events cluster temporally and can be visualized as a timeline showing which event types dominated each phase of the conversation."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3 (Monitor)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-managed-agents-platform.md"
related_findings:
  - file: "structured-streaming-events-observability.md"
    rel: extends
  - file: "unified-tracing-opentelemetry-for-agents.md"
    rel: extends
  - file: "scheduled-task-dashboard-observability-layer.md"
    rel: same-problem
  - file: "session-as-append-only-event-log.md"
    rel: enabled-by
  - file: "anthropic-managed-agents-platform.md"
    rel: extends
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

## What It Is

A harness-level debug interface observed in Anthropic's managed agents platform that provides real-time and post-hoc inspection of agent sessions. The interface has two layers:

**Dual-panel view:**
- Left panel: conversation transcript (user messages + agent responses)
- Right panel: debug log showing raw API events in code form (type, process state, token counts)

**Event-type filtering:**
- Filter by specific event types: agent messages, thinking sections, tool calls, model start/stop events, idle states
- Example: "maybe I only want to filter the actual agent messages" or "only look at the thinking sections so I can see how long the thinking sessions actually took"

**Timeline visualization:**
- Visual bar showing which event types dominated each phase of the conversation
- Events appear in temporal clusters (e.g., running -> message -> model_start -> thinking -> model_stop -> idle)
- Segments color-coded by type, showing relative time allocation

**Token and cost metadata per event:**
- Each model interaction shows input tokens, output tokens, and cache writes
- Example: "Three input 409 output 27,044 cache writes probably a big chunk of its system prompt"

## Why It Matters

When agents fail, the question is always "what happened?" Existing tracing tools (OpenTelemetry, structured events) answer this at the infrastructure level. The debug panel answers it at the practitioner level -- you can visually see that the agent spent most of its time thinking vs. making tool calls, filter to only see tool call results, or inspect token usage per turn to understand cost drivers.

The timeline visualization is particularly valuable for identifying performance bottlenecks: if the agent is spending 80% of wall-clock time in "thinking" segments, the fix is different than if it's spending 80% waiting on tool call responses.

For harness builders, this establishes a UX baseline for agent debugging: conversation view (what the user sees) + event view (what the system did) + timeline view (when things happened) + filters (find what you're looking for).

## Why People Are Using It

Anthropic's managed agents platform ships this as a built-in feature. The practitioner describes it as having "full interpretability and accountability," noting that "every raw API event" is visible and "they put a tremendous amount of work in to make sure that this interface is something you could actually use for work."

## Potential Improvements

- Anomaly detection on event timelines (flag unusually long thinking phases or repeated tool call failures)
- Comparative timeline views across sessions (did the same agent behave differently on similar inputs?)
- Export debug data for offline analysis
- Automated cost optimization suggestions based on token usage patterns (e.g., "this agent's system prompt accounts for 95% of input tokens -- consider shortening it")

## Potential Failure Modes

- Information overload: complex agent sessions may produce event logs too dense to parse even with filtering
- Debug panel only shows what happened, not why -- the thinking content may not explain the reasoning sufficiently
- Performance impact: real-time debug views may slow down agent execution if event streaming is synchronous
- Filter categories may not match the user's mental model of what went wrong (e.g., no filter for "tool calls that returned errors")
