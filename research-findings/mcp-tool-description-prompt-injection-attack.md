---
name: MCP Tool Descriptions as Prompt-Injection Attack Surface
summary: 'MCP standardizes tool discovery via metadata, but that metadata is model-readable, making tool descriptions a live injection vector. Invariant Labs documented ''tool poisoning attacks'' where
  malicious instructions embedded in tool descriptions redirect agent behavior. MCP was designed for high-trust environments and does not enforce access control. Required mitigations: scopes, approval flows,
  audit trails, context-sensitive tool visibility.'
implementation_notes: MetaSystem uses MCP servers (Notion, Perplexity, Context7). Tool descriptions from these servers are injected into agent context. The attack surface is real but currently bounded by
  the trust level of the MCP servers in use. Worth auditing which tool descriptions flow into context and whether any contain instructions that could redirect agent behavior.
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- google-io-mcp-a2a-agui-protocol-stack.md
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-05-25'
related_findings:
- file: tool-gateway-security-boundary.md
  rel: extends
- file: gstack-four-layer-prompt-injection-defense.md
  rel: same-problem
- file: inline-scoped-mcp-servers-per-subagent.md
  rel: extends
- file: tool-access-as-security-boundary-not-feature-toggle.md
  rel: enables
- file: mcp-high-trust-design-assumption.md
  rel: enables
pipeline_status: synthesized
consumed_by:
- rules/mcp-tool-description-prompt-injection-attack-surface.md
- agent-safety-and-permissions.md
tags:
- governance
- tools
- security
---

# MCP Tool Descriptions as Prompt-Injection Attack Surface

## What It Is

MCP tool descriptions are model-readable metadata intended for tool discovery. This makes them a live injection vector: malicious instructions can be embedded in tool descriptions to redirect agent behavior. Invariant Labs published research on "tool poisoning attacks" demonstrating this vulnerability.

## Why It Matters

"Tool access is not a feature toggle — it is a security boundary." MCP was created for high-trust environments and does not enforce access control at the protocol level. Any system consuming MCP servers inherits tool descriptions into agent context without validation. Required mitigations: scopes (which tools are visible per task), approval flows (human confirmation for sensitive operations), audit trails (what tools were called with what parameters), and context-sensitive tool visibility (don't expose tools irrelevant to the current task).

## How It Could Fail

Scoping tool visibility requires knowing upfront which tools are safe for which contexts — a classification problem that grows with the number of MCP servers. Approval flows add latency. The fundamental tension: MCP's value is frictionless tool discovery; security mitigations add friction.

## Extraction Note — 2026-05-24
Extracted as **rule**: [[mcp-tool-description-prompt-injection-attack-surface]] in `extracts/rules/`
