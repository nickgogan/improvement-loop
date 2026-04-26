---
title: "Deep Plan — 4-Agent Planning Pipeline"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "extract-deep-plan-prompt-as-custom-skill"
extraction_date: "2026-04-19"
last_change_session: 44
last_change_sl: "session-44-codifier-extraction-run"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic coding systems requiring deterministic, high-quality planning passes"
    - "any agent workflow where a planner-critic-refiner-finalizer pipeline adds value"
    - "teams wanting to bypass server-controlled planning variant randomization"
  platform_coupling: "specific:claude-code"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — produces a plan document; no system state is modified"
  auditability: "high — critique log is appended to the final plan as a collapsible artifact; every blocking concern is tracked to resolution"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "Clear task description provided. Read access to context files. Reasoning-class model available."
  invariants: "All four stages execute in order. Critic pass is never skipped. All blocking concerns resolved before finalization. No CoT scaffolding in any prompt."
  governance: "Owner: Meta-System. Skill changes require review. Critic criteria extensible without DD. Upstream prompt drift requires periodic re-extraction."
  recovery: "Malformed stage output: retry once, then surface partial results. User rejects plan: re-enter at critic with feedback. Upstream drift: file IB item to re-extract."
tags:
  - "extracted-artifact"
  - "skill"
---

# Deep Plan — 4-Agent Planning Pipeline

**Source:** [[extract-deep-plan-prompt-as-custom-skill]]
**Form:** skill
**Extraction date:** 2026-04-19

A deterministic planning skill implementing the 4-agent pipeline (planner, critic, refiner, finalizer) reverse-engineered from Claude Code's Ultra Plan deep variant. Removes server-side A/B randomization and enables MetaSystem-specific critic criteria.

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `task_description` | string | Yes | What needs to be planned — the goal, not the method. |
| `context_files` | array[string] | No | File paths to load as planning context (e.g., CLAUDE.md, constitution, relevant DDs). |
| `critic_criteria` | array[string] | No | Additional domain-specific criteria for the critic pass. Defaults to MetaSystem standard criteria. |
| `output_path` | string | No | Where to write the final plan. Defaults to stdout. |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `plan` | markdown | The refined, finalized plan document. |
| `critique_log` | markdown | The critic's concerns and the refiner's responses (appended to the plan as a collapsible section). |

## Steps

### Step 1: Context Assembly
- Load `task_description` and any `context_files`.
- If no `context_files` provided, auto-load: project CLAUDE.md, constitution, PROGRESS.md.
- Assemble a unified context block for downstream agents.

### Step 2: Planner
- **Role:** Generate an initial plan.
- **Prompt structure:** Goal (the task) + Constraints (from context) + Context (assembled block).
- **Output:** A structured plan with numbered steps, dependencies, and expected outputs per step.
- **Must not:** Use CoT scaffolding or prescribed reasoning (per reasoning-model anti-pattern rule).

### Step 3: Critic
- **Role:** Identify weaknesses, gaps, risks, and unstated assumptions in the planner's output.
- **Standard criteria:**
  - Does the plan violate any constitutional principles?
  - Are there missing dependencies or ordering errors?
  - Are success criteria defined for each step?
  - Are there scope boundary violations?
- **Domain criteria:** Apply any `critic_criteria` provided as input.
- **Output:** A numbered list of concerns, each tagged as `[blocking]` or `[suggestion]`.

### Step 4: Refiner
- **Role:** Address every `[blocking]` concern from the critic. May accept or reject `[suggestion]` items with rationale.
- **Output:** A revised plan that resolves all blocking concerns, with a change log showing what was modified and why.

### Step 5: Finalizer
- **Role:** Polish the refined plan into a clean, actionable document.
- **Actions:**
  - Remove internal scaffolding and meta-commentary.
  - Ensure consistent formatting.
  - Verify all steps have clear owners, inputs, outputs, and success criteria.
  - Append the critique log as a collapsible `<details>` section.
- **Output:** The final plan document.

### Step 6: Delivery
- If `output_path` is specified: write the final plan to that path.
- Otherwise: return the plan as the skill's output.

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Planner produces an empty or trivially short plan | Step count < 2 or word count < 100 | Re-run planner with explicit constraint: "minimum 3 steps with dependencies" |
| Critic finds no concerns | Concern list is empty | Accept — a clean plan is valid. Log that critic pass was clean. |
| Critic produces only `[suggestion]` items (no `[blocking]`) | No `[blocking]` tags in output | Skip refiner — pass directly to finalizer with suggestions noted. |
| Refiner fails to address a `[blocking]` concern | Diff between critic concerns and refiner change log shows unresolved `[blocking]` items | Re-run refiner with explicit instruction to address the missed concern. Maximum 1 retry. |
| Context too large for single prompt | Token count exceeds model context window | Summarize context files before assembly. Flag to user that full context was not used. |

## Contract

### Preconditions
- A clear task description is provided (not vague or meta — "make things better" is rejected).
- The invoking agent has read access to any specified context files.
- A reasoning-class model is available for all four agent passes.

### Invariants
- All four pipeline stages execute in order: planner -> critic -> refiner -> finalizer.
- The critic pass is never skipped.
- Every `[blocking]` concern from the critic is resolved or explicitly escalated before finalization.
- No CoT scaffolding or prescribed reasoning in any agent prompt (per reasoning-model anti-pattern rule).

### Governance
- **Owner:** Meta-System.
- **Modification gate:** Skill definition changes require review. Critic criteria can be extended without a DD.
- **Upstream dependency:** Based on Claude Code Ultra Plan deep variant. Prompt may drift as Anthropic updates — periodic re-extraction recommended.

### Recovery
- If any pipeline stage produces malformed output: retry that stage once. If retry fails, surface partial results to the user with a clear indication of which stage failed.
- If the user rejects the final plan: re-enter at Step 3 (critic) with user feedback as additional critic criteria.
- If upstream Ultra Plan prompt changes significantly: file an IB item to re-extract and compare.
