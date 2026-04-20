---
notion_id: 3351e08b-9b34-812d-bad2-d8813aadae7c
name: Claude Code /loop -- In-Session Cron Scheduling
summary: 'GA since v2.1.71 (March 7, 2026). `/loop [interval] [prompt]` creates persistent background tasks within a session, up to 50 concurrent, auto-expire after 3 days. Three scheduling surfaces: /loop
  (CLI, session-bound), Desktop Tasks (GUI, machine-bound), Cloud Scheduled Tasks (Anthropic infrastructure, machine-off). Use cases: PR babysitting, deployment monitoring, CI pipeline polling, code quality
  scans, daily summaries. Can invoke other slash commands.'
implementation_notes: 'Transforms Claude Code from a ''one-off chat assistant'' into a ''continuously running background worker.'' Directly relevant to the KB''s Improvement Loop and Record-and-Schedule
  patterns. 3.5M views on launch announcement tweet. Source: https://code.claude.com/docs/en/scheduled-tasks'
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-codes-leak-changes-everything.md
proposals: []
date_discovered: '2026-04-01'
last_updated: 2026-04-08
related_findings:
- file: agent-cost-blowup-mitigation-strategies.md
  rel: enabled-by
- file: monitor-vs-loop-event-driven-vs-time-driven.md
  rel: contrasts-with
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---
# Claude Code /loop -- In-Session Cron Scheduling

## What It Is
Cron-style task scheduling native to Claude Code, GA since v2.1.71. Three scheduling surfaces:
1. **`/loop [interval] [prompt]`** -- CLI-based, session-bound, up to 50 concurrent tasks, auto-expire after 3 days
2. **Desktop Scheduled Tasks** -- GUI-based, machine-bound, persistent across sessions
3. **Cloud Scheduled Tasks** -- Anthropic infrastructure, runs even when machine is off

## Why It Matters
Transforms Claude Code from a "one-off chat assistant" into a "continuously running background worker." The background devops agent pattern becomes practical.

## Why People Are Using It
Addresses the "constant supervision" bottleneck in agentic coding. Enables always-on autonomous monitoring and maintenance.

## Potential Failure Modes
Tasks expire after 3 days. 50-task session limit. All /loop tasks terminate on session close. Tasks run at low priority.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[in-session-cron-scheduling]] in `extracts/patterns/`
