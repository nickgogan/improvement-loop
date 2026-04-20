---
title: "Writing Agent Specifications"
type: "guideline"
category: "Intent Engineering"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-19"
author: "claude"
source_findings:
  - "intent-engineering-framework-seven-part-agent-inten"
  - "autonomy-gradient-not-binary-delegation"
  - "health-metrics-vs-hard-constraints-distinction"
  - "acceptance-criteria-as-verifiable-eval-anchor"
  - "spec-first-agent-briefs-prompt-craft-context-inten"
  - "context-enrichment-for-task-clarity"
  - "task-contract-pattern-schema-first-agent"
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
  invariants: "Every agent spec produced using this guide includes at minimum: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, and stop rules. Templates are filled in completely — no placeholder fields left as 'TBD'."
  governance: "The spec template is a governed artifact. Changes to required fields require DD-level review. Completed specs are retained as audit records. This guide is owned by Meta-System knowledge layer and updated when new intent engineering findings are integrated."
  recovery: "If an agent fails or produces unacceptable output, review the spec before investigating agent behavior. Missing or ambiguous spec fields — especially acceptance criteria, constraints, and autonomy classifications — are the most common root cause. Fix the spec and re-run."
---

# Writing Agent Specifications

How to define what an agent should do, what it should protect, what it can decide on its own, and how you'll know it worked. This guide turns seven research patterns into a single procedure for writing agent specs that are precise enough to be verifiable and flexible enough to handle novel situations.

## When to Use This Guide

- You are defining a new agent, skill, or recurring autonomous task
- You are refactoring an existing agent that drifts, over-asks, or produces off-target output
- You are writing a handoff prompt, build spec, or SKILL.md
- You want to move from "it usually works" to "I can verify it works"

**Do not use for:** one-shot conversational prompts, simple lookups, or tasks where the cost of writing a spec exceeds the cost of re-doing the work.

## Key Concepts

**1. Intent is what determines how an agent acts when instructions run out.** Context without intent is noise. A well-specified agent doesn't need exhaustive instructions for every scenario — it has enough intent to make aligned decisions in novel situations.

**2. Not all boundaries are equal.** Health metrics steer the agent's reasoning ("don't degrade test coverage"). Hard constraints are enforced outside the prompt ("never delete production data" — enforced via filesystem permissions). Mixing them weakens both.

**3. Autonomy is per-decision, not per-agent.** The same agent may have full autonomy for formatting decisions and require human approval for schema changes. Classify decisions by blast radius and reversibility, not by task complexity.

**4. Acceptance criteria make verification objective.** If a third party can't evaluate whether the output is acceptable, the spec is incomplete. "Output should be good" is not a criterion. "Output contains a summary under 200 words with at least 3 cited sources" is.

**5. Contracts prevent hallucination at boundaries.** When agents interact with other agents or consume structured input, explicit schemas prevent drift, ambiguity, and boundary-crossing hallucination.

---

## Procedure

### Step 1: Define the Agent's Intent

Start with why this agent exists. The seven-part intent structure ensures you cover all the dimensions that determine agent behavior:

| Component | Question It Answers |
|-----------|-------------------|
| Objective | What problem is this agent solving, and why does it matter? |
| Desired Outcomes | What 2-4 measurable results indicate success? |
| Health Metrics | What must not degrade while the agent pursues its objective? |
| Strategic Context | What broader system does this agent operate within? |
| Constraints | What are the hard boundaries (enforced) and soft guidance (steering)? |
| Decision Types / Autonomy | Which decisions can the agent make vs. must escalate? |
| Stop Rules | Under what conditions should the agent halt? |

**The critical order:** Objective and outcomes first — they anchor everything else. Constraints and autonomy second — they define the operating envelope. Stop rules last — they define when to exit the envelope entirely.

### Step 2: Enrich the Task Context

For every invocation of the agent (not just the definition), provide four types of context:

| Context Field | What to Provide | Why It Matters |
|---------------|-----------------|----------------|
| **Purpose** | What will the results be used for? | Constrains what the agent emphasizes and what it can safely omit |
| **Audience** | Who will consume the output? | Sets appropriate depth, assumed knowledge, and tone |
| **Workflow Position** | Where does this task sit in a larger workflow? | Helps the agent preserve information for downstream steps |
| **Success Criteria** | What does "done well" look like, as measurable thresholds? | Gives the agent a concrete target, not an implicit quality bar |

Without these fields, the agent optimizes for generic output. With them, the model can make informed tradeoffs between competing qualities (brevity vs. completeness, depth vs. accessibility).

### Step 3: Design the Boundary System

#### 3a: Classify Constraints

Every constraint in your system falls into one of two categories. Classify each one and route it to the correct enforcement mechanism:

| Category | What It Is | Enforcement Layer | Example |
|----------|-----------|-------------------|---------|
| **Health Metric** | What must not degrade while pursuing the objective | Prompt layer (steering) — checked automatically | "Test coverage must not drop below 80%" |
| **Hard Constraint** | Non-negotiable rule where violation is catastrophic | Orchestration layer (enforced) — filesystem permissions, hooks, API gates | "Never modify files outside system boundary" |

**The key test:** If a constraint matters enough to be hard, it must not depend on the LLM choosing to follow a prompt instruction. Prompt-layer instructions are probabilistic guidance; orchestration-layer enforcement is deterministic compliance.

For each hard constraint, verify that a non-prompt enforcement mechanism exists. If it doesn't, either build one or reclassify the constraint as a health metric.

#### 3b: Define Autonomy Levels

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

### Step 4: Write Acceptance Criteria and Contracts

#### 4a: Acceptance Criteria

For every recurring task the agent performs, define:

1. **Pass/fail conditions** evaluable by a third party who did not write the prompt. State as verifiable checks, not subjective judgments.
2. **3-5 eval cases** — known-good examples of expected output quality. Include typical cases, edge cases, and at least one case targeting the hardest criterion.
3. **Iteration anchor** — save the spec with its criteria and eval cases. When the model changes, rerun eval cases to detect regressions. Iterate the spec, not individual prompts.

#### 4b: Task Contracts (for multi-agent systems)

When the agent interacts with other agents or produces structured output consumed by downstream systems, define an explicit contract:

| Contract Component | What to Define |
|-------------------|---------------|
| **Input Schema** | Structure, types, required fields the agent expects to receive |
| **Output Schema** | Structure, types, required fields the agent must produce |
| **Quality Constraints** | Must-constraints (reject on violation) and should-constraints (warn) |
| **Cost/Latency Budgets** | Maximum tokens, wall-clock time, API calls |
| **Allowed Tools** | Explicit tool allowlist per agent role |

Contracts must be validated at runtime, not just documented. A contract that exists only as documentation provides no protection.

---

## Templates

### Agent Intent Specification

```yaml
# {{AGENT_NAME}} — Intent Specification

## Objective
{{PROBLEM_STATEMENT}}
{{WHY_IT_MATTERS}}

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

## Escalation Triggers
- {{TRIGGER_1}} (e.g., ambiguity the agent cannot resolve)
- {{TRIGGER_2}} (e.g., policy conflict detected)
- {{TRIGGER_3}} (e.g., change feels risky or crosses scope boundary)

## Stop Rules
- {{STOP_CONDITION_1}} (e.g., budget exceeded)
- {{STOP_CONDITION_2}} (e.g., health metric violated)
- {{STOP_CONDITION_3}} (e.g., scope expanded beyond original objective)
```

**Variable Reference:**

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `AGENT_NAME` | string | Yes | Descriptive name for the agent or skill |
| `PROBLEM_STATEMENT` | string | Yes | The problem this agent solves |
| `WHY_IT_MATTERS` | string | Yes | Why solving this problem is valuable |
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
| `STOP_CONDITION_N` | string | Yes (1+) | Condition that halts execution |

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

## Escalation Triggers
- Source contradicts an existing finding with strong evidence
- Finding would change a P1 priority classification
- Uncertain whether a pattern is genuinely new or a restatement

## Stop Rules
- Session token budget exceeded
- No more unprocessed URLs in the input set
- Health metric violation (duplicate created, single-authority dominance)
```

---

## Pitfalls

### 1. Omitting stop rules
The most commonly skipped component. Without stop rules, agents run until they exhaust their context window or the user intervenes. Define explicit exit conditions: budget exceeded, objective met, health metric violated, scope expanded beyond original bounds.

### 2. Health metrics without measurement
"Don't degrade test coverage" is meaningless without automated coverage measurement. Every health metric needs three things: a threshold, a measurement mechanism, and a check frequency. If you can't measure it, it's aspirational prose, not a health metric.

### 3. All constraints in the prompt layer
If a constraint matters enough to be called "hard," it should not depend on the LLM choosing to follow a prompt instruction. Prompt compliance is probabilistic. Move safety-critical constraints to the orchestration layer: filesystem permissions, pre-tool-use hooks, CI gates, API authentication.

### 4. Binary autonomy ("ask everything" or "do everything")
A single gate level for all decisions either bottlenecks the agent on trivial work or lets it make catastrophic decisions without oversight. Classify decisions by blast radius and reversibility, then assign the appropriate autonomy level to each type.

### 5. Acceptance criteria that only the prompter can evaluate
"Output should be good" is not verifiable by a third party. Every criterion must be evaluable by someone who did not write the prompt. If you can't hand the criteria to a colleague and have them evaluate the output independently, the criteria are too vague.

### 6. Stale eval cases
Eval cases curated for one model version may not represent current best output quality. When models change, rerun eval cases. If they pass but output quality has visibly improved, update the baselines. Stale cases create false confidence.

### 7. Contracts as documentation only
A task contract that exists only in a markdown file provides no protection against boundary violations. Contracts must be validated at runtime — before input is processed and after output is produced. Documentation-only contracts give false confidence.

### 8. Over-specifying simple tasks
Not every agent interaction needs a seven-part intent spec, four-field context block, and formal acceptance criteria. The spec overhead should be proportional to the task's blast radius and duration. A trivial file lookup does not need a constraint classification worksheet.

---

## Related Guides

- **Acceptance criteria → eval assertions:** The acceptance criteria in Step 4 become the binary assertions in *Building Agent Evaluation Suites* (G4), Step 2.
- **Task contracts → tool registries:** The task contract schema in Step 4b maps to the tool registry design in *Designing Agent Tools* (G5), Step 1.
- **Intent specification → prompt resilience:** Prompts that reinforce intent should follow the three model-agnostic properties in *Model-Resilient Prompt Engineering* (G8), Step 1.

---

## Contract

### Preconditions
- You are building or refactoring an agent that will perform non-trivial autonomous work (3+ tool calls, 2+ minutes of work, or decisions the agent must make without human input).
- You understand the agent's domain well enough to classify its decisions by blast radius and reversibility.
- You have access to the system where the agent will operate (to identify existing constraints and enforcement mechanisms).

### Invariants
- Every agent spec produced using this guide includes at minimum: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, and stop rules.
- Templates are filled in completely — no placeholder fields left as "TBD" or "TODO."
- Hard constraints have corresponding enforcement mechanisms outside the prompt layer.
- Acceptance criteria are evaluable by a third party without access to the prompter's intent.

### Governance
- This guide is owned by the Meta-System knowledge layer.
- The spec template is a governed artifact. Changes to required fields require DD-level review.
- Completed specs are retained alongside agent output as audit records of what was requested vs. what was produced.
- This guide is updated when new intent engineering findings are integrated from the Improvement Loop.

### Recovery
- If an agent fails or produces unacceptable output, review the spec first. Missing or ambiguous spec fields — especially acceptance criteria, constraints, and autonomy classifications — are the most common root cause. Fix the spec and re-run before investigating agent behavior.
- If the spec was adequate and the agent still failed, the issue is agent capability, not specification. Escalate to the agent's owner.
- If acceptance criteria are discovered to be unverifiable by a third party, rewrite them as concrete pass/fail conditions before the next evaluation cycle.
