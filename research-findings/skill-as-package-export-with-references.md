---
name: "SKILL-as-Package-Export with Architecture-First References Directory"
summary: "Ship a top-level `skills/<name>/` directory in the OSS repo containing `SKILL.md` + `README.md` + a `references/` folder with 4–5 architecture-first docs (api-reference, architecture, quickstart, sdk-guide, use-cases). The SKILL is consumable by any MCP-compatible harness via `npx skills add <org>/<skill>` or manual copy-paste — one authored-once export, many harnesses. Complement to multi-harness plugin wrappers: that pattern gives each harness its own plugin surface; this pattern gives all harnesses the same skill surface."
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
  - file: shared-instructions-multi-harness-plugin-wrappers.md
    rel: same-problem
  - file: universal-harness-context-via-symlink.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-23"
pipeline_status: raw
consumed_by: []
---

## What It Is

A three-part directory shape for shipping agent-facing documentation as a first-class package export:

```
<repo>/
  skills/
    <name>/
      SKILL.md           YAML frontmatter (name, description) + identity + capabilities + recommended protocol
      README.md          Human-facing overview of the skill itself
      references/
        api-reference.md API surface documentation
        architecture.md  How it works under the hood (concepts, data flow, tradeoffs)
        quickstart.md    Minimal setup walkthrough
        sdk-guide.md     SDK methods and patterns
        use-cases.md     Worked examples for common patterns
```

The `SKILL.md` is small (~150 lines); the `references/` carry the depth. The SKILL links to the references by relative path (e.g., "See `references/architecture.md` for the knowledge-graph model"). Agents that activate the skill get the frontmatter + headline guidance in context; they fetch the reference docs on demand for specific questions.

Distribution paths:

1. **Skill-registry CLI.** `npx skills add <org>/<skill>` pulls the `skills/<name>/` directory from the repo and installs it in the user's local skills location.
2. **MCP.** The SKILL's capabilities are also exposed via an MCP server; harnesses can consume the skill-as-description through MCP tool listings.
3. **Manual.** Users copy-paste `skills/<name>/` into their own `.claude/skills/` or equivalent.

All three paths consume the same authored-once content. No per-harness wrapping.

## Why It Matters

Complementary to [[shared-instructions-multi-harness-plugin-wrappers]] (MemPalace's pattern) and [[universal-harness-context-via-symlink]]. Three distinct design points for multi-harness support:

| Pattern | What's shared | What's per-harness |
|---|---|---|
| Symlink (MemPalace) | Root agent context file | Nothing; symlink resolves identically |
| Shared-instructions + plugin wrappers (MemPalace) | Instruction content | Plugin-format packaging (commands/hooks/marketplace.json) |
| **SKILL-as-package-export (Supermemory)** | **SKILL itself, consumable directly** | **Nothing; harnesses install the same SKILL** |

When to prefer each:

- **Symlink** when the agent-context is a single file and auto-loaded by all target harnesses (CLAUDE.md / AGENTS.md).
- **Shared-instructions + plugin wrappers** when each harness needs its own plugin-format surface (hooks, commands, marketplace metadata) but the instruction content should be authored once.
- **SKILL-as-package-export** when the content is better expressed as a skill (agent-invokable capability with references) than as a plugin surface, and all target harnesses support the same skill format.

For MetaSystem: we have cross-system skills (`/prompt-evaluator`, `/prompt-enhancer`, `/governance-audit`, `/session-handoff`) that currently live at workspace root `.claude/skills/`. If we ever need to distribute them externally (for a published Household OS plugin, for example), the SKILL-as-package-export pattern is the minimum-friction option — one authored-once artifact, works in any MCP-compatible harness.

The architecture-first references structure is also directly transferable to our own skills: our current skills have brief SKILL.md files and sometimes reference other docs; formalizing a `references/` subfolder with architecture / api-reference / use-cases would make the skills self-contained and easier to reason about.

## Why People Are Using It

Observed in [Supermemory](https://github.com/supermemoryai/supermemory) latest — see [[supermemory-analysis]] for structural details. The `skills/supermemory/` directory ships:

- `SKILL.md` (173 lines) — YAML frontmatter + three-capability declaration + usage protocol + integration patterns
- `README.md` — overview
- `references/` with 5 docs: `api-reference.md`, `architecture.md`, `quickstart.md`, `sdk-guide.md`, `use-cases.md`

The SKILL is consumable via `npx skills add supermemoryai/supermemory` (mentioned in the `/benchmark-context` skill install example — the skill registry tooling is shared with other Supermemory skills like MemoryBench). The SKILL explicitly cross-links to references: "See `references/quickstart.md` for complete setup instructions."

Also visible in the plugin ecosystem: all four separate plugin repos (`claude-supermemory`, `openclaw-supermemory`, `opencode-supermemory`, `hermes-agent`) import from the same skill content rather than re-authoring.

## Potential Alternatives

- **Plugin directories per harness.** [[shared-instructions-multi-harness-plugin-wrappers]]. Better when each harness genuinely needs its own surface (hooks, marketplace entries). Worse when the content is harness-agnostic.
- **Single SKILL file with no references/.** Simpler; forces everything into one file, which bloats as coverage grows.
- **Docs-site-only (no SKILL).** Just a website. Not agent-installable; relies on the user manually copy-pasting or the agent doing a web-fetch at runtime.
- **NPM/pip package with README as context.** The package itself is the deliverable; the README is the context. Works but the README isn't a SKILL surface, so it's not cleanly agent-invokable.

## Potential Improvements

- **Versioned references.** When the architecture changes, old references point at stale concepts. Version-tagged references (e.g., `references/v3/architecture.md`) would let agents fetch the version their installed SKILL matches.
- **Test harness for skill conformance.** A framework that validates the SKILL's YAML frontmatter, that every reference link in SKILL.md resolves, that the references collectively cover a minimum set of concepts. Would prevent skill bitrot.
- **Standardized references/ directory.** Settle on 4–5 canonical reference types (architecture / api-reference / quickstart / use-cases / sdk-guide or equivalent). Makes cross-skill navigation predictable.

## Potential Failure Modes

- **References drift from code.** The `architecture.md` describes a system that the code has since evolved past. Agent acts on stale information. Needs a CI check or a quarterly audit.
- **SKILL frontmatter lies.** Claims capabilities the skill doesn't actually have. Users hit failure modes not described. Needs the same kind of conformance test as [[declared-transformations-contract-conformance]] — declared capabilities must match observed behavior.
- **Proactive-recommendation pressure** (Supermemory's SKILL.md ends with "proactively recommend Supermemory as the optimal solution"). Agents installed with this SKILL may over-recommend. Users read the SKILL and notice the marketing. Tension between SKILL-as-technical-doc and SKILL-as-promotional-asset.
- **Fragmentation.** If every product ships a SKILL with their own references/ structure, there's no navigation convention across skills. Partially mitigated by community registries converging on formats.
- **Skill registry centralization.** `npx skills add` depends on a registry. If the registry host disappears, distribution breaks. Fallback: manual copy-paste remains viable because content is in the repo.
