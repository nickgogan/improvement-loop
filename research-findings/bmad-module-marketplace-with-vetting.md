---
name: BMAD Module Marketplace with Quality and Security Vetting
summary: A curated marketplace for community-built BMAD modules with mandatory quality and security vetting. "Unlike any random skill repository, these things are fully vetted for both quality and security."
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
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
related_findings:
- file: bmad-help-adaptive-module-routing.md
  rel: same-problem
---

# BMAD Module Marketplace with Quality and Security Vetting

## What It Is
A curated marketplace for community-built BMAD modules (announced with a 2-3 week timeline). Unlike open skill repositories where anyone can publish without review, BMad's marketplace requires mandatory quality and security vetting before a module is listed.

## Why It Matters
Current agent skill repos (GitHub, npm) have no quality or security gate. Anyone can publish a skill that makes unsafe tool calls, leaks context, or simply does not work as described. A vetted marketplace addresses the trust/safety gap in open skill ecosystems.

## Why People Are Using It
The vetting process covers both functional quality (does the module work as described) and security (does it follow safe patterns, no malicious tool calls). This gives users confidence when incorporating community modules into their agent workflows.

## Potential Improvements
Relevant if MetaSystem ever opens to external skill contributions or evaluates third-party skills. The vetting model could inform MetaSystem's own skill review process -- establishing clear quality and security criteria before a skill is promoted from incubator to active use.

## Potential Failure Modes
Vetting bottleneck slows community contribution velocity. Needs clear, published criteria and ideally automated checks (linting, sandboxed execution) to scale review. Risk of becoming a gatekeeper that stifles innovation if vetting is too subjective or slow.
