---
notion_id: 32b1e08b-9b34-818c-bcf7-cc890774a399
title: "IL Skill Catalog"
parent: "Improvement Loop Architecture"
extracted: "2026-04-04"
---

# IL Skill Catalog

> **For agents:** This page lists all skills in the Improvement Loop. Each skill follows the pattern defined in Skills Layer Architecture. For the pipeline these skills execute, see Pipeline Architecture.

---

| Skill | Status | Purpose | Cognitive Disposition |
|---|---|---|---|
| **research-loop** | Operational | Scans for emerging best practices across five dimensions. Writes to Research Sources, Findings, and Authorities DBs. | Skeptical, evidence-focused. Neutral on implementation. |
| **research-proposer** | Operational | Reads findings, diffs against current system state, generates improvement proposals with conflict detection. | Pragmatic, system-aware. Opinionated on trade-offs. |
| **prompt-evaluator** | Operational | Evaluates prompts against four-discipline rubric. Produces scorecards. | Analytical, standards-focused. |
| **prompt-enhancer** | Operational | Transforms evaluation output into concrete prompt rewrites. | Creative, precision-focused. |
| **research-codifier** | Planned | Takes approved proposals and codifies them as governing practices under System Governance. | TBD |
| **system-applicator** | Future | Takes codified practices and applies them to a target system's skills and configs. | TBD — one mode per target system |

Each skill's full specification (Access Model, Scope Boundary, detailed Cognitive Disposition) lives in its skill file and will be linked here once formalized.
