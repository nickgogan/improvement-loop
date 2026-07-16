---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-16"
source_guide: "structuring-agent-context"
finding_count: 61
practitioner_question_count: 2
session: 147
sl: null
---

# Split Proposal — Structuring and Loading Agent Context (G2a)

## Source guide identity

- **Guide stem:** `structuring-agent-context`
- **Current title:** "Structuring and Loading Agent Context"
- **Finding count:** 61 (post-resolution; ≥25 — 2.4× the DD-98 threshold, and back at the mass that triggered the original G2 split at 64)
- **Routing-table row:** G2a in `operations/references/guide-routing-table.md` (Synthesis Status + Active Clusters tables)

## Practitioner-question analysis

The source cluster covers 2 distinct practitioner questions:

1. **Q1:** "How do I decide what goes into my agent's context files and how it gets loaded — entry files, tiers, skills, sub-agent packages?"
   - Findings clustering against Q1: [[ace-agentic-context-engineering-evolving-playbook]], [[agent-context-kiss-commandments-minimum-viable]], [[context-curation-over-context-stuffing]], [[context-enrichment-for-task-clarity]], [[context-file-instruction-bloat-eth-zurich]], [[document-sharding-for-context-efficiency]], [[scrum-master-story-contextualization]], [[model-specific-context-file-sensitivity]], [[one-shot-prd-prompt-for-system-bootstrap]], [[tiered-context-injection-over-monolithic-files]], [[pointers-over-copies-in-context-files]], [[progressive-tiered-context-loading-convergence]], [[context-file-taxonomy-claudemd-soulmd-agentsmd]], [[progressive-skill-loading]], [[three-tier-progressive-context-loading]], [[skills-as-pointers-to-second-brain-files]], [[bounded-tiered-memory-inference-driven-curation]], [[claude-code-context-management-decision-matrix-five-tools]], [[inline-scoped-mcp-servers-per-subagent]], [[environment-grounded-context-as-output-quality-multiplier]], [[agent-memory-architecture-multi-agent-layered]], [[interactive-explanations-extend-linear-walkthroughs]], [[always-on-context-minimalism-pointer-only-entry]], [[task-to-file-routing-table-in-context-files]], [[cold-start-chain-and-cold-start-test]], [[docs-split-by-lifespan-not-topic]], [[skill-as-directory-progressive-disclosure-three-levels]], [[skill-content-lifecycle-context-budget]], [[skill-description-budget-context-overflow]], [[skill-dynamic-context-injection-shell-prerender]], [[hub-and-spoke-two-tier-skill-taxonomy]], [[branch-analysis-externalization-rule-skill-reference]], [[shared-context-folder-as-cross-skill-update-multiplier]], [[per-node-context-scoping-skills-mcps-commands]], [[path-scoped-guardrails-edit-time-prevention]], [[lossy-compression-boundary-headless-return]], [[self-contained-phase-prompt-pattern]], [[hybrid-upfront-and-jit-context-architecture]]
2. **Q2:** "How do I structure the knowledge store an agent queries and choose its storage format and retrieval strategy?"
   - Findings clustering against Q2: [[fundamental-limits-of-single-vector-embedding-retr]], [[index-file-navigation-as-rag-replacement]], [[notebooklm-as-external-knowledge-base-for-context]], [[write-time-vs-query-time-synthesis-kb-poisoning]], [[agentic-rag-multi-strategy-retrieval-2026]], [[file-search-outperforms-rag-for-small-corpora]], [[hybrid-retrieval-pattern-semantic-lexical-graph]], [[summary-gate-agent-traversal-pattern]], [[personal-knowledge-hoard-as-agent-substrate]], [[ai-as-primary-reader-design-principle]], [[query-shape-first-storage-design]], [[per-folder-heterogeneous-retrieval-levels]], [[structural-outline-before-read-agent-navigation]], [[untyped-links-as-token-waste-anti-pattern]], [[knowledge-substrate-standardization-cross-agent-interop]], [[okf-open-knowledge-format-curated-bundle-spec]], [[rank-fusion-hybrid-retrieval-mongodb-atlas]], [[query-decomposition-sub-query-rrf-merge]], [[post-retrieval-reranking-weighted-signal-composition]], [[progressive-diorization-pipeline-raw-to-breadcrumb]], [[evergreen-vs-volatile-ingestion-rule]], [[self-describing-codebase-structural-semantic-context]]

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `structuring-agent-context` (retains stem) — practitioner question: "How do I decide what goes into my agent's context files and how it gets loaded — entry files, tiers, skills, sub-agent packages?" Working title: *Structuring and Loading Agent Context Files*.
- **Destination B:** `knowledge-storage-and-retrieval` — practitioner question: "How do I structure the knowledge store an agent queries and choose its storage format and retrieval strategy?" Working title: *Designing Knowledge Storage and Retrieval for Agents*.

Per-finding routing (every finding routed; no implicit handling per DD-98 §Rules #4):

| Finding | Disposition |
|---------|-------------|
| [[ace-agentic-context-engineering-evolving-playbook]] | A |
| [[agent-context-kiss-commandments-minimum-viable]] | A |
| [[context-curation-over-context-stuffing]] | A |
| [[context-enrichment-for-task-clarity]] | A |
| [[context-file-instruction-bloat-eth-zurich]] | A |
| [[document-sharding-for-context-efficiency]] | A |
| [[scrum-master-story-contextualization]] | A |
| [[model-specific-context-file-sensitivity]] | A |
| [[one-shot-prd-prompt-for-system-bootstrap]] | A |
| [[tiered-context-injection-over-monolithic-files]] | A |
| [[pointers-over-copies-in-context-files]] | A |
| [[progressive-tiered-context-loading-convergence]] | A |
| [[context-file-taxonomy-claudemd-soulmd-agentsmd]] | A |
| [[progressive-skill-loading]] | A |
| [[three-tier-progressive-context-loading]] | A |
| [[skills-as-pointers-to-second-brain-files]] | A |
| [[bounded-tiered-memory-inference-driven-curation]] | A (stays shared with G2b per existing routing note) |
| [[claude-code-context-management-decision-matrix-five-tools]] | A |
| [[inline-scoped-mcp-servers-per-subagent]] | A |
| [[environment-grounded-context-as-output-quality-multiplier]] | A |
| [[agent-memory-architecture-multi-agent-layered]] | A |
| [[interactive-explanations-extend-linear-walkthroughs]] | A |
| [[always-on-context-minimalism-pointer-only-entry]] | A |
| [[task-to-file-routing-table-in-context-files]] | A |
| [[cold-start-chain-and-cold-start-test]] | A |
| [[docs-split-by-lifespan-not-topic]] | A |
| [[skill-as-directory-progressive-disclosure-three-levels]] | A |
| [[skill-content-lifecycle-context-budget]] | A |
| [[skill-description-budget-context-overflow]] | A |
| [[skill-dynamic-context-injection-shell-prerender]] | A |
| [[hub-and-spoke-two-tier-skill-taxonomy]] | A |
| [[branch-analysis-externalization-rule-skill-reference]] | A |
| [[shared-context-folder-as-cross-skill-update-multiplier]] | A |
| [[per-node-context-scoping-skills-mcps-commands]] | A |
| [[path-scoped-guardrails-edit-time-prevention]] | A |
| [[lossy-compression-boundary-headless-return]] | A |
| [[self-contained-phase-prompt-pattern]] | A |
| [[hybrid-upfront-and-jit-context-architecture]] | shared (route to both — the upfront layer is A's territory; the JIT layer is B's retrieval question) |
| [[claudemd-as-knowledge-base-traversal-guide]] | shared (route to both — the file is A's entry-file surface; the traversal protocol is B's navigation question) |
| [[fundamental-limits-of-single-vector-embedding-retr]] | B |
| [[index-file-navigation-as-rag-replacement]] | B |
| [[notebooklm-as-external-knowledge-base-for-context]] | B |
| [[write-time-vs-query-time-synthesis-kb-poisoning]] | B |
| [[agentic-rag-multi-strategy-retrieval-2026]] | B |
| [[file-search-outperforms-rag-for-small-corpora]] | B |
| [[hybrid-retrieval-pattern-semantic-lexical-graph]] | B |
| [[summary-gate-agent-traversal-pattern]] | B |
| [[personal-knowledge-hoard-as-agent-substrate]] | B |
| [[ai-as-primary-reader-design-principle]] | B |
| [[query-shape-first-storage-design]] | B |
| [[per-folder-heterogeneous-retrieval-levels]] | B |
| [[structural-outline-before-read-agent-navigation]] | B |
| [[untyped-links-as-token-waste-anti-pattern]] | B |
| [[knowledge-substrate-standardization-cross-agent-interop]] | B |
| [[okf-open-knowledge-format-curated-bundle-spec]] | B |
| [[rank-fusion-hybrid-retrieval-mongodb-atlas]] | B (remains shared with G7) |
| [[query-decomposition-sub-query-rrf-merge]] | B (remains shared with G7) |
| [[post-retrieval-reranking-weighted-signal-composition]] | B (remains shared with G7) |
| [[progressive-diorization-pipeline-raw-to-breadcrumb]] | B |
| [[evergreen-vs-volatile-ingestion-rule]] | B |
| [[self-describing-codebase-structural-semantic-context]] | B |

Bifurcation precision: 59/61 routed cleanly (97%), 2 shared, 0 contested.

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture (no `## Nick's Annotations` section, no `<!-- PRESERVE -->` regions as of the 2026-07-16 regen).

## Routing-table impact

- **Source guide:** G2a row retitled/rescoped to Destination A (retains `structuring-agent-context` stem and G2a ID); no deprecation needed if A keeps the stem — alternatively deprecate G2a and mint G2a-i/G2a-ii per Nick's preference.
- **New rows:**
  - `knowledge-storage-and-retrieval` — practitioner question Q2, dimension Context Engineering, lifecycle stage `build`, status `draft`.
- **Dimension → Guide mapping changes:** Context Engineering row becomes G2a (context files/loading), G2b (degradation defense), plus the new B guide (knowledge storage/retrieval); G7 keeps its secondary-guide role. Trigger-keyword table: move "retrieval" keywords (retrieval, rank fusion, storage format, knowledge base structure, query shape, vector, RAG) to B; A keeps context window, CLAUDE.md, sharding, tiered loading, skills loading, pointers, progressive loading.
- **Disambiguation note update:** B vs G7 needs a discriminator line — B = designing the store and its retrieval (build-time); G7 = what persists across sessions and when to write it (runtime/operational). The three Memongo retrieval findings stay shared.

## Codifier recommendation

**Recommendation:** proceed with split as proposed

**Rationale:** 61 findings is 2.4× the DD-98 volume threshold and matches the mass that justified the original G2→G2a/G2b split (64). Bifurcation is clean — 97% of findings route without ambiguity, only 2 shared, 0 contested — and the two questions have visibly different reader intents (authoring an agent's instruction surface vs. architecting a queryable knowledge store). The regenerated single guide already strains the skill's 5,000-word ceiling.

## Notes

- Three prior split proposals (G3, G9, G10, 2026-05-25) remain unexecuted; if Nick prefers batching split rulings, this proposal can join that queue — the regenerated G2a remains fully serviceable in the interim.
- The G2a harvest queue created this session contains rows sourced from findings on both sides of the proposed bifurcation; on split execution, rows follow their source finding's destination per DD-101 Item 2.c supersession semantics.
