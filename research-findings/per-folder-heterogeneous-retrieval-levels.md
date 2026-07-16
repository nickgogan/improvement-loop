---
name: Per-Folder Heterogeneous Retrieval Levels, Upgraded on Felt Pain
summary: 'A second brain is not one retrieval architecture — each folder gets the retrieval

  level its data shape and query shape deserve: plain routing + markdown here, an LLM

  wiki there, a vector index for one bulk-text corpus, a knowledge graph only where

  relationship traces are actually asked for. And levels are upgraded per folder only

  when a concrete pain is felt ("if there''s not pain, why create more?"), never

  speculatively. Nate Herk''s five-level ladder: (1) CLAUDE.md routing + folders,

  (2) LLM wiki with indexes, (3) semantic search, (4) knowledge graph, (5) always-on

  autonomous brain — with his own production system deliberately sitting at level 2.'
implementation_notes: 'Upgrades the KB''s existing scale-threshold heuristic from a system-wide either/or

  (markdown vs RAG) to a per-folder decision — directly relevant to how the Librarian

  advises consumers and to any future engine retrieval upgrades (e.g., a vector layer

  over transcripts only, while findings stay whole-file markdown). The pain-driven

  trigger aligns with agent-rules rule 11 (abstractions must earn their keep) —

  retrieval infrastructure is an abstraction that needs recurrence evidence.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- General
- IL (knowledge architecture, Librarian advice)
adopted_in:
- Improvement Loop
sources:
- every-level-of-a-claude-second-brain-explained.md
related_findings:
- file: scale-threshold-heuristic-obsidian-vs-rag.md
  rel: extends
- file: context-infrastructure-seven-level-maturity-model.md
  rel: same-problem
- file: query-shape-first-storage-design.md
  rel: enabled-by
- file: hybrid-retrieval-pattern-semantic-lexical-graph.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
---

## What It Is

Two coupled rules over a five-level retrieval ladder:

**The ladder** (each level answers a different question):
1. **Routing files + folders** — can you find it by exact word or name? CLAUDE.md as
   router with "where things live" rules.
2. **LLM wiki** — can you pull everything on a topic together? Index files + concept
   pages + backlinks; trails are followed by reading whole pages.
3. **Semantic search** — you search with different words than you wrote; meaning-match
   instead of keyword-match (Obsidian smart lookup, Pinecone, Supabase).
4. **Knowledge graph** — trace typed relationship chains (works-at, endorsed-by);
   backlinks are "see also," not relations. Often more token-efficient than wikis for
   entity questions because it doesn't require reading whole pages.
5. **Always-on autonomous brain** — constant sync/refresh/ingest (Gbrain-style crons).

**Rule 1 — per-folder assignment:** "your whole project doesn't fit into one level.
Maybe this folder's level two, maybe this folder's level four." One vector-indexed
corpus (e.g., YouTube transcripts) can sit beside plain-markdown decisions and
projects folders.

**Rule 2 — pain-driven upgrades:** find the *lowest* level that fits; upgrade a folder
only when a concrete symptom is felt. His diagnostic mapping: re-explaining your setup
→ level 1 routing is missing; 30+ notes you keep forgetting → level 2 wiki; whiffing on
notes you know exist despite routing → level 3 semantic; needing relationship chains →
level 4; syncing fleets of agents over huge data → level 5. Herk explicitly runs his
whole production business brain at level 2 and declines 4-5: "if there's not pain, then
why create more?"

## Why It Matters

Kills the false dichotomy in "markdown vs RAG" debates: the decision is per-folder, and
the default answer is the cheapest level that hasn't caused pain yet. This is the
selection heuristic behind most of the second-brain advice the engine gives consumers,
now with a concrete symptom→level table instead of a single corpus-size threshold.

## Why People Are Using It

Herk's production system demonstrates the mixed-level layout. The pain-driven stance
matches the KB's scale-threshold heuristic (Chase AI: "just try it, migrate when it
breaks") and the maturity-model finding's warning against skipping levels — now
corroborated from an additional independent channel (Nate Herk).

## Potential Alternatives

Uniform hybrid retrieval over the whole corpus (vector + lexical + graph everywhere,
e.g. Gbrain) — trades per-folder decisions for infrastructure cost. AI-optimized
uniform graph structures (typed-edge knowledge graph over everything, per the KB's
karpathy-second-brain-typed-edge source).

## Potential Improvements

A written per-folder retrieval manifest (folder → level → upgrade symptom to watch
for). Pairing with query-shape analysis at ingestion so the initial level assignment
is informed, not defaulted.

## Potential Failure Modes

Heterogeneity has a coordination cost: the router must know which retrieval mechanism
each folder uses, or queries get mis-dispatched. Pain-driven upgrading is reactive by
design — teams with low observability may not feel the pain signal until well after
retrieval quality degraded.
