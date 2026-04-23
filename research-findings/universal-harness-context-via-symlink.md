---
name: "Universal-Harness Context via AGENTS.md ↔ CLAUDE.md Symlink"
summary: "One authored file (CLAUDE.md) holds the agent context; a filesystem symlink named AGENTS.md points at it. Codex CLI reads AGENTS.md, Claude Code reads CLAUDE.md, both resolve to the same bytes. Zero content duplication, zero maintenance overhead, zero drift risk — smallest possible pattern for multi-harness context compatibility."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources: []
related_findings:
  - file: cross-platform-context-file-strategy.md
    rel: extends
  - file: context-file-taxonomy-claudemd-soulmd-agentsmd.md
    rel: same-problem
  - file: skill-as-package-export-with-references.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-23"
pipeline_status: raw
consumed_by: []
---

## What It Is

A filesystem pattern where `AGENTS.md` is a symlink pointing to `CLAUDE.md`:

```
AGENTS.md -> CLAUDE.md
```

Both files are present in the repo. Claude Code auto-loads `CLAUDE.md`; Codex CLI auto-loads `AGENTS.md`. The symlink resolves both paths to the same authoritative content. The author maintains one file; the filesystem makes it look like two files to each harness.

This is a fourth strategy in the cross-platform context problem — complementing the three strategies documented in [[cross-platform-context-file-strategy]]:

| Strategy | Repo | Drift Risk |
|---|---|---|
| Platform-specific mirroring | Archon | High (3 parallel copies) |
| Chain-loader indirection | n8n | Low (one line in CLAUDE.md: `@AGENTS.md`) |
| Content duplication | LangGraph | High (two full copies) |
| **Symlink** | **MemPalace** | **Zero — filesystem makes them one file** |

## Why It Matters

All three prior strategies have at least one weakness: mirroring drifts, chain-loading is tool-specific (`@` reference is Claude Code syntax), duplication drifts. Symlinks have none of these weaknesses — the two paths are literally the same bytes on disk. The cost is only that the filesystem must support symlinks (all UNIX-likes and modern Windows do), and that tooling that crawls the repo must handle symlinks correctly (most do).

For any MetaSystem incubator eventually published to a repo that will be consumed by multiple harnesses, this is the lowest-friction way to provide compatible context without forking content. The Household OS, Claude Build, and any future public surface benefit directly.

## Why People Are Using It

Observed in [MemPalace](https://github.com/MemPalace/mempalace) 3.3.2 — see [[mempalace-analysis]] for structural details. The repo's top-level listing shows `AGENTS.md -> CLAUDE.md` as a symlink; CLAUDE.md holds the full agent context (mission, 7 non-negotiable design principles, project structure, conventions, architecture), and the author's intent is explicit in the structure: a single content source, two harness entry points, no drift surface.

## Potential Alternatives

- **Chain-loader (n8n pattern)** — a one-line CLAUDE.md containing `@AGENTS.md`. Simpler for the author (no symlink knowledge needed) but the `@` syntax is Claude-specific; other harnesses would need to treat `@` as a pointer manually.
- **Content duplication (LangGraph pattern)** — same content in both files. Simplest to understand, but any edit must be applied twice.
- **Mirroring (Archon pattern)** — different adapted content per platform. Maximum fidelity but maximum maintenance burden.
- **Build-step generation** — a single source compiled to multiple outputs. Works for systems that already have a build pipeline; over-engineering for simple repos.

## Potential Improvements

- Document the symlink's intent in CLAUDE.md itself (a one-liner explaining that AGENTS.md is the same file) so readers who follow one path understand the other.
- For Windows compatibility, use `mklink /D` or equivalent; some Git-for-Windows configurations don't honor symlinks by default and must be configured with `core.symlinks=true`.
- Consider pairing with [[cross-platform-context-file-strategy]]'s chain-loader approach when the agent-context content grows beyond a single file (e.g., symlink for the primary context, chain-loading for auxiliary files like TOOLS.md or MEMORY.md).

## Potential Failure Modes

- **Windows without symlink support** — older Git-for-Windows or non-developer-mode Windows may check out `AGENTS.md` as a plain text file containing the literal string `CLAUDE.md`. Harnesses then read broken content.
- **Tarball/zip distribution** — some archive formats don't preserve symlinks; downstream consumers who extract get one real file and one broken pointer.
- **Index-and-search tools** — full-text search tools that follow symlinks will index the content twice, inflating hit counts.
