---
name: With/Without-Skill A/B Baseline Runs (Measuring a Skill's Marginal Impact)
summary: 'A skill-improvement loop (skill-loop command driving a skill-improver agent over

  multiple rounds) launches separate headless Claude sessions that run the same task two

  ways — once with the skill loaded and once without — and compares the outputs to

  measure the skill''s actual marginal impact. The delta pins down exactly what the skill

  contributes and what needs improving; results and lessons are recorded in a learning.md

  journal inside the skill. Answers the otherwise-unanswered question "is this skill

  actually working the way it should?"'
implementation_notes: 'The engine has no quantitative way to show a skill earns its keep — skill value is

  asserted, not measured. A with/without baseline run is the minimal experiment: same

  task, fresh headless sessions, diff the outcomes. Design required: a small task corpus

  per skill, a headless run harness, and what "better" means per skill type (rule 10

  applies — the skill''s author must not be its scorer).'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (skill evaluation)
- General
adopted_in: []
sources:
- 5-insane-claude-loops.md
related_findings:
- file: generator-assessor-separation-in-skill-iteration.md
  rel: same-problem
- file: self-improving-skill-lessons-log.md
  rel: enables
- file: externalized-real-session-behavior-evals.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---

## What It Is

The measurement core of AI LABS' "learning loop." A `skill-loop` command triggers a
dedicated skill-improver agent and keeps invoking it until no improvements remain. Each
round: the improver makes changes, then launches a separate background Claude session
(headless, no permission stops, reports output back) that executes the target task
**twice — once with the skill and once without it**. The comparison isolates the skill's
marginal impact: what it actually changes about the output, where it helps, where it
does nothing or hurts. Those observations drive the next round's edits and are logged as
structured lessons in a `learning.md` file living inside the skill.

## Why It Matters for Us

Skill portfolios accumulate on faith: a skill is written, assumed useful, and never
re-measured. The with/without baseline is the cheapest honest experiment — no eval
framework, no labeled dataset, just the counterfactual run. For the engine it offers a
concrete answer to "does /X actually improve output," which currently has no
measurement surface. The pattern also cleanly separates generator and assessor: the
improver edits, a fresh headless session executes, and the comparison judges — no agent
grades its own homework.

## Why People Are Using It

Documented by AI LABS (2026-07-09) from their own product work — they built the loop
because "building a skill raises an obvious question, which is how you'd even know
whether it's working the way it should." Single-source for the exact A/B mechanic, but it
composes two well-corroborated KB patterns (headless verification runs, per-skill lessons
journals).

## Potential Alternatives

- **Structured eval suites** (binary assertions, evals.json): more rigorous and
  regression-proof, but require upfront infrastructure and labeled expectations.
- **Human spot-checks**: zero setup, but unmeasured and inconsistent.

## Potential Improvements

- Multiple task samples per round rather than one — a single with/without pair is noisy.
- Persisting deltas over time so a skill's marginal value can be trended (and the skill
  retired when the baseline catches up to it — models improving can erode a skill's
  delta to zero).

## Potential Failure Modes

- Single-run noise mistaken for signal: one lucky/unlucky baseline run misattributes
  impact.
- Cost: every improvement round doubles execution (two runs per test), multiplied by
  rounds.
- Unverifiable domains: where output quality has no hard check, "with is better than
  without" is itself a model judgment and inherits its biases.
