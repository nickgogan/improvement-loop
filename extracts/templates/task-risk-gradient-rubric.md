---
title: "Task Risk Gradient Rubric"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "task-risk-gradient-for-verification-depth"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "verifying-agent-output.harvest-queue"
identification_report: "verifying-agent-output.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams calibrating how much review or verification effort a task deserves, across a domain with many task types"
    - "designing or auditing a review/verification process that currently applies uniform depth regardless of consequence"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "verify"
  reversibility: "trivial — a classification worksheet; mis-tiering a task is corrected by re-classifying it, with no structural cost"
  auditability: "medium — the tier assignment is visible and inspectable, but the judgment behind 'how far does this claim travel' is not independently verifiable without provenance tracking"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A domain has multiple recognizable task or artifact types, and the team currently applies a single review depth (or none) uniformly across all of them rather than scaling effort by consequence."
  invariants: "Every task type in scope is assigned exactly one tier (low, medium, high) before work begins, not retroactively. The tier assignment is driven by consequence of a wrong output and how far the output travels (who acts on it downstream), not by the task's local complexity or the tool used to produce it. High-tier classification is never skipped under deadline pressure without an explicit, documented override."
  governance: "Owner: whoever owns the review or verification process for the domain. Tier definitions are domain-specific and must be documented per domain (a 'low' in one domain is not equivalent to a 'low' in another). Re-tiering an artifact (e.g., a scratch draft gets promoted to a board document) requires an explicit re-classification, not a silent carry-over of the original tier."
  recovery: "If a task is discovered to be under-reviewed relative to its actual downstream mobility (an artifact was promoted without re-tiering), immediately apply the correct tier's review depth retroactively before the artifact is used further. If gradient definitions are being gamed (tasks classified optimistically to avoid review burden), tighten the tier criteria or add a spot-audit step rather than removing the gradient."
tags:
  - "extracted-artifact"
  - "template"
  - "verification"
  - "risk-calibration"
---

# Task Risk Gradient Rubric

**Source:** [[task-risk-gradient-for-verification-depth]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Description |
|----------|-------------|
| `{{DOMAIN}}` | The domain being classified (e.g., document production, code review, governance drafting) |
| `{{LOW_RISK_EXAMPLES}}` | Task or artifact types in this domain where wrongness is cheap and visible |
| `{{MEDIUM_RISK_EXAMPLES}}` | Task or artifact types where wrongness propagates but stays traceable |
| `{{HIGH_RISK_EXAMPLES}}` | Task or artifact types where wrongness is expensive, hard to spot, and travels to a consequential decision |
| `{{TASK_NAME}}` | The specific task or artifact instance being classified |
| `{{DOWNSTREAM_CONSUMER}}` | Who or what acts on this task's output next |

---

## Body

# Task Risk Gradient — {{DOMAIN}}

| Tier | Criteria | Examples in this domain | Review depth |
|---|---|---|---|
| **Low** | Wrongness is cheap and visible; errors are caught on casual inspection | `{{LOW_RISK_EXAMPLES}}` | Light — spot-check or none |
| **Medium** | Wrongness propagates but stays traceable back to its source | `{{MEDIUM_RISK_EXAMPLES}}` | Moderate — verify against source |
| **High** | Wrongness is expensive, invisible, and mobile — the output travels to a consequential decision | `{{HIGH_RISK_EXAMPLES}}` | Full — hostile review, human gate mandatory |

### Per-task classification

**Task:** {{TASK_NAME}}
**Downstream consumer:** {{DOWNSTREAM_CONSUMER}}
**Assigned tier:** low ▢ / medium ▢ / high ▢
**Rationale:** _______________
**Review depth applied:** _______________

---

## Usage

Classify each task or artifact type in a domain into the three tiers before work begins — this produces a standing gradient for the domain, not a one-off judgment. Apply the corresponding review depth automatically once a task is tiered; use the per-task classification block to tier individual instances that don't obviously fall into a pre-classified type, or to re-tier an artifact whose downstream mobility has changed (a scratch draft that gets promoted to something leadership will see).

The model or tool helps at every tier — the gradient does not gate AI assistance itself, only how much verification investment follows it. Keep the human gate mandatory on high-tier items regardless of how confident the output looks.

## Variation Axis

Tier definitions and examples are domain-specific and must be re-instantiated per domain — do not reuse one domain's `{{LOW_RISK_EXAMPLES}}` / `{{HIGH_RISK_EXAMPLES}}` as another's:

- **Document production:** low = formatting, layout, chart drafts, summary wording; medium = source attribution, data extraction; high = numerical synthesis, financial calculations, regulatory language, claims that travel to leadership.
- **Code:** low = generated tests, formatting; medium = business-logic changes with test coverage; high = authentication, authorization, payment, or migration logic.
- **Governance or policy drafting:** low = prose polish, wording clarity; medium = procedural updates; high = binding rule text, constraints that gate other agents' authority.

The sharpest classification signal across all domains is **mobility** — does this specific output get reused or quoted somewhere consequential — not local complexity.
