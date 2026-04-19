---
notion_id: 32b1e08b-9b34-815b-b8ae-c6e86075e888
name: 'Skills vs. Projects: Complementary Role Separation'
summary: 'Claude Projects provide persistent background context for a body of work (files, instructions, project state); Claude Skills teach reusable procedures (how to do a thing). The official recommendation:
  if you''re copying the same instructions across multiple projects, extract them into a skill. Both can operate simultaneously — a project references a skill via the project''s system instructions.'
implementation_notes: null
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- claude-skills-vs-projects-how-i-use-them.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
related_findings:
- file: global-vs-project-level-skill-and-context.md
  rel: same-problem
---
# Skills vs. Projects: Complementary Role Separation

## What It Is
Claude Projects contain: persistent files (reference documents, previous conversation history), a custom system instruction block (project-specific context). Claude Skills are uploadable markdown files that define a reusable capability (writing style, review process, tool usage pattern). A project's instructions can reference a skill by name: 'make sure to reference the Eamonn Cottrell voice skill when writing articles.' Claude will then auto-retrieve and apply the skill without the user explicitly invoking it in each message. Skills are also auto-invoked when the AI detects contextual signals that the skill is relevant.

## Why It Matters
Without this distinction, practitioners duplicate procedural instructions across many projects, creating maintenance debt. A voice style guide copied to 10 projects means 10 places to update when the style evolves. A skill is updated once and propagates everywhere. The skill abstraction also enables composability: a single project can leverage multiple skills (voice, review process, formatting standards) without bloating the project system instructions.

## Why People Are Using It
Directly mirrors software engineering's DRY (Don't Repeat Yourself) principle applied to agent instruction sets. Skills become reusable modules; projects become applications that import them. This enables a skills library that grows and is shared across projects.

## Potential Alternatives
Monolithic system prompts (everything in one place, no separation), project templates with pre-copied instructions (duplicated but versioned), custom API integrations with instruction injection.

## Potential Improvements
Skill versioning: projects should be able to pin to a specific skill version to prevent unexpected behavior changes. Skill composition: a skill that references other skills, enabling a library of modular capabilities that combine.

## Potential Failure Modes
Skill auto-invocation when not intended (Claude infers the skill is relevant when it isn't). Skill conflicts: two skills with overlapping instructions produce inconsistent behavior. Skill drift: the skill document becomes outdated as the task evolves.
