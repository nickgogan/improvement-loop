---
title: "Autonomy Gradient (Not Binary Delegation)"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "autonomy-gradient-not-binary-delegation"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An agent system makes decisions with varying blast radius and reversibility. A decision taxonomy exists or can be constructed for the domain. The system supports per-decision-type configuration of oversight level."
  invariants: "Autonomy level is assigned per decision type, not per agent or per task. Assignment is based on blast radius and reversibility, not task complexity. All four levels (full autonomy, guarded, proposal-first, human-required) are available. No decision type defaults to full autonomy without explicit classification."
  governance: "Decision type classifications are reviewed when system scope changes. Promotion from lower to higher autonomy requires demonstrated track record. Misclassification incidents trigger reclassification review. The classification matrix is a governed artifact, not agent-modifiable."
  recovery: "If a decision is misclassified and causes damage, immediately reclassify to human-required, assess blast radius of the error, remediate, then reclassify to the correct level with additional safeguards."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Autonomy Gradient (Not Binary Delegation)

**Source:** [[autonomy-gradient-not-binary-delegation]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Binary autonomy models force a choice between two extremes: agents that act on everything without oversight (unsafe) or agents that ask permission for everything (bottlenecked). Neither extreme matches reality. Most agent systems handle a mix of trivial reversible decisions and critical irreversible ones, but binary gating applies the same oversight level to both.

## Forces

- **Safety vs. throughput:** More oversight catches more errors but slows the agent down on routine work. Less oversight increases speed but risks irreversible damage.
- **Simplicity vs. precision:** A binary gate (ask/don't ask) is simple to implement and reason about. A multi-level gradient is more precise but requires per-decision-type configuration.
- **Static classification vs. dynamic trust:** Decision risk is knowable in advance for some types (schema migrations are always high-risk) but context-dependent for others (a file edit may be routine or may break a critical dependency).
- **Agent capability growth vs. fixed gates:** As agents improve, decisions that once required human review become safe to delegate -- but the gating system may not evolve.

## Solution

Replace binary autonomy (autonomous vs. human-required) with a four-level gradient, assigned per decision type based on two classification criteria:

**Four autonomy levels:**

1. **Full autonomy:** Agent decides and acts. No notification required. Assign to low-blast-radius, easily reversible decisions. Examples: file formatting, index updates, log entries.

2. **Guarded:** Agent decides and acts, then reports what it did. Assign to medium-blast-radius decisions where speed matters but visibility is needed. Examples: code refactoring within a single module, configuration changes with rollback.

3. **Proposal-first:** Agent proposes a decision, waits for approval, then acts. Assign to high-blast-radius but time-insensitive decisions. Examples: new Design Decisions, cross-system changes, API contract modifications.

4. **Human-required:** Agent cannot act. Must escalate to a human. Assign to irreversible, high-blast-radius decisions. Examples: schema migrations, production deployments, data deletions, DD supersession.

**Classification criteria:**

- **Blast radius:** How many systems, users, or processes are affected by a wrong decision?
- **Reversibility:** Can the decision be undone easily? A renamed variable is fully reversible; a deployed schema migration is not.

This maps to a 2x2 matrix: low blast radius + reversible = full autonomy; high blast radius + irreversible = human-required; the other two quadrants map to guarded and proposal-first respectively.

**Progressive trust ramp (optional extension):** Start an agent at a lower autonomy level for a decision type. As it demonstrates consistent good judgment (track record), promote it to the next level. An agent that consistently makes good guarded decisions could be promoted to full autonomy for that type.

## Consequences

**Positive:**
- Maximizes agent throughput on safe, reversible decisions while preserving human oversight where it matters
- Reduces human bottleneck -- reviewers focus on high-blast-radius decisions instead of approving every action
- Maps directly to existing software engineering concepts: feature flags (reversible), database migrations (irreversible), logging (full autonomy), production deployments (human-required)
- Multiple independent sources converge on this model (Huryn, Campos, Anthropic, Nate B Jones), indicating broad practitioner validation

**Negative:**
- Per-decision-type configuration is more complex than binary gating -- requires building and maintaining a decision taxonomy
- Misclassification of blast radius leads to under-gating (unsafe) or over-gating (bottlenecked)
- Agents may not recognize when a decision's blast radius has changed due to context (a routine file edit that breaks a critical dependency)
- The gradient requires tooling support: per-tool permission tiers, notification mechanisms for guarded actions, approval workflows for proposal-first actions

## Known Uses

- Anthropic's Claude.ai, Claude Desktop, and Claude Code (April 2026): per-tool permission tiers (always allow / needs approval / block) implement the gradient directly
- Claude Code Plan Mode: implements the proposal-first tier at strategy level -- agent shows full intended plan for review/edit/approval
- Huryn's Intent Engineering Framework: four-level model documented across practitioner blogs and architecture talks
- Nate B Jones (OpenClaw production deployments): "scope authority deliberately" as the 5th commandment for agent deployment
- MetaSystem currently uses a binary human gate (DD-29), which this pattern would refine to a four-level gradient

## Contract

### Preconditions
An agent system makes decisions with varying blast radius and reversibility. A decision taxonomy exists or can be constructed for the domain. The system supports per-decision-type configuration of oversight level. All four autonomy levels have corresponding implementation mechanisms (notification for guarded, approval workflow for proposal-first, escalation for human-required).

### Invariants
Autonomy level is assigned per decision type, not per agent or per task. Assignment is based on blast radius and reversibility, not task complexity or agent confidence. All four levels are available in the system. No decision type defaults to full autonomy without explicit classification. The classification matrix is a governed artifact that agents cannot modify.

### Governance
Decision type classifications are reviewed when system scope changes or new decision types emerge. Promotion from lower to higher autonomy requires a demonstrated track record over a defined observation period. Misclassification incidents trigger immediate reclassification review. The classification matrix is maintained as a governed document with human ownership. Periodic audits verify that actual agent behavior matches assigned autonomy levels.

### Recovery
If a decision is misclassified and causes damage: immediately reclassify the decision type to human-required, assess the blast radius of the actual error, remediate the damage, then reclassify to the correct level with additional safeguards (e.g., guarded instead of full autonomy). If an agent acts beyond its assigned autonomy level, treat it as a system boundary violation and investigate the enforcement mechanism.
