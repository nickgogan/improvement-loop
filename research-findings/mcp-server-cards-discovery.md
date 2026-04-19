---
name: MCP Server Cards for Decentralized Discovery
summary: MCP Server Cards enable discovery via .well-known URLs, allowing browsers and crawlers to discover server capabilities without connecting. Combined with Streamable HTTP transport, enables lightweight
  server registration and dynamic client-server matching without central coordination.
implementation_notes: Low immediate relevance -- MetaSystem's MCP servers are manually configured. Relevant if we ever expose our own MCP servers for external consumption or want automated discovery of
  new servers.
category: Tool Integration
evidence_strength: Weak (theoretical)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- mcp-everything-your-team-needs-to-know-workos.md
related_findings:
- file: mcp-ecosystem-critical-mass-97m-installs.md
  rel: enabled-by
- file: tool-registry-metadata-first-design.md
  rel: same-problem
- file: mcp-n-plus-m-integration-economics.md
  rel: extends
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---
# MCP Server Cards for Decentralized Discovery

## What It Is
The 2026 MCP roadmap proposes Server Cards -- metadata documents served via `.well-known` URLs that describe a server's capabilities, authentication requirements, and supported transport. Combined with Streamable HTTP transport (remote deployment via standard HTTP with Server-Sent Events), this enables decentralized server discovery without relying on a central registry.

## Why It Matters
The current MCP Registry (~2,000 servers) is a centralized discovery bottleneck with no conformance testing. Server Cards shift discovery to a DNS-like model where any domain can advertise MCP capabilities. This scales ecosystem discovery without registry coupling.

## Why People Are Using It
Still in the 2026 roadmap phase -- not yet widely deployed. The concept mirrors `.well-known` patterns from OAuth, WebFinger, and security.txt that have proven effective for decentralized discovery.

## Potential Improvements
Conformance testing tied to Server Cards would solve the quality signaling problem. Versioned capability declarations would help clients select compatible servers.

## Potential Failure Modes
Requires clients to validate server metadata freshness and authenticity. Discovery spam (fake servers advertising capabilities they don't deliver). No current mechanism for signaling maintenance status or security review level.
