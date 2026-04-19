---
title: "In-Session Cron Scheduling"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "claude-code-loop-in-session-cron-scheduling"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The agent runtime supports background task execution and can maintain multiple concurrent task contexts. Tasks are expressible as repeatable prompts with bounded execution time."
  invariants: "Scheduled tasks have explicit expiration. Concurrent task limits are enforced. Task scheduling never bypasses the permission system."
  governance: "Task limits (concurrency, expiration) are configured per deployment context. Persistent scheduling surfaces (Desktop, Cloud) require explicit opt-in."
  recovery: "If a scheduled task fails repeatedly, it is suspended after a configurable failure count and reported to the user. Session-bound tasks terminate cleanly on session close."
tags:
  - "extracted-artifact"
  - "pattern"
---

# In-Session Cron Scheduling

**Source:** [[claude-code-loop-in-session-cron-scheduling]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent interactions are treated as one-shot request-response exchanges. Once a task completes, the agent is idle until the next human prompt. This forces humans to manually re-invoke the agent for recurring work -- monitoring deployments, polling CI pipelines, checking PR status, running periodic code quality scans. The human becomes the scheduler, which defeats the purpose of agent autonomy for predictable, repeatable tasks.

## Forces

- **Session ephemerality vs. task persistence.** Agent sessions are designed to start and stop. Recurring tasks need to outlive individual interactions but should not outlive their usefulness.
- **Resource control vs. autonomy.** Allowing agents to schedule arbitrary background work risks runaway token consumption, unbounded concurrency, and tasks that persist after they are no longer relevant.
- **Scheduling granularity.** Some tasks need session-scoped scheduling (terminate when I close the session). Others need machine-scoped persistence (survive session restarts). Still others need infrastructure-scoped persistence (run even when the machine is off).
- **Composability.** Scheduled tasks should be able to invoke existing skills and commands, not require purpose-built scheduling-specific implementations.

## Solution

**Provide three scheduling surfaces with increasing persistence, each appropriate for different task lifetimes.**

1. **Session-bound scheduling (`/loop [interval] [prompt]`):** CLI-based, tied to the current session. Up to 50 concurrent tasks. Auto-expire after 3 days. Tasks terminate on session close. This is the default for most recurring work -- monitoring, polling, periodic checks.

2. **Machine-bound scheduling (Desktop Tasks):** GUI-based, persistent across sessions but tied to the local machine. Appropriate for tasks that should survive session restarts but do not need to run when the machine is off.

3. **Infrastructure-bound scheduling (Cloud Tasks):** Runs on provider infrastructure. Appropriate for tasks that must execute regardless of local machine state -- daily summaries, scheduled deployments, overnight analysis.

**Key design properties:**
- Tasks are expressed as prompts, not code. Any prompt or slash command that works interactively works as a scheduled task.
- Concurrency is capped (50 per session) to prevent resource exhaustion.
- Auto-expiration (3 days for session-bound) prevents forgotten tasks from accumulating.
- Tasks run at low priority to avoid starving interactive work.

**Use cases:** PR babysitting (poll for review status, notify on merge conflicts), deployment monitoring (check health endpoints on interval), CI pipeline polling (watch for failures, summarize results), code quality scans (periodic lint/test runs), daily summaries (aggregate activity across repositories).

## Consequences

**Positive:**
- Transforms the agent from a request-response tool into a continuously running background worker.
- Eliminates human-as-scheduler for predictable recurring tasks.
- Three persistence tiers let users match task lifetime to actual need without over-committing.
- Prompt-based task definition means zero additional development to schedule existing capabilities.

**Negative:**
- Session-bound tasks terminate on session close, which can surprise users who expect persistence.
- 3-day auto-expiration requires re-creation for longer-running monitoring needs.
- 50-task concurrency limit may be insufficient for large-scale monitoring scenarios.
- Low-priority execution means scheduled tasks may be delayed when interactive work is active.
- Token cost of background tasks is continuous and can accumulate without active user awareness.

## Known Uses

- Claude Code `/loop` command, GA since v2.1.71 (March 7, 2026). 3.5M views on launch announcement.
- Desktop Scheduled Tasks and Cloud Scheduled Tasks as the machine-bound and infrastructure-bound tiers.
- Directly relevant to the MetaSystem Improvement Loop (periodic research scans) and Record-and-Schedule patterns.

## Contract

### Preconditions
The agent runtime supports background task execution and can maintain multiple concurrent task contexts without interfering with interactive work. Tasks are expressible as repeatable prompts with bounded execution time per invocation. The scheduling surface appropriate to the task lifetime is available (session, machine, or cloud).

### Invariants
Scheduled tasks have explicit expiration (3 days for session-bound; configurable for other tiers). Concurrent task limits are enforced and not bypassable. Task scheduling never bypasses the permission system -- each task invocation is subject to the same safety checks as interactive execution. Low-priority execution ensures interactive work is never starved by background tasks.

### Governance
Task limits (concurrency cap, expiration period) are configured per deployment context and reviewed when scaling needs change. Persistent scheduling surfaces (Desktop, Cloud) require explicit user opt-in -- session-bound is the default. Token consumption by scheduled tasks is trackable and attributable.

### Recovery
If a scheduled task fails repeatedly, it is suspended after a configurable failure count and reported to the user rather than retrying indefinitely. Session-bound tasks terminate cleanly on session close with no orphaned processes. If the concurrency limit is reached, new task creation fails with a clear error rather than silently queuing.
