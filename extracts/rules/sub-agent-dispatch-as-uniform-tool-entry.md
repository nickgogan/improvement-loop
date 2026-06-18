---
title: "Sub-Agent Dispatch as Uniform Tool Entry"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "subagent-as-uniform-tool-interface"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "orchestrator agents whose tool registry includes both standard tools and sub-agent dispatch"
    - "system builders designing multi-agent orchestration layers"
    - "any framework where an agent can spawn another agent as part of its execution"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — retrofitting a uniform interface onto an orchestration system that already has special-case delegation logic requires refactoring the orchestration layer; forward adoption is straightforward"
  auditability: "high — a single tool registry with a uniform call/result/checkpoint path means all actions (including sub-agent dispatch) appear in the same hook and log pipeline; no separate audit path needed"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Documented from Claude Code's architecture (agent tool in the same registry as bash, file-read, grep). Also present in Anthropic's managed agents (brain-hands decoupling, uniform execute(name, input) -> string interface). Described as a deliberate architectural principle, not an accident. No MetaSystem implementation yet."
contract:
  preconditions: "An orchestration layer is being designed or refactored. The system supports a tool registry — a discrete list of capabilities the orchestrator can invoke. At least one of those capabilities is the dispatch of a sub-agent."
  invariants: "Sub-agent dispatch is registered as a standard tool entry (e.g., 'agent_tool') alongside all other tools. The orchestrator calls sub-agent dispatch through the identical call/result/checkpoint path it uses for all other tools. No special-case logic exists in the orchestrator for delegation — spawning a sub-agent does not require a different code path, error-handling branch, or permission mechanism than invoking bash or file-read. Hooks (pre-tool, post-tool), logging, and permission checks apply to sub-agent dispatch automatically, without modification."
  governance: "Owner: the architect of the orchestration layer. The rule applies at design time, not at the level of individual agent sessions. Any addition of a new sub-agent type is implemented as a new tool entry, not as a change to the orchestration logic. Code review for orchestration layers should flag any conditional branching that distinguishes sub-agent dispatch from standard tool dispatch as a violation."
  recovery: "If special-case delegation logic is discovered in an existing orchestration layer → refactor it to a tool entry; document the refactor as a design change. If the uniform interface masks resource management concerns (e.g., sub-agent cost, depth limits) → handle those concerns in hook logic or tool metadata, not by breaking the uniform call path. If unbounded recursive spawning is detected → enforce depth limits in a pre-tool hook; do not introduce a separate recursion guard in the orchestration layer."
tags:
  - "extracted-artifact"
  - "rule"
  - "orchestration"
  - "multi-agent"
  - "architecture"
---

# Sub-Agent Dispatch as Uniform Tool Entry

**Source:** [[subagent-as-uniform-tool-interface]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An orchestration layer is being designed or refactored, and it includes the ability to spawn sub-agents as part of the execution path. The system supports a tool registry (a discrete list of callable capabilities).

Scope: applies to any orchestration layer where the orchestrator can both invoke standard tools (bash, file operations, API calls) and spawn sub-agents. Does not apply to single-agent systems with no sub-agent dispatch.

## Action

**Required:** Register sub-agent dispatch as a standard tool entry in the tool registry. The orchestrator must invoke sub-agent dispatch through the identical call/result/checkpoint path it uses for all other tools. Pre-tool hooks, post-tool hooks, logging, and permission checks must apply to sub-agent dispatch without requiring modification.

**Forbidden:**
- Introducing special-case logic in the orchestrator that distinguishes sub-agent dispatch from standard tool invocations.
- Creating a separate permission mechanism, error-handling branch, or API surface for sub-agent dispatch that does not exist for other tools.
- Bypassing the tool registry for sub-agent spawning (e.g., direct programmatic invocation of the sub-agent that skips hooks).

## Boundary

Enforced at the design of the orchestration layer. The rule applies at the point where the tool registry is defined and whenever a new sub-agent type is added. It is not a runtime check — it is a structural invariant of the orchestration layer's implementation.

## Enforcement

- **Mechanism:** Code review of the orchestration layer checks that sub-agent dispatch follows the same call path as other tools. The presence of conditional branching that identifies `is_sub_agent_call` as distinct from `is_tool_call` is a violation signal.
- **Check (deterministic):** `(sub_agent_dispatch_registered_as_tool == true) AND (no_special_case_delegation_logic == true) AND (hooks_apply_to_sub_agent_calls == true)`. Any branch false → violation.
- **Violation response:**
  - *Special-case delegation logic present:* refactor to a tool entry; document as a design change.
  - *Hooks not firing on sub-agent dispatch:* the sub-agent is bypassing the tool registry; route it through the registry.
  - *New sub-agent type added outside registry:* treat as an undeclared capability; add it to the registry before production use.
- **Testability benefit:** sub-agent dispatch can be mocked identically to any other tool call; integration tests do not require special harness for multi-agent scenarios.

## Rationale

Interface homogeneity delivers three compounding benefits that justify the rule as a hard constraint rather than a recommendation:

1. **Hooks work for free.** Safety checks, logging, and permission gates that apply to tool calls automatically cover sub-agent dispatch without a separate "agent permission" system. This eliminates a class of security gaps where sub-agent actions bypass the audit trail that covers standard tool use.

2. **Tool registry is the single source of capabilities.** Enumerating all available actions in one place — including sub-agent dispatch — makes the orchestrator's capability set auditable and bounded. Adding a new sub-agent type means adding a tool entry, not modifying orchestration logic. This constrains capability sprawl.

3. **Testability without special harness.** Sub-agent dispatch is mockable the same way as a bash command. This is a direct consequence of structural uniformity.

The pattern is documented in Claude Code's architecture as a deliberate design choice enabling a clean-room rewrite across language implementations (TypeScript → Python → Rust) without accumulating special-case migration debt.

## Failure Modes

- **Leaky abstraction from resource asymmetry.** Sub-agents have fundamentally different resource profiles (longer running, higher cost, own context window) than simple tools. The uniform interface may hide resource management concerns. Mitigation: expose resource metadata (cost estimate, expected duration, context depth) as tool entry fields rather than breaking the call path uniformity.
- **Error semantics mismatch.** A bash command failing returns an error string. A sub-agent failing may mean partial work was done and state was modified. The uniform string return masks this difference. Mitigation: define a structured error envelope within the string return; document that sub-agent errors require a different recovery action than simple tool errors.
- **Unbounded recursive spawning.** If sub-agents can call the agent tool themselves, recursive spawning is possible. The uniform interface does not inherently prevent this. Mitigation: enforce depth limits in a pre-tool hook applied to the agent tool entry; do not introduce a separate recursion guard in the orchestration layer.

## Contract

### Preconditions
An orchestration layer is being designed or refactored. The system supports a tool registry — a discrete list of capabilities the orchestrator can invoke. At least one of those capabilities is the dispatch of a sub-agent.

### Invariants
Sub-agent dispatch is registered as a standard tool entry (e.g., 'agent_tool') alongside all other tools. The orchestrator calls sub-agent dispatch through the identical call/result/checkpoint path it uses for all other tools. No special-case logic exists in the orchestrator for delegation — spawning a sub-agent does not require a different code path, error-handling branch, or permission mechanism than invoking bash or file-read. Hooks (pre-tool, post-tool), logging, and permission checks apply to sub-agent dispatch automatically, without modification.

### Governance
Owner: the architect of the orchestration layer. The rule applies at design time, not at the level of individual agent sessions. Any addition of a new sub-agent type is implemented as a new tool entry, not as a change to the orchestration logic. Code review for orchestration layers should flag any conditional branching that distinguishes sub-agent dispatch from standard tool dispatch as a violation.

### Recovery
If special-case delegation logic is discovered in an existing orchestration layer → refactor it to a tool entry; document the refactor as a design change. If the uniform interface masks resource management concerns (e.g., sub-agent cost, depth limits) → handle those concerns in hook logic or tool metadata, not by breaking the uniform call path. If unbounded recursive spawning is detected → enforce depth limits in a pre-tool hook; do not introduce a separate recursion guard in the orchestration layer.
