---
title: "Four-Mode Skill Lifecycle with Binary Evals"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "claude-code-skills-20-four-mode-skill-lifecycle-wi"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The skill has a defined input-output contract that can be expressed as binary assertions (pass/fail). A test harness can be constructed that exercises the skill without human intervention."
  invariants: "Every skill improvement is measured against the prior version through blind A/B comparison. No skill version is promoted without passing its binary eval suite. The iteration loop is capped."
  governance: "Benchmark baselines are recorded at each skill version. Improvement iterations are tracked in git history. Eval suite coverage is reviewed when the skill's scope changes."
  recovery: "If a skill regresses during improvement, revert to the last passing version using git history. If the eval suite is discovered to be inadequate, freeze improvements until the suite is expanded."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Four-Mode Skill Lifecycle with Binary Evals

**Source:** [[claude-code-skills-20-four-mode-skill-lifecycle-wi]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent skills are created and then left static, or improved through subjective human judgment ("this output looks better"). Without objective measurement, skill improvements are driven by confirmation bias -- the creator believes the new version is better because they designed the change. There is no mechanism to detect regressions, no baseline to compare against, and no way to run improvement iterations without continuous human supervision.

## Forces

- **Subjective quality vs. objective measurement.** Humans evaluate skill output holistically, which captures nuance but introduces bias. Binary evals (pass/fail assertions) are objective but may miss qualitative dimensions.
- **Manual iteration cost.** Each improvement cycle requires a human to review, judge, and direct the next change. This limits improvement throughput to human attention bandwidth.
- **Confirmation bias in A/B testing.** When the skill creator knows which version is which, they tend to favor the version they expect to be better. Blind comparison eliminates this bias but requires infrastructure.
- **Iteration convergence.** Autonomous improvement loops can oscillate, overfit to the test suite, or make changes that pass tests but degrade unmeasured qualities. A cap on iterations prevents runaway optimization.

## Solution

**Implement a four-mode lifecycle for agent skills, with binary evals enabling autonomous overnight improvement.**

**Four Modes:**

1. **Create** -- Define the skill's purpose, trigger conditions, input-output contract, and initial implementation. This is the standard skill authoring step.

2. **Eval** -- Write binary assertions that define "correct" for the skill's output. Each assertion is a pass/fail test case. The assertion suite must cover normal cases, edge cases, and failure modes. This is the critical investment -- the quality of autonomous improvement is bounded by the quality of the eval suite.

3. **Improve** -- Configure an autonomous improvement loop: set an iteration cap (40-50 cycles), point at the eval suite, and let the agent iterate. Each cycle: make one logical change, run the harness, record results. Two improvement dimensions: trigger/description tuning (when does the skill activate and how is it described) and output quality improvement (does the skill produce better results). Full git history is preserved for every iteration.

4. **Benchmark** -- Compare the improved skill against the baseline using three metrics: Pass Rate (does it pass more tests?), Elapsed Time (is it faster or slower?), and Token Usage (does it cost more or less?). Blind A/B comparison between versions eliminates creator bias.

**Four Parallel Sub-Agents:**
- **Executor** -- Runs the skill against test inputs.
- **Grader** -- Evaluates outputs against binary assertions.
- **Comparator** -- Performs blind A/B comparison between skill versions (does not know which is old vs. new).
- **Analyzer** -- Synthesizes results across test cases and produces improvement recommendations.

**The overnight loop:** Write assertions, build harness, configure loop, set iteration cap, start, walk away. Wake up to a refined skill with full git history of every change attempted.

## Consequences

**Positive:**
- Eliminates confirmation bias through blind A/B testing between versions.
- Enables autonomous improvement without continuous human supervision -- the human invests upfront in writing good assertions, then the loop runs unattended.
- Full git history of every iteration provides complete audit trail and easy rollback.
- Benchmark mode answers the fundamental question ("is this actually better?") with objective metrics, not subjective impressions.
- Two improvement dimensions (trigger tuning and output quality) cover the full surface area of skill behavior.

**Negative:**
- Binary assertions only capture pass/fail; they miss qualitative dimensions like tone, coherence, or user experience that matter for some skills.
- Eval suite coverage is the binding constraint -- if the tests do not cover an edge case, autonomous improvement will not find or fix it.
- 40-50 iteration cap may be insufficient for complex skills with large search spaces. May also be excessive for simple skills, wasting tokens.
- Overfitting to the test suite is possible -- the skill may pass all tests but produce worse results on inputs not covered by assertions.
- Requires four parallel sub-agents, which adds infrastructure complexity and token cost.

## Known Uses

- Anthropic's Claude Code Skills 2.0, GA since March 7, 2026. Positioned as the official workflow for skill maintenance.
- MindStudio blog post documenting the binary eval approach with concrete implementation details.
- Extends the Self-Evolving Loop Pattern in this KB with specific mechanics and objective measurement.
- Related to the Builder-Validator Chain pattern, ACE execution feedback, and the 15-30 test input sweet spot finding.

## Contract

### Preconditions
The skill has a defined input-output contract that can be expressed as binary assertions (pass/fail). A test harness can be constructed that exercises the skill without human intervention. The skill's output is deterministic enough that binary assertions produce stable results (or the harness accounts for non-determinism through multiple runs).

### Invariants
Every skill improvement is measured against the prior version through blind A/B comparison -- the Comparator never knows which version is old vs. new. No skill version is promoted to production without passing its binary eval suite. The iteration loop is capped at a configured maximum (default 40-50). Full git history is preserved for every iteration attempt, successful or not.

### Governance
Benchmark baselines (Pass Rate, Elapsed Time, Token Usage) are recorded at each skill version for trend tracking. Improvement iterations are tracked in git history for audit and rollback. Eval suite coverage is reviewed and expanded when the skill's scope or input domain changes. The iteration cap is tunable per skill based on complexity.

### Recovery
If a skill regresses during the improvement loop (new version scores lower than baseline on any benchmark metric), revert to the last passing version using git history. If the eval suite is discovered to be inadequate (tests pass but real-world behavior degrades), freeze autonomous improvements and expand the suite before resuming. Document regressions and their root causes to improve future eval design.
