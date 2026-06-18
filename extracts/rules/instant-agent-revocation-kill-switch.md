---
title: "Instant Agent Revocation (Kill Switch)"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "instant-agent-revocation-kill-switch-pattern"
extraction_date: "2026-05-25"
last_change_session: 96
last_change_sl: "session-96-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-25-identification-report-session-95.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "production agent systems that take real-world actions (API calls, data mutations, external service interactions)"
    - "any deployment where agent misbehavior could cause financial, reputational, or compliance damage during the time it takes to respond"
    - "organizations building incident response procedures for autonomous agent failures"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — the kill switch is additive infrastructure; removing it does not affect normal operation"
  auditability: "high — every revocation event is logged with timestamp, operator, target agent, and reason; the absence of a kill switch is verifiable by testing the revocation procedure"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "An agent is deployed to production with access to one or more external systems. The agent's access is mediated by credentials (API keys, OAuth tokens, service accounts) at the identity/credential layer. An operator with incident response authority is reachable."
  invariants: "Agent access can be revoked within minutes — not through code deploys, tickets, or deletion processes, but through a console-level immediate action. Revocation is immediate (takes effect within the current execution window). Revocation is console-accessible (operable by an incident responder who may not be a developer). Revocation is granular (targets the specific agent without shutting down the entire system). Revocation is auditable (the revocation event is logged with who, when, and why)."
  governance: "Owner: the team responsible for the agent's production deployment. The kill switch procedure must be documented and tested before the agent ships to production. Testing means executing the revocation in a staging environment and verifying access cessation within the target time window. The diagnostic question 'can someone from a console revoke this agent's access in the next 5 minutes?' must have a verified yes answer."
  recovery: "If revocation is triggered: log the event, investigate the triggering incident, and do not restore access until root cause is identified. If partial revocation occurs (primary credential revoked but cached tokens remain active): identify all credential surfaces and revoke at each layer. If revocation cascades to dependent agents: accept the collateral disruption as preferable to continued operation of a compromised agent; restore dependents individually after investigation."
tags:
  - "extracted-artifact"
  - "rule"
  - "governance"
  - "security"
  - "incident-response"
---

# Instant Agent Revocation (Kill Switch)

**Source:** [[instant-agent-revocation-kill-switch-pattern]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent is deployed to production with access to external systems. The deployment does not have a tested, documented procedure for revoking that agent's access within minutes.

## Action

**Required:** Before any agent ships to production, implement and test a kill switch that can revoke the agent's access at the identity/credential layer within 5 minutes. The kill switch must satisfy four requirements: immediate (current execution window, not next deploy), console-accessible (operable by non-developers), granular (targets one agent, not the whole system), and auditable (logged with operator, timestamp, reason).

**Forbidden:** Deploying an agent to production without a tested revocation procedure. Relying on code deploys, tickets, or deletion processes as the primary revocation mechanism. Treating "disable the feature flag" as equivalent to credential revocation (feature flags don't revoke active sessions).

## Boundary

Enforced at the production deployment gate. No agent moves to production without a documented and tested revocation procedure. The test is: execute the revocation in staging, verify access cessation within the target time window.

## Enforcement

Pre-deployment checklist item: "Revocation procedure documented? Tested in staging? Verified within 5-minute window?" Binary pass/fail. The specific mechanism varies by deployment (token revocation API, credential rotation, identity provider suspension) but the diagnostic is universal: can access be cut within minutes from a console?

## Rationale

Agents operate at machine speed — a compromised or malfunctioning agent can enumerate and exploit accessible resources faster than any human can diagnose the problem. The time between detection and revocation is the window during which damage accumulates. The Lilly/McKinsey incident demonstrated that when agents gain unauthorized access, tens of millions of records become accessible. The kill switch shrinks the damage window to the minimum achievable latency.
