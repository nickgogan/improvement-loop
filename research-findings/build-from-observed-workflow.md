---
name: "Build Agents from the Observed Workflow, Not the Paper Workflow"
summary: |-
  Plain English: before automating a job, watch how the best person actually does it —
  and build the agent around that, not around the documented process. Vercel studied
  one of its strongest sales reps closely enough to turn pieces of the workflow into an
  agent: what did the rep ignore, what did they answer, what made a lead real, what
  research happened before a reply, when was a "sales" message actually support, and
  where did the human still make a judgment call. The agent then automated the
  repeatable pieces (filter, qualify, research, draft, route) with human review kept at
  the judgment points that observation — not the SOP — identified.
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "IL (Phase 4 interview design)"
  - "General"
adopted_in: []
sources:
  - "dont-build-more-ai-agents-until-you-watch-this.md"
related_findings:
  - file: "agent-onboarding-via-interview-style-context.md"
    rel: "same-problem"
  - file: "tool-pruning-as-harness-maintenance.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
---

# Build Agents from the Observed Workflow, Not the Paper Workflow

## What It Is

An agent-design sequencing rule from the Vercel SDR case: the build started with
workflow ethnography, not with capabilities. The team watched a top performer's real
behavior — what they ignored, what they answered, what made a lead real, what research
preceded a reply, when an inbound "sales" message was actually a support issue, where
human judgment remained irreducible — and only then built the agent around the
**actual observed workflow, not the paper workflow**. The result automated the
repeatable spine (filter inbound, qualify leads, research companies, draft responses,
route support away from sales) while keeping human review exactly at the judgment
points observation surfaced. The goal, explicitly, was not a bot roaming the company
but taking "a repeatable workflow from a strong employee" and making the repeatable bit
run fast.

Paper workflows (SOPs, wikis, process docs) are already known to drift from reality —
the same world-drift problem that later breaks agents at maintenance time corrupts them
at design time if the SOP is the spec.

## Why It Matters

Where an agent's scope comes from determines both its usefulness and its safe human
boundaries. Deriving scope from observation encodes the expert's real filters
(including what they *don't* do — the ignore list) and locates the human gates
empirically. This is a direct design input for the engine's queued Phase 4
agent-vs-skill interview: elicit Nick's observed operating behavior, not the idealized
process, as the basis for what gets delegated — the same conclusion the KB's
expertise-elicitation onboarding finding reaches from the interview side, and the seam-
identification framing from the gate ruling (which parts belong to the human) reaches
from the triage side.

## Why People Are Using It

Vercel production case; convergent with expertise-elicitation practice already in the
KB (interview-style context extraction as the first agent deployed).

## Potential Improvements

- Pair observation with instrumentation where possible (logs of what the expert
  actually touches) to catch behavior the expert can't self-report.
- Re-observe on a cadence: the observed workflow is a snapshot and drifts like any
  other source.

## Potential Failure Modes

- Overfitting to one expert's idiosyncrasies — the observed workflow may encode habits
  that don't generalize (or shouldn't be preserved).
- Observation without the ignore-list: capturing what the expert does but not what they
  deliberately skip reproduces the inbox, not the judgment.
- The snapshot problem: an agent faithfully encoding last quarter's observed workflow
  is just a higher-fidelity paper workflow once the work moves.
