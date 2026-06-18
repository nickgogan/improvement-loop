---
notion_id: "3251e08b-9b34-8197-967f-e07f13f62500"
title: "Four-System Separation Model"
parent: "Architecture"
extracted: "2026-04-04"
---

> **For agents:** This page defines the Build/Operate separation. If you are an S2 operator agent, you read schema but never modify it. If you are reading this as S3, you own schema changes.

---

## Overview

The Household Operating System is governed by four distinct systems with clear ownership boundaries. This separation was decided on March 16, 2026, and supersedes the earlier "Three-Layer Architecture" and "Builder vs. Operator" framing.

---

## System Definitions

| System | Nature | Primary Owner | Runtime |
|---|---|---|---|
| **S1: Notion Schema** | Shared artifact | S3 produces; Nick approves | Notion workspace |
| **S2: Notion Operations** | Running system | Custom Agents + Nick + JR | Notion + Slack |
| **S3: Claude Code Build** | Running system | Nick via Cursor/Claude Code | Local dev env |
| **S4: Bootstrap** | First-run path within S3 | Nick (once), JR (once) | Local dev env |

---

## Boundary Rules

1. **S2 reads and writes data within S1 schema.** S2 never modifies schema (no creating databases, no adding properties, no changing views).
2. **Schema changes only through S3** via Build Specs with Review Gates. Every structural modification goes through the Claude Code Build system.
3. **Nick is the bridge between S2 and S3.** No automated feedback loop exists. Nick observes S2 operations, translates observations into IB items, and feeds those to S3.
4. **JR's primary interface is S2** (Notion UI + Slack). JR has git access to the shared Tier 2 repo for browsing vault content, but does not operate S3.

---

## Ownership Matrix

| System | Created by | Operated by | Maintained by | Evolved by |
|---|---|---|---|---|
| **S1: Notion Schema** | S3 (Claude Code) | S2 (agents + humans) | S3 (schema changes) | S3 (via IB items from Nick) |
| **S2: Notion Operations** | S3 (agent configs) | Custom Agents + Nick + JR | Nick (monitors, tunes) | S3 (via Improvement Loop) |
| **S3: Claude Code Build** | Nick (vault setup) | Nick via Cursor | Nick + Improvement Loop | Improvement Loop + Nick |
| **S4: Bootstrap** | Nick (skill files) | Nick (once), JR (once) | Nick | Folded into S3 after first run |

---

## Architecture Diagram

```
S3: CLAUDE CODE BUILD          S2: NOTION OPERATIONS
(Running system)               (Running system)
  | WRITES schema                | READS schema
  | (MCP tool calls)             | WRITES data
  v                              v
  S1: NOTION SCHEMA (Shared Artifact)
  42 DDs, 112+ IB items, databases, views, templates

S4: BOOTSTRAP -- First-run path within S3
FEEDBACK LOOP: S2 -> Nick (observes) -> IB items -> S3
```

---

## Implementation Phases

| Phase | Goal | Status |
|---|---|---|
| **Phase A** | Validate S3 -- run first Claude Code build session using vault + MCP | Next |
| **Phase B** | Design S2 Agent Architecture -- Custom Agents (free through May 3, 2026) | Planned |
| **Phase C** | Build S2 via S3 -- use Claude Code to configure and deploy Custom Agents | Planned |
| **Phase D** | Retire Handoff Prompt -- archive after content redistributed to S2 and S3 | Planned |

---

## Teamspace Layers (DD-42)

The four systems above describe ownership and runtime boundaries. DD-42 (Operational Database Placement) adds a complementary structural model for how content is organized in the Household Teamspace:

| Layer | Purpose | Examples |
|---|---|---|
| **Operational/Runtime (UB3)** | Where humans and agents do daily work | Tasks, Projects, Goals, Notes |
| **Governance Infrastructure** | Cross-system databases tracking architectural state | DD DB, IB DB, Improvement Proposals DB |
| **Design-Time Reference** | Architecture docs, decision specs, governance | This page, System Governance, S2/S3/IL Architecture |

The four systems (S1-S4) and three Teamspace layers are orthogonal: S2 and S3 both contribute to all three layers, while the layers describe where artifacts live structurally.

---

## Companion Document

The full analysis (20 pages) lives as **four-system-architecture.pdf** in Google Drive. That document contains the detailed boundary pair analysis, interface contracts, Handoff Prompt section mapping, and decision matrix.

---

## Provenance

This page was created from the reconciliation of the v6 Migration Intelligence Report, the Four-System Architecture document, and a live Notion workspace audit conducted on March 16, 2026.
