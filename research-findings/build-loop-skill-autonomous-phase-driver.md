---
name: Build Loop Skill as Autonomous Phase Driver
summary: A custom Claude Code skill wraps the orchestrator-headless-dispatch pattern into a single invocable command ('build loop'). The skill reads a phase-queue state file, dispatches each incomplete
  phase as a claude -p headless subprocess, collects summaries, updates the state file, and loops until all phases are complete. This packages the dispatch loop as a reusable, triggerable skill rather than
  a one-off bash script.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- gstack-gsd-superpowers-orchestrator-headless.md
related_findings:
- file: orchestrator-headless-dispatch-context-isolation.md
  rel: extends
- file: phase-queue-state-file-as-orchestrator-memory.md
  rel: enables
- file: ralph-wiggum-execution-pattern.md
  rel: same-problem
- file: skill-chaining-composing-workflows-from-modular-s.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- extracts/skills/build-loop-skill-autonomous-phase-driver.md
- autonomous-scheduled-agent-operation.md
tags:
- session-95-reextract
---

# Build Loop Skill as Autonomous Phase Driver

## What It Is

A Claude Code skill that encapsulates the full autonomous build cycle as a single triggerable command. The user invokes the "build loop" skill, and the skill:

1. Reads the phase-queue state file to find all phases and their completion status
2. Identifies the next incomplete phase
3. Dispatches that phase as a `claude -p` headless subprocess with the phase's self-contained prompt
4. Waits for the headless session to complete and exit
5. Reads the headless session's output (summary/results)
6. Updates the state file to mark the phase complete
7. Loops back to step 2 until all phases are done

The skill wraps what would otherwise be a manual, repetitive process (starting a new headless session for each phase, passing the prompt, collecting results, checking what's next) into a single fire-and-forget invocation. In the demonstrated workflow, the user runs the build loop skill, walks away overnight, and returns to find all 16 phases completed.

The critical difference from a raw ralph loop: a ralph loop iterates on a SINGLE task until it passes verification. The build loop iterates across MULTIPLE phases, dispatching each once (or with retry logic). The ralph loop is depth-first on one problem; the build loop is breadth-first across a project.

## Why It Matters

Making the autonomous dispatch loop a skill rather than a script or manual process has three benefits: (1) it is discoverable and invocable through the standard Claude Code skill system, (2) it inherits the skill's context (CLAUDE.md, rules, MCP servers) which the headless sessions also inherit, and (3) it can be composed with other skills -- the build loop skill can invoke Superpowers or gstack skills within each headless session.

For MetaSystem, this pattern suggests that the `/gsd-autonomous` skill (which already runs discuss-plan-execute per phase) could adopt the headless dispatch model instead of running all phases within a single session. This would give each phase a fresh context window while preserving the single-command autonomy that `/gsd-autonomous` provides.

## Why People Are Using It

Demonstrated in a live overnight 16-phase build (Eric Tech). The skill was invoked once in the orchestrator session, ran through the night, and completed all phases. The orchestrator session used <10% context because it only managed dispatch logic, not execution work.

## Potential Improvements

- Add progress callbacks or notifications (e.g., webhook, terminal bell) so the user knows when each phase completes without watching the terminal
- Include a dry-run mode that shows the dispatch plan (which phases, in what order) without actually executing
- Support parallel dispatch for phases without dependencies (dispatch Phases 4 and 5 simultaneously if they are independent)
- Integrate with a verification skill that runs after all phases complete to validate the final output

## Potential Failure Modes

- **Single-threaded bottleneck.** Sequential dispatch means independent phases wait for each other unnecessarily. A 16-phase project with 8 parallelizable phases takes twice as long as it needs to.
- **No mid-run human gate.** Once the build loop is running autonomously, there is no human checkpoint between phases. A phase that produces bad output poisons all subsequent phases with no opportunity for correction.
- **Headless session failures are silent.** If a headless session crashes or produces garbage, the build loop may mark it complete based on exit code alone, missing quality failures.
- **Cost accumulation.** Each headless session is a fresh Claude API call. A 16-phase build with retries can consume significant API credits with no intermediate human review of whether the cost is justified.
