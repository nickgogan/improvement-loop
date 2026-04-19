---
name: GSD Execution Context Profiles — Mode Switching
summary: Three context profiles (dev, research, review) that change agent output guidance per mode, configurable per-project via config.json.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General / Cross-System
adopted_in: []
sources:
- gsd-v1340-v1342-changelog.md
related_findings:
- file: context-curation-over-context-stuffing.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: "extracted"
consumed_by:
  - "templates/execution-context-profiles-mode-switching.md"
---

## What It Is

A mode-switching mechanism that defines three execution context profiles — dev, research, and review — each changing the output guidance a single agent receives. Dev mode produces implementation-focused output (code, commits, tests). Research mode produces analysis and exploration output (summaries, comparisons, options). Review mode produces audit and verification output (issues found, compliance checks, recommendations). Profiles are configured per-project via config.json and are separate from role-based specialist architecture — this is about *what kind of output* a single agent produces, not which specialist agent is invoked.

## Why It Matters

A single agent prompted identically for implementation and research tasks produces muddled output — code mixed with analysis, or analysis that prematurely commits to an approach. Context profiles separate these concerns at the prompt level, giving the agent clear guidance on output format and depth appropriate to the current task mode. This is lighter-weight than maintaining separate specialist agents for each concern.

## Why People Are Using It

Teams need agents to shift between writing code, exploring options, and auditing work — often within the same project session. Rather than building and maintaining separate agent configurations for each mode, context profiles provide a single-agent solution with mode-appropriate output shaping. The per-project config makes it easy to default a project to its dominant mode while allowing overrides.

## Potential Improvements

The profile set could be extensible beyond the three canonical modes — projects may need domain-specific profiles (e.g., "migration" mode for database work, "security" mode for threat modeling). Profile switching could be automatic based on workflow phase rather than requiring manual configuration. Profiles could also influence tool availability, not just output guidance — research mode might enable web search tools while dev mode enables file-write tools.

## Potential Failure Modes

Mode mismatches degrade output quality silently — an agent in dev mode asked to do research will produce shallow analysis that looks like implementation. If profile switching is manual, users forget to switch and receive wrong-mode output. The three-profile taxonomy may also be too coarse — real tasks often blend modes (e.g., "research the best approach then implement it"), and rigid mode boundaries could force artificial task splitting.

## Extraction Note — 2026-04-19
Extracted as **template**: [[execution-context-profiles-mode-switching]] in `extracts/templates/`
