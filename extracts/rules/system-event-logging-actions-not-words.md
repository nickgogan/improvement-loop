---
title: "System Event Logging — Actions, Not Just Words"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "system-event-logging-actions-not-words"
confidence: "MED"
tier: "guided"
reason_codes:
  - "deterministic-check"
  - "enforcement-boundary"
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Structured log format defined. Log storage location specified. Sensitive data handling policy exists."
  invariants: "Every tool call and routing decision is logged. Entries are structured, not free-text. Logs are append-only during a session."
  governance: "Owner: each system owns its own logs. Log format changes require review. No cross-system aggregation without authorization."
  recovery: "Logging failure: warn operator but do not block task. Missing logs: flag session as unauditable. Sensitive data in logs: purge, update policy, file IB item."
tags:
  - "extracted-artifact"
  - "rule"
---

# System Event Logging — Actions, Not Just Words

**Source:** [[system-event-logging-actions-not-words]]
**Form:** rule
**Extraction date:** 2026-04-19

## Condition

Any agent system, workflow, or automated pipeline where agent behavior needs to be auditable, debuggable, or reconstructable after the fact.

## Action

Agent systems MUST log structured action events, not just conversation history. Action logs record what the agent DID — tool executions, routing decisions, permission grants, context loads, registry initializations — as categorized, structured entries.

Conversation logs alone are insufficient. They show what was discussed, not what happened. Without action logging, debugging requires inferring behavior from conversational context, which is unreliable and time-consuming.

Minimum logged event categories:
- **Context events:** What context was loaded, from where, at what point.
- **Tool events:** Which tools were called, with what parameters, what was returned.
- **Decision events:** Routing choices, permission evaluations, gate outcomes.
- **State events:** Registry initialization, configuration changes, session lifecycle.

## Boundary

- **Agent systems in production:** Action logging is mandatory.
- **Development workflows:** Action logging is recommended for complex multi-step skills.
- **Session-scoped work:** MetaSystem's existing system-log entries (DD-59) serve as a manual action log at session granularity. This rule extends the principle to automated, per-event granularity where tooling supports it.

## Enforcement

- **Structural check:** Agent system specifications must include an "action logging" section defining what events are captured.
- **Format check:** Action log entries must be structured (not free-text prose). Minimum fields: timestamp, event category, event type, payload summary.
- **Completeness check:** At minimum, tool call events and decision events must be logged. Context and state events are recommended.

## Rationale

Anthropic's production Claude Code uses structured action logging. Nate B Jones: "easy to add now; expensive to retrofit." Without action logs, post-incident analysis of agent behavior requires reconstruction from conversation transcripts — a process that is slow, incomplete, and error-prone. Structured action logs enable: behavior reconstruction, audit trails, performance profiling, and regression detection.

### Known Risks

- Log volume for long sessions can become substantial. Implement log rotation and retention policies.
- Privacy concerns if action logs capture sensitive data (API keys, personal information in tool parameters). Sanitize sensitive fields before logging.
- Over-logging creates noise. Focus on decision-relevant events, not every minor state change.

## Contract

### Preconditions
- A structured log format is defined for the system (fields, categories, retention).
- Log storage location is specified and accessible.
- Sensitive data handling policy exists for the log context.

### Invariants
- Every tool call event is logged with parameters and outcome.
- Every routing/decision event is logged with the decision rationale.
- Log entries are structured, not free-text.
- Logs are append-only during a session (no retroactive modification).

### Governance
- **Owner:** Each system owns its own action logs.
- **Modification gate:** Log format changes require review to avoid breaking downstream consumers (audit tools, dashboards).
- **Cross-system:** No cross-system log aggregation without explicit authorization.

### Recovery
- If logging fails (disk full, format error): the agent task continues but a warning is surfaced to the operator. Logging failure must not block task execution.
- If logs are missing for a completed session: flag the session as "unauditable" in the system log.
- If sensitive data is found in logs: purge affected entries, update the sanitization policy, file an IB item for the gap.
