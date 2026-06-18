---
name: SKILL.md Anatomy Convergence — 20 of 29 Repos
summary: SKILL.md has converged as a de facto standard across 20/29 analyzed repos with common anatomy (YAML frontmatter + structured body + optional references/). The base pattern is settled. Remaining
  innovation space is in four areas — inheritance (Warp), progressive disclosure (CrewAI), workflow decomposition (BMAD, TACHES), and self-improvement (OB1, Hermes).
implementation_notes: null
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in:
- MetaSystem IL skills (SKILL.md pattern)
sources: []
related_findings:
- file: progressive-skill-loading.md
  rel: extends
- file: skill-as-package-export-with-references.md
  rel: extends
- file: skill-self-improvement-three-approaches.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: raw
consumed_by: []
---

## What It Is

SKILL.md is now the most widely adopted convention in the agentic ecosystem — 20 of 29 analyzed repos use it (69%), more universal than AGENTS.md which has more naming variations. Common anatomy:

- **YAML frontmatter:** name, description, triggers/argument-hint, allowed-tools
- **Structured body:** instructions/cognitive-disposition, procedure/steps, output format, rules
- **Optional extensions:** `references/` directory, workflow sub-files, templates

The base pattern is settled. Remaining innovation happens in four areas:

1. **Inheritance** (Warp) — `specializes` field for skill hierarchy, child skills inherit parent context
2. **Progressive disclosure** (CrewAI) — METADATA → INSTRUCTIONS → RESOURCES three-level loading based on context budget
3. **Workflow decomposition** (BMAD, TACHES) — Complex procedures split into step-files or workflow sub-files for readability
4. **Self-improvement** (OB1, Hermes) — Skills that track their own success rate and evolve their instructions based on outcomes

## Why It Matters

The convergence signal (69% adoption) means SKILL.md is a safe bet for any agent system. Research value in the base pattern is zero — it's infrastructure. The remaining innovation areas (inheritance, progressive disclosure, decomposition, self-improvement) are where investment should focus. Of these, progressive disclosure and self-improvement are the most underexplored in MetaSystem's current implementation.

## Why People Are Using It

Observed across 20 repos in the cross-repo structural comparison — see [[cross-repo-comparison]] for details. The pattern succeeds because it balances human-readability (markdown), machine-parseability (YAML frontmatter), and composability (directory-as-package). It's the skill equivalent of what package.json is for Node modules.

## Potential Alternatives

| Alternative | When to Prefer |
|---|---|
| Code-defined skills (Python decorators) | When skills need runtime parameterization |
| JSON/YAML-only definitions | When human-readability isn't needed |
| Convention-based (directory structure only) | When frontmatter overhead isn't justified |

## Potential Improvements

- Adopt progressive disclosure (three-level loading) for MetaSystem's larger skills to reduce context cost
- Evaluate inheritance/specialization for skill families that share common setup
- Investigate self-improvement mechanisms for skills with measurable success criteria

## Potential Failure Modes

- Skills growing unboundedly without decomposition (>500 lines of instructions becomes unmanageable)
- Frontmatter schema diverging across tools/harnesses (already happening: allowed-tools vs tools vs capabilities)
- Self-improvement creating drift from original intent without governance
