---
name: "Conductor vs Orchestrator: Two Named Operating Modes for Working with Coding Agents"
summary: |-
  Useful vocabulary for a mode split we already live: sometimes you steer an agent keystroke-by-
  keystroke in the IDE (conductor), sometimes you hand a goal to one or more agents and review
  what comes back (orchestrator). The finding's claim is that these are distinct operating modes
  with distinct selection criteria — conductor for exploration and unfamiliar code, orchestrator
  for well-specified work like migrations or test generation — and that moving between them
  "is a skills shift before it's a tooling one."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "osmani-new-sdlc-vibe-coding.md"
related_findings: []
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

## What It Is

A two-mode taxonomy from the Google whitepaper "The New SDLC" (Osmani/Saboo/Kartakis) for how humans operate coding agents:

- **Conductor mode** — "real-time and in the IDE, keystroke by keystroke, good for exploring and for code you don't know yet." Interactive, synchronous, tight feedback loop.
- **Orchestrator mode** — "async: you hand a goal to one or more agents and review what comes back, good for well-specified work like migrations or test generation." Delegation-based, review-gated, parallelizable.

The selection criterion is task specification quality and familiarity: poorly-specified or exploratory work stays in conductor mode; well-specified, verifiable work moves to orchestrator mode. The authors stress that "the move from conductor to orchestrator is a skills shift before it's a tooling one" — the bottleneck is the human's ability to specify, decompose, and review, not the platform.

## Why It Matters

Teams that treat all agent work as one mode either over-supervise well-specified tasks (wasting the parallelism async delegation buys) or under-specify exploratory tasks and ship unreviewed slop. Naming the modes makes the routing decision explicit: "is this task specified well enough to hand off?" becomes a standing question, and specification quality becomes the visible gate to cheaper async execution. It also reframes upskilling — invest in specification and review skills, not just tooling.

## Why People Are Using It

Documented in a Google-published whitepaper on the agentic SDLC; matches the observed industry split between IDE copilots (conductor) and async agent platforms / background agents (orchestrator).

## Potential Alternatives

- Autonomy-level ladders (L1–L5 style) that grade supervision continuously rather than as two modes.
- Complexity-based routing that picks models/harnesses per task without naming the human's operating mode.

## Potential Improvements

- Explicit promotion criteria: a checklist that qualifies a task for orchestrator mode (spec completeness, verifiability, blast radius).
- Pairing with dual verification — orchestrator-mode output needs trajectory review precisely because the human wasn't watching the path.

## Potential Failure Modes

- Mode misrouting: handing exploratory, underspecified work to async agents produces confident wrong results with no human watching.
- The dichotomy hides the middle: plan-then-delegate workflows (interactive planning, async execution) span both modes and shouldn't be forced into one.
