---
title: "Scheduled Job Config Schema Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "scheduled-skill-chaining-with-file-based-activation"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "autonomous-scheduled-agent-operation.harvest-queue"
identification_report: "autonomous-scheduled-agent-operation.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams running scheduled or cron-driven agent workflows composed of more than one chained step"
    - "local-first automation setups with no dedicated infrastructure (no VPS, no cloud scheduler service) that rely on the OS's native scheduler"
    - "anyone building a status dashboard or health view over several recurring automated jobs"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — the config file can be edited or deleted without touching the skills or scripts it references; toggling the activation flag off pauses the job with no other side effects"
  auditability: "medium — the last-run timestamp and status fields give a per-job audit trail if the runner reliably updates them after every attempt; without a dashboard or log consumer reading this data, the trail exists in the file but isn't surfaced anywhere"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Identified by a practitioner as a natural next step after running file-based scheduled jobs without a standard schema — not yet built or formally adopted anywhere cited in the source material."
contract:
  preconditions: "An OS-level scheduler (cron, launchd, Task Scheduler, or equivalent) invokes a wrapper script or headless agent runner on a fixed interval. Every skill or script named in a job's chain exists and is independently invocable outside the scheduler. The runner has write access back to this file (or an adjacent per-job log) to record run outcomes."
  invariants: "Every scheduled job has exactly one config file conforming to this schema. The activation flag is read before each scheduled invocation; the runner MUST NOT execute the skill chain when the flag is off. The last-run timestamp and status fields are updated after every attempted run — success or failure — and are never left stale from a prior run."
  governance: "Owner: whoever maintains the scheduling wrapper/runner. Adding, removing, or reordering a scheduled job is a config-file edit, not a code change. If a scheduled-task dashboard is built, this schema is its read contract — the dashboard should not need a second source of truth for job state."
  recovery: "If the activation flag is malformed or missing, treat the job as inactive (fail closed) and surface a validation warning — never silently run on ambiguous config. If last-run status shows repeated failures, halt the job or flag it for human review rather than continuing to retry indefinitely; this schema records status but does not itself define retry policy or mid-chain error propagation, which the source material flags as an open gap."
tags:
  - "extracted-artifact"
  - "template"
---

# Scheduled Job Config Schema Template

**Source:** [[scheduled-skill-chaining-with-file-based-activation]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{JOB_NAME}}` | string | Human-readable identifier for the scheduled job. Unique within the job store. |
| `{{SCHEDULE}}` | string (cron expression) | When the job runs, in standard cron syntax (or the native scheduler's equivalent — launchd plist interval, Task Scheduler trigger). |
| `{{SKILL_CHAIN}}` | ordered list of strings | The skills or scripts to run in sequence for one job execution. A single-entry list is a plain scheduled prompt; a multi-entry list is a chained pipeline where each step's output feeds the next step's input. |
| `{{ACTIVE}}` | boolean | Whether the scheduler should run this job on its next scheduled tick. `false` skips the job without deleting its config. |
| `{{LAST_RUN_TIMESTAMP}}` | ISO-8601 datetime or null | When the job last attempted a run. Written by the runner, not the job author. `null` before the job has ever run. |
| `{{LAST_RUN_STATUS}}` | enum: `success` \| `failed` \| `partial` \| `never-run` | Outcome of the most recent attempt. Written by the runner. `partial` covers chains where an early step succeeded but a later step failed. |

## Body

```yaml
job_name: "{{JOB_NAME}}"
schedule: "{{SCHEDULE}}"
skill_chain:
  - "{{SKILL_CHAIN[0]}}"
  - "{{SKILL_CHAIN[1]}}"
  # ... one entry per chain step, in execution order
active: {{ACTIVE}}
last_run:
  timestamp: "{{LAST_RUN_TIMESTAMP}}"
  status: "{{LAST_RUN_STATUS}}"
```

One file per scheduled job, typically stored in a flat `jobs/` (or equivalent) config directory that the scheduler wrapper scans on each tick.

## Usage

The OS-level scheduler (cron/launchd/Task Scheduler) fires a wrapper script or headless agent runner on its own interval — often more frequent than any individual job's own `schedule` (e.g., the wrapper runs every 15 minutes and checks each job file to decide whether *this* tick is that job's due time). For each job config file the wrapper finds:

1. Parse `active`. If `false`, skip this job entirely — no chain execution, no `last_run` update.
2. Parse `schedule` and compare against the current tick. If not due, skip.
3. If due and active, execute each entry in `skill_chain` in order, feeding each step's output into the next.
4. On completion (or failure at any step), write back `last_run.timestamp` (now) and `last_run.status` (`success` if every step completed, `failed` if the chain aborted, `partial` if some but not all steps completed).

A scheduled-task dashboard, if built, reads every job file in the directory and renders `job_name`, `schedule`, `active`, and the `last_run` block as a status table — this schema is written to be that dashboard's entire read contract, with no second data source needed.

## Variation Axis

- **Chain length.** `skill_chain` with one entry is a plain single-prompt scheduled job (the pre-pattern baseline); two or more entries is the chained-pipeline pattern this template is optimized for.
- **Schedule cadence.** Daily, weekly, or fixed-interval jobs all use the same schema — only the cron expression's shape changes.
- **Self-updating vs externally-audited.** In the simplest deployment, the runner itself writes back `last_run` on every attempt (self-updating). A stricter deployment could have a separate watchdog process verify and correct `last_run` independently, catching cases where the runner crashed before writing its own status.
