---
name: "Escalating Search-Order Routing (Curated File → Wiki → Live System of Record)"
summary: |-
  A second brain answers vague questions not by containing everything but by knowing
  where to look and in what order: first the curated file most likely to hold the
  answer, then the broader wiki/transcript layer, and only then the live external
  system of record (ClickUp, email). The escalation order is part of the routing
  design, and it is what lets the evergreen-only ingestion rule work — volatile truth
  is reachable, just last in line.
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
  - "every-level-of-a-claude-second-brain-explained.md"
related_findings:
  - file: "evergreen-vs-volatile-ingestion-rule.md"
    rel: "enabled-by"
  - file: "claudemd-as-knowledge-base-traversal-guide.md"
    rel: "extends"
  - file: "intent-based-meta-routing-skill.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

An ordered fallback chain encoded in the brain's routing rules. Nate Herk's worked
example: asked "what did John and I talk about last week about OTA #7?", his system
(1) checks the curated OTA file first, (2) falls back to the wiki and ingested meeting
transcripts, and (3) finally goes to ClickUp itself and pulls the live conversation.
His definition of a working second brain hangs on this: "I'm able to ask a vague
question, and the second brain knows exactly where to look in what order to find that
real-time data." The order runs cheapest-and-most-curated first, live-and-volatile
last.

## Why It Matters

Escalation order is the piece that makes access-not-copy ingestion viable: without a
defined order, an agent either hammers the expensive live system for every question or
never reaches it at all and reports "not found" for anything volatile. It also bounds
token cost — most queries terminate at step 1 or 2.

## Why People Are Using It

Production use in Herk's business brain. Structurally the same move as the OKF-cluster
query router (canonical → curated KB, exploratory → retrieval) and the KB's existing
CLAUDE.md-traversal findings — routing intelligence in a text file rather than a
retrieval stack.

## Potential Improvements

Make the escalation explicit per data domain (each folder's routing note names its own
fallback target). Log which tier answered each query — repeated escalations to tier 3
for the same topic signal that the topic has become evergreen enough to ingest.

## Potential Failure Modes

Stale tier-1 files that answer confidently and stop the escalation before fresher truth
in tier 3 is consulted (the stale-docs problem in routing form). Missing or broken
tool access at tier 3 silently truncates the chain.
