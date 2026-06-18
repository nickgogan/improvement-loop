---
title: "Runtime Extension Governance Policy"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "runtime-self-modification-via-extension-api"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent harnesses that support runtime extension registration (tools, providers, commands, event handlers)"
    - "any system where an agent can register or modify its own capabilities during a live session"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "secure"
  reversibility: "medium — runtime-registered extensions can be unregistered within the session; extensions persisted to disk require file deletion and session restart"
  auditability: "all extension registration events (name, source, registering agent, timestamp) must appear in the session audit log; conflict resolutions must be logged with the winning policy"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "The harness exposes an API by which agents can register new extensions (tools, providers, commands, keyboard shortcuts, message renderers, or event handlers) at runtime. At least one agent in the system is capable of creating and submitting extensions during a live session."
  invariants: "Every extension registration must carry a trust classification (human-authored vs agent-generated) visible in the audit log. Conflict resolution policy (e.g., last-writer-wins, explicit priority, rejection) is declared in static configuration — not resolved ad-hoc at runtime. No agent-generated extension that modifies model routing, provider selection, or security-critical event handlers is activated without a human gate step. The audit log records every registration and conflict resolution event; this log is append-only and cannot be modified by the registering agent."
  governance: "Owner: the harness configuration and the agent specifications that define which agents may submit extensions. Trust classification levels and the list of security-critical extension categories subject to human gating must be declared in static config, not inferred at runtime. Any skill or agent spec that grants extension-registration authority must reference this rule and state which trust class and conflict policy applies."
  recovery: "If a conflict is detected and no resolution policy is declared → reject the second registration; surface a human-readable conflict report and require explicit resolution before re-attempting. If an agent-generated extension passes the trust gate but produces unexpected behavior → disable the extension, restore pre-registration behavior, and log the rollback event. If the audit log is missing or incomplete for a session in which extensions were registered → invalidate all extensions registered in that session and require re-registration under audit."
tags:
  - "extracted-artifact"
  - "rule"
  - "agent-design"
  - "security"
  - "extension-api"
  - "self-modification"
---

# Runtime Extension Governance Policy

**Source:** [[runtime-self-modification-via-extension-api]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent harness exposes a runtime extension API — allowing tools, providers, commands, keyboard shortcuts, message renderers, or event handlers to be registered during a live session. An agent (including the agent itself) may submit an extension for registration.

This rule applies to any extension-registration event regardless of who originates it (human operator, orchestrator, or the agent itself).

## Action

**Required:**
1. Classify every incoming extension by trust level: `human-authored` (operator-submitted) or `agent-generated` (created by the agent at runtime).
2. Apply the declared conflict resolution policy when two extensions claim the same name or hook. Policy must be specified in static configuration before any session begins.
3. Gate agent-generated extensions that touch security-critical categories (model routing, provider selection, auth handlers, audit hook overrides) on an explicit human approval step before activation.
4. Append a registration record to the audit log: extension name, category, trust class, registering identity, timestamp, and conflict resolution outcome.

**Forbidden:** Activating an agent-generated extension on a security-critical hook without a human gate. Resolving name conflicts through undeclared ad-hoc logic. Allowing the registering agent to modify or delete its own audit log entry.

## Boundary

Applies from the moment an extension-registration call is received by the harness until the extension is either activated or rejected. Covers the full runtime of the session — not only startup. The rule does not govern read-only introspection of the extension registry.

## Enforcement

- **Mechanism:** The harness enforces trust classification and the conflict policy as pre-activation checks; these are not delegated to the submitting agent.
- **Check (deterministic):** `(trust_class_assigned == true) AND (conflict_policy_applied == true) AND (security_critical_agent_ext → human_gate_cleared == true) AND (audit_entry_written == true)`. Any branch false → registration rejected.
- **Violation response:** Reject the registration, log the rejection reason, and surface a human-readable report. Do not silently fail or queue for later retry.
- **Cannot be self-certified:** Audit logging must be handled by a layer the submitting agent cannot reach — a harness-level hook, not an agent-level callback.

## Rationale

A harness that lets agents register their own extensions is genuinely self-modifying. This expands capability at the cost of a new attack surface: an agent under adversarial or confused prompt conditions can install tools or override model routing without operator knowledge. The four-point policy (trust classification, conflict resolution, human gate on critical categories, audit logging) bounds the risk surface without prohibiting self-modification. The key principle is that the governance layer is static config that precedes the session; it cannot be overridden by the same runtime mechanism it governs.

The failure modes documented in the source (conflict explosion, security bypass via agent-created extensions, jiti sandboxing risk) map directly to the four invariants: conflicts require a pre-declared policy, security-critical extensions require a human gate, and audit logging is the minimum observable for after-the-fact review.

## Failure Modes

- **Conflict policy gap.** Two extensions claim the same tool name but no conflict policy covers that category. Mitigation: declare a default fallback policy (e.g., reject-on-conflict) in static config; never allow implicit resolution.
- **Misclassified trust level.** An agent-generated extension is mislabeled as human-authored, bypassing the security gate. Mitigation: trust classification is assigned by the harness based on registration channel (operator CLI vs agent API call), not by the submitting agent.
- **Security-critical category list drift.** A new extension category is added to the harness but not added to the security-critical list, creating an ungated bypass. Mitigation: the security-critical category list is reviewed when new extension categories are added to the API; the Owner agent is the reviewer.
- **Audit log omission.** An extension registers successfully but the audit entry write fails silently. Mitigation: treat audit write failure as a registration failure — do not activate an extension whose log entry cannot be confirmed.

## Contract

### Preconditions
The harness exposes an API by which agents can register new extensions (tools, providers, commands, keyboard shortcuts, message renderers, or event handlers) at runtime. At least one agent in the system is capable of creating and submitting extensions during a live session.

### Invariants
Every extension registration must carry a trust classification (human-authored vs agent-generated) visible in the audit log. Conflict resolution policy (e.g., last-writer-wins, explicit priority, rejection) is declared in static configuration — not resolved ad-hoc at runtime. No agent-generated extension that modifies model routing, provider selection, or security-critical event handlers is activated without a human gate step. The audit log records every registration and conflict resolution event; this log is append-only and cannot be modified by the registering agent.

### Governance
Owner: the harness configuration and the agent specifications that define which agents may submit extensions. Trust classification levels and the list of security-critical extension categories subject to human gating must be declared in static config, not inferred at runtime. Any skill or agent spec that grants extension-registration authority must reference this rule and state which trust class and conflict policy applies.

### Recovery
If a conflict is detected and no resolution policy is declared → reject the second registration; surface a human-readable conflict report and require explicit resolution before re-attempting. If an agent-generated extension passes the trust gate but produces unexpected behavior → disable the extension, restore pre-registration behavior, and log the rollback event. If the audit log is missing or incomplete for a session in which extensions were registered → invalidate all extensions registered in that session and require re-registration under audit.
