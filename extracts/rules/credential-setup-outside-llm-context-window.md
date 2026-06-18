---
title: "Credential Setup Outside the LLM Context Window"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "credential-setup-outside-llm-context-window"
extraction_date: "2026-05-25"
last_change_session: 96
last_change_sl: "session-96-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-25-identification-report-session-95.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent setup wizards or onboarding flows that require API keys, tokens, or other secrets"
    - "any agent workflow where credential entry occurs during an interactive session with an LLM"
    - "harness builders designing guided configuration experiences that touch secrets"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "secure"
  reversibility: "medium — requires architectural change to separate credential entry from the agent session; once built, the separation is transparent to the user"
  auditability: "high — the boundary is structural (separate process); compliance is verifiable by inspecting whether credential-handling code paths intersect with LLM API calls"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "The agent workflow includes a step where the user must enter secrets (API keys, OAuth tokens, database credentials). A mechanism exists to spawn a separate process or terminal outside the LLM session (CLI tool, OS terminal, browser-based credential manager)."
  invariants: "No credential value enters the LLM's context window at any point during setup or operation. The LLM session orchestrates credential setup (telling the user what to configure) but never receives the actual credential values. Validation of credential correctness (testing connectivity) occurs without exposing the credential to the model."
  governance: "Owner: the harness or skill author who designs the setup flow. The separation must be enforced by tool architecture (separate process, environment variable injection, vault reference), not by user discipline ('please don't paste your key here'). The boundary is the LLM API call — credentials must not appear in any message sent to the model."
  recovery: "If a credential is accidentally pasted into the LLM session: treat the session as compromised for that credential, rotate the key immediately, and audit the session log for exposure scope. If the separate-terminal mechanism fails (headless environment, no GUI): fall back to environment variable injection or a local config file written outside the session, never to in-session paste."
tags:
  - "extracted-artifact"
  - "rule"
  - "security"
  - "credentials"
---

# Credential Setup Outside the LLM Context Window

**Source:** [[credential-setup-outside-llm-context-window]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent workflow includes a setup or configuration step where the user must enter secrets — API keys, OAuth tokens, database credentials, or any value that would constitute a security exposure if logged, cached, or leaked. The agent is operating within an LLM-backed session where all input becomes part of the model's context.

## Action

**Required:** Route credential entry through a separate process that does not communicate with the LLM. The agent session may orchestrate the flow (instructing the user what to configure, which platforms to set up, what credentials are needed) but must delegate the actual credential-handling to a non-LLM process (separate terminal, CLI tool, environment variable, vault proxy).

**Forbidden:** Accepting credential values directly in the LLM chat session. Logging, caching, or transmitting secrets through any path that intersects with the LLM API. Designing setup flows that require the user to paste secrets into the agent conversation.

## Boundary

Enforced at the interface between the agent session and credential entry. The boundary is the LLM API call itself — any text that will be sent to the model provider is on the wrong side of the boundary for secrets.

## Enforcement

Architectural enforcement via process separation. The credential entry mechanism (CLI tool, setup wizard, vault UI) runs in a separate process with no shared memory or message passing to the LLM session. Validation: the agent session can test whether credentials are working (e.g., attempting an API call and reporting success/failure) without receiving the credential value itself.

## Rationale

Any text entered into an LLM session becomes part of the model's context — sent to the provider's API, potentially logged in conversation history, exposed if the session is shared or if a prompt injection attack extracts context. Process separation creates a hard architectural boundary that cannot be bypassed by user error or agent behavior within the session.
