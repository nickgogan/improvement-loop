---
name: "Permission Compounding Across Agent Delegation Chains"
summary: "When agents delegate to other agents, permissions compound in ways that no single agent's access scope predicts. Each delegation step may inherit, escalate, or intersect permissions from the delegating agent, the target system, and the delegated agent's own capabilities — producing a composite permission surface that nobody designed or reviewed."
implementation_notes: null
category: "Governance"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "lilly-incident-agent-security-permissions.md"
related_findings:
  - file: "agent-identity-governance-enforcement-layer.md"
    rel: "same-problem"
  - file: "actor-passport-schema-bound-identity.md"
    rel: "extends"
  - file: "tool-gateway-security-boundary.md"
    rel: "extends"
  - file: "subagent-scope-priority-ladder.md"
    rel: "same-problem"
  - file: "capability-restricted-agent-spawning-via-allowlist.md"
    rel: "same-problem"
  - file: "screen-as-permissions-model-agent-bypass-failure.md"
    rel: "extends"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: synthesized
consumed_by:
  - "agent-governance-and-trust.md"
  - "rules/permission-compounding-across-agent-delegation-chains.md"
tags:
  - "session-95-reextract"
---

# Permission Compounding Across Agent Delegation Chains

## What It Is

A governance failure mode specific to multi-agent systems: when Agent A delegates to Agent B, Agent B's effective permissions are the compound of A's delegation scope, B's own capabilities, and the target system's access model. This compound is rarely designed explicitly — it emerges at runtime from the intersection of multiple permission systems that were each designed independently.

The video source identifies this as one of the six technical questions that developers should be asking: "How do permissions compound when agents delegate to other agents?"

**Three compounding patterns:**

1. **Inheritance**: Agent B inherits Agent A's credentials and access scope. If A has broad access (e.g., a senior consultant's 40-client access), B may inherit that entire scope even though B's task only requires single-client access.

2. **Escalation**: Agent B's own tool capabilities combine with Agent A's delegated access to produce a higher effective privilege than either agent holds alone. Agent A can read client data. Agent B can write to production. Agent A delegates to Agent B with read context. Agent B now has read + write — a privilege neither was designed to hold.

3. **Intersection gap**: Each system along the delegation chain has its own permission model. The CRM checks one set of roles. The contract management system checks another. The support system checks a third. No system checks the compound — whether the sequence of legitimate accesses across systems produces an illegitimate composite.

## Why It Matters

Human delegation naturally bounds permission compounding through screen-mediated access. When a consultant asks a colleague to review a contract, the colleague sees what their screen shows them — the screen is the permission boundary. Agent delegation has no such implicit bound. Each system the agent touches evaluates access independently, and the compound access across all systems is nobody's problem — until it produces a breach.

The Lilly incident demonstrated the single-agent version of this: one agent accessing 22 unauthenticated endpoints across a single platform. The multi-agent version is worse because the compound permission surface grows combinatorially with each delegation step.

For MetaSystem, this applies to subagent architectures where a parent agent spawns specialized subagents. The parent's permission scope must not automatically transfer to subagents. Each subagent should receive the minimum permissions required for its specific subtask — and the compound permissions across all active subagents should be auditable.

## Why People Are Using It

The video source ties this to the broader vendor convergence: Salesforce headless 360, ServiceNow action fabric, and identity-aware orchestration layers all address the composition problem by requiring that every agent action is identity-bound and auditable at the individual action level — not just at the delegation origin.

## Potential Improvements

- Implement monotonic permission narrowing: each delegation step can only reduce permissions, never expand them. Agent B's permissions must be a strict subset of Agent A's delegated scope.
- Require compound permission audits as a pre-deployment check for multi-agent workflows — enumerate all systems touched and verify the composite access is intentional.
- Apply the "authority ceiling" concept from the actor passport pattern: each agent has a maximum permission scope that cannot be exceeded regardless of what is delegated to it.

## Potential Failure Modes

- **Design-time blindness**: Permission compounds are only visible at runtime. No static analysis can predict all possible delegation chains in a dynamic multi-agent system.
- **Monotonic narrowing is too restrictive**: Some legitimate workflows require a delegated agent to access systems the delegating agent cannot — e.g., a coordinator agent delegates to a specialist with domain-specific credentials.
- **Audit overhead**: Tracking compound permissions across all delegation chains at scale may produce more audit data than reviewers can meaningfully process.
