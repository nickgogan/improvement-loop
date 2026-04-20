---
name: Monitor Stream Filter vs Poll & Diff — Two Monitor Command Patterns
summary: Claude Code's Monitor tool generates two distinct command types depending on the data source. Stream filter (log tailing) is used for processes that emit real-time output (dev server, test runner);
  poll & diff is used for discrete data sources checked at an interval (API endpoints, databases), where events are generated only when the polled value crosses a threshold or changes.
implementation_notes: When instructing Claude Code to set up a monitor, the command type is inferred from context. Be explicit about whether the source is a live stream or a polled endpoint to get the correct
  command generated. Poll & diff monitors are appropriate for external APIs, stock prices, error rate metrics from monitoring systems.
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-code-monitor-tool-event-driven.md
proposals: []
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
related_findings:
- file: claude-code-monitor-tool-event-driven-background.md
  rel: part-of
- file: monitor-vs-loop-event-driven-vs-time-driven.md
  rel: part-of
pipeline_status: raw
consumed_by: []
---
# Monitor Stream Filter vs Poll & Diff — Two Monitor Command Patterns

## What It Is
When Claude Code writes a monitor command, it generates one of two pattern types:

**Stream Filter (log tailing)**
- Source: a process that continuously emits stdout (dev server, test runner, build system)
- Mechanism: pipe/grep the live output stream; each matching line is one event
- Latency: near-real-time — matches appear as the process emits them
- Example: `npm run dev` piped through a filter for `error|warn|failed`

**Poll & Diff**
- Source: a discrete data source polled at an interval (REST API, database query, metric endpoint)
- Mechanism: repeatedly fetch the value at interval N; compare to previous value or threshold; emit an event only when the condition is met
- Latency: up to N seconds (the polling interval)
- Example: price API polled every 30 seconds, event fired only when price drops below threshold

## Why It Matters
The distinction matters when prompting Claude Code to set up a monitor. Specifying the wrong type leads to either a broken command (trying to tail a REST endpoint) or an unnecessarily complex command (poll-and-diff on a process that already emits stdout).

## Why People Are Using It
Poll & diff unlocks the Monitor pattern for external systems that don't push events — stock prices, deployment health checks, business metrics — without requiring the user to write a custom polling script.

## Potential Failure Modes
- Poll & diff at aggressive intervals adds network load and may hit rate limits on external APIs
- Stream filter on a low-traffic process may appear broken (no events for a long time) even when functioning correctly
- No built-in deduplication — if the same threshold condition persists, each poll cycle that matches will fire a new event
