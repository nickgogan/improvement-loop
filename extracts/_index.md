---
title: "Extracted Artifacts"
type: "index"
target_system:
  - "improvement-loop"
created: "2026-04-19"
updated: "2026-04-23"
---

# Extracted Artifacts

Staged artifacts produced by `/extract-artifacts` from research findings. Each artifact is classified into one of 5 forms and carries a ContractSpec (DD-78). Artifacts here are **not yet deployed** — deployment to enforcement locations (`.claude/rules/`, `meta-system/knowledge/`, etc.) is a separate human-gated act.

**Pipeline position:** Research Finding -> `/extract-artifacts` -> **here** -> [human deploy] -> enforcement location

**Design Decision:** DD-80 (pipeline simplification)

## Subdirectories

| Directory | Form | Deployment Target |
|-----------|------|-------------------|
| `rules/` | Binary constraint enforced at a boundary | `.claude/rules/` or `{system}/governance/` |
| `templates/` | Scaffold with variables and a body | `meta-system/knowledge/templates/` |
| `agents/` | Persona with cognitive disposition and durable scope | `meta-system/knowledge/templates/agent-templates/` |
| `skills/` | Procedure with inputs/outputs/steps | `.claude/skills/` |
| `patterns/` | Sub-patterns derived from parent patterns | `meta-system/knowledge/patterns/` |
| `guides/` | End-directed guides synthesized from pattern clusters | `meta-system/knowledge/guides/` |

## Discovery

Browse each form subdirectory directly. Filter by frontmatter using ripgrep — e.g., `rg -l '^deployed: false' extracts/**/*.md` for staged-but-undeployed artifacts, or `rg -l '^form: pattern' extracts/**/*.md` for all patterns.
