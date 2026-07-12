---
name: "OKF (Open Knowledge Format): Curated Knowledge Bundle Spec"
summary: |-
  Google Cloud's OKF (shipped June 2026, v0.1 spec on GitHub) is the first
  vendor-published open standard for the curated markdown knowledge base: a "bundle" is
  a folder of markdown files, one concept per file, YAML frontmatter with `type` as the
  only required field, a reserved index.md table of contents for navigation, an
  append-only log.md change log, and ordinary markdown links that turn the bundle into
  a walkable knowledge graph. The load-bearing category distinction: RAG is a process,
  OKF is a format — RAG re-derives knowledge at query time from raw chunks; an OKF
  bundle stores curated, cross-linked concepts the agent reads directly. Two
  consequences most takes miss: the substrate is read-write (agents edit concepts in
  place, so the KB improves itself), and a bundle can feed a RAG pipeline as clean,
  pre-labeled source — the format composes with the process rather than replacing it.
implementation_notes: |-
  Flagged P2 because the engine's research KB is exactly this shape — curated markdown
  concepts with YAML frontmatter, filename-based relations, and its own bespoke
  `_schema.yaml` — and OKF is the first open spec for that shape. The design work is a
  convention-by-convention comparison (index.md vs frontmatter-driven ripgrep
  discovery, log.md vs git history + System Log, `type` vs our per-folder schemas)
  feeding the Nick-gated conformance question captured in
  knowledge-substrate-standardization-cross-agent-interop.md. Not an adoption
  recommendation; the spec is v0.1 from a single vendor.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (research KB substrate)"
  - "General"
adopted_in: []
sources:
  - "google-okf-vs-rag-confusion-finally-cleared-up.md"
  - "open-standard-for-the-karpathy-llm-wiki.md"
related_findings:
  - file: "knowledge-substrate-standardization-cross-agent-interop.md"
    rel: "extended-by"
  - file: "curated-spine-plus-rag-hybrid-query-router.md"
    rel: "extended-by"
  - file: "index-file-navigation-as-rag-replacement.md"
    rel: "extends"
  - file: "karpathy-llm-knowledge-base-obsidian-rag.md"
    rel: "extends"
  - file: "write-time-vs-query-time-synthesis-kb-poisoning.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

In plain English: the folder-of-markdown knowledge base that practitioners have been
hand-rolling (claude.md, the Karpathy LLM wiki, our own research KB) now has a
vendor-published open spec. Google Cloud shipped OKF — Open Knowledge Format — in June
2026 as a spec on GitHub. The unit is a **knowledge bundle**: a directory of markdown
files with no database, no embedding model, and no retriever.

Spec conventions (deliberately minimal):

- **One concept per file.** Each markdown file is one idea — a table schema, a metric
  definition, a runbook. YAML frontmatter on top, plain markdown below.
- **`type` is the only required metadata field.** Title, description, tags, timestamps,
  and `resource` (a link to the real asset) are recommended but optional. Everything
  else is left to the bundle author.
- **index.md as navigation.** A reserved table of contents for the bundle: the agent
  reads the index, sees what concepts exist, and walks straight to the ones it needs —
  navigation instead of similarity guessing, typically pulling the two files that
  matter instead of a dozen fuzzy chunks.
- **log.md as append-only change log.** Knowledge stays curated *and* versioned.
- **Ordinary markdown links between concepts.** Orders table points at customers table
  points at refunds runbook; the bundle becomes a small knowledge graph an agent walks
  hop by hop.
- **Plain files travel anywhere.** "If you can cat a file, you can read OKF. If you can
  git clone a repo, you can ship it." Diffable, PR-reviewable, ownable, revertible.

The category distinction that clears up the "OKF killed RAG" confusion: **RAG is a
process, OKF is a format** — like asking whether npm beats package.json. RAG re-derives
what your data means on every query, from fragments with no memory between calls. An
OKF bundle stores curated, cross-linked concepts the agent reads directly. Re-derive
versus read.

Two second-order properties:

1. **Read-write substrate.** Retrieval is read-only; an agent can open an OKF concept,
   fix a stale schema, add a note, and commit — the knowledge base improves itself over
   time, the way a shared handbook gets tidied.
2. **Bundle as pre-labeled RAG input.** OKF and RAG compose: feed a bundle into a
   retrieval pipeline as clean, structured, already-labeled source. The format makes
   the process better rather than replacing it.

Google shipped tooling alongside the spec: an enrichment agent that drafts OKF docs for
every table/view in a BigQuery dataset (schemas, citations, join paths), a visualizer
that renders a bundle's knowledge graph as one self-contained HTML file, and sample
bundles (GA4 e-commerce, Stack Overflow dump, Bitcoin public data).

## Why It Matters

The division of labor is crisp: RAG earns its keep on huge, messy, uncurated piles
(millions of support tickets); OKF is for knowledge worth the care — schemas, metric
definitions, the 3 a.m. runbook — the high-value material you need exactly right, not
fuzzily retrieved. Both fight hallucination from different angles: RAG grounds the
model in whatever it happened to retrieve; OKF grounds it in something a human already
decided was correct.

For us specifically: the engine's research KB *is* a curated, cross-linked,
frontmatter-typed markdown knowledge base with agents that read and write it. OKF is
the first external standard describing that shape, which makes it the natural reference
point for auditing our conventions — and the prerequisite reading for the
conformance/exportability question tracked in the substrate-standardization finding.

## Why People Are Using It

The spec landed with unusual traction — thousands of GitHub stars within weeks, real
first-party tooling, and immediate practitioner uptake (Cole Medin demonstrates a
working bundle and ships his own). The instinct it standardizes is already ubiquitous:
anyone who has written a claude.md has built a one-file OKF. Google's own pitch: what
was missing is a format, not another service — the USB-C connector every tool already
speaks.

## Potential Alternatives

The unstandardized Karpathy LLM wiki (same shape, no interop guarantee — see
karpathy-llm-knowledge-base-obsidian-rag.md). Traditional RAG over a vector DB (wins on
uncurated scale). llms.txt / llms-full.txt (single-file, publish-only, no read-write or
graph conventions). Bespoke per-team schemas like our `_schema.yaml` (richer typing,
zero portability).

## Potential Improvements

The spec is v0.1 and deliberately underspecified — expect conventions to accrete around
index granularity, multi-bundle composition, and write-discipline (who may edit
concepts, and how edits are reviewed). Enrichment-style generators for sources beyond
BigQuery would remove the cold-start cost.

## Potential Failure Modes

- **Single-vendor draft risk.** v0.1, weeks old, one vendor; the honest guidance from
  the source itself is bookmark it, don't bet the company on it.
- **Curation is the unpriced cost.** Every concept is somebody's curation work; OKF is
  hopeless as a dumping ground and does not scale itself.
- **Read-write substrate inherits the KB-poisoning tradeoff.** Agents editing concepts
  in place is write-time synthesis — stale or wrong agent edits become curated "truth"
  unless reviewed (see write-time-vs-query-time-synthesis-kb-poisoning.md; log.md and
  git diffs mitigate but don't eliminate this).
- **Minimalism cuts both ways.** With only `type` required, two conformant bundles can
  still diverge enough in optional metadata to degrade cross-agent search.
