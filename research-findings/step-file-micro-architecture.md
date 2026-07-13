---
name: Step-File Micro-Architecture
summary: BMAD decomposes complex workflows into numbered step files (step-01 through step-12), loading only the current step. Forward-loading is forbidden (validator rule STEP-05). Sequential enforcement
  is mandatory (SEQ-01). Principled context window management.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: document-sharding-for-context-efficiency.md
  rel: same-problem
- file: tiered-context-injection-over-monolithic-files.md
  rel: same-problem
- file: skill-flattening-outcome-prose-over-step-files.md
  rel: contradicts
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-07-13'
pipeline_status: raw
consumed_by: []
---
## What It Is

BMAD decomposes complex workflows into numbered step files — `step-01-init.md` through `step-12-complete.md`. Each step file is a self-contained unit with an explicit goal, a next-step reference, and halt conditions. Only the current step is loaded into the agent's context at any time.

Two validator rules enforce this as a hard constraint, not a suggestion:

- **STEP-05**: No forward-loading. The agent must not read or reference any step beyond the current one.
- **SEQ-01**: No skip instructions. Steps must be executed in strict sequential order; jumping ahead is forbidden.

Each step file contains everything needed to complete that step — input expectations, instructions, validation criteria, and the pointer to the next step. The agent does not need context from future steps to execute the current one.

## Why It Matters

Context window pollution from irrelevant information is a primary failure mode for multi-step agent workflows. Loading an entire workflow specification into context means the agent carries instructions for steps 5-12 while executing step 1 — wasting tokens and increasing the risk of the agent prematurely acting on future instructions.

The step-file pattern enforces information isolation at the file level. The agent literally cannot see future steps because they are not loaded. This is more reliable than prompt-level instructions to "ignore steps you haven't reached yet" because the information is physically absent from context.

## Why People Are Using It

Observed in [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.2.2 — see [[bmad-method-analysis]] for structural details.

The validator rules (STEP-05, SEQ-01) indicate this was learned through failure — the rules exist because agents were forward-loading and skipping steps in earlier iterations. The enforcement mechanism (validator rules checked at runtime) is more robust than prompt-based guardrails.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Single-file workflow with section markers | One file with all steps; agent instructed to focus on current section | Simple workflows where context overhead is acceptable |
| Dynamic context loading via tool calls | Agent requests next step via a tool when ready | When step ordering is conditional/branching rather than strictly linear |
| Checkpoint-based workflow | Save/restore state at defined checkpoints without step-file isolation | When steps have complex interdependencies requiring shared context |

## Potential Improvements

- Define a standard step-file schema that other frameworks could adopt (goal, inputs, instructions, halt conditions, next-step pointer)
- Explore branching step files — conditional next-step based on step output
- Add a step-level context budget metric: how many tokens does each step consume, and what is the ceiling?

## Potential Failure Modes

- **Cross-step context loss**: If step 3 produces information needed in step 7, and the agent has no mechanism to persist that information, it is lost when step 3 is unloaded
- **Step granularity misjudgment**: Too coarse and you lose the isolation benefit; too fine and you pay overhead for many small file loads
- **Validator rule circumvention**: If the validator only checks file loads (not semantic references), an agent could reference future-step concepts from its training data without technically loading the file
- **Linear-only limitation**: Strict sequential enforcement (SEQ-01) may not accommodate workflows with legitimate parallelism or conditional branching
- **Maintenance overhead**: 12 separate files per workflow is more to maintain than one workflow definition, especially when step interfaces change
