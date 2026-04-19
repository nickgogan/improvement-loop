---
name: Claude Code 12 Agent Primitives (Three-Tier Architecture)
summary: 'The Claude Code source leak reveals 12 foundational primitives in three tiers that enable production-scale agent systems: Tier 1 (tools/permissions — tool registry, permission tiers, security),
  Tier 2 (persistence/execution — session state, budget tracking, execution counts), Tier 3 (observability/verification — event logging, multi-layer verification, failure recovery). Agents are 80% infrastructure,
  20% model.'
implementation_notes: 'MetaSystem has partial coverage: tool registry (skills), permission system (governance rules), session persistence (PROGRESS.md). Missing: budget tracking, structured event logging,
  multi-layer verification, failure recovery.'
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropics-2-5-billion-leak-12-critical-pieces.md
- claude-codes-leak-changes-everything.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: tiered-permission-system-bash-safety.md
  rel: extends
- file: tool-registry-metadata-first-design.md
  rel: extends
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
---
# Claude Code 12 Agent Primitives (Three-Tier Architecture)

## What It Is
12 primitives extracted from Anthropic's leaked Claude Code source (512K lines TypeScript), organized in three tiers. Tier 1 (Tools & Permissions): tool registry with metadata-first design, permission system with trust tiers (18 modules for bash alone), session persistence surviving crashes. Tier 2 (Persistence & Execution): budget tracking, execution counts, routing decisions. Tier 3 (Observability & Verification): structured event logging, multi-layer verification, failure recovery with provable rollback.

Individual primitives are now documented as standalone findings in this KB: tool-registry-metadata-first-design.md (registry with 207 user-facing + 184 model-facing entries), tiered-permission-system-bash-safety.md (18-module bash security), session-persistence-crash-resilient.md (JSON persistence with load/reconstruct/restore), workflow-state-vs-conversation-state.md (planned → awaiting_approval → executing → waiting_on_external), token-budget-pre-turn-projection.md, structured-streaming-events-observability.md, system-event-logging-actions-not-words.md, agent-type-system-six-roles.md (Explore, Plan, Verify, Guide, General Purpose, Status Line Setup), dynamic-tool-pool-assembly-transcript-compaction.md.

## Why It Matters
Proves production agents need infrastructure discipline. Most teams build the model layer and skip the plumbing — Claude Code invests 80% in infrastructure. This inverts the common assumption that agent quality comes primarily from better prompts or smarter models.

## Why People Are Using It
Anthropic's own production system serving millions of users. Multiple analysts (Nate B Jones, Agentic Lab, Latent Space) independently validated the architecture. The three-tier model provides a concrete checklist for evaluating agent system maturity.

The Agentic Lab transcript reinforces the "80% infrastructure" thesis by walking through concrete primitives: context injection (date + git status on every turn), five compaction strategies (mostly feature-flagged), file read deduplication (18% duplicate reads, one-line stub returns), a verification agent with read-only permissions, and fork_subagent for parallel trajectory exploration. The overall characterization is that Claude Code is "not just a thin wrapper" but "a deeply engineered multi-model system" -- each primitive discovered in the leak maps to infrastructure, not model capability.

## Potential Alternatives
Lighter-weight approaches (GSD, Superpowers) implement subsets of these primitives. Custom agent frameworks can cherry-pick relevant tiers based on project scale.

## Potential Improvements
The primitives could become a standard checklist for agent system design. A maturity model mapping which primitives are needed at which scale would help teams avoid over-engineering.

## Potential Failure Modes
Over-engineering small projects with all 12 primitives. The leak context means some primitives may be internal-only patterns not suited for external use. Cargo-culting infrastructure without understanding the constraints that motivated each primitive.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[three-tier-agent-primitive-architecture]] in `extracts/patterns/`
