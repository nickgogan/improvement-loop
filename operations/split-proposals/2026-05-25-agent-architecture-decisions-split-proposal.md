---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-05-25"
source_guide: "agent-architecture-decisions"
finding_count: 42
practitioner_question_count: 2
session: 97
sl: "session-97-codifier-guide-resynthesis"
---

## Practitioner-question analysis

The source cluster covers 2 distinct practitioner questions:

**Q1: "How do I choose and design my agent system topology?"**
This question covers: single-agent-vs-multi decision, the 45% saturation threshold, task characteristic evaluation, composition pattern selection (Patterns A-F), boundary contracts, agent type enforcement, room-based coordination, human control points (AGUI), and inter-protocol coordination (A2A/MCP/AGUI).

Findings clustering against Q1 (topology/composition):
- capability-saturation-threshold-45-percent
- l-d-hypothesis-information-loss-across-agent-bound
- legitimate-multi-agent-domains-taxonomy
- specialization-theater-anti-pattern
- task-contract-pattern-schema-first-agent
- advisor-executor-api-pattern
- worktree-isolation-for-parallel-agent-sessions
- agent-teams-shared-communication-channel
- deep-plan-multi-agent-exploration-pattern
- agent-sprawl-anti-pattern-microservices-redux
- agent-type-system-six-roles
- google-a2a-protocol-agent-to-agent-interoperabilit
- brain-hands-decoupling-architecture
- bmad-method-v6-multi-agent-sdlc
- gstack-specialist-role-architecture
- oz-multi-agent-room-model
- agui-human-control-layer-not-ui
- four-zone-agent-architecture-framework
- parallel-claude-code-instances-per-workspace
- subagent-exploration-mode-parallel-codebase-mappi

**Q2: "How do I wire, power, and future-proof my agent infrastructure?"**
This question covers: model routing and cost economics, infrastructure layer assessment, layer impermanence and lock-in, harness spectrum positioning (prompt-driven/generic/specialized), sub-agent dispatch mechanics, skill-as-SOP encoding, execution topology selection, and autonomous execution loops.

Findings clustering against Q2 (infrastructure/orchestration):
- task-specific-model-routing-table-march-2026-bench
- frontier-release-compression-march-2026
- six-layer-agent-infrastructure-stack
- agent-architecture-layer-impermanence
- transitional-lock-in-risk-and-shim-assessment
- claude-code-12-agent-primitives
- specialized-harness-engineering-deterministic-rail
- model-tier-routing-expensive-orchestrator-cheap-s
- harness-engineering-third-evolution
- claude-code-max-plan-subsidy-vs-api-cost-tool
- gsd-get-shit-done-plugin
- autoresearch-loop-autonomous-metric-driven
- skills-as-markdown-sop-files-encode-processes
- claude-dispatch-native-mobile-to-local-agent-orch
- error-aware-backtracking-as-compound-error-mitigation

Shared findings (route to both -- they straddle topology and infrastructure):
- orchestrated-execution-one-task-per-sub-agent-wit
- superpowers-plugin-spec-driven-sub-agent-orchestra
- execution-topology-as-runtime-selection
- sub-agent-context-isolation-for-parallel-complex
- subagent-as-uniform-tool-interface
- review-triggered-remediation-dispatch
- skill-phase-pipeline-shared-session-orchestrator

## Proposed bifurcation

Destination guide names (working draft):

- **Destination A:** `agent-topology-and-composition` -- practitioner question: "How do I choose and design my agent system topology?"
- **Destination B:** `agent-infrastructure-and-orchestration` -- practitioner question: "How do I wire, power, and future-proof my agent infrastructure?"

Per-finding routing table -- list ALL 42 findings:

| Finding | Disposition |
|---------|-------------|
| capability-saturation-threshold-45-percent | A |
| l-d-hypothesis-information-loss-across-agent-bound | A |
| legitimate-multi-agent-domains-taxonomy | A |
| specialization-theater-anti-pattern | A |
| task-contract-pattern-schema-first-agent | A |
| advisor-executor-api-pattern | A |
| worktree-isolation-for-parallel-agent-sessions | A |
| agent-teams-shared-communication-channel | A |
| deep-plan-multi-agent-exploration-pattern | A |
| agent-sprawl-anti-pattern-microservices-redux | A |
| agent-type-system-six-roles | A |
| google-a2a-protocol-agent-to-agent-interoperabilit | A |
| brain-hands-decoupling-architecture | A |
| bmad-method-v6-multi-agent-sdlc | A |
| gstack-specialist-role-architecture | A |
| oz-multi-agent-room-model | A |
| agui-human-control-layer-not-ui | A |
| four-zone-agent-architecture-framework | A |
| parallel-claude-code-instances-per-workspace | A |
| subagent-exploration-mode-parallel-codebase-mappi | A |
| task-specific-model-routing-table-march-2026-bench | B |
| frontier-release-compression-march-2026 | B |
| six-layer-agent-infrastructure-stack | B |
| agent-architecture-layer-impermanence | B |
| transitional-lock-in-risk-and-shim-assessment | B |
| claude-code-12-agent-primitives | B |
| specialized-harness-engineering-deterministic-rail | B |
| model-tier-routing-expensive-orchestrator-cheap-s | B |
| harness-engineering-third-evolution | B |
| claude-code-max-plan-subsidy-vs-api-cost-tool | B |
| gsd-get-shit-done-plugin | B |
| autoresearch-loop-autonomous-metric-driven | B |
| skills-as-markdown-sop-files-encode-processes | B |
| claude-dispatch-native-mobile-to-local-agent-orch | B |
| error-aware-backtracking-as-compound-error-mitigation | B |
| orchestrated-execution-one-task-per-sub-agent-wit | shared (route to both) |
| superpowers-plugin-spec-driven-sub-agent-orchestra | shared (route to both) |
| execution-topology-as-runtime-selection | shared (route to both) |
| sub-agent-context-isolation-for-parallel-complex | shared (route to both) |
| subagent-as-uniform-tool-interface | shared (route to both) |
| review-triggered-remediation-dispatch | shared (route to both) |
| skill-phase-pipeline-shared-session-orchestrator | shared (route to both) |

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture.

## Routing-table impact

- **Source guide:** proposed deprecation (`stage: deprecated`) post-split.
- **New rows:**
  - `agent-topology-and-composition` -- "How do I choose and design my agent system topology?", dimensions: Orchestration (primary), lifecycle stage = `draft`.
  - `agent-infrastructure-and-orchestration` -- "How do I wire, power, and future-proof my agent infrastructure?", dimensions: Orchestration (primary), Model Selection (secondary), lifecycle stage = `draft`.
- **Dimension -> Guide mapping changes:** Orchestration primary would need to list both new guides as co-primaries, or route by sub-dimension.

## Codifier recommendation

**Recommendation:** re-evaluate practitioner-question bifurcation

**Rationale:** 7 of 42 findings (17%) route as shared -- above the 15% clean-bifurcation threshold but below the 20% concern threshold. The bigger concern: the reader journey is sequential (decide topology THEN implement infrastructure). Splitting may fragment a natural workflow. The current guide's Steps 1-4 -> 5-8 structure already handles the two questions as a coherent procedure. Defer until the finding count grows further or the two halves develop genuinely independent readerships.

## Notes

The existing G3b (Agent Workflow and Execution) already handles the "how do I run agents in production?" question. A G3->G3c split for infrastructure/orchestration would create a three-guide Orchestration dimension family (G3a topology, G3b workflow/execution, G3c infrastructure/harness) which may be over-decomposed for the current KB size. Monitor on next regen.

## Resolution

**Decision:** deferred — session 104 (2026-05-25)
**Rationale:** At 42 findings, below DD-102 threshold (45). Codifier recommended deferral citing sequential reader journey (decide topology → wire infrastructure) and risk of over-decomposing the Orchestration dimension into a 3-guide family. Nick concurred. Re-evaluate if finding count crosses 45 on a future regen.
