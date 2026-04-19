---
title: "Five Commandments for Agent Deployment (Audit-First Framework)"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "five-commandments-for-agent-deployment-audit-first"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Agent deployment scope is defined. A human decision-maker is identified. All five commandments are evaluated in sequence. Practitioners are accessible for Commandment 1 audit."
  invariants: "Each commandment gate is a hard blocking dependency. Deployment GO requires all five gates passed. Observability is live before agent processes production input. Authority scope is approved by human decision-maker."
  governance: "Owner: MetaSystem governance layer. Applicable to all agent deployments. Modifications require a DD. Nick is the human gate for MetaSystem-scope deployments."
  recovery: "If a gate fails: document the gap, assign remediation ownership, set re-evaluation date. If unauthorized bypass: flag as governance violation, file IB item, schedule post-deployment audit within 30 days."
tags:
  - "extracted-artifact"
  - "skill"
---

# Five Commandments for Agent Deployment (Audit-First Framework)

**Source:** [[five-commandments-for-agent-deployment-audit-first]]
**Form:** skill
**Extraction date:** 2026-04-19

## Purpose

A prerequisite framework for responsible agent deployment. Prevents the "celebration on day one, crisis on day 30" failure mode by enforcing five sequential prerequisites before an agent goes live.

## Inputs

- Agent deployment scope: what the agent will do, what systems it will touch, what authority it will have
- Current process documentation (or absence thereof)
- Data inventory: what sources the agent will read or write
- Org structure and throughput capacity
- Defined authority boundaries

## Outputs

- Audit report: actual process map including edge cases and tribal knowledge
- Data readiness assessment: source of truth, schemas, validation, conflict resolution
- Org throughput plan: capacity model given agent-level production output
- Observability spec: independent evaluation, audit trail design, automated verification
- Authority scope document: guardrail definitions, hard stops, escalation paths
- Deployment gate decision: GO / NO-GO with rationale for each commandment

## Steps

### Commandment 1 — Audit Before You Automate
1. Map the actual process, not the idealized one. Interview practitioners.
2. Document edge cases, exception handling, and tribal knowledge.
3. Identify failure modes in the current human process.
4. Gate: deployment does not proceed until the process map is complete and reviewed.

### Commandment 2 — Fix the Data First
1. Establish a single source of truth for every data input.
2. Define schemas for all inputs and outputs.
3. Build validation — agent must detect and reject malformed input.
4. Decide conflict resolution.
5. Gate: deployment does not proceed until data infrastructure passes validation tests.

### Commandment 3 — Redesign the Org for Throughput
1. If the agent 10x's production capacity, the org must consume 10x output.
2. Map the full value chain. Identify bottlenecks.
3. Hire, restructure, or automate downstream steps before the agent goes live.
4. Gate: deployment does not proceed until throughput capacity matches projected output.

### Commandment 4 — Build Observability from Day One
1. Establish independent evaluation of agent outputs — not agent self-reporting.
2. Build audit trails: every action logged with inputs, outputs, timestamps.
3. Build automated verification against ground truth.
4. Define alert thresholds.
5. Gate: deployment does not proceed until observability is live and tested.

### Commandment 5 — Scope Authority Deliberately
1. Define explicitly what the agent can do.
2. Define explicitly what the agent cannot do.
3. Build guardrails that enforce limits technically, not just by instruction.
4. Gate: deployment does not proceed until authority scope is approved and guardrails tested.

## Failure Modes

- **Sequential thoroughness under pressure.** Framework is slow by design. Treat each gate as a literal blocking dependency.
- **Process maturity assumption.** For greenfield deployments, treat Commandment 1 as process design, not discovery.
- **Org redesign resistance.** Escalate to decision-maker authority before deployment begins.

## Contract

### Preconditions
Agent deployment scope is defined. A human decision-maker is identified. All five commandments are evaluated in sequence. Practitioners are accessible for Commandment 1 audit.

### Invariants
Each commandment gate is a hard blocking dependency. Deployment GO requires all five gates passed. Observability is live before agent processes production input. Authority scope is approved by human decision-maker.

### Governance
Owner: MetaSystem governance layer. Applicable to all agent deployments. Modifications require a DD. Nick is the human gate for MetaSystem-scope deployments.

### Recovery
If a gate fails: document the gap, assign remediation ownership, set re-evaluation date. If unauthorized bypass: flag as governance violation, file IB item, schedule post-deployment audit within 30 days.
