---
name: LLM-as-Judge Pattern for Verification Agents
summary: Using a separate LLM invocation (not the same conversation) as an independent judge for agent output quality. The judge receives only the output and acceptance criteria, not the reasoning chain
  that produced it. This eliminates confirmation bias from shared context.
implementation_notes: Concrete implementation of context-pollution fix. Judge should be read-only with binary pass/fail output.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-codes-leak-changes-everything.md
- anthropic-multi-agent-research-system.md
related_findings:
- file: context-pollution-same-window-verification-bias.md
  rel: enabled-by
- file: verification-agent-seven-prompt-patterns.md
  rel: extends
- file: bmad-deterministic-skill-validator.md
  rel: same-problem
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: enabled-by
- file: builder-validator-chain-pattern.md
  rel: same-problem
- file: cross-model-verification-for-bug-finding.md
  rel: extended-by
- file: ultra-review-multi-agent-bug-hunting-fleet.md
  rel: enables
- file: enumerate-dont-fix-hostile-reviewer-prompt.md
  rel: same-problem
- file: harness-composition-six-pattern-taxonomy.md
  rel: same-problem
- file: pairwise-tournament-judging-over-absolute-scoring.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
---

## What It Is

The LLM-as-Judge pattern uses a separate LLM invocation as an independent evaluator for agent output. The judge receives only the produced output and the acceptance criteria — never the reasoning chain that generated the output. It returns binary pass/fail verdicts, acting as a read-only quality gate.

## Why It Matters

This is the concrete implementation pattern that addresses context-pollution bias in verification. By stripping the reasoning chain from the judge's input, confirmation bias is structurally eliminated. The judge evaluates output on its own merits against explicit criteria rather than rationalizing from shared context.

## Why People Are Using It

Practitioners report that same-window verification consistently misses errors that independent judges catch. The pattern is gaining traction in agentic coding workflows where output quality directly impacts downstream automation. The simplicity of binary pass/fail verdicts makes it easy to integrate into existing pipelines without complex scoring rubrics.

## Potential Improvements

Current workaround in Claude Code: spawn a sub-agent for verification tasks. Future direction: a dedicated verification agent primitive that automatically strips context and enforces read-only evaluation. Could extend to multi-judge panels for high-stakes decisions.

## Potential Failure Modes

Binary pass/fail loses nuance — some outputs need conditional acceptance or specific feedback. The judge may lack domain context that is necessary for accurate evaluation, producing false failures. Cost and latency double when every output requires a separate LLM invocation for judgment.
