---
name: 'Credential Isolation: Bundled Auth and Vault Proxy'
summary: 'Keep credentials out of agent sandbox reach via two patterns: bundled auth (inject at sandbox init, e.g., clone repo with scoped token wired to local remote) and vault proxy (session-associated
  token fetched by dedicated proxy, never exposed to agent). Prevents prompt injection credential theft.'
implementation_notes: null
category: Sandboxing
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-managed-agents-decoupling.md
- anthropic-managed-agents-platform.md
related_findings:
- file: tool-gateway-security-boundary.md
  rel: same-problem
- file: tiered-permission-system-bash-safety.md
  rel: same-problem
- file: anthropic-managed-agents-platform.md
  rel: extends
- file: ai-gateway-model-traffic-layer.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- agent-safety-and-permissions.md
---

## What It Is

Two patterns for keeping credentials away from Claude-generated code in sandboxes. (1) **Bundled auth**: At sandbox initialization, clone the repo with a repo-specific token and wire it to the local git remote. The sandbox can `push/pull` without the agent ever handling the token directly. (2) **Vault proxy**: For custom or MCP tools, a dedicated proxy service fetches credentials from a vault using the session-associated token, then calls the external service on the agent's behalf. The harness never sees the raw credentials; the agent only sees the tool's response.

## Why It Matters

Shared containers expose credentials to untrusted agent-generated code. Prompt injection attacks can read environment tokens, spawn unrestricted sessions, or exfiltrate credentials. Narrow token scoping helps but assumes model limitations that improve over time. Architectural isolation -- keeping tokens physically out of the sandbox -- is more robust than scoping alone.

## Why People Are Using It

Anthropic's production managed agents platform. The bundled auth pattern is specifically documented for git operations; the vault proxy pattern generalizes to any external service integration.

## Potential Improvements

Dynamic credential rotation during long-running sessions. Audit logging of credential usage through the proxy. Credential usage quotas to detect anomalous patterns.

## Potential Failure Modes

Bundled auth tokens cached in git config may persist across sandbox reuse. Vault proxy becomes a single point of failure. Latency of proxied credential fetches for high-frequency tool calls.
