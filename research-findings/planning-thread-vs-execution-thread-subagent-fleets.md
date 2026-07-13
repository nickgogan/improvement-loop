---
name: "Planning Thread vs Execution Thread, Each with Its Own Subagent Fleet"
summary: |-
  Plain English: don't think of a delegated job as one agent doing every step, and don't
  think of subagents as the unit that owns work. The thread (run) owns the job; a
  subagent is a narrow helper inside it, used so the main thread doesn't get buried in
  noise. Split the job lifecycle across two such threads: a planning thread that uses
  subagents for discovery, source-checking, and scouting messy material, and — once the
  goal is clean — a separate execution thread that owns the deliverable and uses its own
  subagents (scout a site, check sources, inspect output, summarize a noisy folder).
  Thread mode then stops looking like a bunch of chats and becomes a way to separate
  planning, execution, and checking.
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "IL (skill/subagent topology)"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "codex-your-first-personal-ai-agent-delegation-loop.md"
related_findings:
  - file: "plan-implement-session-separation-bias-removal.md"
    rel: "extends"
  - file: "chief-of-staff-home-base-thread.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
---

# Planning Thread vs Execution Thread, Each with Its Own Subagent Fleet

## What It Is

A two-level topology rule for personal delegation loops:

- **Thread owns the job; subagent handles a contained piece.** "A thread is the run
  that owns the job. A sub agent is just a smaller helper inside that job" — used for a
  narrow piece of work so the main thread does not get buried in noise.
- **Planning and execution get separate threads, and each gets its own fleet.** The
  planning thread uses subagents for discovery, source checking, scouting, and reading
  through messy material; when the goal is clean, it hands off to an execution thread
  that owns the deliverable and runs its own subagents (scout a site, check sources,
  inspect output, summarize a noisy folder).

This extends the KB's existing plan/implement session separation (Cole Medin's
fresh-context bias-removal rule) in two ways: the separated units are *persistent
threads* in an ongoing delegation practice rather than one-shot workflow nodes, and the
noise rationale is added to the bias rationale — subagents exist at both stages so
neither thread's own context silts up with raw exploration.

## Why It Matters

It gives operators a mental model that scales: the question "which agent does this?"
becomes "which thread owns this job, and is this piece contained enough to farm to a
helper?" Combined with a chief-of-staff home base, most dispatch happens by talking to
the owning thread, not by hand-wiring agents.

## Why People Are Using It

Core to Jones's daily Codex practice (the workflow behind his token-burn receipts); the
same shape appears vendor-neutrally as planner/executor splits across the KB's
orchestration lane — this is the personal-delegation instance.

## Potential Improvements

- Explicit handoff artifact between planning and execution threads (the KB's plan-file
  discipline) rather than conversational handoff, so execution can't inherit planning
  bias through the thread.
- Named fleet budgets per thread (effort-scaling rules) to stop subagent sprawl.

## Potential Failure Modes

- Conversational handoff leaks planning context into execution, weakening the very
  bias-isolation the session-separation rule exists for.
- Two persistent threads double the staleness surface (goal drift must be synced into
  both).
- Overkill for small jobs — a task that fits one context window doesn't need a
  two-thread lifecycle.
