---
name: "Process-Optimizer Agent (Improve the Loop, Not the Artifact)"
summary: |-
  A workflow-improvement loop adds a third agent alongside the builder and the
  rubric-scorer: a process-optimizer agent that, after each round, reviews the loop
  iteration itself (the conversation, the steps taken) and proposes improvements to the
  workflow rather than to the artifact. Scores per round are tracked in a JSON file. End
  state: not just a built app, but a workflow whose every step has been validated as one
  that actually needs to be there. Distinct from a learning loop, which improves one
  piece (a skill) inside the process — this improves the process itself.
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "IL (loop/process design)"
  - "General"
adopted_in: []
sources:
  - "5-insane-claude-loops.md"
related_findings:
  - file: "self-evolving-loop-pattern.md"
    rel: "same-problem"
  - file: "karpathy-autoresearch-self-improvement-loop.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

AI LABS' "workflow improvement loop." An `iterate` command orchestrates three agents per
round: a **builder** implements one requirement; a **scorer** evaluates the result
against a predefined rubric (score out of 100, recorded in a JSON round-tracking file);
and a **process-optimizer** goes back over the round's conversation to spot anything
that could improve *the workflow* — step ordering, missing checks, redundant stages —
and applies those suggestions to the loop definition. The explicit contrast: a learning
loop improves a skill (one piece inside the process); this loop improves the loop.

## Why It Matters for Us

Most self-improvement patterns in the KB target artifacts (code, skills, documents). The
meta-level — does the *procedure* have the right steps — is usually only revisited when
a human notices friction. A designated process-optimizer step makes procedure review a
scheduled part of every run, which is essentially what the engine does manually in
retro/feedback sessions. It names a role the engine's /solicit-proposals reflection
round approximates at system level, scoped down to a single loop.

## Why People Are Using It

AI LABS (2026-07-09) present it as "the core of what a loop is meant to do" — none of
their other four loop types had a step for improving the loop itself. Single-source for
the three-agent decomposition; the underlying idea (loop that edits its own procedure)
has adjacent KB corroboration in autoresearch-style improvement loops.

## Potential Failure Modes

- Unbounded meta-work: process suggestions every round can churn the workflow faster
  than its value stabilizes; changes to the loop need the same gating as changes to
  artifacts.
- Score gaming: with the rubric fixed and visible, the optimizer can tune the process to
  the rubric rather than to quality.
- Role bleed: if the process-optimizer also edits artifacts, the builder/scorer
  separation collapses.
