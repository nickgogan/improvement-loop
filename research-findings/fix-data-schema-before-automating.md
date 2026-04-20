---
name: Fix Data and Schema Before Automating (Commandment Pattern)
summary: 'Before giving an agent access to any system, establish a source of truth, define schemas, build validation, and decide conflict resolution. Nate B Jones: ''super boring work that is very essential.'''
implementation_notes: null
category: Intent Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- agent-produces-100x-org-reviews-3x.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
related_findings:
- file: independent-eval-and-scoped-authority-commandments.md
  rel: same-problem
pipeline_status: extracted
consumed_by:
- rules/fix-data-schema-before-automating.md
---
## What It Is

A prerequisite discipline for agent deployment: before automating any workflow, establish a single source of truth, define explicit schemas for all data the agent will read or write, build validation rules, and decide conflict resolution strategies. This is the "commandment" that precedes all other agent work.

## Why It Matters

The $14K voice agent failure case study illustrates the cost of skipping this step: no one specified schemas, records ended up scattered across systems, and funnel measurement was impossible despite the system being "up and functioning." The agent did exactly what it was told — the problem was that nobody defined what "correct" looked like for the data it produced.

## Why People Are Using It

Schema-first design is the foundation that makes agent work sustainable. MetaSystem's own `_schema.yaml` approach validates this pattern — frontmatter schemas define what valid governance data looks like before any agent writes to it. The pattern applies universally: CRM records, support tickets, knowledge base entries, any structured data an agent touches.

## Potential Improvements

- Define schemas as machine-readable artifacts (YAML, JSON Schema) that agents can reference
- Build validation into the agent's tool layer so invalid writes are rejected before they reach the data store
- Establish conflict resolution rules (last-write-wins, merge, flag-for-human) before the first agent write
- Audit existing data for schema compliance before enabling agent access

## Potential Failure Modes

- **Day 1 vs Day 30 degradation:** Month 1 feels good because the volume of dirty data is small. Months 2-3 expose accumulated drift as schema violations compound and downstream consumers break.
- **Schema rigidity:** Over-specified schemas block legitimate edge cases. Schemas need an evolution path (versioning, migration) or they become a bottleneck.
- **Automating on dirty data:** If existing data does not conform to the schema, the agent inherits garbage on Day 0. Data cleanup must precede automation, not follow it.
- **False confidence from validation:** Passing schema validation does not mean the data is semantically correct — an agent can produce schema-valid but factually wrong records.

## Extraction Note — 2026-04-19
Extracted as **rule**: [[fix-data-schema-before-automating]] in `extracts/rules/`
