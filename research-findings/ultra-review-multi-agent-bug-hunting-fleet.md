---
name: 'Ultra Review: Multi-Agent Bug-Hunting with Verification Pipeline'
summary: 'Claude Code''s hidden Ultra Review feature (codename ''Bug Hunter'') spins up 5-20 sub-agents in parallel on Anthropic''s cloud, each starting from different codebase positions. Four-stage pipeline:
  setup → find (47-64 candidates) → verify (independent agent confirms/refutes each bug) → dedup (merge duplicate findings). The verification stage is the key innovation — it dramatically reduces false
  positives compared to standard review.'
implementation_notes: The find→verify→dedup pipeline pattern is reusable. Even without Ultra Review access, implement independent verification of any multi-agent finding set.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-code-ultra-review-bug-hunter.md
- claude-code-ultra-review-multi-agent-verification.md
related_findings:
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
- file: anthropic-managed-agents-platform.md
  rel: enabled-by
- file: builder-validator-chain-pattern.md
  rel: extends
- file: context-pollution-same-window-verification-bias.md
  rel: same-problem
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
- file: eval-driven-development-autonomous-quality.md
  rel: same-problem
- file: four-layer-agent-evaluation-architecture.md
  rel: same-problem
- file: four-layer-production-eval-stack-with-golden-traces.md
  rel: same-problem
- file: goal-backward-verification.md
  rel: same-problem
- file: gstack-review-army-parallel-specialist-dispatch.md
  rel: same-problem
- file: llm-as-judge-pattern-for-verification-agents.md
  rel: enabled-by
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---
# Ultra Review: Multi-Agent Bug-Hunting with Verification Pipeline

## What It Is
Ultra Review is a hidden feature in Claude Code (behind a feature flag, codename "bug_hunter") that runs on Anthropic's cloud infrastructure. It spins up a fleet of 5 sub-agents (default, max 20) that independently scan a PR or branch for bugs. The four-stage pipeline: (1) Setup — configure the review scope. (2) Find — each sub-agent starts from a different position in the codebase, following different paths. This diversity of context ordering reveals bugs that any single traversal might miss. Found 47-64 candidates in testing on an 11,000-line PR. (3) Verify — an independent verifier sub-agent confirms or refutes each candidate bug. This is the critical innovation: it prevents false positives that plague standard multi-agent review. In testing, many candidates were refuted. (4) Dedup — merge findings where multiple sub-agents found the same bug from different angles. Takes 10-20 minutes on cloud (vs 3-4 minutes for standard local review). Currently limited to ~3 free uses on the $200/month plan. Sub-agents likely use personas (billing-focused, security-focused, etc.) based on binary analysis showing persona-related strings.

## Why It Matters
Standard review tools (including Claude Code's built-in `/review`) spin up sub-agents to find bugs but lack the verification stage. This leads to false positives that waste developer time. The verify stage is what makes Ultra Review qualitatively different — it catches race conditions and lifecycle bugs that standard review misses entirely, because it holds multiple files in context simultaneously.

## Why People Are Using It
Early access users report it finding bugs that standard review completely missed, particularly race conditions and lifecycle issues. The quality difference comes from the independent verification, not just more sub-agents.

## Potential Alternatives
- Standard `/review` command (faster, 3-4 minutes, but no verification)
- Manual code review (thorough but slow)
- Cross-model verification (Claude finds, Codex verifies — see related finding)

## Potential Improvements
- User-configurable fleet size
- Custom persona definitions for domain-specific bug hunting
- Integration with CI/CD pipelines for automated PR review

## Potential Failure Modes
- High cost — 10-20 minutes of cloud compute with multiple sub-agents
- Limited to 3 free uses — unclear pricing for heavy usage
- May use unreleased models for A/B testing, making results non-reproducible

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[multi-agent-find-verify-dedup-pipeline.md]] in `extracts/patterns/`
