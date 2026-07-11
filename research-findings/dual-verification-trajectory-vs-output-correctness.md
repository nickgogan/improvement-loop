---
name: "Dual Verification: Trajectory Correctness as a Distinct Eval Axis from Output Correctness"
summary: |-
  An agent's answer can look right while the path to it was unsound — skipped checks, wrong tool
  calls, lucky guesses — and that failure is invisible if we only grade outputs. This finding
  names trajectory evaluation (was the sequence of tool calls and reasoning sound?) as a separate,
  co-equal axis alongside output evaluation (is the final result correct?). The authors' framing:
  "an answer that looks right but skipped its checks is more dangerous than one that's obviously
  broken."
implementation_notes: |-
  Applies wherever the engine grades agent work: /assess-* skills and /audit-artifacts currently
  judge artifacts (outputs); a trajectory axis would additionally ask whether the producing run
  followed its declared procedure (e.g., did /design-skill actually delegate its Phase 5 audit
  per rule 10, did a research pass actually dedup-grep before writing). Cheapest first step:
  add a "procedure followed?" checklist item to existing assessments rather than building
  trace-capture infrastructure.
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "osmani-new-sdlc-vibe-coding.md"
related_findings:
  - file: "four-layer-agent-evaluation-architecture.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

## What It Is

A dual-axis verification scheme from the Google whitepaper "The New SDLC" (Osmani/Saboo/Kartakis): **output evaluation** asks "whether the final result is correct"; **trajectory evaluation** asks "whether the path it took to get there, the tool calls and the reasoning, was sound." Both axes are required — neither subsumes the other. A correct output from an unsound trajectory is a latent failure; a sound trajectory with a wrong output is a capability gap. The two demand different graders: output checks can be deterministic assertions, trajectory checks inspect the tool-call/reasoning trace.

## Why It Matters

Output-only evaluation systematically passes the most dangerous failure class: results that are correct-looking but produced by processes that skipped verification steps, hallucinated intermediate facts, or got lucky. As the authors put it, "an answer that looks right but skipped its checks is more dangerous than one that's obviously broken" — the obviously-broken answer gets caught; the unsound-but-plausible one ships. Trajectory evaluation is also the axis that catches process regressions early, before they start corrupting outputs.

## Why People Are Using It

Recommended practice in a Google-published whitepaper on the agentic SDLC, as agent evals mature beyond benchmark-style final-answer scoring toward production trace inspection.

## Potential Alternatives

- Output-only evals with higher sampling volume (catches more output failures, still blind to unsound paths).
- Deterministic reasoning-output consistency rules (the Four-Layer architecture's Layer 2) — a narrower, cheaper slice of trajectory checking.

## Potential Improvements

- Trajectory rubrics derived from a skill's own declared procedure (the SKILL.md steps become the grading checklist), avoiding hand-built rubrics per eval.
- Sampling strategy: trajectory-grade a fraction of runs whose outputs passed, specifically hunting right-answer-wrong-path cases.

## Potential Failure Modes

- Trajectory grading via LLM-as-judge inherits judge bias and can reward verbose, ritualistic traces over genuinely sound ones.
- Over-constraining trajectories punishes legitimate alternative paths — grade soundness (checks performed, evidence gathered), not step-order conformance.
- Cost: full trace inspection on every run is expensive; without sampling discipline it gets dropped entirely.
