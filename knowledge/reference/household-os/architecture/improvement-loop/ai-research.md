---
notion_id: 32b1e08b-9b34-8160-870d-cdc2827ba9e9
title: "AI Research"
parent: "Improvement Loop Architecture"
extracted: "2026-04-04"
---

# AI Research

> **For agents:** This is the knowledge base for agentic coding best practices. The research-loop skill populates it. The research-proposer skill reads it to generate improvement proposals (written to the sibling [Improvement Proposals](improvement-proposals-docs.md) page). Neither skill modifies systems outside its designated write scope without human approval.

---

## Purpose

A curated, maintained knowledge base of **how AI agents are being used in practice** — focused on agentic coding patterns (Claude Code, Cursor, MCP, prompt engineering, agent memory, multi-agent orchestration, evaluation). This is not a theoretical AI research library. It tracks **what practitioners are doing** and **what works**.

---

## Researcher Access Model

| Scope | What | Access |
|---|---|---|
| **Read** | URLs, videos, papers, web search results | Read-only — external source material for extraction |
| **Read** | Research Findings DB (this page) — for deduplication checks | Read-only — check existing findings before creating new ones |
| **Write** | Research Sources DB (this page) | Full write — create and update source entries |
| **Write** | Research Findings DB (this page) | Full write — create new findings, update existing ones with new evidence |
| **Write** | Research Authorities DB (this page) | Full write — create and update authority entries |
| **Never** | Improvement Proposals DB, system configs, vault files | No access — the Researcher does not propose changes or modify systems |

---

## Two-Phase Model

One agent, two modes, with a human gate between them.

| Phase | Skill | Reads | Writes |
|---|---|---|---|
| **1. Research + Triage** | research-loop | URLs, videos, papers, web search results | Research Sources DB, Research Findings DB, Research Authorities DB (this page) |
| *Human reviews findings and priorities* | | | |
| **2. Propose** | research-proposer | Research Findings DB, current system state (DDs, Architecture pages, vault files, Perplexity skills) | Improvement Proposals DB (sibling page) |

---

## Databases

Three databases make up this section:

- **Research Sources** — every URL, video, and paper fed into the system, with processing status
- **Research Findings** — distilled knowledge entries, one per pattern/technique, with evidence and applicability tracking
- **Research Authorities** — people, channels, institutions, and organizations that are valuable knowledge sources. Used to track source diversity and prevent over-indexing on any single authority

---

## Relationship to the Improvement Loop

This section feeds **Stage 1** of the Improvement Loop. The Propose phase acts as **Stage 1.5** — reading the KB and generating proposals (written to Improvement Proposals) before the evaluate/enhance/review stages run.

---

## Findings Page Structure

Each Research Finding entry has a full page body with:

- **What it is** — the pattern/technique distilled
- **Why it matters** — the problem it solves
- **Why people are using it** — adoption signals and practitioner evidence
- **Potential alternatives** — (optional) other approaches solving the same problem differently
- **Potential improvements** — where the pattern could evolve
- **Potential failure modes** — how it could go wrong in practice

The tone is concise and distilled — essence, not exhaustive detail. The Proposer agent may do its own follow-up research on implementation specifics.
