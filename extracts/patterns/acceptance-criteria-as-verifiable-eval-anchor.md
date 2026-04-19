---
title: "Acceptance Criteria as Verifiable Eval Anchor"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "acceptance-criteria-as-verifiable-eval-anchor"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A recurring agent task exists with defined expected outputs. The task has been run at least once so that output shape is known."
  invariants: "Every acceptance criterion is evaluable by a third party without access to the prompter's intent. Eval cases are versioned alongside the spec. Criteria are pass/fail, never subjective quality judgments."
  governance: "Spec owners review and update acceptance criteria after model changes or task scope changes. Eval cases are rerun on model upgrades to detect regressions. Criteria cannot be modified by the agent under evaluation."
  recovery: "If eval cases become stale after a model update, freeze the spec, rerun existing cases, document regressions, then update criteria and cases together as a versioned revision."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Acceptance Criteria as Verifiable Eval Anchor

**Source:** [[acceptance-criteria-as-verifiable-eval-anchor]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent task outputs are evaluated subjectively -- the prompter knows what they wanted, but no one else can tell whether the output meets requirements. This makes handoff, review, automated evaluation, and iterative improvement impossible. Without explicit criteria, agents drift, optimize for the wrong thing, and produce outputs that are "80% right but take forever to clean up."

## Forces

- **Specificity vs. flexibility:** Overly rigid criteria prevent the agent from finding better solutions; overly vague criteria provide no evaluation signal.
- **Upfront cost vs. long-term value:** Writing verifiable criteria and eval cases takes effort that feels wasteful for a one-off task but compounds for recurring tasks.
- **Model evolution vs. stable baselines:** Eval cases that were valid for one model version may not represent current best output quality, but without them regressions go undetected.
- **Prompter knowledge vs. third-party verifiability:** The prompter carries implicit context about what "good" looks like that must be externalized into pass/fail conditions.

## Solution

For every recurring agent task, define three components:

1. **Acceptance criteria as pass/fail conditions.** Each criterion must be evaluable by someone who did not write the prompt. State them as verifiable checks: "output contains a summary under 200 words with at least 3 cited sources" rather than "output should be good." Cover output format, constraints, escalation triggers, trade-off priorities, and checkpoints.

2. **3-5 eval cases as known-good baselines.** These are concrete examples of expected output quality. They serve as regression detectors and iteration anchors. Include typical cases, edge cases, and at least one case that targets the hardest acceptance criterion.

3. **Iteration on the spec, not individual prompts.** Save the spec with its criteria and eval cases. When the model changes, rerun eval cases against the new model. If regressions appear, iterate the spec -- adjust criteria, update examples, refine constraints. The spec is the durable artifact; individual prompt tweaks are ephemeral.

Five failure modes this pattern addresses:
- "80% right but takes forever to clean up" -- explicit output format + examples
- "Agent drifted after 30 minutes" -- constraints + escalation triggers + checkpoints
- "Loaded everything and quality got worse" -- curate context
- "Optimized for the wrong thing" -- state trade-offs and priorities explicitly
- "Can't tell if outputs are good" -- build test cases, rerun after updates

## Consequences

**Positive:**
- Evaluation becomes objective, repeatable, and delegatable -- any reviewer can verify outputs
- Regressions after model updates are detected automatically by rerunning eval cases
- Iterative improvement has a stable anchor: change the spec, rerun cases, measure delta
- Bridges the gap between spec-first briefs and binary eval suites

**Negative:**
- Upfront investment per task: writing verifiable criteria and curating 3-5 eval cases takes time
- Risk of criteria that are too narrow, missing edge cases or real-world failure modes
- Eval cases require maintenance -- stale baselines from previous model versions create false confidence
- Criteria that are technically verifiable but practically meaningless ("output is not empty") give a false sense of rigor

## Known Uses

- Documented as the practical on-ramp for the four-discipline prompting stack (Prompt Craft, Context Engineering, Intent Engineering, Specification Engineering)
- MetaSystem Build Specs already require acceptance criteria, though not all skills enforce them with eval cases
- MindStudio's autonomous skill improvement loops use acceptance criteria as the anchor for overnight iteration cycles
- Anthropic's Skills 2.0 Grader sub-agent uses pass/fail acceptance criteria as the basis for its evaluation pipeline

## Contract

### Preconditions
A recurring agent task exists with defined expected outputs. The task has been run at least once so that output shape is known. The spec owner understands the task well enough to distinguish good from bad output.

### Invariants
Every acceptance criterion is evaluable by a third party without access to the prompter's intent. Eval cases are versioned alongside the spec. Criteria are binary pass/fail -- never subjective quality judgments or numeric scores. The agent under evaluation cannot modify its own acceptance criteria or eval cases.

### Governance
Spec owners review and update acceptance criteria after model changes or task scope changes. Eval cases are rerun on model upgrades to detect regressions. New criteria require at least one eval case that targets the new requirement. Criteria cannot be modified by the agent under evaluation.

### Recovery
If eval cases become stale after a model update: freeze the spec, rerun existing cases against the new model, document regressions with specific failing criteria, then update criteria and cases together as a versioned revision. If criteria are discovered to be unverifiable by a third party, rewrite them as concrete pass/fail conditions before the next evaluation cycle.
