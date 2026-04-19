---
title: "Volume Over Quality Eval Principle"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "volume-over-quality-eval-principle"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An agent task exists that is evaluated for correctness. At least one automated grading method is feasible (exact match, string match, code-based check, or LLM-as-judge). The input space is large enough that manual review of every case is impractical."
  invariants: "Test case count is the primary optimization target before grading precision. Automated grading is the default; human grading is reserved for cases where no automated method produces usable signal. Volume without diversity is explicitly flagged as false coverage."
  governance: "Eval suite maintainers review grading noise periodically to detect systematic blind spots. New automated grading methods are validated against a human-graded reference set before replacing manual review. Test case diversity is audited alongside count."
  recovery: "If automated grading is discovered to have a systematic blind spot (consistently missing a failure type), add targeted human-graded cases for that failure type, then develop an automated grader for it. Do not revert to full manual grading."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Volume Over Quality Eval Principle

**Source:** [[volume-over-quality-eval-principle]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent task evaluation relies on small sets of hand-graded test cases because human grading is perceived as the gold standard. But small eval suites -- even with perfect grading -- miss edge cases, rare inputs, and distribution shifts. A hand-graded suite of 50 test cases provides high confidence on those 50 cases while leaving the vast majority of the input space untested. Failure modes that matter in production (unusual inputs, format variations, adversarial cases) are only caught at scale.

## Forces

- **Grading precision vs. coverage breadth:** Human grading produces the highest-quality signal per case, but does not scale. Automated grading is noisier per case but can cover orders of magnitude more of the input space.
- **False confidence from small N:** A perfect score on 50 hand-graded cases feels like the system works. But 50 cases cannot represent the distribution of real-world inputs, and edge cases hide in the untested majority.
- **Systematic noise vs. random noise:** Automated grading with random noise (occasionally misgrades in both directions) is acceptable. Automated grading with systematic noise (consistently misses one failure type) is dangerous because it creates a blind spot at scale.
- **Upfront investment vs. marginal cost:** Building automated grading infrastructure has higher upfront cost than hand-grading a few cases, but the marginal cost per additional test case approaches zero.
- **Model bias in LLM-as-judge:** Using an LLM to grade another LLM's output inherits the grading model's biases, which may align with (and therefore miss) the production model's failure modes.

## Solution

Prioritize test case volume over grading precision, using a tiered grading hierarchy:

1. **Code-based grading (highest priority).** Use exact match, string containment, regex matching, or programmatic checks wherever the output format permits. These are deterministic, fast, and free of grading noise. Apply to structured outputs, format compliance, constraint satisfaction, and boundary conditions.

2. **LLM-as-judge grading (second tier).** For open-ended outputs where code-based checks are insufficient, use an LLM grader with a well-defined rubric. The grader prompt should specify binary pass/fail criteria, not subjective quality scales. Validate the LLM grader against a human-graded reference set to characterize its noise profile.

3. **Human grading (last resort).** Reserve for cases where neither code-based nor LLM-based grading produces usable signal -- typically tasks requiring deep domain expertise or subjective judgment that cannot be decomposed into verifiable criteria. When human grading is necessary, use it to build training data for an automated grader, not as a permanent solution.

Design the eval suite for diversity, not just count. Volume without diversity (many similar test cases) provides false coverage. Include: typical inputs, edge cases, adversarial inputs, format variations, and cases targeting known failure modes. When a new failure mode is discovered, add test cases that specifically target it.

Hybrid approach for critical systems: run automated grading at volume for regression detection, then targeted human review on flagged cases (failures, low-confidence automated grades, and random samples for calibration).

## Consequences

**Positive:**
- Catches edge cases, rare inputs, and distribution shifts that small hand-graded suites miss
- Regression detection scales with the eval suite -- model updates can be validated against thousands of cases in minutes
- Frees human reviewers from routine grading, focusing their attention on genuinely ambiguous cases
- Quantitative coverage metrics replace subjective confidence about eval completeness

**Negative:**
- Noisy automated grading can produce false confidence if noise is systematic rather than random
- Volume without diversity creates an illusion of coverage -- many similar test cases test the same thing
- LLM-based grading inherits the grading model's biases, potentially creating shared blind spots with the production model
- Building automated grading infrastructure requires upfront investment that may feel disproportionate for early-stage systems

## Known Uses

- Anthropic's official eval design principle in their prompt engineering documentation, with concrete code examples for each grading tier
- The three-tier grading hierarchy (code-based, LLM-as-judge, human) is Anthropic's recommended implementation of this principle
- Anthropic's factorial design for eval construction uses this principle to generate high-volume test cases from systematic context variation
- MetaSystem's current eval approach is entirely qualitative (human review), making this principle directly applicable as a transition target

## Contract

### Preconditions
An agent task exists that is evaluated for correctness. At least one automated grading method is feasible for the task's output format. The input space is large enough that manual review of every case is impractical. The eval maintainer can distinguish random grading noise from systematic grading blind spots.

### Invariants
Test case count is the primary optimization target before grading precision is refined. Automated grading is the default method; human grading is reserved for cases where no automated method produces usable signal. Volume without diversity is explicitly flagged as false coverage and does not count toward coverage metrics. The grading method's noise profile is characterized and documented.

### Governance
Eval suite maintainers review grading noise periodically to detect systematic blind spots (failure types that automated grading consistently misses). New automated grading methods are validated against a human-graded reference set before replacing manual review. Test case diversity is audited alongside raw count -- adding 1,000 near-duplicate test cases does not satisfy coverage requirements. When model upgrades occur, the full eval suite is rerun before the new model is deployed.

### Recovery
If automated grading is discovered to have a systematic blind spot: add targeted human-graded cases for the affected failure type to quantify the gap, then develop an automated grader specifically for that failure type. Do not revert to full manual grading -- the coverage loss from reduced volume outweighs the precision gain from human review. If the eval suite loses diversity over time (test cases cluster around easy inputs), audit and rebalance by adding cases that target underrepresented regions of the input space.
