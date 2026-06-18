---
title: "Hook-Based Enforcement for Agent Outputs"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "hook-based-enforcement-for-agent-outputs"
extraction_date: "2026-05-25"
last_change_session: 103
last_change_sl: "session-103-codifier-complete-extract-artifacts-write-phase"
identification_report: "2026-05-24-identification-report-2.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Agents that issue tool calls modifying shared external state — issue trackers, version control, databases, APIs — where structural invalidity causes downstream cost or harm"
    - "Any agent workflow where the gap between 'agent instructed to do X' and 'agent verifiably did X in the correct form' needs to be closed at the tool-call boundary"
    - "Production deployments where context-window pressure or long-running tasks introduce risk of the agent misapplying its own structural rules"
    - "Teams defining agent configurations that need enforcement to be a property of the agent definition itself, not a separate operational layer"
  platform_coupling: "specific:claude-code"
  autonomy: "all"
  stage: "secure"
  reversibility: "medium — hooks are defined in configuration files and can be updated or removed; however, outputs that passed through a permissive or missing hook may have already modified external state and require auditing"
  auditability: "High when hook validation logic is version-controlled alongside the agent definition and hook firing is logged per tool call; medium when hooks exist but firing is not externally logged; low when enforcement is instruction-only"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Observed in Archon v0.3.2 triage agent — PostToolUse hook defined in agent frontmatter validates GitHub label application for type, effort, priority, and area categories."
contract:
  preconditions: "The agent produces tool calls that modify external shared state subject to structural constraints. The execution harness supports PostToolUse hooks. Structural constraints are fully enumerated before the hook is written."
  invariants: "The hook fires on every tool call of the specified type — not selectively or probabilistically. Validation logic covers the full set of enumerated constraints. Failed validation causes retry, never silent pass. The hook is version-controlled alongside the agent definition."
  governance: "The agent definition and its hook are co-owned — changes to structural constraints require changes to both. Hook validation logic is authoritative for structural validity; instructions describe intent, hooks determine the gate."
  recovery: "Hook too strict: diagnose the false positive, add the valid pattern, redeploy — do not disable the hook. Hook too permissive: audit all outputs accepted since the gap was introduced; tighten before re-enabling. Agent fails retry limit: escalate to human with the tool call, error message, and retry attempts."
tags:
  - "extracted-artifact"
  - "rule"
---

# Hook-Based Enforcement for Agent Outputs

**Source:** [[hook-based-enforcement-for-agent-outputs]]
**Source (additional):** [[tool-call-event-interception-pattern]]
**Form:** rule
**Extraction date:** 2026-05-25

A rule requiring that structural constraints on agent tool-call outputs be enforced by PostToolUse hooks — not by instructions alone. Instructions are soft constraints that agents can misinterpret, forget, or override under context pressure; hooks are hard gates at the tool-call boundary that catch violations before they reach external systems.

## Condition

An agent produces outputs — tool calls, API mutations, database writes, external state changes — that must satisfy structural constraints (field presence, valid label combinations, cardinality requirements, enum conformance). The agent receives instructions about these constraints in its system prompt, agent definition, or CLAUDE.md. The outputs modify shared state that is expensive or time-consuming to reverse.

## Action

**Required:** Define a PostToolUse hook in the agent's configuration that fires after every tool call in the relevant category. The hook must:
- Inspect the tool call output or command for structural conformance.
- Apply a deterministic or prompt-based validation check against the required constraints.
- Reject the operation and return a structured error message if the check fails, requiring correction before proceeding.

The hook is defined in the agent's frontmatter or configuration file alongside its name, description, model, and tools — making enforcement a property of the agent definition, not a separate operational layer.

**Forbidden:** Relying solely on agent instructions to enforce structural constraints on outputs that modify shared state. Instruction-only enforcement is not enforcement for purposes of this rule.

## Boundary

Enforced at the **PostToolUse boundary** — after the tool has been called but before the result is accepted as valid. Applies to every tool call of the specified type within the agent's execution scope.

Out of scope: agent-internal reasoning and planning steps (which remain instruction-governed), read-only tool calls with no external state impact, and human-gated actions where a human reviews the output before it reaches the external system.

## Enforcement

- **Mechanism:** A PostToolUse hook defined in the agent's configuration file. The hook receives the tool call and applies a validation function — either deterministic (regex, JSON schema, enum check, cardinality count) or prompt-based (a validator prompt that returns pass/fail + error message).
- **Deterministic checks (preferred):** For label-application commands: count labels per required category; verify cardinality. For field-presence: verify required fields are non-null. For enum conformance: verify the value is a member of the allowed set.
- **Prompt-based checks (fallback):** When structural validity cannot be expressed deterministically. Must return a structured pass/fail verdict. Carries the failure modes of prompt-based evaluation — prefer deterministic checks wherever the constraint can be expressed that way.
- **Violation response:** The hook returns a structured error identifying which constraint was violated. The agent retries with a corrected output. If the agent fails after a configurable retry limit, escalate to human review — do not silently accept an invalid output.

## Rationale

Agent instructions are soft constraints. In long contexts, under pressure, or when inputs are unexpected, agents misinterpret, forget, or rationalize past their own instructions. This is not a model failure — it is a fundamental property of instruction-following systems operating under distribution shift.

Hooks enforce at the tool-call boundary, where the output has already been formed but has not yet been accepted. This is the last intervention point before the output reaches external systems. Catching violations here is categorically cheaper than catching them after the fact.

Defining the hook in the agent's configuration frontmatter makes enforcement a property of the agent definition — the agent ships with its own constraints, reducing the failure mode where enforcement exists in a separate system maintained out of sync.

### Additional Evidence

The tool-call event interception pattern ([[tool-call-event-interception-pattern]]) describes a more capable variant of the hook mechanism: typed `tool_call` events fire before execution and allow handlers to either block (return `{ block: true, reason: "..." }`) or mutate arguments in-place. The pattern is bidirectional — a `tool_result` event fires after execution for post-call inspection. This reinforces the hook-based enforcement approach by showing the full intercept lifecycle: PreToolUse blocking (prevent the call), argument mutation (normalize or transform before execution), and PostToolUse inspection (validate the result). Claude Code's exit-code hooks are a simpler variant of the same pattern. The enforcement invariants in this rule — hook fires on every call of the specified type, validation covers all enumerated constraints, failed validation causes retry — hold for both the exit-code hook variant and the typed event-intercept variant.

## Contract

### Preconditions
The agent produces tool calls that modify external shared state, and those tool calls are subject to structural constraints (field presence, cardinality, enum conformance, or semantic validity). The agent execution harness supports PostToolUse hooks defined in the agent's configuration. The structural constraints are fully enumerated before the hook is written — partial enumeration produces partial enforcement.

### Invariants
The hook fires on every tool call of the specified type within the agent's execution scope — not selectively or probabilistically. The hook's validation logic covers the full set of enumerated structural constraints. A failed validation causes the agent to retry with a corrected output; it does not produce a silent pass. The hook is defined in the agent's configuration frontmatter and is version-controlled alongside the agent definition.

### Governance
The agent definition and its hook are co-owned — changes to structural constraints require changes to both. The hook validation logic is authoritative for what constitutes a structurally valid output; agent instructions describe the intent, but the hook determines the gate. Hook changes must be tested against known-valid and known-invalid outputs before deployment.

### Recovery
If a hook is too strict and blocks valid agent outputs: do not disable the hook — diagnose the false positive, add the valid pattern to the hook's acceptance criteria, and redeploy. If a hook is too permissive and passes invalid outputs: treat all outputs accepted since the permissiveness was introduced as potentially invalid; audit the affected outputs; tighten the hook before re-enabling. If the agent fails to correct after the retry limit: escalate to human review with the original tool call, the hook's error message, and the agent's retry attempts as evidence.
