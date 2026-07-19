---
title: "Dispatch Table Schema Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "self-improvement-dispatch-table-route-never-reimplement"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "production-agent-execution.harvest-queue"
identification_report: "production-agent-execution.harvest-queue.md::self-improvement-dispatch-table-route-never-reimplement::template::dispatch-table-schema-template"
deployed: false
deployed_to: null
context:
  applies_to:
    - "an agent or skill package that owns an ongoing observation or retro loop and needs to route classified findings to other specialized skills without absorbing their remediation logic"
    - "teams designing an umbrella dispatcher capability that must stay bounded in scope as new finding types are discovered over time"
    - "operators who want an auditable, human-amendable table governing which capability owns which class of recurring issue"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a markdown reference table; adding, editing, or retiring a row has no downstream migration cost beyond the review the amendment itself goes through"
  auditability: "high — the table is a human-readable artifact; compliance is checkable by comparing which capability actually handled a given finding against the table's Route column, and confirming an evidence trace exists for each dispatched row"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Demonstrated in one production agentic system's self-improvement loop; a single retro run classified ten findings across internal lessons, harvested eval material, store hygiene, and operator-awareness items, each row carrying an evidence trace."
contract:
  preconditions: "The dispatching capability has a live intake or observation loop that regularly produces raw findings. At least one other specialized capability already exists that should own remediation for some class of those findings. The operator can name, for each class, which file or capability — if edited — would prevent recurrence."
  invariants: "Classification keys on owning surface (which file or capability, if fixed, prevents recurrence), never on topic. Every class row states signals, route, and residual duty — including 'none' explicitly rather than an empty cell. An unmatched finding never invents a new route; it becomes an internal lesson with the operator flagged. Recommending a route is autonomous; invoking the routed capability requires asking first. The table itself is amended only through the same human-gated promotion path used for any other change to the dispatching capability."
  governance: "Owner: the operator or team maintaining the dispatching capability. The table ships inside that capability's own package and versions with it. Any agent that proposes a new row or a route change surfaces the proposal for operator approval before the table is edited — the table is never self-amended mid-run."
  recovery: "If a class's designated route no longer exists or its scope has moved: treat as class-boundary drift, audit the row, and either re-point the route or retire the class through the normal promotion gate — do not silently re-implement the fix locally in the dispatcher. If residual-duty rows are found to be doing more than recording (i.e., scope creep into the routed capability's job), trim the row back to record-only duties at the next audit. If two classes both plausibly match one finding, split the finding: route the part that matches an existing class, keep the remainder as an internal lesson."
tags:
  - "extracted-artifact"
  - "template"
  - "dispatch-table"
  - "routing"
  - "skill-boundaries"
---

# Dispatch Table Schema Template

**Source:** [[self-improvement-dispatch-table-route-never-reimplement]]
**Form:** template
**Extraction date:** 2026-07-19

A reference-table schema for any capability that owns an observation or intake loop but must not become a monolith. One row per finding class, keyed on owning surface rather than topic, carrying three fields per row: how to recognize the class, which capability owns fixing it, and what the dispatching capability itself still does even after handing the fix away. Unmatched findings never invent a new route — they fall through to an internal-lesson row with the operator flagged, and the table itself changes only through the dispatching capability's own human-gated amendment path.

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{DISPATCHER_NAME}}` | string | The umbrella capability (skill/agent/loop) that owns this table and the observation surface feeding it. |
| `{{FINDING_CLASS}}` | string, repeating | A named category of finding the intake loop may produce (e.g., "external corpus drift", "stale platform claim", "internal operational lesson"). |
| `{{SIGNALS}}` | string, repeating | How to recognize an instance of this class — the observable cue that triggers this row rather than another. |
| `{{ROUTE}}` | string, repeating | The capability that owns remediation for this class, or `internal` if `{{DISPATCHER_NAME}}` owns it end-to-end. |
| `{{RESIDUAL_DUTY}}` | string, repeating | What `{{DISPATCHER_NAME}}` still does for this class even after routing (e.g., "records the manifest row and evidence trace only"; "harvests the raw material, never applies the fix"). Never blank — use `none` explicitly if there is truly no residual duty. |
| `{{UNKNOWN_CLASS_FALLBACK}}` | string | The fixed fallback behavior when a finding matches no row — normally "becomes an internal lesson; operator flagged" — never a newly invented route. |

## Body

```markdown
# Dispatch Table — {{DISPATCHER_NAME}}

Classification keys on owning surface (which file or capability, if edited, prevents
recurrence) — never on topic. If a finding plausibly fits two rows, split it: route the
part that matches, keep the remainder here as an internal lesson.

| Finding Class | Signals | Route | Residual Duty |
|---|---|---|---|
| {{FINDING_CLASS}} | {{SIGNALS}} | {{ROUTE}} | {{RESIDUAL_DUTY}} |
| {{FINDING_CLASS}} | {{SIGNALS}} | {{ROUTE}} | {{RESIDUAL_DUTY}} |
| Internal operational lesson (residual) | Anything not matched above | internal | Owned end-to-end by {{DISPATCHER_NAME}} through its normal promotion gate |

## Unmatched Findings

{{UNKNOWN_CLASS_FALLBACK}}

## Amendment Rule

This table is edited only through {{DISPATCHER_NAME}}'s own human-gated promotion path.
No agent invents a new route at runtime — an unmatched finding always falls to the
Internal Operational Lesson row until the operator explicitly adds or amends a row.

## Autonomy Note

Recommending a route (writing a manifest row citing this table) is autonomous.
Invoking the routed capability is a new unit of work — ask the operator first.
```

## Usage

Render this when a capability's own retro or intake loop risks re-implementing fixes that belong to other capabilities. Enumerate the finding classes the loop has actually observed (start from real history, not speculation), fill signals and route per class, and be explicit about residual duty — this is the field most likely to be skipped, and skipping it is exactly where scope creep re-enters. Ship the rendered table inside the dispatching capability's own package so it versions with it. Every dispatch the loop performs should cite a row from this table in its output (a manifest line), not an ad hoc justification.

## Variation Axis

What drives different renderings of this template:

- **Number of classes** — a young loop may start with two or three rows (an internal-lesson catch-all plus one or two known external classes); mature loops accumulate more as new finding types are observed in practice. Do not pre-populate speculative classes that have never actually occurred.
- **Residual-duty granularity** — some deployments record only "manifest row, nothing else"; others (e.g., a class producing raw material another capability will later process) carry a heavier residual duty like harvesting and staging that material without applying the fix. State it explicitly either way.
- **Autonomy split** — whether *recommending* a route and *invoking* the routed capability are both autonomous, both gated, or split (recommend autonomous / invoke gated, as in the source system) is a per-deployment choice the table's Amendment Rule and Autonomy Note sections should state plainly.
- **Amendment cadence** — how often the table is expected to be reviewed for stale routes (roster changes, retired capabilities) versus amended reactively when a genuinely new class first appears.

## Contract

### Preconditions
The dispatching capability has a live intake or observation loop that regularly produces raw findings. At least one other specialized capability already exists that should own remediation for some class of those findings. The operator can name, for each class, which file or capability — if edited — would prevent recurrence.

### Invariants
Classification keys on owning surface (which file or capability, if fixed, prevents recurrence), never on topic. Every class row states signals, route, and residual duty — including 'none' explicitly rather than an empty cell. An unmatched finding never invents a new route; it becomes an internal lesson with the operator flagged. Recommending a route is autonomous; invoking the routed capability requires asking first. The table itself is amended only through the same human-gated promotion path used for any other change to the dispatching capability.

### Governance
Owner: the operator or team maintaining the dispatching capability. The table ships inside that capability's own package and versions with it. Any agent that proposes a new row or a route change surfaces the proposal for operator approval before the table is edited — the table is never self-amended mid-run.

### Recovery
If a class's designated route no longer exists or its scope has moved: treat as class-boundary drift, audit the row, and either re-point the route or retire the class through the normal promotion gate — do not silently re-implement the fix locally in the dispatcher. If residual-duty rows are found to be doing more than recording (i.e., scope creep into the routed capability's job), trim the row back to record-only duties at the next audit. If two classes both plausibly match one finding, split the finding: route the part that matches an existing class, keep the remainder as an internal lesson.
