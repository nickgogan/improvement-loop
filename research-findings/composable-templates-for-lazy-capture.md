---
notion_id: 32b1e08b-9b34-811b-a1bb-ecba6b69859c
name: Composable Templates for Lazy Capture
summary: Every note type (meeting, person, book, quote, movie, evergreen) has a dedicated template that pre-populates YAML properties. Templates are designed to be composable — multiple templates can be
  applied to the same note without overlap — enabling flexible multi-type notes without redundancy.
implementation_notes: null
category: Memory Architecture
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S2 (Notion Operations)
adopted_in: null
sources: []
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Composable Templates for Lazy Capture

## What It Is
The vault includes templates for: journal/daily, meeting, person, book, movie, quote, and evergreen. Each template adds only the YAML properties relevant to that note type. Steph's rule: 'almost every note I create starts from a template. I use templates heavily because they allow me to lazily add information that will help me find the notes later.' A note about an author who is also someone you know personally can receive both the 'person' template (birthday, website) and the 'author' template (books written) without conflict because templates are scoped to non-overlapping property sets.

## Why It Matters
Templates standardize metadata at creation time, making subsequent querying reliable. For AI agent workflows, the analogous pattern is structured output schemas — defining upfront what fields an agent must populate ensures downstream queries can filter reliably rather than parsing free-text.

## Why People Are Using It
Reduces cognitive overhead at capture time. A meeting note auto-includes fields for attendees, location, date, and topics — you just fill in values rather than remember to add metadata. This 'laziness as a feature' philosophy accelerates note volume without sacrificing retrievability.

## Potential Alternatives
Manual front-matter writing, Dataview inline fields, dedicated database apps (Notion, Airtable) with fixed schemas. Templates are the simplest approach for local-first systems.

## Potential Improvements
AI-assisted template selection based on note title/content at creation time. Auto-population of date and linked entities could further reduce friction.

## Potential Failure Modes
Template proliferation: too many templates creates choice paralysis at creation time, defeating the laziness goal. Templates must be maintained when properties evolve.
