---
name: Skill vs. Process Distinction (Deterministic Rails for Business Workflows)
summary: Agent skills (send email, query DB) are not business processes. Workflows should be hardwired with deterministic triggers. The agent operates within the rails doing what it's good at (text composition,
  tool calling), while process flow is not left to agent judgment.
implementation_notes: Review MetaSystem skills for process-vs-skill confusion. Skills should be atomic capabilities; workflows should be deterministic sequences that invoke skills.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources:
- agent-produces-100x-org-reviews-3x.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: task-contract-pattern-schema-first-agent.md
  rel: enabled-by
- file: build-operate-separation-principle.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---

# Skill vs. Process Distinction (Deterministic Rails for Business Workflows)

## What It Is
A design principle from Nate B Jones (multiple deployment case studies) that separates agent skills from business processes. Skills are atomic capabilities (send email, query database, compose text). Processes are deterministic sequences of steps with known handoffs and exception paths. The agent operates within each step; the process flow itself is hardcoded.

## Why It Matters
The railroad analogy: letting an agent decide workflow sequencing is like "ripping up your railroad and sticking your train on the ground." Business processes have known steps, known handoffs, known exception paths. These should be hardcoded infrastructure, not agent decisions. The agent's value is within each step -- composing text, analyzing data, making API calls -- not deciding which step comes next.

## Why People Are Using It
Adjacent to the "Specialized Harness Engineering" finding (from a different source, framed as Python scaffolding). Jones's version is specifically about business process design rather than code scaffolding. Production deployments show that deterministic rails produce consistent, auditable execution while still leveraging agent intelligence where it matters.

## Potential Improvements
MetaSystem skills could be audited for process-vs-skill confusion. Skills that contain workflow logic (multi-step sequences with conditional branching) may need to be refactored into deterministic workflows that invoke atomic skills.

## Potential Failure Modes
Letting agents decide workflow sequencing leads to skipped steps, invented shortcuts, and inconsistent execution. The agent "solves" friction by taking creative detours rather than following the prescribed path. Conversely, over-rigidity in process rails can prevent legitimate adaptation when business requirements change.
