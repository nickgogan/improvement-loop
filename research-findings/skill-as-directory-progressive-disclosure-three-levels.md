---
name: Skill-as-Directory with Three-Level Progressive Disclosure
summary: Agent Skills are filesystem directories containing a required SKILL.md plus optional scripts/, references/, assets/ subdirectories. Content loads progressively in three levels — metadata always
  in system prompt (~100 tokens), full SKILL.md on activation (<5K tokens recommended), bundled files on demand (effectively unbounded). The filesystem model is what makes progressive disclosure mechanically
  possible — Claude reads files via bash only when needed.
implementation_notes: 'Canonical Anthropic primitive as of Oct 2025; open standard at agentskills.io since Dec 2025. The three-level model is the most-cited skill design principle. Token cost per level
  is explicit: ~100 / <5K / unbounded. The ''unbounded'' tier is enabled by Claude reading bundled files via bash — file contents enter context only when read, and scripts can execute without their code
  ever entering context. This is the architectural primitive every other skill pattern composes on top of.'
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in:
- Improvement Loop
- General / Cross-System
sources:
- anthropic-equipping-agents-with-agent-skills.md
- anthropic-agent-skills-overview-docs.md
- anthropic-skills-repo.md
- agentskills-open-standard.md
- anthropic-complete-guide-building-skills-pdf.md
- pydantic-ai-2-0-composing-capabilities.md
related_findings:
- file: mcp-as-code-api-progressive-tool-discovery.md
  rel: same-problem
- file: skill-md-frontmatter-as-discovery-trigger-primitive.md
  rel: enables
- file: code-as-deterministic-tool-inside-skills.md
  rel: enables
- file: skill-content-lifecycle-context-budget.md
  rel: extended-by
- file: branch-analysis-externalization-rule-skill-reference.md
  rel: extended-by
- file: memory-file-to-skill-migration.md
  rel: enables
- file: capability-as-agent-composition-primitive.md
  rel: extended-by
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-07-13'
pipeline_status: raw
consumed_by: []
---

# Skill-as-Directory with Three-Level Progressive Disclosure

## What It Is

A skill is a filesystem directory with a required `SKILL.md` file plus optional `scripts/`, `references/`, and `assets/` subdirectories. Content loads in three levels:

- **Level 1 — Metadata**: The `name` and `description` from YAML frontmatter (~100 tokens per skill, always in Claude's system prompt at startup).
- **Level 2 — Instructions**: The full SKILL.md body (<5K tokens recommended, loaded when Claude decides the skill applies or when the user invokes it explicitly).
- **Level 3+ — Resources**: Any bundled files (effectively unbounded — files only enter context when Claude reads them, and bundled scripts can execute without their code being loaded at all).

Claude invokes Level 2 by reading SKILL.md via bash; the filesystem is the load mechanism. Level 3 files are referenced by name from SKILL.md and read only on demand.

## Why It Matters

This is the architectural primitive every other Anthropic skill pattern composes on top of. It solves a foundational context-engineering problem: how to attach many capabilities to an agent without paying for all of them on every prompt. Static system-prompt scaling caps out at the context window; progressive disclosure pushes the cap to the filesystem.

The model decouples *capability presence* (cheap, Level 1) from *capability detail* (paid only when invoked, Level 2) from *capability execution* (decoupled entirely from context for scripts, Level 3). An agent can carry dozens of skills with the system-prompt cost of a short paragraph each.

## Why People Are Using It

The pattern has now migrated up the stack into framework primitives: Pydantic AI 2.0
capabilities implement the same catalog/full-load split at capability granularity —
brief descriptions always visible, full instructions loaded only when the agent decides
it needs that capability (`pydantic-ai-2-0-composing-capabilities.md`, 2026-07). Cross-
platform corroboration that the three-level economics generalize beyond SKILL.md files.

Documented as the core design principle in Anthropic's engineering post (Oct 2025) and reiterated across all canonical sources — the platform.claude.com overview, the Claude Code docs, the anthropics/skills repo, the open standard at agentskills.io, and the Complete Guide PDF. Adopted across Claude.ai, Claude Code, the Claude Agent SDK, and the Claude Developer Platform. Open standard published December 2025 with adopters listed at agentskills.io/clients. Used at scale internally for Claude's document-editing capabilities (docx, pdf, pptx, xlsx skills).

## Potential Alternatives

System-prompt-only context (cap at context window; doesn't scale past ~10 capabilities). Tool-call-only patterns (MCP) — capabilities are advertised but workflow knowledge is not packaged. Static markdown rules in CLAUDE.md or `.cursorrules` — always loaded, no progressive disclosure, harder to scope. Sub-agents-as-capabilities — heavier, full-context-fork per invocation. The Claude Code docs explicitly recommend skills for content that "loads only when it's used, so long reference material costs almost nothing until you need it" — explicitly contrasting against CLAUDE.md's always-loaded model.

## Potential Improvements

Level-4 (or deeper) progressive disclosure inside references/ — references that themselves reference further files. The spec already allows arbitrary depth but agentskills.io specifically guides "keep file references one level deep from SKILL.md; avoid deeply nested reference chains" — open question whether deeper structures pay off. Dynamic context windows by skill (skills carrying their own context budgets). Skill-to-skill composition primitives (one skill calling another as a named operation, rather than spawning a forked subagent).

## Potential Failure Modes

**Skill bloat past Level 2 budget.** If SKILL.md grows past ~500 lines / 5K tokens, Level 2 starts paying full context cost on every invocation and the model spends tokens on guidance it doesn't need. Anthropic's authoring guide explicitly says "Keep `SKILL.md` under 500 lines."

**Reference chain depth.** Deeply nested reference graphs (SKILL.md → refs/foo.md → refs/foo/bar.md → ...) shift the cost discovery from "read one file" to "navigate a tree" and the model may load the wrong subset or thrash.

**Description ambiguity at Level 1.** Because Level 1 is the only thing Claude sees before deciding to load Level 2, vague descriptions cause skills to under- or over-trigger. Skill descriptions are the bottleneck between "capability exists" and "capability gets used."

**Context budget pressure.** When many skills are installed, the Level 1 descriptions compete for a fixed budget (in Claude Code: 1% of context window default). Below the cap, descriptions get truncated and the keywords Claude needs to match a request can be stripped.
