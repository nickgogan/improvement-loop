---
name: Self-Describing Codebases via Structural and Semantic Context Layers
summary: 'Making a codebase inherently self-describing requires two distinct context layers: structural context (module manifests answering ''where'' — what a module does, what it depends on, what depends
  on it) and semantic context (behavioral contracts on interfaces answering ''what'' — performance expectations, failure modes, retry semantics, not just data shape). Together, these make comprehension
  embedded in the code rather than locked in individual heads.'
implementation_notes: 'Add module manifests to each app/ directory in MetaSystem — short markdown files covering purpose, dependencies in/out, and key constraints. Add behavioral contract annotations to
  all skill interfaces: expected output format, failure modes, retry behavior, and performance expectations. These are the structural and semantic layers of a self-describing codebase.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- dark-code-spec-driven-comprehension-gates.md
related_findings:
- file: context-file-taxonomy-claudemd-soulmd-agentsmd.md
  rel: same-problem
- file: context-curation-over-context-stuffing.md
  rel: same-problem
- file: dark-code-organizational-capability-problem.md
  rel: enabled-by
- file: ai-readable-naming-conventions-as-a-navigation.md
  rel: same-problem
- file: claudemd-as-signal-to-noise-problem-not-size-probl.md
  rel: same-problem
- file: claudemd-as-knowledge-base-traversal-guide.md
  rel: same-problem
- file: ai-as-primary-reader-design-principle.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
---
# Self-Describing Codebases via Structural and Semantic Context Layers

## What It Is

Context engineering applied at the codebase level — not just prompt or session context, but the codebase itself restructured so comprehension is embedded rather than residing in individual developers' heads or external documentation.

Two distinct layers:

**Structural context (answers "where"):** Every module should have a manifest that describes:
- What the module does
- What it depends on (dependencies in)
- What depends on it (dependencies out)

This makes navigation and impact analysis legible without requiring a human expert to explain the dependency graph.

**Semantic context (answers "what"):** Every interface — not just API endpoints, but all interfaces within the system — should carry behavioral contracts that specify:
- Performance expectations
- Failure modes
- Retry semantics
- Behavioral contracts (how the interface is expected to behave, not just the data shape)

The distinction from API contracts is scope: semantic context applies to all interfaces, not just external APIs. The intent is to give any AI (or human) reading the interface the rules of engagement, not just the type schema.

## Why It Matters

The organizational risk of AI-generated code is that comprehension does not transfer: the person who prompted the generation never fully understood it, and the next person to read it has no embedded documentation to bootstrap understanding. Structural and semantic context layers mean that the codebase self-explains — the navigation structure, dependency graph, and interface behavior are all immediately legible without requiring tribal knowledge.

This is particularly high-leverage for agentic development: when an AI agent reads a module manifest, it has explicit dependency context that would otherwise require inference from code structure. When an agent reads a behavioral contract on an interface, it has explicit failure mode and retry guidance that would otherwise require reverse-engineering.

## Why People Are Using It

Framed as part of the response to "dark code" — AI-generated code that nobody can explain. The structural + semantic context layer approach is positioned as the means by which codebase comprehension becomes durable and transferable rather than residing in individual heads or external wikis.

## Potential Improvements

- Standardized manifest schema that agents can parse consistently (YAML frontmatter per module directory)
- Behavioral contract format that extends OpenAPI-style specs to cover all interface types, not just HTTP
- Automated manifest generation from code analysis as a first-pass, with human refinement

## Potential Failure Modes

- Manifests and behavioral contracts drift from actual implementation — they become misleading rather than clarifying
- High upfront cost to retrofit existing codebases
- Teams write structural manifests but skip semantic behavioral contracts (the harder, more valuable layer)
- Semantic context becomes bloated with edge cases and loses signal-to-noise ratio
