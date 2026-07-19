---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-19"
source_guide: "building-agentic-systems"
finding_count: 39
practitioner_question_count: 2
session: 152
sl: "session-152 (SL retired as producer per session-138 ruling; git is the session record)"
---

# Split Proposal — Building Agentic Systems

## Source guide identity

- **Guide stem:** `building-agentic-systems`
- **Current title:** "Building Agentic Systems"
- **Finding count:** 39 (post-resolution; ≥25)
- **Routing-table row:** G11 in `operations/references/guide-routing-table.md` (Synthesis Status table)

## Practitioner-question analysis

This proposal re-emits the DD-98 conjunction that fired at the 2026-07-16 (session-147) regen — see `operations/split-proposals/2026-07-16-building-agentic-systems-split-proposal.md`. The session-152 refresh added 2 Agentic Systems findings ([[shared-spaces-multiplayer-human-agent-surfaces]], [[agentic-file-classification-reliability-calibration]]), **both of which answer Q1 (build/operate)** — neither touches portability. The bifurcation is therefore structurally identical to the prior proposal, with Q1 grown from 31 to 33 findings and Q2 unchanged at 6.

The source cluster covers 2 distinct practitioner questions:

1. **Q1: "How do I build a personal/team/business agentic system on top of a knowledge store?"**
   Maturity models, viability assessment, substrate choice, SDK/framework infrastructure, ingestion, querying, proactive loops, long-term operations (incl. the new team-scale collaboration-surface and small-taxonomy classification-reliability material).
   Findings clustering against Q1: [[agentic-file-classification-reliability-calibration]], [[ai-delegated-knowledge-organization]], [[ai-managed-vault-separate-from-human-vault]], [[ai-shepherding-anti-pattern-manual-workflow-sequencing]], [[claude-code-daily-brief-multi-source-inbox-obsidian]], [[coding-agent-sdk-as-non-coding-agent-foundation]], [[compounding-knowledge-loop-internal-data]], [[context-assembly-cost-as-strategy-blocker]], [[context-infrastructure-seven-level-maturity-model]], [[context-layer-operator-role-and-maintenance-cadence]], [[dr-research-to-skill-gated-pipeline]], [[five-layer-recursive-ai-loop-architecture]], [[five-pillar-agentic-os-framework]], [[implementation-is-strategy-for-agentic-systems]], [[karpathy-llm-knowledge-base-obsidian-rag]], [[learn-plan-act-review-loop-closing-the-knowledge-gap]], [[monitoring-agent-failure-detection-autonomous-repair]], [[morning-routine-skill-active-experiment-check-in]], [[multi-agent-proportional-content-summarization]], [[notebooklm-mcp-claude-code-cited-knowledge-layer]], [[obsidian-as-transparent-frontend-vs-rag-black-box]], [[obsidian-experiment-notes-personal-health-tracking]], [[open-brain-personal-knowledge-store-pattern]], [[org-world-model-three-architecture-patterns]], [[pr-acceptance-rate-harness-multiplier-evidence]], [[progressive-adoption-path-compounding-extensions]], [[project-onboarding-skill-multi-source-ingestion-dashboard]], [[scale-threshold-heuristic-obsidian-vs-rag]], [[scheduled-tasks-for-real-time-context-maintenance]], [[sdk-to-framework-graduation-path]], [[shared-spaces-multiplayer-human-agent-surfaces]], [[signal-capture-as-byproduct-of-work]], [[time-window-proactive-agent-loop]]

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
| All 32 non-shared Q1 findings listed above | A |
| [[machine-readable-system-contract-with-wiring-rows]] | B |
| [[invariant-column-as-contract-field]] | B |
| [[receiver-relative-tier-semantics]] | B |
| [[harness-adaptation-protocol-graded-capability-intersection]] | B |
| [[wiring-canon-abstract-then-adapt-doc-structure]] | B |
| [[harness-non-portability-across-model-families]] | shared (route to both — motivates B's contracts; also grounds A's Section 4 model-commitment decision) |

Bifurcation precision: 38/39 route cleanly (97%); 1 shared; 0 contested.

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture (no `## Nick's Annotations`, no `<!-- PRESERVE -->` regions).

## Routing-table impact

- **Source guide:** retains stem as Destination A; finding count drops to 34 (33 + shared).
- **New rows:**
  - `porting-agentic-systems` — practitioner question: portability/install contracts; dimension: Agentic Systems (secondary); lifecycle stage = `draft`.
- **Dimension → Guide mapping changes:** Agentic Systems dimension gains a secondary guide (G11b/G12); trigger keywords `system contract, wiring rows, adaptation protocol, harness portability, install, invariant` route to the new guide.

## Codifier recommendation

**Recommendation:** defer pending more findings

**Rationale:** The picture is unchanged from the 2026-07-16 proposal, whose "defer" recommendation set an explicit re-eval condition: revisit *if the portability cluster grows past ~10 findings or gains a second independent source system.* Neither happened. Q2 still stands on the same 6 findings, 5 of them sourced from a single production system (CareerBuddy's wiring-canon corpus), all discovered 2026-07-12/13; the 2 findings added this session are both Q1. A standalone portability guide from a young, near-single-source cluster remains thin, and the source guide's Section 9 continues to carry the material adequately. Bifurcation is clean (97%; 1 shared; 0 contested), so the split is *executable* whenever Nick chooses — the blocker is Q2 maturity, not routing ambiguity.

## Notes

The re-eval trigger stands: execute the split when the portability cluster crosses ~10 findings or gains a second independent source system (e.g., a `/repo-analyzer` pass on another harness-shipping vendor, or further CareerBuddy contributions). The shared finding ([[harness-non-portability-across-model-families]]) should be duplicated, not moved, if the split executes. This is the second identical-shape emission; a third with the same "defer" rationale would be evidence the trigger should be dampened for this guide until the re-eval condition is met, to avoid regen-cycle proposal churn.
