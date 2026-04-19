---
notion_id: 3351e08b-9b34-81d0-9dea-c35d8a597939
name: Claude Code Skills 2.0 -- Four-Mode Skill Lifecycle with Binary Evals
summary: 'Anthropic redesigned the Claude Code skill-creator (March 3, 2026) with four modes: Create / Eval / Improve / Benchmark. Four parallel sub-agents in isolated contexts: Executor, Grader, Comparator
  (blind A/B), Analyzer. Binary-eval overnight loop: write assertions -> build harness -> configure CLAUDE.md improvement loop -> Claude iterates autonomously for 40-50 cycles. Benchmark mode tracks Pass
  Rate, Elapsed Time, and Token Usage vs. baseline.'
implementation_notes: 'Extends the KB''s Self-Evolving Loop Pattern with specific mechanics and objective measurement. The key addition is Benchmark mode: answering ''does this skill actually improve things
  vs. the baseline?'' with objective metrics. Also adds blind A/B testing between skill versions. GA in Claude Code as of March 7. Source: https://www.mindstudio.ai/blog/self-improving-ai-skills-binary-evals-claude-code'
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- how-to-build-self-improving-ai-skills-with-binary.md
- anthropic-claude-code-best-practices.md
proposals: []
date_discovered: '2026-04-01'
last_updated: '2026-04-09'
related_findings:
- file: ace-execution-feedback-no-labels-required.md
  rel: same-problem
- file: success-rate-eval-over-binary-pass-fail.md
  rel: enables
- file: test-input-coverage-design-15-30-sweet-spot.md
  rel: enables
- file: builder-validator-chain-pattern.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---
# Claude Code Skills 2.0 -- Four-Mode Skill Lifecycle with Binary Evals

## What It Is
A complete self-improving skill lifecycle redesign (Anthropic, March 3 2026). Four Modes: Create, Eval, Improve, Benchmark. Four Parallel Sub-Agents: Executor, Grader, Comparator (blind A/B), Analyzer.

**The overnight loop:** Write binary assertions -> build test harness -> configure improvement loop -> set iteration cap (40-50) -> Claude makes one logical change at a time, runs harness, iterates -> wake up to refined skill with full git history.

## Why It Matters
Key additions: Benchmark mode provides objective measurement. Blind A/B testing removes human confirmation bias. Two improvement layers: trigger/description tuning and output quality improvement.

## Why People Are Using It
GA in Claude Code as of March 7. Anthropic positioned Skills 2.0 as the official workflow for skill maintenance.

## Potential Failure Modes
Binary assertions only capture pass/fail. Test set must cover edge cases. 40-50 iteration cap may not be sufficient for complex skills.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[four-mode-skill-lifecycle]] in `extracts/patterns/`
