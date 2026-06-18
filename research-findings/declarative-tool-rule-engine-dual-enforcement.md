---
name: "Declarative Tool Rule Engine with Dual Enforcement"
summary: "Combined soft (prompt-rendered XML constraints) + hard (programmatic constraint solver) enforcement for tool usage rules. XML tells the model what it should/shouldn't do; the solver rejects invalid tool calls that slip through. Dual layer catches both cooperative failures (model forgets) and adversarial failures (prompt injection)."
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "middleware-as-enforcement-architecture.md"
    rel: same-problem
  - file: "hook-based-enforcement-over-convention.md"
    rel: same-problem
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: raw
consumed_by: []
---

## What It Is

Letta's tool rule system implements a two-layer enforcement architecture for constraining agent tool usage. The **soft layer** renders tool rules as `<tool_usage_rules>` XML in the system prompt — the model reads these and (cooperatively) follows them. The **hard layer** is a `ToolRulesSolver` that programmatically validates each tool call against the declared rules and rejects invalid invocations before execution.

**Rule types supported:**
- `InitToolRule` — first tool that MUST be called
- `TerminalToolRule` — calling this tool ends the agent loop
- `ChildToolRule` — after tool X, must use one of [Y, Z]
- `ParentToolRule` — tool Y can only be called after tool X
- `ConditionalToolRule` — route to child based on tool output
- `MaxCountPerStepToolRule` — limit invocations per step
- `RequiredBeforeExitToolRule` — must call before agent can exit
- `RequiresApprovalToolRule` — human approval required

The solver maintains a state machine of valid transitions. When the model proposes a tool call, the solver checks it against the current state. If invalid, the call is rejected without execution — the model never gets the chance to cause side effects from a rule-violating call.

## Why It Matters

Prompt-only constraints are fundamentally unreliable: models forget instructions, context windows compress rules away, and adversarial inputs can override them. Code-only constraints are robust but invisible to the model, causing confusing failures when the model repeatedly proposes calls that get silently rejected. The dual-layer approach gives the model visibility into what it should do (prompt layer) while guaranteeing enforcement regardless of model compliance (solver layer).

This is particularly relevant for tool sequences where ordering matters — workflows that require initialization before execution, or mandatory cleanup before exit. A single-layer approach either trusts the model (fragile) or fights the model (frustrating UX). The dual layer aligns model behavior with enforcement.

## Why People Are Using It

Observed in [Letta](https://github.com/letta-ai/letta) v0.16.8 — see [[letta-analysis]] for structural details.

**Cross-repo corroboration (CR-25):** Two additional repos independently implement dual-enforcement: DeerFlow (middleware logs intent in prompt via `<tool_usage_rules>` AND intercepts at runtime) and ADK-Python (agent validation at construction + runtime LLM call limits). See [[cross-repo-comparison]] §4 CR-25. This convergence from 3 independent implementations suggests dual enforcement is emerging as a best practice — single-channel enforcement (prompt-only or code-only) is a maturity gap signal.

The system supports 9 distinct rule types covering sequencing, gating, counting, and approval — indicating real production use cases that demanded each constraint type. The `RequiresApprovalToolRule` creates an `ApprovalRequestMessage` that pauses execution for human review, showing integration with human-in-the-loop workflows.

## Potential Alternatives

- Prompt-only rules: simpler implementation, no solver complexity, but relies entirely on model compliance. Appropriate for advisory constraints where violations are annoying but not dangerous.
- Code-only middleware: tool calls validated by hooks without prompt visibility. Robust but the model has no guidance on what is valid, leading to repeated rejected attempts.
- Schema-based validation: constrain tool parameters via JSON Schema rather than tool sequencing. Complementary but orthogonal — handles parameter correctness, not invocation ordering.

## Potential Improvements

- Solver feedback to model: when a tool call is rejected, inject an explanation into the conversation so the model can self-correct rather than blindly retrying.
- Rule composition: allow rule sets to be composed from reusable fragments (e.g., "always-init-first" + "cleanup-before-exit" as composable policies).
- Runtime rule modification: dynamically add or remove rules based on agent state, enabling adaptive constraint tightening as risk increases.

## Potential Failure Modes

- **Rule conflict**: Complex rule sets may contain contradictions (e.g., ChildToolRule says call X, MaxCountPerStepToolRule says X is exhausted) that create deadlocks where no valid tool call exists.
- **Prompt desync**: If the XML-rendered rules and the solver's actual rule set diverge due to a bug, the model follows one set of rules while enforcement follows another.
- **Performance overhead**: The solver checks every tool call against all active rules; for large rule sets with conditional branching, this adds latency to each agent step.
- **Over-constraining**: Too many rules can reduce the model's ability to handle edge cases that the rule author didn't anticipate, turning a flexible agent into a rigid script.
