---
name: "Skill Shipped Inside the Package Wheel, Release-Gated with the Code"
summary: |-
  Plain English: a library can ship the coding-agent skill that teaches agents how to
  use it INSIDE its own distribution artifact, so the skill version always matches the
  installed library version — and gate releases on keeping that skill current. Pydantic
  AI packages `building-pydantic-ai-agents` (SKILL.md + 11 progressive-disclosure
  reference docs) inside the pip wheel at
  `pydantic_ai_slim/pydantic_ai/.agents/skills/`, installable into consumers' coding
  agents via library-skills.io, the Claude plugin marketplace, or agentskills.io. The
  repo's CLAUDE.md requires feature PRs to update the skill — documentation-as-dependency,
  versioned and released with the code it documents.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "skill-as-package-export-with-references.md"
    rel: "extends"
  - file: "shared-instructions-multi-harness-plugin-wrappers.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "context-engineering"
  - "skills"
  - "distribution"
---

# Skill Shipped Inside the Package Wheel, Release-Gated with the Code

## What It Is

Two coupled mechanisms:

1. **Distribution:** the consumer-facing coding-agent skill lives inside the library's
   Python package (`.agents/skills/building-pydantic-ai-agents/` — a lean SKILL.md plus
   11 on-demand reference files), so `pip install` delivers it alongside the code, and
   skill marketplaces (library-skills.io, Claude plugin marketplace, agentskills.io)
   resolve it from the installed wheel.
2. **Release gating:** the contributor constitution (CLAUDE.md) requires PRs that add
   features to update the packaged skill, making skill currency a merge requirement
   rather than a docs backlog item.

The result is a hard version coupling: whatever library version an agent's project has
installed, the skill teaching that agent is the matching one. (`docs/coding-agent-skills.md`)

## Why It Matters

Skills that document external libraries rot on a different clock than the library — the
classic failure is an agent confidently using last year's API. Shipping the skill in the
distribution artifact eliminates the version-skew class entirely and moves skill
maintenance from "someone should update the marketplace" to a structural release gate.
It extends the repo-side `skills/` export pattern (skill-as-package-export) one step
further: from *authored in the repo* to *versioned into the artifact consumers actually
install*.

## Why People Are Using It

Adopted by a top-tier framework as its primary channel for teaching consumer coding
agents; the skill preaches the framework's own disclosure discipline (lean entrypoint,
on-demand references). Source: Observed in
[pydantic-ai](https://github.com/pydantic/pydantic-ai) v2.9.0 — see
[[pydantic-ai-analysis]] for structural details.

## Potential Alternatives

- **Repo-level `skills/` export** consumed via `npx skills add` — same authored-once
  goal, but skill version tracks the repo HEAD, not the installed dependency version.
- **Marketplace-hosted skills** — discoverable without installing, but independently
  versioned and prone to skew.
- **Docs-site scraping / Context7-style retrieval** — no packaging work, but no
  curation for agent consumption and no version guarantee.

## Potential Improvements

- Ecosystem convention for where in-package skills live (`.agents/skills/` is emerging)
  so harnesses can auto-discover them across all installed dependencies.
- Wheel-size etiquette: reference docs balloon packages; a slim-skill + fetch-references
  split could keep artifacts lean.

## Potential Failure Modes

- **Package bloat** — every consumer pays the docs bytes whether or not they use agents.
- **Release-gate erosion** — the CLAUDE.md requirement is agent/reviewer-enforced, not
  CI-enforced; skill drift returns quietly if the gate is skipped.
- **Multi-version projects** — monorepos with several installed versions of the library
  surface competing skill versions to the same agent.
