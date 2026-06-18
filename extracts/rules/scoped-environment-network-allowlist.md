---
title: "Scoped Environment Network Allowlist"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "scoped-environment-network-allowlist-governance"
extraction_date: "2026-05-25"
last_change_session: 96
last_change_sl: "session-96-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-25-identification-report-session-95.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "hosted or sandboxed agent environments where the agent executes code with network access"
    - "any deployment where an agent could reach external services beyond what its task requires"
    - "teams provisioning agent environments that need auditable network security posture"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "secure"
  reversibility: "low — adding network restrictions after deployment requires environment reconfiguration and may break existing workflows that relied on unrestricted access"
  auditability: "high — the allowlist is declarative and inspectable; compliance is verifiable by comparing the allowlist against actual network traffic logs"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "An agent environment is being provisioned (container, VM, hosted sandbox, or equivalent). The environment will have network access. The provisioning system supports network-level access control (firewall rules, security groups, egress policies)."
  invariants: "Every hosted agent environment declares an explicit network allowlist at provisioning time. The default network posture is deny-all — only allowlisted endpoints are reachable. The allowlist specifies exact endpoints (not wildcards covering entire cloud provider domains). MCP server access is a separate, explicitly declared permission. The allowlist is environment-scoped (tied to the agent's purpose), not organization-wide."
  governance: "Owner: the team or individual provisioning the agent environment. Allowlist entries are reviewed at provisioning time and auditable afterward. Adding a new endpoint to the allowlist requires explicit justification (what task needs this endpoint?). Periodic review ensures the allowlist hasn't accumulated stale entries from previous tasks."
  recovery: "If an agent needs an endpoint not on the allowlist: the request goes through a human-gated approval flow, not a self-grant. If the allowlist is discovered to be overly broad (wildcards, entire domains): narrow to specific endpoints and verify the agent still functions. If network traffic audit reveals connections to non-allowlisted endpoints: investigate as a potential security boundary breach."
tags:
  - "extracted-artifact"
  - "rule"
  - "governance"
  - "security"
  - "infrastructure"
---

# Scoped Environment Network Allowlist

**Source:** [[scoped-environment-network-allowlist-governance]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

A hosted agent environment is being provisioned or configured — any environment where an agent will execute code with the ability to make network connections to external services.

## Action

**Required:** Declare an explicit network allowlist specifying exactly which external endpoints the environment can reach. Set the default network posture to deny-all. Declare MCP server access as a separate boolean permission. Scope the allowlist to the agent's specific task requirements.

**Forbidden:** Provisioning agent environments with unrestricted network access. Using broad wildcards that effectively negate the allowlist (e.g., `*.googleapis.com` instead of specific API endpoints). Treating the allowlist as a one-time setup that never needs review.

## Boundary

Enforced at environment provisioning time. The boundary is the network layer — before any agent code runs, the environment's reachable surface area is declared and constrained. This is orthogonal to sandbox isolation (which constrains execution) — network allowlists constrain reachability.

## Enforcement

Infrastructure-level enforcement via firewall rules, security groups, or egress policies. The check is declarative: inspect the environment configuration and verify (1) an allowlist exists, (2) it specifies exact endpoints, (3) the default is deny-all, and (4) MCP access is explicitly declared.

## Rationale

Network allowlists solve a different problem than sandbox isolation. Sandboxes prevent the agent from affecting the host; network allowlists prevent the agent from reaching unauthorized external services. An agent inside a perfect sandbox can still exfiltrate data through unrestricted network access. The deny-all default ensures that every external connection is a conscious, auditable decision — not an inherited permission from a broad environment configuration.
