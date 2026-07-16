---
name: Evergreen-vs-Volatile Ingestion Rule
summary: 'Only ingest data into the second brain that you would still want there in a year

  (locked-in decisions, quarterly priorities, holistic context). Volatile data — Slack

  threads, emails, live customer records — stays in its system of record; the brain

  gets ACCESS to those systems, not copies. Copied volatile data is noise that demands

  monthly deletion sweeps and degrades recall. The test at ingestion time: "in a year,

  will it be good to have this memory in here?"'
implementation_notes: 'The engine already practices this shape implicitly (local markdown KB holds curated

  findings; Household OS operational data stays live in Notion and is accessed via MCP,

  never copied). Worth making the rule explicit in Librarian design guidance and in any

  future ingestion-skill contract: an ingest step should classify evergreen vs volatile

  before writing, and route volatile items to an access pointer instead of a copy.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- General
- IL (knowledge architecture)
adopted_in:
- Improvement Loop
sources:
- every-level-of-a-claude-second-brain-explained.md
related_findings:
- file: escalating-search-order-routing.md
  rel: enables
- file: write-time-vs-query-time-synthesis-kb-poisoning.md
  rel: same-problem
- file: write-back-discipline-memory-is-not-the-brain.md
  rel: same-problem
- file: docs-split-by-lifespan-not-topic.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
---

## What It Is

An ingestion gate for curated knowledge bases. Nate Herk splits candidate data along
his "context vs connections" line:

- **Context (evergreen)** — what the business has decided and what is durably true:
  quarterly objectives with statuses, locked-in decisions, holistic background. This is
  what gets ingested into the brain.
- **Connections (volatile)** — "real data that isn't as evergreen": Slack threads,
  emails, customer data, anything that changes next week. This is deliberately NOT
  ingested — "that's just noise then. Then you have to go back every month and delete
  old stuff." Instead the brain gets tool access to the live system of record (ClickUp,
  email) and pulls current data on demand.

The ingestion-time test: "in a year, will it be good for me to have this memory in
here? Yes → ingest. Otherwise it's just adding noise."

## Why It Matters

The dual of the drowning problem at the corpus level: an over-ingested brain
accumulates stale copies that compete with (and contradict) live truth, imposes a
recurring deletion/maintenance tax, and pollutes retrieval. The rule bounds the curated
corpus to what curation actually buys — durable, low-churn knowledge — while keeping
volatile truth exactly one tool-call away.

## Why People Are Using It

Herk runs his production business brain this way and explicitly frames control over
ingestion as the reason he declines always-on autonomous ingestion (level 5 / Gbrain
crons): "I am in complete control of what my second brain ingests." Converges with the
Gbrain camp's own write-back discipline (world facts to the KB, ephemeral chatter not),
approaching the same boundary from the opposite side.

## Potential Alternatives

Always-on ingestion with TTL/decay metadata (accept volatile copies, expire them
automatically). Derived-index approaches that ingest everything but rank by recency and
provenance.

## Potential Improvements

An explicit staleness contract per folder (this folder's contents are evergreen; that
folder is a synced mirror with refresh cadence). Ingestion skills that classify
evergreen/volatile and emit an access pointer instead of a copy for the volatile class.

## Potential Failure Modes

The evergreen judgment is made at ingestion time and can be wrong — "durable" decisions
get superseded (mitigate with a decisions log that appends supersessions rather than
silently rotting). Under-ingestion: if access tooling to the system of record is
missing or broken, the brain simply doesn't know the volatile half exists.
