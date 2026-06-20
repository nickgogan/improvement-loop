---
notion_id: 32b1e08b-9b34-81c5-a152-e11bba9c0a4a
title: "Pipeline Architecture"
parent: "Improvement Loop Architecture"
extracted: "2026-04-04"
---

# Pipeline Architecture

> **For agents:** This page defines the Improvement Loop pipeline architecture — how research flows from discovery through codification. For the operational description of the loop, see the Improvement Loop page. For the governing system boundaries, see Constitution.

---

## 4-Stage Core Pipeline

The minimal pipeline that runs each monthly cycle. Stages 1-3 run autonomously via Perplexity Computer; Nick reviews at the human gate.

| Stage | Skill | Input | Output |
|-------|-------|-------|--------|
| **1. Research** | research-loop | Current prompts/configs + search queries across four dimensions (Context, Model, Prompt, Tools) | Delta report: gaps, conflicts, aspirational patterns → AI Research KB |
| **2. Evaluate** | prompt-evaluator | Flagged prompts from delta report | Scorecards with per-dimension ratings and improvement targets |
| **3. Enhance** | prompt-enhancer | Scorecards + original prompts | Proposed rewrites with rationale and diffs |
| **4. Review Gate** | Human (Nick) | Package: original, diff, rationale per proposed change | Approved changes deployed via Cursor/Claude Code |

---

## 6-Stage Extended Pipeline

Full pipeline adding Propose and Codify stages for governance-grade changes.

| Stage | Skill | Input | Output | Human Gate |
|-------|-------|-------|--------|------------|
| **1. Research** | research-loop | URLs, search queries, current configs | Research Sources, Findings, Authorities (AI Research DBs) | After: Nick reviews findings and priorities |
| **2. Propose** | research-proposer | Research Findings (filtered by priority) + current system docs | Improvement Proposals | After: Nick reviews proposals |
| **3. Evaluate** | prompt-evaluator | Flagged prompts from proposals | Scorecards with ratings | — |
| **4. Enhance** | prompt-enhancer | Scorecards + original prompts | Proposed rewrites with diffs | After: Nick approves rewrites |
| **5. Codify** | research-codifier (planned) | Approved proposals | Codified Practices entries | After: Nick confirms codification |
| **6. Apply** | system-applicator (future) | Codified Practices + target system docs | System-specific skill/config updates | After: Nick approves application |

---

## AI Research Knowledge Base Structure

Three databases under the Improvement Loop:

- **Research Sources** — Every URL, video, and paper fed into the system, with processing status.
- **Research Findings** — Distilled knowledge entries, one per pattern/technique, with evidence and applicability tracking. Each has a full page body: What it is, Why it matters, Why people use it, Alternatives, Improvements, Failure modes.
- **Research Authorities** — People, channels, institutions as valuable knowledge sources. Tracks source diversity; prevents over-indexing on a single authority.

**Routing mechanism:** The `Applicability` property on Research Findings is a multi-select across `S2`, `S3`, `Perplexity Skills`, `General`. This determines which system receives proposals.

**Priority flow:** `Proposer Priority` (P1/P2) on Research Findings gates which findings flow into Improvement Proposals.

---

## Key Architectural Decisions

- **Two-phase, two-skill model** — Research and Proposal are separate skills with separate Cognitive Dispositions (DD-30)
- **Strict read/write boundaries** — Each skill has an explicit Access Model (DD-35)
- **Human-gated pipeline** — No autonomous modification of live systems (DD-29)
- **Conflict detection** — The Proposer identifies conflicting proposals as first-class output (DD-31)
- **One-way vs. two-way door classification** — Every proposal assessed for reversibility (DD-31)
- **Codification before application** — Approved proposals become Codified Practices before system-specific changes (DD-39)

---

## Governing DDs

| DD | Title | Key Rule |
|----|-------|----------|
| DD-29 | Human-Gated IL Pipeline | No autonomous modification of any live system |
| DD-30 | IL Agent Architecture | Two-skill model with strict read/write boundaries |
| DD-31 | Proposal Assessment Model | Scoped assessment, conflict detection, door-type classification |
| DD-35 | IL Skill Pipeline | Distinct skills with enforced scope boundaries and handoff points |
| DD-36 | Research-Driven Improvement Model | Evolution driven by periodic external research |
| DD-39 | Codification Pipeline | Codified Practices as distinct stage before application |
| DD-41 | IL Data Ownership | AI Research and Proposals live under IL Architecture |

---

## Recent Governance Extensions

- **DD-45** (supersedes DD-43): MetaSystem as active knowledge layer. Knowledge generated through the IL pipeline flows back into MetaSystem patterns, not just into target system configs.
- **DD-46**: Knowledge flows through IL into MetaSystem patterns. The IL is not just a pipeline for improving S2/S3 — it is the mechanism by which MetaSystem itself evolves.
