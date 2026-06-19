---
title: "Boundary Rules — IL Governance"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-19"
updated: "2026-04-22"
author: "agent"
source_governance:
  - "CHARTER.md"
source_sections:
  - "Boundary Rules"
  - "Ownership Matrix"
  - "The Three Systems"
  - "DD-89 (four-zone artifact placement)"
tags:
  - "governance"
  - "improvement-loop"
  - "boundaries"
  - "four-zone"
---

# Boundary Rules — IL Governance

> Derived from: Charter (`CHARTER.md`), DD-89 (four-zone architecture)
> Last reconciled: 2026-04-22

## Rules

1. **The pipeline agents modify only engine files.** The research pipeline's write scope is limited to the `systems/improvement-loop/` directory tree and its engine directories (`.claude/skills/` under the engine, `.claude/agents/` subagent definitions). Never modify files under `archive/` or `incubator/`. Workspace-root config and the charter are Owner-stewarded (proposal-first), not pipeline-agent territory.
   - *Source:* Charter; Owner Constitution — Boundaries

2. **Research KB is engine-owned.** Findings, sources, authorities, watched-libraries, watched-blogs, and extracts are engine operational data. They do not belong at workspace root.
   - *Source:* DD-41

3. **IL does not modify Notion schema or operations.** Schema changes go through Claude Build. Notion operations go through Household OS agents. IL has no Notion write access.
   - *Source:* Constitution — Boundary Rules, rules 1-2

4. **Cross-system changes require human authorization.** If IL discovers a problem in another system, the Owner flags it — never fixes it directly. Nick routes the fix to the appropriate system.
   - *Source:* Constitution — Boundary Rules; Owner Autonomy Table — Human-Required tier

5. **IL is self-improving within its scope.** IL can evolve its own agents, skills, governance, and pipeline. But changes to how IL interacts with other systems (interface contracts, shared artifacts) require human authorization.
   - *Source:* Constitution — Ownership Matrix (IL: "Self-improving via research cycle")

6. **Nick is the bridge for external feedback.** IL does not receive automated feedback from Household OS or Claude Build. Nick observes, translates observations into IB items or feedback, and feeds them to IL.
   - *Source:* Constitution — Boundary Rules, rule 3; Feedback Loop diagram

7. **Artifact placement by shape, not author role.** IL has four zones for design-and-governance artifacts. Deliberative specifications (substrate audits, read contracts, use-case registries, acceptance rubrics, lifecycle specs, spot-checks, tracking-mechanism specs) go to `project-management/design-notes/`. Agent-initiated proposals (from `/solicit-proposals` rounds or ad-hoc) go to `governance/proposals/`. Ratified governance rules go to `governance/` root. Runtime event output (SL entries, handoffs, research-reports, loop-reports, identification reports, extraction reports) goes to `operations/`. `operations/design-notes/` does not exist (deprecated 2026-04-22). Owner + Nick collaborative governance work writes DDs directly and does not pass through `governance/proposals/`.
   - *Source:* DD-89 (four-zone architecture) — artifact shape governs placement; author role is a heuristic, not authority.

## Applicability Notes

These rules apply to all IL agents (Owner, Researcher, Codifier, Librarian) and all IL skills. The Owner agent is responsible for enforcing boundary awareness — if a skill or agent action would cross a boundary, the Owner flags it. Artifact-placement questions route through Rule 7's shape-determines-zone mapping; when in doubt about placement, the Owner adjudicates against DD-89.
