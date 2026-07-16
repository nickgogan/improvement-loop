---
name: Scoped Environment Network Allowlist Governance
summary: Hosted agent environments use explicit network allowlists as the primary security boundary. Each environment declares exactly which external endpoints it can connect to (e.g., 'can connect to mcp.clickup.com'),
  with MCP access enabled/disabled as a separate flag. The environment type defaults to 'highly limited' -- only the declared endpoints are reachable.
implementation_notes: null
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-managed-agents-platform.md
related_findings:
- file: credential-isolation-bundled-auth-vault-proxy.md
  rel: same-problem
- file: tool-gateway-security-boundary.md
  rel: extends
- file: sandbox-architecture-by-threat-model-microvm-vs-container.md
  rel: same-problem
- file: per-node-tool-restrictions-workflow-governance.md
  rel: same-problem
- file: explicit-permission-allow-listing-for-agent-resou.md
  rel: extends
- file: anthropic-managed-agents-platform.md
  rel: extends
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- extracts/rules/scoped-environment-network-allowlist.md
- agent-safety-and-permissions.md
tags:
- session-95-reextract
---

## What It Is

A security governance pattern for hosted agent environments where the environment declares an explicit allowlist of network endpoints the agent can reach. Observed in Anthropic's managed agents platform:

- **Environment scope**: organization-level (shared across team members)
- **Network permissions**: explicit allowlist (e.g., `mcp.clickup.com`)
- **MCP access**: separate boolean flag (enabled/disabled)
- **Packages**: explicit package list (can be empty)
- **Type**: defaults to "highly limited" -- deny-all except allowlisted endpoints

The practitioner notes: "This environment can connect to mcp.clickup.com. It has no packages. It has MCP access enabled and its type is highly limited because obviously this can only really chat internally between it and then mcp.clickup.com."

This is architecturally distinct from sandbox isolation (which isolates execution) -- this is network-level access control that determines what external services the agent can reach regardless of what code it runs.

## Why It Matters

Network allowlists solve a different problem than sandbox isolation. Sandboxes prevent the agent from affecting the host system; network allowlists prevent the agent from reaching unauthorized external services. This is the difference between "the agent can't escape its container" and "the agent can't call services it shouldn't."

For enterprise adoption, the practitioner notes this is "the sort of security stuff that allows you to work mid-market and then enterprise." The explicit permission model creates an auditable security posture: you can inspect any environment and see exactly what it can access.

For harness builders, this pattern means agent environments need two orthogonal security layers: execution isolation (sandbox) and network access control (allowlist). Most current frameworks focus only on the former.

## Why People Are Using It

Anthropic's managed agents platform as a production feature. The pattern mirrors how enterprise network security already works (firewall rules, security groups) -- applied to agent environments.

## Potential Improvements

- Dynamic allowlist modification through a human-gated approval flow (agent requests new endpoint access, human approves)
- Per-session network access rather than per-environment (different runs of the same agent get different permissions based on the task)
- Network traffic logging per agent for usage auditing
- Allowlist templates for common integration patterns (e.g., "CRM integration" pre-approves Salesforce, HubSpot, etc.)

## Potential Failure Modes

- Overly broad allowlists that undermine the security benefit (e.g., allowing `*.googleapis.com` instead of specific API endpoints)
- Allowlist maintenance burden: as tools evolve their domains, allowlists need updating
- False sense of security: network allowlists don't prevent data exfiltration through allowed endpoints (e.g., encoding stolen data in ClickUp task descriptions)
- No egress content inspection: the allowlist controls which endpoints, not what data flows through them
