---
name: "Core/Specialized Skill Inheritance Pattern"
summary: "Skills declare a 'specializes' field linking to a core skill from a shared repository. Core skills define categories that are overridable; specialized (local) skills only customize those declared slots. Enables shared skill logic across many repos with per-repo behavioral customization — without forking or duplicating the core skill."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P1 (Implement Now)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "progressive-skill-loading.md"
    rel: "extends"
  - file: "domain-expertise-as-loadable-context-sub-skill.md"
    rel: "same-problem"
  - file: "four-layer-config-merge-with-customization-sidecar.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-24"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "agent-design-patterns.md"
  - "templates/core-specialized-skill-pair-spec.md"
---

# Core/Specialized Skill Inheritance Pattern

## Pattern

A two-layer skill architecture with explicit inheritance:

**Core skills** (shared `common-skills` repo):
- Define the full skill contract (output schema, safety rules, evidence rules)
- Declare specific categories as "overridable" by specializations
- Portable across all repos that install them

**Specialized skills** (per-repo `.agents/skills/`):
- Declare `specializes: <core-skill-name>` in frontmatter
- Override only the declared-overridable categories
- Cannot redefine the core contract (schema, safety, follow-up rules)
- Provide repo-specific heuristics, label taxonomies, style patterns

Example from Warp:
```yaml
name: triage-issue-local
specializes: triage-issue
description: Repo-specific triage guidance for warp. Only the categories declared overridable by the core triage-issue skill may be specialized here.
```

## Why It Matters

Solves the skill portability vs customization dilemma. Without this pattern, teams either:
- Copy skills per-repo (divergence, maintenance burden)
- Use one global skill (can't handle repo-specific needs)

The core/specialized split provides a middle path: shared logic stays shared, customization is scoped and auditable, and the contract about what CAN be customized is explicit.

## How It Could Fail

- Core skill's "overridable" contract becomes too restrictive (specializations can't do what they need)
- Version drift between core and specialized skills
- No enforcement that specializations stay within declared override slots
- Complex resolution logic when core + specialized both contribute content

## Evidence

Warp (warpdotdev/warp) — 15 skills in `.agents/skills/`, multiple using `specializes` field (triage-issue-local, review-pr-local, dedupe-issue-local, reproduce-bug-report-local). Core skills managed in separate `common-skills` repo with `skills-lock.json` versioning. Production-tested at scale (thousands of Oz agent sessions publicly visible at build.warp.dev).
