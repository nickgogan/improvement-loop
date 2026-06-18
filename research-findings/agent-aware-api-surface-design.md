---
name: "Agent-Aware API Surface Design"
summary: "APIs must be designed with the assumption that autonomous agents will call them — not just human users clicking through UIs. This means every endpoint needs authentication by default, agent-specific rate limiting, scoped permissions that distinguish agent access from human access, and the ability to enforce per-task permission boundaries rather than per-user boundaries."
implementation_notes: null
category: "Agent Design"
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
  - file: "screen-as-permissions-model-agent-bypass-failure.md"
    rel: "extends"
  - file: "secure-by-default-posture-as-organizational-invariant.md"
    rel: "same-problem"
  - file: "tool-gateway-security-boundary.md"
    rel: "extends"
  - file: "agent-identity-governance-enforcement-layer.md"
    rel: "same-problem"
  - file: "mcp-enterprise-governance-gaps.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "templates/agent-aware-api-surface-audit-checklist.md"
  - agent-design-patterns.md
tags:
  - "session-95-reextract"
---

# Agent-Aware API Surface Design

## What It Is

A design principle for any API surface that may be accessed by autonomous agents: the API must be designed assuming programmatic, high-speed, machine-driven access patterns — not human-mediated, screen-constrained access patterns.

The video source traces the Lilly incident's root cause to this principle's absence: "No one asked whether the API endpoint itself was the correct shape for assuming strong agentic access on the web. We need to be assuming that the production software we put into place is going to meet AI agents."

**Key design requirements for agent-aware surfaces:**

1. **Human/agent identity distinction**: The platform must know the difference between a human user and an AI agent. A senior consultant might legitimately access 40 client accounts built over 5 years. An agent running on one client account should be bounded to that single account. If the platform cannot enforce this distinction, one agent incident becomes a company-wide exposure event.

2. **Per-task permission scoping**: Agent permissions should be scoped to the specific task, not inherited from the user's full access. A user delegates "prepare the renewal brief for Client X." The agent should access only Client X's data — not the user's entire 40-client access scope.

3. **Rate and volume awareness**: Agents operate at machine speed. An endpoint designed for human click rates (seconds between requests) will be overwhelmed by agent query patterns (milliseconds between requests). API surfaces need agent-specific rate limiting.

4. **Write-access audit**: Every write operation by an agent must be separately auditable from human writes. Regulators ask "what did the system do on behalf of the user?" — not "what did the user do?"

## Why It Matters

The Lilly platform was designed 2+ years before autonomous agents could hack through public endpoints to production data. The video source notes: "When Lilly first came out 2 years ago, we didn't have autonomous AI agents that could hack through a public endpoint and get to production data. That is something that is very normal in 2026."

This is not a retroactive criticism — it is a forward design requirement. Any API surface being built today must assume agent access because the capability exists now and will only expand. The video source identifies this as a systemic industry problem, not specific to McKinsey: "The shape of this failure shows up in a lot of places."

For MetaSystem, this applies to any tool or MCP server surface that agents interact with. Each surface should be evaluated: does it distinguish agent from human access? Does it scope permissions per-task? Can it audit agent-specific actions?

## Why People Are Using It

The six-vendor convergence documented in the source is essentially a market-wide pivot toward agent-aware surface design. Salesforce headless 360 exposes platform APIs explicitly for agents ("because agents don't click through screens"). ServiceNow action fabric provides governed workflow surfaces with identity and audit. These are not new features bolted onto existing platforms — they represent architectural recognition that the surface itself must be agent-aware from the ground up.

## Potential Improvements

- Develop an "agent-readiness checklist" for evaluating any API surface MetaSystem agents interact with: authentication, per-task scoping, rate limiting, write-access audit, revocation capability.
- Apply this principle retroactively to existing MCP server configurations — audit each server's access model against agent-aware design requirements.

## Potential Failure Modes

- **Backward compatibility**: Redesigning existing APIs for agent-awareness may break existing human-user integrations.
- **Over-scoping**: Per-task permission scoping requires knowing the task boundary in advance, which may not be possible for exploratory or open-ended agent workflows.
- **Performance overhead**: Adding authentication, rate limiting, and audit logging to every endpoint adds latency and complexity that may be unnecessary for low-risk surfaces.
