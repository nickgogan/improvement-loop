---
name: Acceptance Criteria as Verifiable Eval Anchor for Agent Tasks
summary: The most reliable way to prevent agent drift and detect output quality issues is to define acceptance criteria that another person (not the prompter) could verify. This shifts evaluation from subjective
  'does this look right' to objective 'does this pass these checks.' Combined with 3-5 eval cases (known-good examples), acceptance criteria become the anchor for iterative improvement.
implementation_notes: 'MetaSystem Build Specs already require acceptance criteria but not all skills enforce them. Pattern: every recurring agent task should have verifiable acceptance criteria + 3-5 eval
  cases saved as baseline. Iterate the spec as models change.'
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- prompting-after-feb-2026-prompt-craft-context-inten.md
related_findings:
- file: spec-first-agent-briefs-prompt-craft-context-inten.md
  rel: extended-by
- file: social-context-anchoring-bias-in-llm-agent-output.md
  rel: same-problem
- file: spec-as-source-of-truth-for-agent-construction.md
  rel: same-problem
- file: specialized-harness-engineering-deterministic-rail.md
  rel: same-problem
- file: stop-rules-as-execution-boundaries.md
  rel: same-problem
- file: success-rate-eval-over-binary-pass-fail.md
  rel: same-problem
- file: task-contract-pattern-schema-first-agent.md
  rel: same-problem
- file: three-tier-grading-hierarchy.md
  rel: same-problem
- file: tool-shaped-object-evaluation-lens.md
  rel: same-problem
- file: volume-over-quality-eval-principle.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: eval-driven-development-autonomous-quality.md
  rel: same-problem
- file: factorial-design-eval-systematic-context-variati.md
  rel: same-problem
- file: four-layer-agent-evaluation-architecture.md
  rel: same-problem
- file: four-layer-production-eval-stack-with-golden-traces.md
  rel: same-problem
- file: independent-eval-and-scoped-authority-commandments.md
  rel: same-problem
- file: iterative-refinement-loop-with-quality-gate.md
  rel: same-problem
- file: llm-as-judge-pattern-for-verification-agents.md
  rel: enables
- file: mandatory-user-acceptance-testing-uat-at-phase-bo.md
  rel: same-problem
- file: multidimensional-success-criteria-smart.md
  rel: same-problem
- file: binary-eval-assertion-design-deterministic-plus-ll.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- writing-agent-specifications.md
---
## What It Is

A discipline where every agent task spec includes acceptance criteria that a third party (not the original prompter) could evaluate independently. The pattern has three components:

1. **Acceptance criteria:** Verifiable checks stated as pass/fail conditions, not subjective quality judgments. "The output contains a summary under 200 words with at least 3 cited sources" rather than "the output should be good."

2. **Eval cases:** 3-5 known-good examples that represent expected output quality. These serve as the baseline for iterative improvement and regression detection.

3. **Iteration anchor:** When the spec is saved and reused, acceptance criteria + eval cases become the anchor. After model updates, rerun eval cases to detect regressions. Iterate the spec, not individual prompts.

Five common failure modes that acceptance criteria fix:
- "It's 80% right but takes forever to clean up" -- fix: explicit output format + examples
- "The agent drifted after 30 minutes" -- fix: constraints + escalation triggers + checkpoints
- "We loaded everything and quality got worse" -- fix: curate context
- "It optimized for the wrong thing" -- fix: state trade-offs and priorities explicitly
- "We can't tell if outputs are good" -- fix: build test cases, rerun after updates

## Why It Matters

Without verifiable acceptance criteria, evaluation is subjective and inconsistent. The prompter knows what they wanted, but no one else can tell whether the output meets the requirement. This makes handoff, review, and automated evaluation impossible. Acceptance criteria are the bridge between spec-first briefs and binary eval suites.

## Why People Are Using It

Documented as the practical on-ramp for the four-discipline prompting stack. The recommendation: pick one recurring task, write a self-contained spec with acceptance criteria, create 3-5 eval cases, save as baseline, and iterate.

## Potential Failure Modes

- **Criteria too vague:** "Output should be professional" is not verifiable by a third party
- **Missing edge case coverage:** Acceptance criteria that only cover the happy path miss real-world failure modes
- **Stale eval cases:** Known-good examples that were valid for a previous model version may not represent current best output quality

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[acceptance-criteria-as-verifiable-eval-anchor]] in `extracts/patterns/`
