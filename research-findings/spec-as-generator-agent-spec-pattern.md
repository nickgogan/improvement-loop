---
name: Spec-as-Generator (AGENT_SPEC) Pattern
summary: A machine-readable specification file that lets an AI agent generate all required contribution files from a single prompt. OB1's AGENT_SPEC.md defines the exact output files (5), their schemas,
  naming conventions, validation checklist, and an example prompt — enabling one-shot scaffold generation for new extensions.
implementation_notes: MetaSystem's /bootstrap skill generates fractal structure but doesn't use a machine-readable spec file. The AGENT_SPEC pattern could improve bootstrap quality by providing a strict
  contract that AI agents follow for file generation.
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: meta-skill-for-skill-authorship.md
  rel: same-problem
- file: spec-as-source-of-truth-for-agent-construction.md
  rel: extends
- file: yaml-template-dual-structure.md
  rel: same-problem
- file: agent-onboarding-via-interview-style-context.md
  rel: same-problem
- file: declarative-agent-spec-with-serialization-registry.md
  rel: same-problem
date_discovered: '2026-04-20'
last_updated: '2026-07-13'
pipeline_status: raw
consumed_by: []
---

## What It Is
A contribution template that includes a machine-readable spec file (`AGENT_SPEC.md`) alongside the human-readable template files. The spec defines: exact output files required (README.md, metadata.json, schema.sql, index.ts, deno.json), their complete schemas with field-by-field documentation, naming conventions (directory, function name, MCP server name, table names, tool names), a validation checklist, and an example prompt that demonstrates expected usage.

The key insight: the spec is written FOR AI agents, not for human developers. It's designed so that an AI agent given the spec + a description can produce all 5 files in a single pass with correct structure, naming, and schema compliance.

## Why It Matters
Template directories typically contain example files that humans copy-paste and modify. The AGENT_SPEC pattern adds a layer designed for AI consumption — a contract that tells the agent exactly what to produce, how to structure it, and how to validate it. This reduces the back-and-forth when using AI to scaffold new contributions, and ensures consistency across community submissions.

## Why People Are Using It
Observed in [OB1 (Open Brain)](https://github.com/NateBJones-Projects/OB1) — see [[ob1-analysis]] for structural details. The `extensions/_template/AGENT_SPEC.md` is 298 lines and covers every file, field, and convention. The spec includes a "Tool Design Rules" section and "Validation Checklist" — both designed for AI agent consumption rather than human reading.

## Potential Alternatives
- **Template files only** (traditional approach): Human copies and modifies. Works but inconsistent across contributors.
- **Meta-skill for skill authorship** (Superpowers): A skill that teaches agents to write skills. Similar goal but uses persuasion principles rather than strict specs.
- **JSON Schema validation only** (OB1's CI): Catches structural errors post-hoc. The AGENT_SPEC prevents them at generation time.

## Potential Improvements
- Multiple spec files per category (OB1 only has one for extensions — recipes, skills could benefit from their own AGENT_SPEC)
- Version-controlled spec evolution — when the spec changes, existing contributions may drift
- Spec validation: a tool that checks generated files against the spec before PR submission

## Potential Failure Modes
- Spec maintenance burden — must stay in sync with CI rules, metadata schema, and README standards
- AI agents may not follow the spec perfectly, creating a false sense of quality
- The spec is only as good as its examples — edge cases not covered by examples will produce inconsistent output
