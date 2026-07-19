---
title: "Worker Handoff Schema Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "structured-handoff-schema-self-healing-multi-agent-missions"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-architecture-decisions.harvest-queue"
identification_report: "agent-architecture-decisions.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "multi-agent systems where one worker's output becomes the next worker's or an orchestrator's input, and the receiving party has no visibility into what actually happened during the work"
    - "long-running or multi-stage autonomous missions where errors need to be caught at defined checkpoints, rather than discovered much later and far from their root cause"
    - "any workflow that currently relies on a worker's free-text 'I'm done' summary, where the receiving party needs a checkable account instead of a narrative one"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — a filled handoff is a reporting document; editing its fields or discarding a malformed one costs nothing. The risk is not in the artifact but in what an orchestrator fails to catch if the handoff is skipped or unread."
  auditability: "high — each field is meant to leave a specific, checkable record (a completion claim, an explicit undone item, a command paired with its exit code, a compliance statement), so a reviewer can verify what happened by reading the handoff alone rather than reconstructing it from a conversation. Auditability degrades if commands are logged as one opaque script invocation instead of granular steps, since a single exit code then hides everything that happened inside it."
  evidence_strength: "Strong"
  adoption:
    status: "Partially Adopted"
    notes: "Reported as production-tested and credited as the specific enabling condition for the longest reported run of a multi-agent coding mission (16 days) in the source system. Not yet observed as a machine-checkable (structured-data) implementation — the reported use is a prose-filled schema read by a human-supervised orchestrator, not a fully automated one."
contract:
  preconditions: "A worker (human or agent) is completing a bounded unit of work inside a larger multi-step or multi-day mission, and hands control back to an orchestrator or to the next worker in sequence. The orchestrator has defined procedures the worker is expected to follow. The orchestrator (or a downstream reader) will read accumulated handoffs at milestone boundaries to decide what happens next."
  invariants: "Every handoff states all five fields at the moment work ends: what was completed, what was explicitly left undone, every command run paired with its exit code, issues discovered during the work, and whether the worker's actual behavior followed the defined procedure. 'Left undone' is never inferred from silence — it must be named. A handoff is never replaced by an unstructured 'done' report for the same boundary."
  governance: "Owner: whoever defines the worker-to-orchestrator (or worker-to-worker) reporting contract for a given multi-agent or human-plus-agent mission — e.g., the author of an orchestrator's completion protocol or a mission's handoff convention. That owner is responsible for keeping all five fields intact if the schema is adapted, and for deciding how granular command logging must be (single script vs. individual commands) to keep the commands-and-exit-codes field meaningful. Any downstream tooling that audits mission health checks for presence of all five fields on every handoff."
  recovery: "If a handoff surfaces left-undone items or discovered issues, the orchestrator scopes corrective work precisely from what is documented, rather than re-deriving it from scratch. If a handoff's command log is a single opaque invocation with no internal detail, treat the completion claim as unverified until a more granular account is available. If handoffs accumulate but the orchestrator does not read them at milestone boundaries, the schema's information is captured but not used — this is a process failure to surface in review, not a schema failure; the schema cannot self-heal a mission whose handoffs go unread."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-orchestration"
  - "task-handoff"
  - "multi-agent-coordination"
---

# Worker Handoff Schema Template

**Source:** [[structured-handoff-schema-self-healing-multi-agent-missions]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{WORKER_ID}}` | string | Identifier of the worker (agent or human) filing the handoff. |
| `{{TASK_ID}}` | string | Identifier of the bounded unit of work (feature, ticket, phase) this handoff closes out. |
| `{{COMPLETED}}` | list of strings | What was actually finished during this unit of work — stated as accomplished facts, not intentions. |
| `{{LEFT_UNDONE}}` | list of strings (explicit; empty list, not omission, if nothing was left undone) | What was in scope but explicitly NOT completed. Never inferred by the reader from what `{{COMPLETED}}` fails to mention — the worker states it directly. |
| `{{COMMANDS_RUN}}` | list of (command, exit code) pairs | Every command executed during the work, paired with its exit code. Granular enough that a single entry doesn't hide multiple sub-steps behind one exit code. |
| `{{ISSUES_DISCOVERED}}` | list of strings | Problems, surprises, or risks found during the work, whether or not they blocked completion of `{{TASK_ID}}`. |
| `{{PROCEDURE_COMPLIANCE}}` | string (compliant, or a description of the deviation) | Whether the worker's actual behavior followed the procedure the orchestrator defined for this kind of task, and — if not — exactly how it diverged. |

## Body

```
WORKER HANDOFF: {{WORKER_ID}} — {{TASK_ID}}

COMPLETED
{{COMPLETED}}

LEFT UNDONE
{{LEFT_UNDONE}}

COMMANDS RUN (command -> exit code)
{{COMMANDS_RUN}}

ISSUES DISCOVERED
{{ISSUES_DISCOVERED}}

PROCEDURE COMPLIANCE
{{PROCEDURE_COMPLIANCE}}
```

## Usage

Render this template at the end of every worker's bounded unit of work — in place of a free-text "done" message — whenever the worker's output feeds an orchestrator or another worker that did not observe the work directly.

1. **Fill all five fields before handing back control.** The worker fills the handoff itself, immediately after finishing (or stopping) the unit of work — not from memory later, and not by an orchestrator reconstructing it secondhand.
2. **State `{{LEFT_UNDONE}}` explicitly, even when empty.** The field exists specifically so the reader never has to infer gaps from silence in `{{COMPLETED}}`.
3. **Log commands at the granularity that matters.** If a single script wraps several meaningfully distinct steps, log the steps individually — one exit code covering an opaque script hides everything that happened inside it.
4. **Report `{{PROCEDURE_COMPLIANCE}}` honestly, including deviations.** The field's value is precisely in catching cases where the worker's actual behavior didn't match what was expected, not in confirming the happy path.
5. **The receiving party reads the handoff at the next milestone boundary**, not just at the very end of the mission — errors get caught, and corrective work gets scoped, from what accumulated handoffs say at each checkpoint along the way.

## Variation Axis

What drives a different rendering of this template:

- **Task-unit granularity.** A handoff can close out a single feature, a whole session, or a phase of a longer mission — the finer the granularity, the sooner errors surface, at the cost of more handoffs to read.
- **Command-log structure.** Free-text command-and-exit-code pairs work for a human-read handoff; a machine-checkable version (structured data instead of prose) lets the receiving party programmatically detect gaps — missing exit codes, unexplained left-undone items — rather than relying on a reader's comprehension.
- **Schema versioning.** For a long-running mission, whether the schema itself is versioned matters: if what counts as a "good handoff" changes partway through, unversioned schema drift silently breaks comparability between earlier and later handoffs.
- **Escalation on deviation.** Whether a non-`compliant` value in `{{PROCEDURE_COMPLIANCE}}` triggers an automatic pause for review, or is simply logged for the next milestone read, is a variation point independent of the schema's fields.

## Contract

### Preconditions
A worker (human or agent) is completing a bounded unit of work inside a larger multi-step or multi-day mission, and hands control back to an orchestrator or to the next worker in sequence. The orchestrator has defined procedures the worker is expected to follow. The orchestrator (or a downstream reader) will read accumulated handoffs at milestone boundaries to decide what happens next.

### Invariants
Every handoff states all five fields at the moment work ends: what was completed, what was explicitly left undone, every command run paired with its exit code, issues discovered during the work, and whether the worker's actual behavior followed the defined procedure. "Left undone" is never inferred from silence — it must be named. A handoff is never replaced by an unstructured "done" report for the same boundary.

### Governance
Owner: whoever defines the worker-to-orchestrator (or worker-to-worker) reporting contract for a given multi-agent or human-plus-agent mission — e.g., the author of an orchestrator's completion protocol or a mission's handoff convention. That owner is responsible for keeping all five fields intact if the schema is adapted, and for deciding how granular command logging must be (single script vs. individual commands) to keep the commands-and-exit-codes field meaningful. Any downstream tooling that audits mission health checks for presence of all five fields on every handoff.

### Recovery
If a handoff surfaces left-undone items or discovered issues, the orchestrator scopes corrective work precisely from what is documented, rather than re-deriving it from scratch. If a handoff's command log is a single opaque invocation with no internal detail, treat the completion claim as unverified until a more granular account is available. If handoffs accumulate but the orchestrator does not read them at milestone boundaries, the schema's information is captured but not used — this is a process failure to surface in review, not a schema failure; the schema cannot self-heal a mission whose handoffs go unread.
