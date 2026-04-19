---
title: "Three-Tier Eval Grading Hierarchy"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "three-tier-grading-hierarchy"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An evaluation task exists with defined expected outputs or quality criteria. The output type (structured vs. open-ended) has been classified."
  invariants: "Code-based grading is always preferred when the output supports it. LLM judges use a different model than the one being evaluated. Human grading is reserved for cases where neither automated tier has been validated."
  governance: "Grading tier assignment is reviewed when new output types are introduced. LLM rubrics are versioned and tested for inter-rater reliability."
  recovery: "If code-based grading produces false negatives on semantically correct outputs, escalate to LLM-based grading. If LLM judge shows systematic bias, fall back to human grading for calibration."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Three-Tier Eval Grading Hierarchy

**Source:** [[three-tier-grading-hierarchy]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Evaluation systems must choose how to grade outputs, but the options span a wide range of cost, speed, reliability, and flexibility. Teams frequently default to the wrong tier -- using expensive human grading for tasks that could be code-checked, or using unreliable LLM grading without rubrics where deterministic checks would suffice. Without a principled selection hierarchy, evaluation is either too expensive to run at scale or too unreliable to trust.

## Forces

- **Speed vs. nuance:** Code-based grading is instant and perfectly reliable but cannot judge semantic quality. Human grading captures nuance but is slow and expensive.
- **Cost vs. scale:** Human grading does not scale. LLM grading scales but costs tokens. Code-based grading is effectively free.
- **Reliability vs. flexibility:** Exact match is 100% reliable but rejects semantically correct answers with different phrasing. LLM judges are flexible but introduce variance and potential bias.
- **Same-family bias:** LLM judges from the same model family as the generator may share systematic biases, inflating scores.

## Solution

Select the grading method from a three-tier hierarchy, always preferring the highest (cheapest, fastest, most reliable) tier that can adequately grade the output type.

**Tier 1: Code-Based Grading (prefer when possible)**
- Exact match: `output == golden_answer`
- String containment: `key_phrase in output`
- Regex matching for structured formats
- Cosine similarity for embedding-based comparison
- ROUGE-L for summarization quality
- Use when: outputs are structured, deterministic, or have known golden answers.

**Tier 2: LLM-Based Grading (when code cannot capture quality)**
- Write detailed, specific rubrics -- not vague instructions.
- Use empirical scales: binary (`correct`/`incorrect`) or ordinal (1-5 with anchored descriptions for each level).
- Prompt the judge to reason before scoring, then discard the reasoning (keep only the score). This "reason-then-score" technique measurably improves accuracy.
- Use a different model family than the one that generated the output to avoid same-family bias.
- Use when: outputs are open-ended, require judgment, or have no single correct answer.

**Tier 3: Human Grading (avoid if possible)**
- Reserve for novel evaluation criteria where neither Tier 1 nor Tier 2 has been validated.
- Use human grading to calibrate LLM judges, then replace with Tier 2.
- Use when: establishing ground truth for a new task type, or auditing Tier 2 reliability.

**Selection rule:** For each eval task, start at Tier 1. If the output type does not support deterministic checking, move to Tier 2. Move to Tier 3 only if Tier 2 has not been validated for this output type.

## Consequences

**Positive:**
- Orders-of-magnitude cost reduction by routing structured outputs to code-based grading instead of human or LLM grading.
- The "reason-then-score" technique for LLM judges is a non-obvious accuracy improvement that costs only a few extra tokens.
- Cross-model judging reduces same-family bias.
- Explicit hierarchy prevents the common default of using the most expensive method for everything.

**Negative:**
- Code-based grading rejects semantically correct but syntactically different outputs (false negatives).
- LLM judges may still share biases with the generator, especially on subtle dimensions.
- Overly specific rubrics may fail to generalize across diverse test cases.
- The hierarchy requires upfront classification of output types, which is itself a judgment call.

## Known Uses

- Anthropic's official prompt evaluation documentation provides concrete code examples for each tier: exact match for sentiment classification, cosine similarity for consistency, ROUGE-L for summarization, LLM Likert scales for tone, LLM binary classification for privacy, and LLM ordinal scales for context utilization.

## Contract

### Preconditions
An evaluation task exists with defined expected outputs or quality criteria. The output type (structured, semi-structured, open-ended) has been classified before grading tier selection.

### Invariants
Code-based grading is always the first option considered. LLM judges always use a different model family than the generator. Human grading is never used at scale -- only for calibration or novel task types.

### Governance
Grading tier assignments are reviewed whenever new output types are introduced to the evaluation suite. LLM judge rubrics are versioned, and inter-rater reliability is measured periodically (e.g., by comparing LLM judge scores to human scores on a calibration set).

### Recovery
If code-based grading produces false negatives on semantically correct outputs, escalate that output type to LLM-based grading. If an LLM judge shows systematic bias (detected via calibration set), fall back to human grading for recalibration, then update the rubric. If human grading is unavailable, flag the eval results as unvalidated.
