---
name: "Two-Constraint Decomposition: Split for Memory or Split for Eval"
summary: |-
  Plain English: there are exactly two good reasons to split work across multiple
  agents, and if a multi-agent design isn't answering one of them it's "just more
  agents." (1) The memory constraint — the task is bigger than one agent can hold at
  full quality; context fill degrades output, so capacity forces delegation. (2) The
  eval/integrity constraint — some parts of the work poison each other and need
  different minds (the auditor who kept the books isn't an auditor; peer review works
  because the reviewer didn't write the paper). Agents add something new to the second
  reason: "fresh eyes on demand" — you can now start a mind that has never seen the
  artifact, for the first time in history.
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "IL (subagent topology rationale)"
  - "General"
adopted_in:
  - "Improvement Loop"
related_findings:
  - file: "repeated-sampling-scaling-law-and-verifier-ceiling.md"
    rel: "extends"
  - file: "four-estimate-agent-routing-test.md"
    rel: "same-problem"
  - file: "plan-implement-session-separation-bias-removal.md"
    rel: "same-problem"
sources:
  - "1-6m-agents-registered-for-openclaw-and-did-nothing.md"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
---

# Two-Constraint Decomposition: Split for Memory or Split for Eval

## What It Is

A theory of when multi-agent decomposition is justified: "every team-of-agents design
that actually works is an answer to one of these two problems; everything else is just
more agents."

- **Memory constraint.** A single agent cannot absorb unlimited spend — everything it
  reads piles into one context window, quality drops as it fills (even with
  auto-compaction), and eventually the agent must delegate or abandon. When a task
  exceeds what one agent can hold at full quality, capacity forces a split. (Jones
  notes newer agentic models already do this implicitly on big tasks — part of the goal
  is making that split intentional.)
- **Eval/integrity constraint.** Some parts of work inherently need different minds —
  not because one mind lacks skill, but because the parts poison each other: the
  auditor who also kept the books, the payment enterer who approves the payment, the
  author reviewing their own draft. You cannot unknow something you wrote. Agents add a
  historically new capability here: **fresh eyes on demand** — start a mind that has
  never seen the artifact, whenever a genuine conflict of interest needs balancing
  (contracts, drafts, plans).

## Why It Matters

It converts "should this be multi-agent?" from an aesthetic choice into a two-question
check, and it names the null result: a decomposition answering neither constraint is
overhead. The eval half is the theoretical grounding for the engine's already-standing
generator-assessor separation rule and its plan/implement session-separation findings —
this finding supplies the *why* those patterns keep independently re-emerging.

## Why People Are Using It

Jones presents it as the durable core beneath his routing test, grounded in the Stanford
sampling/ceiling results (eval constraint) and context-window degradation behavior
(memory constraint), and demonstrated across three on-camera tasks with real spend.

## Potential Improvements

- A third-constraint watch: latency/parallelism (wall-clock, not capacity or integrity)
  sometimes motivates splits; the theory as stated folds it into memory, which may be
  too coarse.
- Map each engine subagent boundary to its governing constraint and flag boundaries
  that answer neither.

## Potential Failure Modes

- The memory constraint moves as context windows and compaction improve — splits
  justified by capacity last year may be pure overhead now (harness-simplification
  problem).
- Fresh-eyes value degrades if the "fresh" agent inherits the author's context anyway
  (shared thread, leaked reasoning) — the isolation has to be real.
- Over-applying the eval constraint: not every task has a genuine conflict of interest;
  reflexive reviewer agents double cost for no integrity gain.
