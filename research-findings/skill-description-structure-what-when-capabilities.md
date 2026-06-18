---
name: Skill Description Structure — [What it does] + [When to use it] + [Key capabilities]
summary: Anthropic's Complete Guide PDF prescribes a three-part structure for the skill description field: [What it does] + [When to use it] + [Key capabilities]. Good descriptions are specific and actionable, include trigger phrases users would naturally say, mention file types if relevant, and have a clear value proposition. Bad descriptions are vague, miss trigger phrases, or are too technical. Reserved words 'claude' and 'anthropic' are forbidden in names. Description max 1024 chars; no XML angle brackets.
implementation_notes: "Worked examples from the PDF: GOOD — 'Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for design specs, component documentation, or design-to-code handoff.' BAD — 'Helps with projects.' / 'Creates sophisticated multi-page documentation systems.' / 'Implements the Project entity model with hierarchical relationships.' The PDF lists three failure modes: too vague, missing triggers, too technical with no user triggers. Pair with skill-creator's 'be a little bit pushy' guidance: to combat Claude's undertriggering tendency, descriptions should include not just trigger conditions but a slight push toward use ('Make sure to use this skill whenever the user mentions X, Y, Z, even if they don't explicitly ask')."
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-complete-guide-building-skills-pdf.md"
related_findings:
  - file: "skill-md-frontmatter-as-discovery-trigger-primitive.md"
    rel: "extends"
  - file: "skill-description-optimization-loop-held-out-test.md"
    rel: "same-problem"
  - file: "skill-frontmatter-validation-rules.md"
    rel: "extends"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skill Description Structure — [What it does] + [When to use it] + [Key capabilities]

## What It Is

A three-part structure prescribed by Anthropic's Complete Guide PDF for the skill `description` field:

`[What it does] + [When to use it] + [Key capabilities]`

Worked examples from the guide:

**Good — specific and actionable:**
> Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for "design specs", "component documentation", or "design-to-code handoff".

**Good — includes trigger phrases:**
> Manages Linear project workflows including sprint planning, task creation, and status tracking. Use when user mentions "sprint", "Linear tasks", "project planning", or asks to "create tickets".

**Good — clear value proposition:**
> End-to-end customer onboarding workflow for PayFlow. Handles account creation, payment setup, and subscription management. Use when user says "onboard new customer", "set up subscription", or "create PayFlow account".

**Bad — three named failure modes:**
- *Too vague:* "Helps with projects."
- *Missing triggers:* "Creates sophisticated multi-page documentation systems."
- *Too technical, no user triggers:* "Implements the Project entity model with hierarchical relationships."

Validation constraints (also from the PDF): name kebab-case only, must match folder name, cannot contain reserved words `claude` or `anthropic`, no XML angle brackets in frontmatter. Description max 1024 chars, no XML, MUST include both what and when.

## Why It Matters

The description structure is the most actionable authoring guidance for the most consequential field. Three observations:

1. **"What" alone misses trigger context.** Claude knows the skill does X but doesn't know when X is wanted.
2. **"When" alone is unanchored.** Trigger phrases without a value statement leave Claude guessing what executing the skill commits to.
3. **"Key capabilities" prevents undertriggering.** Specific capabilities give Claude more keywords to match against varied user phrasing.

The structure pairs with skill-creator's "pushy descriptions" advice: include explicit "Make sure to use this skill whenever..." language to combat Claude's documented undertriggering bias. The PDF doesn't go as far as recommending pushy framing, but the optimization loop in skill-creator does.

The named failure modes are concrete and recognizable. "Helps with projects" is the recurring shape of bad descriptions — vague, no triggers, no specificity. The lint surface for description quality is small enough to enumerate.

## Why People Are Using It

Codified in Anthropic's Complete Guide PDF as the recommended structure. The worked examples are the most concrete description authoring guidance in the official material. skill-creator's optimization loop assumes descriptions follow this structure as a starting point.

## Potential Alternatives

Free-form description (anything goes — most common in the wild). One-sentence summary only (loses trigger context). Trigger-list-only ("Use when: X, Y, Z" — loses value statement). Two-part: [What] + [When] without explicit capabilities ([What] + [When] is sufficient minimal but capabilities help triggering).

## Potential Improvements

A description lint that scores against the three-part structure. Templates for common skill categories. A spec-level recommendation in the open standard (currently spec says "what it does and when to use it" without the three-part structure). Telemetry-derived heuristics: capture which descriptions actually trigger reliably and reverse-engineer the patterns.

## Potential Failure Modes

**Trigger phrases over-broad.** "Use when user mentions data, charts, files, work, or tasks" matches too much. Skill triggers on everything; user disables it.

**Trigger phrases too narrow.** "Use when user says 'create a sprint with story points and Fibonacci-scale estimates'." Skill never triggers because users never phrase it that way.

**Key capabilities as marketing.** Authors write the value proposition for humans (other authors reading the README), not for Claude. The capabilities listing is the wrong audience.

**Reserved-word naming.** "claude-fixup" and "anthropic-helper" silently fail to load. The Complete Guide names this; authors hit it anyway.

**Description bloat.** Three-part structure plus pushy language plus trigger phrases easily exceeds the 1,024-char limit. Hard wall — the description gets truncated at install or fails validation.

**Description-body mismatch.** Description promises capabilities the body doesn't deliver. The skill triggers, then fails to perform.
