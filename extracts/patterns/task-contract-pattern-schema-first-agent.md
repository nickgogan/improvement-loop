---
title: "Task Contract Pattern: Schema-First Agent Interactions"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "task-contract-pattern-schema-first-agent"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Multiple agents interact with each other or with a shared orchestrator. Agent boundaries exist where one agent's output becomes another's input. The interaction occurs more than once (not purely ad-hoc)."
  invariants: "Every agent interaction has an explicit contract defining input schema, output schema, quality constraints, and allowed tools. Contracts are validated at runtime, not just documented. Agents cannot negotiate their interfaces in natural language at execution time -- the contract is the interface."
  governance: "Contracts are maintained centrally and versioned. Schema changes follow a review process before deployment. Contract validation failures are logged and surfaced, never silently swallowed."
  recovery: "If an agent produces output that fails contract validation, the output is rejected and the failure is reported with the specific schema violation. The agent may retry with the contract constraints re-emphasized, but the contract is never relaxed to accommodate invalid output."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Task Contract Pattern: Schema-First Agent Interactions

**Source:** [[task-contract-pattern-schema-first-agent]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Without explicit contracts, agents negotiate their interfaces in natural language at runtime -- introducing ambiguity, drift, and hallucination at every boundary. Agent A produces output that agent B cannot parse. Agent B fills in missing fields with hallucinated values. Schema drift accumulates silently across sessions. The system appears to work until a subtle boundary mismatch causes a cascade failure that is difficult to diagnose.

## Forces

- **Flexibility vs. predictability:** Agents are valued for their ability to handle ambiguous tasks, but boundaries between agents require predictable interfaces. Over-specifying contracts constrains flexibility; under-specifying them invites hallucination.
- **Upfront specification cost vs. runtime failure cost:** Defining schemas, quality constraints, and tool permissions for every interaction takes effort. Skipping it feels faster until the first boundary-crossing hallucination wastes hours of debugging.
- **Centralized control vs. agent autonomy:** Centrally maintained contracts ensure consistency but create a bottleneck for contract updates. Agent-local contracts enable faster iteration but drift from each other.
- **Schema evolution vs. backward compatibility:** Agents and their capabilities evolve. Contracts must evolve with them without breaking downstream consumers that depend on the previous schema.

## Solution

Establish explicit contracts as Layer 0 (foundational infrastructure) of any multi-agent system. Every agent interaction gets a contract defining five components:

1. **Input schema.** The exact structure, types, and required fields the agent expects to receive. Validated before the agent begins processing. Invalid input is rejected, not guessed at.

2. **Output schema.** The exact structure, types, and required fields the agent must produce. Validated after the agent completes. Invalid output is rejected, not passed downstream.

3. **Quality constraints (must/should).** Mandatory constraints ("output must contain at least one cited source") and advisory constraints ("output should be under 500 words"). Must-constraints trigger rejection on violation; should-constraints trigger warnings.

4. **Cost/latency budgets.** Maximum allowed token usage, maximum allowed wall-clock time, maximum allowed API calls. Prevents unbounded agent execution and makes resource usage predictable.

5. **Allowed tools per role.** Each agent role has an explicit tool allowlist. The orchestrator agent can read/write state; the researcher agent can search but not write; the executor can write code but not modify configs. This prevents privilege creep across agent boundaries.

Contracts are maintained centrally and inherited by all agent sessions. They are the single source of truth for what each agent can receive, produce, and do. This maps directly to API contract-first development, which has decades of precedent in service-oriented architecture.

Runtime validation is non-negotiable. A contract that exists only as documentation provides no protection against boundary violations. Validation must happen at the boundary -- before input is processed and after output is produced.

## Consequences

**Positive:**
- Eliminates hallucination at agent boundaries by replacing natural-language negotiation with validated schemas
- Makes agent behavior predictable and testable -- contracts serve as both specification and test harness
- Prevents context rot across sessions by enforcing structural consistency
- Provides organizational infrastructure that scales with the number of agents and interactions
- Cost/latency budgets prevent unbounded agent execution and make resource usage plannable

**Negative:**
- Over-specification constrains agent flexibility for genuinely exploratory tasks where the output shape is not known in advance
- Contract maintenance overhead accumulates as the number of agent interactions grows
- Schema drift between contract definition and actual behavior occurs if validation is not enforced at runtime -- documentation-only contracts provide false confidence
- Centralized contract management can become a bottleneck if contract updates require heavyweight review processes
- Initial contract design requires understanding agent capabilities well enough to specify realistic schemas -- premature contracts may need frequent revision

## Known Uses

- Nick Gupta's production multi-agent playbook -- identifies task contracts as Layer 0 (foundational) infrastructure
- Microsoft Agent Framework -- treats contracts as first-class primitives for agent interaction
- API contract-first development in service-oriented architecture -- decades of precedent for schema-first interface design
- MetaSystem SKILL.md files -- partially implement this pattern by defining inputs and outputs, but lack formal schemas, quality constraints, and cost/latency budgets
- MetaSystem ContractSpec (DD-78) -- the governance contract pattern (preconditions, invariants, governance, recovery) applied to all codified artifacts

## Contract

### Preconditions
Multiple agents interact with each other or with a shared orchestrator. Agent boundaries exist where one agent's output becomes another agent's input. The interaction occurs more than once -- purely ad-hoc one-time interactions do not justify the upfront cost of contract definition. The contract author understands both the producing agent's capabilities and the consuming agent's requirements.

### Invariants
Every agent interaction has an explicit contract defining input schema, output schema, quality constraints, and allowed tools. Contracts are validated at runtime at every boundary crossing, not just documented. Agents cannot negotiate their interfaces in natural language at execution time -- the contract is the interface. Must-constraints trigger rejection on violation; should-constraints trigger warnings. Cost/latency budgets are enforced, not advisory.

### Governance
Contracts are maintained in a central registry and versioned. Schema changes follow a review process before deployment to prevent breaking downstream consumers. Contract validation failures are logged with the specific schema violation and surfaced to operators, never silently swallowed. The contract registry is audited periodically for unused, stale, or conflicting contracts.

### Recovery
If an agent produces output that fails contract validation, the output is rejected and the failure is reported with the specific schema violation. The agent may retry with the contract constraints re-emphasized in its context, but the contract is never relaxed to accommodate invalid output. If a contract is discovered to be systematically unachievable (agents consistently fail validation), the contract is revised through the governance process -- not bypassed at runtime. If the central registry becomes unavailable, agents halt at boundaries rather than proceeding without validation.
