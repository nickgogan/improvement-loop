---
title: "Three-Bucket Change Review File"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "three-bucket-change-approval-tiering"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-governance-and-trust.harvest-queue"
identification_report: "agent-governance-and-trust.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "self-improving or self-proposing systems that generate change proposals faster than a human can review each one individually"
    - "teams choosing between full automation (drift risk) and review-everything (reviewer abandonment) for a system's own proposed changes"
    - "workflows where some proposed changes are low-risk and mechanical while others require taste or judgment a system cannot yet supply"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "verify"
  reversibility: "trivial — a review-file convention; adopting or discontinuing it changes no downstream state by itself"
  auditability: "high — auto-applied changes are logged to a changelog; sign-off items are recorded as an explicit checkbox decision with a timestamp, so both tiers leave a durable trail"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented and demonstrated by a single practitioner across two sessions; not yet adopted in any tracked system at time of extraction — recorded as a design pattern, not a live deployment."
contract:
  preconditions: "A system generates its own change proposals (self-improvement, self-audit, or similar) faster than a human reviewer can inspect each one individually. The system can classify a proposed change into at least a coarse risk tier before applying or surfacing it. A human reviewer is available on some cadence (daily, per-session) to sit through a single review file."
  invariants: "Every proposed change lands in exactly one of three buckets: auto-approve (applied immediately, logged), needs-sign-off (written to the review file, held pending decision), or more-context-required (written to the same review file, held pending human input the system could not supply itself). Auto-applied changes are never silently unlogged. Needs-sign-off and more-context items are never auto-applied, regardless of how much time passes."
  governance: "Owner: whoever accepts changes into the system on the human's behalf. The bucket classifier's ruleset is itself a governance-relevant artifact — loosening it (moving categories from sign-off to auto-approve) should go through the same or a stricter gate than the changes it now waves through. 'Approve-and-don't-ask-again' selections are preference-memory writes and should periodically be reviewed as a set, not just applied."
  recovery: "If a bucket-1 (auto-approved) change turns out to have been high-stakes, that is a misclassification: revert the change, and treat the classifier rule that let it through as itself needing sign-off before it fires again. If the auto-approve surface has grown large via accumulated don't-ask-again selections, periodically re-review the accumulated ruleset as its own review-file batch. If the review file goes unread for multiple cycles, treat that as reviewer abandonment risk — the same failure mode this pattern exists to prevent — and reduce the review cadence or bucket-1 threshold rather than letting it silently pile up."
tags:
  - "extracted-artifact"
  - "template"
  - "governance"
  - "change-approval"
  - "human-gate"
---

# Three-Bucket Change Review File

**Source:** [[three-bucket-change-approval-tiering]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{REVIEW_DATE}}` | date | The date the review file was opened; also its filename component. |
| `{{CHANGELOG_PATH}}` | path | Where auto-approved (bucket-1) changes are logged. |
| `{{CHANGE_ITEM}}` | string | One proposed change, described concretely enough for a yes/no decision without re-deriving context. |
| `{{RATIONALE}}` | string | Why the system placed this item in bucket-2 or bucket-3 rather than auto-approving it. |
| `{{CONTEXT_QUESTION}}` | string (bucket-3 only) | The specific question the system needs answered before it can classify or apply the item. |

## Body

```markdown
# Change Review — {{REVIEW_DATE}}

Auto-approved changes this cycle are logged to `{{CHANGELOG_PATH}}` and not repeated here.

## Needs Sign-Off

- [ ] **{{CHANGE_ITEM_1}}** — {{RATIONALE_1}}
      _Options: approve / reject / approve-and-don't-ask-again_
- [ ] **{{CHANGE_ITEM_2}}** — {{RATIONALE_2}}
      _Options: approve / reject / approve-and-don't-ask-again_

## More Context Required

- [ ] **{{CHANGE_ITEM_3}}** — {{CONTEXT_QUESTION_3}}
```

## Usage

Classify every proposed change into exactly one bucket before doing anything with it:

1. **Auto-approve** — low-risk, mechanical, not-up-for-debate (e.g., cleanup, obvious linkage fixes). Apply immediately; append one line to the changelog per change so the human can audit after the fact without gating before it.
2. **Needs sign-off** — anything where a wrong call degrades output quality or crosses a governance boundary (structural changes, new capability surfaces, edits to shared instructions). Append to the dated review file as a checkbox item with rationale and all three response options.
3. **More context required** — the system genuinely cannot classify the item alone (ambiguous entity resolution, a judgment call outside its evidence). Append to the same review file so the human handles buckets 2 and 3 together in one sitting.

Open one review file per cycle (per day, per session — whatever cadence the human actually sits down for). Never split sign-off and more-context items across separate files; the point is one sitting, one decision pass. When the human selects "approve-and-don't-ask-again," record that as a preference-memory rule so the same class of future item routes to bucket-1 — this is the compounding mechanism that shrinks review load over time.

## Variation Axis

- **Cadence:** daily review file vs. per-session vs. per-batch — driven by how fast proposals accumulate and how often the human is willing to review.
- **Bucket granularity:** the base pattern uses exactly three buckets; resist adding a fourth (e.g., "auto-approve with delayed notification") until the two-bucket-plus-context split proves insufficient in practice.
- **Preference-memory scope:** don't-ask-again rules can be scoped narrowly (this exact change) or broadly (this whole class of change) — broader scope compounds faster but raises the misclassification blast radius; periodically re-review the accumulated ruleset as its own batch.
- **Changelog verbosity:** a changelog can be a one-line-per-change ledger or a fuller diff-style record; the review-file pattern only requires that bucket-1 changes are logged somewhere, not any particular log shape.

## Contract

### Preconditions
A system generates its own change proposals (self-improvement, self-audit, or similar) faster than a human reviewer can inspect each one individually. The system can classify a proposed change into at least a coarse risk tier before applying or surfacing it. A human reviewer is available on some cadence (daily, per-session) to sit through a single review file.

### Invariants
Every proposed change lands in exactly one of three buckets: auto-approve (applied immediately, logged), needs-sign-off (written to the review file, held pending decision), or more-context-required (written to the same review file, held pending human input the system could not supply itself). Auto-applied changes are never silently unlogged. Needs-sign-off and more-context items are never auto-applied, regardless of how much time passes.

### Governance
Owner: whoever accepts changes into the system on the human's behalf. The bucket classifier's ruleset is itself a governance-relevant artifact — loosening it (moving categories from sign-off to auto-approve) should go through the same or a stricter gate than the changes it now waves through. "Approve-and-don't-ask-again" selections are preference-memory writes and should periodically be reviewed as a set, not just applied.

### Recovery
If a bucket-1 (auto-approved) change turns out to have been high-stakes, that is a misclassification: revert the change, and treat the classifier rule that let it through as itself needing sign-off before it fires again. If the auto-approve surface has grown large via accumulated don't-ask-again selections, periodically re-review the accumulated ruleset as its own review-file batch. If the review file goes unread for multiple cycles, treat that as reviewer abandonment risk — the same failure mode this pattern exists to prevent — and reduce the review cadence or bucket-1 threshold rather than letting it silently pile up.
