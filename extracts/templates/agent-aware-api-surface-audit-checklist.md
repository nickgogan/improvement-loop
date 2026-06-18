---
title: "Agent-Aware API Surface Audit Checklist"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "agent-aware-api-surface-design"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "any API or tool surface that autonomous agents will call"
    - "MCP server configurations and tool definitions in agent systems"
    - "teams evaluating whether an existing API is safe for agent access"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "secure"
  reversibility: "trivial — checklist produces an audit document; findings require separate remediation work with varying cost"
  auditability: "high when the completed checklist is stored as a design artifact and linked to the API surface it audits"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: "Pattern derived from analysis of the Lilly incident and six-vendor convergence on agent-aware platform design. No known prior audit of MetaSystem MCP server surfaces against these criteria."
contract:
  preconditions: "An API surface, tool definition, or MCP server exists and will be accessed by an autonomous agent. The auditor has access to the surface's authentication model, permission scope, rate limiting configuration, and audit logging setup."
  invariants: "All four dimensions are assessed — no dimension is skipped on grounds of being inapplicable without documentation. Each 'no' answer triggers a remediation item. The completed checklist is stored as a persistent artifact linked to the surface being audited."
  governance: "Owner: The team or individual responsible for the API surface or tool configuration. New surfaces introduced into an agent system require a completed audit before the agent is granted access. Existing surfaces are audited retroactively when the agent's access scope changes."
  recovery: "If a 'no' answer cannot be remediated immediately → document it as an accepted risk with a named owner and target remediation date. If the surface fails dimension 1 (cannot distinguish agent from human identity) → block agent access until remediation is complete; this is a blocking finding. If the surface fails dimension 4 (no write-access audit) → restrict the agent to read-only access until remediation is complete."
tags:
  - "extracted-artifact"
  - "template"
  - "api-security"
  - "agent-design"
  - "audit-checklist"
---

# Agent-Aware API Surface Audit Checklist

**Source:** [[agent-aware-api-surface-design]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Variable | Description |
|----------|-------------|
| `{{SURFACE_NAME}}` | Name of the API, tool, or MCP server being audited |
| `{{SURFACE_OWNER}}` | Team or individual responsible for the surface |
| `{{AUDITOR}}` | Name or role conducting the audit |
| `{{AUDIT_DATE}}` | Date of the audit |
| `{{AGENT_PURPOSE}}` | What the agent will use this surface for |
| `{{AGENT_IDENTITY}}` | How the agent authenticates to this surface |

---

## Body

```markdown
# Agent-Aware API Surface Audit — {{SURFACE_NAME}}

**Surface:** {{SURFACE_NAME}}
**Surface owner:** {{SURFACE_OWNER}}
**Auditor:** {{AUDITOR}}
**Date:** {{AUDIT_DATE}}
**Agent purpose:** {{AGENT_PURPOSE}}
**Agent identity:** {{AGENT_IDENTITY}}

---

## Dimension 1 — Human/Agent Identity Distinction

**Question:** Does the surface know the difference between a human user and an AI agent accessing it?

- [ ] The surface authenticates agents with a separate credential or identity from human users.
- [ ] The surface can enforce different access scopes for agents vs. humans (e.g., an agent scoped to one client account cannot access another, even if the delegating user has multi-account access).
- [ ] A single agent incident cannot escalate to full user-scope exposure because the identity boundary is enforced at the surface, not only by the agent.

**Status:** [ ] Pass  [ ] Fail  [ ] Partial

**Notes:**
[Fill in: how identity distinction is or is not implemented]

**Remediation required:**
[Fill in if Fail or Partial, or write "None"]

---

## Dimension 2 — Per-Task Permission Scoping

**Question:** Are the agent's permissions scoped to the specific task, rather than inherited from the delegating user's full access?

- [ ] The agent's access scope is bounded by the task it is performing (e.g., "access Client X's data for a renewal brief" does not grant access to other clients).
- [ ] Permission scope is declared at task initiation and revocable when the task ends.
- [ ] The surface provides a mechanism to limit access scope at invocation time, not only at account level.

**Status:** [ ] Pass  [ ] Fail  [ ] Partial

**Notes:**
[Fill in: how per-task scoping is or is not implemented]

**Remediation required:**
[Fill in if Fail or Partial, or write "None"]

---

## Dimension 3 — Rate and Volume Awareness

**Question:** Is the surface designed for machine-speed access patterns, not human click rates?

- [ ] Agent-specific rate limiting exists and is distinct from human-user rate limiting.
- [ ] The surface has been load-tested or characterized for agent query patterns (millisecond-scale, high-volume).
- [ ] Unexpected volume spikes from agents do not cause service degradation for human users sharing the same surface.

**Status:** [ ] Pass  [ ] Fail  [ ] Partial

**Notes:**
[Fill in: current rate limiting configuration and whether agent patterns have been considered]

**Remediation required:**
[Fill in if Fail or Partial, or write "None"]

---

## Dimension 4 — Write-Access Audit

**Question:** Are agent write operations separately auditable from human write operations?

- [ ] Every write operation by an agent is logged with agent identity (not attributed to the delegating user).
- [ ] The audit log is queryable: "what did the agent do on behalf of user X?" is answerable separately from "what did user X do?"
- [ ] Agent writes are revocable or correctable with a named process (e.g., rollback, undo, soft delete).

**Status:** [ ] Pass  [ ] Fail  [ ] Partial

**Notes:**
[Fill in: current audit logging setup and whether agent-attributed writes are distinguishable]

**Remediation required:**
[Fill in if Fail or Partial, or write "None"]

---

## Audit Summary

| Dimension | Status | Blocking? |
|-----------|--------|-----------|
| 1. Human/agent identity distinction | [ ] Pass / Fail / Partial | Yes — block agent access if Fail |
| 2. Per-task permission scoping | [ ] Pass / Fail / Partial | No — restrict scope where possible |
| 3. Rate and volume awareness | [ ] Pass / Fail / Partial | No — monitor and throttle if Fail |
| 4. Write-access audit | [ ] Pass / Fail / Partial | Partial block — read-only if Fail |

**Overall readiness:** [ ] Ready for agent access  [ ] Conditionally ready (accepted risks documented)  [ ] Not ready

**Open remediation items:**
1. [Fill in or write "None"]

**Accepted risks (if any):**
| Risk | Owner | Target remediation date |
|------|-------|------------------------|
| [Fill in] | [Fill in] | [Fill in] |
```

---

## Usage

1. Fill in all `{{VARIABLES}}` before starting the audit.
2. Assess each dimension independently. Do not skip a dimension — if it truly does not apply, document why.
3. A "Fail" on Dimension 1 is a blocking finding. Do not grant agent access until remediated.
4. A "Fail" on Dimension 4 restricts the agent to read-only access until remediated.
5. "Partial" findings require an accepted-risk entry with a named owner.
6. Store the completed checklist as a persistent artifact linked to the surface. Update when the surface changes or the agent's access scope changes.

---

## Variation Axis

| Variation | When to use |
|-----------|-------------|
| **Lightweight (Dimensions 1 and 4 only)** | For low-risk read-heavy surfaces where rate limiting and scoping are less critical |
| **Extended (add Dimension 5: revocation)** | For surfaces where emergency kill-switch capability is required — add: "Can the agent's access be revoked in under 60 seconds?" |
| **Retroactive audit** | For existing surfaces already in use by agents — run the checklist and document accepted risks for any existing gaps |
| **Vendor evaluation** | When evaluating a third-party platform for agent integration — apply the four dimensions as selection criteria, not just post-selection audit |

---

## Contract

### Preconditions
An API surface, tool definition, or MCP server exists and will be accessed by an autonomous agent. The auditor has access to the surface's authentication model, permission scope, rate limiting configuration, and audit logging setup.

### Invariants
All four dimensions are assessed — no dimension is skipped on grounds of being inapplicable without documentation. Each "no" answer triggers a remediation item. The completed checklist is stored as a persistent artifact linked to the surface being audited.

### Governance
Owner: The team or individual responsible for the API surface or tool configuration. New surfaces introduced into an agent system require a completed audit before the agent is granted access. Existing surfaces are audited retroactively when the agent's access scope changes.

### Recovery
If a "no" answer cannot be remediated immediately → document it as an accepted risk with a named owner and target remediation date. If the surface fails Dimension 1 (cannot distinguish agent from human identity) → block agent access until remediation is complete; this is a blocking finding. If the surface fails Dimension 4 (no write-access audit) → restrict the agent to read-only access until remediation is complete.
