---
name: "Write-Back Discipline: Memory Is Not the Brain"
summary: |-
  The usage habit that makes a world-KB actually accumulate value: durable calls made
  in conversation get written back to the knowledge base as pages, at decision time.
  Gbrain's five operating rules: search the brain first for people/companies/projects/
  meetings/decisions; answer from the pages themselves; write decisions back; cite
  everything; and "memory is not the brain" — world facts go into the KB, not agent
  memory. Without the write-back habit, decisions rot in session history where only
  conversation search can find them.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "General"
  - "IL (knowledge architecture)"
adopted_in:
  - "Improvement Loop"
sources:
  - "give-your-ai-agent-a-second-brain-gbrain-hermes.md"
related_findings:
  - file: "memory-wiki-world-kb-trichotomy.md"
    rel: "enabled-by"
  - file: "memory-cross-layer-promotion-governance.md"
    rel: "same-problem"
  - file: "evergreen-vs-volatile-ingestion-rule.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

An operating discipline for agents paired with a world-KB, codified as Gbrain's five
usage rules and demonstrated round-trip in the source:

1. **Search the brain first** for people, companies, projects, meetings, decisions —
   before memory, before guessing.
2. **Answer from the pages** — grounded in stored content, not reconstruction.
3. **Write decisions back** — "durable calls become brain pages." The source closes
   the loop live: a decision made in Hermes chat ("start the Acme pilot on local PG
   lite; zero-infra proof of concept before hosted Postgres") is written via MCP tool
   into the brain as a typed decision page, immediately verified and searchable.
4. **Everything is cited** — every answer references its source pages.
5. **Memory is not the brain** — world facts go into the KB, not agent memory.

The write-back is the promotion step of the memory/wiki/world-KB trichotomy: content
that originates in conversation (memory's territory) but is durable by nature
(world-KB territory) must be explicitly moved at the moment it becomes durable.

## Why It Matters

The trichotomy's boundary lines only hold if something enforces them at write time.
Skip rule 3 and every decision is findable only by conversation search — exactly the
architectural blindness the world-KB exists to fix. The engine practices the same
discipline in its own domain (session decisions become DDs and findings, not chat
residue); this is the general form.

## Why People Are Using It

Shipped as Gbrain's official usage rules and demonstrated live with Hermes Agent. The
discipline framing ("the real advantage is seen as you develop this habit") matches
practitioner consensus in the KB's memory findings that storage layers without
curation habits become noise.

## Potential Improvements

Automating the promotion trigger: detect decision-shaped statements in-session and
prompt "write this back?" instead of relying on the human to remember. Policy gates on
what qualifies as durable (see memory-cross-layer-promotion-governance) to keep
write-back from becoming auto-ingestion noise.

## Potential Failure Modes

Over-write-back reintroduces the volatile-noise problem the ingestion rule guards
against — every passing thought becomes a "decision page." Write-back without
supersession handling accumulates contradictory decision pages over time; cited
answers then confidently quote the outdated one.
