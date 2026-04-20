---
name: Monitor vs /loop — Event-Driven vs Time-Driven Background Execution
summary: Claude Code's Monitor tool and /loop command solve overlapping problems with opposite triggering mechanisms. /loop fires a full API call on a fixed time interval (N minutes); Monitor fires only when
  a filter-matched event occurs in a background process stream. Monitor costs zero tokens between events; /loop incurs a full API call per iteration regardless of whether anything changed.
implementation_notes: When choosing between Monitor and /loop for a background watching task, default to Monitor if the watched system emits observable output (logs, stdout, file events). Use /loop only
  when no event stream exists and you need time-based polling as a fallback. This distinction directly affects token budget in any long-running MetaSystem session.
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Plan)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-code-monitor-tool-event-driven.md
proposals: []
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
related_findings:
- file: claude-code-loop-in-session-cron-scheduling.md
  rel: contrasts-with
- file: claude-code-monitor-tool-event-driven-background.md
  rel: part-of
- file: agent-cost-blowup-mitigation-strategies.md
  rel: enabled-by
pipeline_status: raw
consumed_by: []
---
# Monitor vs /loop — Event-Driven vs Time-Driven Background Execution

## What It Is
Two distinct background execution primitives in Claude Code with different triggering models:

| Dimension | `/loop` | Monitor |
|-----------|---------|---------|
| Trigger | Time interval (every N minutes) | Event occurrence (filter match in process output) |
| API cost per check | Full API call each iteration | Zero tokens between events |
| Latency | Up to N minutes to detect | Near-real-time (process stdout lag only) |
| Best for | Anything without an observable event stream | Processes that emit logs or stdout |
| Overhead at idle | Continuous (every N minutes) | Zero |

## Why It Matters
The choice between Monitor and /loop has a direct, compounding effect on token budget. A `/loop 2m` watching a dev server costs a full API call every 2 minutes regardless of whether any error occurred. A Monitor watching the same server costs nothing until an error line appears. Over a 4-hour coding session, this difference is substantial.

## Why People Are Using It
The decision is often made by default (using /loop because it was the only option before Monitor shipped). Now that Monitor exists, the correct default is Monitor for any process that emits observable output.

## Potential Alternatives
- Combined approach: Monitor for event detection, /loop as fallback for polling endpoints with no event stream (e.g., external APIs that don't push events)

## Potential Failure Modes
- Using /loop where Monitor applies wastes tokens and adds latency
- Using Monitor where no reliable event stream exists produces silent false-negatives (no events = no awareness of problems)
