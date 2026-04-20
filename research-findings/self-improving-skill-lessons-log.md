---
name: "Self-Improving Skill with Lessons Log"
summary: "Individual skills include a self-improvement phase and a Lessons Log table. After every use, the skill checks for lost work, token waste, and user corrections, then updates its own file. Creates a production-tested feedback loop within individual skills without requiring a separate eval framework."
implementation_notes: "MetaSystem skills don't currently self-modify. The IL's self-evolving loop operates at system level. OB1's approach pushes the improvement loop down to individual skill granularity — each skill carries its own operational history."
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "self-evolving-loop-pattern.md"
    rel: "extends"
  - file: "meta-skill-for-skill-authorship.md"
    rel: "same-problem"
  - file: "eval-driven-tool-iteration-loop.md"
    rel: "same-problem"
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: raw
consumed_by: []
---

## What It Is
A skill design pattern where each skill file includes a Phase 4 "self-improvement" step and a persistent Lessons Log table. After every invocation, the skill evaluates: (1) Did any work get lost? (2) Was token usage reasonable? (3) Did the user correct the extraction? If any lesson is learned, the skill updates its own file immediately.

The Panning for Gold skill in OB1 demonstrates this with 6 documented lessons from production sessions, including: "Background evaluator agents lost to compaction — evaluators must write to permanent files" and "10 speaker labels generated for 2-person conversation — must clean speaker data before extraction." Each lesson maps to a concrete rule change in the skill file.

## Why It Matters
System-level improvement loops (like MetaSystem's IL) operate on a scan-report-deploy cadence. This pattern pushes improvement down to the individual skill level — each skill accumulates its own operational wisdom. Failure modes that are skill-specific (token waste from re-reading, compaction-induced data loss) get captured where they matter, not in a centralized report.

## Why People Are Using It
Observed in [OB1 (Open Brain)](https://github.com/NateBJones-Projects/OB1) — see [[ob1-analysis]] for structural details. The Panning for Gold skill (v2.0.0) has been through 13+ sessions of iterative refinement. Six of its rules were added after production failures, including a complete Phase 0.5 (Speaker Consolidation) that was added after a lunch meeting transcript misattributed 40+ threads due to auto-generated speaker labels.

## Potential Alternatives
- **System-level eval loops** (MetaSystem's self-evolving loop, OpenAI's self-evolving agents pattern): Operate at system scope, not skill scope. Better for cross-cutting concerns but miss skill-specific failure modes.
- **Separate eval frameworks** (binary evals, test suites): More rigorous but require infrastructure. The lessons log is zero-infrastructure — just markdown appended to the skill file.

## Potential Improvements
- Version-tracking the lessons (currently flat table — could track which version of the skill each lesson applies to)
- Cross-skill lesson aggregation — common failure modes (compaction, token waste) recur across skills and could be promoted to shared guidance
- Automated regression detection — if a previously-learned lesson is violated, flag it

## Potential Failure Modes
- Skill files grow unbounded as lessons accumulate — needs periodic pruning
- Self-modification can introduce errors (the skill edits its own process steps based on lessons)
- Lessons learned from one user's environment may not transfer to another
