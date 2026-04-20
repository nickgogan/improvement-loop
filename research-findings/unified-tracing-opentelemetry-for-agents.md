---
name: Unified Tracing (OpenTelemetry) for Agent Systems
summary: 'Standards-based telemetry linking every run: user request -> retrieval -> model calls -> tool calls -> output -> evaluation. Trace IDs assigned to all runs enable root-cause analysis with a structured
  error taxonomy: retrieval fail vs reasoning fail vs tool fail. ''If you can''t trace it, you can''t improve it.'''
implementation_notes: Extends the structured-streaming-events finding from Anthropic's internal implementation to a broader industry pattern. MetaSystem lacks any tracing infrastructure. When agents run
  autonomously (Kairos, background research), tracing becomes the primary debugging mechanism.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- multi-agent-orchestration-production-playbook-nick.md
related_findings:
- file: structured-streaming-events-observability.md
  rel: same-problem
- file: tool-gateway-security-boundary.md
  rel: same-problem
- file: system-event-logging-actions-not-words.md
  rel: extends
- file: mcp-enterprise-governance-gaps.md
  rel: enabled-by
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---
# Unified Tracing (OpenTelemetry) for Agent Systems

## What It Is
Layer 4 of production multi-agent systems. Standards-based telemetry (OpenTelemetry) that links every component of an agent run into a single trace: user request, retrieval calls, model calls (with prompts and completions), tool calls (with inputs and outputs), final output, and evaluation results. Each run gets a unique trace ID. The trace enables a structured error taxonomy: was the failure in retrieval (wrong documents), reasoning (model hallucination), or tools (API error)?

## Why It Matters
"If you can't trace it, you can't improve it." Multi-agent systems fail in ways that are impossible to diagnose without end-to-end tracing. The error taxonomy (retrieval fail vs reasoning fail vs tool fail) is critical because each failure type requires a different fix -- you cannot improve retrieval by changing the prompt or fix a tool error by changing the model.

## Why People Are Using It
Nick Gupta identifies observability as a non-negotiable production artifact, not an optional add-on. LangSmith is commonly used for cost/latency monitoring. The pattern draws from established observability practices (Datadog, Jaeger, Zipkin) applied to LLM-specific concerns.

## Potential Improvements
Automated failure classification using the error taxonomy. Cost attribution per trace segment. Anomaly detection on trace patterns to identify emerging failure modes before they impact users.

## Potential Failure Modes
Tracing overhead can impact latency. Storage costs for high-volume trace data. Privacy concerns when traces contain user data or model completions.
