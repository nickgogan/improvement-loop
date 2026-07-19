---
name: Volume Over Quality Eval Principle
summary: More test cases with slightly lower signal automated grading is better than fewer test cases with high-quality human hand-graded evals. Anthropic's official eval design principle. Prioritize automated
  grading (code-based, LLM-based) over human grading for scalability, reserving human grading only when automated methods are insufficient.
implementation_notes: Directly applicable to MetaSystem's prompt-evaluator and any future eval infrastructure. Current eval approach is entirely qualitative (human review). Shifting to automated evals with
  high volume would catch more failure modes. Start with exact-match and string-match for structured outputs, LLM-as-judge for open-ended outputs.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- anthropic-prompt-evaluation-framework.md
related_findings:
- file: karpathy-autoresearch-self-improvement-loop.md
  rel: enables
- file: success-rate-eval-over-binary-pass-fail.md
  rel: same-problem
- file: three-tier-grading-hierarchy.md
  rel: enabled-by
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
- file: four-discipline-prompt-evaluator.md
  rel: same-problem
- file: four-layer-agent-evaluation-architecture.md
  rel: enables
- file: factorial-design-eval-systematic-context-variati.md
  rel: enabled-by
- file: balanced-positive-negative-eval-sets.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
---
# Volume Over Quality Eval Principle

## What It Is
Anthropic's official eval design principle: "More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals." This establishes a clear priority order for eval design: maximize test case count first, then optimize grading quality. The principle implies that statistical coverage of failure modes matters more than precision on individual test cases.

## Why It Matters
Human grading is the gold standard for quality but does not scale. A hand-graded eval suite of 50 test cases misses more failure modes than an automated suite of 5,000 test cases with noisier grading. Edge cases, rare inputs, and distribution shifts are only caught with volume. This principle is especially important for agentic systems where the input space is large and failure modes are numerous.

## Why People Are Using It
Anthropic's official documentation for building with Claude. The principle is supported by their three-tier grading hierarchy (see below) and concrete code examples for each tier.

## Potential Improvements
Hybrid approaches: use automated grading at volume for regression detection, then targeted human grading on flagged cases. Adaptive test case generation that focuses volume on discovered failure modes.

## Potential Failure Modes
Noisy automated grading can produce false confidence if the noise is systematic (consistently missing a specific failure type). Volume without diversity (many similar test cases) provides false coverage. LLM-based grading inherits the biases of the grading model.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[volume-over-quality-eval-principle.md]] in `extracts/patterns/`
