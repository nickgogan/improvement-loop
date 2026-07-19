---
name: Cross-Model Verification for Bug Finding
summary: A practitioner-built 'fleet review' skill that combines Claude Code sub-agents and Codex sub-agents for bug finding, then passes results through both a Claude verifier and a Codex verifier. Sometimes
  Claude says a Codex-found bug isn't real, and vice versa. The disagreement signal itself is informative — bugs confirmed by both models have higher confidence.
implementation_notes: Implement cross-model verification for any high-stakes multi-agent review. Model disagreement is a feature, not a bug.
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- claude-code-ultra-review-bug-hunter.md
- claude-code-ultra-review-multi-agent-verification.md
related_findings:
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
- file: builder-validator-chain-pattern.md
  rel: same-problem
- file: context-pollution-same-window-verification-bias.md
  rel: same-problem
- file: eval-driven-development-autonomous-quality.md
  rel: same-problem
- file: goal-backward-verification.md
  rel: same-problem
- file: gstack-review-army-parallel-specialist-dispatch.md
  rel: same-problem
- file: llm-as-judge-pattern-for-verification-agents.md
  rel: extends
- file: qa-agent-independent-compliance-review.md
  rel: same-problem
- file: ralph-loop-brute-force-security-and-ui-testing.md
  rel: same-problem
- file: success-rate-eval-over-binary-pass-fail.md
  rel: same-problem
- file: sweci-benchmark-ai-fails-at-code-maintenance.md
  rel: same-problem
- file: test-driven-development-as-counterweight-to-agenti.md
  rel: same-problem
- file: two-level-verification-agent-run-plus-harness-inte.md
  rel: same-problem
- file: two-stage-sequential-review.md
  rel: same-problem
- file: ultra-review-multi-agent-bug-hunting-fleet.md
  rel: same-problem
- file: verification-agent-seven-prompt-patterns.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- skills/cross-model-verification-for-bug-finding.md
- verifying-agent-output.md
---
# Cross-Model Verification for Bug Finding

## What It Is
A fleet review skill that uses both Claude Code and Codex (via headless mode) for parallel bug finding, then cross-verifies results. Three Claude sub-agents and three Codex sub-agents independently search for bugs. Each model's findings are then passed to the other model's verifier. Claude verifies Codex's bugs; Codex verifies Claude's bugs. The disagreement signal is informative: bugs that both models confirm have highest confidence; bugs that one model refutes deserve human attention. This exploits the fact that different models have different blind spots and biases.

## Why It Matters
Single-model review has systematic blind spots. Cross-model verification catches bugs that no amount of single-model parallelism would find, because the biases are different. The verification step matters more than the finding step — it's what separates high-precision from high-recall review.

## Why People Are Using It
Practitioners building review pipelines report that cross-model disagreement is the most valuable signal — it highlights exactly the areas that need human judgment, rather than burying them in a long list of findings.

## Potential Alternatives
- Single-model verification with persona diversity (cheaper, less diverse)
- Human verification of all findings (thorough but slow)
- Ensemble voting without detailed verification (faster but less informative)

## Potential Improvements
- Adding more models (Gemini, open-source) for wider blind spot coverage
- Weighted confidence scoring based on model agreement patterns
- Learning which model is more reliable for which bug categories over time

## Potential Failure Modes
- Doubles or triples token cost
- Models may have correlated blind spots on certain bug types
- Codex headless mode availability and cost constraints

## Extraction Note — 2026-04-19
Extracted as **skill**: [[cross-model-verification-for-bug-finding]] in `extracts/skills/`
