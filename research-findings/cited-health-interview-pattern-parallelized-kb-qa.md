---
name: 'Cited Health Interview Pattern: Parallelized KB Q&A for Personal Protocol Design'
summary: Run multiple Claude Code sub-agents in parallel against a NotebookLM expert knowledge base, each tasked with querying a different health dimension (sleep, exercise, supplements, stress, biomarkers,
  etc.), then aggregate the citation-grounded answers into a structured assessment that drives personal experiment design.
implementation_notes: null
category: Agentic Systems
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources:
- notebooklm-claude-code-expert-experiments.md
proposals: []
date_discovered: '2026-04-19'
last_updated: '2026-04-20'
related_findings:
- file: notebooklm-mcp-claude-code-cited-knowledge-layer.md
  rel: companion
- file: learn-plan-act-review-loop-closing-the-knowledge-gap.md
  rel: companion
- file: claude-code-daily-brief-multi-source-inbox-obsidian.md
  rel: same-problem
- file: multi-agent-proportional-content-summarization.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Cited Health Interview Pattern: Parallelized KB Q&A for Personal Protocol Design

## What It Is

A two-phase Claude Code workflow for turning an expert knowledge base into a personalized protocol:

**Phase 1 — Expert interview (parallel):**
- Claude Code spawns 6 sub-agents simultaneously, each querying NotebookLM on a different health dimension (sleep optimization, exercise, supplements, stress management, light exposure, biomarkers)
- Each agent returns a question and a grounded answer with source citations
- Results are saved to Obsidian as individual Q&A notes, with a dashboard note linking all questions and sources
- Claude can be asked to verify citation quality (scored 7/8 as strong matches in the demonstration)

**Phase 2 — Personal gap assessment:**
- The user answers the interview questions in natural language
- Claude reads existing experiment data from Obsidian ("go grab my fitness data") to enrich the assessment
- Claude produces a current-state vs. target-state gap assessment with high/medium/low priority ratings
- The top-priority gaps become candidate experiments

The pattern uses scientific method framing: each proposed experiment has an explicit hypothesis, protocol steps, and a measurable success criterion (e.g., "80% of days within 30 minutes of target wake-up time").

## Why It Matters

The interview pattern bridges two gaps:

1. **Coverage gap:** A single question ("how do I improve my health?") returns a generic answer. Six parallel dimension-specific questions produce comprehensive, actionable coverage with far less back-and-forth.

2. **Personalization gap:** Generic expert advice is rarely optimal for an individual's specific current state. The gap assessment step combines expert knowledge with the user's actual current state (read from their existing experiment data) to produce a prioritized, personalized protocol.

Citation traceability means every recommended protocol can be traced to a specific expert source — the recommendation is not Claude's opinion but a documented expert position.

## Why People Are Using It

- Parallel execution collapses what would be a multi-hour manual research session into minutes
- Citation grounding means the user can verify or challenge any recommendation by reading the source
- The gap assessment framing (current state, target state, gap severity) structures decision-making rather than producing a flat list of suggestions
- The scientific method framing (hypothesis + success criterion) makes experiments falsifiable and time-bounded

## Potential Improvements

A follow-up "experiment review" query at interval (e.g., 30 days) could re-run the gap assessment with updated experiment data to show progress and reprioritize. Domain generalization: the same pattern works for any expert domain (product management, fitness programming, nutrition, etc.) by swapping the NotebookLM knowledge base.

## Potential Failure Modes

- Dimension selection determines coverage: a poorly chosen set of 6 dimensions will miss important areas
- The gap assessment depends on the quality of the user's self-report; vague or inaccurate answers produce poor prioritization
- Citation quality depends on transcript quality in the source videos — auto-captions with errors produce lower-quality grounding
- The parallel query pattern may exceed NotebookLM's rate limits for simultaneous queries against a single notebook
