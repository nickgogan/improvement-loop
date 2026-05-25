---
title: "Writing Agent Specifications"
type: "guideline"
category: "Intent Engineering"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-05-25"
author: "claude"
source_findings:
  - "agent-clarification-over-assumption-pattern"
  - "agent-context-kiss-commandments-minimum-viable"
  - "four-discipline-prompt-evaluator"
  - "goal-backward-verification"
  - "multidimensional-success-criteria-smart"
  - "context-gap-task-vs-job"
  - "intent-based-meta-routing-skill"
  - "project-specific-custom-skills-for-repeated-task"
  - "stop-rules-as-execution-boundaries"
source_dd:
  - "DD-81"
  - "DD-78"
tags:
  - "guide"
  - "intent-engineering"
  - "agent-specification"
  - "context-engineering"
contract:
  preconditions: "You are building or refactoring an agent that will perform non-trivial autonomous work (3+ tool calls, 2+ minutes, or decisions the agent must make without human input). You understand the agent's domain well enough to classify its decisions by blast radius."
  invariants: "Every agent spec produced using this guide includes at minimum: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, stop rules, and a context supply plan. Templates are filled in completely — no placeholder fields left as 'TBD'."
  governance: "The spec template is a governed artifact. Changes to required fields require DD-level review. Completed specs are retained as audit records. This guide is owned by Meta-System knowledge layer and updated when new intent engineering findings are integrated."
  recovery: "If an agent fails or produces unacceptable output, review the spec before investigating agent behavior. Missing or ambiguous spec fields — especially stop rules, context supply, acceptance criteria, and autonomy classifications — are the most common root cause. Fix the spec and re-run."
---

# Writing Agent Specifications

How to define what an agent should do, what it should protect, what it can decide on its own, and how you'll know it worked. This guide turns eleven research patterns into a single procedure for writing agent specs that are precise enough to be verifiable and flexible enough to handle novel situations.

## When to Use This Guide

- You are defining a new agent, skill, or recurring autonomous task
- You are refactoring an existing agent that drifts, over-asks, or produces off-target output
- You are writing a handoff prompt, build spec, or SKILL.md
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

**9. Intent routing scales agent systems.** When a skill library grows past a handful of entries, the "which skill applies?" problem becomes real. A meta-routing layer that classifies user intent and dispatches to the right specialized workflow eliminates the need for users to memorize the catalog.

---

## Procedure

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
- Never auto-deploy findings to meta-system/knowledge/: enforced via pipeline
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

---

## Related Guides

- **Acceptance criteria to eval assertions:** The acceptance criteria in Step 5 become the binary assertions in *Building Agent Evaluation Suites* (G4), Step 2.
- **Task contracts to tool registries:** The task contract schema in Step 5b maps to the tool registry design in *Designing Agent Tools* (G5), Step 1.
- **Intent specification to prompt resilience:** Prompts that reinforce intent should follow the three model-agnostic properties in *Model-Resilient Prompt Engineering* (G8), Step 1.
- **Subagent specs to memory directives:** A subagent's `memory: user|project|local` declaration and curation directive are specification-level decisions; see *Session Persistence and Memory* (G7), Step 1.4 and the Subagent Memory Directory Setup template for how to declare them in a subagent's contract.
- **Context gap to context management:** The context supply plan in Step 2a feeds into the context loading strategies in *Managing Agent Context* (G2).
- **Skill packaging to tool design:** Skills packaged in Step 6 follow the structural patterns in *Designing Agent Tools* (G5) for invocation, validation, and versioning.

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
