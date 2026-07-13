---
title: "Plan-Carried Contract Blocks"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "plans-that-carry-their-own-contract"
extraction_date: "2026-07-13"
last_change_session: 146
last_change_report: "writing-agent-specifications.harvest-queue"
identification_report: "writing-agent-specifications.harvest-queue.md::plans-that-carry-their-own-contract::template::plan-carried-contract-blocks"
deployed: false
deployed_to: null
context:
  applies_to:
    - "plan documents dispatched to context-isolated implementers (subagents, contractors, or teammates) who see only their own task brief"
    - "multi-agent build pipelines where project-wide constraints live in a spec that individual task executors never read"
    - "plan self-review gates that need mechanical checks for placeholder entries and missing interface declarations before dispatch"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a document-structure convention; dropping the blocks reverts to plain linear plans with no migration cost"
  auditability: "high — block presence, verbatim-constraint traceability to spec lines, and Consumes/Produces signature matching between neighboring tasks are all mechanically checkable"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Upstream A/B evidence from the originating framework: plans structured this way needed one fix round versus two-to-four for unstructured control plans, and the control shipped a real bug. Two independent frameworks converged on carried-contract handoffs (plan header blocks in one, sealed frontmatter manifests in the other)."
contract:
  preconditions: "A spec exists with enumerated project-wide constraints. The plan is authored at the point of maximum context (the planner has read the full spec). Tasks will be dispatched to executors who do not re-read the spec. Interface signatures between tasks are decidable at plan time."
  invariants: "Every Global Constraint in the plan header is copied verbatim from the spec and traces to a specific spec line. Every task carries an Interfaces block declaring Consumes and Produces with exact signatures, and each Consumes entry matches some neighbor's Produces entry. No task contains TBD, placeholder, or figure-out-later entries. Each task is the smallest unit that carries its own test cycle and is worth a fresh reviewer's gate."
  governance: "The planner owns the carried blocks; executors treat them as read-only binding context. Spec amendments trigger re-synchronization of the verbatim constraint copies before any further dispatch from the plan. Plan self-review (checking the No Placeholders list and interface matching) gates dispatch."
  recovery: "Verbatim staleness (spec amended mid-branch): halt dispatch, re-copy amended constraints into the header, re-check affected tasks. Signature mismatch between a task's Consumes and its neighbor's Produces: reconcile at the plan level before dispatching either task — never let executors negotiate interfaces peer-to-peer. Placeholder detected at self-review: the plan fails review and returns to the planner. Executor discovers a signature must change mid-task: escalate to the planner to amend the plan, then re-dispatch dependents."
tags:
  - "extracted-artifact"
  - "template"
  - "plan-contracts"
  - "intent-engineering"
  - "multi-agent-handoff"
---

# Plan-Carried Contract Blocks

**Source:** [[plans-that-carry-their-own-contract]]
**Form:** template
**Extraction date:** 2026-07-13

A plan-document scaffold that front-loads what context-isolated executors would otherwise re-derive or miss. Project-wide constraints are copied verbatim into a mandatory plan header, and every task declares its Consumes/Produces interfaces with exact signatures — so an implementer handed nothing but its own task brief still knows the binding constraints and its neighbors' contracts. The contract is authored once at the point of maximum context (the planner), instead of being re-derived N times with N chances of divergence.

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{PLAN_TITLE}}` | string | The plan's name and scope in one line. |
| `{{SPEC_REF}}` | path/link | The authoritative spec this plan implements. Every Global Constraint must trace to a line in it. |
| `{{GLOBAL_CONSTRAINTS}}` | list of (constraint, spec-line ref) | Project-wide requirements copied **verbatim** from the spec — not paraphrased. Each entry cites the spec line it came from so staleness is detectable. |
| `{{TASK_ID}}` | identifier | Stable per-task ID (survives plan updates; downstream references use it). |
| `{{TASK_GOAL}}` | string | What this task delivers, in one sentence. |
| `{{CONSUMES}}` | list of signatures | Exact signatures (function/API/file/schema shapes) this task takes as input, each naming the producing task. |
| `{{PRODUCES}}` | list of signatures | Exact signatures this task outputs, as its neighbors will consume them. |
| `{{TEST_CYCLE}}` | string | The task's own test cycle — the check that makes this task independently verifiable. |
| `{{REVIEWER_GATE}}` | string | What a fresh reviewer checks before this task's output is accepted. |

## Body

```markdown
# {{PLAN_TITLE}}

**Implements:** {{SPEC_REF}}

## Global Constraints (verbatim from spec — binding on every task)

<!-- Copy each constraint word-for-word. Cite the spec line. Do not paraphrase. -->
1. "{{GLOBAL_CONSTRAINTS[0].text}}" — spec §{{GLOBAL_CONSTRAINTS[0].ref}}
2. "{{GLOBAL_CONSTRAINTS[1].text}}" — spec §{{GLOBAL_CONSTRAINTS[1].ref}}
...

## Tasks

### Task {{TASK_ID}}: {{TASK_GOAL}}

**Interfaces**
- **Consumes:** {{CONSUMES}}   <!-- exact signature + producing task ID -->
- **Produces:** {{PRODUCES}}   <!-- exact signature, as consumers will see it -->

**Test cycle:** {{TEST_CYCLE}}
**Reviewer gate:** {{REVIEWER_GATE}}

**Steps**
- [ ] ...

<!-- Repeat per task. Right-size: the smallest unit that carries its own
     test cycle and is worth a fresh reviewer's gate. -->

## Plan Self-Review — No Placeholders

- [ ] No task contains TBD, "figure out later", or unnamed dependencies.
- [ ] Every Global Constraint traces to a spec line.
- [ ] Every Consumes signature matches a neighbor's Produces signature exactly.
- [ ] Every task has a test cycle and a reviewer gate.

A plan failing any check is a plan failure — return to planning; do not dispatch.
```

## Usage

Render one plan per spec, before any task is dispatched to an isolated executor. The planner fills all blocks; executors receive their single task brief **plus** the Global Constraints header (always carried along). Run the self-review checklist as a gate: dispatch only a plan that passes all four checks. When the spec is amended mid-plan, re-synchronize the verbatim constraint copies before further dispatch.

The same move applies at the spec boundary: a spec's frontmatter can carry sealed file-contract manifests (what downstream must read and must not re-read, with stable IDs that survive updates). Use stable task IDs here for the same reason.

## Variation Axis

- **Dispatch isolation depth** — full isolation (executor sees one task + header only) demands complete Interfaces blocks; looser isolation (executor may read the whole plan) can thin them, at the cost of re-derivation divergence creeping back.
- **Signature rigidity** — exact frozen signatures suit stable designs; for exploratory work, mark signatures as `provisional` and route changes through the planner rather than freezing prematurely.
- **Constraint volume** — many constraints bloat every task brief; counterweight with task right-sizing and by scoping constraints that only bind a subset of tasks into those tasks' briefs instead of the global header.

## Contract

### Preconditions
A spec exists with enumerated project-wide constraints. The plan is authored at the point of maximum context (the planner has read the full spec). Tasks will be dispatched to executors who do not re-read the spec. Interface signatures between tasks are decidable at plan time.

### Invariants
Every Global Constraint in the plan header is copied verbatim from the spec and traces to a specific spec line. Every task carries an Interfaces block declaring Consumes and Produces with exact signatures, and each Consumes entry matches some neighbor's Produces entry. No task contains TBD, placeholder, or figure-out-later entries. Each task is the smallest unit that carries its own test cycle and is worth a fresh reviewer's gate.

### Governance
The planner owns the carried blocks; executors treat them as read-only binding context. Spec amendments trigger re-synchronization of the verbatim constraint copies before any further dispatch from the plan. Plan self-review (checking the No Placeholders list and interface matching) gates dispatch.

### Recovery
Verbatim staleness (spec amended mid-branch): halt dispatch, re-copy amended constraints into the header, re-check affected tasks. Signature mismatch between a task's Consumes and its neighbor's Produces: reconcile at the plan level before dispatching either task — never let executors negotiate interfaces peer-to-peer. Placeholder detected at self-review: the plan fails review and returns to the planner. Executor discovers a signature must change mid-task: escalate to the planner to amend the plan, then re-dispatch dependents.
