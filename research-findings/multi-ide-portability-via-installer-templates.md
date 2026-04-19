---
name: Multi-IDE Portability via Installer Templates
summary: BMAD packages the same skills for 7+ IDE platforms (Claude Code, OpenCode, Kiro, Windsurf, Trae, Rovodev, Antigravity) via installer templates. Same skills, different harness packaging. Demonstrates
  that SKILL.md-based architecture is genuinely platform-agnostic.
implementation_notes: null
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: skills-migration-claude-code-to-co-work-for-dis.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-08'
pipeline_status: "raw"
consumed_by: []
---
## What It Is

BMAD maintains installer templates in `tools/installer/ide/templates/` that package the same skill definitions for 7+ IDE platforms: Claude Code, OpenCode, Kiro, Windsurf, Trae, Rovodev, and Antigravity. Each template adapts the SKILL.md format to the target platform's conventions — different file locations, configuration schemas, and activation mechanisms — while the underlying skill content remains identical.

This demonstrates a key architectural property: when skills are defined as self-contained markdown files with a consistent schema, they can be deployed across fundamentally different AI-assisted development environments without rewriting the skill logic. The installer template is a thin adapter layer; the skill is the portable unit.

## Why It Matters

The AI-assisted development tool landscape is fragmenting rapidly. Teams may use Claude Code for some workflows, Windsurf for others, and switch tools as capabilities evolve. If agent skills are tightly coupled to a specific platform, every tool switch requires rewriting accumulated organizational knowledge.

Platform-agnostic skills mean organizational investment in agent capabilities is preserved across tool migrations. The installer template pattern provides a concrete mechanism for achieving this — a thin translation layer rather than a deep integration.

## Why People Are Using It

Observed in [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.2.2 — see [[bmad-method-analysis]] for structural details.

The breadth of supported platforms (7+) indicates real demand for portability. Compare to gstack (8 host configs with template generation) and Superpowers (5 platform integrations via plugin directories). BMAD's approach is the most explicit about the adapter-template mechanism.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Single-platform optimization | Deep integration with one IDE's native extension system | When locked into one platform and maximum platform-specific capability matters |
| Plugin-directory approach | Platform-specific plugin directories with shared core (Superpowers model) | When platforms have fundamentally different plugin models requiring more than templates |
| Template generation from schema | Generate platform-specific configs from a canonical schema (gstack model) | When the translation is complex enough to warrant code generation rather than static templates |
| Universal agent protocol | Wait for a standard agent protocol (e.g., MCP convergence) | When standardization is imminent and custom adapters would be throwaway work |

## Potential Improvements

- Define a test harness that validates skill behavior is equivalent across platforms after template adaptation
- Explore whether the template layer can be auto-generated from platform capability manifests rather than hand-maintained
- Document which platform-specific features are unavailable through the portable skill layer (the portability tax)

## Potential Failure Modes

- **Lowest common denominator**: Portable skills may be limited to capabilities available on all platforms, missing platform-specific advantages
- **Template drift**: 7+ templates must be updated whenever the skill schema changes; templates for less-popular platforms may fall behind
- **Platform-specific behavior differences**: Same skill content may produce different behavior on different platforms due to underlying model differences, tool availability, or context handling
- **False portability**: The skill content is portable but the skill's effectiveness may depend on platform-specific features (e.g., file watching, sub-agent spawning) that not all platforms support
- **Maintenance multiplication**: Every new platform requires a new template; every skill schema change requires updating all templates
