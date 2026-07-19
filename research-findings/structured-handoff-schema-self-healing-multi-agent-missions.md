---
name: Structured Handoff Schema for Self-Healing Multi-Agent Missions
summary: |-
  Factory's Missions: every worker agent fills out a fixed schema at the end of its
  feature instead of reporting "I'm done" — what was completed, what was explicitly left
  undone, every command run paired with its exit code, issues discovered, and whether the
  worker's actual behavior abided by the orchestrator's defined procedures. This is the
  named mechanism for how a multi-day mission "self-heals": not by hoping agents remember
  or infer what happened upstream, but by forcing each agent to write a specific,
  checkable account of its own work at the boundary. Errors get caught at milestone
  boundaries when the orchestrator reads the accumulated handoffs, corrective work gets
  scoped precisely from the documented gap, and the mission pulls itself back on track.
  Credited as the specific enabling condition for the longest reported mission (16 days).
implementation_notes: |-
  IL already has a file-mediated handoff mechanism in principle (agents/handoff-
  protocol.md, pipeline_status on findings) — this finding's specific field set
  (completed / left-undone / commands+exit-codes / issues-discovered / procedure-
  adherence) is a concrete upgrade to check that protocol against, particularly for the
  Researcher-to-Codifier and Codifier-to-Nick handoffs where "what was left undone" is
  currently implicit rather than a required field.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- multi-agent-architecture-that-actually-ships.md
related_findings:
- file: l-d-hypothesis-information-loss-across-agent-bound.md
  rel: extends
- file: agent-teams-shared-communication-channel.md
  rel: same-problem
- file: ai-shepherding-anti-pattern-manual-workflow-sequencing.md
  rel: same-problem
- file: missions-three-role-architecture-serial-targeted-parallelization.md
  rel: enables
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
  - "templates/worker-handoff-schema-template.md"
---

## What It Is

A fixed schema every worker agent fills out at the end of its feature, instead of simply
reporting "done." Required fields: what was completed; what was explicitly left undone;
every command that was run during the work, paired with its exit code; issues discovered
along the way; and whether the worker's actual behavior abided by the procedures the
orchestrator defined for it. This is the named mechanism for how Missions "self-heals"
across a multi-day run: not by the system hoping agents remember or infer what happened
upstream, but by *forcing* each agent to write a specific, checkable account of its own
work at the boundary — errors then get caught at milestone boundaries (where the
orchestrator reads the accumulated handoffs), corrective work gets scoped precisely from
the documented gap, and the mission "pulls itself back on track."

## Why It Matters

This directly answers an open question the KB's own L>D finding poses without resolving:
"L could potentially be reduced through structured handoff protocols, shared memory
stores, or training models specifically for agent-to-agent communication" — this is a
concrete, production-tested instance of the first option, with a specific field-level
schema rather than an abstract gesture at "better handoffs." It's also a sharper, more
structured cousin of the KB's existing agent-teams-shared-communication-channel.md (which
flags "define a standard message schema" as an open improvement, unresolved) — this
finding supplies exactly that schema, for the handoff sub-case specifically (as opposed
to real-time cross-agent chat).

## Why People Are Using It

Framed as the specific enabling condition for Missions' longest reported run (16 days) —
the claim is explicit that this works "not by hoping that agents remember what happened
but by forcing them to write it down and then actually address issues," i.e., the schema
is credited as doing causal work in sustaining multi-day coherence, not documented as a
nice-to-have.

## Potential Alternatives

- **Free-text handoff summaries** ("here's what I did"): lower authoring overhead per
  worker, but not mechanically checkable by the orchestrator or by downstream tooling the
  way a fixed-field schema is.
- **Shared mutable state/memory store** instead of discrete per-worker handoff
  documents: a different point on the same design space; a shared store risks exactly the
  kind of silent cross-talk contamination the KB's agent-teams finding already flags as a
  failure mode for shared channels.

## Potential Improvements

- A machine-checkable version of the schema (structured data rather than prose) that lets
  the orchestrator programmatically detect gaps (missing exit codes, unexplained
  "left undone" items) rather than relying on the orchestrator's own reading
  comprehension.
- Explicit versioning of the schema itself, so a change to what "good handoff" means
  doesn't silently break comparability across a long-running mission's earlier versus
  later handoffs.

## Potential Failure Modes

- **Schema blind spots:** a worker can fill every field and still omit the thing that
  actually matters if the schema's categories don't happen to have a slot for it —
  structure reduces but doesn't eliminate the underlying information-loss-across-
  boundaries problem the L>D finding names.
- **Opaque commands:** exit-code-and-command logging is only as informative as the
  commands themselves are legible — a worker running one large opaque script reports one
  exit code that hides everything that happened inside it.
- **Orchestrator inattention:** self-healing depends on the orchestrator actually reading
  and acting on handoffs at every milestone boundary; if that step is skipped or rushed
  under load, the schema's information is captured but not used, and the mission drifts
  anyway.

## Extraction Note — 2026-07-19
Extracted as **template**: [[worker-handoff-schema-template]] in `extracts/templates/`
