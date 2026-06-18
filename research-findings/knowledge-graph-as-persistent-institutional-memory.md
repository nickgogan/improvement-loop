---
name: "Knowledge Graph as Persistent Institutional Memory"
summary: "A typed knowledge graph functions as institutional memory that outlives any individual team member. New team members who lack historical context (why a pricing decision was made, what alternatives were considered, which constraints drove the choice) can query the graph and trace the full decision provenance. The graph captures not just what was decided, but the supporting evidence, contradicting arguments, and dependencies that informed the decision."
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: P3
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "karpathy-second-brain-typed-edge-alternative.md"
related_findings:
  - file: typed-edge-knowledge-graph-token-reduction.md
    rel: enables
  - file: concept-graph-support-contradiction-detection.md
    rel: same-problem
  - file: domain-specific-intelligence-from-historical-busi.md
    rel: same-problem
  - file: personal-knowledge-hoard-as-agent-substrate.md
    rel: same-problem
  - file: tacit-knowledge-as-agent-delegation-barrier.md
    rel: same-problem
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

# Knowledge Graph as Persistent Institutional Memory

## What It Is

Using a typed knowledge graph as a durable store of institutional knowledge that survives team transitions. The key differentiator from personal knowledge management is the focus on decision provenance and organizational context rather than individual learning.

The practitioner illustrates with a pricing decision example: the graph stores not just "we decided: no free tier" but also:
- The pricing philosophy that led to the decision (via `depends-on` edge)
- The Stripe fee analysis that informed it (via `derived-from` edge)
- The question of whether to offer a team tier (via `related-to` edge)
- The hypothesis about creator willingness to pay (via `supports` edge)
- The monthly recurring revenue data that contextualized the decision (via `related-to` edge)

A new team member can trace this graph and understand not just what was decided but why — "all this amazing understanding of this unique complex question or all the ideas of pricing. And then let's say you have a new team member that maybe doesn't have all this institutional knowledge. They weren't on these calls talking about it. This is documented and it can outlive the team that you have today."

The critical structural property is that institutional knowledge is not stored as a narrative document ("here's why we made this decision") but as a graph of typed relationships between atomic facts. This makes it queryable by agents along any axis — by decision, by source, by hypothesis, by data point — rather than requiring reading a linear document.

## Why It Matters

Institutional knowledge loss is one of the most expensive organizational problems. When a key person leaves, the "why" behind decisions walks out the door. Written documentation (decision logs, wikis, meeting notes) captures some of it, but unstructured documentation is hard to query and easy to let go stale.

A typed knowledge graph addresses both problems:
- **Queryable by agents** — an AI agent can trace the provenance of any decision in seconds, surfacing the full reasoning chain
- **Maintained by AI** — the graph is AI-constructed and AI-maintained, so it doesn't depend on humans keeping docs up to date

For MetaSystem: the IL's Design Decisions (DDs) already serve an institutional memory function — each DD records what was decided and why. The gap is that DDs are standalone documents without typed edges to the evidence, alternatives, and dependencies that informed them. Adding typed cross-references between DDs, findings, and proposals would create the kind of provenance graph described here.

## Why People Are Using It

The practitioner deploys this with clients for business knowledge management, with pricing decisions and strategic analysis as primary use cases. The Karpathy LLM-compiled wiki pattern provides a corroborating case — Karpathy's wiki compiles knowledge from raw sources into a navigable structure. The concept graph with support/contradiction detection (TasteMatter) adds the relationship-tracking layer that makes institutional memory queryable.

## Potential Improvements

- **Decision provenance views** — specialized graph traversals that start from a decision node and walk backwards through all supporting evidence, contradicting evidence, and dependencies
- **Temporal layering** — distinguishing between current institutional knowledge and historical knowledge (decisions that were valid then but superseded now)
- **Confidence scoring** — weighting edges by the strength of the supporting evidence (a decision backed by data analysis vs. a decision backed by intuition)

## Potential Failure Modes

- **Incomplete capture** — the graph only captures what was explicitly recorded. Informal hallway conversations, unspoken assumptions, and political considerations are not captured
- **Stale provenance** — if the underlying evidence changes but the decision edges are not updated, the provenance chain becomes misleading
- **Over-trust in provenance** — a well-structured graph of reasoning can make a bad decision look well-supported if the evidence was flawed
- **Maintenance burden** — institutional memory only works if the graph is continuously updated. If the team stops feeding new decisions into the graph, it becomes a historical snapshot rather than a living memory
