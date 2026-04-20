---
name: Planning Session Bias — Separate Context Windows for Planning vs. Implementation
summary: Running planning and implementation in the same agent session causes "planning bias" — the agent becomes anchored to its own earlier reasoning and defends decisions rather than executing
  them cleanly. Harness engineering enforces separate sessions by design, passing a plan artifact as the only bridge.
implementation_notes: MetaSystem already uses separate sessions for different tasks, but the bias problem justifies making this explicit in workflow design. When using Archon (or manual session management),
  planning output must be captured as a file artifact before starting a fresh implementation session. The plan becomes the only shared context — not the conversation history.
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- archon-live-stream-agent-workflows-dark-factory.md
related_findings:
- file: archon-yaml-defined-harness-workflows.md
  rel: enabled-by
- file: artifact-as-contract-pattern.md
  rel: enabled-by
- file: incremental-one-feature-per-session-pattern.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: boris-chernys-explore-plan-implement-commit-workf.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

# Planning Session Bias — Separate Context Windows for Planning vs. Implementation

## What It Is
When an agent does both planning and implementation in the same session, the implementation quality degrades due to "planning bias": the agent has anchored itself to the reasoning it developed during planning and is less able to adapt when implementation reveals new information. The planning conversation becomes an inertia that resists clean execution. Cole Medin described this as a specific reason Archon separates planning and implementation into different nodes (separate Claude Code sessions) — the planning session "can get pretty bogged down and you can build up a lot of bias over time." The workaround: produce a plan artifact, end the planning session, and start a fresh implementation session that reads only the plan file.

## Why It Matters
This is distinct from general context rot (session becoming too long). The bias problem occurs even in short sessions — it's about the agent defending its own prior reasoning rather than executing against a spec. A fresh session reads the plan document neutrally, without the weight of having generated it. The plan artifact acts as a clean specification rather than a continuation of the planning conversation.

## Why People Are Using It
Archon enforces this by design: planning nodes produce an artifact to the `artifact_dir`, and implementation nodes start fresh sessions that read that artifact via their prompt. The PIV loop (Plan → Implement → Validate) is the practitioner pattern that operationalizes this. Boris Cherny's Explore → Plan → Implement → Commit workflow also encodes phase separation.

## Potential Alternatives
- Single long session with a strong "now switch to implementation mode" instruction (risks planning bias)
- Human review of the plan before implementation (adds friction but catches planning errors)
- Plan as a CLAUDE.md section (present every turn but static — doesn't capture fresh-session benefits)

## Potential Improvements
- Explicit plan artifact template with acceptance criteria, so the implementation session has a checkable done condition
- Diff check between planned steps and implemented steps to surface when implementation diverged from plan
- Post-implementation review of whether the plan was correct (closes the loop for future planning quality)

## Potential Failure Modes
- If the plan artifact is incomplete or ambiguous, the fresh implementation session has worse context than a biased single session would
- Plan quality becomes the bottleneck — garbage plan → garbage implementation with no self-correction
- Overhead of session management (creating worktrees, writing artifacts, starting fresh sessions) creates friction that teams avoid
