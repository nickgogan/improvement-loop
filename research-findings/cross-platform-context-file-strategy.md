---
name: Cross-Platform Context File Strategy
summary: 'Three distinct strategies for maintaining AI coding context files that work across multiple tools (Claude Code, GitHub Copilot, Cursor, Codex): platform-specific mirroring (Archon), chain-loader
  indirection (n8n), and content duplication (LangGraph). As multi-tool environments become standard, cross-platform context portability is an emerging architectural concern.'
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- careerbuddy-meta-skill-author-references.md
related_findings:
- file: seven-context-loading-mechanisms-no-convergence.md
  rel: extends
- file: context-file-taxonomy-claudemd-soulmd-agentsmd.md
  rel: extends
- file: three-layer-context-chain-loading.md
  rel: extends
- file: monorepo-context-distribution-three-strategies.md
  rel: same-problem
- file: universal-harness-context-via-symlink.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- defending-agent-context.md
---

## What It Is

Three repos in the watched-libraries registry address the problem of maintaining context files that work across multiple AI coding tools, each with a different strategy:

1. **Platform-specific mirroring (Archon):** Maintains parallel agent definitions in `.claude/agents/`, `.github/agents/`, and `.github/prompts/` — same specialists adapted for Claude Code, GitHub Copilot agents, and Copilot prompts respectively. Full copies with platform-specific adaptations. Maximum fidelity per platform, but content can drift between copies.

2. **Chain-loader indirection (n8n):** Root `CLAUDE.md` is a single line: `@AGENTS.md`. Claude Code auto-loads CLAUDE.md (which is just a pointer) and follows the `@` reference to AGENTS.md. Other tools (Copilot, Cursor) can read AGENTS.md directly. The naming constraint is solved at the pointer level — minimal duplication, works across tools.

3. **Content duplication (LangGraph):** `CLAUDE.md` and `AGENTS.md` at root contain identical content. Simplest approach but content can drift when one file is updated and the other is not.

This problem didn't surface in the original 7-repo comparison because those repos targeted a single AI tool.

## Why It Matters

As development teams adopt multiple AI coding assistants (Claude Code for complex tasks, Copilot for inline completions, Cursor for IDE-integrated work), the question of "how do I maintain one set of project conventions that all tools can read?" becomes a real architectural decision. Each tool has different auto-loading conventions (Claude Code: CLAUDE.md, Copilot: AGENTS.md, Cursor: .cursorrules). Without a strategy, teams either maintain duplicate files that drift or accept that some tools operate without project context.

## Why People Are Using It

Observed across [Archon](https://github.com/coleam00/archon) v0.3.2, [n8n](https://github.com/n8n-io/n8n) v2.16.0, and [LangGraph](https://github.com/langchain-ai/langgraph) v1.1.6 — see [[archon-analysis]], [[n8n-analysis]], and [[langgraph-analysis]] for structural details.

n8n's chain-loading approach is the most elegant: it solves the naming constraint with zero content duplication and a one-line pointer file. Archon's mirroring is the most thorough but requires maintaining three copies. LangGraph's duplication is pragmatic for a small context file (~58 lines) but wouldn't scale.

## Potential Alternatives

A tool-agnostic context standard that all AI tools agree to read (unlikely near-term). A build step that generates tool-specific files from a single source. A symlink strategy (platform-dependent).

## Potential Improvements

A canonical "source" file with tool-specific pointer/adapter files generated automatically. Drift detection tooling that alerts when mirrored files diverge.

## Potential Failure Modes

Content drift between copies (mirroring and duplication strategies). Chain-loader syntax not supported by all tools (n8n's `@` reference is Claude Code-specific). Over-engineering for repos that only use one AI tool.

## Extension — Adapter-Strategy Selection Table (CareerBuddy meta-skill-author, 2026-07-12)

CareerBuddy's meta-skill-author reference layer (`platform-matrix.md`) expands the original three strategies to five and — the new contribution — maps each to the situation where it wins:

| Situation | Strategy |
|-----------|----------|
| Two platforms with identical context-loading mechanism | Symlink (`AGENTS.md -> CLAUDE.md`) — zero drift; Windows needs `mklink /D`; breaks in tarball/zip distribution |
| Two platforms with different command/skill formats | Plugin wrapper + runtime delegation (MemPalace: harness-agnostic `instructions/` source; per-harness wrappers < 40 lines carrying only packaging metadata, never instruction prose) |
| 3–8 platforms, stable skill schema | Template generation (gstack: `.tmpl` sources + build step generate platform-specific SKILL.md files as build artifacts; 38 templates → 41 skills across 8 hosts) |
| Small skill count, maximum per-platform fidelity | Platform-specific mirroring (Archon) |
| Lowest setup effort, highest drift risk | Content duplication (LangGraph) — "not recommended at scale" |

This resolves the "Potential Alternatives" above: both the build-step and symlink alternatives are now production-observed. Two new failure modes come with the added strategies: manually editing a generated file bypasses the template (drift), and a forgotten build step deploys stale SKILL.md; wrapper delegation fails confusingly when the delegated CLI isn't on PATH. Plus a standing "false portability" warning: content ports, but effectiveness may depend on platform features (file watching, subagent spawning) absent on the target.
