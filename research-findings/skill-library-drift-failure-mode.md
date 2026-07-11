---
name: "Skill-Library Drift — Unbounded Accumulation Degrades the Agent"
summary: |-
  If an agent system keeps adding skills without ever retiring any, the library itself becomes the problem: retrieval degrades, stale skills get injected as false positives, and performance stagnates or drops below the no-skill baseline. The failure is silent — no error signal fires. Empirical anchor: human-curated skills delivered +16.2pp over baseline while ungoverned LLM-authored skills delivered +0.0pp (SkillsBench, reproduced and diagnosed in arXiv 2605.19576). Directly relevant to our own growing skill roster and extracts pipeline: accumulation without lifecycle management is a named, measured failure mode, not a hypothetical.
implementation_notes: |-
  Flagged P2 because the engine's own roster and extracts/ staging accumulate monotonically today —
  nothing retires artifacts based on outcomes. The paper defines drift as accumulated skills pushing
  expected performance below the no-skill baseline, via three compounding stages: accumulation
  without quality gates, retrieval degradation as the bank grows, and silent injection harm (stale
  skills mislead without explicit errors). Design consideration: any skill/extract lifecycle rule
  for the engine should include an outcome-linked retirement path, not just an intake gate. Note
  the counter-result: overly harsh retirement (evidence floor cut from 100 to 20 trials, threshold
  tightened to 0) drove performance BELOW the no-skill baseline — governance itself can cause the
  harm it targets if the evidence floor is too low.
category: "Governance"
evidence_strength: "Medium (empirical benchmarks)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "arxiv-skill-library-drift-ratchet-recipe.md"
related_findings:
  - file: "skill-self-improvement-three-approaches.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

# Skill-Library Drift — Unbounded Accumulation Degrades the Agent

## What It Is

A named, reproduced failure mode of self-evolving skill libraries (arXiv 2605.19576, "Library Drift", ICML 2026 Workshop on Failure Modes in Agentic AI). Formally: accumulated skill artifacts reduce expected pass@1 below the no-skill baseline. The mechanism compounds in three stages:

1. **Accumulation without quality gates** — LLM-authored skills enter the bank unchecked.
2. **Retrieval degradation** — as the bank grows unbounded, the router increasingly surfaces wrong or stale skills.
3. **Silent injection harm** — injected stale skills mislead the solver without any explicit error signal, so aggregate metrics are the first place the damage becomes visible, long after it started.

The motivating gap: SkillsBench found LLM-authored skills gave **+0.0pp** over no-skill baselines while human-curated skills gave **+16.2pp**. The paper reproduces the drift with ablations: forcing no skill injection lands at the no-skill floor (+0.002), while overly aggressive retirement (evidence floor Nmin 100→20, threshold τ→0.0) lands at **−0.019** — actively below baseline.

## Why It Matters

Any system that accretes skills, extracts, or knowledge artifacts over time — including this engine — is exposed. The finding converts "our library keeps growing" from a housekeeping observation into a measured performance risk, and shows the failure is silent by construction: nothing errors when a stale skill misleads. It also warns that the naive fix (aggressive pruning) can be worse than the disease when retirement decisions run on insufficient evidence.

## Why People Are Using It

The paper was accepted to ICML 2026's Workshop on Failure Modes in Agentic AI and directly explains the SkillsBench +0.0pp anomaly that the self-evolving-agent community had observed without diagnosis. It supplies reproducible triggers (ablations) and trace-level diagnostics, making drift testable rather than anecdotal.

## Potential Improvements

- Extend beyond single-benchmark, single-model evidence (only MBPP+ hard-100 on Claude Opus 4.7; the authors flag SWE-Bench-class and multi-step-agent validation as future work).
- Apply the drift lens to non-executable artifact libraries (findings, extracts, guides), where "injection harm" becomes context pollution rather than wrong code.

## Potential Failure Modes

- **Misapplied to curated libraries**: drift is demonstrated for ungoverned LLM-authored accumulation; a human-gated library (like this engine's) has a quality gate at intake and may drift far slower — the risk shifts to staleness, not junk.
- **Over-reaction**: the paper's own A4 ablation shows harsh retirement is worse than no retirement; adopting retirement without an adequate evidence floor reproduces the failure in the opposite direction.
