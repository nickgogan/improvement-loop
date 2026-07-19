---
title: "Default to Event-Driven Watching Over Time-Based Polling"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "monitor-vs-loop-event-driven-vs-time-driven"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "designing-agent-tools.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agents, harness authors, or engineers choosing between an event-driven watch primitive and a time-based polling primitive for a background monitoring task"
    - "long-running or unattended sessions that observe a subprocess, dev server, deployment, or other subordinate process and must react to its state changes"
    - "designers of a tool surface that offers (or could offer) both a filter-triggered watcher and a fixed-interval poller"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "low — switching a watch task from one primitive to the other after initial setup requires reconfiguring how the watched system's output is captured (adding an event filter/subscription for event-driven mode, or removing it in favor of a timer for time-driven mode); no external state or downstream contract needs migration, but the watch logic itself must be rewritten"
  auditability: "high — the chosen primitive is visible in the watch task's own configuration (an event filter/subscription vs. a fixed-interval timer), and misuse is independently observable: a time-driven watch against a system with observable output shows up as a fixed per-tick cost in usage/billing logs regardless of whether state ever changed"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A background or unattended watching task is being designed, configured, or reviewed — one that observes an external or subordinate system (a subprocess, dev server, deployment pipeline, external API, file system) and must react when its state changes. The environment offers, or could offer, both an event-driven watch primitive (fires only on a filter-matched event) and a time-based polling primitive (fires on a fixed interval regardless of whether anything changed)."
  invariants: "When the watched system emits observable output (logs, stdout, structured events, file-system change notifications), the watch task uses the event-driven primitive, triggering only on a filter match. The time-based polling primitive is used only when the watched system emits no observable event stream, as a fallback for state that must be sampled rather than observed."
  governance: "Owner: whoever designs or configures the watch task (harness author, agent/task designer, session operator). Reviewable at configuration time against a single question — does the watched system emit observable output? — with the answer checkable against which primitive the task actually uses."
  recovery: "If a polling-based watch task is later found to be watching a system that does emit observable output, reconfigure it as event-driven to eliminate the fixed per-tick cost incurred while idle. If an event-driven watch is found to mis-fire or silently miss state changes because its 'event stream' is unreliable or incomplete, fall back to a time-based polling primitive until the event source is fixed, since polling degrades to missed-latency rather than silent unawareness."
tags:
  - "extracted-artifact"
  - "rule"
  - "background-execution"
  - "event-driven"
  - "polling"
  - "tool-design"
  - "token-budget"
---

# Default to Event-Driven Watching Over Time-Based Polling

**Source:** [[monitor-vs-loop-event-driven-vs-time-driven]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

Designing, configuring, or reviewing a background or unattended watching task — one that observes some external or subordinate system (a subprocess, dev server, deployment pipeline, external API, file system) and needs to react when that system's state changes.

## Action

**Required:** Default to an event-driven watch primitive whenever the watched system emits observable output — logs, stdout, structured events, or file-system change notifications. In Claude Code, this is the Monitor tool: it fires only when a filter-matched event occurs in a background process stream, at zero token cost between events. Use a time-based polling primitive only when no event stream exists from the watched system and periodic sampling is the only way to detect state changes. In Claude Code, this is `/loop`: it fires a full check on a fixed interval regardless of whether anything changed.

**Forbidden:** Defaulting to time-based polling out of habit, or because it was historically the only option, when an event-driven primitive is available and the watched system does emit observable output. Choosing a fixed-interval poll against such a system "for simplicity" without first checking whether an event-driven watch applies.

## Boundary

Enforced at the point a background watching task is designed or configured — whenever an agent, harness, or operator sets up ongoing observation of another process or system. Applies for the lifetime of that watch configuration; revisit the choice if the watched system's output characteristics change (e.g., a previously silent external API adds a webhook or event stream).

The boundary is per-signal, not per-task: a single watch task may legitimately combine both primitives — event-driven for signals that emit observable output, time-based polling as a periodic fallback for state with no push mechanism (e.g., an external API that doesn't push events).

## Enforcement

- **Mechanism:** At design or review time, ask: does the watched system emit observable output? Check the watch task's actual configuration against the answer.
- **Check (deterministic):** `emits_observable_output(watched_system) == true → primitive_used == event_driven`. Violation when the watched system emits observable output but the task uses time-based polling with no documented justification (e.g., the platform genuinely lacks an event-driven primitive).
- **Violation response:** Reconfigure the watch task to use the event-driven primitive. If the platform genuinely lacks one, record that as an explicit precondition exemption rather than leaving the polling choice undocumented.

## Rationale

The choice between the two primitives compounds directly into token/compute budget over the life of a session. A fixed-interval poll incurs its full check cost on every tick regardless of whether anything changed; an event-driven watch costs nothing between events. Over a long-running or unattended session, this difference is substantial — a poll against an idle process wastes budget on every single check, while an event-driven watch sitting idle costs nothing.

The default frequently gets set by inertia rather than by a considered choice: a time-based polling primitive is adopted because it was the only option before an event-driven one existed on the platform, and the choice is never revisited once both are available. Once both primitives exist, the correct default flips — event-driven for any system with an observable event stream, with time-based polling reserved for the genuinely un-observable case.

## Failure Modes

- **Wasted budget and added latency.** Using the polling primitive where an event-driven one applies wastes token/compute budget on every idle tick and adds detection latency of up to the full poll interval, where an event-driven watch would react near-instantly.
- **Silent false-negatives.** Using the event-driven primitive where no reliable event stream exists produces silent false-negatives: no events emitted means no awareness that something is wrong, rather than a clear, if delayed, failure signal. Polling degrades gracefully (late detection); a broken or absent event stream degrades silently (no detection).
- **Combined watches are not violations.** A single watch task legitimately mixing event-driven detection for signals that emit output with periodic polling for signals that don't is expected, not a boundary violation — see Boundary above.

## Contract

### Preconditions
A background or unattended watching task is being designed, configured, or reviewed — one that observes an external or subordinate system (a subprocess, dev server, deployment pipeline, external API, file system) and must react when its state changes. The environment offers, or could offer, both an event-driven watch primitive (fires only on a filter-matched event) and a time-based polling primitive (fires on a fixed interval regardless of whether anything changed).

### Invariants
When the watched system emits observable output (logs, stdout, structured events, file-system change notifications), the watch task uses the event-driven primitive, triggering only on a filter match. The time-based polling primitive is used only when the watched system emits no observable event stream, as a fallback for state that must be sampled rather than observed.

### Governance
Owner: whoever designs or configures the watch task (harness author, agent/task designer, session operator). Reviewable at configuration time against a single question — does the watched system emit observable output? — with the answer checkable against which primitive the task actually uses.

### Recovery
If a polling-based watch task is later found to be watching a system that does emit observable output, reconfigure it as event-driven to eliminate the fixed per-tick cost incurred while idle. If an event-driven watch is found to mis-fire or silently miss state changes because its "event stream" is unreliable or incomplete, fall back to a time-based polling primitive until the event source is fixed, since polling degrades to missed-latency rather than silent unawareness.
