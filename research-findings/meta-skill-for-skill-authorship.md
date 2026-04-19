---
name: Meta-Skill for Skill Authorship
summary: Superpowers' writing-skills/ directory contains a skill that teaches agents how to write skills — including persuasion principles, Anthropic best practices, testing methodology, and example skills.
  Self-referential capability development enabling the framework to extend itself.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Meta-Skill for Skill Authorship

## What It Is
Superpowers includes a `writing-skills/` directory containing a skill whose purpose is to teach agents how to write new skills for the framework. This meta-skill includes: persuasion principles to apply (from Meincke et al. 2025), Anthropic best practices for skill structure, testing methodology for validating new skills, and example skills to use as templates. The system that defines skills also has a skill for defining skills — enabling agents to contribute to the framework's own growth.

## Why It Matters
Most agent frameworks are human-extended only — when you need a new capability, a human writes the new skill. A meta-skill for skill authorship enables agent-assisted framework extension. The agent can draft new skills following the established patterns, applying the correct persuasion principles, and structuring output to match the framework's conventions. This creates a self-reinforcing loop: the more skills the framework has, the better the meta-skill's examples, the better the agent gets at writing new skills.

## Why People Are Using It
Observed in [Superpowers](https://github.com/obra/superpowers) v5.0.7 — see [[superpowers-analysis]] for structural details. No equivalent exists in GSD, BMAD, or other analyzed repos. GSD's skills are authored by the framework maintainer. BMAD's persona definitions are human-written. Superpowers is the only analyzed repo that has formalized skill authorship as itself a skill, closing the meta-loop.

## Potential Alternatives
Human-only skill authorship with documentation guides. Template-based scaffolding (generate skill boilerplate, human fills in logic). Copy-paste from existing skills without formalized methodology. External tooling that generates skills from specifications.

## Potential Improvements
Skill testing automation — the meta-skill could include a test harness that validates new skills against behavioral expectations before deployment. Skill quality scoring that evaluates how well a new skill applies the persuasion principles and structural patterns. Skill registry that catalogs all skills with metadata, making it easier for the meta-skill to find relevant examples. Version tracking for skills so changes can be reviewed and rolled back.

## Potential Failure Modes
Quality degradation — agent-written skills may be subtly worse than human-written ones, and the degradation compounds if agent-written skills are used as examples for writing future skills. Consistency drift — without strong validation, each generation of agent-written skills may drift further from the framework's design principles. Over-production of low-value skills that clutter the framework without adding meaningful capability. The meta-skill itself needs maintenance as the framework's conventions evolve.
