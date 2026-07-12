---
name: "Knowledge-Substrate Standardization for Cross-Agent Interop"
summary: |-
  The argument for standardizing the knowledge base layer itself: everyone building a
  Karpathy-style LLM wiki structures it differently (metadata fields, folder layout,
  linking conventions), so nobody's agent can consume anybody else's wiki — small
  divergences compound into non-interoperability. A shared format ("what MCP did for
  agent-to-tool communication, OKF does for agent-to-knowledge-base communication")
  makes knowledge bases both consumable and producible by any conformant agent, and
  unlocks concrete mechanics: paste the spec.md into a coding agent to one-shot a
  conformant KB or refactor an existing one (parallelize the refactor across
  subagents), manage many bundles with two-tier indexing plus a thin CLI, and ship
  curated knowledge as shareable bundles — a distribution format for expertise.
implementation_notes: |-
  Flagged P2 because it puts a live, Nick-gated design question on the table: should
  the engine's KB (bespoke `_schema.yaml` today — exactly the non-interoperable
  artifact this argues against) be OKF-conformant, or at least OKF-exportable as a
  bundle? Decision-relevant context is captured in the body; no engine change is
  proposed here. The spec-as-skill and subagent-parallelized-refactor mechanics bound
  the migration cost if the answer is ever yes.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (research KB substrate)"
  - "General"
adopted_in: []
sources:
  - "open-standard-for-the-karpathy-llm-wiki.md"
  - "google-okf-vs-rag-confusion-finally-cleared-up.md"
related_findings:
  - file: "okf-open-knowledge-format-curated-bundle-spec.md"
    rel: "extends"
  - file: "karpathy-llm-knowledge-base-obsidian-rag.md"
    rel: "extends"
  - file: "skills-as-open-portable-standard.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

In plain English: your carefully curated knowledge base is useless to anyone else's
agent, because you invented its structure. This finding is the interop argument on top
of the OKF spec (see okf-open-knowledge-format-curated-bundle-spec.md for the format
itself).

The problem, concretely: two people follow the same Karpathy LLM-wiki gist and get
structurally different wikis — one has `tags`, the other `categories`; entity pages
link differently; folders differ. Hand your wiki to someone else's agent and it can't
search it optimally; it would have to reverse-engineer your conventions first, and it
may not bother. These little divergences compound. There is no way to share a wiki, run
a team-wide wiki that everyone's second brain queries independently, or distribute
curated knowledge as a product.

The fix is a standard for the substrate — Cole Medin's framing: **what MCP did for
agent-to-tool communication, OKF does for agent-to-knowledge-base communication.**
Notably, the spec standardizes both directions: *consuming* a knowledge base (search,
traversal) and *producing* one (how the wiki evolves, how entity pages build up). And
it standardizes only two things — how information is organized, and the metadata fields
— which is the point: a minimally opinionated floor everyone can target, not a rich
schema anyone will fork.

Adoption mechanics demonstrated in the source:

- **Spec-as-skill.** The spec.md file works like a skill document: paste it into a
  coding agent and it can one-shot a new conformant KB *or refactor an existing one* —
  the spec is long but trivial instruction volume for current frontier models.
- **Subagent-parallelized refactor.** For large existing KBs, have the agent fan the
  refactor out across subagents working different sections — migration cost scales
  sub-linearly with KB size.
- **Multi-bundle two-tier indexing + thin CLI.** A top-level document lists the bundles
  you have (layer one); each bundle carries its own index (layer two). A small CLI
  (list bundles / view a bundle's index / read by bundle + concept ID) gives agents
  deterministic access without any retrieval stack.
- **Shareable bundles as a distribution format.** Package curated knowledge (e.g. a
  channel's videos plus extracted concept pages) as a bundle; a consumer pastes the
  spec plus one prompt and their agent imports it into Obsidian/Notion/whatever and
  starts answering questions. Expertise becomes a git-cloneable artifact.

## Why It Matters

Standardized substrate turns knowledge bases from private infrastructure into an
ecosystem layer: team wikis, published bundles, and portable second brains all fall out
of one guarantee — any conformant agent can navigate any conformant bundle. The
secondary benefit holds even for never-shared KBs: with a common foundation,
practitioners can exchange *techniques* ("here are the entity-page conventions working
for me") that transfer directly instead of dying in translation between bespoke
schemas.

**Decision-relevant context for us (Nick-gated architecture question, not a
proposal):** the engine's research KB is a bespoke wiki with its own `_schema.yaml` —
exactly the non-interoperable artifact this finding argues against. The open question
is whether the KB should be OKF-conformant, or more conservatively OKF-*exportable*
(keep `_schema.yaml` internally, emit a conformant bundle as a distribution/consumption
surface for external agents and the portfolio-presenter/practitioner-friend consumer
archetypes). Both directions have real costs and the spec is v0.1; this is context for
a future gate, not a recommendation.

## Why People Are Using It

The Karpathy gist hit 40,000 stars and "pretty much everybody" is building an LLM wiki
— the installed base that makes non-interoperability hurt. OKF drew thousands of GitHub
stars within weeks. Cole Medin is restructuring his own bundles to it, shipping a
public bundle of his content, and explicitly betting on the *category*: even if OKF
itself doesn't win, "there's going to be something like this" — the same trajectory
skills took to an open portable standard (see skills-as-open-portable-standard.md).

## Potential Alternatives

Stay bespoke and translate on demand (an agent reverse-engineers each foreign wiki —
works, costs tokens and reliability every time). Export-only conformance (bespoke
internals, standard emission — the conservative middle). Richer standards that
standardize semantics too (higher interop, much harder to get adopted; OKF's minimalism
is a deliberate rejection of this).

## Potential Improvements

Conformance validators (the skills standard grew one). Registry/discovery conventions
for published bundles. A standard answer to write-access discipline for shared bundles
— today "producing" is standardized but review/merge is not.

## Potential Failure Modes

- **The standard doesn't win.** Single-vendor v0.1; the source itself doubts OKF is the
  final form. Early conformance work could be stranded by a successor standard.
- **"Too simple" critique.** The floor is so minimal that two conformant KBs can still
  differ enough in optional metadata to frustrate cross-agent search — the interop
  guarantee is weaker than the pitch.
- **Refactor risk.** One-shot spec-driven refactors of a large bespoke KB (especially
  subagent-parallelized) can silently drop schema semantics the standard has no slot
  for — for us, fields like evidence_strength or typed related_findings edges.
- **Shared-bundle trust.** Distribution-format bundles imported into a second brain are
  unreviewed third-party content an agent will treat as curated truth.
