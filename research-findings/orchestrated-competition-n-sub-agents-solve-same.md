---
notion_id: 32b1e08b-9b34-81d0-8a20-e474d7b82ae3
name: 'Orchestrated Competition: n Sub-Agents Solve the Same Problem in Parallel'
summary: Spawn n sub-agents to solve the same problem from different perspectives simultaneously, then select the winner by quantitative test or qualitative judgment — samples the LLM's probabilistic solution
  space rather than accepting the first output.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- these-3-frameworks-make-claude-code-unstoppable.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-09'
related_findings:
- file: competitive-module-development-parallel-teams.md
  rel: extends
- file: archon-yaml-defined-harness-workflows.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Orchestrated Competition: n Sub-Agents Solve the Same Problem in Parallel

## What It Is
For problems where the best solution is uncertain (UI design, algorithm choice, API design), spawn 3-5 sub-agents with the same goal but different approaches or framings. Run them in parallel in git worktrees or isolated directories. After completion, evaluate the outputs: either run the same test suite against all outputs and pick the highest scorer, or inspect outputs qualitatively and pick the most compelling one. The pattern exploits both the parallel and probabilistic nature of LLMs — different model instances produce genuinely different solution trajectories, not just minor variations. This can be applied recursively: the winning output becomes the input for a new round of competitive sub-agents for the next problem layer.

## Why It Matters
Traditional single-agent coding accepts the LLM's first attempt. Competition patterns sample the distribution of possible solutions and select from the best of the sample. This is especially valuable in UI/animation/design work where quality is subjective and 'first attempt' acceptance leaves gains on the table.

## Why People Are Using It
Closes the feedback loop on design decisions in seconds rather than days. Particularly useful when the developer has a preference but cannot articulate precise specs in advance.

## Potential Alternatives
Sequential prompt iteration ('try a different approach'). A/B testing in production (slower, requires real users). Human design review of multiple mockups.

## Potential Improvements
Automated test-based winner selection for algorithmic problems. Recursive competition (applying the pattern across multiple refinement layers).

## Potential Failure Modes
5 parallel sub-agents generate 5x token cost — cost-benefit analysis needed for each use case. If the evaluation criterion is poorly defined, winner selection is arbitrary. Sub-agents may converge on similar solutions if the problem framing is too constraining.
