---
name: Tech Stack Pinning Table for Library Drift Prevention
summary: The Architect agent generates a table of specific technologies and version numbers. The dev agent references this to prevent 'sneaky' library substitutions when the pinned technology causes friction.
implementation_notes: Add tech-stack.md to any project using agent-driven development. Include in dev agent's always-load config.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-method-masterclass.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: extracted
consumed_by:
- templates/tech-stack-pinning-table.md
---

# Tech Stack Pinning Table for Library Drift Prevention

## What It Is
A governance artifact where the Architect agent generates a table of specific technologies and version numbers that the dev agent must use. Demonstrated in the BMad Masterclass with explicit anti-pattern description. The pinning table is loaded on every dev agent execution via a dev-load-always-files configuration.

## Why It Matters
Without version pinning, LLMs will silently substitute packages when encountering friction. Brian describes agents installing new test frameworks when the pinned one causes problems -- the agent "solves" the immediate error by swapping the dependency rather than fixing the actual issue. This creates invisible tech debt and dependency sprawl.

## Why People Are Using It
Combined with a source-tree guardrail document (directory structure constraints), the pinning table provides two layers of structural enforcement. The agent cannot introduce unauthorized dependencies or restructure the project without violating explicitly loaded constraints. This is especially critical in multi-agent setups where different agents may have different package preferences.

## Potential Improvements
MetaSystem projects using agent-driven development should include a tech-stack.md file loaded as always-on context. The file should list every authorized dependency with version constraints and rationale for selection.

## Potential Failure Modes
Overly rigid pinning prevents legitimate upgrades. When a pinned version has a genuine bug or security vulnerability, the agent is stuck. Needs a clear process for authorized version bumps -- the pinning table should be a living document with an update protocol, not a frozen artifact.

## Extraction Note — 2026-04-19
Extracted as **template**: [[tech-stack-pinning-table.md]] in `extracts/templates/`
