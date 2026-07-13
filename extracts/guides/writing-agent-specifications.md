---
title: "Writing Agent Specifications"
type: "guideline"
category: "Intent Engineering"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-19"
updated: "2026-07-13"
author: "claude"
source_findings:
  - "acceptance-criteria-as-verifiable-eval-anchor"
  - "agent-clarification-over-assumption-pattern"
  - "agent-context-kiss-commandments-minimum-viable"
  - "autonomy-gradient-not-binary-delegation"
  - "context-enrichment-for-task-clarity"
  - "context-gap-task-vs-job"
  - "four-discipline-prompt-evaluator"
  - "goal-backward-verification"
  - "health-metrics-vs-hard-constraints-distinction"
  - "human-ai-seam-identification-three-question-rubric"
  - "intent-based-meta-routing-skill"
  - "intent-engineering-framework-seven-part-agent-inten"
  - "multidimensional-success-criteria-smart"
  - "plans-that-carry-their-own-contract"
  - "project-specific-custom-skills-for-repeated-task"
  - "role-registry-prompt-hook-routing-backstop"
  - "spec-first-agent-briefs-prompt-craft-context-inten"
  - "stop-rules-as-execution-boundaries"
  - "task-contract-pattern-schema-first-agent"
  - "unknowns-reduction-phase-anchored-technique-set"
  - "war-game-plan-format-for-executor-handoff"
source_dd:
  - "DD-81"
  - "DD-78"
tags:
  - "guide"
  - "intent-engineering"
  - "agent-specification"
  - "context-engineering"
  - "plan-contracts"
contract:
  preconditions: "You are building or refactoring an agent that will perform non-trivial autonomous work (3+ tool calls, 2+ minutes, or decisions the agent must make without human input). You understand the agent's domain well enough to classify its decisions by blast radius."
  invariants: "Every agent spec produced using this guide includes at minimum: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, stop rules, and a context supply plan. Plan artifacts handed to context-isolated executors additionally carry their own contract: verbatim global constraints, per-task interfaces, and explicit failure handling. Templates are filled in completely — no placeholder fields left as 'TBD'."
  governance: "The spec template is a governed artifact. Changes to required fields require DD-level review. Completed specs are retained as audit records. This guide is owned by Meta-System knowledge layer and updated when new intent engineering findings are integrated."
  recovery: "If an agent fails or produces unacceptable output, review the spec before investigating agent behavior. Missing or ambiguous spec fields — especially stop rules, context supply, acceptance criteria, and autonomy classifications — are the most common root cause. Fix the spec and re-run."
---

# Writing Agent Specifications

How to define what an agent should do, what it should protect, what it can decide on its own, and how you'll know it worked. This guide synthesizes the knowledge base's intent-engineering pattern cluster into a single procedure for writing agent specs that are precise enough to be verifiable and flexible enough to handle novel situations — from deciding which work should cross to the agent at all, through the intent spec itself, to the plan artifact you hand a context-isolated executor.

## When to Use This Guide

- You are deciding whether a candidate workflow should be delegated to an agent at all — and which parts must stay human
- You are defining a new agent, skill, or recurring autonomous task
- You are refactoring an existing agent that drifts, over-asks, or produces off-target output
- You are writing a handoff prompt, build spec, or SKILL.md
- You are writing a plan that context-isolated implementers or a cheaper executor model will run without you
- You want to move from "it usually works" to "I can verify it works"
- You are converting a repeated multi-step process into a reusable skill specification
- You are designing a routing layer that dispatches to specialized agent workflows

**Do not use for:** one-shot conversational prompts, simple lookups, or tasks where the cost of writing a spec exceeds the cost of re-doing the work.

## Key Concepts

**1. Intent is what determines how an agent acts when instructions run out.** Context without intent is noise. A well-specified agent doesn't need exhaustive instructions for every scenario — it has enough intent to make aligned decisions in novel situations.

**2. Tasks succeed where jobs fail — the context gap.** An agent excels at tasks (bounded work with all context provided) but fails at jobs (open-ended work requiring organizational memory the agent was never given). The gap between a task and a job is missing context: unwritten decisions, informal agreements, historical constraints, stakeholder politics. Every agent spec must identify what context the agent needs that exists only in human heads — and plan how to supply it.

**3. Not all boundaries are equal.** Health metrics steer the agent's reasoning ("don't degrade test coverage"). Hard constraints are enforced outside the prompt ("never delete production data" — enforced via filesystem permissions). Mixing them weakens both.

**4. Autonomy is per-decision, not per-agent.** The same agent may have full autonomy for formatting decisions and require human approval for schema changes. Classify decisions by blast radius and reversibility, not by task complexity.

**5. Stop rules are execution boundaries, not suggestions.** Explicit halt conditions, escalation triggers, and completion criteria are the most commonly omitted spec component. Without them, agents loop indefinitely, declare premature completion, or silently degrade. Stop rules must be defined before deployment, not discovered during failure.

**6. Acceptance criteria make verification objective.** If a third party can't evaluate whether the output is acceptable, the spec is incomplete. "Output should be good" is not a criterion. "Output contains a summary under 200 words with at least 3 cited sources" is.

**7. Contracts prevent hallucination at boundaries.** When agents interact with other agents or consume structured input, explicit schemas prevent drift, ambiguity, and boundary-crossing hallucination.

**8. Repeated tasks earn skill specifications.** When you find yourself invoking the same multi-step process more than twice — with the same domain context, file paths, and procedure — encode it as a reusable skill specification. The first investment in specifying the skill pays back every subsequent invocation by eliminating re-establishment of context.

**9. Intent routing scales agent systems.** When a skill library grows past a handful of entries, the "which skill applies?" problem becomes real. A meta-routing layer that classifies user intent and dispatches to the right specialized workflow eliminates the need for users to memorize the catalog. When no single front-door agent owns intake, a deterministic prompt-time backstop (registry + hook) is the one place routing can still happen reliably.

**10. The seam comes before the spec.** Before specifying what an agent should do, partition the candidate workflow: which parts stay human (problem identification, standards, direction), which cross to the AI (playbook-executable execution), and which are joint. A spec written before the seam is located automates the wrong things — usually nice-to-haves instead of the avoided-but-important work where delegation actually pays.

**11. Plans handed to isolated executors must carry their own contract.** Information loss at agent boundaries is the documented killer of multi-agent pipelines. A plan dispatched to context-isolated implementers must front-load what they would otherwise re-derive or miss: project-wide constraints copied verbatim into the plan, per-task interfaces with exact signatures, and pre-simulated failure handling (expected observations, failure signals, countermoves, abort conditions). Author the contract once at the point of maximum context; don't pay the re-derivation cost N times with N chances of divergence.

---

## Procedure

### Step 0: Locate the Human/AI Seam

Before specifying anything, decide which parts of the candidate workflow should cross to the agent at all. Three selection questions locate high-leverage delegation targets:

| Question | What It Surfaces |
|----------|------------------|
| **What are you avoiding?** | Procrastinated-but-important work signals a complicated, energy-expensive first hurdle — exactly where an agent unlocking the start changes outcomes. This counters the default of automating nice-to-haves that nobody looks at again. |
| **What would you hire for?** | If you could onboard an intern with a playbook, that playbook onboards an agent. If you can't write the playbook, the work isn't ready to delegate. |
| **What moves the North Star?** | Tie workflow selection to your declared goal, not to what's easy to spin up. |

The output is not a yes/no on automation — it is a **seam map**: a partition of the workflow into human-owned, AI-owned, and joint parts. Problem identification, standards, and direction stay on the human side; playbook-executable execution crosses to the AI.

```markdown
## Seam Map — {{WORKFLOW_NAME}}

| # | Workflow Part | Owner | Rationale |
|---|--------------|-------|-----------|
| 1 | {{PART}} | Human | {{REQUIRES_JUDGMENT_STANDARDS_OR_DIRECTION}} |
| 2 | {{PART}} | AI | {{PLAYBOOK_EXECUTABLE}} |
| 3 | {{PART}} | Joint | {{HUMAN_GATES_AI_EXECUTES}} |
```

Working the rubric also forces you to articulate where you're blocked and why — surfacing tacit structure that makes the eventual spec specific. Only the AI-owned and joint parts proceed to Step 1; re-apply the rubric periodically, because seams move as agent capability grows.

**Beware:** avoidance is not the same as delegable. Some avoided work is avoided precisely because it requires human judgment or authority — the parts that must not cross the seam.

### Step 1: Assess the Context Gap

Before writing any spec, determine whether the agent is performing a task or a job:

| | Task | Job |
|---|---|---|
| **Context source** | Provided in the prompt/files | Must be supplied from organizational memory |
| **Scope** | Bounded — clear start and end | Open-ended — judgment calls about what matters |
| **Missing knowledge** | None (or easily retrieved) | Unwritten decisions, informal agreements, historical constraints |
| **Spec requirement** | Standard (Step 2 onward) | Must include explicit context supply plan (Step 2a) |

**The litmus test:** If an experienced colleague could not perform this work using only the information in the prompt — if they would need "to have been there" — the agent has a context gap that must be addressed in the spec.

For tasks: proceed to Step 2.
For jobs: complete Step 2a (Context Supply Plan) before proceeding.

#### Step 1a: Reduce Your Own Unknowns

The context gap covers what the *agent* is missing; this step covers what *you* are missing. Before writing the intent spec, run the elicitation techniques matched to the kind of unknown you have:

| Technique | Unknown It Attacks | How |
|-----------|-------------------|-----|
| **Blind-spot pass** | Unknown unknowns | Ask the model directly: "Do a blind-spot pass to help me find my relevant unknown unknowns" — with context on who you are and what you already know |
| **Prototype-to-react** | Unknown knowns (criteria you'd recognize but can't articulate) | Request several wildly different mock directions with fake data; react to them instead of describing requirements from scratch |
| **Interview-me** | Known unknowns | "Interview me one question at a time about anything ambiguous; prioritize questions where my answer would change the architecture" |
| **References-as-spec** | Articulation gaps | Hand over working source code that implements the behavior you want — richer than screenshots or prose descriptions |

Calibrate by instructional balance: over-specification blocks the agent's ability to pivot; under-specification forces it to assume. Run only the techniques matched to unknowns actually present — running every pass on every task is technique theater that inflates cost and delays work the agent could just do.

### Step 2: Define the Agent's Intent

Start with why this agent exists. The seven-part intent structure ensures you cover all the dimensions that determine agent behavior:

| Component | Question It Answers |
|-----------|-------------------|
| Objective | What problem is this agent solving, and why does it matter? |
| Desired Outcomes | What 2-4 measurable results indicate success? |
| Health Metrics | What must not degrade while the agent pursues its objective? |
| Strategic Context | What broader system does this agent operate within? |
| Constraints | What are the hard boundaries (enforced) and soft guidance (steering)? |
| Decision Types / Autonomy | Which decisions can the agent make vs. must escalate? |
| Stop Rules | Under what conditions should the agent halt, escalate, or declare completion? |

**The critical order:** Objective and outcomes first — they anchor everything else. Constraints and autonomy second — they define the operating envelope. Stop rules last — they define when to exit the envelope entirely.

#### Step 2a: Context Supply Plan (for jobs, not tasks)

When the context gap assessment reveals organizational knowledge the agent needs but won't have, enumerate it explicitly:

| Context Needed | Where It Lives Today | How to Supply It | Freshness Requirement |
|----------------|---------------------|------------------|----------------------|
| `{{CONTEXT_ITEM}}` | `{{CURRENT_LOCATION}}` (e.g., "in Sarah's head", "informal Slack agreement") | `{{SUPPLY_METHOD}}` (e.g., decision log, elicitation interview, knowledge base entry) | `{{FREQUENCY}}` (e.g., once, per-quarter, per-invocation) |

If a context item cannot be supplied, the spec must either: (a) narrow the agent's scope to exclude decisions requiring that context, or (b) add an escalation trigger for situations where the missing context would affect the outcome.

### Step 3: Enrich the Task Context

For every invocation of the agent (not just the definition), provide four types of context:

| Context Field | What to Provide | Why It Matters |
|---------------|-----------------|----------------|
| **Purpose** | What will the results be used for? | Constrains what the agent emphasizes and what it can safely omit |
| **Audience** | Who will consume the output? | Sets appropriate depth, assumed knowledge, and tone |
| **Workflow Position** | Where does this task sit in a larger workflow? | Helps the agent preserve information for downstream steps |
| **Success Criteria** | What does "done well" look like, as measurable thresholds? | Gives the agent a concrete target, not an implicit quality bar |

Without these fields, the agent optimizes for generic output. With them, the model can make informed tradeoffs between competing qualities (brevity vs. completeness, depth vs. accessibility).

### Step 4: Design the Boundary System

#### 4a: Classify Constraints

Every constraint in your system falls into one of two categories. Classify each one and route it to the correct enforcement mechanism:

| Category | What It Is | Enforcement Layer | Example |
|----------|-----------|-------------------|---------|
| **Health Metric** | What must not degrade while pursuing the objective | Prompt layer (steering) — checked automatically | "Test coverage must not drop below 80%" |
| **Hard Constraint** | Non-negotiable rule where violation is catastrophic | Orchestration layer (enforced) — filesystem permissions, hooks, API gates | "Never modify files outside system boundary" |

**The key test:** If a constraint matters enough to be hard, it must not depend on the LLM choosing to follow a prompt instruction. Prompt-layer instructions are probabilistic guidance; orchestration-layer enforcement is deterministic compliance.

For each hard constraint, verify that a non-prompt enforcement mechanism exists. If it doesn't, either build one or reclassify the constraint as a health metric.

#### 4b: Define Autonomy Levels

Classify each decision type the agent will encounter using two criteria:

| | Low Blast Radius | High Blast Radius |
|---|---|---|
| **Reversible** | Full Autonomy — act without notification | Guarded — act then report |
| **Irreversible** | Guarded — act then report | Human-Required — escalate |

The four levels:

1. **Full Autonomy:** Agent decides and acts. No notification. (File formatting, index updates, log entries.)
2. **Guarded:** Agent decides and acts, then reports. (Code refactoring within a module, configuration changes with rollback.)
3. **Proposal-First:** Agent proposes, waits for approval, then acts. (New Design Decisions, cross-system changes, API modifications.)
4. **Human-Required:** Agent escalates. Cannot act. (Schema migrations, production deployments, data deletions.)

#### 4c: Define Stop Rules

Stop rules define three types of execution boundaries. Every agent spec must include at least one of each type:

| Type | What It Defines | Examples |
|------|----------------|----------|
| **Halt conditions** | When the agent stops working entirely | "Stop if error rate exceeds 5%"; "Stop after 3 unsuccessful attempts at the same approach"; "Stop if token budget reaches 80%" |
| **Escalation triggers** | When the agent hands off to a human | "Escalate if the customer mentions legal action"; "Escalate if proposed change touches more than 5 files"; "Escalate if ambiguity exceeds threshold" |
| **Completion criteria** | How the agent knows it is genuinely done | "Complete when all tests pass and diff is under 200 lines"; "Complete when all URLs are processed and delta report is written" |

**The enforcement principle:** "The reasoning layer proposes. The orchestration layer enforces." Stop rules in the prompt guide the agent's judgment; stop rules in the orchestration layer (timeouts, token budgets, iteration caps) guarantee enforcement. Prompt-only stop rules are necessary but not sufficient for high-autonomy agents.

**Dynamic stop rules:** Simple tasks warrant tight iteration caps (stop after 2 attempts). Complex debugging tasks warrant generous ones (stop after 10 attempts). Token budget awareness — firing when remaining context window drops below a threshold — prevents degraded output from exhausted context.

### Step 5: Write Acceptance Criteria and Contracts

#### 5a: Acceptance Criteria

For every recurring task the agent performs, define:

1. **Pass/fail conditions** evaluable by a third party who did not write the prompt. State as verifiable checks, not subjective judgments.
2. **3-5 eval cases** — known-good examples of expected output quality. Include typical cases, edge cases, and at least one case targeting the hardest criterion.
3. **Iteration anchor** — save the spec with its criteria and eval cases. When the model changes, rerun eval cases to detect regressions. Iterate the spec, not individual prompts.

#### 5b: Task Contracts (for multi-agent systems)

When the agent interacts with other agents or produces structured output consumed by downstream systems, define an explicit contract:

| Contract Component | What to Define |
|-------------------|---------------|
| **Input Schema** | Structure, types, required fields the agent expects to receive |
| **Output Schema** | Structure, types, required fields the agent must produce |
| **Quality Constraints** | Must-constraints (reject on violation) and should-constraints (warn) |
| **Cost/Latency Budgets** | Maximum tokens, wall-clock time, API calls |
| **Allowed Tools** | Explicit tool allowlist per agent role |

Contracts must be validated at runtime, not just documented. A contract that exists only as documentation provides no protection.

### Step 6: Consider Skill Packaging

If the agent spec describes a task that will be invoked repeatedly with the same domain context, consider packaging it as a skill specification:

**Skill candidate signals:**
- The task is performed more than twice per week
- It requires project-specific file paths, schemas, or vocabulary
- The setup context (what files exist, what conventions apply) is the same each time
- Multiple steps must execute in sequence with domain-specific logic

**Skill spec additions (beyond the base intent spec):**
- Invocation pattern: the command or trigger phrase that activates the skill
- Domain context preamble: project-specific knowledge embedded once (file locations, naming conventions, schema shapes)
- Procedure steps: ordered sequence of actions with decision points
- Version coupling: how the skill evolves when the project structure changes

**For systems with multiple skills:** add a routing layer that maps user intent keywords to specific skill files. This eliminates the need for users to know the skill catalog. The routing table is a simple keyword-to-skill mapping in markdown — deterministic, not AI-classified.

**For systems with no front-door agent:** when multiple entry points exist and no single agent owns intake, add a deterministic routing backstop at the one chokepoint every request passes — prompt submission. A prompt-submit hook scores each incoming prompt against a role/skill registry read straight from disk. Design properties that matter:

- **Whole-word token matching only** — substring matching fires on incidental hits and injects noise
- **Gate, not ranking** — inject context only when the best match clears a threshold; never a best-effort guess
- **Fail-open always** — on missing registry, malformed input, or any error, do nothing and never block the request; a routing aid must never become an availability risk

Because it is plain token scoring on a disk file, the backstop cannot hallucinate, cannot drift with model changes, costs nothing when it doesn't fire, and catches prompts that description-based routing misses — including brand-new skills not yet integrated into the catalog.

### Step 7: Structure Executor Handoffs as Carried Contracts

When the spec becomes a plan that context-isolated implementers — subagents, parallel workers, or a cheaper executor model — will run without you, the plan itself must carry the binding context. Constraints that live only in the spec never reach an implementer who is handed one task's brief.

**Four structural requirements:**

1. **Global Constraints header.** Copy project-wide requirements *verbatim* from the spec into a mandatory plan header block. Every implementer and reviewer sees them regardless of which task they hold.
2. **Per-task Interfaces block.** Each task declares what it Consumes and Produces with exact signatures, so an implementer who sees nothing but its own task knows what its neighbors expect and provide.
3. **Task right-sizing.** A task is the smallest unit that carries its own test cycle and is worth a fresh reviewer's gate — sized to the review architecture, not to effort estimates.
4. **No placeholders.** TBDs and "figure out later" entries are plan failures, caught by plan self-review before dispatch.

**Order the plan by decision volatility.** Lead with the decisions the human reviewer is most likely to tweak — data model changes, type interfaces, anything user-facing — and bury trusted mechanical work at the bottom. The reviewer's attention lands where it changes the outcome.

**Pre-simulate the failure branches (war-gaming).** Linear plans assume a blue-sky scenario; executors then improvise at exactly the moments improvisation is most expensive. For high-stakes handoffs, have the strongest available model war-game the plan move by move:

| Element | What It Defines |
|---------|----------------|
| **Expected observation** | What you see if the move worked — and if it didn't |
| **Failure signal + countermove** | The most likely failure per move, its observable signal, and the pre-decided response |
| **Fork triggers** | "If you observe X, take route A" — explicit conditions at every branch |
| **Blocked-variables ledger** | Assumptions the planner could not resolve, listed as placeholders the human must fill before dispatch |
| **Abort conditions** | Errors or missing access that should stop execution entirely (these are the plan-level twin of the spec's halt conditions from Step 4c) |

Name the executing model or agent in the plan so the war-game is tailored to that executor's documented behavior. Cap the war-game depth explicitly — branch simulation is unbounded, and a plan that is 90% boilerplate branches buries the few decision-relevant forks.

**Log deviations, don't relitigate.** Instruct the executor: on hitting an edge case that forces deviation from the plan, pick the conservative option, log it under a Deviations section in an implementation-notes file, and keep going. The human reviews deviations at the gate instead of being interrupted per incident.

**The payoff is measured.** Upstream A/B evidence: structured carried-contract plans needed one fix round versus two-to-four for unstructured control plans — which also shipped a real bug. The structure downstream agents used to re-derive on every dispatch is authored once, at the point of maximum context.

**Maintenance obligations:** verbatim-copied constraints fork from the spec when the spec is amended mid-execution — give the copy an update trigger. Exact Consumes/Produces signatures written at plan time can prematurely freeze design decisions an implementer would legitimately revise — mark signatures that are contracts versus signatures that are current best guesses.

---

## Templates

### Agent Intent Specification

```yaml
# {{AGENT_NAME}} — Intent Specification

## Objective
{{PROBLEM_STATEMENT}}
{{WHY_IT_MATTERS}}

## Context Supply Plan
# Include only if context gap assessment identified missing organizational knowledge
| Context Needed | Where It Lives Today | How to Supply It | Freshness |
|----------------|---------------------|------------------|-----------|
| {{CONTEXT_ITEM}} | {{CURRENT_LOCATION}} | {{SUPPLY_METHOD}} | {{FREQUENCY}} |

## Desired Outcomes (2-4 max)
1. {{OUTCOME_1}} — measured by: {{METRIC_1}}
2. {{OUTCOME_2}} — measured by: {{METRIC_2}}
3. {{OUTCOME_3}} — measured by: {{METRIC_3}}

## Health Metrics
- {{METRIC_NAME}}: must not drop below {{THRESHOLD}}
  Measurement: {{HOW_CHECKED}} at {{CHECK_FREQUENCY}}
- {{METRIC_NAME_2}}: must not exceed {{THRESHOLD_2}}
  Measurement: {{HOW_CHECKED_2}} at {{CHECK_FREQUENCY_2}}

## Strategic Context
- Part of: {{BROADER_SYSTEM_OR_WORKFLOW}}
- Upstream: {{WHAT_FEEDS_INTO_THIS_AGENT}}
- Downstream: {{WHAT_CONSUMES_THIS_AGENT_OUTPUT}}
- Owner: {{WHO_IS_RESPONSIBLE}}

## Constraints
### Hard (orchestration-enforced)
- {{CONSTRAINT}}: enforced via {{MECHANISM}}
- {{CONSTRAINT_2}}: enforced via {{MECHANISM_2}}

### Steering (prompt-layer)
- Must: {{REQUIREMENT}}
- Must-not: {{PROHIBITION}}
- Prefer: {{PREFERENCE}}

## Decision Types / Autonomy
| Decision | Blast Radius | Reversibility | Autonomy Level |
|----------|-------------|---------------|----------------|
| {{DECISION_TYPE_1}} | {{LOW/MED/HIGH}} | {{YES/NO}} | {{FULL/GUARDED/PROPOSAL/HUMAN}} |
| {{DECISION_TYPE_2}} | {{LOW/MED/HIGH}} | {{YES/NO}} | {{FULL/GUARDED/PROPOSAL/HUMAN}} |

## Acceptance Criteria
- [ ] {{CRITERION_1}} — verifiable by: {{METHOD}}
- [ ] {{CRITERION_2}} — verifiable by: {{METHOD}}
- [ ] {{CRITERION_3}} — verifiable by: {{METHOD}}

## Eval Cases
1. {{CASE_DESCRIPTION}}: expected output is {{EXPECTED}}
2. {{EDGE_CASE}}: expected behavior is {{EXPECTED}}
3. {{HARDEST_CRITERION_CASE}}: expected output is {{EXPECTED}}

## Stop Rules
### Halt Conditions
- {{HALT_1}} (e.g., error rate exceeds threshold)
- {{HALT_2}} (e.g., token budget reaches 80%)
- {{HALT_3}} (e.g., N unsuccessful attempts at same approach)

### Escalation Triggers
- {{ESCALATION_1}} (e.g., ambiguity the agent cannot resolve)
- {{ESCALATION_2}} (e.g., policy conflict detected)
- {{ESCALATION_3}} (e.g., change crosses scope boundary)

### Completion Criteria
- {{COMPLETION_1}} (e.g., all tests pass and diff is under N lines)
- {{COMPLETION_2}} (e.g., all input items processed and report written)
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `AGENT_NAME` | string | Yes | Descriptive name for the agent or skill |
| `PROBLEM_STATEMENT` | string | Yes | The problem this agent solves |
| `WHY_IT_MATTERS` | string | Yes | Why solving this problem is valuable |
| `CONTEXT_ITEM` | string | Conditional | Organizational knowledge the agent needs (required if context gap exists) |
| `CURRENT_LOCATION` | string | Conditional | Where the context lives today (human heads, informal channels, etc.) |
| `SUPPLY_METHOD` | string | Conditional | How to transfer the context to the agent |
| `OUTCOME_N` | string | Yes (2-4) | Measurable result indicating success |
| `METRIC_N` | string | Yes | How the outcome is measured |
| `METRIC_NAME` | string | Yes (1+) | Health metric name |
| `THRESHOLD` | string | Yes | Minimum/maximum acceptable value |
| `HOW_CHECKED` | string | Yes | Measurement mechanism (automated preferred) |
| `CHECK_FREQUENCY` | string | Yes | When the metric is checked (per-action, per-session, continuous) |
| `BROADER_SYSTEM_OR_WORKFLOW` | string | Yes | What this agent is part of |
| `CONSTRAINT` | string | No (0+) | Hard constraint statement |
| `MECHANISM` | string | Conditional | Enforcement mechanism (required if constraint exists) |
| `DECISION_TYPE_N` | string | Yes (1+) | A class of decisions the agent makes |
| `CRITERION_N` | string | Yes (1+) | Verifiable pass/fail condition |
| `HALT_N` | string | Yes (1+) | Condition that halts execution entirely |
| `ESCALATION_N` | string | Yes (1+) | Condition that triggers handoff to human |
| `COMPLETION_N` | string | Yes (1+) | Condition that indicates genuine completion |

### Task Context Block

For each invocation of the agent, prepend this context block:

```yaml
## Task Context
- Purpose: {{WHAT_RESULTS_WILL_BE_USED_FOR}}
- Audience: {{WHO_CONSUMES_OUTPUT}} — assumes {{KNOWLEDGE_LEVEL}}
- Position: Step {{N}} of {{TOTAL}} in {{WORKFLOW_NAME}}
  - Receives from step {{N-1}}: {{INPUT_DESCRIPTION}}
  - Feeds into step {{N+1}}: {{OUTPUT_REQUIREMENTS}}
- Success Criteria:
  - {{MEASURABLE_CRITERION_1}}
  - {{MEASURABLE_CRITERION_2}}
```

### Context Gap Assessment Worksheet

Use when determining whether an agent is performing a task or a job:

```markdown
## Context Gap Assessment — {{AGENT_NAME}}

### What the agent needs to know
| # | Knowledge Item | Available in Prompt/Files? | Where It Actually Lives | Classification |
|---|---------------|---------------------------|------------------------|----------------|
| 1 | {{KNOWLEDGE_ITEM}} | {{YES/NO}} | {{LOCATION}} | Task context / Organizational memory |

### Gap Analysis
- Items available: {{COUNT}} (these are task-appropriate)
- Items missing: {{COUNT}} (these make it a job)
- Critical gaps (would cause wrong output): {{LIST}}

### Resolution
- [ ] Narrow scope to exclude decisions requiring gap #{{N}}
- [ ] Add escalation trigger for situations requiring gap #{{N}}
- [ ] Build context supply mechanism for gap #{{N}}: {{METHOD}}
```

### Skill Specification Addendum

When packaging a repeated task as a reusable skill, append to the base intent spec:

```yaml
## Skill Packaging

### Invocation
- Command: {{TRIGGER_PHRASE}} (e.g., "/creature-forge", "/deploy-service")
- Intent keywords: {{KEYWORD_LIST}} (for routing table registration)

### Domain Context (embedded once)
- Project structure: {{RELEVANT_FILE_PATHS_AND_CONVENTIONS}}
- Schema/vocabulary: {{DOMAIN_TERMS_AND_THEIR_MEANINGS}}
- Dependencies: {{WHAT_MUST_EXIST_BEFORE_THIS_SKILL_RUNS}}

### Procedure
1. {{STEP_1}} — decision point: {{WHAT_TO_DECIDE}}
2. {{STEP_2}} — output: {{WHAT_IS_PRODUCED}}
3. {{STEP_3}} — validation: {{HOW_TO_VERIFY_STEP_OUTPUT}}

### Version Coupling
- Breaks when: {{WHAT_PROJECT_CHANGES_INVALIDATE_THIS_SKILL}}
- Update trigger: {{HOW_TO_DETECT_STALENESS}}
```

### Plan Handoff Contract

Use when dispatching a plan to context-isolated implementers or a cheaper executor model (Step 7):

```markdown
# Plan — {{PLAN_NAME}}
Executor: {{EXECUTOR_MODEL_OR_AGENT}} (plan tailored to this executor's documented behavior)

## Global Constraints (copied verbatim from {{SPEC_SOURCE}})
- {{CONSTRAINT_1_VERBATIM}}
- {{CONSTRAINT_2_VERBATIM}}
<!-- Update trigger: re-copy on any amendment to {{SPEC_SOURCE}} -->

## Blocked Variables (human fills before dispatch)
| Variable | Why the Planner Could Not Resolve It | Value |
|----------|--------------------------------------|-------|
| {{BLOCKED_VAR}} | {{REASON}} | ___ |

## Tasks
<!-- Right-sizing: each task is the smallest unit that carries its own
     test cycle and is worth a fresh reviewer's gate. No TBDs. -->
<!-- Ordering: decision-volatile tasks first (data models, interfaces,
     user-facing); trusted mechanical work last. -->

### Task {{N}}: {{TASK_NAME}}
- Consumes: {{INPUT_WITH_EXACT_SIGNATURE}} (from Task {{M}})
- Produces: {{OUTPUT_WITH_EXACT_SIGNATURE}} (for Task {{P}})
- Steps: {{ORDERED_STEPS}}
- Expected observation on success: {{WHAT_YOU_SEE_IF_IT_WORKED}}
- Most likely failure: {{FAILURE}} — signal: {{OBSERVABLE_SIGNAL}} —
  countermove: {{PRE_DECIDED_RESPONSE}}
- Fork trigger: if you observe {{CONDITION}}, take {{ALTERNATE_ROUTE}}
- Verify: {{TASK_LEVEL_TEST}}

## Deviations Protocol
On any edge case forcing deviation: pick the conservative option, log it
under "Deviations" in {{NOTES_FILE}}, and keep going.

## Abort Conditions
- {{ABORT_1}} (e.g., missing access to a required system)
- {{ABORT_2}} (e.g., a Global Constraint cannot be satisfied)
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `PLAN_NAME` | string | Yes | Descriptive name for the plan |
| `EXECUTOR_MODEL_OR_AGENT` | string | Yes | Who runs this plan — the war-game and phrasing are tailored to it |
| `SPEC_SOURCE` | string | Yes | The spec document constraints are copied from (the update-trigger anchor) |
| `CONSTRAINT_N_VERBATIM` | string | Yes (1+) | Project-wide requirement, copied word-for-word — never paraphrased |
| `BLOCKED_VAR` | string | No (0+) | Assumption the planner could not resolve; human supplies the value pre-dispatch |
| `TASK_NAME` | string | Yes (1+) | Task title; task sized to its own test cycle and review gate |
| `INPUT/OUTPUT_WITH_EXACT_SIGNATURE` | string | Yes | Exact interface signatures — what neighbors provide and expect |
| `WHAT_YOU_SEE_IF_IT_WORKED` | string | Yes | Observable success state per task or move |
| `FAILURE` / `OBSERVABLE_SIGNAL` / `PRE_DECIDED_RESPONSE` | string | High-stakes plans | War-gamed failure branch per move; cap depth explicitly |
| `CONDITION` / `ALTERNATE_ROUTE` | string | Conditional | Explicit fork trigger where the plan branches |
| `NOTES_FILE` | string | Yes | Where the executor logs deviations (e.g., implementation-notes.md) |
| `ABORT_N` | string | Yes (1+) | Condition that stops execution entirely |

### Constraint Classification Worksheet

Use when auditing an existing system's constraints:

```markdown
## Constraint Audit — {{SYSTEM_NAME}}

| # | Constraint Statement | Current Location | Classification | Enforcement Mechanism | Gap? |
|---|---------------------|-----------------|----------------|----------------------|------|
| 1 | {{CONSTRAINT}} | {{WHERE_IT_LIVES_NOW}} | Health / Hard | {{MECHANISM_OR_NONE}} | {{YES_IF_HARD_WITH_NO_MECHANISM}} |

### Action Items
- [ ] Build enforcement for constraint #{{N}}: {{WHAT_TO_BUILD}}
- [ ] Reclassify constraint #{{N}}: {{WHY}}
- [ ] Add measurement for health metric #{{N}}: {{WHAT_TO_MEASURE}}
```

---

## Worked Example: MetaSystem `/research-loop` Agent

A filled-in agent intent specification for a real MetaSystem agent.

```yaml
# Research Loop Agent — Intent Specification

## Objective
Extract actionable findings from research sources (blogs, papers, videos,
repos) into the Improvement Loop knowledge base.
Why: The IL's value is proportional to the breadth and depth of its KB.
Without systematic research intake, the KB stagnates and MetaSystem's
guidance drifts from frontier practice.

## Context Supply Plan
| Context Needed | Where It Lives Today | How to Supply It | Freshness |
|----------------|---------------------|------------------|-----------|
| What counts as "actionable" for MetaSystem | Nick's head + constitution | Constitution doc + IL governance rules | Stable |
| Current KB coverage gaps | Distributed across findings | research-dimensions.md registry | Per-session |
| Priority of research dimensions | Nick's prioritization | PROGRESS.md attention queue | Per-session |

## Desired Outcomes (3)
1. New findings extracted — measured by: count of new finding files created
2. Existing findings enriched — measured by: count of findings with updated
   evidence or new source links
3. Source coverage expanded — measured by: count of new source entries with
   complete metadata

## Health Metrics
- Deduplication rate: must not create duplicate findings for the same pattern
  Measurement: grep for same-problem links across new findings, post-session
- Source diversity: no single authority should account for >30% of new findings
  in a session
  Measurement: authority distribution check at session end

## Strategic Context
- Part of: Improvement Loop pipeline (stage 1 of 4)
- Upstream: URLs provided by Nick, /watch-blogs triage, /watch-upstream triage
- Downstream: /identify-artifacts consumes P1/P2 findings
- Owner: Improvement Loop system

## Constraints
### Hard (orchestration-enforced)
- Never modify files outside systems/improvement-loop/: enforced via CLAUDE.md
  scope rules (aspirational — no filesystem enforcement yet)
- Never auto-deploy findings to knowledge/: enforced via pipeline
  stage gates (DD-29)

### Steering (prompt-layer)
- Must: cite specific evidence for every claim in a finding
- Must-not: create findings based on a single blog post with no corroboration
- Prefer: full transcript extraction over summary-based extraction for
  high-value sources

## Decision Types / Autonomy
| Decision | Blast Radius | Reversibility | Autonomy Level |
|----------|-------------|---------------|----------------|
| Create new finding | Low | Yes (delete file) | Full Autonomy |
| Update existing finding | Low | Yes (git revert) | Full Autonomy |
| Create new source | Low | Yes (delete file) | Full Autonomy |
| Change evidence_strength | Med | Yes (revert) | Guarded |
| Change priority | Med | Yes (revert) | Guarded |
| Merge/split findings | Med | Partially | Proposal-First |
| Modify authority tier | High | Yes but consequential | Human-Required |

## Acceptance Criteria
- [ ] Every new finding has: name, summary, category, evidence_strength,
      at least 1 source link — verifiable by: frontmatter field check
- [ ] No duplicate findings — verifiable by: grep for existing finding
      with same-problem relationship
- [ ] Every source entry has: URL, authority link, finding links —
      verifiable by: frontmatter field check
- [ ] Delta report produced — verifiable by: file exists in loop-reports/

## Eval Cases
1. Blog post with 3 extractable patterns: expected 3 findings + 1 source
2. Blog post that duplicates existing finding: expected 0 new findings,
   1 finding updated with new source link
3. Video URL requiring transcript: expected transcript fetch before
   extraction, not summary-only

## Stop Rules
### Halt Conditions
- Session token budget exceeded (80% of context window)
- Health metric violation (duplicate created, single-authority dominance)

### Escalation Triggers
- Source contradicts an existing finding with strong evidence
- Finding would change a P1 priority classification
- Uncertain whether a pattern is genuinely new or a restatement

### Completion Criteria
- All URLs in the input set have been processed
- Delta report is written to loop-reports/
- No unresolved escalation triggers remain
```

---

## Worked Example: Plan Handoff Contract for a KB Backfill

A filled-in (abridged) plan handoff contract for dispatching a two-task finding-backfill to a parallel subagent.

```markdown
# Plan — Backfill source links on wave-3 findings
Executor: Sonnet subagent (tailored: explicit file paths, no judgment calls
on priority fields)

## Global Constraints (copied verbatim from CLAUDE.md + governance rules)
- "Frontmatter is the source of truth."
- "Never write counts of DDs, IB items, or other entries into prose."
- "Researcher writes to Findings, Sources, and Authorities only."
<!-- Update trigger: re-copy on any amendment to governance/agent-rules.md -->

## Blocked Variables (human fills before dispatch)
| Variable | Why the Planner Could Not Resolve It | Value |
|----------|--------------------------------------|-------|
| authority tier for kome.ai | New source; tier assignment is Nick-gated | ___ |

## Tasks
### Task 1: Link findings to sources
- Consumes: list of 12 finding stems (from dispatch prompt)
- Produces: `sources:` frontmatter arrays updated in those 12 files,
  each entry an existing research-sources/ stem
- Expected observation on success: rg 'sources: \[\]' over the 12 files
  returns zero hits
- Most likely failure: source file stem mismatch — signal: wikilink
  target does not exist on disk — countermove: log to Deviations, skip
  the link, do NOT create a new source file
- Fork trigger: if a finding already has sources, append — never replace
- Verify: kb_parser round-trip parses all 12 files without error

### Task 2: Reverse links (sources → findings)
- Consumes: the 12 updated finding files (from Task 1)
- Produces: `findings:` arrays on each touched source file
- Expected observation on success: every Task-1 link has a reverse link
- Verify: linkage-repair audit reports zero unidirectional links

## Deviations Protocol
On any edge case: pick the conservative option, log it under "Deviations"
in operations/plans/backfill-notes.md, and keep going.

## Abort Conditions
- kb_parser fails to parse any target file (schema drift — stop, report)
- Any write would touch a file outside research-findings/ or research-sources/
```

---

## Pitfalls

### 1. Omitting stop rules entirely
The most commonly skipped component. Without stop rules, agents exhibit three failure modes: infinite loops (retrying a failing approach because nothing says stop), premature completion (declaring "done" without meeting completion criteria), and silent degradation (output quality declining because the agent is past the point of useful work). Define all three types: halt conditions, escalation triggers, and completion criteria.

### 2. Stop rules only in the prompt layer
Prompt-layer stop rules guide the agent's judgment but are not deterministic. High-autonomy agents need orchestration-layer enforcement too: timeouts, token budgets, iteration caps. The principle: "The reasoning layer proposes. The orchestration layer enforces."

### 3. Ignoring the context gap
Specifying a job as if it were a task — assuming the agent has organizational context it was never given. The agent will fill the gap with plausible-sounding confabulation. Before writing the spec, assess whether the work requires knowledge that exists only in human heads. If it does, either supply that context explicitly or narrow the scope.

### 4. Health metrics without measurement
"Don't degrade test coverage" is meaningless without automated coverage measurement. Every health metric needs three things: a threshold, a measurement mechanism, and a check frequency. If you can't measure it, it's aspirational prose, not a health metric.

### 5. All constraints in the prompt layer
If a constraint matters enough to be called "hard," it should not depend on the LLM choosing to follow a prompt instruction. Prompt compliance is probabilistic. Move safety-critical constraints to the orchestration layer: filesystem permissions, pre-tool-use hooks, CI gates, API authentication.

### 6. Binary autonomy ("ask everything" or "do everything")
A single gate level for all decisions either bottlenecks the agent on trivial work or lets it make catastrophic decisions without oversight. Classify decisions by blast radius and reversibility, then assign the appropriate autonomy level to each type.

### 7. Acceptance criteria that only the prompter can evaluate
"Output should be good" is not verifiable by a third party. Every criterion must be evaluable by someone who did not write the prompt. If you can't hand the criteria to a colleague and have them evaluate the output independently, the criteria are too vague.

### 8. Stale eval cases
Eval cases curated for one model version may not represent current best output quality. When models change, rerun eval cases. If they pass but output quality has visibly improved, update the baselines. Stale cases create false confidence.

### 9. Contracts as documentation only
A task contract that exists only in a markdown file provides no protection against boundary violations. Contracts must be validated at runtime — before input is processed and after output is produced. Documentation-only contracts give false confidence.

### 10. Over-specifying simple tasks
Not every agent interaction needs a seven-part intent spec, four-field context block, and formal acceptance criteria. The spec overhead should be proportional to the task's blast radius and duration. A trivial file lookup does not need a constraint classification worksheet.

### 11. Re-specifying the same task repeatedly
If you find yourself writing the same context block and procedure for the third time, the task has earned a skill specification. Encode the domain context once; invoke it by command thereafter. The maintenance cost of a skill file is lower than the cumulative cost of re-establishing context on every invocation.

### 12. Happy-path plans for isolated executors
A plan that assumes linearity looks logical but doesn't say what to do when reality deviates — so the executor improvises at exactly the moments improvisation is most expensive. Plans dispatched to context-isolated or cheaper executors need pre-simulated failure branches: expected observations, failure signals, countermoves, fork triggers, and abort conditions. Constraints that live only in the spec never reach an implementer handed one task's brief — copy them into the plan verbatim.

### 13. Carried contracts that silently go stale
Verbatim-copied constraints fork from the spec when the spec is amended mid-execution, and exact interface signatures written at plan time can freeze design decisions an implementer would legitimately revise. Give every copied block an update trigger, and distinguish signatures that are contracts from signatures that are current best guesses. The counterweight to plan bloat is task right-sizing — if per-task briefs are no longer extractable, the carried contract has outgrown the plan.

### 14. Delegating by capability instead of by seam
"The agent *can* do this" is not the question — "should this leave the human" is. Automating what is easy to spin up produces morning-brief workflows nobody reads, while the avoided-but-important work stays manual. Conversely, some avoided work is avoided because it requires human judgment or authority — the parts that must not cross. Run the seam questions (Step 0), produce an explicit seam map, and re-run it as capability grows: seams move, and a static partition goes stale.

### 15. Unknowns-reduction theater
Running every elicitation pass (blind-spot, interview-me, prototypes, references) on every task inflates cost and delays work the agent could just do. Match technique to the unknowns actually present — and be honest about which kind you have. The inverse failure is skipping elicitation on architecture-shaping work and letting the agent fill your unarticulated criteria with plausible assumptions.

---

## Related Guides

- **Acceptance criteria to eval assertions:** The acceptance criteria in Step 5 become the binary assertions in *Building Agent Evaluation Suites* (G4), Step 2.
- **Task contracts to tool registries:** The task contract schema in Step 5b maps to the tool registry design in *Designing Agent Tools* (G5), Step 1.
- **Intent specification to prompt resilience:** Prompts that reinforce intent should follow the three model-agnostic properties in *Model-Resilient Prompt Engineering* (G8), Step 1.
- **Subagent specs to memory directives:** A subagent's `memory: user|project|local` declaration and curation directive are specification-level decisions; see *Session Persistence and Memory* (G7), Step 1.4 and the Subagent Memory Directory Setup template for how to declare them in a subagent's contract.
- **Context gap to context management:** The context supply plan in Step 2a feeds into the context loading strategies in *Managing Agent Context* (G2).
- **Skill packaging to tool design:** Skills packaged in Step 6 follow the structural patterns in *Designing Agent Tools* (G5) for invocation, validation, and versioning.
- **Carried contracts to context defense:** The plan handoff contract in Step 7 is the dispatch-time counterpart of file-mediated handoff and context-residency economics in *Defending Against Context Degradation* (G2b) — the plan carries the context so the executor's window doesn't have to.
- **Executor handoffs to orchestration:** Which work gets dispatched to isolated executors at all — and how planner and executor roles divide — is an architecture decision; see *Agent Architecture Decisions* (G3).

---

## Contract

### Preconditions
- You are building or refactoring an agent that will perform non-trivial autonomous work (3+ tool calls, 2+ minutes of work, or decisions the agent must make without human input).
- You understand the agent's domain well enough to classify its decisions by blast radius and reversibility.
- You have access to the system where the agent will operate (to identify existing constraints and enforcement mechanisms).

### Invariants
- Every agent spec produced using this guide includes at minimum: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, stop rules (all three types), and a context supply plan (if context gap exists).
- Templates are filled in completely — no placeholder fields left as "TBD" or "TODO."
- Hard constraints have corresponding enforcement mechanisms outside the prompt layer.
- Acceptance criteria are evaluable by a third party without access to the prompter's intent.
- Stop rules include at least one halt condition, one escalation trigger, and one completion criterion.
- Plans dispatched to context-isolated executors carry their own contract: global constraints copied verbatim, per-task Consumes/Produces interfaces, abort conditions, and a deviations protocol. Blocked variables are filled by the human before dispatch, never left as silent assumptions.

### Governance
- This guide is owned by the Meta-System knowledge layer.
- The spec template is a governed artifact. Changes to required fields require DD-level review.
- Completed specs are retained alongside agent output as audit records of what was requested vs. what was produced.
- This guide is updated when new intent engineering findings are integrated from the Improvement Loop.

### Recovery
- If an agent fails or produces unacceptable output, review the spec first. Missing or ambiguous spec fields — especially stop rules, context supply, acceptance criteria, and autonomy classifications — are the most common root cause. Fix the spec and re-run before investigating agent behavior.
- If the spec was adequate and the agent still failed, the issue is agent capability, not specification. Escalate to the agent's owner.
- If acceptance criteria are discovered to be unverifiable by a third party, rewrite them as concrete pass/fail conditions before the next evaluation cycle.
- If the agent confabulates organizational context it was never given, add a context supply plan and re-scope the spec.
