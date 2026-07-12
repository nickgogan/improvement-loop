---
term: memory
type: concept
variants:
  - working
  - episodic
  - semantic
  - global-learnings
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-concept"
  - "memory"
  - "variant-carrier"
aliases:
  - "Memory"
  - "Agent memory"
  - "Memory architecture"
---

# Memory

## Short definition

**Memory** is the read/write policy system by which an agent retains information across time — within a turn, across turns of one session, and across sessions. Memory is not the context window, not a vector store, and not a knowledge base. Memory is *deliberate* — every read has a policy, every write has a gate (G7 §Key Concepts, line 51).

The canonical memory architecture is four-tiered (working, episodic, semantic, governance); **global-learnings** is a widely cited practitioner realization of the semantic + episodic surface for cross-session persistence (see Variants below). Variant selection is usually implicit in the consumer's phrasing and should be resolved before composing substrate.

## Not to be confused with

| Not memory | What it is instead |
|---|---|
| **Context window** | Volatile, per-turn model input. Memory *loads into* the context window; the window is not itself memory. See `context-rot.md` for context-window failure modes. |
| **Second brain** | A knowledge *surface* (vault, KB, notes). Memory spans more than a single surface — working tier is in-context, governance tier is append-only audit. See `second-brain.md`. |
| **Long context** | A larger window is not memory — it has no write policy, no retrieval logic, no tier discipline. G7 Key Concept 1 is emphatic: "Long context is not memory." |
| **RAG / vector store** | A retrieval mechanism over *some* tier (usually episodic or semantic). The store is not the memory; the memory is the policy over the store. |
| **Session state / workflow state** | "What step am I on" and "what side effects happened" — that's workflow state (G3b). Memory is "what do I know"; workflow state is "where am I in the plan." G7 Key Concept 2 draws this line. |

## Variant selection

Variants here are **tiers of one architecture**, not mutually exclusive designs. A consumer query usually names one tier — or implies the whole architecture when variant-ambiguous (UC-1.5, UC-4.3). Quick heuristics:

| Consumer says… | Variant | Why |
|---|---|---|
| "my agent loses constraints mid-session," "the last few turns are blurry," "compaction is dropping details" | **Working** | In-context, current-turn memory — the window itself, plus the compaction discipline operating on it. |
| "my agent can't recall what it did last week," "the task log is gone after restart," "it keeps re-doing the same work" | **Episodic** | Task-history tier — who / what / when / why with provenance, retrieved by similarity. |
| "my agent forgets *facts* (entity names, project conventions, decisions) across sessions" | **Semantic** | Entities, relationships, policies. Curated, schema-owned, rarely pruned. |
| "my agent doesn't remember lessons from previous runs," "the same failures keep happening," "what it learned last time is gone" | **Global-learnings** | Cross-session learnings store — a specific practitioner pattern that usually lives at semantic + episodic tier boundaries. |

If the consumer says "my agent's memory architecture" with no further qualifier, the query spans all four — load the whole composition (UC-1.5 is this case).

## Variants (stubs)

Stubs only. Deeper per-tier composition iterates as queries arrive.

### Variant A — Working memory

The current context window plus the policies that shape what stays and what gets compacted. Compaction discipline, delta updates, attention-budget mechanics, and proactive-compaction-before-degradation all fire here. **Primary failure mode:** context rot — see `context-rot.md`. Guide surface: G2b. Practitioner pattern: `proactive-compaction-before-intelligence-degradation`.

### Variant B — Episodic memory

Task history with provenance. Append-only on the write path with evidence pointers; retrieved by semantic similarity on the read path. Lifespan months with pruning by importance/recency. Highest-risk transition is *promotion* from episodic to semantic — distilling episodes into durable facts requires explicit policy (G7 Part 1 §Step 1.2, line 86). Guide surface: G7. Practitioner patterns: `four-tier-agent-memory-model-with-write-policy`, `importance-based-decay-permanent-exemption`.

### Variant C — Semantic memory

Entities, relationships, constraints, policies. Curated. Schema-owned — not every agent can write to shared semantic memory. Retrieval is by structured query, not similarity. Writes are policy-gated (G7 Key Concept 5, line 61). Guide surface: G7. Practitioner patterns: `mongodb-single-store-polymorphic-evidence-memory` (contradicts `triple-storage-memory-architecture` — surface the debate on design-debate queries per UC-5.2), `memory-cross-layer-promotion-governance`.

### Variant D — Global-learnings

Cross-session learnings store — the "what did I learn last time" tier. Canonically *auto-recalled* (injected into context before every prompt) rather than tool-looked-up, per G7 Key Concept 4 (line 59): "Auto-recall beats tool-based memory." Without expiry / validation mechanisms the store decays into noise (G2b, line 242). Guide surface: G7 (primary) + G2a (on the injection-into-context side). Practitioner patterns: `gsd-global-learnings-store-cross-session-persistence`, `claude-code-long-term-memory-via-pre-prompt-recall`, `memorymd-cross-session-preference-persistence`.

## Composition

Substrate pointers for the core Librarian operations. Rows that apply to only some variants mark the applicable set.

| Aspect | Tier 1 (guides, default) | Tier 2 (patterns / findings) | Tier 3 (watched-libraries) |
|---|---|---|---|
| Architecture / four-tier design | G7 `session-persistence-and-memory.md` §Key Concepts, §Part 1 "Design Your Memory Architecture" | `four-tier-agent-memory-model-with-write-policy`, `four-layer-enterprise-memory-stack`, `production-memory-architecture-spectrum` | — |
| Write gates and policy | G7 §Key Concepts 5, §Part 1 §Step 1.2 (Promotion/Demotion policies) | `surprisal-novelty-as-memory-write-gate`, `importance-based-decay-permanent-exemption`, `memory-field-immutability-via-merge-operations` | — |
| Recall strategy (auto vs tool) | G7 §Part 1 §Step 1.3 "Choose Your Recall Strategy" | `claude-code-long-term-memory-via-pre-prompt-recall`, `biomimetic-memory-auto-recall-over-tool-based`, `hook-based-transparent-memory-injection` | Anthropic memory-tool docs |
| Retrieval mechanics (semantic + episodic) | G7 §Part 1 §Step 1.3 | `post-retrieval-reranking-weighted-signal-composition`, `rank-fusion-hybrid-retrieval-mongodb-atlas`, `hybrid-retrieval-pattern-semantic-lexical-graph`, `query-decomposition-sub-query-rrf-merge` | Memongo repo; Letta / MemGPT source |
| Persistence and recovery | G7 §Part 2 "Implement Session State and Persistence", §Key Concept 3 (persist after events) | `database-as-shared-memory-coordination`, `claude-code-hooks-for-automatic-session-memory` | — |
| Write-path synthesis (episodic→semantic) | G7 §Part 1 §Step 1.2 (promotion), §Part 4 §Ingestion | `structured-fact-extraction-from-conversations`, `dreaming-memory-consolidation`, `memory-decay-compaction-convergence` | — |
| Working-tier into context (Variant A) | G2b `defending-agent-context.md` §"Detecting Context Degradation", §Contract | `context-rot-attention-budget-depletion`, `proactive-compaction-before-intelligence-degradation` — see `context-rot.md` | — |
| Cross-session policy / governance | G7 §Part 3 "Manage Session Lifecycle"; G9 §Contract for HITL on semantic writes | `governance-memory-append-only-audit-layer`, `memory-cross-layer-promotion-governance` | — |
| Single-store vs multi-store debate | — (guides summarize; Tier 2 carries the debate) | `mongodb-single-store-polymorphic-evidence-memory` ↔ `triple-storage-memory-architecture` (typed `contradicts`) | Memongo repo |
| Decision tree for failure modes | G7 §Decision Tree "What Kind of Memory Problem Do You Have?" (line 533), §Pitfalls (line 567) | — | — |

## Librarian read rule

**Default (Tier 1).** Resolve the variant from the consumer's phrasing. For single-variant queries, pull the operation's named subsection kind from G7 (+ G2b for Variant A context-window concerns, + G9 for semantic-write governance). For variant-ambiguous queries (UC-1.5 "memory architecture"), read G7 §Key Concepts and §Part 1 wholesale — they are the architecture-level overview.

**Escalate to Tier 2 when:**
- Consumer is in a design-debate (single-store vs triple-storage) — surface the `contradicts` pair (`mongodb-single-store-polymorphic-evidence-memory` ↔ `triple-storage-memory-architecture`) proactively. This is load-bearing for UC-5.2.
- Consumer asks about write-gate or retrieval mechanics that guides summarize without unpacking.
- Consumer reports a symptom that maps to a practitioner-pattern cluster (e.g., "forgets facts across sessions" → `memorymd-cross-session-preference-persistence` + `gsd-global-learnings-store-cross-session-persistence`).

**Escalate to Tier 3 when:**
- Consumer is building a reference-implementation comparison (Memongo's rank-fusion implementation, Letta/MemGPT episodic design).
- Consumer needs the exact shape of Anthropic's memory tool API.

**Do not:**
- Treat "long context" or "vector store" questions as memory questions without confirming. They are adjacencies; redirect or clarify.
- Answer "what should my memory architecture look like?" from Variant A alone. Variant-ambiguous queries span all four tiers.
- Skip the `contradicts` surface on single-vs-multi-store questions. The debate is the substance.

## Provenance surfacing

Tier-1 citations: `<guide>.md#<anchor>` with line-range appendix until the section manifest lands (Nick's session-49 gate). Tier-2 citations: finding file path + slug. Tier-3 citations: `watched-lib/<path>:<line-range>`. When the Librarian surfaces a `contradicts` pair, cite *both* findings and state that they contradict — never paper over the debate.

## Cross-references

- Related concepts: `context-rot.md`, `second-brain.md`, `agent.md` (this directory).
- Related operations: `audit.md`, `diagnose.md`, `design.md`, `decide.md` (planned) — all compose this file for memory-aspect queries.
- Use-case registry (UC-1.5, UC-4.3, UC-5.2, UC-7.1, UC-8.3): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role), DD-82 (IL 4-agent architecture).
