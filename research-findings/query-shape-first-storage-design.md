---
name: Query-Shape-First Storage Design
summary: 'Design the storage format of knowledge backwards from the questions you will ask it —

  how data will be accessed and recalled determines how it should be put in. Concrete

  test case: a query like "summarize the March 5th meeting" fails on vector-chunked

  storage (retrieval returns a few similarity-matched chunks, never the whole

  transcript) but succeeds trivially on one whole markdown file the agent reads in

  full. Conversely, "what was rule 17 of our 1,000 rules?" is wasteful as a whole-file

  read and ideal as a vector snippet lookup. The anticipated query shape — whole-object

  synthesis vs pinpoint lookup vs relationship trace — is the storage-format decision

  input, not the data''s topic or size.'
implementation_notes: 'Directly usable Librarian advice substrate: when consumers ask "should this be

  markdown files, a wiki, or vector search?", the first question is what query shapes

  they anticipate. Also validates the engine''s own KB shape — findings are queried as

  whole documents (read the finding, not chunks of it), which is exactly the shape

  markdown-file storage serves. Candidate criteria-delta for /ask-kb Builder-mode

  design guidance.'
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
- file: ai-as-primary-reader-design-principle.md
  rel: same-problem
- file: per-folder-heterogeneous-retrieval-levels.md
  rel: enables
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
---

## What It Is

Reverse-engineer the storage format from the anticipated query shape. Nate Herk's
framing: "how it's going to be accessed and recalled determines the way that you put it
in in the first place" — the basketball-hoop analogy (you know the hoop's shape, so you
don't design the ball as a square). Three query shapes map to three storage answers:

- **Whole-object synthesis** ("summarize the March 5th meeting", "which week had the
  highest sales in this table") → one markdown file, read in full. Vector chunking
  actively fails here: the agent retrieves ~5 similarity-matched chunks of a 20-chunk
  document and summarizes only those, or answers "highest sales" from whichever chunk
  the match landed on while higher values sit in unretrieved chunks.
- **Pinpoint lookup in bulk text** ("what was rule 17?" across 1,000 stored rules) →
  vector/semantic search. Reading the whole rules file for one rule wastes time and
  tokens; a chunk snippet is the right return shape.
- **Relationship trace** ("ask about topic X, trace it back to topic A") → knowledge
  graph with typed edges; wiki backlinks ("see also") approximate but don't carry
  relation semantics.

The practical procedure he recommends: describe the data and the intended usage to the
agent itself and ask which storage format fits ("I have this data. Here's how I want to
use it. Markdown files or semantic search — what makes more sense?").

## Why It Matters

The most common second-brain failure he sees is not retrieval quality but mismatched
storage format: practitioners assumed a vector DB was "a magic solution where it could
always pull back what you need" and then hit systematic failures on summary- and
aggregate-shaped queries. Deciding storage per query shape prevents both
over-engineering (RAG for data that's read whole) and under-engineering (whole-file
reads over bulk text needing pinpoint recall).

## Why People Are Using It

Practitioner-documented across Herk's production "Herc 2" business brain; consistent
with the KB's existing corroboration that coding agents dropped vector DBs for
file-and-grep retrieval (file-search-outperforms-rag-for-small-corpora) and with the
AI-as-primary-reader principle (design for the reader — here, for the reader's
question).

## Potential Alternatives

Uniform storage plus hybrid retrieval (vector + lexical + graph over the same corpus,
as Gbrain does) — pays infrastructure cost to avoid per-corpus format decisions.
Metadata-enriched chunking to patch vector search's whole-object blindness.

## Potential Improvements

A small catalog of query-shape → storage-format mappings the Librarian can cite. An
intake-time prompt ("what will you ask this data?") in ingestion skills.

## Potential Failure Modes

Anticipated query shapes are guesses — usage drifts, and a format chosen for
summary-queries later gets pinpoint-queries (mitigated by per-folder retrofit, see
per-folder-heterogeneous-retrieval-levels). Multi-shape data (both summarized whole and
pinpoint-queried) forces either duplication or hybrid retrieval.
