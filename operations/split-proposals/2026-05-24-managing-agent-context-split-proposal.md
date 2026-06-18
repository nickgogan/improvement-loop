---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-05-24"
source_guide: "managing-agent-context"
finding_count: 48
practitioner_question_count: 3
session: 93
sl: "session-93-codifier-synthesize-guides"
---

# Split Proposal — Managing Agent Context

## Source guide identity

- **Guide stem:** `managing-agent-context`
- **Current title:** "Managing Agent Context"
- **Finding count:** 48 (post-resolution; ≥25)
- **Routing-table row:** G2 in `operations/references/guide-routing-table.md`

## Practitioner-question analysis

Reading the guide's 48 findings reveals three distinct practitioner questions. Each maps to a coherent cluster of findings with its own arc, its own step sequence, and its own template set. Mixing them into one guide creates a document that is too long to navigate quickly and crosses two conceptually independent problems.

The three clusters:

1. **Q1:** "How do I structure and load context efficiently — what to include, how to tier it, and how to retrieve it?"
   - Core concern: signal vs. noise, tiered loading, selective retrieval, pointers over copies, progressive skill loading, self-describing codebases.
   - Findings: [[ace-agentic-context-engineering-evolving-playbook]], [[agent-context-kiss-commandments-minimum-viable]], [[context-curation-over-context-stuffing]], [[context-enrichment-for-task-clarity]], [[context-file-instruction-bloat-eth-zurich]], [[document-sharding-for-context-efficiency]], [[fundamental-limits-of-single-vector-embedding-retr]], [[hybrid-upfront-and-jit-context-architecture]], [[index-file-navigation-as-rag-replacement]], [[claudemd-as-knowledge-base-traversal-guide]], [[model-specific-context-file-sensitivity]], [[one-shot-prd-prompt-for-system-bootstrap]], [[tiered-context-injection-over-monolithic-files]], [[notebooklm-as-external-knowledge-base-for-context]], [[pointers-over-copies-in-context-files]], [[five-context-management-techniques-in-claude-code]], [[progressive-tiered-context-loading-convergence]], [[context-file-taxonomy-claudemd-soulmd-agentsmd]], [[progressive-skill-loading]], [[self-describing-codebase-structural-semantic-context]], [[three-tier-progressive-context-loading]], [[skills-as-pointers-to-second-brain-files]], [[write-time-vs-query-time-synthesis-kb-poisoning]], [[agentic-search-memory-retrieval-architecture]]

2. **Q2:** "How do I prevent context degradation, rot, and cost blowout — keeping quality high across long sessions and multi-step workflows?"
   - Core concern: context rot defense, dynamic tool pools, compaction avoidance, session scoping, cost measurement, trajectory engineering, window-headroom awareness.
   - Findings: [[context-rot-attention-budget-depletion]], [[context-rot-silent-killer-and-mitigations]], [[dynamic-tool-pool-assembly-transcript-compaction]], [[response-format-enum-for-adaptive-verbosity]], [[reasoning-token-overhead-from-context-files]], [[ide-context-streaming-silent-token-tax]], [[new-chat-per-agent-step-context-hygiene]], [[prompt-caching-for-stable-agent-context]], [[scrum-master-story-contextualization]], [[gsd-global-learnings-store-cross-session-persistence]], [[catastrophic-context-collapse-risk-during-claudemd]], [[claudemd-context-rot-from-indiscriminate-rule-accu]], [[model-native-context-window-awareness]], [[session-atomicity-single-issue-scope-quadratic-cost-reduction]], [[trajectory-engineering-non-linear-session-forking]], [[ace-delta-updates-over-monolithic-rewrites]], [[session-tree-as-first-class-abstraction]], [[orchestrator-headless-dispatch-context-isolation]], [[bounded-tiered-memory-inference-driven-curation]]

3. **Q3:** "How do I architect context across sessions, tools, tiers, and teams — making context decisions that hold at the workspace and system level?"
   - Core concern: vault architecture, cross-platform portability, monorepo distribution, session bridges, skill scoping, folder-as-workspace architecture, memory architecture cross-over.
   - Findings: [[global-vs-project-level-skill-and-context]], [[monorepo-context-distribution-three-strategies]], [[three-layer-folder-as-workspace-architecture]], [[three-tier-vault-architecture-global-shared-local]], [[cross-platform-context-file-strategy]], [[progress-md-session-bridge]], [[self-describing-codebase-structural-semantic-context]] (shared), [[agent-memory-architecture-multi-agent-layered]], [[agentic-search-memory-retrieval-architecture]] (shared)

Note: `self-describing-codebase-structural-semantic-context` is contested — it has structural loading implications (Q1) AND workspace-architecture implications (Q3). Routed to Q1 as the primary value is per-call codebase legibility. `agentic-search-memory-retrieval-architecture` is contested — retrieval architecture spans Q1 (retrieval patterns) and Q3 (persistent memory). See per-finding table below.

## Proposed bifurcation

The three-way analysis argues for bifurcation (not trifurcation) at this stage: Q3 (cross-session/workspace architecture) is growing but thin as a standalone guide — only ~7 unshared findings. Recommended approach: bifurcate Q1 and Q2 now; fold Q3 into the G7 (Session Persistence and Memory) expansion or stage it as a future G2c only when the finding count for pure-architecture findings reaches ≥15.

- **Destination A:** `structuring-agent-context` — "Structuring and Loading Agent Context" (Q1: what to include, how to tier, how to retrieve)
- **Destination B:** `defending-agent-context` — "Defending Against Context Degradation" (Q2: rot prevention, cost control, session discipline)

Q3 findings (cross-session/workspace architecture) that do not fit neatly into A or B are routed to B as "session and workspace architecture" is a natural home in the degradation-prevention discipline — architecture decisions that prevent degradation before it starts.

Per-finding routing (all 48 findings):

| Finding | Disposition |
|---------|-------------|
| [[ace-agentic-context-engineering-evolving-playbook]] | A |
| [[ace-delta-updates-over-monolithic-rewrites]] | B |
| [[agent-context-kiss-commandments-minimum-viable]] | A |
| [[context-curation-over-context-stuffing]] | A |
| [[context-enrichment-for-task-clarity]] | A |
| [[context-file-instruction-bloat-eth-zurich]] | A |
| [[context-rot-attention-budget-depletion]] | B |
| [[context-rot-silent-killer-and-mitigations]] | B |
| [[document-sharding-for-context-efficiency]] | A |
| [[fundamental-limits-of-single-vector-embedding-retr]] | A |
| [[hybrid-upfront-and-jit-context-architecture]] | A |
| [[prompt-caching-for-stable-agent-context]] | B |
| [[scrum-master-story-contextualization]] | A |
| [[dynamic-tool-pool-assembly-transcript-compaction]] | B |
| [[response-format-enum-for-adaptive-verbosity]] | B |
| [[reasoning-token-overhead-from-context-files]] | B |
| [[ide-context-streaming-silent-token-tax]] | B |
| [[index-file-navigation-as-rag-replacement]] | A |
| [[new-chat-per-agent-step-context-hygiene]] | B |
| [[claudemd-as-knowledge-base-traversal-guide]] | A |
| [[model-specific-context-file-sensitivity]] | A |
| [[one-shot-prd-prompt-for-system-bootstrap]] | A |
| [[tiered-context-injection-over-monolithic-files]] | A |
| [[notebooklm-as-external-knowledge-base-for-context]] | A |
| [[pointers-over-copies-in-context-files]] | A |
| [[gsd-global-learnings-store-cross-session-persistence]] | B |
| [[five-context-management-techniques-in-claude-code]] | B |
| [[progressive-tiered-context-loading-convergence]] | A |
| [[catastrophic-context-collapse-risk-during-claudemd]] | B |
| [[claudemd-context-rot-from-indiscriminate-rule-accu]] | B |
| [[context-file-taxonomy-claudemd-soulmd-agentsmd]] | A |
| [[cross-platform-context-file-strategy]] | B |
| [[global-vs-project-level-skill-and-context]] | B |
| [[model-native-context-window-awareness]] | B |
| [[monorepo-context-distribution-three-strategies]] | B |
| [[progressive-skill-loading]] | A |
| [[self-describing-codebase-structural-semantic-context]] | A (contested; B is secondary home) |
| [[session-atomicity-single-issue-scope-quadratic-cost-reduction]] | B |
| [[three-layer-folder-as-workspace-architecture]] | B |
| [[three-tier-progressive-context-loading]] | A |
| [[three-tier-vault-architecture-global-shared-local]] | B |
| [[progress-md-session-bridge]] | B |
| [[skills-as-pointers-to-second-brain-files]] | A |
| [[trajectory-engineering-non-linear-session-forking]] | B |
| [[bounded-tiered-memory-inference-driven-curation]] | shared (primary A; memory architecture aspect → B) |
| [[session-tree-as-first-class-abstraction]] | B |
| [[write-time-vs-query-time-synthesis-kb-poisoning]] | A |
| [[orchestrator-headless-dispatch-context-isolation]] | B |

Routing tally (at proposal time, 48 findings): A = 21, B = 25, shared = 1 (bounded-tiered-memory-inference-driven-curation). Shared finding content to be split by section in both destination guides.

**Updated routing (session 104, 64 findings):** 16 findings added since proposal. New routing: A += claude-code-context-management-decision-matrix-five-tools, inline-scoped-mcp-servers-per-subagent, agentic-rag-multi-strategy-retrieval-2026, file-search-outperforms-rag-for-small-corpora, hybrid-retrieval-pattern-semantic-lexical-graph, summary-gate-agent-traversal-pattern, personal-knowledge-hoard-as-agent-substrate, ai-as-primary-reader-design-principle, environment-grounded-context-as-output-quality-multiplier, agent-memory-architecture-multi-agent-layered, interactive-explanations-extend-linear-walkthroughs. B += proactive-compaction-before-intelligence-degradation, token-economics-as-architecture-driver, html-output-as-human-in-the-loop-restorer, format-constrained-improvisation-tax, output-format-token-cost-reframed-by-context-window-size. Final tally: A = 34, B = 29, shared = 1.

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture.

## Routing-table impact

- **Source guide:** proposed deprecation post-split; redirect row to point at A + B
- **New rows:**
  - `structuring-agent-context` — G2a — "Structuring and Loading Agent Context" — ~22 findings — draft
  - `defending-agent-context` — G2b — "Defending Against Context Degradation" — ~26 findings — draft
- **Dimension mapping changes:** G2 currently maps to "Context Engineering" category. Both destinations inherit the same category. G2a leans toward "Context Architecture / Loading" sub-dimension; G2b leans toward "Context Rot / Cost / Session Discipline" sub-dimension.

## Codifier recommendation

**Recommendation:** `proceed with split as proposed`

**Rationale:** Both DD-98 triggers are met (48 findings ≥ 25; 3 distinct practitioner questions identified, with 2 large enough for standalone guides now). The resulting guides (22 and 26 findings) will each be below the 25-finding split trigger, meaning they will be stable for several research cycles. The shared finding (`bounded-tiered-memory-inference-driven-curation`) is the only contested routing; its memory-architecture aspect can be noted with a cross-reference rather than full duplication. Q3 (workspace architecture) is intentionally folded into B rather than staged as a third guide — the finding count is too thin for a standalone guide and the practitioner question ("how do I architect at the workspace level?") is most naturally answered in the rot-prevention context (architecture decisions that *prevent* degradation are architectural countermeasures).

## Notes

- The split requires updating the guide routing table (`operations/references/guide-routing-table.md`) to add G2a and G2b rows and mark G2 deprecated.
- Templates are unevenly distributed: the Context Budget Worksheet, Context Audit Checklist, and Context File Template all belong to A; the Delta Update Entry, Sub-Agent Context Package, Module Manifest, and Multi-Tool Context Mirror Map straddle A and B. On split, recommend: Delta Update Entry → B; Sub-Agent Context Package → A; Module Manifest → A; Multi-Tool Context Mirror Map → B.
- The `bounded-tiered-memory-inference-driven-curation` finding introduces memory-tier content that partially overlaps with G7 (Session Persistence and Memory). Its loading/curation aspect belongs in A; its persistence/eviction aspect belongs in G7. The finding's primary home remains G2 (context management); the G7 cross-reference should be strengthened.

## Resolution

**Decision:** proceed with split — session 104 (2026-05-25)
**Rationale:** At 64 findings (above DD-102 threshold of 45), Codifier recommended proceeding. Two distinct practitioner questions confirmed. Nick approved. G2 deprecated; replaced by G2a (`structuring-agent-context`, 34 findings) and G2b (`defending-agent-context`, 29 findings), plus 1 shared finding in both.
