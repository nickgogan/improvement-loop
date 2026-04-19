---
name: DX Review — Developer Experience Audit
summary: Developer experience review as a distinct specialist skill evaluating setup friction, API ergonomics, documentation quality, error messages, and onboarding flow.
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General / Cross-System
adopted_in: []
sources:
- gstack-v01590-v015160-changelog.md
related_findings:
- file: gstack-review-army-parallel-specialist-dispatch.md
  rel: extends
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: raw
consumed_by: []
---
# DX Review — Developer Experience Audit

## What It Is
Developer experience review skills (`/plan-devex-review` + `/devex-review`) as a distinct specialist review category in gstack's skill taxonomy. Unlike code review (which evaluates correctness, security, and performance), DX review evaluates the usability of a codebase or feature for developers: setup friction, API ergonomics, documentation quality, error messages, and onboarding flow. The two-phase pattern — plan the DX review first, then execute — mirrors gstack's plan-then-execute discipline. Part of gstack's 31-skill taxonomy.

## Why It Matters
Developer experience is a leading indicator of adoption and maintenance burden. Poor DX (confusing error messages, undocumented setup steps, inconsistent APIs) compounds over time as more developers interact with the codebase. Treating DX as a reviewable dimension — on par with security or performance — ensures it gets systematic attention rather than ad-hoc complaints.

## Why People Are Using It
gstack separates DX review from code review because the evaluation criteria are fundamentally different. Code review asks "is this correct and safe?" while DX review asks "is this usable and learnable?" The two-phase pattern (plan then execute) allows scoping the DX review to the most impactful surfaces before investing review effort.

## Potential Improvements
DX review could incorporate actual developer feedback data (support tickets, onboarding time metrics) alongside static analysis. The review dimensions could be weighted by audience — internal developer DX priorities differ from public API DX priorities. Automated DX scoring (e.g., measuring time-to-first-successful-API-call in a sandbox) could complement the review skill.

## Potential Failure Modes
DX is inherently subjective — different developers have different ergonomic preferences. Without calibration against real developer feedback, DX reviews may optimize for the reviewer's preferences rather than the target audience. The two-phase pattern adds overhead that may not be justified for small surface areas.
