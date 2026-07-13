---
notion_id: 32b1e08b-9b34-81f6-a744-c7f9a4aabaf5
name: 'Superpowers Plugin: Spec-Driven Sub-Agent Orchestration'
summary: The Superpowers Claude Code plugin implements a three-phase development workflow (brainstorm -> write plan -> execute plan) that automatically dispatches sub-agents for implementation, code review,
  and testing -- shifting from vibe coding to spec-driven development.
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-code-plus-superpowers-tutorial.md
- claude-code-works-better-when-you-do-this.md
- how-to-make-claude-code-less-dumb.md
- obra-superpowers-agentic-skills-framework-dev-meth.md
- these-3-frameworks-make-claude-code-unstoppable.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-07-13'
related_findings:
- file: agent-architecture-layer-impermanence.md
  rel: contradicts
- file: agent-management-tool-landscape-2026.md
  rel: same-problem
- file: archon-yaml-defined-harness-workflows.md
  rel: same-problem
- file: skill-phase-pipeline-shared-session-orchestrator.md
  rel: enables
- file: review-triggered-remediation-dispatch.md
  rel: enables
- file: execution-topology-as-runtime-selection.md
  rel: enables
- file: html-mockup-generation-as-brainstorm-artifact.md
  rel: enables
- file: external-ticket-as-brainstorm-seed.md
  rel: enables
- file: tdd-step-ordering-in-plan-tasks.md
  rel: enables
- file: file-mediated-subagent-handoff-workspace.md
  rel: extended-by
- file: unified-dual-verdict-reviewer.md
  rel: extended-by
- file: controller-deauthorization-reviewer-independence.md
  rel: enables
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
---
# Superpowers Plugin: Spec-Driven Sub-Agent Orchestration

> **Upstream supersession note (added 2026-07-13).** Superpowers v6.0.0 (released 2026-06-16) replaced the two-stage review architecture this finding describes. The two sequential per-task reviewers (spec-compliance reviewer, then code-quality reviewer) were collapsed into a **single unified task reviewer** that reads the task's diff once and returns both verdicts (spec compliance + code quality) in one pass, with a new "cannot verify from diff" verdict routed back to the controller. Per-task review became a narrow task-scoped gate, with one **whole-branch review at the end** on the most capable model. Handoffs became file-mediated: task briefs, implementer reports, and review diffs move as files in a self-ignoring `.superpowers/sdd/` workspace (v6.0.3) instead of pasted text. Plans now carry a Global Constraints block and per-task Interfaces blocks; every dispatch must name its model explicitly; reviews are read-only and the controller may not suppress or pre-rate findings. Upstream evals: similar quality, ~2x faster, ~50% fewer tokens vs the v5.x flow. The workflow description below (two-stage review, v5.0.7-era details, star counts) is preserved as a historical record of the v5 architecture. Current structure: `watched-libraries/analysis/superpowers-analysis.md` (v6.1.1, 2026-07-13); registry delta: `watched-libraries/superpowers.md` §Upstream Delta.

## What It Is
Superpowers is a composable skills framework and software development methodology for coding agents (120k GitHub stars, 9.7k forks). It enforces a seven-step workflow: (1) brainstorming with hard-gate preventing code before approval; (2) git worktrees; (3) writing plans with 2-5 min chunks; (4) subagent-driven development with two-stage review; (5) RED-GREEN-REFACTOR TDD; (6) code review; (7) branch finishing.

## Why It Matters
Ad hoc "vibe coding" with a single agent leads to context rot, inconsistent architecture, and lack of documentation. Superpowers forces spec-first discipline through a hard gate that blocks ALL implementation until design is approved.

## Why People Are Using It
Officially endorsed by Anthropic. 120k GitHub stars. Multi-platform support (Claude Code, Cursor, Codex, OpenCode, Gemini CLI). Eric Tech provides a full tutorial demonstrating 14 enforced skills, 7-phase workflow, TDD enforcement (deletes pre-test code), subagent per task, two-stage review, and a demo building a Google Keep clone. v5.0.7 as of March 2026.

## Potential Alternatives
TACHES create-plans skill, manual spec writing, Cursor's composer mode, custom CLAUDE.md workflows.

### Mega-Orchestrator Concept (2026-04-07)

New evidence clarifies Superpowers' orchestration model as a **mega-orchestrator**: a single persistent Claude Code conversation that stays alive throughout the entire project and spins up sub-agents for each phase (brainstorm, plan, execute). The orchestrator never resets -- it maintains full session continuity.

**Tension with GSD:** This mega-orchestrator model directly conflicts with GSD's fresh-session model, which resets context at phase boundaries to stay under the 50% context window threshold. Superpowers prioritizes continuity; GSD prioritizes freshness. These two frameworks have fundamentally different orchestrator models and may require reconciliation before combining them. Practitioners have not yet documented a resolution to this tension.

**Execution and planning details (2026-04-07):** Two execution modes: (a) sub-agent per task with human review between tasks, (b) inline/batch with checkpoints in the same session. HTML mockup generation: the brainstorm skill generates HTML pages served on localhost for visual comparison of UI options. Jira ticket as brainstorm input: paste a ticket URL and Superpowers reads scope, UX requirements, and edge cases. 3-level plan hierarchy: tasks (e.g., 11) -> steps within tasks -> checkboxes per step. Commit-per-step: auto-commits after each TDD step passes. Code reviewer dispatches fix agents: review identifies critical/important issues, then spawns remediation sub-agents. Spec output goes to docs/ folder (both brainstorm spec and implementation plan).

## Potential Improvements
Visual companion for brainstorming is still new and token-intensive. Integration with project management tools.

## Potential Failure Modes
Quality depends heavily on spec generated in brainstorming. Human review of plans is essential but easy to skip. The hard gate may frustrate experienced developers on trivial changes.
