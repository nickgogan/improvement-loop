---
name: 'Agent Context KISS Commandments: Five Rules for Minimum Viable Agent Context'
summary: 'Five commandments for agent token efficiency: (1) index references instead of dumping full docs, (2) pre-process context for consumption not reading, (3) cache all stable context at 90% discount,
  (4) scope each agent to minimum needed context, (5) instrument and measure per-call token cost.'
implementation_notes: Directly applicable to MetaSystem's sub-agent architecture. Rule 4 (scope each agent's context) maps to the Sub-Agent Context Isolation finding. Rule 2 (pre-process context) is an
  argument for pre-summarized reference docs in agent context files.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- your-claude-limit-burns-in-90-minutes.md
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: ai-readable-naming-conventions-as-a-navigation.md
  rel: same-problem
- file: bmad-outcome-based-skill-rewrite-pattern.md
  rel: same-problem
- file: bmad-v6-diataxis-documentation-and-llms-txt.md
  rel: same-problem
- file: catastrophic-context-collapse-risk-during-claudemd.md
  rel: same-problem
- file: claudemd-as-knowledge-base-traversal-guide.md
  rel: same-problem
- file: claudemd-context-rot-from-indiscriminate-rule-accu.md
  rel: same-problem
- file: claudemd-minimum-viable-rule-only-add-globally.md
  rel: same-problem
- file: context-as-tree-mental-model-with-trunk-and.md
  rel: same-problem
- file: context-bracket-auto-adaptation.md
  rel: same-problem
- file: context-curation-over-context-stuffing.md
  rel: same-problem
- file: context-file-instruction-bloat-eth-zurich.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: context-usage-status-line-visual-budget-tracking.md
  rel: same-problem
- file: document-sharding-for-context-efficiency.md
  rel: same-problem
- file: dynamic-tool-pool-assembly-transcript-compaction.md
  rel: same-problem
- file: file-read-deduplication-pattern.md
  rel: same-problem
- file: first-principles-context-management-taxonomy.md
  rel: same-problem
- file: five-context-management-techniques-in-claude-code.md
  rel: same-problem
- file: git-status-context-injection-token-hygiene.md
  rel: same-problem
- file: global-vs-project-level-skill-and-context.md
  rel: same-problem
- file: ide-context-streaming-silent-token-tax.md
  rel: same-problem
- file: index-file-navigation-as-rag-replacement.md
  rel: same-problem
- file: llms-full-txt-ai-optimized-documentation.md
  rel: same-problem
- file: micro-compact-stale-tool-call-removal.md
  rel: same-problem
- file: new-chat-per-agent-step-context-hygiene.md
  rel: same-problem
- file: notebooklm-as-external-knowledge-base-for-context.md
  rel: same-problem
- file: pointers-over-copies-in-context-files.md
  rel: extends
- file: reasoning-token-overhead-from-context-files.md
  rel: same-problem
- file: rlm-pattern-external-prompt-environment-with-dyna.md
  rel: same-problem
- file: scrum-master-story-contextualization.md
  rel: same-problem
- file: stupid-button-six-question-token-audit-diagnostic.md
  rel: same-problem
- file: subagent-exploration-mode-parallel-codebase-mappi.md
  rel: same-problem
- file: task-to-file-routing-table-in-context-files.md
  rel: same-problem
- file: three-layer-folder-as-workspace-architecture.md
  rel: same-problem
- file: three-tier-vault-architecture-global-shared-local.md
  rel: same-problem
- file: tiered-context-injection-over-monolithic-files.md
  rel: same-problem
- file: token-waste-taxonomy-and-two-mode-workflow.md
  rel: same-problem
pipeline_status: "synthesized"
consumed_by:
  - "managing-agent-context.md"
---

## What It Is

Five commandments from Nate B Jones for managing token efficiency in agent systems specifically (as opposed to human chat sessions). Called the "KISS commandments for agents" because agents burn hundreds of millions of tokens in some deployments:

1. **Index your references.** If an agent gets raw documents instead of relevant chunks, "you've already failed." Retrieval should scope what the model sees to what it needs. Do not dump a full document set into the window on every agent call.

2. **Prepare context for consumption.** Pre-process, pre-summarize, pre-chunk reference material. "A reference document should arrive in an agent's context ready to be used, not ready to be read or processed." If the model's first several thousand tokens of reasoning are spent dealing with raw input, you are not building responsibly.

3. **Cache stable context.** System prompts, tool definitions, persona instructions, reference material -- anything stable should be cached. Cache hits on Opus cost $0.50/M vs $5/M standard (90% discount). "Lowest effort, highest impact optimization." If you are making thousands of agent calls a day without caching, "it's just pouring money down the drain."

4. **Scope every agent's context to the minimum it needs.** A planning agent does not need the full codebase. An editing agent does not need the project roadmap. "Passing everything to every agent is architectural laziness." Models perform worse when drowning in irrelevant context. If agents need to find context dynamically, give them a searchable, pre-processed repo -- not the entire knowledge base.

5. **Measure what you burn.** Instrument agent calls. Track input tokens, output tokens, model mix, and cost ratio. "You cannot improve what you do not measure." Most teams optimize for semantic correctness, not functional correctness, and ignore model cost because it does not make or break the project today. But plan for more expensive models.

## Why It Matters

These five rules are agent-specific extensions of the broader Token Waste Taxonomy. While that finding addresses human chat habits, these commandments address system architecture -- how agent pipelines are designed, not how humans chat. The distinction matters because agent token waste scales multiplicatively (thousands of calls per day) while human chat waste scales linearly (sessions per day).

Jones frames this in terms of upcoming model pricing: if Mythos costs $50/$250 per million tokens (10x Opus), the 8-10x reduction from clean practices becomes the difference between viable and unviable agent deployments. "Your mistakes scale with the price of intelligence."

## Why People Are Using It

Advanced users running agentic systems are the highest-leverage target for token optimization. Their mistakes are "the most expensive ones" because they operate at hundreds of thousands or millions of tokens per project. The five commandments provide a structured checklist that can be applied to any agent pipeline.

## Potential Improvements

MetaSystem could implement commandment 1 (index references) via the existing index-file pattern. Commandment 2 (pre-process context) could be automated as a pre-hook on agent context loading. Commandment 5 (measure) is currently unimplemented -- adding per-skill token instrumentation would be a direct implementation.

## Potential Failure Modes

Aggressive context scoping (commandment 4) can starve agents of context they actually need, leading to incorrect outputs. The tension between "minimum viable context" and "sufficient context for correct operation" requires calibration per task type. Over-indexing on token cost could lead teams to use cheaper models where quality models are genuinely needed.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[minimum-viable-agent-context]] in `extracts/patterns/`
