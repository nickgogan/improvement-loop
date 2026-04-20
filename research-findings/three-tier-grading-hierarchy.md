---
name: Three-Tier Eval Grading Hierarchy
summary: 'Choose the fastest, most reliable, most scalable grading method: (1) Code-based grading (exact match, string match) -- fastest and most reliable; (2) LLM-based grading -- fast, flexible, scalable
  for complex judgment; (3) Human grading -- most flexible but slow and expensive, avoid if possible. For LLM grading: use detailed rubrics, empirical scales, and encourage reasoning before scoring (then
  discard the reasoning).'
implementation_notes: MetaSystem should default to code-based grading for structured outputs (YAML frontmatter validation, schema compliance) and LLM-based grading for open-ended outputs (finding quality,
  proposal quality). Human grading reserved for novel evaluation criteria where neither automated method has been validated.
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
- file: binary-eval-assertion-design-deterministic-plus-ll.md
  rel: same-problem
- file: volume-over-quality-eval-principle.md
  rel: enables
- file: eval-driven-development-autonomous-quality.md
  rel: enables
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
- file: four-discipline-prompt-evaluator.md
  rel: enables
- file: four-layer-agent-evaluation-architecture.md
  rel: enables
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---
# Three-Tier Eval Grading Hierarchy

## What It Is
Anthropic's official grading hierarchy for prompt evaluations, ordered by preference:

1. **Code-based grading:** Exact match (`output == golden_answer`), string match (`key_phrase in output`). Fastest, most reliable, extremely scalable. Lacks nuance for complex judgments.
2. **LLM-based grading:** Fast, flexible, scalable, suitable for complex judgment. Best practices: detailed clear rubrics, empirical/specific output format (e.g., 'correct'/'incorrect', or 1-5 scale), encourage reasoning before scoring then discard the reasoning (this improves evaluation performance). Use a different model to evaluate than the model that generated the output.
3. **Human grading:** Most flexible and highest quality but slow and expensive. Avoid if possible.

## Why It Matters
Choosing the wrong grading tier wastes resources or produces unreliable results. Code-based grading for tasks that support it is orders of magnitude cheaper and more reliable than LLM-based grading. LLM-based grading with proper rubrics approaches human quality at a fraction of the cost. The "reasoning then discard" technique for LLM judges is a non-obvious but significant accuracy improvement.

## Why People Are Using It
Anthropic's official documentation with concrete code examples for each tier: exact match for sentiment classification, cosine similarity for consistency, ROUGE-L for summarization quality, LLM Likert scales for tone evaluation, LLM binary classification for privacy preservation, and LLM ordinal scales for context utilization.

## Potential Improvements
Ensemble grading: combine code-based and LLM-based grading for higher accuracy. Grading model calibration: measure and correct systematic biases in LLM judges. Automatic tier selection based on output structure.

## Potential Failure Modes
LLM judges may share biases with the model being evaluated (especially same-family models). Overly specific rubrics that fail to generalize across test cases. Code-based grading that misses semantically correct but syntactically different outputs.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[three-tier-grading-hierarchy.md]] in `extracts/patterns/`
