---
name: Scheduled Task Dashboard Observability Layer
summary: A web dashboard that surfaces all scheduled Claude Code tasks (cron jobs, periodic checks) with visual activate/deactivate toggles, test-run buttons, last-run status indicators, and output log
  links. Separates scheduled task management from the terminal interface.
implementation_notes: Relevant to MetaSystem's periodic maintenance skills (watch-upstream, research-loop). A dashboard layer could surface skill execution status.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- stop-using-claude-code-in-terminal.md
related_findings:
- file: claude-code-loop-in-session-cron-scheduling.md
  rel: extends
- file: kairos-autonomous-background-daemon.md
  rel: extends
- file: conway-always-on-persistent-agent.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
pipeline_status: "raw"
consumed_by: []
---

# Scheduled Task Dashboard Observability Layer

## What It Is
A web-based dashboard that aggregates all scheduled Claude Code tasks -- cron jobs, periodic checks, recurring maintenance runs -- into a single visual interface. Each task shows activate/deactivate toggles, test-run buttons, last-run status indicators, and links to output logs. This is distinct from scheduling primitives; it is the observability and management layer that sits on top of them.

## Why It Matters
Without a centralized view, scheduled tasks become invisible infrastructure. Operators cannot tell which tasks are active, when they last ran, or whether they succeeded without checking individual cron entries or log files. This opacity compounds as the number of scheduled tasks grows, creating maintenance blind spots.

## Why People Are Using It
Practitioners running multiple periodic agent tasks (daily skill update checks, weekly activity digests, monthly learnings consolidation) need a single pane of glass to manage them. The dashboard reduces the cognitive overhead of remembering what is scheduled and provides quick intervention points when tasks fail or need temporary suspension.

## Potential Improvements
MetaSystem's periodic skills like watch-upstream and research-loop could benefit from a lightweight status view showing last execution time, success/failure state, and next scheduled run. This would make the improvement loop's operational health visible without terminal inspection.

## Potential Failure Modes
Dashboard becomes a maintenance burden itself if it requires manual registration of new tasks rather than auto-discovery. Also risks creating a false sense of control -- seeing green status indicators does not guarantee the task produced correct output, only that it ran without errors.
