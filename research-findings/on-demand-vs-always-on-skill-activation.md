---
name: "On-Demand vs Always-On Skill Activation Discipline"
summary: |-
  Plain English: behavior-shaping skills should be invoked at the workflow stage where they
  apply, not installed as permanent system-prompt overrides — always-on skills pollute
  every other skill in the stack. Ponytail offers both modes; the practitioner verdict is
  on-demand: with many skills installed (Superpowers, G-Stack, custom skills), an
  always-on code-minimization override interferes with whatever another skill is trying to
  do; invoking it only at its stage (audit after build, review before commit) keeps skills
  composable. Validates the engine's existing skill design — engine skills are explicitly
  invoked with scoped procedures, not standing behavior overrides.
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Already Adopted"
priority: "Not Flagged"
applicability:
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "claude-code-cuts-token-usage-by-94-percent.md"
related_findings:
  - file: "seven-rung-minimal-code-decision-ladder.md"
    rel: "same-problem"
  - file: "per-node-context-scoping-skills-mcps-commands.md"
    rel: "same-problem"
  - file: "context-file-instruction-bloat-eth-zurich.md"
    rel: "same-problem"
  - file: "disclosure-granularity-decision-rubric.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-13"
pipeline_status: "raw"
---

# On-Demand vs Always-On Skill Activation Discipline

## What It Is

A deployment decision every behavior-shaping skill forces: **always-on** (the skill's
rules apply to all code-writing/output in the session, effectively a system-prompt
override) versus **on-demand** (the skill is invoked at the specific workflow stage where
its behavior is wanted). The source's rule of thumb for multi-skill stacks: on-demand.
Concretely, build with your primary workflow skills unmodified, then invoke the
minimization skill's `audit`/`review` subcommands at the review/pre-commit stage — "I
don't want Ponytail to pollute the other skills I have. I would never use Ponytail to
overwrite a system prompt."

## Why It Matters

Skill interference is a real and mostly invisible failure mode: two always-on skills with
conflicting dispositions (e.g., a completeness-driven spec skill and a minimization skill)
degrade each other with no error surfaced. Stage-scoped activation turns skills from
competing standing policies into composable pipeline steps. For the engine this is
validation, not news — engine skills are invoked, scoped, and terminate — but it names the
anti-pattern to watch for when importing third-party plugins that request system-prompt
residency.

## Why People Are Using It

Practitioners with large skill stacks (Superpowers + G-Stack + custom skills in the
source) converge on it after experiencing cross-skill pollution; plugin authors now ship
both modes plus an `off` escape hatch, implicitly conceding always-on is situational.

## Potential Failure Modes

On-demand discipline depends on remembering to invoke the stage skill — the failure mode
is omission rather than interference. Some behaviors genuinely need always-on residency
(safety constraints, security rules) and shouldn't be stage-scoped; the discipline applies
to *preference*-shaping skills, not invariants. Stage boundaries blur in freeform
sessions, making "the right stage" ambiguous.
