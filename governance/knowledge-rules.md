---
title: "Knowledge Rules — IL Governance"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-19"
updated: "2026-04-19"
author: "agent"
source_governance:
  - "systems/meta-system/governance/constitution.md"
  - "systems/meta-system/governance/values.md"
  - "systems/meta-system/governance/vocabulary.md"
source_sections:
  - "Design Philosophy (knowledge serves expression)"
  - "Core Principles (start lean, refine later)"
  - "Pipeline vocabulary"
tags:
  - "governance"
  - "improvement-loop"
  - "knowledge"
  - "research"
---

# Knowledge Rules — IL Governance

> Derived from: Constitution, Values (`systems/meta-system/governance/values.md`), Vocabulary (`systems/meta-system/governance/vocabulary.md`)
> Last reconciled: 2026-04-19

## Rules

1. **Knowledge serves expression.** Every research finding, extracted pattern, and staged artifact must serve a downstream purpose — informing a design decision, improving an agent's behavior, or enabling a new capability. Findings that don't lead somewhere are dead weight. Prune or deprioritize them.
   - *Source:* Values — "Knowledge serves expression"

2. **One canonical entry per pattern.** Deduplication is intellectual honesty. When a new source covers something already in the KB, update the existing finding rather than creating a new one. The Researcher enforces this during extraction; the Owner checks during audits.
   - *Source:* Vocabulary — Research Finding; Researcher Cognitive Disposition

3. **Evidence strength is tracked, not inflated.** Every finding carries an `evidence_strength` field: Strong (production-tested), Medium (practitioner-documented), Weak (theoretical). Academic papers default to Weak. Don't upgrade evidence strength without production-tested evidence.
   - *Source:* Vocabulary — Proposer Priority; Research Loop calibration notes

4. **Start lean, refine later.** New KB entries, governance docs, and agent definitions should be minimal viable versions. Don't over-engineer the first draft. Complexity is earned through use, not anticipated in design.
   - *Source:* Values — "Start lean, refine later"

5. **Terminology is governed.** Use terms as defined in `vocabulary.md`. When IL introduces system-specific terms, they complement — not contradict — the cross-system vocabulary. Key terms: Research Finding, Improvement Proposal, Proposer Priority, Cognitive Disposition, Human Gate.
   - *Source:* Vocabulary — all sections

6. **Frontmatter is the query interface.** All KB entries carry YAML frontmatter defined in `_schema.yaml`. This enables Obsidian Dataview queries, agent filtering, and future MongoDB backing. Missing or malformed frontmatter is an audit finding.
   - *Source:* Fractal Pattern — "All Content Files Use Vault Frontmatter"

7. **Structural memory over conversation memory.** Everything learned is captured in files with frontmatter, not in conversation history. Agents are stateless across sessions — they re-read system state each time. If it's not in a file, it doesn't exist.
   - *Source:* Values — "Structural memory"; Owner Constitution — Continuity

## Applicability Notes

These rules govern how the IL manages its knowledge base (research-findings, research-sources, research-authorities) and how knowledge flows through the pipeline. The Researcher creates knowledge; the Codifier refines and classifies it; the Librarian queries it; the Owner ensures it stays consistent and useful.
