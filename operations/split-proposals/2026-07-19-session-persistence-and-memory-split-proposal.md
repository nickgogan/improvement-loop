---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-19"
source_guide: "session-persistence-and-memory"
finding_count: 40
practitioner_question_count: 2
session: 152
sl: "session-152 (SL retired as producer per session-138 ruling; git is the session record)"
---

# Split Proposal — Session Persistence and Memory

## Source guide identity

- **Guide stem:** `session-persistence-and-memory`
- **Current title:** "Session Persistence and Memory"
- **Finding count:** 40 (post-resolution; ≥25)
- **Routing-table row:** G7 in the Synthesis Status table of `operations/references/guide-routing-table.md` (Question: "How do I handle memory and session continuity?"; Stage: operate; Dimensions: Context Engineering, Orchestration)

## Practitioner-question analysis

The source cluster covers **2 distinct practitioner questions**. The guide's own title conjoins them ("Persistence *and* Memory"), and its six Parts partition cleanly along the seam:

1. **Q1 — Memory design:** "What should my agent remember across sessions, how do I retrieve it, and how do I govern what gets written?" (Guide Parts 1 Design Your Memory Architecture, 2 Retrieval Pipeline, 5 Govern Memory Writes, 6 Ingestion Pipelines.)
   - Findings clustering against Q1: [[four-tier-agent-memory-model-with-write-policy]], [[four-layer-enterprise-memory-stack]], [[biomimetic-memory-auto-recall-over-tool-based]], [[claude-code-long-term-memory-via-pre-prompt-recall]], [[ace-agentic-context-engineering-rag-based]], [[concept-graph-support-contradiction-detection]], [[memory-bank-isolation-per-agent-per-project]], [[mongodb-single-store-polymorphic-evidence-memory]], [[open-brain-personal-knowledge-store-pattern]], [[org-world-model-three-architecture-patterns]], [[post-retrieval-reranking-weighted-signal-composition]], [[query-decomposition-sub-query-rrf-merge]], [[rank-fusion-hybrid-retrieval-mongodb-atlas]], [[surprisal-novelty-as-memory-write-gate]], [[memory-cross-layer-promotion-governance]], [[subagent-persistent-memory-directory]], [[memory-wiki-world-kb-trichotomy]], [[memory-system-evaluation-triad-storage-injection-recall]], [[memory-file-to-skill-migration]], [[scalpel-local-parse-then-llm-cost-optimization]], [[dual-ingestion-funnel-human-clip-plus-llm-research]], [[signal-capture-as-byproduct-of-work]], [[append-only-lesson-store-owning-surface-identity]], [[agentic-file-classification-reliability-calibration]]
2. **Q2 — Session & state persistence:** "How do I persist and recover session/workflow state across crashes, compaction, and session boundaries — including the disk the agent runs on?" (Guide Parts 3 Session State and Persistence, 4 Session Lifecycle.)
   - Findings clustering against Q2: [[session-persistence-crash-resilient]], [[workflow-state-vs-conversation-state]], [[incremental-one-feature-per-session-pattern]], [[ground-truth-environmental-feedback-loops]], [[effort-scaling-rules-embedded-in-orchestrator]], [[file-based-task-locking-parallel-agents]], [[derive-dont-edit-artifacts-as-log-renders]], [[phase-queue-state-file-as-orchestrator-memory]], [[durable-checkpointed-sessions-as-framework-default]], [[incremental-snapshotting-copy-on-write-block-diffing]], [[posix-tiered-cache-persistence-over-object-storage]], [[snapshot-lineage-aware-fleet-scheduling]]

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `agent-memory-architecture` — practitioner question: "What should my agent remember, how do I retrieve it, and how do I govern writes?" (Parts 1, 2, 5, 6)
- **Destination B:** `session-and-workflow-state-persistence` — practitioner question: "How do I persist and recover session/workflow state across crashes and boundaries?" (Parts 3, 4)

Per-finding routing (every finding routed; no implicit handling per DD-98 §Rules #4):

| Finding | Disposition |
|---------|-------------|
| [[four-tier-agent-memory-model-with-write-policy]] | A |
| [[four-layer-enterprise-memory-stack]] | A |
| [[biomimetic-memory-auto-recall-over-tool-based]] | A |
| [[claude-code-long-term-memory-via-pre-prompt-recall]] | A |
| [[ace-agentic-context-engineering-rag-based]] | A |
| [[concept-graph-support-contradiction-detection]] | A |
| [[memory-bank-isolation-per-agent-per-project]] | A |
| [[mongodb-single-store-polymorphic-evidence-memory]] | A |
| [[open-brain-personal-knowledge-store-pattern]] | A |
| [[org-world-model-three-architecture-patterns]] | A |
| [[post-retrieval-reranking-weighted-signal-composition]] | A |
| [[query-decomposition-sub-query-rrf-merge]] | A |
| [[rank-fusion-hybrid-retrieval-mongodb-atlas]] | A |
| [[surprisal-novelty-as-memory-write-gate]] | A |
| [[memory-cross-layer-promotion-governance]] | A |
| [[subagent-persistent-memory-directory]] | A |
| [[memory-wiki-world-kb-trichotomy]] | A |
| [[memory-system-evaluation-triad-storage-injection-recall]] | A |
| [[memory-file-to-skill-migration]] | A |
| [[scalpel-local-parse-then-llm-cost-optimization]] | A |
| [[dual-ingestion-funnel-human-clip-plus-llm-research]] | A |
| [[signal-capture-as-byproduct-of-work]] | A |
| [[agentic-file-classification-reliability-calibration]] | A |
| [[session-persistence-crash-resilient]] | B |
| [[workflow-state-vs-conversation-state]] | B |
| [[incremental-one-feature-per-session-pattern]] | B |
| [[ground-truth-environmental-feedback-loops]] | B |
| [[effort-scaling-rules-embedded-in-orchestrator]] | B |
| [[file-based-task-locking-parallel-agents]] | B |
| [[phase-queue-state-file-as-orchestrator-memory]] | B |
| [[durable-checkpointed-sessions-as-framework-default]] | B |
| [[incremental-snapshotting-copy-on-write-block-diffing]] | B |
| [[posix-tiered-cache-persistence-over-object-storage]] | B |
| [[snapshot-lineage-aware-fleet-scheduling]] | B |
| [[append-only-run-log-as-working-memory]] | shared (durable working memory for Q2 crash/compaction recovery AND the accumulation surface Q1's lesson store distills from) |
| [[derive-dont-edit-artifacts-as-log-renders]] | shared (log→artifact discipline: a Q2 persistence mechanic, but the event-sourcing pattern also governs Q1 derived knowledge renders) |
| [[append-only-lesson-store-owning-surface-identity]] | shared (a Q1 durable semantic store, but the long-term complement to Q2's run log; the two findings are a pair) |
| [[structured-fact-extraction-from-conversations]] | shared (Q2 places it in the persistence path — survive compaction; Q1 owns it as the memory-write mechanism) |
| [[memorymd-cross-session-preference-persistence]] | shared (cross-session preference file: a Q1 memory surface delivered through Q2's session-boundary discipline) |
| [[session-history-import-as-memory-bootstrap]] | shared (bootstraps Q1 memory *from* Q2 session history — spans the seam by construction) |

Bifurcation precision: 34 of 40 route cleanly (23 A, 11 B); **6 shared (15%)**, 0 contested. Under the 20% shared/contested threshold, but the shared set is structurally load-bearing (the append-only run log and its derived-artifact/lesson-store pair are the connective tissue the guide is built around).

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture (no `## Nick's Annotations` block, no `<!-- PRESERVE -->` regions). Nothing to route.

## Routing-table impact

- **Source guide:** proposed deprecation (`stage: deprecated`) post-split, mirroring the G2→G2a/G2b precedent (session 104).
- **New rows:**
  - `agent-memory-architecture` — Q1; Dimensions: Context Engineering; lifecycle stage = `draft`.
  - `session-and-workflow-state-persistence` — Q2; Dimensions: Orchestration, Context Engineering; lifecycle stage = `draft`.
- **Dimension → Guide mapping changes:** Context Engineering's "Session Persistence and Memory" secondary would point to `agent-memory-architecture`; Orchestration's tertiary secondary would point to `session-and-workflow-state-persistence`. Trigger-keyword table: memory/persistence/memory-tiers/write-policy → A; session/crash-recovery/handoff/state-management/durable-workflow/disk-snapshot → B.

## Codifier recommendation

Closed enum: `proceed with split as proposed` | `defer pending more findings` | `re-evaluate practitioner-question bifurcation` | `absorb into adjacent guide instead`

**Recommendation:** defer pending more findings

**Rationale:** The two practitioner questions are real and the finding mass routes cleanly (85% clean, 0 contested), so the split is *executable* — but it is not yet *compelling*. The guide's coherence rests on a deliberate coupling the intro states explicitly ("six concerns that look separate but are deeply coupled"), and the 6 shared findings are exactly the connective tissue: the append-only run log is simultaneously Q2's crash/compaction-recovery mechanism and Q1's accumulation surface, and it travels as a pair with the derived-artifact and lesson-store findings. A split would duplicate that spine across both guides or arbitrarily assign it to one. The guide is also stable, heavily cross-referenced (G2a/G2b/G3/G3b/G6/G9/G11), and functions well as a single operate-stage playbook. Defer until one side's finding mass clearly dominates or the shared spine thins — at which point the bifurcation becomes clean enough to be worth the duplication cost.

## Notes

- This regen's changelog entry (Step 4.5) uses its normal `nick-request` trigger; this split-proposal is a separate side-channel artifact and did not alter the regen, which proceeded against the existing single-guide structure.
- Edge case to watch on any future re-evaluation: the wave-4 disk-persistence findings (findings 37–39, category Sandboxing/Orchestration) are Nick-routed into G7 and land firmly on the Q2 side — they deepen Q2's mass, nudging the balance toward a future clean split if more infrastructure-persistence findings arrive.
