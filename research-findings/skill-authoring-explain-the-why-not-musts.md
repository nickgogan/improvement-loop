---
name: Skill Authoring — Explain the Why, Don't Bludgeon With MUSTs
summary: |-
  Anthropic's skill-creator guidance treats ALL-CAPS MUST/NEVER and rigid structural constraints as yellow flags in skill authoring. Recommended pattern: explain WHY behind every instruction. Modern Claude has good theory of mind; when given the reasoning, the model can extend behavior to unanticipated edge cases. Prescriptive rules without reasoning produce brittle compliance and worse generalization. Yellow flag: 'If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag — if possible, reframe and explain the reasoning so that the model understands why the thing you're asking for is important.'
implementation_notes: "Verbatim from skill-creator: 'Try hard to explain the **why** behind everything you're asking the model to do. Today's LLMs are *smart*. They have good theory of mind and when given a good harness can go beyond rote instructions and really make things happen.' Counter-pattern from skill-creator: 'Even if the feedback from the user is terse or frustrated, try to actually understand the task and why the user is writing what they wrote, and what they actually wrote, and then transmit this understanding into the instructions.' The advice is about prompt craft inside skills specifically, but generalizes to all instruction-shaped LLM context."
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-skills-repo.md"
related_findings:
  - file: "skill-authoring-four-guidelines.md"
    rel: "same-problem"
  - file: "iterate-on-single-task-then-extract-skill.md"
    rel: "same-problem"
  - file: "agent-context-kiss-commandments-minimum-viable.md"
    rel: "same-problem"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skill Authoring — Explain the Why, Don't Bludgeon With MUSTs

## What It Is

A skill-authoring principle from Anthropic's skill-creator skill: treat ALL-CAPS MUST/ALWAYS/NEVER and rigid structural constraints as yellow flags, not best practices. The recommended replacement is to explain the WHY behind every instruction.

Direct quote: "Try hard to explain the **why** behind everything you're asking the model to do. Today's LLMs are *smart*. They have good theory of mind and when given a good harness can go beyond rote instructions and really make things happen. Even if the feedback from the user is terse or frustrated, try to actually understand the task and why the user is writing what they wrote, and what they actually wrote, and then transmit this understanding into the instructions. If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag — if possible, reframe and explain the reasoning so that the model understands why the thing you're asking for is important."

The principle generalizes beyond skills to any instruction-shaped LLM context (system prompts, agent definitions, CLAUDE.md fragments, slash commands).

## Why It Matters

The practical reasoning: prescriptive rules without underlying reasoning produce brittle compliance. The model follows the rule mechanically when the rule fits, fails to extend it when the rule's spirit applies in an unanticipated edge case, and treats the rule as the entirety of the relevant context (missing related considerations).

When the model has the reasoning, it can:
- **Extend** the rule to similar-but-not-identical situations.
- **Recognize exceptions** where the underlying concern doesn't apply.
- **Coordinate** the rule with other rules whose reasoning interacts.
- **Communicate** about the rule with the user (explain why it's behaving a certain way).

Modern Claude has good theory of mind. Treating it like a 1990s rule-based system understates the model's actual capability and produces worse outcomes than treating it as a reasoning agent.

This is a content-level skill authoring principle that pairs with the higher-level "iterate with Claude" guideline: the iteration loop reveals which constraints actually matter; the authoring style expresses them as reasoned principles rather than blunt prohibitions.

## Why People Are Using It

Embedded in Anthropic's official skill-creator skill, which is the canonical authoring guide for new skill authors. Reinforced by Anthropic's broader publicly stated philosophy across their Engineering blog (effective context engineering, building effective agents, writing effective tools for agents) — all of which emphasize reasoned context over rigid rules.

## Potential Alternatives

ALL-CAPS rules-based authoring (works for narrow compliance but generalizes poorly). Strict schema/format enforcement only (loses flexibility; brittle to edge cases). Few-shot examples without explanations (less brittle than rules but still doesn't communicate the reasoning Claude can extend from). Long lists of negative constraints (don't do X, don't do Y — leaves the positive space underspecified).

## Potential Improvements

A formal "yellow flag pattern" lint for skills — automated detection of ALL-CAPS imperatives or rigid templates. Conventional shapes for explaining why ("Why: [reasoning]" as a recurring section). Per-skill examples of well-explained vs. poorly-explained instructions. The principle pairs naturally with positive-space governance (the MetaSystem feedback rule about preferring positive invariants over rejection lists).

## Potential Failure Modes

**Why-explanation as bloat.** Explaining reasoning adds tokens. A skill that explains the why of every micro-decision overflows the 5K Level 2 budget and becomes harder to read. Discipline: explain the why of consequential decisions, accept that some details are self-evident.

**Wrong why.** Explaining reasoning the author got wrong propagates the error. The model now has a clear (incorrect) framework to extend from.

**Reasoning conflicts.** Multiple skills explaining mutually inconsistent whys leave the model arbitrating between them. Cross-skill consistency requires authoring discipline.

**Necessary hard constraints.** Some constraints are not negotiable — security boundaries, format requirements, regulatory rules. Reasoning explanations should accompany them, not replace them. "ALWAYS validate input — because the downstream consumer assumes well-formed data" is better than either "ALWAYS validate input" alone or "the downstream consumer assumes well-formed data so consider validating input."

**Author skill gap.** Some authors don't know the why. They captured a working pattern empirically. Reaching for "explain the why" when you don't know the why produces handwaving. The honest move is to say "we found this works; not sure exactly why" — which is also useful context.
