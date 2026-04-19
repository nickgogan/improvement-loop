---
notion_id: 32b1e08b-9b34-81ed-b02e-cc0480d1c375
name: 'Context Type Taxonomy: Structural vs. Operational vs. Proprietary'
summary: 'Three enterprise context types have different defensibility: structural context (system connections, data locations, permissions) is commodity plumbing; operational context (informal decision-making
  knowledge) is defensible only if it changes faster than platforms can ingest; proprietary context (data that gives competitive advantage) is the most durable moat.'
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: Not Flagged
applicability:
- General
adopted_in: []
sources: []
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Context Type Taxonomy: Structural vs. Operational vs. Proprietary

## What It Is
Structural context: How systems connect, where data lives, what permissions exist. Commodity by 2026. Operational context: How decisions actually get made; the informal knowledge in senior people's heads. Defensible only when the update frequency exceeds what platforms can ingest. Proprietary context: Data and judgment that exists nowhere else. This is where the enterprise calculation flips -- don't hand it to the platform.

## Why It Matters
Most companies claiming to have domain context moats have not rigorously identified which type of context they actually have. The distinction determines build strategy, pricing strategy, and partnership strategy with model providers.

## Why People Are Using It
Practitioners building AI systems for enterprises need this taxonomy to identify whether they're building on sand (structural context) or rock (proprietary context).

## Potential Improvements
The taxonomy could be extended with a fourth dimension: temporal context (how quickly a company's context changes) as a separate axis from the content type.

## Potential Failure Modes
The taxonomy oversimplifies mixed-context scenarios where a company has some structural, some operational, and some proprietary context in their system.
