---
name: Tiered Context Injection over Monolithic Files
summary: Instead of loading one large CLAUDE.md/AGENTS.md into every interaction, categorize instructions by operation type (coding, testing, reviewing, deploying) and inject only the relevant subset per
  task. ETH Zurich data shows 60-80% context reduction while maintaining or improving accuracy. This is the structural fix for instruction bloat.
implementation_notes: 'MetaSystem already has some structure (CLAUDE.md per system, skills with own SKILL.md). Next step: audit which instructions in each CLAUDE.md are operation-specific vs always-relevant.
  Move operation-specific rules to scoped files or skill definitions. Claude Code''s rule scoping features and Cursor''s per-file-type rules are early implementations of this pattern.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- eth-zurich-context-files-paper-march-2026.md
related_findings:
- file: pointers-over-copies-in-context-files.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: claudemd-context-rot-from-indiscriminate-rule-accu.md
  rel: same-problem
- file: claudemd-minimum-viable-rule-only-add-globally.md
  rel: same-problem
- file: ace-delta-updates-over-monolithic-rewrites.md
  rel: same-problem
- file: document-sharding-for-context-efficiency.md
  rel: same-problem
- file: new-chat-per-agent-step-context-hygiene.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: context-file-instruction-bloat-eth-zurich.md
  rel: enabled-by
- file: context-file-taxonomy-claudemd-soulmd-agentsmd.md
  rel: enabled-by
- file: claudemd-as-signal-to-noise-problem-not-size-probl.md
  rel: same-problem
- file: context-aware-routing-skill-classifier-sub-skill.md
  rel: same-problem
- file: step-file-micro-architecture.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---
## What It Is

A structural alternative to monolithic context files, recommended by the ETH Zurich study and practitioner community. Instead of one file loaded into every agent interaction, instructions are categorized into tiers based on operation type:

- **Always-on (Tier 0)**: Identity, safety constraints, hard rules (< 20 lines)
- **Task-scoped (Tier 1)**: Coding conventions when coding, test patterns when testing, review criteria when reviewing
- **On-demand (Tier 2)**: Architecture overviews, dependency docs, retrieved only when the agent signals need

The ETH Zurich study showed that task-relevant instruction subsets reduce context by 60-80% while maintaining or improving accuracy compared to monolithic file loading.

## Why It Matters

Monolithic context files impose a worst-case cost increase of up to 159% per session (larger files, more API calls). The cost scales linearly with file size and call count. Tiered injection eliminates this tax for instructions irrelevant to the current operation.

Early implementations are already shipping: Claude Code performs partial context management by analyzing which portions of CLAUDE.md are relevant. Cursor has introduced rule scoping by file type. GitHub Copilot experiments with instruction weighting. The industry trajectory points toward "structured instruction registries" replacing flat markdown files within 12-18 months.

## Why People Are Using It

The ETH Zurich data provides the empirical justification. The cost savings alone (20%+ reduction in inference cost) are compelling. For enterprise deployments running agents at scale, a 20% inference premium on every task is a material line item.

## Potential Improvements

Automatic tier classification: analyze an instruction's impact on task completion across a history of agent runs, then auto-assign it to the appropriate tier. Instructions that never improve outcomes get demoted or removed.

## Potential Failure Modes

Tier misclassification can hide critical instructions from tasks that need them. The routing logic itself consumes tokens and adds latency. Requires tooling support -- manual tiering is maintenance-heavy and will drift.
