---
name: "TDD Step Ordering Embedded in Plan Task Structure"
summary: "Each task in the implementation plan encodes a fixed step ordering: (1) write test file, (2) run test to verify it fails, (3) implement code, (4) run test to verify it passes, (5) commit. This TDD cycle is not a separate concern layered on top — it is the task structure itself. The plan's checkboxes enforce the ordering mechanically, and each step has a checkbox that must complete before the next begins."
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "S3 (Claude Code Build)"
sources:
  - "claude-code-plus-superpowers-tutorial.md"
related_findings:
  - file: "confirm-failure-first-tdd-agent-discipline.md"
    rel: "extends"
  - file: "test-driven-development-as-counterweight-to-agenti.md"
    rel: "extends"
  - file: "superpowers-plugin-spec-driven-sub-agent-orchestra.md"
    rel: "extends"
  - file: "artifact-as-contract-pattern.md"
    rel: "same-problem"
  - file: "step-file-micro-architecture.md"
    rel: "same-problem"
adopted_in: []
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: synthesized
consumed_by:
  - "building-agent-evaluation-suites.md"
  - "templates/tdd-step-ordering-in-plan-tasks.md"
tags:
  - "session-95-reextract"
---

# TDD Step Ordering Embedded in Plan Task Structure

## What It Is

A plan artifact design where the TDD cycle is not a separate instruction given to the agent at execution time — it is baked into the structure of each task in the plan document. Each task in the implementation plan contains a fixed sequence of checkboxed steps:

1. Write the test file for this task's expected behavior
2. Run the test suite to verify the new test fails (red)
3. Implement the code that should make the test pass
4. Run the test suite to verify the test passes (green)
5. Commit the changes

In the observed Superpowers workflow (Eric Tech tutorial, BookZero.ai):
- The plan contained 11 tasks, each broken into steps with checkboxes
- Each task's first step was "add test file for [capability]"
- Each task explicitly included "run test to verify it fails" before implementation
- After implementation, "run test to verify it passes"
- After test passes, "commit changes"

The composition insight is structural: **the plan document is the enforcement mechanism for TDD, not the agent's prompt.** The agent does not need to be told "use TDD" — the plan's checkbox ordering makes TDD the only possible execution path. If the agent follows the checkboxes in order (which checkbox-style plans naturally encourage), it has no choice but to write tests first.

This contrasts with prompt-level TDD instructions ("Use red/green TDD") which depend on the agent's interpretation and can be rationalized away. Plan-level TDD is structural enforcement.

## Why It Matters

The confirm-failure-first finding identifies the problem: agents can skip or fake the red step in TDD. Prompt-level TDD instructions are suggestions; agents can rationalize skipping them. Plan-level TDD checkboxes are structural: the step exists in the plan document, and task completion requires checking it off.

This is a specific instance of a broader principle: **embed process discipline in artifact structure, not in agent instructions.** When the plan document's format enforces the process, changing the agent or model does not change the process. The discipline lives in the data, not in the prompt.

For MetaSystem: GSD's PLAN.md format does not currently embed TDD step ordering. If TDD discipline is desired for S3 build work, the plan template itself should include the red/green/commit steps rather than relying on the executing agent's prompt to mention TDD.

## Why People Are Using It

Demonstrated in Superpowers' plan-writing skill (Eric Tech tutorial). The write-plan skill automatically generates plans with TDD step ordering from the spec. The practitioner does not need to request TDD — it is the default structure.

Superpowers has 120k GitHub stars and is Anthropic-endorsed. The TDD-first plan structure is a distinguishing feature cited in multiple Superpowers reviews as the key differentiator from other spec-driven frameworks.

## Potential Improvements

- Plan-level TDD should be optional per task, not blanket: pure configuration changes, database migrations, and documentation tasks do not benefit from TDD step ordering
- The plan template could include specific test expectations (what the failure message should contain) to enable automated red-verification beyond "test fails"
- Plan steps could include estimated token cost per step, letting the human identify tasks where TDD overhead is disproportionate to task complexity
- Integration with existing test infrastructure: the plan should reference the project's test runner and test directory conventions

## Potential Failure Modes

- **Checkbox fatigue.** 11 tasks x 5 steps = 55 checkboxes. For the human reviewer, this is a wall of checkmarks. Important steps may be rubber-stamped rather than verified.
- **Test quality is not plan-enforceable.** The plan can force "write a test" but cannot force "write a GOOD test." Trivial tests (assert true == true) satisfy the checkbox but provide no value.
- **Refactor step often missing.** Classical TDD is red/green/refactor. The observed plan structure has red/green/commit but no explicit refactor step. Without refactor, the codebase accumulates implementation-first code that passes tests but is not clean.
- **Commit-per-step creates noisy git history.** 11 tasks x 1 commit per step = potentially 55+ commits for a single feature. Squash-on-merge is assumed but not enforced by the plan.
- **Plan assumes test infrastructure exists.** If the project has no test framework, test runner, or test conventions, the TDD steps fail at step 1. The plan should detect and flag this prerequisite.
