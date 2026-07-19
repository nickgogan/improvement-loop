---
name: Repeated-Sampling Scaling Law and the Verifier Ceiling
summary: 'Plain English: throwing more attempts at a problem reliably raises the odds a correct

  answer exists somewhere in the pile — but without a cheap mechanical checker you can''t

  find it, so eval quality (not model quality or token budget) is the binding constraint

  on multi-agent scale. Stanford 2024: a cheap coding model went from 15.9% bugs fixed

  at 1 attempt to 56% at 250 attempts (beating the best single-attempt frontier model''s

  43%), on a smooth predictable curve across four orders of magnitude; at 10,000

  attempts a correct answer existed in over 95% of runs. But where no automatic checker

  existed, every selection method tried (majority voting, reward models) stalled at

  ~100 attempts. Anthropic''s production corroboration: token spend explains 80% of

  run-quality variance in their multi-agent research system.'
implementation_notes: 'P2: this is the eval-ceiling half of the pending Nate B Jones gap-check against the

  engine. Design implication: before any engine workflow fans out to parallel

  sampling/competition (e.g. orchestrated competition, wide subagent fan-outs), it

  should name its verifier — a mechanical check that grades attempts cheaply. Where no

  such check exists, cap parallelism low (~100-attempt selection ceiling) or route to a

  single agent. Spend past the selection ceiling buys answers that are generated but

  never found.'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (subagent fan-out sizing, verifier design)
- General
adopted_in: []
sources:
- 1-6m-agents-registered-for-openclaw-and-did-nothing.md
related_findings:
- file: orchestrated-competition-n-sub-agents-solve-same.md
  rel: extends
- file: effort-scaling-rules-embedded-in-orchestrator.md
  rel: same-problem
- file: ensemble-eval-majority-required-for-success.md
  rel: same-problem
- file: two-constraint-decomposition-memory-vs-eval.md
  rel: extended-by
- file: four-estimate-agent-routing-test.md
  rel: enables
proposals: null
date_discovered: '2026-07-13'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
---

# Repeated-Sampling Scaling Law and the Verifier Ceiling

## What It Is

Two coupled empirical facts about scaling attempts instead of scaling the model:

1. **The sampling law.** Stanford (2024) gave a cheap coding model one attempt per bug
   on a standard benchmark: 15.9% solved. At 250 attempts per bug: 56% — beating the
   best single attempt from the best model money could buy at the time (43%). The
   improvement curve was smooth and predictable across four orders of magnitude of
   attempts. Pushed to 10,000 attempts, a correct answer existed somewhere in the pile
   for over 95% of problems.

2. **The verifier ceiling.** Coverage only converts to results where something
   mechanical can grade each attempt (a test suite, an exit code, a source document to
   point at). Where the model had to pick the best answer itself — majority voting,
   reward models — selection stalled out at roughly 100 attempts. The right answer is in
   the pile; nobody can tell which one it is. Every dollar spent past that line buys
   attempts that are generated but never found.

Production corroboration from Anthropic's multi-agent research system: the single
biggest factor explaining run quality — 80% of the variance between good and bad runs —
was token spend (how much the system was allowed to think), not prompt wording; and a
team of agents beat the frontier model working alone by 90.2%. Jones's plain-terms
reading of Anthropic's explanation: a team of agents is how you spend more tokens than
one agent can usefully hold.

## Why It Matters

It reframes what limits multi-agent systems: not model capability and not budget, but
**evals**. You need external, mechanical validation to scale multi-agent work — the
checker is what turns coverage into results. This gives a principled basis for the
engine's routine chat-vs-subagent-vs-fan-out routing decision, and a measured reason to
treat verifier design as a prerequisite of fan-out, not an afterthought.

## Why People Are Using It

The Stanford numbers (2024) still hold as a pattern in 2026 agent behavior per Jones,
who built his routing test and his Ringer multi-agent harness on these two facts and
demonstrated three tasks on camera. Anthropic's production numbers come from their
published multi-agent research system analysis (already in the KB via
`anthropic-multi-agent-research-system.md`-sourced findings).

## Potential Improvements

- Per-task-class verifier catalogs: what the "cheap mechanical check" looks like for
  research findings, code, plans, and prose respectively.
- Empirical recalibration of the ~100-attempt selection ceiling as judge models improve
  — the ceiling is where 2024-era selection methods stalled, not a law of nature.

## Potential Failure Modes

- Treating the law as "spend more, get more" while ignoring the ceiling — the shaded
  area past the selection ceiling is pure waste.
- The numbers are relayed secondhand (a practitioner quoting a 2024 study and vendor
  blog); benchmark-specific rates won't transfer literally to other domains.
- A weak or gameable checker reintroduces the ceiling silently: attempts optimize
  against the checker rather than the task.
