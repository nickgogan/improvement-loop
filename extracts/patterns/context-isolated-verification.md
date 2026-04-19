---
title: "Context-Isolated Verification"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "context-pollution-same-window-verification-bias"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The workflow includes a verification step that must independently evaluate output; infrastructure exists to spawn an isolated context (sub-agent, fresh session, or separate tool invocation)."
  invariants: "The verifier never shares a context window with the generator; the verifier receives only the output and acceptance criteria, not the reasoning that produced the output."
  governance: "Verification isolation is enforced by architecture, not convention; verification results are logged with their context provenance."
  recovery: "If isolated verification produces false negatives (rejecting correct work due to missing context), provide the verifier with additional factual context without exposing the generator's reasoning chain."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Context-Isolated Verification

**Source:** [[context-pollution-same-window-verification-bias]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

When an agent verifies its own work within the same conversation context that produced it, the verification is systematically biased. The verifier inherits all prior reasoning, assumptions, and errors from the generation phase. It sees the exact reasoning chain that led to the mistake, making it predisposed to rationalize flawed conclusions rather than independently detect them. The verification step appears to work (the agent confidently confirms its output) but provides near-zero error-catching value.

## Forces

- **Implementation simplicity:** Same-window verification is the path of least resistance -- just add another prompt turn. Isolated verification requires spawning separate contexts, which adds infrastructure complexity and latency.
- **Context loss vs. context pollution:** Isolating the verifier removes the polluting reasoning chain but also removes legitimate context (design rationale, constraints, trade-off decisions) that the verifier might need to make correct judgments.
- **Confidence illusion:** Same-window verification produces confident confirmations, which users interpret as genuine validation. The bias is invisible without controlled comparison against independent verification.
- **Cost and latency:** Spawning a separate context for every verification step multiplies inference costs and adds wall-clock time. Not every task warrants this overhead.
- **Proportionality:** Some tasks are low-risk enough that same-window verification is adequate. Over-engineering verification for trivial tasks wastes resources.

## Solution

Spawn verification in an isolated context that does not share the generation context's reasoning history. The verifier receives only:

1. **The output to verify** -- the artifact, code, plan, or answer produced by the generator.
2. **The acceptance criteria** -- what "correct" looks like, expressed as testable conditions.
3. **Relevant factual context** -- project constraints, specifications, and domain facts that the verifier needs to make an informed judgment. Critically, this does NOT include the generator's reasoning chain, explored alternatives, or discarded approaches.

**Implementation options (from lightest to heaviest):**
- **Sub-agent spawn:** Fork a sub-agent that receives only the output and criteria. Available in Claude Code via the `/re` command and fork primitives.
- **Fresh session:** Start a new conversation session for verification. Maximum isolation but highest overhead.
- **Separate tool invocation:** Call an external tool or API that evaluates the output against criteria without access to the conversation history.
- **Cross-model verification:** Use a different model for verification, which provides both context isolation and cognitive diversity.

**When to isolate vs. when same-window is acceptable:**
- Isolate for: architectural decisions, security-relevant code, any output where the cost of an undetected error exceeds the cost of isolated verification.
- Same-window is acceptable for: trivial formatting checks, syntax validation, tasks where external tooling (linters, tests, type checkers) provides the real verification.

## Consequences

**Positive:**
- Verification becomes genuinely independent, capable of catching errors the generation process missed.
- Eliminates the false confidence that same-window verification provides.
- Forces explicit articulation of acceptance criteria, which improves specification quality as a side effect.
- Cross-model verification adds cognitive diversity on top of context isolation.

**Negative:**
- **False negatives from context loss:** The isolated verifier may reject correct work because it lacks legitimate design rationale that explains non-obvious choices.
- **Cost multiplication:** Each isolated verification step adds inference cost (roughly 2x per verified output if using the same model).
- **Latency increase:** Spawning separate contexts adds wall-clock time, which may be unacceptable for interactive workflows.
- **Over-engineering risk:** Applying full context isolation to trivial tasks wastes resources without proportionate benefit.

## Known Uses

- **Claude Code `/re` command and fork-subagent primitive** -- Infrastructure for spawning verification in an isolated context within the Claude Code environment.
- **Builder-Validator Chain pattern** -- Architectural pattern where a builder agent produces output and a separate validator agent evaluates it, each in their own context.
- **Ultra Review multi-agent bug-hunting fleet** -- Multiple independent agents review code in separate contexts, with results aggregated. Context isolation is inherent in the multi-agent architecture.
- **Cross-model verification** -- Using a different model (e.g., GPT for verification of Claude output, or vice versa) provides both context isolation and model-level cognitive diversity.

## Contract

### Preconditions
- The workflow includes a verification step intended to independently evaluate output quality or correctness.
- Infrastructure exists to spawn an isolated context: sub-agent capability, multi-session support, or external evaluation tooling.
- Acceptance criteria can be articulated independently of the generation reasoning (i.e., "correct" is definable without reference to "how we got here").

### Invariants
- The verifier never shares a context window with the generator. This is enforced by architecture, not convention.
- The verifier receives only the output and acceptance criteria, never the reasoning chain that produced the output.
- Factual context (project constraints, specifications) may be shared; generative context (explored alternatives, discarded approaches, intermediate reasoning) must not be.

### Governance
- Verification isolation is enforced by the system architecture (separate processes, sessions, or agents), not by prompting conventions that can be bypassed.
- Verification results are logged with their context provenance (what the verifier saw) so the isolation guarantee is auditable.
- A proportionality rule determines which outputs require isolated verification vs. same-window or tool-based checks.

### Recovery
- If isolated verification produces false negatives (rejecting correct work due to missing context), provide the verifier with additional factual context (specifications, constraints) without exposing the generator's reasoning chain.
- If verification infrastructure fails (sub-agent spawn fails, external service unavailable), fall back to same-window verification with an explicit annotation that isolation was not achieved.
- If cost or latency of isolated verification becomes prohibitive, triage: apply isolation only to high-risk outputs and use tool-based verification (tests, linters) for lower-risk work.
