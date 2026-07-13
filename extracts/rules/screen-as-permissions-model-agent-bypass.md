---
title: "Screen-as-Permissions-Model Agent Bypass Failure"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "screen-as-permissions-model-agent-bypass-failure"
extraction_date: "2026-05-24"
last_change_session: 146
last_change_report: "2026-07-13-source-drift"
identification_report: "2026-05-24-identification-report.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Teams or individuals deploying agents that call third-party or internal APIs originally built for browser-based human users"
    - "Systems where agents are granted API access without an explicit review of which endpoints are authenticated vs. UI-only gated"
    - "Any agentic workflow that integrates with APIs across organizational boundaries where the agent operator does not control the API design"
    - "Security reviews of existing agent integrations where the original API was not designed with programmatic agent callers in mind"
    - "Organizations evaluating agent-platform infrastructure, where permission scoping, data reach, and audit trails — not model capability — are the load-bearing layer"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "secure"
  reversibility: "medium — revoking agent API access and rotating credentials is straightforward; remediating unauthenticated endpoints in an API the agent operator does not own may require coordination with a third party"
  auditability: "High when the API audit checklist is a versioned document co-located with the agent definition and credential scope is recorded in a configuration file; low if the audit is informal and undocumented."
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Confirmed as an industry-wide systemic pattern, not a single-org failure: six major vendors (Anthropic, OpenAI, SAP, Pinecone, Salesforce, ServiceNow) announced converging agent-permission infrastructure in a single week in early 2026. No local adoption yet."
contract:
  preconditions: "An agent is being configured to call one or more external APIs. The APIs were originally designed for human users navigating a UI. An audit process exists or can be bootstrapped. The agent deployment is not yet live, or if live, the API surface has not been previously audited for agent-unaware permission surfaces."
  invariants: "Every external API endpoint callable by an agent has authentication that does not depend on UI navigation. Every API surface is treated as potentially callable by an adversarial agent, regardless of whether any agent is currently pointed at it. Agent credentials are scoped narrower than full user session credentials. No new external API is added to an agent's toolset without completing the API audit checklist first. The audit record is preserved alongside the agent definition."
  governance: "Owner: whoever maintains the agent definition or integration configuration. The audit checklist must be completed and signed off before the integration is approved. Credential scoping decisions require explicit human review — they cannot be delegated to model judgment. When an API surface changes (new endpoints added, authentication model updated), a re-audit is triggered."
  recovery: "If an unauthenticated write endpoint is discovered post-integration: (1) immediately revoke agent access to the API, (2) notify the API owner to gate or authenticate the endpoint, (3) re-audit the full API surface before restoring agent access. If overly broad credentials were issued: rotate to scoped credentials before the next agent session. If the audit was skipped at onboarding: treat the integration as unreviewed and run the audit before the next agent invocation."
tags:
  - "extracted-artifact"
  - "rule"
  - "security"
  - "governance"
---

# Screen-as-Permissions-Model Agent Bypass Failure

**Source:** [[screen-as-permissions-model-agent-bypass-failure]]
**Form:** rule
**Extraction date:** 2026-05-24

## Condition

An agent calls an external API that was designed for human users navigating a UI. The API relies on the UI as an implicit permissions boundary — endpoints that human users can only reach through a gated screen are exposed directly at the HTTP layer without their own authentication. The agent bypasses the UI entirely, calling endpoints programmatically.

This condition is systemic, not incidental: any API designed under the assumption that only humans reach it via a screen carries this exposure, whether or not an agent has been pointed at it yet.

## Action

**Required:** Before any agent is authorized to call an external API, that API must be audited for agent-unaware permission surfaces: endpoints that lack authentication, endpoints whose only access control was the UI path required to reach them, and endpoints with write or delete semantics that were assumed to be safe because they were UI-only. Every endpoint an agent may call must have its own authentication check, independent of whether a human could reach it through a gated screen.

**Required:** Agent permissions must be scoped separately from user permissions. An agent acting on behalf of a user must not inherit that user's full session scope; it must be issued a narrower credential scoped to the specific operations the agent is authorized to perform.

**Required:** Treat every API surface as potentially callable by an adversarial agent. The audit posture is not "which endpoints will our agent call" but "which endpoints can any agent reach" — autonomous agents probing public endpoints for production data is an observed, routine occurrence.

**Forbidden:** Assuming that an endpoint is safe for agent consumption because it requires human navigation to reach in the UI. Deploying agents against APIs that have not been audited for unauthenticated endpoints. Issuing agents broad session-level credentials when operation-scoped credentials are feasible.

## Boundary

Enforced at **API onboarding** — before an agent integration is approved and before any agent makes live calls to an external API. Also enforced at **permission provisioning** — the moment agent credentials are issued, their scope must be documented and reviewed.

## Enforcement

- **Mechanism:** An API audit checklist is completed before any new external API is added to an agent's toolset. The checklist verifies: (1) each callable endpoint has authentication independent of UI gating, (2) write/delete endpoints require explicit scope grants, (3) agent credentials are narrower than user session credentials.
- **Check:** `(api_endpoint_auth_independent_of_ui == true) AND (agent_credential_scope != full_user_session_scope) AND (audit_completed_before_first_agent_call == true)`.
- **Violation response:** If an unauthenticated write endpoint is discovered post-integration, revoke agent access to that API immediately, patch or gate the endpoint, then re-audit before restoring access. If broad credentials were issued, rotate to narrower scoped credentials before the next agent session.

## Rationale

The Lilly/McKinsey incident demonstrated this failure mode at production scale: 22 of 200 API endpoints were unauthenticated, including endpoints with production write access. A $20 autonomous agent obtained read/write access to data used by 70% of 40,000 consultants. As of early 2026, autonomous agents probing public endpoints for production data is described as "very normal."

This is not a single-organization hygiene failure — it is an industry-wide systemic pattern. Within a single week in early 2026, six major vendors (Anthropic, OpenAI, SAP, Pinecone, Salesforce, ServiceNow) announced converging infrastructure aimed at exactly this gap. As the source analysis puts it: "The model was never the hard part. The hard part is whether the agent can reach the right data, use the right permissions, trigger the right workflow, leave the right audit trail." APIs designed under the assumption that only humans reach them via a UI are inherently unsafe for agentic consumption. The UI was the security boundary; agents have no UI — and the market-wide vendor response confirms the pattern's systemic scope.

## Contract

### Preconditions
An agent is being configured to call one or more external APIs. The APIs were originally designed for human users navigating a UI. An audit process exists or can be bootstrapped. The agent deployment is not yet live, or if live, the API surface has not been previously audited for agent-unaware permission surfaces.

### Invariants
Every external API endpoint callable by an agent has authentication that does not depend on UI navigation. Every API surface is treated as potentially callable by an adversarial agent, regardless of whether any agent is currently pointed at it. Agent credentials are scoped narrower than full user session credentials. No new external API is added to an agent's toolset without completing the API audit checklist first. The audit record is preserved alongside the agent definition.

### Governance
Owner: whoever maintains the agent definition or integration configuration. The audit checklist must be completed and signed off before the integration is approved. Credential scoping decisions require explicit human review — they cannot be delegated to model judgment. When an API surface changes, a re-audit is triggered.

### Recovery
If an unauthenticated write endpoint is discovered post-integration: (1) immediately revoke agent access, (2) notify the API owner, (3) re-audit before restoring access. If overly broad credentials were issued: rotate to scoped credentials before the next agent session.
