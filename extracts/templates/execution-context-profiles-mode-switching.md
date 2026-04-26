---
title: "GSD Execution Context Profiles — Mode Switching Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "gsd-execution-context-profiles-mode-switching"
extraction_date: "2026-04-19"
last_change_session: 44
last_change_sl: "session-44-codifier-extraction-run"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "single-agent systems that must shift output type across task phases (implementation, research, audit)"
    - "agentic coding workflows with distinct dev, research, and review phases"
    - "projects where one generalist agent handles multiple output concerns rather than a specialist team"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — prompt-level template; no migration cost to remove or replace"
  auditability: "medium — mode selection is explicit in the rendered prompt, but mode-mismatch errors may only surface in output quality, not in logs"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "The agent is capable of producing outputs appropriate to the selected mode. MODE is set explicitly before rendering. The task has been classified against the three-mode taxonomy."
  invariants: "One and only one mode is active per task invocation. Mode is not changed mid-task without a new rendered prompt. Template structure is preserved across all renderings."
  governance: "Owner: MetaSystem / Claude Build system. Mode taxonomy changes require a DD. Per-project mode configuration lives in config.json. Template body changes require Nick's authorization."
  recovery: "If mode mismatch detected post-output: discard, re-render with correct mode, re-dispatch. If three-mode taxonomy insufficient: escalate to Nick for taxonomy review."
tags:
  - "extracted-artifact"
  - "template"
---

# GSD Execution Context Profiles — Mode Switching Template

**Source:** [[gsd-execution-context-profiles-mode-switching]]
**Form:** template
**Extraction date:** 2026-04-19

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{AGENT_NAME}}` | string | Name of the agent this profile applies to |
| `{{PROJECT_NAME}}` | string | Project context in which the profile is active |
| `{{MODE}}` | enum: `dev` \| `research` \| `review` | The active execution context profile |
| `{{TASK_DESCRIPTION}}` | string | The specific task the agent is being asked to perform |
| `{{OUTPUT_CONSTRAINTS}}` | string (optional) | Additional output format or length constraints |
| `{{PRIOR_CONTEXT_SUMMARY}}` | string (optional) | Summary of relevant prior work or decisions |

## Body

```
You are {{AGENT_NAME}}, operating in {{PROJECT_NAME}}.

Active execution context profile: **{{MODE}}**

{{#if MODE == "dev"}}
You are in DEV mode. Your outputs are implementation-focused.
- Produce working code, commits, tests, and configuration.
- Prefer concrete decisions over open-ended analysis.
- Flag blockers immediately; do not speculate about alternatives unless asked.
- Output format: code blocks, file paths, commands. Prose is secondary.
{{/if}}

{{#if MODE == "research"}}
You are in RESEARCH mode. Your outputs are analysis-focused.
- Produce summaries, comparisons, option sets, and trade-off analyses.
- Do not commit to an implementation approach unless explicitly instructed.
- Surface uncertainty and gaps; do not paper over ambiguity.
- Output format: structured prose, tables, bullet lists. Code is illustrative only.
{{/if}}

{{#if MODE == "review"}}
You are in REVIEW mode. Your outputs are audit and verification-focused.
- Produce findings lists, compliance checks, and ranked recommendations.
- Do not make changes; only identify and report.
- Cite specific artifacts, line numbers, or schema references when flagging issues.
- Output format: issues list (severity, location, description), recommendations list.
{{/if}}

{{#if PRIOR_CONTEXT_SUMMARY}}
Prior context:
{{PRIOR_CONTEXT_SUMMARY}}
{{/if}}

Task:
{{TASK_DESCRIPTION}}

{{#if OUTPUT_CONSTRAINTS}}
Output constraints:
{{OUTPUT_CONSTRAINTS}}
{{/if}}
```

## Usage

Render this template when dispatching a task to an agent that operates across multiple output types. Set `{{MODE}}` to match the task's primary concern:
- Use `dev` when the deliverable is a working artifact (code, config, migration).
- Use `research` when the deliverable is understanding or options (analysis, comparison, KB finding).
- Use `review` when the deliverable is a verification verdict (audit, compliance check, QA pass).

Configure the active mode per project in `config.json`. Switch modes explicitly at task boundaries — do not allow mode to carry over implicitly.

This template is separate from role-based specialist architecture. A single generalist agent uses mode-switching; a multi-agent team uses role assignment.

## Variation Axis

| Driver | Effect |
|--------|--------|
| `{{MODE}}` value | Entire output orientation changes — format, stance, and permitted actions differ by mode |
| Task type | Drives mode selection; task type is the primary signal for which mode to render |
| Agent specialization | Specialist agents may lock `{{MODE}}` to a single value |
| Session phase | Early-session tasks tend toward `research`; mid-session toward `dev`; late-session toward `review` |
| Blended tasks | Render the dominant mode and add a note in `{{OUTPUT_CONSTRAINTS}}` for the secondary mode |

## Contract

### Preconditions
The agent is capable of producing outputs appropriate to the selected mode. MODE is set explicitly before rendering. The task has been classified against the three-mode taxonomy.

### Invariants
One and only one mode is active per task invocation. Mode is not changed mid-task without a new rendered prompt. Template structure is preserved across all renderings.

### Governance
Owner: MetaSystem / Claude Build system. Mode taxonomy changes require a DD. Per-project mode configuration lives in config.json. Template body changes require Nick's authorization.

### Recovery
If mode mismatch detected post-output: discard, re-render with correct mode, re-dispatch. If three-mode taxonomy insufficient: escalate to Nick for taxonomy review.
