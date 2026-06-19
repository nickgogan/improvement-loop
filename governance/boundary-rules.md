---
title: "Boundary Rules — IL Governance"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-19"
updated: "2026-06-18"
author: "agent"
source_governance:
  - "CHARTER.md"
source_sections:
  - "Boundary Rules"
  - "Ownership Matrix"
  - "DD-89 (four-zone artifact placement)"
  - "DD-103 / DD-106 (single-engine collapse; Household OS → Notion consumer)"
tags:
  - "governance"
  - "improvement-loop"
  - "boundaries"
  - "four-zone"
---

# Boundary Rules — IL Governance

> Derived from: Charter (`CHARTER.md`), DD-89 (four-zone architecture)
> Last reconciled: 2026-06-18 (post-collapse: rules 3–6 updated for single-engine, Household-OS-on-Notion)

## Rules

1. **The pipeline agents modify only engine files.** The research pipeline's write scope is limited to the `systems/improvement-loop/` directory tree and its engine directories (`.claude/skills/` under the engine, `.claude/agents/` subagent definitions). Never modify files under `archive/` or `incubator/`. Workspace-root config and the charter are Owner-stewarded (proposal-first), not pipeline-agent territory.
   - *Source:* Charter; Owner Constitution — Boundaries

2. **Research KB is engine-owned.** Findings, sources, authorities, watched-libraries, watched-blogs, and extracts are engine operational data. They do not belong at workspace root.
   - *Source:* DD-41

3. **The engine does not write to consumer systems.** Household OS now lives in Notion (DD-106) as a consumer the engine helps *design*, not a peer it operates — the engine has no Notion write access and runs no Notion operations. Claude Build is retired (DD-103); there is no separate schema-owning system to route changes through.
   - *Source:* DD-103, DD-106; Charter — consumer boundary

4. **Issues in consumer systems are flagged, not fixed.** If the engine discovers a problem in a system it helps design (e.g. the Notion Household OS), the Owner flags it for Nick — it never modifies the consumer directly.
   - *Source:* Charter; Owner Autonomy Table — Human-Required tier

5. **The engine is self-improving within its scope.** It can evolve its own agents, skills, governance, knowledge, and pipeline. But changes to how it interfaces with consumer systems (contracts, shared artifacts) require human authorization.
   - *Source:* Charter — self-evolving engine; Ownership Matrix

6. **Nick is the bridge for external feedback.** The engine does not receive automated feedback from consumer systems. Nick observes, translates observations into IB items or `feedback/` entries, and feeds them in.
   - *Source:* Charter; Feedback Loop

7. **Artifact placement by shape, not author role.** IL has four zones for design-and-governance artifacts. Deliberative specifications (substrate audits, read contracts, use-case registries, acceptance rubrics, lifecycle specs, spot-checks, tracking-mechanism specs) go to `project-management/design-notes/`. Agent-initiated proposals (from `/solicit-proposals` rounds or ad-hoc) go to `governance/proposals/`. Ratified governance rules go to `governance/` root. Runtime event output (SL entries, handoffs, research-reports, loop-reports, identification reports, extraction reports) goes to `operations/`. `operations/design-notes/` does not exist (deprecated 2026-04-22). Owner + Nick collaborative governance work writes DDs directly and does not pass through `governance/proposals/`.
   - *Source:* DD-89 (four-zone architecture) — artifact shape governs placement; author role is a heuristic, not authority.

## Applicability Notes

These rules apply to all IL agents (Owner, Researcher, Codifier, Librarian) and all IL skills. The Owner agent is responsible for enforcing boundary awareness — if a skill or agent action would cross a boundary, the Owner flags it. Artifact-placement questions route through Rule 7's shape-determines-zone mapping; when in doubt about placement, the Owner adjudicates against DD-89.
