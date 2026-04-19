---
name: 'BMAD Builder: Custom Agent and Workflow Creation Tool'
summary: BMAD V6 introduces the BMAD Builder -- a tool for creating custom personalized agents with memory, full workflows for structured processes, and simple skills, all compliant with the BMAD ecosystem.
  Designed for skill-compliant cross-platform operation.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-v6-is-finally-here.md
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
related_findings:
- file: archon-yaml-defined-harness-workflows.md
  rel: same-problem
- file: skills-as-markdown-sop-files-encode-processes.md
  rel: same-problem
- file: specialized-harness-engineering-deterministic-rail.md
  rel: same-problem
---

## What It Is

The BMAD Builder is a meta-tool within BMAD V6 for creating custom agents, workflows, and skills that are compliant with the BMAD ecosystem. Key capabilities: custom personalized agents with memory, full workflows that guide users through structured processes, simple skills for atomic tasks, and ecosystem compliance so created artifacts work across all supported platforms. The builder is described as "no simple skill builder or toy" -- it produces agents that integrate with the broader BMAD module system.

The tool was in early alpha at time of recording, undergoing a heavy rewrite for launch. It is being made "fully skill compliant" to work across Claude Code, Cursor, Auggie, Gemini CLI, GitHub Copilot, Windsurf, and 15+ other platforms.

## Why It Matters

Creating reusable agents and workflows currently requires manual prompt engineering and platform-specific configuration. A builder tool that outputs cross-platform-compatible artifacts lowers the barrier to agent creation and standardizes the output format. The skill compliance aspect is particularly notable -- it signals convergence toward a common skill/agent interchange format across AI coding tools.

## Why People Are Using It

BMAD's community is actively building modules for the upcoming marketplace. The builder enables non-technical users to create agents for domains beyond software (therapy, legal, entertainment, creative writing). The cross-platform skill compliance is the key differentiator -- write once, deploy to any supported IDE or CLI.

## Potential Improvements

Monitor the skill compliance standard as it matures. If a cross-platform skill format emerges from BMAD or the broader ecosystem, MetaSystem skills could adopt it for portability.

## Potential Failure Modes

Early alpha status means the tool may change significantly. Cross-platform skill compliance depends on each platform adopting a common standard, which is not guaranteed. The "everything is a module" approach risks over-abstraction for simple use cases.
