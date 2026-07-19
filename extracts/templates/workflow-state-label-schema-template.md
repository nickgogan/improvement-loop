---
title: "Workflow-State Label Schema Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "github-label-as-workflow-state"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "autonomous-scheduled-agent-operation.harvest-queue"
identification_report: "autonomous-scheduled-agent-operation.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "autonomous pipelines that use a shared issue or ticket tracker as coordination state across multiple workflow stages"
    - "teams avoiding a separate state database for pipeline coordination, preferring a substrate already visible in an existing tracker's UI"
    - "operators who want the full workflow state of every in-flight item visible to a human without building a dedicated dashboard"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — labels can be renamed or the schema table edited without touching the tracker's underlying data model; existing items keep their current label until explicitly relabeled"
  auditability: "high — a human scanning the tracker's normal UI sees the complete workflow state of every item with no dashboard required; the label itself is the audit trail"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Derived by a practitioner from studying a production autonomous-pipeline's own label/status approach and adapting it for their own workflows; not yet adopted as a standalone reusable schema in the extracting system."
contract:
  preconditions: "A shared issue or ticket tracker exists (GitHub Issues, or any tracker with an equivalent label/tag primitive that can be applied and queried programmatically) and is the shared source of truth for the work items an autonomous pipeline processes. Multiple workflow stages (triage, implement, validate, etc.) need to coordinate over the same item without a separate state database."
  invariants: "Every item carries at most one in-flight state label from the closed label set at any time — no item is ambiguously in two mutually-exclusive states simultaneously. The orchestrator consults an item's current label(s) before every dispatch decision and never dispatches an item whose current label excludes it. Label application is a deterministic, non-reasoning step, separate from any LLM classification step that decided the new state — decide and act are distinct nodes (see [[deterministic-nodes-for-non-reasoning-steps]])."
  governance: "Owner: whoever maintains the orchestrator/pipeline. The label set is declared and versioned alongside the orchestrator's dispatch logic — adding or retiring a state requires updating both the schema table and the dispatch rules together, never one without the other."
  recovery: "If an item is found holding a stale or orphaned in-flight label (its workflow crashed without clearing it), the label needs a timeout/cleanup mechanism — clear it after a defined interval and write an audit log entry rather than leaving the item permanently skipped. If two mutually-exclusive labels are found on the same item simultaneously, treat it as a race condition: cordon the item (apply a needs-human-equivalent label) for manual review rather than guessing which state is authoritative."
tags:
  - "extracted-artifact"
  - "template"
---

# Workflow-State Label Schema Template

**Source:** [[github-label-as-workflow-state]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{PIPELINE_NAME}}` | string | The autonomous pipeline or workflow this label set governs. |
| `{{LABEL_NAME}}` | string (repeatable row) | The literal label/tag string applied to a tracker item. |
| `{{STATE_MEANING}}` | string (repeatable row) | Plain-English description of what the label means about the item's current position in the workflow. |
| `{{ORCHESTRATOR_DISPATCH_RULE}}` | string (repeatable row) | What the orchestrator does when it sees this label on an item — dispatch to a specific stage, skip, or hold for human action. |
| `{{ESCALATION_THRESHOLD}}` | integer | Number of consecutive failures (or ambiguous classifications) after which an item is force-labeled into a human-escalation state. |

## Body

```markdown
# {{PIPELINE_NAME}} — Workflow State Labels

| Label | State Meaning | Orchestrator Dispatch Rule |
|---|---|---|
| `{{LABEL_NAME}}` | {{STATE_MEANING}} | {{ORCHESTRATOR_DISPATCH_RULE}} |
| ... | ... | ... |

Escalation: an item is force-labeled into the human-review state after {{ESCALATION_THRESHOLD}} consecutive failures, or when the classification step reports ambiguity.
```

**Illustrative default set** (from the source pipeline — adapt names and states to the target pipeline's own stages, this is a starting shape, not a fixed vocabulary):

| Label | State Meaning | Orchestrator Dispatch Rule |
|---|---|---|
| `pipeline-accepted` | Triage stage classified this item as in-scope | Eligible for the implementation stage |
| `pipeline-rejected` | Triage stage classified this item as out-of-scope | Skip — no further stages |
| `in-progress` | A stage is currently running on this item | Skip — already being processed; do not double-dispatch |
| `needs-fixed` | The active stage failed; awaiting retry or human input | Skip automatic retry after threshold; otherwise retry |
| `needs-human` | Failed past the escalation threshold, or the classifier flagged ambiguity | Skip all automatic dispatch until a human clears the label |
| `pipeline-rate-limit` | Daily token/spend budget reached | Skip all workflows on all items until the label is cleared (usually next period) |

## Usage

Create one schema instance per autonomous pipeline that uses a tracker's label/tag primitive as its coordination substrate. The orchestrator (typically a scheduled/cron-driven process) reads an item's current label set **before** every dispatch decision:

1. No pipeline-state label present → item is eligible for the first stage (usually triage).
2. A "positive" label with no "in-flight" label present → eligible for the next stage.
3. An "in-flight" label present → skip; another cycle is already processing this item.
4. A "held" label (`needs-human`, rate-limit, or equivalent) present → skip until a human clears it.

Label *application* is performed by a deterministic node in the workflow, separate from whatever LLM-driven classification step decided the new state — the decision and the act of writing it are different nodes so that the state transition itself is machine-checkable independent of the reasoning that produced it.

## Variation Axis

- **Number of states.** Simple two-stage pipelines may need only 3-4 labels; multi-stage pipelines with retries and rate limiting need more. Add rows, don't overload existing ones with compound meanings.
- **Naming convention.** A label prefix scoped to the pipeline (e.g. `pipeline-*`) avoids collision with labels used for other, human-driven purposes in the same tracker.
- **Escalation threshold.** How many consecutive failures before forcing human review is a per-pipeline risk tolerance call — lower for high-stakes pipelines, higher for cheap-to-retry ones.
- **Cleanup policy.** Whether orphaned in-flight labels (from a crashed run) are cleared by a timeout watchdog, a manual audit, or left for a human to notice is a deployment-specific choice not fixed by this schema.
