---
title: "Receipt Schema — Sources / Changes / Needs-Approval"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "receipt-artifact-as-agent-trust-mechanism"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-governance-and-trust.harvest-queue"
identification_report: "agent-governance-and-trust.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "autonomous or semi-autonomous agents that pause at a human-review checkpoint before an action takes effect"
    - "any workflow where a human must decide whether to approve a machine-prepared draft, change, or action"
    - "teams trying to make agent output review sustainable at volume rather than re-derived from scratch each time"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "verify"
  reversibility: "trivial — an output-contract addition; removal is a deletion with no migration cost"
  auditability: "high — the receipt itself is the audit artifact; external reviewers can check whether cited sources actually support the listed changes without re-deriving the draft"
  evidence_strength: "Medium"
  adoption:
    status: "Partially Adopted"
    notes: "Demonstrated across multiple agent-build case studies (email, insurance-appeal, and tax-prep workflows) in the source material as an ad hoc case-file packet; not yet standardized as a reusable schema in general agent tooling."
contract:
  preconditions: "An agent has reached a human-review checkpoint before an action takes effect (e.g., before a draft is sent, a change is committed, or a calendar hold is confirmed). The agent has addressable pointers back to whatever source material it consulted, and can enumerate the specific changes it made relative to inputs or prior state."
  invariants: "Every gate pause emits exactly one receipt containing three non-empty sections — sources used (with addresses back to originals), changes made, and items still needing approval. The receipt accompanies the draft/action; it never substitutes for it. Citations in the receipt must be traceable back to the stored originals, not paraphrased from memory."
  governance: "Owner: any skill, agent, or output contract that stops at a human-approval gate. This schema is the minimum shape a gate-stopping output must satisfy. Consumer-side audit tooling validates that gate-stopping skills declare all three sections; a skill that stops at a human gate without emitting a receipt is under-specified."
  recovery: "If a section is empty where content is expected (e.g., sources consulted but not listed), treat the receipt as incomplete and hold the gate until it is filled — do not present an incomplete receipt as complete. If a cited source doesn't actually support its paired change entry ('receipt theater'), spot-check before approval and reject the receipt, not just the draft. If receipts grow so verbose they recreate the review burden they were meant to remove, compress to the minimum sources/changes/approval triplet per item rather than dropping a section."
tags:
  - "extracted-artifact"
  - "template"
  - "trust"
  - "human-gate"
  - "auditability"
---

# Receipt Schema — Sources / Changes / Needs-Approval

**Source:** [[receipt-artifact-as-agent-trust-mechanism]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{AGENT_OR_SKILL_NAME}}` | string | Identifies which agent/skill emitted the receipt. |
| `{{GATE_CONTEXT}}` | string | One line naming what the gate is for (e.g., "draft appeal letter ready for review", "calendar hold pending confirmation"). |
| `{{SOURCES_USED}}` | list of `(claim, source_address)` pairs | Every fact or input the draft/action relies on, each paired with an address back into the stored, chunked original (file path + section, URL + anchor, record ID). Not a bibliography — a claim-to-source map. |
| `{{CHANGES_MADE}}` | list of strings | What the agent actually did or produced, stated as concrete deltas ("added X", "changed Y from A to B"), not narrative summary. |
| `{{NEEDS_APPROVAL}}` | list of strings | The specific decisions or actions still requiring a human yes/no before they take effect. Empty only if the gate is informational and nothing downstream depends on approval. |
| `{{DRAFT_OR_ACTION_REF}}` | pointer | Where the actual draft/action artifact lives, so the receipt sits alongside it rather than replacing it. |

## Body

```markdown
## Receipt — {{AGENT_OR_SKILL_NAME}}

**Gate:** {{GATE_CONTEXT}}
**Draft/action:** {{DRAFT_OR_ACTION_REF}}

### Sources Used
- {{CLAIM_1}} — [{{SOURCE_ADDRESS_1}}]
- {{CLAIM_2}} — [{{SOURCE_ADDRESS_2}}]
<!-- one line per claim; every non-obvious factual input to the draft appears here -->

### Changes Made
- {{CHANGE_1}}
- {{CHANGE_2}}
<!-- concrete deltas, not a narrative recap -->

### Needs Your Approval
- [ ] {{APPROVAL_ITEM_1}}
- [ ] {{APPROVAL_ITEM_2}}
<!-- checklist form; each item is a distinct yes/no decision -->
```

## Usage

Render this block immediately after the agent produces a draft or proposed action and stops for human review — it is the last thing emitted before the gate, not a follow-up. The three sections are mandatory and always appear in this order (sources establish what's true, changes establish what happened, needs-approval establishes what's left to decide). If any section would be empty, that itself is a signal worth surfacing explicitly ("no external sources consulted") rather than omitting the section.

For workflows that repeat the same gate many times (e.g., a multi-document review), append successive receipts to a running log rather than discarding each after review — the log becomes the audit trail for the whole session.

## Variation Axis

- **Simple gate (single action):** three flat lists as shown above.
- **Complex gate (case-file style):** the sources/changes/approval triplet generalizes into a fuller packet — a timeline, a per-claim evidence map (have/missing), and the draft — while preserving the same three-question backbone (what did I use, what did I change, what's left for you).
- **Diff-shaped changes:** for file-mutating agents, replace the flat `{{CHANGES_MADE}}` list with an actual diff or before/after pair per item, so "what changed" is directly inspectable rather than described.
- **Accumulation mode:** for agents that pass the same gate repeatedly, render receipts as append-only log entries (timestamped) instead of one-shot documents, building a cumulative audit trail.

## Contract

### Preconditions
An agent has reached a human-review checkpoint before an action takes effect (e.g., before a draft is sent, a change is committed, or a calendar hold is confirmed). The agent has addressable pointers back to whatever source material it consulted, and can enumerate the specific changes it made relative to inputs or prior state.

### Invariants
Every gate pause emits exactly one receipt containing three non-empty sections — sources used (with addresses back to originals), changes made, and items still needing approval. The receipt accompanies the draft/action; it never substitutes for it. Citations in the receipt must be traceable back to the stored originals, not paraphrased from memory.

### Governance
Owner: any skill, agent, or output contract that stops at a human-approval gate. This schema is the minimum shape a gate-stopping output must satisfy. Consumer-side audit tooling validates that gate-stopping skills declare all three sections; a skill that stops at a human gate without emitting a receipt is under-specified.

### Recovery
If a section is empty where content is expected (e.g., sources consulted but not listed), treat the receipt as incomplete and hold the gate until it is filled — do not present an incomplete receipt as complete. If a cited source doesn't actually support its paired change entry ("receipt theater"), spot-check before approval and reject the receipt, not just the draft. If receipts grow so verbose they recreate the review burden they were meant to remove, compress to the minimum sources/changes/approval triplet per item rather than dropping a section.
