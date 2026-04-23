---
name: Audit-Skill as Expert Harness Distribution Channel
summary: Nate B. Jones distributes his "12 agent primitives" expertise as a free installable Claude Code skill package that runs a gap-analysis audit against the user's own codebase and reports which of the 12 primitives are missing. A parallel example is Supermemory's MemoryBench, distributed as `npx skills add supermemoryai/memorybench` — install turns the expert's mental model into a runnable diagnostic against your code. This is a new expert-distribution pattern: replace "read my blog / buy my course" with "install my skill and get a customized report."
implementation_notes: MetaSystem could mirror this pattern once IL is mature — package consumer-facing audits (assess-agent, assess-prompt, assess-skill) as installable skills distributable outside the workspace. Not an adoption goal for this session; pattern worth monitoring.
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- nate-b-jones-your-agent-12-blind-spots-substack.md
- affaan-m-everything-claude-code-repo.md
related_findings:
- file: agent-native-app-store-emerging-category.md
  rel: same-problem
- file: claude-code-12-agent-primitives.md
  rel: extends
- file: skill-self-improvement-three-approaches.md
  rel: same-problem
- file: template-generated-skills-multi-host.md
  rel: enables
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-04-23'
pipeline_status: raw
consumed_by: []
---

# Audit-Skill as Expert Harness Distribution Channel

## What It Is

A class of Claude Code skills where the unit of distribution is an *audit*: install the skill, and it inspects the consumer's own codebase to produce a customized gap-analysis report against the author's mental model.

Observed examples:
- **Nate B. Jones — "12 Agent Primitives" audit**: a free skill package that grades a user's agent against Nate's 12-primitive taxonomy and returns a prioritized gap list
- **Supermemory MemoryBench**: distributed as `npx skills add supermemoryai/memorybench`; runs benchmark-style evaluation against the user's memory adapter
- **affaan-m/everything-claude-code**: 38 agents + 156 skills + 72 legacy command shims packaged together, reading the user's repo and suggesting improvements

The pattern inverts the traditional expertise-distribution model: instead of the reader learning the author's framework and applying it, the framework *arrives as code* and self-applies.

## Why It Matters for Us

Plain English: this is how content experts are starting to deliver their thinking in an agent-first world. A blog post tells you what to think; an installable audit skill runs the thinking against your actual codebase and tells you where *you* specifically are weak. For IL, this matters two ways:

1. **As consumer**: we can test installed audit skills against MetaSystem's own artifacts (agents, prompts, skills) and treat their findings as additional Researcher signal.
2. **As producer**: IL already has `assess-agent`, `assess-prompt`, `assess-skill` internally. Those are candidates for this distribution pattern if/when MetaSystem opens up.

## Why People Are Using It

Nate B. Jones is a Tier-1 practitioner authority with an existing audience; the skill version of his framework is installed by many of the same people who read his Substack. Anthropic's own skills marketplace seems to encourage this distribution shape. Multiple hackathon-originated skill packs (e.g., Cerebral Valley Claude Code Hackathon, Feb 2026) suggest the pattern is crystallizing into a norm.

## Potential Alternatives

- Written framework (blog / book / course) — the reader has to apply it themselves
- Agent-native app-store listing without the audit behavior — just a tool, not a diagnostic
- Paid consulting where the expert runs the audit manually

## Potential Improvements

- A shared "audit output schema" so results from multiple author-skills can be aggregated into one gap report
- Versioning discipline — what happens when the author updates the framework and the installed skill drifts?

## Potential Failure Modes

- Audit outputs are lowest-common-denominator to fit diverse codebases — generic advice
- Trust: an installed skill reads your code and reports results; security model matters
- "Audit inflation" — every expert ships a skill, user drowns in overlapping recommendations
- Static skills can't keep pace with evolving frameworks; outdated audits are worse than no audit
