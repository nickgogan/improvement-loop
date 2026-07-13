---
name: "Memory / Wiki / World-KB Trichotomy"
summary: |-
  Three distinct knowledge stores that practitioners keep conflating: agent MEMORY
  remembers your conversations (only what passed through the agent — an architectural
  boundary, not a bug); an LLM WIKI knows one domain (curated concept pages compiled
  through a pipeline with human gates); a WORLD-KB knows your world (typed pages for
  people, companies, meetings, decisions — including things that never touched any
  chat). "Memory remembers our conversations, wikis know domains, the world-KB knows
  our world." The three compose rather than compete; each has a different ingestion
  path and a different failure mode when asked the wrong question.
implementation_notes: |-
  The cleanest boundary vocabulary yet for a recurring Librarian advice topic — where
  agent memory ends and a knowledge base begins. Maps onto engine surfaces: Claude
  Code auto-memory/session state = memory; the research KB and guides = domain wiki;
  a world-KB layer (people/orgs/meetings/decisions) is the piece the engine does NOT
  have and Household OS-adjacent work keeps gesturing at. Use the trichotomy when
  advising consumers which store their data belongs in. Gbrain (the source's
  world-KB implementation, 25k stars, MIT) is a watched-libraries CANDIDATE —
  Nick-gated, not yet registered.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "General"
  - "IL (knowledge architecture, Librarian advice)"
adopted_in:
  - "Improvement Loop"
sources:
  - "give-your-ai-agent-a-second-brain-gbrain-hermes.md"
related_findings:
  - file: "memory-vs-rag-product-distinction.md"
    rel: "same-problem"
  - file: "open-brain-personal-knowledge-store-pattern.md"
    rel: "same-problem"
  - file: "karpathy-llm-knowledge-base-obsidian-rag.md"
    rel: "extends"
  - file: "write-back-discipline-memory-is-not-the-brain.md"
    rel: "enables"
  - file: "memory-system-evaluation-triad-storage-injection-recall.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "session-persistence-and-memory.md"
---

## What It Is

A boundary taxonomy for three stores that get lumped together as "the agent's brain":

- **Agent memory** (e.g., Hermes memory: curated always-loaded memory.md/user.md,
  FTS session search over past conversations, pluggable providers). Built to remember
  a *collaboration* — what was said, decided, and inferred inside the agent. Its hard
  limit is architectural: every layer only remembers what passed through the agent.
  Ask it about a meeting it never saw and full-text search over every conversation
  still returns zero.
- **LLM wiki / domain KB**: curated concept-and-entity pages about ONE domain,
  compiled by a pipeline with human gates, published for any agent to read. Answers
  "how does X work" for its domain; knows nothing outside it.
- **World-KB** (Gbrain's category): typed pages for people, companies, projects,
  meetings, decisions — with a graph and cited synthesis — that deliberately ingests
  what never touched chat (notes folders, Obsidian vaults, meeting write-ups). "The
  difference between what the agent picked up along the way and what you deliberately
  decide to keep."

The one-line compression: memory remembers our conversations, wikis know domains, the
world-KB knows our world. The stores compose: memory stays the lean curator layer in
every prompt; the world-KB is the catalog the agent searches first for
people/projects/decisions.

## Why It Matters

Most "my agent forgot X" complaints are category errors — asking memory a world
question or a wiki a conversation question. The trichotomy gives designers a routing
rule for where each datum belongs and users a correct expectation of what each store
can answer. It also explains why bolting more memory providers onto an agent never
fixes the "it doesn't know about the Acme pilot" class of failure.

## Why People Are Using It

Tonbi's AI Garage demonstrates the failure live (session search over all history: zero
matches for a decision that lives in unseen meeting notes) and the fix (Gbrain
world-KB returns it with cited sources). Gbrain itself: 25k+ stars, MIT, actively
developed, commonly paired with OpenClaw/Hermes. The wiki leg matches the KB's
existing Karpathy-wiki cluster; the memory leg matches its layered-memory findings —
this finding supplies the boundary lines between them.

## Potential Alternatives

Converged single-substrate designs (one governed DB with vector/relational/graph
access for all memory types — see converged-memory-substrate-vs-patchwork) collapse
the trichotomy into access patterns instead of separate stores. Memory-provider
products (Supermemory, Honcho) blur memory and world-KB by ingesting external data
into "memory."

## Potential Improvements

A fourth column for procedural knowledge (skills/how-to), which the trichotomy leaves
implicit. Explicit promotion paths between stores (conversation decision → world-KB
page; recurring world pattern → wiki concept).

## Potential Failure Modes

Boundary disputes in practice: a decision made in-chat is memory by origin but
world-KB by nature — without a write-back discipline it lands in the wrong store and
becomes unfindable. Running all three stores multiplies curation surfaces; a solo
operator may only have budget to keep one healthy.
