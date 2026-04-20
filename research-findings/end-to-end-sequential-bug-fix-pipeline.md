---
name: End-to-End Sequential Bug-Fix Pipeline
summary: A single skill chains an entire bug-fix workflow — read ticket (Jira MCP) → reproduce (Playwright) → research → implement → review (sub-agents) → verify (Playwright) → commit → deploy → QA push
  — executing all stages in strict sequential order within one orchestrator thread.
implementation_notes: Sub-agents can be spawned at individual stages (review, QA) to avoid context bloat in the main thread; the pipeline as a whole is still sequential even if a stage internally uses parallelism.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- five-claude-code-agent-patterns.md
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-20'
related_findings:
- file: skill-chaining-composing-workflows-from-modular-s.md
  rel: same-problem
- file: builder-validator-chain-pattern.md
  rel: same-problem
- file: two-stage-sequential-review.md
  rel: same-problem
- file: dag-vs-bsp-two-graph-based-orchestration-models.md
  rel: same-problem
- file: claude-routines-webhook-triggered-pipeline-chaining.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
## What It Is

A fully automated bug-fix skill that chains all stages of a software fix pipeline in strict sequential order within a single orchestrator thread:

1. **Read ticket** — Jira MCP fetches bug description and acceptance criteria
2. **Reproduce** — Playwright CLI verifies the bug is reproducible
3. **Research** — sub-agent gathers relevant context (codebase, docs, prior fixes)
4. **Implement** — the fix is written
5. **Review** — multiple specialist sub-agents review the changes (frontend, backend, testing)
6. **Verify** — Playwright CLI re-runs to confirm the fix resolved the bug
7. **Commit** — changes committed to version control
8. **Deploy** — change deployed to environment
9. **QA push** — changes promoted to QA session (possibly via sub-agent)

The key characteristic: stages must complete in order. Stage N cannot start until Stage N-1 is complete. This sequential dependency is intentional — you cannot commit an unverified fix, and you cannot verify before implementing.

Sub-agents appear within individual stages (review, research, QA) to contain context growth, but their results must feed back to the main thread before the next stage begins.

## Why It Matters

Manual bug-fix workflows require a developer to context-switch through multiple tools (Jira, IDE, test runner, CI/CD) across hours. A sequential pipeline skill compresses this into a single invocation that runs autonomously from ticket to QA. Each stage uses the right tool for the job (Playwright for reproduction, Jira MCP for ticket reads, sub-agents for review) composable under one skill definition.

The pipeline also encodes institutional process: you cannot skip verification, you cannot deploy without review. The skill makes implicit process explicit and enforceable.

## Why People Are Using It

Speaker (ex-Amazon/Microsoft AI engineer) demonstrated the `fix-tickets` skill as their primary sequential flow example. The pattern is compelling because it converts a multi-hour human workflow into a single `claude fix-tickets` invocation. The speaker explicitly called out that sub-agents at specific stages do not change the sequential nature of the pipeline.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Manual pipeline | Developer coordinates each tool manually | When bug complexity requires human judgment at each step |
| Split-and-merge | Parallelize multiple fixes simultaneously | When multiple independent bugs can be fixed concurrently |
| CI/CD pipeline (non-agent) | Traditional automated pipeline with scripts | When deterministic tools (linters, tests) suffice without LLM reasoning |

## Potential Improvements

- Conditional branching: if reproduction fails (bug not reproducible), halt and notify rather than proceeding to research
- Staged commit gates: require human approval before deploy step
- Failure logging: if any stage fails, log the stage, error, and attempted fix strategy for retrospective analysis
- Parallel review: the review stage can run N specialist sub-agents concurrently; their outputs should be merged before proceeding to verify

## Potential Failure Modes

- **Context accumulation**: each stage appends to the orchestrator's context; a long pipeline on a large codebase may exhaust the context window before reaching deploy
- **Playwright environment coupling**: the pipeline assumes a working Playwright setup; environment drift breaks reproduction and verification stages
- **Silent failures at handoff**: if a stage produces a misleading success signal, downstream stages act on incorrect state (e.g., a test that passes for the wrong reason)
- **Jira dependency**: ticket-reading via MCP creates an external dependency; Jira schema changes or MCP failures abort the pipeline at stage 1
