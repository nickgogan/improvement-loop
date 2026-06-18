---
name: "Cross-System Permission Composition Audit Gap"
summary: "When an agent crosses permission boundaries across multiple backend systems (CRM, support, contracts, wiki), each system evaluates access independently. No system checks whether the composite access across all systems is legitimate. The audit trail for the sequence of cross-system accesses must compose — but composition of audit trails across independently-governed systems does not exist by default."
implementation_notes: null
category: "Governance"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "lilly-incident-agent-security-permissions.md"
related_findings:
  - file: "screen-as-permissions-model-agent-bypass-failure.md"
    rel: "extends"
  - file: "mcp-enterprise-governance-gaps.md"
    rel: "same-problem"
  - file: "runtime-governance-gap-buildtime-to-production.md"
    rel: "same-problem"
  - file: "agent-identity-governance-enforcement-layer.md"
    rel: "same-problem"
  - file: "unified-tracing-opentelemetry-for-agents.md"
    rel: "extends"
  - file: "permission-compounding-across-agent-delegation-chains.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: synthesized
consumed_by:
  - "agent-governance-and-trust.md"
tags:
  - "session-95-reextract"
---

# Cross-System Permission Composition Audit Gap

## What It Is

A structural gap in how permissions and audit trails compose across independently-governed systems when an agent operates across multiple backends in a single workflow.

The video source walks through a concrete scenario: an agent preparing a renewal brief pulls from CRM, support tickets, contract management, product usage data, call transcripts, and an internal wiki. Each system has its own permissions model, its own audit log, and its own definition of authorized access. For a human, the screen mediates all of this invisibly — the human opens each system and sees what they're allowed to see. For an agent, each system must be queried programmatically with explicit authentication, and each query must be auditable.

**Three composition problems:**

1. **Permission composition**: Each system grants access independently. System A says yes, System B says yes, System C says yes. But the composite — reading A's data, correlating it with B's data, and writing a synthesis to C — may violate a policy that no individual system knows about. No system evaluates the composite.

2. **Audit trail composition**: When a regulator asks "what happened in this sequence?", each system can answer for its own portion. But composing the audit trails across systems into a coherent narrative of what the agent did, in what order, across which boundaries — this does not exist by default. It requires engineering work against a deadline before the agent ships.

3. **Staleness composition**: The agent pulls from a wiki with stale pages, correlates with fresh CRM data, and produces a synthesis that blends stale and fresh information without distinguishing them. A human would notice ("this wiki page looks old") because humans read with judgment. Agents process data without freshness awareness unless explicitly designed to check.

## Why It Matters

The video source's key framing: "None of this exists by default. All of it is engineering work that someone has to do against a deadline before the agent ships. And that's just for one task. Multiply that by all the workflows your roadmap promises to automate."

This is the scaling dimension that makes agentic systems categorically different from SaaS. SaaS is bounded — a vendor gives you an admin console, integration points, a published API, and a permissions model. Agent workflows are unbounded — every new workflow may cross new system boundaries, each with its own permission and audit requirements.

For MetaSystem, this applies to any workflow where an agent reads from multiple data sources (research findings + governance docs + source files) and produces a synthesized output. The composition of what was read, from where, with what freshness, under what authority, should be traceable.

## Why People Are Using It

The vendor convergence documented in the source illustrates market recognition of this gap: Salesforce headless 360 exposes APIs because "agents don't click through screens." ServiceNow action fabric provides governed workflow surfaces "with identity and audit attached." Pinecone Nexus addresses context assembly ("stop making your agent rebuild the business from scratch every time it runs"). Each vendor is selling one piece of the composition solution.

## Potential Improvements

- Implement cross-system correlation IDs: every agent run generates a unique trace ID that is passed to every system the agent touches, enabling post-hoc composition of audit trails.
- Add freshness metadata to all data retrieved by agents — timestamp of last update, staleness threshold, confidence level.
- Design a "permission manifest" that declares all systems an agent workflow will touch, reviewed and approved before deployment.

## Potential Failure Modes

- **Correlation ID overhead**: Passing trace IDs through systems that don't natively support them requires custom middleware for each integration.
- **Audit trail volume**: Full cross-system audit trails for every agent run may produce more data than is practical to store or review.
- **Permission manifest drift**: The declared manifest may not match what the agent actually does at runtime, especially if the agent dynamically discovers which systems to query based on the task.
