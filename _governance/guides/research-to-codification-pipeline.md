---
title: "Research-to-Codification Pipeline"
id: "research-to-codification-pipeline"
type: "guideline"
category: "knowledge-management"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-07"
updated: "2026-04-19"
author: "nick"
source_dd:
  - "DD-45"
  - "DD-46"
  - "DD-29"
  - "DD-65"
  - "DD-80"
tags:
  - "guide"
  - "knowledge-management"
  - "improvement-loop"
  - "codification"
  - "meta-system"
aliases:
  - "How findings become patterns"
  - "Codification pipeline"
  - "Research to artifacts"
---

# Research-to-Codification Pipeline

How research findings in the Improvement Loop become actionable artifacts in meta-system's knowledge layer. This is the bridge between "we learned something" and "our systems can use it."

## The Pipeline

```
Research KB (IL)  -->  Identification Report (IL)  -->  Extracted Artifacts (IL)  -->  Deployed Artifacts
  findings/             research-reports/                    extracts/           meta-system / .claude/
       |                        |                                |                           |
  research-loop          identify-artifacts               extract-artifacts           deployment (manual)
       |                        |                                |                           |
  [human gate]            [human gate]                    [human gate]                 [human gate]
```

Four stages, four human gates (DD-29). No autonomous deployment — Nick decides what gets deployed, in what form, and where.

**Pipeline simplification (DD-80):** The Proposer stage (`/research-proposer` -> `improvement-proposals/`) was eliminated in session 23. Classification and drafting are split into two skills: `/identify-artifacts` (lightweight, Sonnet-parallelizable) and `/extract-artifacts` (drafts from approved report). See DD-80 for rationale.

## Stage 1: Research Intake

**Skill:** `/research-loop`
**Input:** URLs (papers, videos, blog posts), periodic web scans, arXiv scans
**Output:** Research Findings in `systems/improvement-loop/research-findings/`

Each finding is a named pattern with:
- Evidence strength (Strong / Medium / Weak)
- Proposer priority (P1 / P2 / P3 / Not Flagged)
- Category (Context Engineering, Prompt Craft, Tool Integration, etc.)
- Adoption status (Already Adopted / Partially Adopted / Not Yet Started)

**What happens here:** Raw sources are processed into structured findings. One canonical finding per pattern — new sources update existing findings, not create duplicates. The research-loop is neutral on adoption; it flags priority and evidence, not recommendations.

**Human gate:** Review findings. Adjust priorities. Flag anything that needs deeper investigation or immediate attention.

## Stage 2: Artifact Identification

**Skill:** `/identify-artifacts`
**Input:** Research Findings (filtered by priority, evidence strength, category)
**Output:** Identification report in `systems/improvement-loop/operations/research-reports/`

Each classified finding gets:
- Assigned form (pattern / skill / rule / template / agent) — classified via the Form Router rubric
- Confidence level and tier (auto / guided / hitl)
- Reason codes and rationale
- Co-occurrence notes (secondary forms embedded in primary)

**What happens here:** `/identify-artifacts` reads findings and classifies each into one of 5 forms using the rubric (`systems/improvement-loop/operations/references/form-classification-rubric.md`). Classification is parallelized via Sonnet subagent batches. No artifact drafting — output is a structured report.

**Human gate:** Review the identification report. Set Status to APPROVED / REJECTED / REDIRECTED per finding. Redirect allows changing the assigned form before extraction.

## Stage 3: Artifact Extraction

**Skill:** `/extract-artifacts`
**Input:** Approved identification report
**Output:** Staged artifacts in `systems/improvement-loop/extracts/{form}/`

Each extracted artifact specifies:
- Form-appropriate body (pattern: problem/forces/solution; rule: condition/action/boundary; etc.)
- ContractSpec (DD-78): preconditions, invariants, governance, recovery
- Source finding traceability and identification report reference

**What happens here:** `/extract-artifacts` reads an approved identification report, reads the full finding files for approved entries, and drafts form-appropriate artifacts. Drafting can use a smarter model since the set is smaller (only approved findings). Artifacts are staged in IL — not deployed to enforcement locations.

**Human gate:** Review staged artifacts before deployment.

### Artifact Type Selection

The Form Router rubric classifies findings by level of abstraction:

| If the finding describes... | It becomes... | Staged in... |
|------------------------------|---------------|-------------|
| A reusable design approach (philosophy, forces, tradeoffs) | **Pattern** | `extracts/patterns/` |
| A step-by-step procedure with inputs/outputs | **Skill** | `extracts/skills/` |
| A binary constraint enforced at a boundary | **Rule** | `extracts/rules/` |
| A scaffold with named variables and a body | **Template** | `extracts/templates/` |
| A persona with cognitive disposition and durable scope | **Agent** | `extracts/agents/` |
| Not actionable yet — interesting but premature | **Stays as finding** | `research-findings/` at P3 (Monitor) |

**Out of scope for extraction:** Guides are synthesis-layer artifacts produced by `/synthesize-guide` (IB-146) from aggregated patterns.

Use the [[capability-type-selection]] pattern to distinguish between agents, skills, workflows, hooks, and rules.

## Stage 4: Deployment

**Currently:** Manual — Nick moves artifacts from `extracts/` to their deployment targets.
**Future:** Could become a `/deploy-artifact` skill.

| Artifact Form | Deployment Target |
|---------------|-------------------|
| Pattern | `meta-system/knowledge/patterns/` |
| Skill | `.claude/skills/` or `{system}/.claude/skills/` |
| Rule | `.claude/rules/` or `{system}/governance/` |
| Template | `meta-system/knowledge/templates/` |
| Agent | `meta-system/knowledge/templates/agent-templates/` |

### Artifact Quality Bar

A deployed artifact must be:
- **Self-contained** — readable without needing to trace back to the original finding
- **Actionable** — a reader (human or agent) can apply it without further research
- **Scoped** — clear about what systems it applies to and what it doesn't cover
- **Linked** — references the source findings and DDs that motivated it
- **Contracted** — carries a ContractSpec (DD-78) with preconditions, invariants, governance, recovery

If you can't write it to that bar, it's not ready for deployment. Leave it staged in `extracts/`.

### After Deployment

1. Update the artifact's `deployed` flag in `extracts/`
2. Update the finding's `adoption_status` to "Already Adopted" or "Partially Adopted"
3. Update the relevant `_index.md` catalogs
4. If the artifact creates new constraints, consider whether it warrants a DD

## How Systems Consume Deployed Artifacts

Per DD-46: **MetaSystem does not push work to systems — systems pull what's relevant.**

- **Nick and JR** browse the knowledge layer in Obsidian (graph view, Dataview queries)
- **Agents** read files via Glob/Grep/Read; parse frontmatter for filtering
- **Skills** reference patterns and guides in their procedures
- **Bootstrap** uses templates to scaffold new projects

A pattern in `meta-system/knowledge/patterns/` is a reference document. It becomes operational when a system creates a skill, agent, or configuration that implements it.

## Upstream Dependencies

When a codified artifact derives from an external package (GSD, gstack, BMAT, etc.), the [[upstream-dependency-spectrum]] pattern applies:

- Record the upstream source in the artifact's metadata or body
- Track the upstream project in the watched-libraries registry
- When upstream changes, triage based on spectrum position (cherry-pick / thin-wrapper / wholesale)

## Current State

| Layer | Status |
|-------|--------|
| Research intake (`/research-loop`) | Working — KB populated (check `_index.md` files for current counts) |
| Artifact identification (`/identify-artifacts`) | Skill built, not yet run against KB |
| Artifact extraction (`/extract-artifacts`) | Skill built, not yet run against KB |
| Deployment | Manual. Two patterns exist (capability-type-selection, upstream-dependency-spectrum). Templates, guides, and agent-templates directories are empty or near-empty. |

The bottleneck is extraction and deployment. The IL has material; meta-system's knowledge layer needs to be populated from it.

## Archived: Proposal Stage

The Proposer stage (`/research-proposer` skill, `improvement-proposals/` directory) was active from session 6 through session 22. Six proposals were generated (2026-03-23) but the intermediate document added no value beyond what the finding itself contained. DD-80 formalized this simplification. The 6 existing proposals are preserved as historical artifacts.

## Related

- [[upstream-dependency-spectrum]] — How to position external dependencies on the cherry-pick/adopt spectrum
- [[capability-type-selection]] — How to choose between agent, skill, workflow, hook, and rule
- DD-45: Knowledge layer architecture
- DD-46: Knowledge flow pipeline (IL produces, meta-system codifies, systems consume)
- DD-29: Human gates in the improvement pipeline
- DD-80: Pipeline simplification (Proposer stage eliminated)
