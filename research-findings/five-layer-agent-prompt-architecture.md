---
name: Five-Layer Agent Prompt Architecture -- Role to Tool-Calling Stack
summary: 'A production agent prompt architecture with five explicit layers: (1) Role & Scope -- what the agent is and where its job begins/ends; (2) Instructions & Constraints -- priorities and security
  boundaries; (3) Context & Retrieved Data -- trust classification of inputs; (4) Examples & Edge Cases -- diverse coverage including adversarial cases; (5) Output Format & Tool-Calling -- action discipline
  for reliability. Prompt engineering is becoming reliability engineering.'
implementation_notes: Maps well to MetaSystem's existing CLAUDE.md structure. The key addition is explicit trust classification of retrieved data (Layer 3) and the framing of output format as reliability
  engineering rather than readability (Layer 5). Use as a checklist when designing new agent prompts.
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- ai-agent-prompt-engineering-best-practices-inflect.md
- prompting-best-practices-nick-gogan.md
related_findings:
- file: soul-md-agent-constitution-pattern.md
  rel: same-problem
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
- file: the-four-discipline-prompting-stack-nate-b-jones.md
  rel: same-problem
- file: prompt-as-policy-version-control-and-cicd-for-agen.md
  rel: same-problem
- file: spec-first-agent-briefs-prompt-craft-context-inten.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- agent-design-patterns.md
---
## What It Is

A five-layer architecture for production agent prompts, where each layer addresses a distinct concern:

**Layer 1 -- Role & Scope:** What the agent is, what its job is, and where that job begins and ends. Establishes operational responsibility and how it interprets instructions. Scope defines what the agent should AND should not do.

**Layer 2 -- Instructions & Constraints:** Clear, direct priorities in plain language. Security-focused constraints preventing prompt injection, privilege escalation. Establishes: system instructions override conflicting user instructions; ask for clarification when inputs are missing.

**Layer 3 -- Context & Retrieved Data:** Trust classification of all inputs. Explicitly covers: what counts as trusted instruction vs. untrusted context; how to use retrieved data in decision-making; what to do when retrieved data is incomplete or contradictory. Without this, models may over-trust low-quality information.

**Layer 4 -- Examples & Edge Cases:** Diverse, structured examples covering common cases AND edge cases. Must teach decision patterns: when to call a tool (or not), when to ask for clarification, how to handle missing parameters, when to refuse requests. Polished-only examples fail in production.

**Layer 5 -- Output Format & Tool-Calling:** Action discipline for reliability. Output format is tied to whether the agent can hand work to another component, call tools correctly, and return usable results without ambiguity.

The framing: "Agent prompt engineering is a systems problem. Prompt quality depends on how well retrieval, tools, and memory are scoped and orchestrated, not just how polished the prompt verbiage is."

## Why It Matters

Most agent prompts address Layers 1-2 (role and instructions) but neglect Layers 3-5 (trust classification, adversarial coverage, action discipline). The result is agents that work in demos but fail in production. The five-layer architecture provides a complete checklist for production-grade agent prompts.

## Why People Are Using It

Inflectra documents this alongside OWASP AI safety recommendations. The pattern is consistent with but more granular than the four-discipline prompting stack -- it operates at the implementation level within the Prompt Craft discipline.

## Potential Improvements

- Map each layer to specific sections in MetaSystem CLAUDE.md files
- Create a pre-deployment checklist based on the five layers
- Add adversarial test cases to Layer 4 for all production skills

## Potential Failure Modes

- **Layer 3 neglect:** The most commonly skipped layer. Without trust classification, agents treat all retrieved content as equally authoritative
- **Example poverty:** Layer 4 with only happy-path examples creates agents that fail on the first edge case
- **Over-specification:** Excessively detailed Layer 5 constraints can prevent the agent from adapting to legitimate novel situations
