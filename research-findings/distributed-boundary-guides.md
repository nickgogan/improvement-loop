---
name: Distributed Boundary Guides
summary: OpenClaw places AGENTS.md/CLAUDE.md symlink pairs at each major subsystem boundary. Root AGENTS.md (~300 lines) sets global rules; subsystem files add local constraints. CLAUDE.md is always a symlink
  to AGENTS.md for cross-AI-tool compatibility. Progressive disclosure for governance.
implementation_notes: null
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: context-file-taxonomy-claudemd-soulmd-agentsmd.md
  rel: extends
- file: middleware-as-enforcement-architecture.md
  rel: same-problem
- file: three-enforcement-pipeline-architectures.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
## What It Is

OpenClaw places AGENTS.md files at each major subsystem boundary — `extensions/`, `src/channels/`, `src/plugins/`, `src/gateway/`. The root AGENTS.md (~300 lines) establishes global rules applicable everywhere. Each subsystem AGENTS.md adds subsystem-specific constraints: import restrictions, public contract definitions, testing requirements, and boundary rules specific to that area of the codebase.

At each location, CLAUDE.md is a symlink pointing to AGENTS.md. This ensures that both Claude Code (which reads CLAUDE.md) and other AI tools (which may read AGENTS.md or other convention files) see identical governance context. The symlink is the compatibility mechanism — one source of truth, two access paths.

This creates progressive disclosure: an agent working in `src/plugins/` loads the root rules plus the plugins-specific rules, without being burdened by gateway-specific constraints that are irrelevant to its current scope.

## Why It Matters

Monolithic context files (one large CLAUDE.md at the project root) scale poorly. As a project grows, the root file accumulates rules for every subsystem, and agents working in any part of the codebase must process all of them. This wastes context budget and increases the chance of rule conflicts.

Distributed boundary guides solve this by scoping rules to the subsystem where they apply. The root file carries only universal rules. Subsystem files carry local rules. An agent working in a specific subsystem gets a focused, relevant ruleset rather than a global dump.

The symlink pattern is a pragmatic solution to the multi-tool compatibility problem. Rather than maintaining separate files for each AI tool's convention, one canonical file (AGENTS.md) is symlinked to each tool's expected filename.

## Why People Are Using It

Observed in [OpenClaw](https://github.com/openclaw/openclaw) v2026.4.5 — see [[openclaw-analysis]] for structural details.

The pattern is used at 4+ subsystem boundaries in a real codebase, indicating it scales beyond a proof-of-concept. The symlink approach to cross-tool compatibility is a practical engineering solution that avoids file duplication.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Single root context file with sections | One file with clearly labeled sections per subsystem | Small projects where the total rule count fits comfortably in context |
| Dynamic context assembly | Rules assembled at runtime based on the agent's current working directory | When the file system layout doesn't cleanly map to subsystem boundaries |
| Hierarchical inheritance (CSS-like) | Child rules override parent rules with explicit cascade semantics | When subsystem rules need to modify (not just extend) root rules |
| Tagged rule system | All rules in one file with tags; loader filters by current context | When rule granularity is finer than subsystem boundaries |

## Potential Improvements

- Define explicit inheritance semantics — can a subsystem AGENTS.md override a root rule, or only add new ones?
- Explore whether the symlink pattern should be standardized across the ecosystem (AGENTS.md as canonical, everything else as symlink)
- Add a validation step that checks for conflicts between root and subsystem rules

## Potential Failure Modes

- **Rule fragmentation**: Distributing rules across many files makes it harder to get a complete picture of all active rules
- **Inheritance ambiguity**: Without explicit override semantics, it is unclear whether a subsystem rule supplements or replaces a root rule
- **Symlink maintenance**: Symlinks can break during file moves, renames, or cross-platform operations (Windows symlink support is limited)
- **Stale subsystem files**: Root rules may be updated while subsystem files lag behind, creating inconsistencies
- **Discovery difficulty**: New contributors may not realize subsystem AGENTS.md files exist if they only look at the root
