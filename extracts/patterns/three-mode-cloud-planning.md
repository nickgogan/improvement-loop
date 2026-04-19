---
title: "Three-Mode Cloud Planning"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "claude-code-ultra-plan-three-mode-planning"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Agent has access to a cloud planning service with multiple planning strategies; task complexity can be assessed before planning begins."
  invariants: "Planning output is always reviewed by a human before execution begins; the planning context remains isolated from the execution context."
  governance: "Plan selection criteria are explicit and auditable; plan artifacts are versioned and diffable between iterations."
  recovery: "If cloud planning is unavailable, fall back to local planning mode; if the wrong plan mode is selected, discard and re-plan without polluting the execution context."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Three-Mode Cloud Planning

**Source:** [[claude-code-ultra-plan-three-mode-planning]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Single-strategy planning produces plans that are either too shallow for complex tasks or wastefully elaborate for simple ones. Agents that plan in the same context where they execute risk polluting their working memory with planning artifacts, and local planning is slower than cloud-offloaded alternatives.

## Forces

- **Complexity variance:** Tasks range from trivial (rename a variable) to architecturally significant (redesign a module). A single planning depth wastes resources on one end and misses risks on the other.
- **Context contamination:** Planning reasoning (explored alternatives, rejected approaches, risk assessments) occupies context window space that execution needs for code, tests, and tool output.
- **Speed vs. thoroughness:** Deeper planning catches more issues but delays execution. Shallow planning is fast but misses dependencies and risks.
- **Autonomy vs. control:** Fully autonomous mode selection may mismatch user intent; fully manual selection adds friction.

## Solution

Separate planning from execution by offloading it to an isolated environment (cloud or sub-agent), and provide three graduated planning modes matched to task complexity:

1. **Simple plan** -- Basic task breakdown. Suitable for well-understood, low-risk changes. Produces a linear sequence of steps.
2. **Visual plan** -- Structured plan augmented with diagrams (ASCII, Mermaid, or similar). Suitable for tasks with non-trivial control flow or data dependencies where spatial reasoning aids comprehension.
3. **Deep plan** -- Multi-agent exploration with a dedicated critique pass. Separate agents analyze existing code, identify affected files, assess risks and dependencies, and review the plan for missing steps. Suitable for high-blast-radius changes.

The planning output is presented to the human for review, inline commenting, and approval before execution begins. Execution can occur in the original context or a fresh one, preserving context isolation.

**Key mechanisms:**
- A blast-radius heuristic selects the appropriate mode (but the user can override).
- Plans are discardable -- rejecting a plan does not pollute the execution context.
- The critique pass in deep mode acts as a verify-before-build gate within the planning phase itself.

## Consequences

**Positive:**
- Right-sized planning reduces wasted effort on simple tasks and missed risks on complex ones.
- Context isolation means failed or rejected plans leave no residue in the execution window.
- The multi-agent critique pass in deep mode catches dependency and ordering errors that single-agent planning misses.
- Cloud offloading is measurably faster (2x in benchmarks) than local planning.

**Negative:**
- Cloud dependency introduces a connectivity requirement and potential privacy concerns for sensitive codebases.
- Server-controlled mode selection may not match user intent (simple tasks get deep plans, complex tasks get simple plans).
- The pattern adds infrastructure complexity -- three modes to maintain, test, and evolve.
- Users may over-rely on deep planning for tasks where quick local reasoning would suffice.

## Known Uses

- **Claude Code Ultra Plan** -- Production implementation with three server-selected modes (simple, visual, deep). Deep mode uses multi-agent architecture with code analysis, file identification, risk detection, and plan review agents. Demonstrated by Ray Amjad with inline commenting and local-to-cloud refinement workflows.
- **GSD plan-phase** -- Local planning with research and verification sub-phases, implementing a two-mode (research + plan) approach without cloud offloading.

## Contract

### Preconditions
- The agent has access to a planning service that supports multiple planning strategies.
- Task complexity can be assessed (via heuristic or user input) before planning begins.
- The execution context is separate from the planning context.

### Invariants
- Planning output is always reviewed by a human before execution begins.
- The planning context is isolated from the execution context -- rejected plans leave no residue.
- Mode selection rationale is logged so users can understand and override the choice.

### Governance
- Plan selection criteria are explicit, auditable, and overridable by the user.
- Plan artifacts are versioned so iterations can be compared.
- Privacy policy for cloud-offloaded planning is documented and enforced.

### Recovery
- If cloud planning is unavailable, fall back to local planning mode with degraded but functional capability.
- If the wrong plan mode is selected (too shallow or too deep), the plan can be discarded and re-planned without cost to the execution context.
- If the critique pass in deep mode identifies blocking issues, the plan is revised before presentation to the user -- not silently accepted.
