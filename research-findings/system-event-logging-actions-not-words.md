---
name: System Event Logging (Actions, Not Just Words)
summary: A structured log of agent actions (context loaded, registry init, routing decisions, tool executions, permission grants) distinct from the conversation transcript, enabling post-hoc auditing, debugging,
  and behavioral analysis.
implementation_notes: MetaSystem's System Log (DD-59) captures operational events at the system level. Extending this to agent-level action logging would close the observability gap.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropics-2-5-billion-leak-12-critical-pieces.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: session-as-append-only-event-log.md
  rel: same-problem
- file: structured-streaming-events-observability.md
  rel: same-problem
- file: workflow-state-vs-conversation-state.md
  rel: same-problem
- file: unified-tracing-opentelemetry-for-agents.md
  rel: extended-by
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
- rules/system-event-logging-actions-not-words.md
---
# System Event Logging (Actions, Not Just Words)

## What It Is
Log what the agent DID, not just what it SAID. The history log records: context loaded, registry initialization, routing decisions, tool executions, permission grants. Events are categorized and structured, enabling reconstruction of agent behavior and auditing.

## Why It Matters
Conversation logs show what was discussed; action logs show what happened. Without action logging, debugging requires inferring behavior from conversation context. This is foundational for auditing any agent system.

## Why People Are Using It
Anthropic's production Claude Code. Nate B Jones: "easy to add now; expensive to retrofit."

## Potential Alternatives
Conversation log parsing. Manual observation. Tool-level logging (each tool logs its own invocations).

## Potential Improvements
Structured query interface for action logs. Anomaly detection on action patterns. Action replay for debugging.

## Potential Failure Modes
Log volume for long sessions. Privacy concerns if action logs capture sensitive data. Log rotation and retention policies needed.

## Extraction Note — 2026-04-19
Extracted as **rule**: [[system-event-logging-actions-not-words.md]] in `extracts/rules/`
