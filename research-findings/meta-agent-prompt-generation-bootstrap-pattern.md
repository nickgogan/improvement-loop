---
name: "Meta-Agent Prompt-Generation Bootstrap Pattern"
summary: "A composition pattern where an agent platform generates a prompt for a different agent tool to execute. In the observed case: Anthropic's managed agent dashboard has an 'Ask Claude' button that generates a complete prompt for Claude Code to scaffold a frontend. The first agent (dashboard) produces a specification that the second agent (Claude Code) consumes -- a two-agent handoff where the artifact is a prompt."
implementation_notes: null
category: "Orchestration"
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
  - file: "orchestrator-headless-dispatch-context-isolation.md"
    rel: same-problem
  - file: "metaprompting-karpathy-autoresearch-for-build.md"
    rel: extends
  - file: "anthropic-managed-agents-platform.md"
    rel: extends
  - file: "nl-description-to-agent-spec-creation-loop.md"
    rel: extends
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

## What It Is

A composition pattern where one agent system generates a prompt designed for consumption by a different agent system. Observed in Anthropic's managed agents platform:

1. User builds and tests an agent on the managed platform
2. User clicks "Ask Claude" button within a session view
3. User says: "I want to spin up a frontend and connect it to this agent"
4. The dashboard agent generates a complete, copy-pasteable prompt for Claude Code
5. User copies the prompt, pastes it into Claude Code
6. Claude Code scaffolds the entire frontend in ~30 seconds

The handoff artifact is a prompt -- not code, not a config file, not an API spec. The dashboard agent has enough context about the managed agent (API endpoint, expected inputs, authentication) to generate a prompt that another AI tool can execute without additional context.

The practitioner's request: "Just give me a prompt I can feed into Claude Code to set this up in 30 seconds. Assume I have Netlify and everything else ready."

## Why It Matters

This is a meta-automation pattern: AI generates instructions for AI. The implications for harness builders:

1. **Prompt as handoff artifact** -- prompts are becoming first-class inter-agent communication artifacts, not just human-to-AI interfaces
2. **Context compression** -- the dashboard agent compresses all relevant context (agent config, API details, auth setup) into a prompt that another agent can execute from cold start
3. **Two-agent pipeline without shared state** -- the dashboard agent and Claude Code share no memory, no session, no context window. The prompt is the only connection point.
4. **Self-bootstrapping ecosystems** -- agent platforms can generate the glue code for their own integration by producing prompts for general-purpose coding agents

This pattern extends the concept of "spec as generator" -- instead of a static spec file, the generator is itself an agent that produces context-aware prompts dynamically.

## Why People Are Using It

Anthropic's managed agents platform ships this as the "Ask Claude" button. The practitioner uses it to go from tested agent to deployed app in under a minute. The speed comes from eliminating the human translation step: instead of reading the agent's config and writing integration code, the user asks one agent to generate instructions for another.

## Potential Improvements

- Direct agent-to-agent dispatch (skip the copy-paste step -- dashboard agent directly invokes Claude Code)
- Prompt quality evaluation before handoff (does the generated prompt contain all necessary context?)
- Template library of handoff prompts for common integration patterns
- Version-aware prompts that adapt to the target agent's capabilities (e.g., generate different prompts for Claude Code vs. Cursor)

## Potential Failure Modes

- Generated prompts that assume context the target agent doesn't have (e.g., referencing specific API endpoints without including them)
- Prompt quality degrades as agent complexity increases (simple agents produce clear prompts; complex agents produce ambiguous ones)
- Copy-paste as handoff mechanism is fragile (user may modify the prompt, breaking assumptions)
- The target agent may interpret the prompt differently than intended, producing incorrect integration code
- No feedback loop: if Claude Code fails to execute the prompt correctly, the dashboard agent has no way to know or correct
