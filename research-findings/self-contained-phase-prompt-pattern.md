---
name: Self-Contained Phase Prompt Pattern
summary: Each phase in an autonomous build queue is represented as a fully self-contained prompt that includes all context the headless session needs to execute the phase without access to the orchestrator's
  conversation history or prior phase execution details. The prompt is generated during the planning/decomposition stage and stored in the phase-queue state file. This front-loads context engineering into
  planning time rather than execution time.
implementation_notes: null
category: Context Engineering
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
  rel: enables
- file: phase-queue-state-file-as-orchestrator-memory.md
  rel: enables
- file: hands-off-routine-prompt-precision-pattern.md
  rel: same-problem
- file: spec-as-source-of-truth-for-agent-construction.md
  rel: same-problem
- file: artifact-as-contract-pattern.md
  rel: extends
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
tags:
- session-95-reextract
---

# Self-Contained Phase Prompt Pattern

## What It Is

A context engineering pattern where each phase's prompt is designed to be fully self-contained -- the headless session receiving the prompt can execute the phase using ONLY the prompt content plus the codebase on disk. The prompt does not assume access to:

- The orchestrator's conversation history
- Prior phases' execution details (beyond what's in committed code/files)
- Accumulated design decisions from earlier in the session
- Any context that isn't either in the prompt itself or in the filesystem

This means the planning/decomposition stage (typically done with gstack or GSD) must front-load all necessary context into each phase prompt. A well-crafted phase prompt includes:
- What this phase must accomplish (goal and scope)
- Which files/areas of the codebase to focus on
- What patterns or conventions to follow
- What constitutes "done" (verification criteria)
- Any constraints from prior phases that affect this one (via file references, not conversation)

The demonstrated workflow stores each phase prompt in a state file during the GSD decomposition stage. When the build loop dispatches a phase, it passes this stored prompt to `claude -p`. The headless session starts fresh, reads the prompt, and has everything it needs.

## Why It Matters

Self-contained prompts are what make the orchestrator-headless pattern actually work. If phase prompts were NOT self-contained -- if they implicitly depended on accumulated context from the orchestrator -- then headless dispatch would produce wrong or incomplete results.

The pattern shifts the burden of context engineering from execution time (when context is scarce and the agent is under pressure) to planning time (when the full project context is available and the planner can carefully construct each prompt). This is analogous to pre-computing function arguments vs. relying on runtime state: pre-computation is more reliable because the full context is available at composition time.

For MetaSystem, this has direct implications for skill design. Skills invoked via subagents or headless dispatch must receive self-contained prompts -- they cannot assume they share the invoking session's context. This is already partially true for GSD's `/gsd-execute-phase` but the principle could be applied more systematically.

## Why People Are Using It

Demonstrated in the 16-phase overnight build (Eric Tech). GSD's phase decomposition generates per-phase prompts stored in the build queue. Each prompt was self-contained enough to be dispatched to a headless session that had no prior context.

The pattern also appears in GSD's PLAN.md artifacts (which contain self-contained task descriptions for sub-agent dispatch) and in the Anthropic harness pattern's spec.md (which gives each iteration of a ralph loop its full context).

## Potential Improvements

- Prompt templates per phase type (e.g., "API endpoint phase" template includes standard sections for route, handler, tests, integration; "UI component phase" template includes design spec, accessibility, responsive behavior)
- Automated self-containment validation: a linter that checks whether a phase prompt references context that isn't available to a fresh session
- Context injection: the orchestrator can append relevant prior-phase summaries to the phase prompt, enriching it without requiring the headless session to have shared context
- Iterative refinement: if a phase fails, the orchestrator can augment the phase prompt with the failure details and re-dispatch

## Potential Failure Modes

- **Prompt bloat.** Making each prompt fully self-contained may require duplicating context across phases (e.g., architecture decisions stated in every prompt). This wastes tokens and creates inconsistency risk if the duplicated context drifts.
- **Planning-time blind spots.** The planner cannot anticipate every piece of context the execution session will need. Phases that encounter unexpected situations (a dependency not in the plan, a file that doesn't exist yet) will fail because the prompt didn't include that context.
- **Implicit dependencies masquerading as self-contained.** A prompt may reference "the authentication module" assuming it exists -- but if Phase 3 was supposed to create it and Phase 3 failed, Phase 5's "self-contained" prompt has an invisible dependency.
- **Prompt quality bottleneck.** The quality of the entire autonomous build depends on the quality of per-phase prompts generated during planning. Bad prompts at planning time compound into bad execution across all phases.
