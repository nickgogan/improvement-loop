---
name: Domain Expertise as Loadable Context Sub-Skill
summary: 'Domain knowledge (macOS, iOS, n8n) lives in skills/expertise/[domain]/SKILL.md with a references_index that maps planning phase types to specific reference files. Selective loading achieves 8-12k
  tokens vs 20-27k for full load. The pattern is extensible: a meta-skill can generate new domain expertise sub-skills for unfamiliar domains.'
implementation_notes: MetaSystem's research dimensions and Librarian reference layer serve a similar function but are not structured as loadable sub-skills. This pattern suggests packaging domain expertise
  as skill directories with explicit reference indices — selected per-task rather than loaded monolithically.
category: Context Engineering
evidence_strength: Anecdotal
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- taches-claude-code-resources-commands-skills-thinki.md
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-05-24'
related_findings:
- file: skill-as-package-export-with-references.md
  rel: extends
- file: task-to-file-routing-table-in-context-files.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
pipeline_status: raw
tags:
- context-engineering
- skills
- claude-code
---

# Domain Expertise as Loadable Context Sub-Skill

## What It Is

Domain knowledge packaged as skill directories under `skills/expertise/[domain]/SKILL.md`. Each domain skill contains a `references_index` that maps planning phase types (e.g., "UI implementation", "API design") to specific reference files within the skill. The planning skill selectively loads only the references relevant to the current phase, achieving 8-12k tokens vs 20-27k for full domain load.

## Why It Matters

Domain expertise is expensive context — loading everything wastes tokens on irrelevant material. The references_index pattern creates a routing table from task type to relevant domain knowledge. The pattern is also self-extending: a meta-skill (`create-agent-skills`) can generate new domain expertise sub-skills for unfamiliar domains by researching and structuring the knowledge.

## How It Could Fail

The references_index requires upfront classification of which domain knowledge applies to which phase types. Misclassification means the wrong references are loaded. For small domains, the overhead of maintaining a structured sub-skill may exceed the token savings.
