---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-19"
source_guide: "agent-architecture-decisions"
finding_count: 72
practitioner_question_count: 2
session: 152
sl: "session-152"
---

# Split Proposal — Agent Architecture Decisions

## Source guide identity

- **Guide stem:** `agent-architecture-decisions`
- **Current title:** "Agent Architecture Decisions"
- **Finding count:** 72 (post-resolution; ≥25)
- **Routing-table row:** G3 in `operations/references/guide-routing-table.md` (dimensions: Orchestration, Model Selection)

## Practitioner-question analysis

The source cluster covers two distinct practitioner questions that have grown far enough apart to read as separate playbooks:

1. **Q1 (topology & composition):** "One agent or many, and how do they coordinate?" — the single-agent default, legitimate multi-agent domains, escalation ladder, composition patterns A–J and the six micro-patterns, the five-pattern communication axis, execution topology, boundary contracts (work-ticket, handoff schema, validation contract), protocol stack (MCP/A2A/AGUI), and the human-in-the-loop role progression.
2. **Q2 (harness engineering & determinism):** "How much scaffolding should I build, and how deterministic?" — the prompt/generic/specialized harness spectrum, the six harness dimensions, the enforcement-locus consensus, specialized-harness primitives, the three-tier orchestration hierarchy, infrastructure-longevity and lock-in assessment, the infrastructure-tier stack, model-tier/routing economics, and the prompt→context→harness evolution.

This bifurcation is **de-facto already present** in the guide's structure: Steps 1–4 + the pattern library answer Q1; Steps 6–8 answer Q2. Step 5 (model selection) supports both and also routes secondarily to G8.

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `agent-topology-and-composition` — practitioner question: "One agent or many, and how do they coordinate?"
- **Destination B:** `harness-engineering-and-determinism` — practitioner question: "How much scaffolding should I build, and how deterministic?"

Per-finding routing (every finding routed; `shared` = route to both):

| Finding | Disposition |
|---------|-------------|
| capability-saturation-threshold-45-percent | A |
| l-d-hypothesis-information-loss-across-agent-bound | A |
| legitimate-multi-agent-domains-taxonomy | A |
| specialization-theater-anti-pattern | A |
| task-contract-pattern-schema-first-agent | A |
| advisor-executor-api-pattern | shared |
| worktree-isolation-for-parallel-agent-sessions | A |
| task-specific-model-routing-table-march-2026-bench | B |
| frontier-release-compression-march-2026 | B |
| agent-teams-shared-communication-channel | A |
| deep-plan-multi-agent-exploration-pattern | A |
| agent-sprawl-anti-pattern-microservices-redux | A |
| agent-type-system-six-roles | A |
| google-a2a-protocol-agent-to-agent-interoperabilit | A |
| brain-hands-decoupling-architecture | A |
| bmad-method-v6-multi-agent-sdlc | A |
| gstack-specialist-role-architecture | A |
| agent-architecture-layer-impermanence | B |
| transitional-lock-in-risk-and-shim-assessment | B |
| six-layer-agent-infrastructure-stack | B |
| claude-code-12-agent-primitives | A |
| specialized-harness-engineering-deterministic-rail | B |
| oz-multi-agent-room-model | A |
| agui-human-control-layer-not-ui | A |
| model-tier-routing-expensive-orchestrator-cheap-s | B |
| orchestrated-execution-one-task-per-sub-agent-wit | A |
| superpowers-plugin-spec-driven-sub-agent-orchestra | B |
| autoresearch-loop-autonomous-metric-driven | shared |
| claude-dispatch-native-mobile-to-local-agent-orch | B |
| error-aware-backtracking-as-compound-error-mitigation | A |
| execution-topology-as-runtime-selection | A |
| four-zone-agent-architecture-framework | A |
| gsd-get-shit-done-plugin | B |
| harness-engineering-third-evolution | B |
| parallel-claude-code-instances-per-workspace | A |
| review-triggered-remediation-dispatch | A |
| skill-phase-pipeline-shared-session-orchestrator | shared |
| skills-as-markdown-sop-files-encode-processes | B |
| sub-agent-context-isolation-for-parallel-complex | A |
| subagent-as-uniform-tool-interface | A |
| subagent-exploration-mode-parallel-codebase-mappi | A |
| claude-code-max-plan-subsidy-vs-api-cost-tool | B |
| five-pattern-complexity-escalation-ladder | A |
| four-estimate-agent-routing-test | A |
| effort-scaling-rules-embedded-in-orchestrator | A |
| harness-composition-six-pattern-taxonomy | shared |
| hub-and-spoke-10-agent-ceiling-with-queueing | A |
| three-tier-orchestration-hierarchy-scheduler-worker-framework | B |
| ralph-wiggum-execution-pattern | A |
| loop-node-anatomy-schema-enforced-ralph-primitive | A |
| archon-yaml-defined-harness-workflows | B |
| planner-executor-deterministic-guardrails | B |
| skill-forked-subagent-execution | A |
| file-based-task-locking-parallel-agents | A |
| issue-based-agent-orchestration-replacing-markdown-plans | A |
| database-as-shared-memory-coordination | A |
| work-ticket-contract-prompt-mode-vs-work-mode | A |
| standardized-io-as-infrastructure-scaling-prerequisite | A |
| three-layer-core-agent-protocol-stack | A |
| task-complexity-tiering-quick-campaign-deep-build | A |
| framework-tension-taxonomy-superpowers-gsd-gstack | B |
| gstack-spec-team-parallel-research-agents | A |
| parallel-independent-workflow-execution-at-scale | A |
| per-function-recursive-loop-composition | A |
| meta-agent-prompt-generation-bootstrap-pattern | A |
| five-pattern-multi-agent-communication-taxonomy | A |
| missions-three-role-architecture-serial-targeted-parallelization | A |
| flat-parentless-cross-model-agent-communication | A |
| droid-whispering-per-role-model-assignment | B |
| structured-handoff-schema-self-healing-multi-agent-missions | A |
| pre-code-validation-contracts-dual-blind-validators | A |
| oracle-evaluator-architect-domain-expert-progression | A |

**Bifurcation precision:** ~50 findings route cleanly to A, ~18 to B, 4 shared (≈6% shared, no contested). The split is clean on the routing test; the asymmetry (A remains large at ~54) means A would still be a big guide post-split — B carves off the coherent harness cluster rather than halving the guide.

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture (no `## Nick's Annotations`, no `<!-- PRESERVE -->` regions).

## Routing-table impact

- **Source guide:** proposed deprecation (`stage: deprecated`) post-split, OR retention of A under the existing G3 stem with B carved off — Nick's call.
- **New rows:**
  - `agent-topology-and-composition` — Q1; dimensions Orchestration; stage `draft`.
  - `harness-engineering-and-determinism` — Q2; dimensions Orchestration, Model Selection; stage `draft`.
- **Dimension → Guide mapping changes:** Orchestration's primary would point to A; the "harness engineering" material (currently implicit under G3) gets an explicit home in B — relevant because the E4 harness epic will need a canonical harness-guide target.

## Codifier recommendation

**Recommendation:** `defer pending more findings`

**Rationale:** The bifurcation is clean (~94% cleanly routed, coherent 18-finding harness cluster for B), so this is a *viable* split, not a forced one. But two structural reasons argue for deferral over immediate execution: (1) the **E4 harness epic is imminent** and will formally shape the harness dimension (six-dimension model, enforcement-locus, posture 2→3 materialization) — it may itself determine whether the harness material becomes a standalone guide, a kernel-spec surface, or stays in G3; splitting now risks doing carve-out work E4 will redo or re-home. (2) G3 already spun off **G3b (Agent Workflow and Execution)** for the operate-stage material, so a further build-stage carve-out should be coordinated with E4's structural input rather than executed speculatively this session. The finding mass will keep growing (harness is the active intake theme), so the trigger will re-fire; the right moment to execute is when E4 has ruled on the harness guide's canonical shape.

## Notes

- Step 5 (model selection) is the natural seam-of-ambiguity: it supports both destinations and also routes secondarily to G8 (Model-Resilient Prompt Engineering). If the split proceeds, model-routing findings could alternatively consolidate under G8 rather than duplicating into A and B — a third option for Nick.
- This proposal supersedes nothing; a prior `2026-05-25-agent-architecture-decisions-split-proposal.md` exists (that one preceded the G3b spinoff). Nick reads the latest.
