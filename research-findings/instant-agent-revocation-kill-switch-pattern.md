---
name: Instant Agent Revocation (Kill Switch Pattern)
summary: Production agent systems require the ability to revoke an agent's access within minutes — not through code deploys, tickets, or deletion, but through a console-level immediate revocation. Without
  this, incident response for agent misbehavior has an unbounded window during which a compromised or malfunctioning agent continues operating.
implementation_notes: null
category: Governance
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- lilly-incident-agent-security-permissions.md
related_findings:
- file: graceful-degradation-modes-for-agent-failure.md
  rel: same-problem
- file: agent-identity-governance-enforcement-layer.md
  rel: extends
- file: tool-gateway-security-boundary.md
  rel: extends
- file: screen-as-permissions-model-agent-bypass-failure.md
  rel: same-problem
- file: advisory-only-for-persistent-mutations.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- extracts/rules/instant-agent-revocation-kill-switch.md
- agent-governance-and-trust.md
tags:
- session-95-reextract
---

# Instant Agent Revocation (Kill Switch Pattern)

## What It Is

A production governance requirement: any agent operating in a system must be revocable within minutes by a human operator, without requiring a code deploy, a ticket, or a deletion process. The revocation surface must be:

1. **Immediate** — takes effect within the current execution window, not the next deployment cycle
2. **Console-accessible** — operable by an incident responder who may not be a developer
3. **Granular** — revokes the specific agent's access without shutting down the entire system
4. **Auditable** — the revocation itself is logged with who, when, and why

The video source poses the diagnostic question: "Can someone from a console revoke the agent's access in the next 5 minutes while you figure out what happened?" If the answer is no, the incident response plan has a gap that will only be discovered during a tabletop exercise or at 3 AM during a real incident.

## Why It Matters

The Lilly/McKinsey incident demonstrated that when an agent gains unauthorized access, the blast radius is unbounded and operates at machine speed. Tens of millions of records were accessible. The speed asymmetry between agent action and human response creates a window during which damage accumulates. The kill switch pattern shrinks that window to the minimum achievable latency.

For agentic systems, this is categorically different from SaaS incident response. SaaS systems are bounded — the vendor controls the surface area, and disabling a user account is a standard capability. Agent systems cross permission boundaries across multiple backend systems, and there may be no single "disable" button because the agent's access was assembled ad-hoc across multiple service endpoints.

The kill switch must therefore operate at the identity/credential layer (revoking the agent's authentication tokens across all systems it can reach), not at the application layer (disabling a feature flag in one system).

## Why People Are Using It

ServiceNow's action fabric and Anthropic's enterprise services both include governed workflow surfaces with identity and audit attached — which implicitly provide a revocation point. The video source identifies this as one of six vendor announcements converging on the same architectural gap: agents need identity-aware, revocable access surfaces.

## Potential Improvements

- Implement as a pre-requisite for any agent deployment: no agent ships to production without a documented revocation procedure that has been tested.
- Combine with time-boxed credential leases (from the JIT identity provisioning pattern) so that agent access auto-expires even if no one pulls the kill switch.
- Add a "dead man's switch" variant: agent must periodically re-authenticate to maintain access. Failure to re-authenticate results in automatic revocation.

## Potential Failure Modes

- **Partial revocation**: The kill switch disables the agent's primary credential but not all service-specific tokens, leaving residual access.
- **Cascade failure**: Revoking one agent's access breaks a multi-agent workflow, causing collateral damage to agents that depended on the revoked agent's outputs.
- **False positive revocation**: Overly sensitive monitoring triggers revocation on a healthy agent, causing unnecessary downtime.
- **Revocation lag**: The revocation signal takes effect at the identity layer but cached credentials allow the agent to continue operating until cache TTL expires.
