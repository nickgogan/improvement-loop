---
name: "AI Shepherding Anti-Pattern: Manual Workflow Sequencing"
summary: "The practice of a human manually invoking skills and commands in sequence, remembering what comes next after each step, and kicking off each phase of a multi-step process. Named 'AI shepherding' by Cole Medin as the problem that harness engineering solves. The human becomes the orchestrator — a role better served by deterministic automation."
implementation_notes: "MetaSystem's current workflow involves Nick manually invoking skills in sequence (e.g., /research-loop then /identify-artifacts then /extract-artifacts). This is textbook AI shepherding. The harness pattern (Archon, GSD /autonomous) addresses this by encoding the full sequence as a runnable workflow."
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "archon-open-source-harness-builder.md"
related_findings:
  - file: "archon-yaml-defined-harness-workflows.md"
    rel: "same-problem"
  - file: "harness-engineering-third-evolution.md"
    rel: "same-problem"
  - file: "planner-executor-deterministic-guardrails.md"
    rel: "same-problem"
  - file: "skill-chaining-composing-workflows-from-modular-s.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "rules/encode-stable-manually-sequenced-workflows-as-harnesses.md"
  - building-agentic-systems.md
tags:
  - "session-95-reextract"
---

## What It Is

"AI shepherding" is the practice where a human operator manually sequences an AI coding workflow: invoke the planning skill, review the output, invoke the implementation skill, review, invoke the test skill, review, invoke the code review skill, and so on. The human serves as the orchestrator — remembering the process order, deciding when to proceed, and kicking off each step manually.

Cole Medin names this explicitly: "You have your skills and commands and you're running workflows there, but you still have your entire process where you're running different skills and different commands, and you have to remember what comes next, and you have to kick off the code review after the implementation."

The alternative is encoding the full sequence as a workflow that runs end-to-end: "Define once, run forever, reusable across projects." The harness handles sequencing, context management, model selection, validation, and branching — the human only intervenes at explicit human gates.

## Why It Matters

AI shepherding creates several failure modes:
1. **Process amnesia** — the human forgets a step (e.g., skipping tests after implementation)
2. **Inconsistency** — the sequence varies between runs, making outcomes non-reproducible
3. **Human bottleneck** — the process can only run when the human is actively managing it
4. **Context fragmentation** — manually moving between skills/commands without structured handoff artifacts

The naming itself is valuable as a diagnostic label. When teams recognize they are "shepherding" their AI, they can identify the pattern and evaluate whether to invest in harness automation for that specific workflow.

## Why People Are Using It

Most practitioners are still in the AI shepherding phase — it's the default mode of working with coding agents. Skills and commands are powerful individually but lack built-in sequencing. The transition from shepherding to harnessed workflows represents the same evolution as moving from manual deployments to CI/CD pipelines.

## Potential Improvements

- Shepherding audit: instrument skill invocations to detect recurring manual sequences that could be automated
- Gradual harnessing: start by encoding the 2-3 most common sequences as workflows, keep shepherding for rare/novel tasks
- Hybrid mode: harness runs the sequence but pauses at every step for human review (training wheels before full automation)

## Potential Failure Modes

- Over-automating workflows that genuinely need human judgment at every step
- Premature harnessing before individual skills are reliable (automating unreliable steps faster doesn't help)
- The diagnostic label becoming dismissive — some manual sequencing is appropriate for exploratory or novel work
