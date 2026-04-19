---
name: Everything-as-Skill Architecture
summary: Post-v6.2.2, BMAD merged agents, workflows, and personas into a unified SKILL.md-based architecture. Agent personas ARE skills — when activated, the skill "becomes" the persona. Eliminates the
  agent/skill/workflow three-way distinction.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: extends
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
## What It Is

In BMAD Method v6.2.2, agents, workflows, and skills were consolidated into a single architectural unit: the SKILL.md file. Named agent personas — Mary the Analyst, John the PM, Winston the Architect, Amelia the Dev — are no longer separate definitions maintained alongside skill files and workflow definitions. Instead, each persona IS a skill. When a skill is activated, the agent "becomes" the persona defined in that skill, inheriting its communication style, domain expertise, and sub-skill menu.

This eliminates the three-way distinction between agents (who), skills (what), and workflows (how) that frameworks like GSD maintain as separate concepts. In the everything-as-skill model, there is one primitive: the skill. Identity, capability, and process are all encoded in the same artifact.

## Why It Matters

Multi-agent frameworks frequently suffer from a proliferation of configuration types — agent definitions, skill registries, workflow specifications, persona templates — each with its own schema and lifecycle. This creates maintenance overhead and conceptual fragmentation. A developer must understand three or more abstractions to trace how work flows through the system.

Collapsing these into a single SKILL.md primitive simplifies the mental model: one file type, one schema, one loading mechanism. It also simplifies the runtime — there is no agent/skill binding step because the skill already contains the agent.

## Why People Are Using It

Observed in [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.2.2 — see [[bmad-method-analysis]] for structural details.

The consolidation appears to have been driven by practical experience maintaining the earlier multi-artifact architecture across 7+ IDE platforms. Fewer artifact types means fewer adapter templates per platform.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Separate agent/skill/workflow definitions | Traditional three-way split (e.g., GSD model) | When agents need to compose arbitrary skills at runtime rather than being bound to a fixed skill set |
| Role-based skill composition | Skills are capabilities; roles are composable sets of skills (no persona) | When persona consistency is not needed and flexibility matters more |
| Capability-based skills without identity | Skills define what to do, not who does it (e.g., Superpowers model) | When multiple agents should share the same skill without inheriting a persona |

## Potential Improvements

- Define a mechanism for skill composition — can one skill invoke sub-skills while maintaining persona consistency?
- Explore whether the everything-as-skill model supports runtime skill discovery or if all skills must be pre-registered
- Document the migration path from a three-way architecture to everything-as-skill for existing systems

## Potential Failure Modes

- **Persona lock-in**: If a skill IS a persona, switching between analytical and creative modes requires switching skills entirely, which may lose accumulated context
- **Skill bloat**: Encoding identity, capability, and process in one file may make individual SKILL.md files large and difficult to maintain
- **Reduced composability**: The three-way split exists because it enables mix-and-match — Agent A with Skill B using Workflow C. Collapsing these removes that combinatorial flexibility
- **Platform-specific persona behavior**: Different LLMs may interpret persona instructions differently, making the "becomes the persona" guarantee unreliable across platforms
