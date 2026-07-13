---
name: "Skill Flattening: Retreat from Step-File Micro-Architecture"
summary: |-
  Plain English: the framework that invented step-file skill decomposition has
  retreated from it for all judgment-heavy work — cutting workflow orchestrators from
  22 to 1 and step files from 112 to 35 — and rebuilt its flagship skills as single
  outcome-driven SKILL.md files (~85–160 lines) with intent-scoped reference modules
  and deterministic side-rails. BMAD v6.10.0 keeps step files only in mechanical
  execution skills (dev-auto, code-review, checkpoint-preview), drawing an empirical
  boundary: sequencing enforcement pays where the work is mechanical, and fights model
  judgment where it isn't. The v6.7.0+ changelogs call the old shape "five-stage
  scripted workflow" and the new one "a single outcome-driven SKILL.md"; the lost
  step-sequencing enforcement was replaced by scripts, linters, and reviewer gates at
  the boundaries. Partial supersession signal for the KB's
  step-file-micro-architecture finding.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "step-file-micro-architecture.md"
    rel: "contradicts"
  - file: "rules-layer-collapse-monolithic-context-counter-signal.md"
    rel: "same-problem"
  - file: "everything-as-skill-architecture.md"
    rel: "extends"
  - file: "specialized-harness-engineering-deterministic-rail.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "context-engineering"
  - "skill-design"
  - "counter-signal"
---

# Skill Flattening: Retreat from Step-File Micro-Architecture

## What It Is

A structural reversal by the pattern's own inventor. At v6.2.2, BMAD's signature was
step-file micro-architecture: 22 `workflow.md` orchestrators fanning into 112 numbered
step files with just-in-time loading and forward-loading forbidden by validator rule.
At v6.10.0:

- 1 workflow.md and 35 step files remain, confined to mechanical execution skills
  (dev-auto, code-review, checkpoint-preview, epics, research).
- Flagship judgment-heavy skills (prd, spec, architecture, ux, product-brief,
  forge-idea, party-mode) are each a single outcome-driven SKILL.md (~85–160 lines)
  plus `references/` modules loaded per detected intent, `assets/` templates, and a
  `customize.toml`.
- The enforcement that step sequencing provided moved to deterministic side-rails at
  the boundaries: memlog.py (state), lint_spine.py (artifact shape),
  resolve_config.py (config), validate-skills.js (skill quality), reviewer gates
  before finalize.

Markdown file count fell while skill count grew 41→47 — the direct signature of the
flattening.

## Why It Matters

This is the strongest available empirical answer to a live design question: where does
prescribed sequencing help an LLM, and where does it fight model judgment? The
inventor's revealed boundary — steps for mechanical execution, outcome prose plus
side-rails for judgment work — comes from operating both shapes at scale across eight
minor versions. It also generalizes the KB's rules-layer-collapse counter-signal:
decomposition-for-context-economy keeps losing to "short judgment-driven prose +
deterministic rails" as models improve. Any system authoring procedure-heavy skills
should read its own skills against this boundary.

## Why People Are Using It

The v6.7.0–v6.10.0 changelogs document the rebuild skill by skill; the retained
step-file holdouts are exactly the unattended/mechanical surfaces. Source: Observed in
[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] for structural details; supersedes-in-part the architecture
recorded in [[step-file-micro-architecture]] (v6.2.2 era).

## Potential Alternatives

- **Keep step files everywhere** — maximal sequencing control; the abandoned position.
- **Pure outcome prose, no rails** — trusts model judgment entirely; loses the
  deterministic checks that made flattening safe.
- **Graph/engine-enforced workflows** — move sequencing out of prose into an engine
  (Archon); strongest enforcement, heaviest infrastructure.

## Potential Improvements

- A crisper published test for "mechanical vs judgment" classification of a skill —
  the boundary is currently demonstrated, not defined.
- Migration evidence: before/after quality or token measurements for the rebuilt
  flagships would upgrade this from revealed preference to measured result.

## Potential Failure Modes

- **Model-dependence** — the flattening bet assumes strong models; weaker deployment
  targets may still need the scaffolding the steps provided.
- **Side-rail coverage gaps** — sequencing enforced everything implicitly; rails check
  only what someone thought to lint, and drift can hide between them.
- **Activation-chain fragility** — v6.8.0 had to harden 23+ skills against LLMs
  short-circuiting prose boot sequences ("guessing variables instead of executing in
  order"); flattened skills lean harder on exactly that kind of prose discipline.
