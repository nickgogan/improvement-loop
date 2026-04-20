---
notion_id: 32b1e08b-9b34-81c4-84ae-e0a3fb562163
name: Iterative Refinement Loop with Quality Gate
summary: A skill pattern where Claude drafts output, scores it against explicit criteria (e.g., 4 dimensions rated 1-5), and loops up to N times if below threshold — preventing both infinite token consumption
  and premature termination.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1
applicability:
- Perplexity Skills
adopted_in: []
sources:
- most-people-build-claude-skills-wrong-heres-what-w.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: eval-driven-development-autonomous-quality.md
  rel: same-problem
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: planner-executor-deterministic-guardrails.md
  rel: same-problem
- file: builder-validator-chain-pattern.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Iterative Refinement Loop with Quality Gate

## What It Is
The iterative refinement pattern instructs Claude to: (1) produce an initial draft, (2) score the draft against predefined criteria (e.g., tone, accuracy, brevity, compliance — each scored 1-5 with a threshold of >=4), (3) if any criterion scores below threshold, rewrite addressing the specific failure, (4) re-score, and (5) loop until all criteria pass or a maximum iteration count (e.g., 3) is reached. Bart notes this is how Claude Code itself works when reviewing a codebase — it loops through chunks with predefined criteria (security, efficiency, compliance) and refactors until each chunk passes.

## Why It Matters
Single-pass generation produces inconsistent quality. Adding a self-evaluation loop makes quality explicit and measurable within the skill, not dependent on human review of every output. The max-iteration cap prevents runaway token consumption.

## Why People Are Using It
Claude Code uses this pattern natively for code review. The pattern extends naturally to any quality-sensitive output (customer responses, compliance checks, content generation).

## Potential Alternatives
External LLM judge (a separate model evaluates the output), human-in-the-loop review, or single-pass generation with human post-editing.

## Potential Improvements
Logging scores and failure reasons per iteration creates an audit trail and can inform future criteria refinement. Scoring criteria could be weighted by importance. Nate B Jones's "build observability from day one" commandment strengthens the case for this pattern: quality gates must produce independent, inspectable evidence of pass/fail rather than relying on the generating agent's self-assessment. The iterative loop's scoring mechanism is a form of the independent evaluation Jones demands -- provided the scoring criteria are externally defined and the pass/fail verdict is logged for audit.

## Potential Failure Modes
Self-evaluation by the same model that generated the output has known limitations — the model may be consistently biased toward rating its own outputs highly. Max 3 loops may be insufficient for complex outputs.
