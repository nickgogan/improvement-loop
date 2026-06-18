---
title: "Context Degradation at 40-50% Utilization Threshold"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "context-degradation-40-50-percent-threshold"
extraction_date: "2026-05-24"
last_change_session: 103
last_change_sl: "session-103-codifier-complete-extract-artifacts-write-phase"
identification_report: "2026-05-24-identification-report.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Developers or operators running multi-step agent workflows where output quality and plan fidelity matter across the full session"
    - "Orchestrator agents that manage sequences of subtasks and must decide when to dispatch work to subagents vs. continue in the current session"
    - "Anyone designing the session management policy for a long-running agent harness where context accumulates across tool calls, file reads, and task outputs"
    - "Teams observing inconsistent output quality in long agent sessions and investigating whether context utilization is a contributing factor"
  platform_coupling: "specific:Claude"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — adjusting the utilization threshold and dispatch policy is a configuration change; no data is at risk"
  auditability: "Low — context utilization percentage is observable per session if the harness exposes it, but verifying that the rule was followed requires logging of session utilization at each dispatch point."
  evidence_strength: "Low"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "An agent or orchestrator session is being used for complex work requiring reasoning quality, plan fidelity, or multi-step output. The harness provides some mechanism to check or estimate context window utilization. The work can be decomposed into phases or tasks that can be dispatched to fresh sessions."
  invariants: "Plans are scoped to 2-3 tasks maximum per session. Context utilization is checked before each new phase or task addition. Work that would push utilization to or past 40% is dispatched to a fresh session with a handoff summary. The 40% threshold is treated as the effective quality ceiling until stronger evidence establishes a different threshold."
  governance: "Owner: whoever designs the orchestrator session management policy. The threshold (40%) is an observed heuristic — if controlled measurements establish a different threshold, the owner should update this rule with the observed value and evidence. The rule applies to quality-sensitive work; simple file edits or deterministic operations may tolerate higher utilization."
  recovery: "If a session exceeds 40% utilization before work is complete: (1) immediately compact or summarize session context, (2) create a handoff summary capturing current state, completed work, and remaining tasks, (3) dispatch remaining tasks to a fresh session. Do not attempt to improve quality by retrying within the same degraded session."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
---

# Context Degradation at 40-50% Utilization Threshold

**Source:** [[context-degradation-40-50-percent-threshold]]
**Source (additional):** [[proactive-compaction-before-intelligence-degradation]]
**Form:** rule
**Extraction date:** 2026-05-24

## Condition

An AI agent or orchestrator session accumulates context through conversation turns, file reads, tool outputs, and in-progress task state. The session approaches 40-50% of the model's context window capacity. The session is being used for complex tasks requiring plan fidelity, multi-step reasoning, or high-quality output.

## Action

**Required:** Treat 40% context utilization as the effective planning ceiling for quality-sensitive work, not 80%. When designing plans or phases, scope each unit of work to complete before the orchestrating session reaches the 40% threshold.

**Required:** Limit active plans to a maximum of 2-3 tasks per session. When a task set would push utilization past 40%, dispatch remaining tasks to fresh context sessions rather than continuing in the current session.

**Required:** Use fresh context per phase for complex multi-phase work. Each phase should begin in a context where prior session accumulation does not yet create quality pressure.

**Required:** Treat natural task boundaries (phase completion, post-test-pass, after a successful tool call sequence where next-step direction is clear) as **checkpoint compaction triggers** — independently of utilization percentage. Compact proactively at these stable checkpoints while the model is still sharp, rather than waiting for utilization pressure to force compaction when the model is least capable of producing a quality summary. The two triggers are complementary: the 40% utilization ceiling caps by quantity; the checkpoint trigger caps by quality opportunity. Either trigger fires a compaction or fresh-session dispatch.

**Forbidden:** Continuing to add tasks or expand scope in a session that has already reached or exceeded 40% utilization for work requiring reasoning quality or plan adherence. Assuming that the technical 80% limit is the effective quality limit. Using a single long-running orchestrator session to execute a full multi-phase plan without dispatching to fresh context between phases. Deferring compaction to autocompact or near-capacity pressure when proactive checkpoints are available — compaction quality degrades precisely as context load increases.

## Boundary

Enforced at **plan construction** — when scoping a plan or set of tasks, estimate context utilization and cap at 2-3 tasks if the session will reach 40% before completion. Also enforced at **phase dispatch** — before starting a new phase in an existing session, check utilization and dispatch to a fresh session if at or near 40%.

## Enforcement

- **Mechanism:** Context utilization is checked before each new phase or task addition. If utilization is at or above 40%, the task is dispatched to a fresh session rather than appended to the current session.
- **Check:** `(tasks_per_plan <= 3) AND (new_phase_dispatched_when_utilization >= 0.40 == true)`.
- **Violation response:** If a session has already exceeded 40% utilization for quality-sensitive work: compact or summarize context immediately, dispatch remaining work to a fresh session with a concise handoff summary, and do not attempt to recover quality by continuing in the degraded session.

## Rationale

Practitioners have documented that Claude exhibits "completion mode" behavior — rushing responses, cutting corners, losing plan fidelity — at approximately 40-50% context window utilization, well before the technical 80% capacity limit. The degradation is triggered by the model perceiving context mounting, not by actual capacity exhaustion. The orchestrator-delegates-to-headless pattern is not merely an architectural preference; it is a quality requirement. Note: this threshold is practitioner-observed without controlled measurement and may be task-dependent or model-version-dependent — treat it as a conservative heuristic, not a precise limit.

The checkpoint-based compaction trigger complements the percentage ceiling ([[proactive-compaction-before-intelligence-degradation]]). Anthropic's explicit recommendation: "compact proactively at stable checkpoints (task boundary, post-test-pass), not reactively at capacity pressure." The rationale is direct: "model is at its least intelligent point when compacting" — autocompact fires when the model has the least headroom and the most to summarize, producing the worst summaries. A 1M context window is not a license to defer compaction; it defers the eventual compaction further, making it worse. Proactive compaction at moments of maximum clarity (unambiguous test results, successful tool calls, confirmed plan direction) produces quality summaries because the model is still sharp and the next-phase direction is clear. The two triggers in this rule — utilization ceiling and checkpoint opportunity — implement different sides of the same quality-preservation goal: the ceiling prevents accumulating past the quality cliff; the checkpoint exploits windows of maximum compaction quality.

## Contract

### Preconditions
An agent or orchestrator session is being used for complex work requiring reasoning quality. The harness provides some mechanism to estimate context window utilization. The work can be decomposed into phases dispatchable to fresh sessions.

### Invariants
Plans are scoped to 2-3 tasks maximum per session. Context utilization is checked before each new phase. Work that would push utilization past 40% is dispatched to a fresh session. The threshold is treated as the effective quality ceiling until stronger evidence updates it.

### Governance
Owner: whoever designs the orchestrator session management policy. The threshold is an observed heuristic — update with controlled measurement evidence when available. The rule applies to quality-sensitive work; deterministic operations may tolerate higher utilization.

### Recovery
If a session exceeds 40% utilization: (1) compact or summarize context, (2) create a handoff summary, (3) dispatch remaining tasks to a fresh session. Do not retry within the degraded session.
