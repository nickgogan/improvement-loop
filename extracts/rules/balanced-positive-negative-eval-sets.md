---
title: "Balanced Positive and Negative Eval Sets"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "balanced-positive-negative-eval-sets"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An eval suite exists or is being designed for an agent decision axis. The capability has at least one identifiable scenario where restraint is correct."
  invariants: "Every eval suite used to drive optimization contains documented negative cases. Class balance is reviewed whenever new cases are added."
  governance: "Owner: MetaSystem / Claude Build system. Modifications require Nick's authorization. Applies at eval design gate."
  recovery: "If positive-only suite found after optimization: halt further optimization, reconstruct with negative cases, re-run from last known-balanced checkpoint."
tags:
  - "extracted-artifact"
  - "rule"
---

# Balanced Positive and Negative Eval Sets

**Source:** [[balanced-positive-negative-eval-sets]]
**Form:** rule
**Extraction date:** 2026-04-19

## Condition

When designing or reviewing an eval suite for any agent decision (tool call, action, restraint), and the suite contains only cases where the agent should act.

## Action

Eval suites MUST include explicit negative cases — scenarios where the correct behavior is restraint or inaction — alongside positive cases where action is required. The ratio must be calibrated to the expected real-world distribution, not defaulted to 50/50.

## Boundary

Enforced at eval suite design time, before any agent optimization or fine-tuning run begins. Must be reviewed when a new agent capability or tool is added.

## Enforcement

- Eval suite MUST contain at least one documented negative case per positive case category.
- Negative cases must be distinct from positive cases by the decision axis being tested.
- Suite review gate must include a class-balance inspection step before results drive optimization.
- Anti-pattern flag: Any eval suite where 100% of examples result in action is automatically flagged as incomplete.

## Rationale

Class imbalance in evals produces class-imbalanced agent behavior. When optimization pressure is applied to a suite that only rewards action, the agent learns to always act. Claude.ai's web search overtriggering — caused by early evals that only tested "should search" scenarios — required many rounds of refinement to correct after rebalancing.

## Contract

### Preconditions
An eval suite exists or is being designed for an agent decision axis. The capability has at least one identifiable scenario where restraint is correct.

### Invariants
Every eval suite used to drive optimization contains documented negative cases. Class balance is reviewed whenever new cases are added.

### Governance
Owner: MetaSystem / Claude Build system. Modifications require Nick's authorization. Applies at eval design gate.

### Recovery
If positive-only suite found after optimization: halt further optimization, reconstruct with negative cases, re-run from last known-balanced checkpoint.
