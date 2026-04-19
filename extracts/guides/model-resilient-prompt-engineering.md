---
title: "Model-Resilient Prompt Engineering"
type: "guideline"
category: "Prompt Craft"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-19"
author: "claude"
source_findings:
  - "model-agnostic-prompting-three-properties"
  - "reasoning-model-anti-pattern-prescribed-reasoning"
  - "extract-deep-plan-prompt-as-custom-skill"
  - "advisor-executor-api-pattern"
  - "task-specific-model-routing-table-march-2026-bench"
  - "brevity-constraints-reverse-llm-performance"
  - "advanced-elicitation-techniques-library"
  - "oneshot-infrastructure-setup-prompt-pattern"
  - "cot-fails-without-inductive-generalization"
  - "negative-constraints-as-probabilistic-output-collapse"
  - "yaml-template-dual-structure"
  - "design-evaluate-dual-phase-prompting-framework"
  - "prompt-as-policy-version-control-and-cicd-for-agen"
  - "bmad-outcome-based-skill-rewrite-pattern"
  - "frontier-release-compression-march-2026"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "prompt-engineering"
  - "model-resilience"
contract:
  preconditions: "You are writing or auditing prompts for agent systems that may run on different models or survive model upgrades. You understand the distinction between reasoning models (extended thinking, internalized CoT) and standard models. You have access to test the prompts against acceptance criteria."
  invariants: "Prompts tell the model what to produce, not how to think. No prescribed reasoning paths in prompts for reasoning models. Constraints are expressed as boundaries (negative) rather than aspirations (positive) for high-priority rules. Model selection is task-based, not provider-based. Prompts are versioned artifacts with testable acceptance criteria."
  governance: "Prompts are versioned and tested against acceptance criteria after model upgrades. Model routing tables are reviewed when new benchmark data is available. Anti-pattern audits are conducted after major model releases. This guide is owned by Meta-System knowledge layer."
  recovery: "If a prompt breaks after a model upgrade: audit against the three durability properties and remove prescribed reasoning patterns. If model costs are too high: apply the Advisor-Executor pattern or reroute to cheaper models for bulk work. If prompt performance varies across models: check for violated durability properties first, then check constraint specificity. If brevity constraints degrade complex reasoning: switch to dynamic brevity (verbose for planning, terse for execution)."
---

# Model-Resilient Prompt Engineering

How to write prompts that survive model upgrades, route tasks to the right model, and manage prompts as versioned policy. This guide synthesizes three concerns that are usually treated separately -- prompt durability, model selection, and prompt lifecycle -- because they interact: a prompt that encodes model-specific reasoning patterns breaks on upgrade, costs too much on the wrong model, and cannot be versioned meaningfully if it drifts with every release.

## When to Use This Guide

- You are writing prompts for skills, agents, or recurring tasks that must survive model upgrades
- You are auditing existing prompts after a model update broke behavior
- You need to choose which model to assign to which agent role
- Agent costs are too high and you want to optimize model routing
- You are designing prompt templates for reuse across teams or systems
- You want to version-control prompts with testable acceptance criteria

---

## Key Concepts

### Prompt Durability

**Three properties make prompts model-agnostic.** Prompts that survive across model generations share three testable properties: (1) they tell the model *what* to produce, not *how* to think; (2) they surface human judgment *before* the model generates; (3) they keep evaluation responsibility on the human side. These properties emerged from testing 19 techniques across GPT-5.4, Claude 4.6, and Gemini 3.1 -- the common thread across every technique that survived reasoning models.

**Five classic techniques degrade reasoning models.** Chain-of-thought ("think step by step"), few-shot examples, self-consistency runs, least-to-most decomposition, and skeleton-of-thought all conflict with reasoning models' internalized reasoning. They prescribe a thinking process the model already performs better on its own.

**CoT has a hard ceiling.** Chain-of-thought amplifies existing reasoning capabilities but cannot create new ones. When a model lacks the right inductive generalization for a task, no amount of additional reasoning tokens helps. This means reasoning models are not universal amplifiers -- they improve tasks within training distribution but add nothing for genuinely novel abstraction.

**Outcome-based instructions outperform procedural ones.** Rewriting skill instructions from step-by-step procedures ("do step 1, then step 2") to outcome specifications ("ensure X is true, ensure Y is complete") cuts token consumption approximately 50% while making prompts more resilient to model changes. The model selects its own execution path rather than following scaffolding that encodes assumptions about its reasoning strategy.

### Constraint Engineering

**Negative constraints collapse the output space.** Explicit negative instructions ("never begin with an apology," "do not use technical jargon in summaries") create hard probabilistic walls that remove undesirable output regions, producing more reliable behavior changes than positive guidance ("try to be confident," "aim for clarity"). Use negative constraints for the highest-priority behavioral rules where consistency matters most.

**Brevity constraints improve accuracy.** Research across 31 models and 1,500 problems shows that forcing brief responses improves accuracy by up to 26 percentage points. Larger models suffer from "spontaneous scale-dependent verbosity" -- RLHF training rewards thoroughness, which introduces error accumulation through over-elaboration. A conciseness constraint is a quality intervention, not just a token-saving measure.

**Design before prompting, evaluate after.** Every prompt interaction has two phases requiring human judgment: a *Design* phase (choosing the lens, prioritizing constraints, curating evidence) and an *Evaluate* phase (judging whether the output matches intent). Skipping the Design phase produces prompts without intentionality. Skipping the Evaluate phase means the human cannot detect when the model's reasoning diverges from their goals.

### Prompt Architecture

**Templates should encode interaction protocols, not just output schemas.** YAML templates that embed coaching instructions alongside the document schema ("which questions to ask per section, what level of detail to push for, when to move on") produce consistently higher-quality outputs than templates that only define structure. The dual structure makes the agent both a producer and a facilitator.

**Oneshot prompts beat interactive setup.** For infrastructure and configuration tasks, a single comprehensive prompt containing all decisions, known fixes, and overrides is more reliable than an interactive back-and-forth. Each conversation turn introduces noise. A oneshot prompt also serves as living documentation -- reproducible, reviewable, and shareable.

**Elicitation techniques are a library, not a default.** Eighteen advanced techniques (tree of thought, red team/blue team, critique-and-refine, stakeholder roundtable, etc.) exist for pushing past first-pass quality. The key is selective application based on task type, not applying all techniques everywhere. Overuse wastes tokens and produces analysis paralysis.

### Model Selection

**Route by task, not by provider.** Different models excel at different task types, and the gaps are now wide enough that routing matters. March 2026 benchmarks show clear specialization: Claude Sonnet for coding, GPT-5.4 for browser automation, Gemini 3.1 Pro for abstract reasoning, Gemini Flash for batch extraction at cost floor. Using one model for everything is a documented cost mistake.

**The Advisor-Executor pattern beats single-model defaults.** Pairing Opus as a reasoning-only advisor with Sonnet as the tool-calling executor achieves higher quality at lower cost than either model alone -- SWE-Bench 74.8 vs 72.1 at roughly half the cost. The relationship is dynamic (not one-shot planning) -- the executor consults the advisor when it hits hard decisions.

**Frontier releases compress faster than routing tables update.** Five major model releases in 23 days (March 2026) means routing guidance has a shorter shelf life. The routing *structure* (task-based, not provider-based) remains stable even when specific model recommendations change. Set review cadence by release events, not calendar quarters.

### Prompt Lifecycle

**Prompts are policy artifacts.** Production prompts should carry explicit ROLE, AUTHORITY, CONSTRAINT, and FAILURE SIGNAL properties. They should be versioned with commit messages, diffed like code, and tested with automated validation before deployment. Treating prompts as informal text that lives in chat history is the prompt equivalent of unversioned infrastructure.

**Planning prompts can be extracted and customized.** Proven multi-agent planning pipelines (e.g., Claude Code's 4-agent deep plan: planner, critic, refiner, finalizer) can be reverse-engineered and run as deterministic custom skills, bypassing vendor A/B randomization and enabling domain-specific critic criteria.

---

## Procedure

### Step 1: Audit Prompts Against the Three Durability Properties

For every prompt in your system, apply three binary tests:

| Property | Test Question | If Failing |
|----------|--------------|------------|
| **Goal-oriented** | Does it say *what* to produce, or does it prescribe *how* to think? | Remove reasoning scaffolding. State the deliverable, constraints, and context only. |
| **Human judgment first** | Does it require human decisions (priorities, trade-offs, curated evidence) *before* generation? | Front-load constraints and choices into the prompt. Do not hope the model infers intent. |
| **Human-side evaluation** | Does it keep evaluation on the human side, or delegate self-assessment to the model? | Replace "verify your answer" with external acceptance criteria or a separate evaluator. |

**Techniques that satisfy all three:** structured output formats, constraint specification, role/persona assignment, context curation, negative behavioral constraints.

**Techniques that violate at least one (avoid on reasoning models):** chain-of-thought, few-shot reasoning examples, self-consistency, least-to-most decomposition, skeleton-of-thought, "check your work."

### Step 2: Remove Reasoning Anti-Patterns and Rewrite as Goal + Constraints + Context

| Anti-Pattern | Replacement |
|-------------|-------------|
| "Think step by step" | Remove entirely -- reasoning models do this internally |
| Few-shot reasoning examples | Provide output format examples only, not reasoning chains |
| "First analyze X, then consider Y, then decide Z" | "Produce a decision on Z considering X and Y" |
| "Break this into sub-problems" | State the goal; let the model decompose |
| "Check your work and verify" | Use external verification (tests, assertions, independent evaluator) |
| Step-by-step procedural skill instructions | Rewrite as outcome specifications: "ensure X is true" not "do step 1, step 2" |

When removing reasoning scaffolding, compensate with explicit constraints. Under-specifying the goal while also removing process instructions produces worse results than either approach alone.

### Step 3: Engineer Constraints for Reliability

Apply these constraint principles in priority order:

1. **Express high-priority rules as negative constraints.** "Never skip the validation step" is more reliably followed than "always remember to validate." Negative constraints collapse the output space; positive guidance merely nudges within it.

2. **Add brevity constraints for accuracy.** Include conciseness directives ("be concise, no filler," or explicit length limits) in system prompts. This improves output quality on problems where verbosity causes error accumulation -- not just token savings.

3. **Pair negatives with positive examples.** Each "never do X" should be accompanied by an example of what to do instead, so the model has a viable output path after the constraint removes the undesirable one.

4. **Scope constraints to avoid collateral damage.** "Never use technical jargon" will prevent accurate technical descriptions. Scope: "Never use technical jargon in user-facing summaries."

5. **Watch for diminishing returns.** Beyond a threshold, additional constraints add cognitive load without improving compliance. If a prompt has more than 8-10 hard constraints, prioritize and cut.

### Step 4: Structure Prompts with Design/Evaluate Phases

Before writing the prompt (Design phase):
- Choose the interpretive lens (role, persona, expertise domain)
- Prioritize trade-offs explicitly (format vs. depth, speed vs. thoroughness)
- Curate what counts as evidence (specific sources, not "use your knowledge")
- Define what a "good enough" output looks like

After receiving the output (Evaluate phase):
- Does the model's strategic frame match yours?
- Did it stay grounded in the evidence you provided?
- Is the synthesis genuine or a false compromise?
- Would a different lens have produced a better result?

This is not a one-time checklist -- it is the cognitive discipline that makes prompting work across model boundaries.

### Step 5: Route Models by Task Type

| Task Type | Recommended Model | Evidence | Relative Cost |
|-----------|------------------|----------|---------------|
| Repository-level coding, knowledge work | Claude Sonnet 4.6 | GDPval Elo 1633, SWE-bench ~79.6% | 1x |
| Complex reasoning, architectural decisions | Claude Opus 4.6 (via Advisor pattern) | SWE-Bench 74.8 with advisor vs 72.1 alone | ~0.5x (advisor) |
| Computer use, browser automation | GPT-5.4 | WebArena-Verified 67.3% | ~1.2x |
| Abstract reasoning, long-horizon math | Gemini 3.1 Pro | ARC-AGI-2 77.1% | ~1.5x |
| Extraction, batch processing | Gemini Flash | 97.1% quality, $0.003/task | ~0.1x |

**Anti-default:** Opus 4.6 costs 3.5x Sonnet with no accuracy premium on most benchmarks. Do not default to it.

**Hard ceiling reminder:** All frontier models score 0% on ARC-AGI-3 (novel abstraction). For tasks requiring genuinely novel inductive generalization, route to human judgment, not a more powerful model.

**Review cadence:** Re-evaluate when any constituent model has a major release. The routing structure (task-based) is durable; the specific model assignments are snapshots.

### Step 6: Implement the Advisor-Executor Pattern (API Applications)

For API-based applications where quality matters but Opus for everything is too expensive:

```
[Executor: Sonnet]        [Advisor: Opus]
  handles all tools    <->  reasoning guidance only
  most decisions            consulted at decision points
  $0.96/task average        full shared context
                            never makes tool calls
```

**Configuration:** Set `type: "advisor"` and `max_uses` in API calls. The executor consults the advisor when it hits a decision it cannot resolve.

**Tuning max_uses:**
- Start with 3-5 for general tasks
- Too low: executor makes avoidable mistakes at decision points
- Too high: unnecessary advisor calls increase cost without quality gain
- Monitor consultation logs to find the right level per task type

**When NOT to use:** Claude Code sessions (not API-based), tasks that are entirely routine (Sonnet alone is sufficient), tasks requiring primarily tool calls with no reasoning decisions.

### Step 7: Version and Test Prompts as Policy

Treat production prompts as versioned artifacts:

1. **Structure prompts with explicit properties:** ROLE (who the agent is), AUTHORITY (what it can do), CONSTRAINT (what it must not do), FAILURE SIGNAL (how to detect and report failure).

2. **Version with diffs:** Store prompts in version control. Write commit messages that explain *why* the prompt changed, not just *what* changed.

3. **Test before deployment:** Define acceptance criteria for each prompt. After a model upgrade, run the prompt against the acceptance criteria before deploying to production.

4. **Extract and customize proven pipelines:** When a vendor feature (like a planning mode) produces good results, extract the underlying prompt as a custom skill so you get deterministic access to the best variant and can add domain-specific criteria.

---

## Templates

### Template 1: Model-Resilient Prompt Structure

```markdown
## {{PROMPT_NAME}}

### Role
You are {{ROLE_DESCRIPTION}}.

### Authority
You may {{PERMITTED_ACTIONS}}.
You must not {{PROHIBITED_ACTIONS}}.

### Goal
Produce {{DELIVERABLE_DESCRIPTION}} that satisfies:
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
- {{CONSTRAINT_3}}

### Context
{{CURATED_CONTEXT — specific sources, files, or evidence the model should use}}

### Output Format
{{FORMAT_SPECIFICATION — structure, length, sections}}

### Failure Signal
If {{FAILURE_CONDITION}}, then {{FAILURE_ACTION — stop, escalate, report}}.
```

#### Worked Example: Research Extraction Prompt

```markdown
## Extract Research Findings

### Role
You are a research analyst extracting actionable patterns from technical sources.

### Authority
You may create new finding entries in the research-findings directory.
You must not modify existing findings, source files, or governance documents.

### Goal
Produce a structured finding entry for each distinct pattern in the source that satisfies:
- Each finding describes a single, testable pattern (not a vague observation)
- Evidence strength is assessed as Strong/Medium/Weak with justification
- Implementation notes are specific enough for a developer to act on without re-reading the source
- No duplicate of an existing KB finding (check first)

### Context
Source transcript: {{SOURCE_PATH}}
Existing findings index: systems/improvement-loop/research-findings/_index.md

### Output Format
YAML frontmatter per _schema.yaml, followed by markdown body with sections:
What It Is, Why It Matters, Why People Are Using It, Potential Failure Modes.

### Failure Signal
If the source contains fewer than 2 extractable patterns, report "low-density source"
and stop. Do not generate filler findings.
```

### Template 2: Prompt Audit Worksheet

```markdown
## Prompt Audit — {{SYSTEM_NAME}}
Date: {{AUDIT_DATE}}
Auditor: {{AUDITOR}}
Trigger: {{MODEL_UPGRADE / SCHEDULED_REVIEW / QUALITY_INCIDENT}}

### Durability Property Check
| Prompt Location | Goal-oriented (P1) | Human Judgment First (P2) | Human-side Eval (P3) | Action |
|----------------|---------------------|---------------------------|----------------------|--------|
| {{PROMPT_PATH}} | {{PASS/FAIL: detail}} | {{PASS/FAIL: detail}} | {{PASS/FAIL: detail}} | {{REMOVE/REWRITE/OK}} |

### Anti-Pattern Scan
| Location | Anti-Pattern | Current Text | Replacement |
|----------|-------------|-------------|-------------|
| {{PATH:LINE}} | {{CoT/few-shot/self-verify/decomposition/skeleton}} | "{{CURRENT_TEXT}}" | "{{REPLACEMENT_TEXT}}" |

### Constraint Quality Check
| Constraint | Type (neg/pos) | Scoped? | Collateral risk? | Action |
|-----------|----------------|---------|-------------------|--------|
| {{CONSTRAINT_TEXT}} | {{negative/positive}} | {{yes/no — scope described}} | {{risk if any}} | {{CONVERT_TO_NEGATIVE / ADD_SCOPE / OK}} |

### Model Routing
| Agent Role | Current Model | Recommended Model | Rationale |
|-----------|--------------|-------------------|-----------|
| {{ROLE}} | {{CURRENT}} | {{RECOMMENDED}} | {{BENCHMARK_EVIDENCE}} |

### Prompt Policy Properties
| Prompt | ROLE defined? | AUTHORITY defined? | CONSTRAINTS defined? | FAILURE SIGNAL defined? |
|--------|--------------|-------------------|---------------------|------------------------|
| {{PROMPT_PATH}} | {{yes/no}} | {{yes/no}} | {{yes/no}} | {{yes/no}} |
```

#### Worked Example: MetaSystem Prompt Audit

```
Prompt Audit — MetaSystem Skills
Date: 2026-04-19
Auditor: Claude (session 26)
Trigger: P2 finding integration

DURABILITY PROPERTY CHECK:
/synthesize-guide:
  P1 (goal-oriented): PASS — "Synthesize findings into guide" (goal, not process)
  P2 (human judgment first): PASS — findings pre-curated by human
  P3 (human-side eval): PASS — human reviews draft before deployment

/identify-artifacts (subagent prompt):
  P1: PASS — "Classify this finding into a form" (goal-oriented after session 24 fix)
  P2: PASS — rubric front-loaded as context
  P3: PASS — human reviews identification report

ANTI-PATTERN SCAN: None found after session 24 prompt improvement.

CONSTRAINT QUALITY CHECK:
  "Be concise" in CLAUDE.md: positive, unscoped — CONVERT to
    "Do not include filler phrases, hedging language, or restated instructions in output"
  "Never skip the Review Gate": negative, scoped — OK

MODEL ROUTING:
  Orchestrator: Opus — justified (architectural decisions, low volume)
  Subagents: Sonnet — justified (batch classification, parallel, lossy-tolerant)
  Advisor pattern: Not applicable (Claude Code, not API)

PROMPT POLICY PROPERTIES:
  /synthesize-guide: ROLE yes, AUTHORITY partial (no explicit prohibitions),
    CONSTRAINTS yes, FAILURE SIGNAL no — ADD failure signal for low-finding-count edge case
```

### Template 3: Outcome-Based Skill Rewrite

```markdown
## {{SKILL_NAME}} — Outcome Specification

### Outcomes (what must be true when the skill completes)
1. {{OUTCOME_1 — a verifiable end-state, not a step}}
2. {{OUTCOME_2}}
3. {{OUTCOME_3}}

### Constraints (boundaries, not process)
- {{CONSTRAINT_1 — "never," "must not," or "must"}}
- {{CONSTRAINT_2}}

### Context (what the skill needs to work with)
- {{CONTEXT_ITEM_1 — file, schema, or reference}}
- {{CONTEXT_ITEM_2}}

### Acceptance Criteria
- [ ] {{CRITERION_1 — binary testable}}
- [ ] {{CRITERION_2}}

### Failure Signal
If {{CONDITION}}, then {{ACTION}}.
```

#### Worked Example: Rewriting a Procedural Skill

**Before (procedural, 180 tokens):**
```
Step 1: Read the source transcript.
Step 2: Identify each distinct pattern.
Step 3: For each pattern, check the existing KB for duplicates.
Step 4: For each non-duplicate pattern, write a finding entry.
Step 5: Use the _schema.yaml for frontmatter format.
Step 6: Include all required sections.
Step 7: Save to research-findings/ directory.
Step 8: Report what was extracted.
```

**After (outcome-based, 90 tokens):**
```
Outcomes:
1. Every distinct, non-duplicate pattern in the source has a finding entry
   in research-findings/.
2. Each entry conforms to _schema.yaml frontmatter and includes all
   required sections.
3. Extraction report summarizes what was created and any duplicates skipped.

Constraints:
- Never create a finding that duplicates an existing KB entry.
- Never modify existing findings or source files.

Failure Signal:
If fewer than 2 patterns found, report "low-density source" and stop.
```

### Template 4: YAML Template with Dual Structure (Schema + Coaching)

```yaml
# {{TEMPLATE_NAME}}
# This template defines both the output structure and the interaction protocol.

sections:
  - name: "{{SECTION_1_NAME}}"
    schema:
      required_fields:
        - "{{FIELD_1}}"
        - "{{FIELD_2}}"
    coaching: |
      {{INSTRUCTION_FOR_LLM — what questions to ask the user for this section,
       what level of detail to push for, when this section is "done enough"}}

  - name: "{{SECTION_2_NAME}}"
    schema:
      required_fields:
        - "{{FIELD_3}}"
    coaching: |
      {{INSTRUCTION_FOR_LLM — elicitation guidance for this section}}

quality_gate: |
  {{CRITERIA_FOR_WHEN_THE_TEMPLATE_IS_COMPLETE — e.g., "all required fields
   populated, no placeholder text remaining, user has confirmed priorities"}}
```

#### Worked Example: PRD Template with Coaching

```yaml
# Product Requirements Document
# Defines PRD structure + tells the agent how to elicit each section.

sections:
  - name: "Problem Statement"
    schema:
      required_fields:
        - "user_pain_point"
        - "current_workaround"
        - "impact_if_unsolved"
    coaching: |
      Ask: "What specific problem does the user face today?"
      Push for: A concrete scenario, not an abstract description.
      Move on when: The user has described the pain in terms of
      observable behavior, not feelings.

  - name: "Success Criteria"
    schema:
      required_fields:
        - "metric"
        - "target_value"
        - "measurement_method"
    coaching: |
      Ask: "How will you know this is working?"
      Push for: A number, not a qualitative statement.
      Move on when: At least one metric has a target value
      and a measurement method.

quality_gate: |
  All required fields populated. Problem statement describes
  observable behavior. At least one success metric has a numeric target.
```

---

## Pitfalls

### 1. Removing reasoning scaffolding without adding constraints
Stripping "think step by step" and few-shot examples is correct for reasoning models, but if you also remove the implicit structure those techniques provided, the model has less guidance than before. Compensate: specify the goal precisely, add explicit constraints, and define the output format. The replacement pattern is Goal + Constraints + Context, not just Goal.

### 2. Over-constraining with negatives
Negative constraints are powerful, but too many create contradictions. If the model cannot satisfy all constraints simultaneously, behavior becomes unpredictable as it attempts partial compliance. Keep hard negative constraints to the highest-priority rules (5-8 maximum) and use positive guidance for preferences.

### 3. Defaulting to the most expensive model
Opus 4.6 costs 3.5x Sonnet with no accuracy premium on most benchmarks. The Advisor-Executor pattern achieves higher quality at lower cost than Opus alone. Route bulk work to Sonnet or cheaper models. "Use Opus for everything" is a cost mistake, not a quality strategy.

### 4. Provider-based model selection
"We're a Claude shop" is not a routing strategy. Different models excel at different tasks. The March 2026 release compression (5 launches in 23 days) means the competitive landscape shifts monthly. Route by task characteristics, re-evaluate at each major release.

### 5. Treating CoT as a universal amplifier
Chain-of-thought amplifies reasoning within the model's training distribution but adds nothing for tasks requiring genuinely novel abstraction (ARC-AGI-3: all models 0%). For novel-abstraction tasks, route to human judgment rather than throwing more thinking tokens at the problem.

### 6. Applying brevity constraints to planning tasks
Brevity improves accuracy on many problem types, but complex multi-step planning genuinely benefits from elaboration. Use dynamic brevity: verbose for planning and analysis, terse for execution and output. Do not apply a blanket conciseness constraint to every prompt.

### 7. Elicitation technique overload
Eighteen advanced elicitation techniques exist, but applying multiple techniques to every prompt wastes tokens and produces analysis paralysis. Select 1-2 techniques based on task type. Critique-and-refine for design work. Red team/blue team for security reviews. Stakeholder roundtable for cross-functional decisions. Not all eighteen, not all the time.

### 8. Unversioned prompt changes
Changing a production prompt without versioning, testing, or rollback capability is the prompt equivalent of pushing untested code to production. Treat prompt changes like policy changes: diff, test against acceptance criteria, deploy with rollback.

---

## Related Guides

- **G1 — Writing Agent Specifications:** The three durability properties (Step 1) depend on clear intent specification. G1 Step 1 covers how to define agent goals and constraints that feed into model-resilient prompts.
- **G2 — Managing Agent Context:** The Design/Evaluate framework (Step 4) is the prompt-level application of context curation. G2 covers the broader context engineering discipline that determines what the model sees.
- **G3 — Agent Architecture Decisions:** The Advisor-Executor pattern (Step 6) is one of three orchestration patterns in G3. The model routing table (Step 5) connects to G3's multi-agent architecture guidance.
- **G10 — Agent Design Patterns:** The five-layer prompt architecture in G10 provides the structural framework for applying the durability properties from this guide at each layer. The agent constitution pattern (G10, Step 1) is where model-resilient identity prompts live.

---

## Contract

### Preconditions
- You are writing or auditing prompts for agent systems.
- You understand the distinction between reasoning models and standard models.
- You can test prompts against acceptance criteria after model upgrades.
- You have access to benchmark data or a routing table for model selection.

### Invariants
- Prompts tell the model what to produce, not how to think.
- No prescribed reasoning paths (CoT, few-shot, decomposition, skeleton-of-thought) in prompts for reasoning models.
- High-priority behavioral rules are expressed as negative constraints, not positive aspirations.
- Model selection is task-based, not provider-based.
- The Advisor-Executor pattern is considered before defaulting to the most expensive model.
- Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, and FAILURE SIGNAL properties.
- Prompt changes are versioned and tested before deployment.

### Governance
- Prompts are versioned and tested against acceptance criteria after model upgrades.
- Model routing tables are reviewed when any constituent model has a major release.
- Anti-pattern audits are conducted after major model releases.
- Prompt policy properties (ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL) are checked during skill review.
- Elicitation technique selection is justified per task type, not applied by default.
- This guide is owned by Meta-System knowledge layer.

### Recovery
- **Prompt breaks after model upgrade:** Audit against the three durability properties. Remove prescribed reasoning patterns first (most common cause). If the prompt passes all three properties, escalate to context engineering or constraint specificity.
- **Model costs too high:** Apply the Advisor-Executor pattern for API applications. Reroute bulk work to Gemini Flash or equivalent cost-floor models. Check for Opus-as-default anti-pattern.
- **Prompt performance varies across models:** Check for violated durability properties (especially property 1 -- prescribed reasoning). If properties pass, the issue is likely in context quality or constraint underspecification.
- **Brevity constraints degrade output:** Switch to dynamic brevity -- verbose for planning and analysis phases, terse for execution and final output. Do not apply blanket brevity to all prompt types.
- **Elicitation produces diminishing returns:** Reduce to 1-2 techniques per prompt. The problem is technique overload, not technique failure.
- **Routing table is stale:** Update specific model assignments; the task-based routing structure remains valid. Set a review trigger on major model releases, not calendar dates.
