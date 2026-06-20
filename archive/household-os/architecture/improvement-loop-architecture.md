---
notion_id: "32b1e08b-9b34-815c-808e-dce34af87d8f"
title: "Improvement Loop Architecture"
parent: "Architecture"
extracted: "2026-04-04"
---

> **For agents:** This is the documentation home for the Improvement Loop -- the self-improvement subsystem within the Meta-System that researches, proposes, evaluates, enhances, and codifies improvements to S2, S3, and itself. It uses a human-gated pipeline: Research -> [Human Gate] -> Propose -> [Human Gate] -> Evaluate -> Enhance -> [Human Gate] -> Deploy. For the live operational databases (Improvement Proposals), see the [Improvement Loop operational page](3251e08b-9b34-8143-859c-def8ed31b7ec).

---

## Overview

The Improvement Loop runs as a four-stage pipeline, each stage feeding the next:

| Stage | Tool | Input | Output |
|---|---|---|---|
| **1. Research** | research-loop skill | Current prompts/configs + search queries across four dimensions (Context, Model, Prompt, Tools) | Delta report: gaps, conflicts, aspirational patterns |
| **2. Evaluate** | prompt-evaluator skill | Flagged prompts from delta report | Scorecards with per-dimension ratings and improvement targets |
| **3. Enhance** | prompt-enhancer skill | Scorecards + original prompts | Proposed rewrites with rationale and diffs |
| **4. Review Gate** | Human (Nick) | Package: original, diff, rationale for each proposed change | Approved changes deployed via Cursor/Claude Code |

**Cadence:** Monthly (automated cron triggers the research scan via Perplexity Computer). Stages 1-3 run autonomously. Nick reviews at Stage 4.

**Scope:** Currently S3 vault prompts (CLAUDE.md, Build Specs, reference files). Future: S2 Custom Agent instructions.

---

## Relationship to The Compass (DD-18)

| Dimension | The Compass (DD-18) | Improvement Loop |
|---|---|---|
| **Monitors** | System health (vital signs, review cadences, orphan detection) | System evolution (are we using best practices? have new patterns emerged?) |
| **Cadence** | Daily/Weekly/Quarterly per review cadence | Monthly |
| **Scope** | S2 operational health within current schema | S2 + S3 configuration quality against external frontier |
| **Actor** | S2 agents + Nick/JR at review cadences | Perplexity Computer (automated) + Nick (review gate) |

They are **complementary, not overlapping**. The Compass asks "is the system healthy?" The Improvement Loop asks "is the system current?"

---

## Infrastructure

[Pipeline Architecture](32b1e08b-9b34-81c5-a152-e11bba9c0a4a)

[IL Skill Catalog](32b1e08b-9b34-818c-bcf7-cc890774a399)

[IL Vocabulary](32b1e08b-9b34-8109-8eae-c30adb7e2e01)

---

## AI Research

Curated knowledge base of agentic coding best practices. Maintained by the Researcher agent (research-loop skill). Contains Research Sources, Findings, and Authorities databases.

[AI Research](32b1e08b-9b34-8160-870d-cdc2827ba9e9)

[Improvement Proposals](32b1e08b-9b34-81b1-b124-dfa47e49116f)

---

## Design Decision Specs

Per DD-43, IL DD spec pages (DD-29, DD-30, DD-31, DD-36, DD-39, DD-41) now live in the DD database page bodies -- query the [Design Decisions](https://www.notion.so/cffef89836724e29822ec894594752bc) database with `Target System = "Improvement Loop"` to find them.

---

## Tool References

The pipeline uses three Perplexity Computer skills:

- **research-loop** -- Scans across four dimensions (Context Engineering, Model Selection, Prompt Craft, Tool Integration) plus an Intent meta-dimension
- **prompt-evaluator** -- Four-discipline rubric (Prompt Craft, Context Engineering, Intent Engineering, Specification Engineering)
- **prompt-enhancer** -- Transforms evaluation output into concrete prompt rewrites

## Child Pages Not Extracted

The following child pages under Improvement Loop Architecture were not included in this extraction:

- **Pipeline Architecture** (32b1e08b-9b34-81c5-a152-e11bba9c0a4a)
- **IL Skill Catalog** (32b1e08b-9b34-818c-bcf7-cc890774a399)
- **IL Vocabulary** (32b1e08b-9b34-8109-8eae-c30adb7e2e01)
- **AI Research** (32b1e08b-9b34-8160-870d-cdc2827ba9e9)
- **Improvement Proposals** (32b1e08b-9b34-81b1-b124-dfa47e49116f)
