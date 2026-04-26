---
title: "One-Shot PRD Prompt for Full System Bootstrap"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "one-shot-prd-prompt-for-system-bootstrap"
extraction_date: "2026-04-19"
last_change_session: 44
last_change_sl: "session-44-codifier-extraction-run"
version: 1
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "greenfield system initialization in agentic coding environments"
    - "declarative scaffold generation from a single PRD document"
    - "teams seeking reproducible, one-pass project bootstrapping without interactive setup"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "low — the bootstrapped file structure is a system artifact; removing it requires manually deleting the generated scaffold, though the PRD template itself is trivially removable"
  auditability: "high — the PRD is the sole source of truth; a produced scaffold can be diffed against the PRD's declared structure to verify compliance"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production-validated independently by Karpathy (LLM KB system gist) and Cole Medin (working implementation). No adoption within this system at time of extraction."
contract:
  preconditions: "The PRD document is complete — all variables populated before rendering. Agent starts in a fresh context. Target system has no existing files to reconcile."
  invariants: "The rendered PRD is the sole source of truth for the bootstrap session. Reproducibility anchors must be present when the same PRD will be used across multiple sessions."
  governance: "Owner: Improvement Loop (research origin), Meta-System (codification home). Modifications require a new finding or Nick authorization. Reproducibility Anchors section is mandatory."
  recovery: "If structurally inconsistent output: start fresh context with same PRD, compare divergence against Reproducibility Anchors, strengthen anchors, re-run."
tags:
  - "extracted-artifact"
  - "template"
---

# One-Shot PRD Prompt for Full System Bootstrap

**Source:** [[one-shot-prd-prompt-for-system-bootstrap]]
**Form:** template
**Extraction date:** 2026-04-19

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{SYSTEM_NAME}}` | string | Human-readable name of the system being bootstrapped |
| `{{SYSTEM_PURPOSE}}` | string | One-sentence statement of what the system does and for whom |
| `{{FOLDER_STRUCTURE}}` | markdown list | Hierarchical folder tree with per-folder purpose annotations |
| `{{INDEX_CONVENTIONS}}` | string | Rules for `_index.md` files: location, required fields, update triggers |
| `{{COMPILATION_RULES}}` | string | Any build, compilation, or generation steps the agent must set up |
| `{{HOOK_CONFIGURATION}}` | string | Pre/post hooks to configure |
| `{{AGENTS_MD_SPEC}}` | string | What the `agents.md` or equivalent context file must contain |
| `{{CONSTRAINT_LIST}}` | markdown list | Hard constraints (naming, casing, forbidden patterns) |
| `{{REPRODUCIBILITY_ANCHORS}}` | markdown list | Explicit rules that enforce identical output across sessions |
| `{{FAILURE_MODES}}` | markdown list | Known failure modes and mitigations |

## Body

```
You are implementing {{SYSTEM_NAME}} from scratch. This document is the complete specification. Read it fully before writing a single file. Your job is to produce an implementation that matches this design — not to interpret, invent, or extend it.

## System Purpose

{{SYSTEM_PURPOSE}}

## Folder Structure

{{FOLDER_STRUCTURE}}

## Index Conventions

{{INDEX_CONVENTIONS}}

## Compilation and Build Rules

{{COMPILATION_RULES}}

## Hook Configuration

{{HOOK_CONFIGURATION}}

## Agent Context File (agents.md)

{{AGENTS_MD_SPEC}}

## Hard Constraints

{{CONSTRAINT_LIST}}

## Reproducibility Anchors

The following rules exist to ensure two independent agents reading this document produce structurally identical output:

{{REPRODUCIBILITY_ANCHORS}}

## Known Failure Modes

{{FAILURE_MODES}}

---

Begin implementation now. Create all folders and files. Do not ask clarifying questions unless a constraint is directly contradictory. When implementation is complete, produce a brief summary listing every file created and any decisions you made where the PRD was silent.
```

## Usage

Bootstrap a new system in a single agent invocation. Paste the rendered document into a fresh Claude Code context (no prior conversation history). The agent reads the PRD in full, then implements all folders, files, hooks, and scaffolding in one pass.

Do not use this template for:
- Iterative or incremental builds where scope is not yet known
- Systems where the folder structure depends on runtime discovery
- Situations where the agent must negotiate requirements mid-build

## Variation Axis

1. **Constraint density** — More explicit constraints and reproducibility anchors produce more deterministic output across sessions. Underspecified PRDs produce structurally divergent implementations.
2. **System complexity** — Simple systems need minimal variables. Complex systems (fractal folder patterns, multi-hook configs, agents.md with role definitions) require all variables fully populated.

## Contract

### Preconditions
The PRD document is complete — all variables populated before rendering. Agent starts in a fresh context. Target system has no existing files to reconcile.

### Invariants
The rendered PRD is the sole source of truth for the bootstrap session. Reproducibility anchors must be present when the same PRD will be used across multiple sessions.

### Governance
Owner: Improvement Loop (research origin), Meta-System (codification home). Modifications require a new finding or Nick authorization. Reproducibility Anchors section is mandatory.

### Recovery
If structurally inconsistent output: start fresh context with same PRD, compare divergence against Reproducibility Anchors, strengthen anchors, re-run.
