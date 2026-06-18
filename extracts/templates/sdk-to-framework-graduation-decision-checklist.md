---
title: "SDK-to-Framework Graduation Decision Checklist"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "sdk-to-framework-graduation-path"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams or individuals deciding whether to migrate an agent from an SDK prototype to a production framework"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "medium — the decision to graduate triggers a build effort; reversing means maintaining two implementations or reverting the migration"
  auditability: "high when graduation triggers are documented with evidence at decision time; low when the migration is driven by intuition or deadline pressure"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Cole Medin demonstrates the SDK-to-framework path using Claude Code to build Pydantic AI agents. No MetaSystem adoption yet."
contract:
  preconditions: "An agent prototype exists and is running on an SDK (Claude Agent SDK, Codex SDK, or equivalent). At least one graduation trigger has been observed or is projected. The team has access to the target framework (Pydantic AI, LangGraph, or equivalent)."
  invariants: "The graduation decision is made on documented evidence of at least one trigger, not on timeline pressure or preference. Skills and MCP server integrations are identified as portable assets before migration begins. Agent loop, state management, and conversation history are identified as rebuild targets. The graduation checklist is completed before the first framework line of code is written."
  governance: "Owner: the agent developer or architect at the time of the graduation decision. The completed checklist is filed with the agent's design documentation. Graduation decisions that affect production-scale deployments require a DD. The SDK prototype is retained and documented as the reference implementation until the framework agent passes validation."
  recovery: "If graduation is started but the trigger evidence turns out to be insufficient → pause the migration; continue on the SDK until a trigger is confirmed. If skills break during migration → do not modify the skill; investigate whether the skill has an implicit SDK dependency and document it. If the framework agent cannot be validated to match the SDK prototype's behavior → retain the SDK prototype in production; treat the migration as a failed graduation and file a finding."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-architecture"
  - "framework-selection"
  - "migration"
---

# SDK-to-Framework Graduation Decision Checklist

**Source:** [[sdk-to-framework-graduation-path]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Variable | Description |
|----------|-------------|
| `{{AGENT_NAME}}` | Name of the agent being evaluated for graduation |
| `{{CURRENT_SDK}}` | SDK the prototype is running on (e.g., Claude Agent SDK, Codex SDK) |
| `{{TARGET_FRAMEWORK}}` | Proposed framework (e.g., Pydantic AI, LangGraph) |
| `{{DECISION_DATE}}` | Date the checklist is completed |
| `{{DECISION_OWNER}}` | Person or team completing the checklist |
| `{{SKILL_LIST}}` | Comma-separated list of skills used by the agent |
| `{{MCP_SERVER_LIST}}` | Comma-separated list of MCP servers used by the agent |
| `{{TRIGGER_EVIDENCE}}` | Description of the observed or projected trigger(s) |

---

## Body

# Agent Graduation Evaluation: {{AGENT_NAME}}

**SDK:** {{CURRENT_SDK}}
**Target framework:** {{TARGET_FRAMEWORK}}
**Date:** {{DECISION_DATE}}
**Owner:** {{DECISION_OWNER}}

---

## Part 1 — Graduation Trigger Assessment

Check each trigger that applies. At least one must be confirmed or credibly projected before proceeding.

- [ ] **Multi-user deployment required.** The agent needs to serve more than one user simultaneously, which the SDK's subscription ToS restricts.
  - Evidence: {{TRIGGER_EVIDENCE}}

- [ ] **Sub-second response time required.** The agent's use case requires latency the SDK's reasoning overhead cannot deliver.
  - Evidence: {{TRIGGER_EVIDENCE}}

- [ ] **API-key cost at scale is prohibitive.** Run frequency × token cost at the projected scale exceeds the budget ceiling that SDK-based operation allows.
  - Evidence: {{TRIGGER_EVIDENCE}}

- [ ] **Production observability required.** The agent needs custom conversation history storage, monitoring dashboards, or audit trails that the SDK does not support.
  - Evidence: {{TRIGGER_EVIDENCE}}

**Trigger verdict:** (check one)
- [ ] At least one trigger confirmed — proceed to Part 2
- [ ] No trigger confirmed — do not graduate; continue on SDK; revisit when a trigger is reached

---

## Part 2 — Portable Asset Inventory

Skills and MCP servers survive graduation. Identify them before migration.

**Skills (carry over — do not rewrite during migration):**
- {{SKILL_LIST}}

Verify for each skill:
- [ ] Skill has no implicit SDK dependency (e.g., does not call SDK-internal APIs directly)
- [ ] Skill is documented with its interface contract
- [ ] Skill can be invoked from the target framework using the same call signature

**MCP servers (carry over — do not rewrite during migration):**
- {{MCP_SERVER_LIST}}

Verify for each MCP server:
- [ ] MCP server is protocol-level portable (not SDK-specific)
- [ ] MCP server connection configuration is documented

---

## Part 3 — Rebuild Target Inventory

These components do NOT carry over. They are rebuilt in the framework from scratch.

- [ ] **Agent loop.** The SDK-managed conversation loop is replaced with the framework's equivalent.
- [ ] **Conversation history management.** SDK-managed history is replaced with the framework's state store.
- [ ] **State management.** Any SDK-managed state (session context, run state) is rebuilt in the framework.

Note: the SDK prototype is the reference implementation. The framework agent must replicate its observable behavior on the validation test suite before the SDK prototype is retired.

---

## Part 4 — Validation Plan

Before retiring the SDK prototype:

- [ ] Define the validation test suite (input/output pairs covering the agent's main capabilities)
- [ ] Run the test suite against the SDK prototype; record baseline outputs
- [ ] Run the test suite against the framework agent; compare to baseline
- [ ] All critical capability tests pass at or above baseline quality

---

## Part 5 — Decision Record

| Field | Value |
|-------|-------|
| Graduate? | Yes / No |
| Trigger(s) confirmed | |
| Portable assets count | Skills: N, MCP servers: M |
| Rebuild targets | Agent loop, conversation history, state management |
| SDK prototype retained until | Validation suite passes |
| DD required? | Yes / No (production-scale: always yes) |

---

## Usage

1. Complete variables at the top of the document.
2. Work through Parts 1–5 in order; do not skip Part 1 (trigger check).
3. File the completed checklist with the agent's design documentation.
4. If graduation is approved, use Part 2's portable asset inventory as the migration scope boundary.
5. Do not begin writing framework code until Parts 1–3 are complete.

---

## Variation Axis

| Variation | Adjustment |
|-----------|-----------|
| Greenfield agent (no SDK prototype) | Skip Part 3 (no SDK to compare); add a Part 0 that decides SDK vs. framework from the start using the trigger criteria |
| Multi-agent system | Repeat Parts 1–3 per agent; coordinate portable assets across all agents before beginning migration |
| Framework already chosen by organizational policy | Skip the framework selection variable; retain all trigger and portable-asset steps |
| Trigger is projected (not yet observed) | Document the projection basis in the evidence field; revisit when the projected trigger is reached; do not graduate on projection alone unless timeline risk justifies it |

---

## Contract

### Preconditions
An agent prototype exists and is running on an SDK. At least one graduation trigger has been observed or is credibly projected. The team has access to the target framework.

### Invariants
The graduation decision is made on documented evidence of at least one trigger, not on timeline pressure or preference. Skills and MCP server integrations are identified as portable assets before migration begins. Agent loop, state management, and conversation history are identified as rebuild targets. The graduation checklist is completed before the first framework line of code is written.

### Governance
Owner: the agent developer or architect at the time of the graduation decision. The completed checklist is filed with the agent's design documentation. Graduation decisions that affect production-scale deployments require a DD. The SDK prototype is retained and documented as the reference implementation until the framework agent passes validation.

### Recovery
If graduation is started but the trigger evidence turns out to be insufficient → pause the migration; continue on the SDK until a trigger is confirmed. If skills break during migration → do not modify the skill; investigate whether the skill has an implicit SDK dependency and document it. If the framework agent cannot be validated to match the SDK prototype's behavior → retain the SDK prototype in production; treat the migration as a failed graduation and file a finding.
