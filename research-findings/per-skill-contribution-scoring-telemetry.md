---
name: "Per-Skill Contribution Scoring as Drift Telemetry"
summary: |-
  You can see a skill library going bad before task metrics drop: log every skill injection to an append-only evidence log, score each skill as (successes - failures) / trials, and have a critic label each use helped / hurt / neutral / inapplicable. A rising proportion of "hurt" verdicts and falling mean contribution are leading indicators of library drift, visible before aggregate pass@1 declines. For us this is the telemetry design to watch for any future skill-roster or extracts lifecycle instrumentation — retirement decisions (Ratchet Recipe) consume exactly these scores.
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (empirical benchmarks)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "arxiv-skill-library-drift-ratchet-recipe.md"
related_findings:
  - file: "ratchet-recipe-skill-retirement.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

# Per-Skill Contribution Scoring as Drift Telemetry

## What It Is

The instrumentation layer beneath the Ratchet Recipe (arXiv 2605.19576):

- **Evidence log**: append-only record of every skill injection ("capsule") with outcome.
- **Contribution score**: per skill, ĉ(s) = (successes(s) − failures(s)) / trials(s). Retirement and cap-eviction decisions read this score.
- **Attribution verdicts**: a separate critic LLM call per failure produces a structured verdict — helped / hurt / neutral / inapplicable — with pattern label and confidence. Verdicts serve double duty: clusters of ≥3 similar failures trigger synthesis of a new skill, and rising "hurt" proportion is an early-warning drift signal.
- **Router engagement**: the fraction of tasks assigned any skill. Healthy runs sat at 70–80%; a drifting configuration collapsed to 19% as the bank emptied; a no-gate configuration hit 98% engagement with lower quality — the router's ability to *decline* injection is itself protective.

These trace-level signals expose drift before end-task metrics decline, enabling intervention (e.g., halt synthesis when engagement drops below a threshold).

## Why It Matters

Library drift is silent by construction — stale skills mislead without errors — so aggregate benchmarks detect it last. Per-skill scoring moves detection upstream to the injection level. For this engine, it defines what a minimal "skill/extract health" telemetry would look like if roster lifecycle governance is ever built: usage log, per-artifact outcome score, and an attribution verdict, with declining mean score and rising hurt-rate as the alarm conditions.

## Why People Are Using It

It is the measurement substrate that makes outcome-driven retirement possible at all — without per-skill scores there is nothing for the evidence floor (Nmin, τ) to evaluate. The paper demonstrates the diagnostics distinguishing healthy from drifting runs across its ablations.

## Potential Improvements

- Principled intervention thresholds (the authors note theirs are empirically chosen).
- Per-step verdicts for multi-step agents, isolating *which* step a stale skill harmed — hypothesized by the authors to make drift signals more sensitive; unvalidated.
- Cheap proxies for low-volume libraries where 100-trial evidence floors are unreachable.

## Potential Failure Modes

- **Critic miscalibration**: helped/hurt verdicts come from an LLM judge; systematic bias silently corrupts every downstream retirement decision.
- **Attribution ambiguity**: when multiple skills are injected together, per-skill credit assignment blurs; scores become correlated noise.
- **Telemetry cost**: a critic call per failure is a real share of the recipe's 43% call overhead; naive adoption in a high-volume system multiplies cost.
