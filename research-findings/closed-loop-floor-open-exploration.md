---
name: "Closed-Loop Floor Plus One Open Exploration Instruction"
summary: |-
  Design rule for non-deterministic agent loops: a closed loop (success pinned up front,
  every step checked, stops on command) is predictable but can't explore; an open loop
  (goal plus room to explore) finds novel solutions but burns tokens and slides into slop
  because "better" is undefined. The rescue: keep the hard checks as a floor and add
  exactly one open instruction ("surprise me with the headline") — exploration that
  cannot drop below your standard. Framing: a loop is a generator wired to a verifier;
  the generator is a commodity, the verifier is the bottleneck, and writing a verifier is
  writing a reward function — your definition of "good" is the moat. Companion rule: pick
  the least autonomous tool that does the job (bare shell loop → goal command with a
  separate small model judging done → goal tracking → always-on agents).
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented; key quote secondhand)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "IL (loop/skill design)"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "loop-engineering-explained-by-claude-code-creators.md"
related_findings:
  - file: "generator-assessor-separation-in-skill-iteration.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

The concrete design move that makes open-ended loops shippable. A weak verifier produces
the "slop machine": *make this landing page better, keep going* — with no definition of
better, the loop rewrites the hero eight times, none clearly better, and reports success:
paid motion without progress. The fix is structural, not motivational:

- **Floor:** keep every hard, checkable standard as non-negotiable verification (tests
  pass, constraints hold, stop conditions fire).
- **One open instruction:** grant exactly one degree of exploratory freedom above the
  floor ("surprise me with the headline"). Exploration happens, but it cannot sink below
  the checked standard.

The surrounding theory: every loop is a generator wired to a verifier. Generators
(models) run over and over for almost nothing and are commodities; the verifier — your
encoded judgment of what "correct" looks like — is the bottleneck and the moat. Writing a
verifier is writing a reward function. Corollary: never let an agent grade its own work
(it always gives itself an A); Claude Code's goal command accordingly hands the stop
decision to a separate, faster model. And a tooling ladder from rigid to autonomous —
bare shell loop, goal command, goal-tracking setups, always-on agents — with the rule:
pick the least autonomous tool that does the job.

**Provenance note:** the video's anchor quote ("I do not prompt Claude anymore… my job
is to write loops") is attributed secondhand to Anthropic's Claude Code lead via a
June-2026 field guide — unverified.

## Why It Matters for Us

The engine already operates the floor side (validators, assess-* audits, human gates) and
the least-autonomy instinct. The delta worth keeping is the *one* open instruction: a
disciplined way to buy exploration in research and synthesis loops without opening the
whole loop — e.g., a scan skill whose extraction rules are the floor plus a single
"flag one thing that doesn't fit the dimensions" instruction. The
verifier-as-reward-function framing is also a clean teaching handle for why rule-10
generator/assessor separation exists.

## Why People Are Using It

Cloud Codes synthesis (2026-06-26) of the June-2026 loop-engineering wave; the
generator/verifier asymmetry and no-self-grading rule are corroborated across the KB
(goal-command small-model judge, generator-assessor findings). The floor+one-open-move
formulation itself is single-source.

## Potential Improvements

- Quantifying "one": whether two or three open instructions degrade gracefully or
  collapse into slop is untested.
- Verifier libraries: reusable floors per artifact type, so the open instruction is the
  only per-task authoring.

## Potential Failure Modes

- A floor with gaps: exploration reliably finds the dimensions the checks don't cover.
- Open-instruction creep: one becomes several, and the loop is an open loop again.
- Verifier cost: hard checks for non-code artifacts are exactly what's hardest to write —
  where no floor exists, this pattern silently degrades into the slop machine it warns
  about.
