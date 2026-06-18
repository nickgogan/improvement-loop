---
title: "TDD Step Ordering Template for Plan Task Checkboxes"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "tdd-step-ordering-in-plan-tasks"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "plan documents where each task requires TDD-disciplined implementation by an agent or human"
    - "implementation plan authoring for any project where test infrastructure exists"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — plan template is a document format; altering or removing it has no migration cost"
  auditability: "high — each step is a checkbox; completion status is visible in the plan artifact"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Demonstrated in Superpowers (120k GitHub stars, Anthropic-endorsed). Not yet adopted in MetaSystem plan formats."
contract:
  preconditions: "The project has a test runner and test conventions in place. The task in question implements testable behavior (not pure configuration, documentation, or data migration)."
  invariants: "Steps appear in fixed order: write test → verify red → implement → verify green → commit. The red-verification step is present before implementation. No step is optional unless the task is explicitly flagged as non-TDD."
  governance: "Plan authors include the full 5-step ordering for each TDD-eligible task. Tasks that are non-testable (documentation, config, migration) must be explicitly marked as TDD-exempt in the plan. The executing agent must not reorder or skip steps."
  recovery: "If red-verification (step 2) passes instead of fails, halt; do not proceed to step 3. Reformulate the test before continuing. If the test runner is unavailable at plan authoring time, flag the task as TDD-deferred rather than omitting the steps silently."
tags:
  - "extracted-artifact"
  - "template"
  - "tdd"
  - "plan"
  - "agent-discipline"
---

# TDD Step Ordering Template for Plan Task Checkboxes

**Source:** [[tdd-step-ordering-in-plan-tasks]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Placeholder | Description | Required |
|-------------|-------------|----------|
| `{{TASK_NAME}}` | Short description of what the task implements | Yes |
| `{{TEST_FILE}}` | Path or name of the test file to create or extend | Yes |
| `{{IMPLEMENTATION_FILE}}` | Path or name of the implementation file to create or extend | Yes |
| `{{TEST_RUNNER_COMMAND}}` | Shell command used to run the test suite | Recommended |

## Body

```markdown
### Task: {{TASK_NAME}}

- [ ] Write test in `{{TEST_FILE}}` covering the expected behavior of `{{TASK_NAME}}`
- [ ] Run `{{TEST_RUNNER_COMMAND}}` — confirm the new test **fails** (red)
- [ ] Implement the code in `{{IMPLEMENTATION_FILE}}` to satisfy the test
- [ ] Run `{{TEST_RUNNER_COMMAND}}` — confirm the new test **passes** (green)
- [ ] Commit changes
```

## Usage

1. At plan-authoring time, for each task that implements testable behavior, instantiate this template with the relevant `{{TASK_NAME}}`, `{{TEST_FILE}}`, and `{{IMPLEMENTATION_FILE}}` values.
2. Include `{{TEST_RUNNER_COMMAND}}` to make steps 2 and 4 deterministic — if the test runner command is ambiguous, the agent may guess.
3. Embed the instantiated steps directly in the plan document (e.g., `PLAN.md`, a GSD phase). Do **not** rely on a separate prompt instruction to enforce TDD.
4. Tasks that are not TDD-eligible (pure configuration, database migrations, documentation) should be marked `<!-- TDD-exempt: <reason> -->` in the plan rather than silently omitting the steps.

## Variation Axis

| Variation | Adjustment |
|-----------|------------|
| **Refactor step desired** | Add a 6th checkbox: `- [ ] Refactor `{{IMPLEMENTATION_FILE}}` for clarity; re-run `{{TEST_RUNNER_COMMAND}}` to confirm still green` |
| **No test runner command known at plan time** | Replace `{{TEST_RUNNER_COMMAND}}` with `[test runner]` and flag the task as needing runner resolution before execution |
| **Multi-file implementations** | Expand step 3 to enumerate each file: `- [ ] Implement in \`file-a.py\`, \`file-b.py\`` |
| **BDD/given-when-then framing** | Replace step 1 label with `Write given-when-then scenario in {{TEST_FILE}}` |

## Rationale

Plan-level step ordering enforces TDD structurally rather than via prompt instructions. When the red-verification step is a checkbox in the plan document, the agent must complete it before proceeding — independent of which model is executing. This makes the discipline resident in the data artifact, not in the agent's internalized definition of TDD (which is unreliable per `confirm-failure-first-tdd-agent-discipline`).

## Contract

### Preconditions
The project has a test runner and test conventions in place. The task in question implements testable behavior (not pure configuration, documentation, or data migration).

### Invariants
Steps appear in fixed order: write test → verify red → implement → verify green → commit. The red-verification step is present before implementation. No step is optional unless the task is explicitly flagged as non-TDD.

### Governance
Plan authors include the full 5-step ordering for each TDD-eligible task. Tasks that are non-testable (documentation, config, migration) must be explicitly marked as TDD-exempt in the plan rather than silently omitting the steps. The executing agent must not reorder or skip steps.

### Recovery
If red-verification (step 2) passes instead of fails, halt; do not proceed to step 3. Reformulate the test before continuing. If the test runner is unavailable at plan authoring time, flag the task as TDD-deferred rather than omitting the steps silently.
