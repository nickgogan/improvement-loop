---
name: GSD Gates Taxonomy — Four Canonical Types
summary: 'Classification of quality gates into four types: pre-flight (before action), revision (during iteration), escalation (when stuck), and abort (when unsafe).'
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General / Cross-System
adopted_in: []
sources:
- gsd-v1340-v1342-changelog.md
related_findings:
- file: agent-architecture-layer-impermanence.md
  rel: contradicts
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
---

## What It Is

A taxonomy that classifies quality gates into four canonical types. Pre-flight gates check preconditions before an action begins. Revision gates evaluate quality during iterative refinement loops. Escalation gates detect when an agent is stalled or blocked and trigger human or higher-authority intervention. Abort gates enforce safety boundaries and halt execution when constraints are violated. This is a *classification framework* for gates, not a specific gate implementation — the reference doc is wired into GSD workflows for consistent gate design.

## Why It Matters

Without a shared vocabulary for gate types, teams build ad-hoc checks that overlap, leave gaps, or fire at the wrong moment. A canonical taxonomy ensures every gate has a clear purpose and firing point in the workflow. It also makes gate coverage auditable — you can ask "do we have an escalation gate for this workflow?" rather than inspecting each check individually.

## Why People Are Using It

Agentic workflows accumulate quality checks organically, leading to inconsistent coverage — some phases have extensive validation while others have none. The four-type taxonomy provides a checklist for gate coverage: does this workflow check preconditions, monitor iteration quality, detect stalls, and enforce safety boundaries? Teams use it as a design-time reference when building new workflows.

## Potential Improvements

The taxonomy could be extended with a post-flight gate type for validating outcomes after action completion — distinct from revision gates which operate during iteration. Each gate type could carry a recommended implementation pattern (e.g., escalation gates should include a cooldown period before re-escalating). The taxonomy could also define composability rules for when multiple gate types interact.

## Potential Failure Modes

Over-classification can lead to gate proliferation — teams adding all four gate types to every workflow regardless of risk level. The taxonomy is only useful if gate implementations actually match their declared type; a "pre-flight" gate that silently passes without meaningful checks provides false assurance. The framework also risks becoming bureaucratic overhead if applied dogmatically to low-stakes workflows.
