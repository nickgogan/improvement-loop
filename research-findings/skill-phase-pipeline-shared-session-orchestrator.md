---
name: Skill-Phase Pipeline with Shared-Session Orchestrator
summary: A development lifecycle encoded as a sequence of skill invocations within a single persistent orchestrator session. Each skill defines one phase boundary (brainstorm, plan, execute, review, finish).
  The orchestrator session persists across all skill invocations, carrying design decisions, user preferences, and accumulated context forward — unlike artifact-only handoff where inter-phase state is limited
  to files.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
sources:
- claude-code-plus-superpowers-tutorial.md
related_findings:
- file: superpowers-plugin-spec-driven-sub-agent-orchestra.md
  rel: extends
- file: artifact-as-contract-pattern.md
  rel: same-problem
- file: skill-chaining-composing-workflows-from-modular-s.md
  rel: extends
- file: orchestrator-headless-dispatch-context-isolation.md
  rel: contradicts
- file: framework-tension-taxonomy-superpowers-gsd-gstack.md
  rel: extends
- file: leg-work-amplification-hiding-future-steps.md
  rel: same-problem
adopted_in: []
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
tags:
- session-95-reextract
---

# Skill-Phase Pipeline with Shared-Session Orchestrator

## What It Is

A composition pattern where a complete development lifecycle is encoded as a sequence of skill invocations within one persistent orchestrator session. In Superpowers, the human triggers skills in order: brainstorm -> write-plan -> execute-plan -> code-review -> finish. Each skill defines a phase boundary — it has its own prompt, its own tool permissions, its own output format — but the orchestrator session persists across all invocations.

The key structural feature: the orchestrator session accumulates context across phases. When the user approves a brainstorm spec, the orchestrator carries that approval context into the plan-writing skill. When the user chooses sub-agent execution over inline execution, the orchestrator carries that choice into the execute phase. This is fundamentally different from the artifact-only handoff pattern (GSD) where inter-phase state is limited to files and each phase gets a fresh context.

In the observed workflow (Eric Tech tutorial on BookZero.ai):
1. User pastes a Jira ticket URL and invokes the brainstorm skill
2. Brainstorm skill explores existing architecture, generates HTML mockups, asks questions one at a time, produces a spec to docs/
3. User approves spec and tells the orchestrator to transition to planning
4. The write-plan skill converts the approved spec into an 11-task implementation plan with TDD step ordering
5. User reviews the plan and selects execution mode (sub-agent vs inline)
6. The execute-plan skill dispatches sub-agents per task within a git worktree
7. After all tasks complete, the code-review skill runs a final review and dispatches fix agents

The orchestrator never resets between these skill invocations. It knows the user chose option C for the UI mockup, knows the spec was approved, knows sub-agent mode was selected — all from conversational context, not from reading files.

## Why It Matters

This pattern solves a real composition problem: how do you chain phases that need accumulated context without paying the artifact-serialization tax? In artifact-only handoff (GSD, MetaSystem IL), every piece of inter-phase context must be explicitly written to a file by the producing phase and explicitly read by the consuming phase. This is reliable but lossy — conversational context, user preferences expressed informally, and design rationale discussed but not documented all get lost at phase boundaries.

The skill-phase pipeline keeps all of that in the orchestrator's context window. The tradeoff is clear: richness of inter-phase context vs. context rot risk as the session grows long.

For MetaSystem: the IL pipeline is artifact-only (Researcher writes findings, Codifier reads findings). This is correct for the IL's scale, but the pattern is worth knowing for S3 (Claude Build) where a single build session might benefit from carrying brainstorm decisions through to execution without serializing every design choice to disk.

## Why People Are Using It

Demonstrated in the Superpowers plugin tutorial (Eric Tech, BookZero.ai feature build). The orchestrator persisted across brainstorm, plan, execute, and review phases for an 11-task feature addition to a production app. Superpowers has 120k GitHub stars and is Anthropic-endorsed.

Also structurally present in: any Claude Code session where a user invokes multiple skills in sequence without clearing context. The pattern is implicit in how slash-command skills work — they execute within the current conversation, not in a new one.

## Potential Improvements

- Explicit context checkpointing between skill phases — let the orchestrator write a summary of accumulated decisions before moving to the next phase, creating a recoverable state without full context reset
- Graduated context management — compact older phase context as new phases begin, keeping decision summaries but dropping conversation detail
- Hybrid model — use shared-session orchestrator for brainstorm-to-plan (where conversational context matters most) and switch to artifact-only handoff for execute-to-review (where fresh context matters more)

## Potential Failure Modes

- **Context rot on long projects.** The orchestrator accumulates brainstorm discussion, plan details, execution logs, and review notes in a single session. For large features (11+ tasks), this can push past the 50% context threshold where performance degrades.
- **Non-recoverable session loss.** If the session crashes or is accidentally closed mid-pipeline, all accumulated context is lost. Artifact-only handoff is crash-resilient by design; this pattern is not.
- **Implicit state is invisible.** Design decisions carried in conversational context are invisible to external reviewers. A teammate reading the PR has no record of why option C was chosen for the UI — that decision lived in the session, not in the spec.
- **Contradicts context-isolation best practices.** The orchestrator-delegates-to-headless-sessions finding recommends keeping orchestrator context under 10% utilization. This pattern goes the opposite direction.
