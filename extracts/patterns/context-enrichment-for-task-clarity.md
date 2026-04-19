---
title: "Context Enrichment for Task Clarity"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "context-enrichment-for-task-clarity"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The task must have a defined purpose beyond its literal output. The invoker must know (or be able to infer) the audience, workflow position, and success criteria before dispatching the task."
  invariants: "Every agent invocation or skill dispatch includes all four context fields: purpose, audience, workflow position, and success criteria. Success criteria are measurable, not subjective."
  governance: "Owned by Meta-System knowledge layer. Skill templates and agent dispatch protocols enforce the four-field requirement. Waivers for trivial tasks (e.g., file reads) are permitted but must be explicit."
  recovery: "If output quality degrades and root cause is traced to missing context enrichment, add the missing fields and re-run. If context enrichment is incorrect (wrong audience, wrong success criteria), the output will be confidently wrong -- re-run with corrected context rather than patching the output."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Context Enrichment for Task Clarity

**Source:** [[context-enrichment-for-task-clarity]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

When agents or skills receive a task without context about why the task matters, they optimize for generic output. A prompt that says "summarize this document" produces a different (and worse) result than one that says "summarize this document for a technical reviewer who needs to decide whether to approve the architecture, focusing on risk and constraint coverage." Without explicit purpose, audience, workflow position, and success criteria, the model cannot make informed tradeoffs between competing output qualities (brevity vs. completeness, technical depth vs. accessibility, speed vs. thoroughness).

## Forces

- **Effort vs. payoff.** Adding context to every task invocation takes time. For simple tasks, the overhead may exceed the quality improvement. For complex tasks, missing context almost always degrades output.
- **Knowledge availability.** The invoker must know the purpose, audience, and success criteria to provide them. In exploratory work, these may not be well-defined yet.
- **Precision vs. over-specification.** Too little context produces generic output. Too much context constrains the model's ability to surface unexpected insights. Incorrect context (wrong audience, wrong success criteria) produces confidently wrong output, which is worse than generic output.
- **Consistency vs. flexibility.** Standardizing a four-field context template ensures nothing is forgotten but can feel rigid for tasks that do not fit the template cleanly.

## Solution

Every task dispatched to an agent or skill includes four types of contextual information upfront:

1. **Purpose.** What will the results be used for? ("This summary will be used to decide whether to approve the architecture proposal.") This constrains what the model emphasizes and what it can safely omit.

2. **Audience.** Who will consume the output? ("The audience is a senior engineer familiar with distributed systems but unfamiliar with this specific codebase.") This sets the appropriate level of technical depth, assumed knowledge, and tone.

3. **Workflow position.** Where does this task sit in a larger workflow? ("This is step 3 of 5 in the review pipeline. Step 2 produced a risk assessment. Step 4 will use this summary to draft approval criteria.") This helps the model understand what information to preserve for downstream steps and what can be safely condensed.

4. **Success criteria.** What does "done well" look like, expressed as measurable thresholds? ("The summary must cover all 5 risk categories identified in step 2. It must be under 500 words. Every claim must cite a specific section of the source document.") This gives the model a concrete target rather than an implicit quality bar.

In MetaSystem, every skill SKILL.md should include a Task Context section defining how these four fields are populated for that skill's invocations. Subagent dispatch calls should pass purpose, audience, position, and criteria as structured fields.

## Consequences

**Positive:**
- Dramatically improves output quality by constraining the solution space to what is actually needed.
- Reduces revision cycles -- the model is more likely to produce acceptable output on the first pass when it understands the target.
- Makes quality assessable: with explicit success criteria, output can be evaluated against a defined standard rather than subjective impression.
- Composable with other patterns: context enrichment fields can be auto-populated from workflow metadata, reducing manual effort.

**Negative:**
- Adds overhead to every task invocation. For trivial tasks (file reads, simple lookups), the overhead is not justified.
- Incorrect context is worse than absent context. A wrong audience specification produces output tuned for the wrong reader. A wrong success criterion produces output optimized for the wrong goal.
- Maintaining context accuracy across multi-step workflows requires careful propagation. If step 3's context references step 2's output, changes to step 2 can silently invalidate step 3's context.
- Can suppress serendipity: a heavily constrained model is less likely to surface unexpected but valuable observations.

## Known Uses

- **Anthropic prompting best practices.** Context enrichment is documented as a foundational prompting pattern in Anthropic's official guidance.
- **OpenAI prompting best practices.** Similar four-field pattern documented independently, suggesting convergent best practice.
- **MetaSystem's partial adoption.** Some skills and prompts include purpose and audience; adoption is inconsistent. The finding's implementation note flags this as "low effort, high impact" to standardize.

## Contract

### Preconditions

- The task must have a defined purpose beyond its literal output. If the purpose is unknown, exploratory mode applies (no enrichment, but output is flagged as un-enriched).
- The invoker must know or be able to infer the audience, workflow position, and success criteria before dispatching the task.
- Success criteria must be expressible as measurable thresholds, not subjective qualities ("good," "thorough," "complete").

### Invariants

- Every agent invocation or skill dispatch includes all four context fields: purpose, audience, workflow position, and success criteria.
- Success criteria are measurable (counts, lengths, coverage targets, citation requirements), not subjective.
- Context fields are populated from task metadata when available, not invented by the agent.

### Governance

- Owned by Meta-System knowledge layer.
- Skill templates and agent dispatch protocols enforce the four-field requirement.
- Waivers for trivial tasks (e.g., single file reads, simple lookups) are permitted but must be documented in the skill definition.

### Recovery

- If output quality degrades and root cause is traced to missing context enrichment, add the missing fields and re-run the task. Do not patch the output.
- If context enrichment is incorrect (wrong audience, wrong success criteria), the output will be confidently wrong. Discard and re-run with corrected context rather than attempting to fix the output.
- If success criteria cannot be defined for a task (genuinely exploratory work), omit the criteria field but tag the output as "un-enriched, requires human review before downstream use."
