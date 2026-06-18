---
name: "NL-Description-to-Agent-Spec Creation Loop"
summary: "A harness pattern where agents are created from natural language descriptions through a structured loop: describe intent -> platform generates spec -> review/approve spec -> create agent -> test interactively -> observe results -> modify spec from test observations -> redeploy. The spec (system prompt + tool config) is the persistent artifact that survives iteration."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-managed-agents-platform.md"
related_findings:
  - file: "spec-as-generator-agent-spec-pattern.md"
    rel: same-problem
  - file: "anthropic-managed-agents-platform.md"
    rel: extends
  - file: "iterative-refinement-loop-with-quality-gate.md"
    rel: same-problem
  - file: "meta-prompting-separating-analysis-from-execution.md"
    rel: same-problem
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - agent-design-patterns.md
tags:
  - "session-95-reextract"
---

## What It Is

A creation pattern observed in Anthropic's managed agents platform where the harness guides the user through a structured loop to go from intent to deployed agent:

1. **Describe** -- user provides natural language description of what the agent should do (voice or text)
2. **Spec generation** -- platform generates a structured spec: agent name, description, required tools, credential needs, system prompt
3. **Review/approve** -- user reviews the spec and clicks "create this agent"
4. **Provision** -- platform creates the agent alongside its hosted environment and credential vault in a single atomic operation
5. **Test interactively** -- user runs test conversations in a debug-enabled interface
6. **Observe** -- user examines test results, debug logs, and downstream effects (e.g., tasks created in ClickUp)
7. **Modify from observations** -- platform asks "what do you want to change?" and user provides refinements in natural language; platform patches the system prompt
8. **Redeploy** -- updated agent is created and the cycle repeats

The spec (system prompt + tool configuration + environment permissions) is the durable artifact. Everything else -- the environment, the vault, the test sessions -- exists to support iteration on the spec.

## Why It Matters

This pattern inverts the traditional agent development workflow. Instead of writing code, configuring tools, and debugging integrations manually, the developer works at the intent level and the platform handles implementation. The key insight is that the loop is conversational -- modifications happen through natural language dialogue with the platform, not through code edits. This dramatically lowers the barrier to agent creation while keeping the spec as a reviewable, versionable artifact.

For harness builders, this pattern provides a template for how agent creation UX should work: the user should never need to write a system prompt directly; they should describe intent and review generated specs.

## Why People Are Using It

The practitioner (a professional automation builder) demonstrates building a complete sales-call-to-ClickUp-tasks agent in minutes, including OAuth setup, testing, and deployment. The speed comes from the platform handling three traditionally slow tasks: credential management, environment provisioning, and system prompt authoring.

## Potential Improvements

- Version history for specs so users can roll back changes
- Diffing between spec versions to show what changed after each refinement
- Automated test generation from the spec (the platform could propose test cases based on the described intent)
- Collaborative spec editing for team-built agents

## Potential Failure Modes

- NL descriptions may produce vague or overly broad specs that pass review but fail in edge cases
- The "modify from observations" step requires the user to notice what went wrong -- subtle failures (wrong task format, missing fields) may not surface in quick tests
- Spec drift: after many modification cycles, the spec may accumulate conflicting instructions that the user doesn't notice because they only see the latest change
- Over-reliance on the creation loop may prevent users from understanding the underlying system prompt, making debugging harder when the loop's suggestions don't fix the problem
