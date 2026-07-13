---
name: "Shared Instructions Source with Multi-Harness Plugin Wrappers"
summary: "Instruction content is authored once in a harness-agnostic directory (e.g., `mempalace/instructions/*.md`). Each harness-specific plugin (Claude Code, Codex CLI, OpenClaw) ships thin wrapper commands/skills that delegate to the shared source at runtime via a CLI call (`mempalace instructions <name>`). Plugin-format churn decouples from instruction content; adding a new harness means packaging metadata, not rewriting instructions."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: cross-platform-context-file-strategy.md
    rel: same-problem
  - file: universal-harness-context-via-symlink.md
    rel: same-problem
  - file: skill-as-package-export-with-references.md
    rel: same-problem
  - file: skill-shipped-inside-the-package-wheel.md
    rel: same-problem
  - file: vendor-neutral-skill-vocabulary-per-harness-tool-maps.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-07-13"
pipeline_status: raw
consumed_by: []
---

## What It Is

A three-layer architecture for command/skill content in a multi-harness package:

1. **Shared source layer** — instruction content authored once in a harness-agnostic location (`mempalace/instructions/init.md`, `.../help.md`, `.../mine.md`, `.../search.md`, `.../status.md`). This is the single source of truth for *what each command does*.
2. **Harness wrapper layer** — each harness gets its own plugin directory (`.claude-plugin/commands/*.md`, `.codex-plugin/skills/*/SKILL.md`, `integrations/openclaw/SKILL.md`). These are thin shells that delegate at runtime.
3. **Runtime delegation** — the harness wrapper's content is essentially: "Run `mempalace instructions <command>` and follow what it returns." The shared-source content is fetched dynamically rather than statically inlined.

The wrapper files carry *only* harness-specific packaging metadata — plugin.json, hooks.json, marketplace.json, SKILL frontmatter, MCP registration. They do not carry instruction prose.

Contrast with the universal-harness symlink pattern (see [[universal-harness-context-via-symlink]]): the symlink pattern works when both harnesses have the same context-loading mechanism (auto-load a named markdown file at repo root). Plugin wrappers solve a different problem — each harness has a *different* command/skill format, so a single file can't serve both. The shared-source pattern handles the format divergence by keeping the instruction content in one place and letting the harness-specific wrappers delegate to it.

## Why It Matters

Multi-harness packaging has two failure modes: instruction drift (the Cursor version says one thing, the Claude version says another) and format coupling (a change in Anthropic's command schema forces a rewrite of instruction content that should be harness-agnostic). This architecture eliminates both. Instruction authors write one file; adding a new harness means adding a wrapper directory, not rewriting instructions.

For MetaSystem's own skills, this is directly relevant. Our cross-system skills (`/prompt-evaluator`, `/prompt-enhancer`, `/governance-audit`, `/session-handoff`) currently live at workspace root `.claude/skills/` — harness-coupled to Claude Code's format. If MetaSystem ever needs to publish these for Codex CLI or OpenClaw consumption, this pattern is the template.

## Why People Are Using It

Observed in [MemPalace](https://github.com/MemPalace/mempalace) 3.3.2 — see [[mempalace-analysis]] for structural details. MemPalace ships three plugin surfaces (`.claude-plugin/`, `.codex-plugin/`, `.agents/`) plus an OpenClaw integration SKILL. All five commands (init, help, mine, search, status) have identical behavior across harnesses because the harness wrappers all delegate to `mempalace instructions <name>`, which reads from `mempalace/instructions/*.md`. The wrapper files are <40 lines each; the instruction sources are 1.7k–3.8k bytes each. No instruction content is duplicated.

## Potential Alternatives

- **Full content duplication** — authoring the same instructions in three plugin directories. Works but drifts.
- **Single-harness commit** — ship only Claude Code or only Codex CLI bindings. No cross-harness compatibility.
- **Build-step generation** — a single source compiled into harness-specific wrappers by a build script. Works if the project already has a build pipeline.
- **Runtime-fetched from HTTP** — wrappers call an HTTP endpoint to fetch instruction content. Decouples content and binary but adds a network dependency.

## Potential Improvements

- **Versioned instruction contracts.** If `mempalace instructions init` changes its output shape between CLI versions, plugin wrappers could break silently. A contract version field in the CLI output would let wrappers fail loudly on incompatible versions.
- **Test harness that verifies wrapper coverage.** For every instruction file in the shared source, every harness wrapper directory should have a corresponding entry. A CI check catches missing wrappers.
- **Dev-mode inlining.** For local iteration, a dev flag that inlines the instruction content into the wrapper would shortcut the CLI call and speed up iteration.

## Potential Failure Modes

- **Runtime dependency on the CLI.** If `mempalace` isn't installed or on the PATH when the wrapper runs, the delegation fails and the harness user sees a confusing error. The wrapper could include a pre-check that verifies CLI availability.
- **Instruction drift when a harness needs platform-specific steps.** If one harness truly needs different setup (e.g., Windows-specific pip invocation vs Linux), forcing everything through a shared source either duplicates platform logic in the CLI or produces harness-wrong instructions. Pragmatic exit: the wrapper can wrap *and* override, but this re-opens the drift surface.
- **Opaqueness in the harness UI.** Users browsing the `.claude-plugin/commands/init.md` file see only a wrapper, not the actual steps. Discovery requires knowing the shared-source location.
