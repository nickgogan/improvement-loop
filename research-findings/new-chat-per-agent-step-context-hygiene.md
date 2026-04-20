---
name: New-Chat-Per-Agent-Step as Context Hygiene Discipline
summary: A strict discipline of starting a new chat window at every agent phase boundary, transferring information only via documents (not conversation state), to prevent context window degradation in multi-phase
  workflows.
implementation_notes: MetaSystem's session-handoff skill generates structured handoff prompts. Extending this to intra-session agent boundaries would implement this pattern.
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-method-masterclass.md
proposals: []
date_discovered: '2026-04-07'
last_updated: 2026-04-08
related_findings:
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: enabled-by
- file: tiered-context-injection-over-monolithic-files.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---
# New-Chat-Per-Agent-Step as Context Hygiene Discipline

## What It Is
At each phase boundary (Analyst -> PM -> Architect -> Dev -> QA), kill the current chat window and start fresh. Information transfers via document artifacts only — the next agent reads the output files, not the conversation history. Use /clear or kill window to reset. Avoid memory compaction mid-workflow. Add reference files to project-references.md instead of leaving them in active context.

## Why It Matters
Multi-step workflows in a single context window accumulate noise, outdated instructions, and conflicting context. Fresh context per step ensures each agent sees only what it needs.

## Why People Are Using It
Core discipline in BMad Method. Brian's rule: "Every file that you keep here is potential context... better to add these to a project references file."

## Potential Alternatives
- Single long context with periodic /compact.
- Agent sub-processes with isolated context (Claude Code's subagent model).
- Selective context injection per step.

## Potential Improvements
- Automated context handoff templates per phase boundary.
- Cross-phase summary documents generated automatically.
- Metrics on context quality degradation across phases.

## Potential Failure Modes
Loss of nuance that existed in conversation but wasn't captured in documents. Overhead of frequent context switches for small tasks. Requires discipline — easy to skip "just this once" and accumulate debt.
