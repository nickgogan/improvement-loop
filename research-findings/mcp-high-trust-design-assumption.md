---
name: "MCP High-Trust Design Assumption"
summary: "MCP was designed for high-trust environments where the agent and all connected tool servers are trusted. It standardizes tool discovery and invocation but does not enforce access control, scope boundaries, or security policies at the protocol level. This creates a fundamental tension: MCP's value is frictionless tool composition, but production deployment requires friction (scopes, approvals, audit trails). Teams deploying MCP outside high-trust environments must layer security on top of a protocol that was not designed for it."
implementation_notes: "MetaSystem operates in a medium-trust environment: MCP servers are chosen by Nick (trusted), but the tools they expose include mutation capabilities (Notion write, Calendar event creation, Gmail send) that should not be invoked without approval. Claude Code's per-call permission system adds the missing friction layer. The finding suggests this is the right architecture: MCP for discovery, a separate layer for enforcement."
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "google-io-mcp-a2a-agui-protocol-stack.md"
related_findings:
  - file: "mcp-tool-description-prompt-injection-attack.md"
    rel: "extends"
  - file: "tool-access-as-security-boundary-not-feature-toggle.md"
    rel: "same-problem"
  - file: "mcp-enterprise-governance-gaps.md"
    rel: "same-problem"
  - file: "tool-gateway-security-boundary.md"
    rel: "same-problem"
  - file: "mcp-session-scoped-authorization.md"
    rel: "same-problem"
  - file: "secure-by-default-posture-as-organizational-invariant.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
  - "governance"
  - "security"
  - "protocols"
---

# MCP High-Trust Design Assumption

## What It Is

MCP (Model Context Protocol) was created for a high-trust environment. Its design intent: standardize how agents discover and invoke tools so that new capabilities compose without every agent platform rebuilding every connector. It succeeds at this -- 14,000+ servers, universal provider support, N+M integration economics.

The high-trust assumption means:
- **No built-in access control.** The protocol does not define scopes, permissions, or authorization policies. A connected server exposes all its tools to the agent.
- **No built-in audit trail.** The protocol does not log or trace tool invocations. Observability must be layered on top.
- **Tool descriptions are model-readable.** They are injected into agent context as-is, making them both a discovery mechanism and an injection surface.
- **Arbitrary execution by design.** MCP is designed to allow agents to use tools in arbitrary ways to complete tasks. This is the explicit design goal, not a bug.

The fundamental tension: MCP's value comes from being frictionless (easy tool composition, no per-tool integration work). Production security requires friction (scopes, approvals, audit trails). Teams must reconcile "designed for trust" with "deployed in distrust."

## Why It Matters

This is not a vulnerability finding -- MCP works as designed. The finding is about the mental model: teams treat MCP as if standardization implies security ("it's a standard, so it must be safe"). Standardization solves the integration problem; it does not solve the security problem. The security problem requires a separate layer.

The correct architecture: **MCP for discovery and invocation, a separate enforcement layer for scopes, approvals, and audit.** This is what Claude Code's permission system does, what the tool-gateway pattern describes, and what AGUI is designed to formalize.

For MetaSystem: the current architecture (MCP for tool access + Claude Code permissions for enforcement) is the right layered approach. The finding confirms that this layering is not accidental but necessary -- MCP's design assumption requires it.

## Why People Are Using It

Discussed in the context of Google I/O's agent protocol analysis. The author explicitly states: "It's tempting to treat MCP as if it makes tools safe just because it's a standard across the internet. It doesn't." This is positioned as a warning to build teams who conflate standardization with security.

## Potential Improvements

- Document the "MCP for discovery, separate layer for enforcement" architecture pattern explicitly
- Audit existing MCP server connections for capabilities that exceed what any agent needs
- Track MCP specification evolution (the 2026 roadmap includes enterprise security features) to know when the protocol itself may close these gaps
- Consider whether MCP's high-trust assumption affects MetaSystem's threat model for MCP servers from third parties

## Potential Failure Modes

- Teams trust MCP because it is a standard, leading to insecure deployments
- The separate enforcement layer is treated as optional ("we'll add security later"), creating the same debt pattern as supervision debt
- MCP's specification evolves to include security features that are weaker than what teams have already built independently, creating a "race to the bottom" if teams adopt the spec-level security as sufficient
- The high-trust assumption makes MCP a poor fit for adversarial environments (public-facing agent services); teams may need alternative protocols for untrusted contexts
