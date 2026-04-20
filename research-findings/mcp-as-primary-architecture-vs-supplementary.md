---
name: "MCP as Primary Architecture vs. Supplementary Tool"
summary: "Two distinct roles for MCP across 4 repos: supplementary (Sandbox, DeerFlow, OpenViking — MCP is one of several integration methods) vs. primary architecture (OB1 — MCP is the ONLY way AI clients interact with the system, enforced by CI). First MCP-native architecture in the registry."
implementation_notes: "MetaSystem uses MCP servers for external services (Notion, Perplexity) but has no MCP-based internal architecture. OB1's pattern — all capabilities as remote MCP Edge Functions — trades local speed for universal AI client access. Worth monitoring as MCP protocol matures."
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: P3 (Monitor)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "mcp-as-code-api-progressive-tool-discovery.md"
    rel: "extends"
  - file: "cli-first-tool-integration-less-overhead-than-mcp.md"
    rel: "contradicts"
  - file: "mcp-enterprise-governance-gaps.md"
    rel: "same-problem"
  - file: "all-in-one-sandbox-architecture.md"
    rel: "same-problem"
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: raw
consumed_by: []
---

## What It Is
MCP (Model Context Protocol) is used in two fundamentally different ways across the registry:

**MCP as supplementary** (AIO Sandbox, DeerFlow, OpenViking — 3 repos): MCP is one of several integration methods. Sandbox uses MCP Hub to aggregate sub-servers but also exposes a REST API. DeerFlow supports MCP alongside native LangGraph tooling. OpenViking provides MCP tools via Claude Code plugin alongside direct filesystem access. In these repos, MCP is a convenience layer, not the primary architecture.

**MCP as primary architecture** (OB1 — 1 repo): MCP is the ONLY way AI clients interact with Open Brain. Every extension deploys as a Supabase Edge Function exposing MCP tools. CI actively blocks local server patterns (`claude_desktop_config.json`, `StdioServerTransport`). No REST API, no CLI alternative, no direct database access for AI clients. MCP is the architecture, not an add-on.

## Why It Matters
The distinction between "MCP as tool" and "MCP as architecture" has significant implications:
- **Portability**: OB1's MCP-primary design means any MCP-compatible AI client (Claude, ChatGPT, Cursor, Claude Code, Codex) automatically gets access to all capabilities. No per-client integration needed.
- **Governance**: All AI interactions go through a single protocol, making audit and access control consistent. The `x-brain-key` auth header on every MCP request provides a uniform security boundary.
- **Capability design**: New capabilities (extensions, recipes) are designed as MCP tool sets rather than APIs or libraries. This shapes how developers think about what agents can do.

## Why People Are Using It
Observed across four repos: [OB1](https://github.com/NateBJones-Projects/OB1) (see [[ob1-analysis]]), AIO Sandbox (see [[sandbox-analysis]]), DeerFlow (see [[deer-flow-analysis]]), OpenViking (see [[openviking-analysis]]). OB1 is the only MCP-primary architecture; the other three use MCP as supplementary.

## Potential Alternatives
- **REST API primary** (traditional): Direct HTTP endpoints. More mature, better tooling, wider client support. But requires per-client integration.
- **CLI primary** (Beads, GSD): Command-line tools as the interface. Lower overhead but limited to clients that can execute shell commands.
- **Native SDK** (mem0, LangGraph): Library imports. Tightest integration but locked to specific languages/runtimes.

## Potential Improvements
- **Hybrid**: MCP as primary for AI clients + REST API for programmatic access + CLI for debugging. OB1 currently lacks non-MCP fallbacks.
- **MCP capability discovery**: Progressive tool loading (DeerFlow's pattern) applied to MCP — expose tool descriptions first, full schemas on demand.
- **MCP governance layer**: Middleware between MCP protocol and backend that enforces rate limits, audit logging, and permission checks.

## Potential Failure Modes
- **Protocol dependency**: MCP is still maturing. Breaking changes in the protocol affect the entire architecture, not just one integration.
- **Latency**: Remote MCP via Edge Functions adds network round-trips vs. local tool calls.
- **Single point of failure**: If Supabase Edge Functions are down, all AI capabilities are offline.
- **No offline mode**: MCP-primary requires network connectivity for every interaction.
