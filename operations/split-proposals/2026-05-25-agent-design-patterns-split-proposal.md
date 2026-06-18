---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-05-25"
source_guide: "agent-design-patterns"
finding_count: 37
practitioner_question_count: 2
session: 99
dd102_note: "Moot — emitted under DD-98 threshold (25); DD-102 raised threshold to 45. G10 at 37 would not trigger. Codifier also recommended defer."
sl: "session-99-codifier-finish-batch2-and-harvest-rulings"
---

# Split Proposal: Agent Design Patterns (G10)

## Source guide identity

- **Title:** Agent Design Patterns
- **Current finding count:** 37
- **Routing-table row:** G10, primary dimension: Agent Design, practitioner question: "How do I design an individual agent's identity, prompts, and behavior?"

## Practitioner-question analysis

The source cluster covers 2 distinct practitioner questions:

**Q1: "How do I design a single agent's internal architecture — identity, prompts, capabilities, and tools?"**

This question covers: agent constitution and identity design, five-layer prompt architecture, pre-compression identity pinning, clarification behavior calibration, tool-vs-capability classification, model slot configuration, runtime extension governance, agent-aware API surface design, operating surface specification, subagent isolation contracts, skill inheritance, description-based dispatch, built-in sub-agent triad, specialized parallel roles, three-question protocol framework, NL-to-agent-spec creation loop.

Findings clustering against Q1 (static architecture and design):
- soul-md-agent-constitution-pattern
- five-layer-agent-prompt-architecture
- pre-compression-identity-pinning
- agent-clarification-over-assumption-pattern
- two-layer-plugin-model-tools-vs-capabilities
- auxiliary-model-slot-architecture
- runtime-self-modification-via-extension-api
- core-specialized-skill-inheritance-pattern
- agent-aware-api-surface-design
- operating-surface-underspecification-anti-pattern
- three-question-protocol-selection-framework
- subagent-isolation-contract
- specialized-parallel-agent-roles
- built-in-sub-agent-triad-explore-plan-general
- agent-description-auto-dispatch-routing
- nl-description-to-agent-spec-creation-loop
- tacit-knowledge-as-agent-delegation-barrier

**Q2: "How do I keep my agent reliable, improving, and production-ready across its operational lifecycle?"**

This question covers: lifecycle formalization, pilot-to-production hardening, harness simplification over model generations, incremental session execution, planning-vs-implementation session separation, work disavowal mitigation, anti-slop reliability standards, error recovery in novel environments, environmental feedback loops, state machine monitoring, self-improvement patterns, execution context mode switching, initializer scaffolding, role-voting for autonomous decisions, descent-into-madness avoidance.

Findings clustering against Q2 (runtime lifecycle and operational reliability):
- agent-lifecycle-formalization-spectrum
- agentic-infrastructure-pilot-to-production
- harness-simplification-as-models-improve
- incremental-one-feature-per-session-pattern
- planning-session-bias-separate-context-windows
- work-disavowal-failure-mode-context-limit-cheating
- anti-slop-reliability-standard-first-try-quality
- finite-training-generalization-via-error-recovery
- ground-truth-environmental-feedback-loops
- agent-state-machine-with-witness-monitoring
- gsd-execution-context-profiles-mode-switching
- initializer-agent-scaffolding-pattern
- role-voting-for-autonomous-design-decisions
- self-improving-skill-lessons-log
- skill-self-improvement-three-approaches
- self-improving-agent-prompt-tool-diagnosis
- ai-developer-descent-into-madness-anti-pattern

Shared findings (straddle both questions):
- critic-verifier-loop-with-termination (design pattern AND operational reliability)
- emergent-agentic-behaviors-from-outcome-rl (design implications AND runtime behavior)
- conway-always-on-persistent-agent (architecture AND lifecycle)

## Proposed bifurcation

Destination guide names (working draft):

- **Destination A:** `agent-internal-design` -- practitioner question: "How do I design a single agent's internal architecture -- identity, prompts, capabilities, and tools?"
- **Destination B:** `agent-operational-lifecycle` -- practitioner question: "How do I keep my agent reliable, improving, and production-ready across its operational lifecycle?"

Per-finding routing table:

| Finding | Disposition |
|---------|-------------|
| soul-md-agent-constitution-pattern | A |
| five-layer-agent-prompt-architecture | A |
| pre-compression-identity-pinning | A |
| agent-clarification-over-assumption-pattern | A |
| two-layer-plugin-model-tools-vs-capabilities | A |
| auxiliary-model-slot-architecture | A |
| runtime-self-modification-via-extension-api | A |
| core-specialized-skill-inheritance-pattern | A |
| agent-aware-api-surface-design | A |
| operating-surface-underspecification-anti-pattern | A |
| three-question-protocol-selection-framework | A |
| subagent-isolation-contract | A |
| specialized-parallel-agent-roles | A |
| built-in-sub-agent-triad-explore-plan-general | A |
| agent-description-auto-dispatch-routing | A |
| nl-description-to-agent-spec-creation-loop | A |
| tacit-knowledge-as-agent-delegation-barrier | A |
| agent-lifecycle-formalization-spectrum | B |
| agentic-infrastructure-pilot-to-production | B |
| harness-simplification-as-models-improve | B |
| incremental-one-feature-per-session-pattern | B |
| planning-session-bias-separate-context-windows | B |
| work-disavowal-failure-mode-context-limit-cheating | B |
| anti-slop-reliability-standard-first-try-quality | B |
| finite-training-generalization-via-error-recovery | B |
| ground-truth-environmental-feedback-loops | B |
| agent-state-machine-with-witness-monitoring | B |
| gsd-execution-context-profiles-mode-switching | B |
| initializer-agent-scaffolding-pattern | B |
| role-voting-for-autonomous-design-decisions | B |
| self-improving-skill-lessons-log | B |
| skill-self-improvement-three-approaches | B |
| self-improving-agent-prompt-tool-diagnosis | B |
| ai-developer-descent-into-madness-anti-pattern | B |
| critic-verifier-loop-with-termination | shared (route to both) |
| emergent-agentic-behaviors-from-outcome-rl | shared (route to both) |
| conway-always-on-persistent-agent | shared (route to both) |

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture.

## Routing-table impact

- **Source guide:** proposed deprecation (`stage: deprecated`) post-split.
- **New rows:**
  - `agent-internal-design` -- "How do I design a single agent's internal architecture?", dimensions: Agent Design (primary), lifecycle stage = `draft`.
  - `agent-operational-lifecycle` -- "How do I keep my agent reliable, improving, and production-ready?", dimensions: Agent Design (primary), lifecycle stage = `draft`.
- **Dimension -> Guide mapping changes:** Agent Design primary would need to list both new guides as co-primaries, or use sub-dimension routing (internal architecture vs operational lifecycle).

## Codifier recommendation

**Recommendation:** defer pending more findings

**Rationale:** The bifurcation is structurally sound -- only 3 of 37 findings (8%) route as shared, well below the 15% concern threshold. However, two factors argue for deferral:

1. **Sequential reader journey.** The current guide's procedure flows naturally from design (Steps 1-6) to production readiness (Steps 7-10). A practitioner designing a new agent reads both halves in sequence. Splitting would fragment this flow without a clear gain.

2. **Q2 guide overlap with existing guides.** Several Q2 topics already have natural homes: session management patterns overlap G7 (Session Persistence and Memory), evaluation patterns overlap G4 (Building Agent Evaluation Suites), and production hardening overlaps G6 (Agent Governance and Trust). Splitting G10 would create a new guide whose content partially duplicates or borders these existing guides.

3. **Volume distribution.** Q1 gets 17 findings, Q2 gets 17 findings, 3 shared. Both halves would be moderate-sized guides (~20 findings each) but neither is oversized. The current 37-finding guide is manageable with good structural organization.

Monitor on next regen. If the finding count approaches 45+ with the same bifurcation pattern, revisit.
