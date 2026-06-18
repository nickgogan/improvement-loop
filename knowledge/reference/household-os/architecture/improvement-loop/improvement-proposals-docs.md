---
notion_id: 32b1e08b-9b34-81b1-b124-dfa47e49116f
title: "Improvement Proposals"
parent: "Improvement Loop Architecture"
extracted: "2026-04-04"
---

# Improvement Proposals

> **For agents:** This is the Proposer's workspace. The Proposer reads from the AI Research KB (Research Findings, Sources, Authorities) and writes proposals here. It does NOT modify the Research KB or any other system without human approval.

---

## Purpose

Concrete, actionable proposals for improving S2 (Notion Operations), S3 (Claude Code Build), and Perplexity Skills — derived from patterns in the AI Research Knowledge Base.

---

## Access Model

| Scope | What | Access |
|---|---|---|
| **Read** | Research Findings DB, Research Sources DB, Research Authorities DB (under AI Research) | Read-only — never modify these |
| **Read** | Current system state (CLAUDE.md, S2 agent configs, Perplexity skills) | Read-only — fetch for diffing |
| **Write** | Improvement Proposals DB (below) | Full write — create and update proposals |

---

## Workflow (v2)

The Proposer runs a six-phase pipeline. All phases run by default; the user may request a partial run (e.g., "stop after phase 3") for early conflict review.

1. **Scope Determination** — Query findings by priority/category/name. Use each finding's Applicability to build a scope map of which DDs, Architecture pages, and vault files to read. Max 8-10 system documents per run.
2. **System State Reading** — Fetch only the scoped system documents. Extract current design decisions, patterns, and "we chose X over Y" constraints.
3. **Grouping & Conflict Analysis** — Group findings by theme. Identify synergistic, independent, dependent, and conflicting relationships. Classify each as one-way or two-way door.
4. **Cost & Complexity Assessment** — Estimate implementation complexity, operational impact (reduces/neutral/adds ops burden), and net value signal.
5. **Proposal Generation** — Write enriched proposals to this DB with conflict flags, door types, and full page body analysis.
6. **Summary** — Report to user: proposals created, conflicts found, high-risk items flagged, review recommendations.

---

## Relationship to AI Research

This page is a sibling to [AI Research](ai-research.md) under Improvement Loop Architecture. The Research KB is the knowledge layer; this is the action layer. The Proposer Priority field in Research Findings is the handoff mechanism — findings flagged P1/P2 flow here as proposals.
