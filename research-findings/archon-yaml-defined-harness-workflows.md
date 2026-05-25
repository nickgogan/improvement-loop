---
name: 'Archon: YAML-Defined Harness Workflow DAGs'
summary: Archon is an open-source harness builder that encodes software development workflows as YAML-defined DAGs of nodes. Each node is either an agentic prompt sent to a coding agent session or a deterministic
  command. Supports parallel execution, node-level model selection, human approval gates, and skill/MCP injection per node.
implementation_notes: 'The hybrid deterministic+agentic node approach and per-node model selection are the key patterns. Evidence: Stripe Minion ships 1,300 AI PRs/week using similar harness; PR acceptance
  rate jumps from 6.7% (raw) to ~70% (harnessed).'
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- archon-open-source-harness-builder.md
- archon-live-stream-agent-workflows-dark-factory.md
- dark-factory-archon-autonomous-coding.md
related_findings:
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: same-problem
- file: durable-workflow-engine-for-agent-systems.md
  rel: same-problem
- file: gsd-get-shit-done-plugin.md
  rel: same-problem
- file: multi-framework-orchestration-power-stack.md
  rel: same-problem
- file: orchestrated-competition-n-sub-agents-solve-same.md
  rel: same-problem
- file: orchestrated-execution-one-task-per-sub-agent-wit.md
  rel: same-problem
- file: phase-task-hierarchical-plan-decomposition.md
  rel: same-problem
- file: planner-executor-deterministic-guardrails.md
  rel: same-problem
- file: specialized-harness-engineering-deterministic-rail.md
  rel: same-problem
- file: superpowers-plugin-spec-driven-sub-agent-orchestra.md
  rel: same-problem
- file: bmad-v6-builder-custom-agent-workflow-creation.md
  rel: same-problem
- file: claude-routines-webhook-triggered-pipeline-chaining.md
  rel: same-problem
- file: description-based-workflow-routing-lazy-dispatch.md
  rel: extended-by
- file: parallel-independent-workflow-execution-at-scale.md
  rel: extended-by
- file: per-node-context-scoping-skills-mcps-commands.md
  rel: extended-by
- file: meta-workflow-builder-self-extending-harness.md
  rel: extended-by
- file: cross-project-workflow-portability-register-and-run.md
  rel: extended-by
- file: multi-adapter-workflow-invocation-cli-web-chat-github.md
  rel: extended-by
- file: default-workflow-library-as-adoption-accelerator.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---

## What It Is
Archon (open-source, by the creator of the previous Archon AI command center) sits above coding agents and orchestrates multiple sessions into repeatable workflows. Workflows are YAML files defining a DAG of nodes. Node types: (1) Agentic — a prompt sent into a Claude Code or Codex session. (2) Deterministic — a bash command or script that always runs the same way. (3) Human gate — pauses for approval. Key features: per-node model selection (Haiku for classification, Sonnet for implementation, Opus for planning), separate context windows per node (preventing context rot), parallel workflow execution (6+ simultaneous issue fixes demonstrated), web UI for monitoring, and a skill for invoking workflows from within Claude Code. Ships with default workflows: fix GitHub issue, create PRD, PR review, Ralph loop, adversarial dev. Supporting evidence: 40% of Claude Code's codebase is harness code. Stripe Minion ships 1,300 AI-only PRs/week via harness. Raw AI PR acceptance: 6.7%; harnessed: ~70%.

## Why It Matters
Harness engineering represents the third evolution: prompt engineering → context engineering → harness engineering. Single-agent prompting has a ceiling. Harnesses break through by chaining multiple focused sessions with deterministic validation between them.

## Why People Are Using It
Practitioners report going from "AI shepherding" (manually kicking off skills/commands in sequence) to "define once, run forever" workflows. The parallel execution capability (fixing 6 GitHub issues simultaneously) is a multiplier.

## Potential Alternatives
- GSD (Get Shit Done) plugin — phase-based orchestration, more opinionated
- BMAD Method — multi-agent SDLC framework
- Custom harness scripts (shell scripts chaining Claude Code sessions)
- Anthropic's agent teams (native, but experimental and expensive)

## Additional Implementation Details (from live stream)
- **Context persistence parameter**: each node can be set to `continue` (extend prior node's session) or `fresh` (new session reading only the artifact). Fresh sessions prevent planning bias — planning node writes to `artifact_dir`, implementation node reads from it.
- **Adapters**: CLI (invoked from Claude Code/Codex), web UI (mission control dashboard with live log streaming), Slack, GitHub (comment `@archon` on an issue), Telegram. All adapters support parallel execution.
- **Installation**: clone repo → open Claude Code in the Archon directory → say "setup Archon" → the Archon skill self-configures (installs bun, registers repos, configures credentials in a separate terminal to avoid API key exposure in the LLM session).
- **Skill deployment**: copy `.claude/skills/archon/` into any target codebase so Claude Code can invoke Archon workflows from that codebase's context without opening the Archon repo.
- **Database**: SQLite (default) or Postgres. Stores registered projects, conversations, workflow execution history.
- **Default workflows shipped**: fix GitHub issue (most-used), interactive PRD, plan-to-PR (PIV loop), Ralph loop, validate PR, adversarial dev, workflow builder (meta: build new workflows).
- **Token efficiency**: four parallel GitHub issue fix + validate PR workflows used ~20% of 5-hour Claude subscription limit (Sonnet default, Opus for implementation nodes only).
- **Provider model aliasing via environment variables**: Archon workflow YAML specifies model names (`opus`, `sonnet`, `haiku`). To run workflows on a non-Anthropic provider, set environment variables that remap these names to alternative model IDs (e.g., `ANTHROPIC_MODEL_OPUS=minimax-m2.7`, `ANTHROPIC_BASE_URL=https://api.minimax.io/v1`). This allows all existing workflow YAMLs to run unchanged on MiniMax, GLM 5.1, Qwen, or any OpenAI-compatible provider. Useful for high-volume autonomous pipelines where Claude subscription rate limits are a constraint.
- **VPS deployment for autonomous pipelines**: For dark factory use (public-facing, autonomous, always-on), Archon runs on a VPS rather than a developer's local machine. A cron job (orchestrator shell script) triggers on schedule, reads GitHub issue labels, and dispatches Archon workflows via CLI. VPS avoids Anthropic TOS issues with running workflows triggered by external users.
- **Triage workflow node design (5 nodes)**: (1) Fetch untriaged issues (deterministic GitHub CLI), (2) Fetch factory rules/mission files (deterministic read), (3) Fetch open PRs (deterministic GitHub CLI, optional — helps detect in-flight duplicates), (4) Classify issues against mission (agentic, LLM decision, uses Sonnet-tier model for nuance), (5) Apply labels and comments (deterministic — separates the "decide" step from the "act" step). Batch cap: 10 issues per cycle.

## Potential Improvements
- Visual workflow builder (N8N-like interface — explicitly on the Archon roadmap)
- Cross-workflow state sharing for dependent tasks
- Auto-workflow generation from git history patterns
- Model override via CLI flag (not yet supported — must edit YAML or ask agent to temporarily change it)
- Sub-workflow execution (nesting workflows — requested but not yet built)

## Potential Failure Modes
- Token cost amplification — each node is a full session, complex workflows burn many tokens
- Workflow rigidity — YAML-defined steps may not adapt well to unexpected intermediate states
- Model mismatch — using Haiku for a node that needs Sonnet-level reasoning silently degrades output
- Workflow iteration required — first-run workflows often have minor issues (missing artifact paths in human-gate messages, research gaps not propagated) that require a few debug cycles
