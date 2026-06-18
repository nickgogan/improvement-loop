---
name: "Tool Access as Security Boundary, Not Feature Toggle"
summary: "MCP tool access is treated as a feature toggle in most UIs (enable/disable server), but it is actually a security boundary crossing. MCP was designed for high-trust environments and does not enforce access control at the protocol level. Enabling a tool grants the agent arbitrary code execution and arbitrary data access within that tool's scope. Required security posture: scopes (which tools visible per context), approval flows (human confirmation for sensitive ops), audit trails (full call logging), and context-sensitive visibility (don't expose tools irrelevant to the current task)."
implementation_notes: "MetaSystem treats MCP server enablement as a configuration decision, not a security decision. Claude Code's permission system provides per-call approval, which is a form of context-sensitive visibility. But the finding argues that the security boundary is at the 'which servers are connected' level, not the 'which calls are approved' level. Worth auditing: which MCP servers expose capabilities that MetaSystem agents should never use?"
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "google-io-mcp-a2a-agui-protocol-stack.md"
related_findings:
  - file: "mcp-tool-description-prompt-injection-attack.md"
    rel: "extends"
  - file: "tool-gateway-security-boundary.md"
    rel: "same-problem"
  - file: "inline-scoped-mcp-servers-per-subagent.md"
    rel: "same-problem"
  - file: "mcp-enterprise-governance-gaps.md"
    rel: "same-problem"
  - file: "mcp-session-scoped-authorization.md"
    rel: "same-problem"
  - file: "explicit-permission-allow-listing-for-agent-resou.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: synthesized
consumed_by:
  - "agent-governance-and-trust.md"
  - "rules/explicit-permission-allow-listing-for-agent-resource-access.md"
tags:
  - "session-95-reextract"
  - "governance"
  - "security"
  - "tools"
---

# Tool Access as Security Boundary, Not Feature Toggle

## What It Is

A design principle for agent tool configuration. The prevailing UI pattern treats MCP server enablement as a feature toggle -- a checkbox that turns on capabilities. The actual security reality is different:

- **MCP was designed for high-trust environments.** The protocol allows agents to use tools in arbitrary ways to complete tasks. That is its purpose. It was not designed to enforce access control.
- **Enabling a tool server crosses a security boundary.** The agent gains arbitrary code execution and arbitrary data access within that tool's scope.
- **Tool descriptions are model-readable metadata.** They enter agent context as part of tool discovery, making them an injection surface (see: tool poisoning attacks).

The principle: "MCP gets the agent close to the work. It does not decide whether the agent should do the work." The security boundary is at the server-connection level, not the individual-call level.

Required mitigations when crossing the boundary:
1. **Scopes:** Which tools can the agent see in which context?
2. **Approval flows:** Which operations require human confirmation?
3. **Audit trails:** What tools were called, with what parameters, producing what results?
4. **Context-sensitive visibility:** Do not expose tools irrelevant to the current task.

## Why It Matters

Most agent platforms present tool enablement as feature configuration, not security configuration. This mental model leads teams to enable MCP servers casually -- "turn on the Slack integration" -- without assessing what the agent can now do with Slack access (read any channel, post as the user, modify settings). The feature-toggle framing masks the actual attack surface expansion.

For MetaSystem: Claude Code's permission system provides per-call approval, which partially mitigates the risk. But the finding points to a higher-level concern: which MCP servers are connected at all, and whether any expose capabilities that no MetaSystem agent should ever use. Per-call approval is defense-in-depth; the primary defense should be "don't connect servers whose capabilities exceed what the agent needs."

This aligns with the inline-scoped MCP servers pattern: scope MCP connections to the specific subagent that needs them, rather than making all servers available to all conversations.

## Why People Are Using It

Presented alongside the Invariant Labs tool-poisoning research in a Google I/O protocol analysis. The framing distinguishes between MCP's design intent (frictionless tool discovery in trusted environments) and the security reality of deploying MCP in production (untrusted or semi-trusted environments where tool descriptions, parameters, and return values all become attack surfaces).

## Potential Improvements

- Classify MCP servers by trust tier (read-only, write-with-approval, write-autonomous) and enforce connection policies per tier
- Implement connection-time scoping: when an MCP server connects, specify which tools from that server the agent can see (rather than all-or-nothing)
- Build security assessment into MCP server selection: before enabling a server, enumerate its capabilities and match them to agent needs
- Combine with subagent-scoped MCP to ensure the principle of least privilege at the server-connection level

## Potential Failure Modes

- Over-restriction: teams that internalize this principle may disable useful MCP servers out of security caution, reducing agent effectiveness
- False sense of security: per-call approval creates an illusion of control, but approval fatigue leads to rubber-stamping
- Scope creep: tools that are safe individually may compose into dangerous workflows (e.g., read + write + delete = full data lifecycle access)
- The principle requires ongoing audit: new MCP server versions may add capabilities that expand the security boundary without the team's awareness
