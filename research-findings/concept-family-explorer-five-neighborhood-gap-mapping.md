---
name: 'Concept-Family Explorer — Five-Neighborhood Family Mapping with Scored Gaps Above the Build Engine'
summary: 'Where the build engine (/dr) makes a skill for a topic you NAME, concept-family-explorer answers "what am I missing?" It maps a subject''s full conceptual family across five neighborhoods — parent, sibling, child/sub-concept, adjacent/cross-over, frontier — scores every discovered concept against a rubric (novelty, usefulness, coverage gap), then loops the build engine over each viable gap with a bounded brief until the concept tree saturates. Resumable, and it both reads and writes the shared concept tree, so coverage discovery and coverage recording are the same loop.'
implementation_notes: 'The engine''s research intake is reactive (Nick supplies links/topics; /research-loop scans dimensions) — this is the missing proactive layer: a repeatable procedure for asking "what does the KB not know about domain X" before spending research budget. The five-neighborhood frame is directly adoptable as a checklist inside /research-query or a future gap-analysis skill even without the full loop: for any engine research dimension, enumerate parent/sibling/child/adjacent/frontier concepts and diff against existing findings (the KB''s ~900 findings make the diff cheap with rg). The scored-gaps step matters for Nick-gating: it converts "here is everything we could research" into a ranked shortlist with explicit criteria, which is the shape the engine''s human gate wants. Relevant to the restructure program''s Phase 1 (research grounding): wave planning could be neighborhood-mapped instead of link-driven.'
category: Orchestration
evidence_strength: Medium (practitioner-documented, production system at a large enterprise (repo private, author-shared writeup))
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- hub-and-spoke-context-hub.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: dr-research-to-skill-gated-pipeline.md
  rel: extends
- file: skill-tree-architect-whole-tree-shape-audit.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
tags:
- gap-analysis
- concept-mapping
- research-planning
- saturation
---

# Concept-Family Explorer — Five-Neighborhood Family Mapping with Scored Gaps

## What It Is

The discovery layer that sits *above* the research-to-skill build engine. Given a subject
(e.g. "vector databases"), it maps the subject's complete conceptual family across five
neighborhoods, each answering one question:

| Neighborhood | Question |
|---|---|
| **Parent** | What broader domain contains this? |
| **Sibling** | What peers sit alongside it under the same parent? |
| **Child / sub-concept** | What does this decompose into? |
| **Adjacent / cross-over** | What neighboring fields overlap or feed in? |
| **Frontier** | What is emerging / next at the edge of the field? |

It then scores each discovered concept against a rubric (novelty, usefulness, coverage
gap), and loops the build engine (`/dr`) over every viable gap with a bounded brief until
the concept tree saturates. Runs are resumable and persist their results to the shared
hub, so a half-finished domain mapping survives a session.

## Why It Matters

Plain English: research systems are usually good at answering the questions someone asks
and bad at noticing the questions nobody asked. This gives "what am I missing?" a
mechanical procedure with a termination condition. The five neighborhoods are the load-
bearing idea — they force coverage to be checked in *every direction* (up, sideways,
down, diagonal, forward), which is exactly where ad-hoc research goes lopsided (deep on
children, blind on adjacents and frontier).

The division of labor is also clean and worth copying: use the explorer to *complete
coverage* of a domain; use the build engine directly when you already know the topic.

## How It Works

- **Map first, build second.** The strategy's best-practices list is explicit: for any
  non-trivial domain, run the explorer before building anything — it prevents lopsided
  coverage and duplicate artifacts.
- **Scoring gates the loop.** Discovered concepts are not all built; the rubric (novelty,
  usefulness, coverage gap) filters to *viable* gaps, and each gets a bounded brief so
  the downstream build engine cannot scope-creep.
- **Shared state through the concept tree.** The explorer reads the tree to know what
  exists and the build engine writes researched concepts back — the tree is both input
  and output of every run, which is what lets stateless tools coordinate across runs and
  operators.
- **Worked example.** "Vector databases" maps siblings (pgvector, Milvus, Weaviate,
  Qdrant), children (HNSW, IVF, quantization), adjacent (RAG retrieval, embeddings), and
  frontier (disk-based ANN); ~12 gaps score as viable; the ≥8-sibling family spawns a hub
  on the first build and the rest land as spokes.

## How It Could Fail

- **Neighborhood explosion.** Adjacent/cross-over is unbounded for broad subjects; the
  scoring rubric and bounded briefs are the only containment.
- **Rubric subjectivity.** Novelty and usefulness scores are model judgment; a scored
  shortlist looks more objective than it is. Human review of the shortlist (not the full
  map) is the cheap correction.
- **Saturation without freshness.** A saturated tree goes stale; this only works long-
  term because the concept tree carries a staleness clock that re-queues old concepts.
