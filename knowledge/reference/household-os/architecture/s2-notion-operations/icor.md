---
notion_id: 30f1e08b-9b34-80c9-9c31-cf91aaac7613
title: "ICOR"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# ICOR

> **For agents:** ICOR (Input, Control, Output, Refine) is the meta-framework for this entire system. Per DD-01, all other methodologies nest within ICOR stages. When processing any item, identify which ICOR stage it belongs to and apply the relevant sub-framework. See the Architecture section for detailed mappings.

## What is ICOR?

**ICOR** stands for **Input, Control, Output, Refine** — a productivity methodology created by Dr. Thomas Roedl (Tom Solid) and Paco Cantero of the Paperless Movement. It is built on **systems theory**, meaning it views your entire productivity setup as one interconnected organism rather than separate tools doing separate jobs.

In our Household Operating System, ICOR serves as the **meta-framework** that unifies PARA, CODE, OKR, GTD-Lite, Zettelkasten, and OODA into a single coherent architecture (Design Decision DD-01).

---

## The Four Stages

### Input

Gathering information from the external environment into your system. Defines sources, what to capture, how, and where. Guarded by **The Capturing Beast** — a 3-lens filter that prevents information overload.

*Sub-frameworks active:* CODE Capture, Zettelkasten fleeting notes, OODA Observe

### Control

Processing captured information into decisions. The bridge from information to action. "Act on it or Think about it" — route to execution or to knowledge storage.

*Sub-frameworks active:* GTD-Lite Clarify/Organize, CODE Organize, PARA routing, OODA Orient/Decide, **Family Meeting** (primary shared ritual — DD-08)

### Output

Executing tasks and projects to generate tangible results. Structured by **The Execution Beast** — a five-tier hierarchy (Goal → Project → Workstream → Operation → Task/Speedy) governed by the PEA rhythm (Plan, Execute, Align).

*Sub-frameworks active:* OKR cascade, GTD-Lite Engage, CODE Express, OODA Act

### Refine

Continuously improving the system itself — not just individual components but the interactions between them. This is what makes ICOR a *systems* framework.

*Sub-frameworks active:* GTD-Lite Weekly Review (personal), Health Monitoring, Quarterly OKR scoring

---

## Four Domains

ICOR further divides the productivity spectrum into four domains:

| Domain | Scope |
|--------|-------|
| **PKM** | Personal Knowledge Management — individual learning, notes, references |
| **PPM** | Personal Project Management — individual tasks, goals, execution |
| **HKM** | Household Knowledge Management — shared family knowledge, procedures |
| **HPM** | Household Project Management — shared family projects, coordination |

---

## Tool Classification

ICOR classifies tools by role:

| Type | Definition | Our System |
|------|-----------|------------|
| **Core App** | Where most work happens. The SSOT. | Notion |
| **Satellite App** | Extends the Core for specialized functions. | Google Workspace, Heptabase |
| **Utility App** | Single-purpose tools. | Scanner, password manager |
| **AI Layer** | Intelligence tools mapped to ICOR stages. | Perplexity (Input/Refine), Notion AI (Control/Output), Claude (Output/Refine) |

---

## Single Source of Truth (SSOT)

Also called Source of Truth (SOT) or System of Record (SOR). The definitive reference point for both action and information storage and retrieval. In our system, **Notion** is the SSOT.

---

## Key Design Decisions

The following binding decisions govern how ICOR operates in our system:

- **DD-01**: ICOR is the meta-framework; all others nest within it
- **DD-02**: PARA provides the universal organizational taxonomy across all stages
- **DD-03**: CODE maps to ICOR stages (Capture→Input, Organize→Control, Distill→Control/Output, Express→Output)
- **DD-04**: OODA is ICOR at micro-scale, not a separate framework
- **DD-05**: GTD-Lite provides execution methodology within Output
- **DD-08**: Family Meeting is the primary Control ritual

For the full set of design decisions, see the Design Decisions database in the Architecture section.

---

---

## Companion Diagrams

The following diagrams in the workspace folder visualize ICOR concepts:

- `D1_System_Architecture.svg` — The four ICOR columns with framework placements, PARA Areas, and tool ecosystem
- `D2_ICOR_Flow_Integration.svg` — Left-to-right information flow through all stages, showing the Beasts and feedback paths
- `KnowledgeActionLoop.svg` — The knowledge-action feedback loop: how knowledge formation in Control feeds back into Output execution
- `DecisionLoop.png` — John Boyd's original OODA Loop reference (the micro-scale pattern that DD-04 says ICOR embodies)

---

*Deep-dive resources:* Architecture → Framework Integration Map · The Capturing Beast · The Execution Beast · Vocabulary
