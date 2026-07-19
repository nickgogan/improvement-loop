---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-19"
source_guide: "agent-design-patterns"
finding_count: 47
practitioner_question_count: 2
session: 152
sl: "none (System Log retired as producer, session-138 ruling)"
---

# Split Proposal — Agent Design Patterns

## Source guide identity

- **Guide stem:** `agent-design-patterns`
- **Current title:** "Agent Design Patterns"
- **Finding count:** 47 (post-resolution; ≥25)
- **Routing-table row:** G10 in `operations/references/guide-routing-table.md` (Synthesis Status table)

## Practitioner-question analysis

The source cluster covers 2 distinct practitioner questions, already reflected in the guide's own Part I / Part II split, plus a nascent third micro-theme:

1. **Q1 (specify/build):** "How do I design an individual agent's identity, prompts, behavior, and internal structure?"
   - Constitution, five-layer prompt stack, clarification behavior, tools-vs-capabilities, composition units, subagent isolation, operating surface, model slots, filesystem assembly.
2. **Q2 (operate):** "How do I operate an agent reliably over time and improve it from experience?"
   - Reliability/first-try bar, complexity audits, session boundaries, planning/impl separation, lifecycle state machine, self-improvement mechanisms, autonomous decision-making, provisioning/elicitation.
3. **Emerging micro-theme (org-level, 2 findings):** "Who owns the agent's/AI-product's quality, and what role should they play?" — not cleanly Q1 or Q2 (organizational design, not agent-internal). Flagged contested below.

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `designing-the-agent` — practitioner question: "How do I design an individual agent's identity, prompts, and internal structure?" (stage: specify/build)
- **Destination B:** `operating-and-improving-the-agent` — practitioner question: "How do I operate an agent reliably over time and improve it?" (stage: operate)

Per-finding routing (every finding routed; no implicit handling per DD-98 §Rules #4):

| Finding | Disposition |
|---------|-------------|
| [[agent-as-folder-compiled-to-manifest]] | A |
| [[agent-aware-api-surface-design]] | A |
| [[agent-clarification-over-assumption-pattern]] | A |
| [[agent-description-auto-dispatch-routing]] | A |
| [[auxiliary-model-slot-architecture]] | A |
| [[built-in-sub-agent-triad-explore-plan-general]] | A |
| [[cache-stable-progressive-disclosure-catalog]] | A |
| [[capability-as-agent-composition-primitive]] | A |
| [[capability-composition-declared-ordering-constraints]] | A |
| [[core-specialized-skill-inheritance-pattern]] | A |
| [[critic-verifier-loop-with-termination]] | A |
| [[declarative-agent-spec-with-serialization-registry]] | A |
| [[disclosure-granularity-decision-rubric]] | A |
| [[emergent-agentic-behaviors-from-outcome-rl]] | A |
| [[five-layer-agent-prompt-architecture]] | A |
| [[guardrails-as-hook-lattice-capabilities]] | A |
| [[operating-surface-underspecification-anti-pattern]] | A |
| [[soul-md-agent-constitution-pattern]] | A |
| [[specialized-parallel-agent-roles]] | A |
| [[subagent-isolation-contract]] | A |
| [[three-question-protocol-selection-framework]] | A |
| [[two-layer-plugin-model-tools-vs-capabilities]] | A |
| [[runtime-self-modification-via-extension-api]] | A |
| [[ai-developer-descent-into-madness-anti-pattern]] | A |
| [[pre-compression-identity-pinning]] | shared (identity design ∩ session continuity) |
| [[framework-abstraction-tax-for-agents]] | shared (transparency check ∩ complexity audit) |
| [[finite-training-generalization-via-error-recovery]] | shared (behavior design ∩ reliability) |
| [[agentic-infrastructure-pilot-to-production]] | B |
| [[anti-slop-reliability-standard-first-try-quality]] | B |
| [[agent-lifecycle-formalization-spectrum]] | B |
| [[agent-state-machine-with-witness-monitoring]] | B |
| [[conway-always-on-persistent-agent]] | B |
| [[ground-truth-environmental-feedback-loops]] | B |
| [[gsd-execution-context-profiles-mode-switching]] | B |
| [[harness-simplification-as-models-improve]] | B |
| [[incremental-one-feature-per-session-pattern]] | B |
| [[initializer-agent-scaffolding-pattern]] | B |
| [[nl-description-to-agent-spec-creation-loop]] | B |
| [[planning-session-bias-separate-context-windows]] | B |
| [[role-voting-for-autonomous-design-decisions]] | B |
| [[self-improving-agent-prompt-tool-diagnosis]] | B |
| [[self-improving-skill-lessons-log]] | B |
| [[skill-self-improvement-three-approaches]] | B |
| [[tacit-knowledge-as-agent-delegation-barrier]] | B |
| [[work-disavowal-failure-mode-context-limit-cheating]] | B |
| [[oracle-evaluator-architect-domain-expert-progression]] | contested (org-level ownership; not cleanly A or B) |
| [[principal-domain-expert-single-ownership]] | contested (org-level ownership; not cleanly A or B) |

**Bifurcation precision:** 45/47 route cleanly to a single side or as A/B-shared; 2/47 (~4%) are contested (the emerging domain-expert-ownership micro-theme). Shared+contested = 5/47 (~11%), under the 20% imprecision flag.

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture (no `## Nick's Annotations` section; no `<!-- PRESERVE -->` regions).

## Routing-table impact

- **Source guide:** proposed deprecation (`stage: deprecated`) post-split, mirroring the G2→G2a/G2b precedent.
- **New rows:**
  - `designing-the-agent` — Q1 (specify/build), dimensions: Agent Design, Tool Integration, Orchestration; lifecycle stage = `draft`.
  - `operating-and-improving-the-agent` — Q2 (operate), dimensions: Agent Design, Orchestration; lifecycle stage = `draft`.
- **Dimension → Guide mapping changes:** the "Agent Design → Agent Design Patterns (G10)" row splits into two guide targets; the operate-half overlaps G3b (Agent Workflow and Execution), which already owns the operate stage — see recommendation.

## Codifier recommendation

Closed enum: `proceed with split as proposed` | `defer pending more findings` | `re-evaluate practitioner-question bifurcation` | `absorb into adjacent guide instead`

**Recommendation:** defer pending more findings

**Rationale:** The Part I / Part II boundary is real and routes cleanly (~89% clean, 11% shared/contested), but three signals argue against splitting now: (1) A and B are densely cross-linked (identity↔continuity, composition↔self-improvement, framework-tax spans both), so a split would multiply the shared-finding and cross-reference maintenance; (2) the operate-half (Destination B) overlaps G3b (Agent Workflow and Execution, also `operate` stage) — the right move for B may be absorption into G3b rather than a new guide, which a bare split would foreclose; (3) a distinct third micro-theme (domain-expert quality ownership) is emerging at only 2 findings and is not cleanly A or B — better to let it accrete and decide its home alongside the split, not before it. Defer until the operate-half's G3b-vs-new-guide question is settled and the ownership theme crosses the graduation threshold.

## Notes

- The guide's own two-part structure (Part I: Agent Internal Design; Part II: Agent Operational Lifecycle) is the natural seam and would make an eventual split low-friction.
- The domain-expert-ownership pair also serves G3 (oracle is `consumed_by` agent-architecture-decisions.md) and is org-level; if it graduates, its home may be G3/G11 rather than either half of a G10 split.
