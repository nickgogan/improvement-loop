---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-16"
source_guide: "building-agentic-systems"
finding_count: 37
practitioner_question_count: 2
session: 147
sl: "session-147 (SL retired as producer per session-138 ruling; git is the session record)"
---

# Split Proposal — Building Agentic Systems

## Source guide identity

- **Guide stem:** `building-agentic-systems`
- **Current title:** "Building Agentic Systems"
- **Finding count:** 37 (post-resolution; ≥25)
- **Routing-table row:** G11 in `operations/references/guide-routing-table.md` (Synthesis Status table)

## Practitioner-question analysis

Through the 2026-05-25 regen (30 findings) the cluster was single-question. The session-147 sweep absorbs 8 new P1/P2 Agentic Systems findings, 6 of which do not answer "how do I build the system" — they answer "how do I make the system I built installable somewhere else": machine-readable system contracts, per-row invariants, receiver-relative tier semantics, an adaptation/install protocol, abstract-then-adapt wiring docs, and the harness-non-portability evidence that motivates all of it.

The source cluster covers 2 distinct practitioner questions:

1. **Q1: "How do I build a personal/team/business agentic system on top of a knowledge store?"**
   Maturity models, viability assessment, substrate choice, SDK/framework infrastructure, ingestion, querying, proactive loops, long-term operations.
   Findings clustering against Q1: [[ai-delegated-knowledge-organization]], [[ai-managed-vault-separate-from-human-vault]], [[ai-shepherding-anti-pattern-manual-workflow-sequencing]], [[claude-code-daily-brief-multi-source-inbox-obsidian]], [[coding-agent-sdk-as-non-coding-agent-foundation]], [[compounding-knowledge-loop-internal-data]], [[context-assembly-cost-as-strategy-blocker]], [[context-infrastructure-seven-level-maturity-model]], [[context-layer-operator-role-and-maintenance-cadence]], [[dr-research-to-skill-gated-pipeline]], [[five-layer-recursive-ai-loop-architecture]], [[five-pillar-agentic-os-framework]], [[implementation-is-strategy-for-agentic-systems]], [[karpathy-llm-knowledge-base-obsidian-rag]], [[learn-plan-act-review-loop-closing-the-knowledge-gap]], [[monitoring-agent-failure-detection-autonomous-repair]], [[morning-routine-skill-active-experiment-check-in]], [[multi-agent-proportional-content-summarization]], [[notebooklm-mcp-claude-code-cited-knowledge-layer]], [[obsidian-as-transparent-frontend-vs-rag-black-box]], [[obsidian-experiment-notes-personal-health-tracking]], [[open-brain-personal-knowledge-store-pattern]], [[org-world-model-three-architecture-patterns]], [[pr-acceptance-rate-harness-multiplier-evidence]], [[progressive-adoption-path-compounding-extensions]], [[project-onboarding-skill-multi-source-ingestion-dashboard]], [[scale-threshold-heuristic-obsidian-vs-rag]], [[scheduled-tasks-for-real-time-context-maintenance]], [[sdk-to-framework-graduation-path]], [[signal-capture-as-byproduct-of-work]], [[time-window-proactive-agent-loop]]

2. **Q2: "How do I make the system I built portable — installable on another harness, hand-off-able, or migratable across model families?"**
   System contracts with wiring rows, per-row invariants, receiver-relative tier semantics, the adaptation/install protocol, abstract-then-adapt wiring canon, harness-coupling economics.
   Findings clustering against Q2: [[harness-non-portability-across-model-families]], [[machine-readable-system-contract-with-wiring-rows]], [[invariant-column-as-contract-field]], [[receiver-relative-tier-semantics]], [[harness-adaptation-protocol-graded-capability-intersection]], [[wiring-canon-abstract-then-adapt-doc-structure]]

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `building-agentic-systems` — practitioner question: "How do I build a personal/team/business agentic system on top of a knowledge store?" (retains current stem)
- **Destination B:** `porting-agentic-systems` — practitioner question: "How do I make the system I built portable across harnesses and model families?"

Per-finding routing (every finding routed; no implicit handling per DD-98 §Rules #4):

| Finding | Disposition |
|---------|-------------|
| All 31 Q1 findings listed above | A |
| [[machine-readable-system-contract-with-wiring-rows]] | B |
| [[invariant-column-as-contract-field]] | B |
| [[receiver-relative-tier-semantics]] | B |
| [[harness-adaptation-protocol-graded-capability-intersection]] | B |
| [[wiring-canon-abstract-then-adapt-doc-structure]] | B |
| [[harness-non-portability-across-model-families]] | shared (route to both — motivates B's contracts; also grounds A's Section 4 model-commitment decision) |

Bifurcation precision: 36/37 route cleanly (97%); 1 shared; 0 contested.

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture (no `## Nick's Annotations`, no `<!-- PRESERVE -->` regions).

## Routing-table impact

- **Source guide:** retains stem as Destination A; finding count drops to 32 (31 + shared).
- **New rows:**
  - `porting-agentic-systems` — practitioner question: portability/install contracts; dimension: Agentic Systems (secondary); lifecycle stage = `draft`.
- **Dimension → Guide mapping changes:** Agentic Systems dimension gains a secondary guide (G11b/G12); trigger keywords `system contract, wiring rows, adaptation protocol, harness portability, install, invariant` route to the new guide.

## Codifier recommendation

**Recommendation:** defer pending more findings

**Rationale:** Bifurcation is clean (97% routed; 1 shared; 0 contested) but Destination B would stand on 6 findings, 5 of them sourced from a single production system (CareerBuddy's wiring-canon corpus) and all discovered 2026-07-12/13. A standalone guide from a young, near-single-source cluster is thin; the new Section 9 of the source guide carries the material adequately until independent corroboration accrues. Re-evaluate at next regen if the portability cluster grows past ~10 findings or gains a second independent source system.

## Notes

The portability cluster is directly on the engine's own restructure-program path (portable governance kernel), so finding inflow is likely: `/repo-analyzer` runs on harness-shipping vendors and further CareerBuddy corpus contributions are both plausible sources. The shared finding (harness-non-portability) should be duplicated, not moved, if the split executes.
