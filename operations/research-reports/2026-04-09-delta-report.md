# Delta Report — 2026-04-09 (Session 15)

## Scan Summary
- **Type:** URL batch processing (Pass 2 transcript-based deep extraction)
- **Sources provided:** 13 URLs (1 duplicate removed → 12 unique videos)
- **Already in KB:** 3 (FtCdYhspm7w, 7huCP6RkcY4, OSZdFnQmgRw — all status: Done)
- **New sources created:** 9
- **New findings created:** 13
- **Existing findings updated:** 1 (Hybrid Retrieval Pattern)
- **Authorities updated:** 3 (Nate B Jones, Cole Medin, Chase AI)
- **Previous report:** 2026-04-08-crosslink-targeted-report.md
- **KB state after:** 382 findings, 85 sources

## New Sources Created

| Filename | Title | Channel | Relevance |
|----------|-------|---------|-----------|
| five-agentic-patterns-claude-code.md | 5 Agentic Patterns for Claude Code | Unknown | High |
| caveman-brevity-constraints-llm-performance.md | Caveman Claude — Brevity Constraints | Chase AI | Medium |
| claude-code-architecture-under-the-hood.md | Claude Code Architecture Under the Hood | Unknown | High |
| anthropic-managed-agents-platform.md | Anthropic Managed Agents Platform | Unknown | High |
| sdk-vs-framework-decision-ai-agents.md | SDK vs Framework Decision | Cole Medin | High |
| archon-open-source-harness-builder.md | Archon: Open-Source Harness Builder | Cole Medin | High |
| conway-anthropics-always-on-agent.md | Conway — Always-On Persistent Agent | Nate B Jones | High |
| claude-code-ultra-review-bug-hunter.md | Ultra Review Bug Hunter Fleet | Unknown | High |
| anthropic-advisor-strategy-api.md | Advisor Strategy API | Chase AI | High |

## New Findings

| Filename | Category | Evidence | Priority |
|----------|----------|----------|----------|
| brevity-constraints-reverse-llm-performance.md | Prompt Craft | Medium | P2 |
| worktree-isolation-for-parallel-agent-sessions.md | Orchestration | Strong | P1 |
| builder-validator-chain-pattern.md | Evaluation | Medium | — |
| anthropic-managed-agents-platform.md | Tool Integration | Strong | P2 |
| sdk-vs-framework-decision-for-agent-building.md | Tool Integration | Medium | P2 |
| archon-yaml-defined-harness-workflows.md | Orchestration | Medium | P2 |
| harness-engineering-third-evolution.md | Orchestration | Medium | — |
| conway-always-on-persistent-agent.md | Agent Design | Medium | P2 |
| behavioral-context-portability-intelligence-lock-in.md | Governance | Medium | P2 |
| proprietary-extension-layer-on-open-protocol.md | Tool Integration | Medium | P3 |
| ultra-review-multi-agent-bug-hunting-fleet.md | Evaluation | Strong | P1 |
| cross-model-verification-for-bug-finding.md | Evaluation | Medium | P2 |
| advisor-executor-api-pattern.md | Model Selection | Strong | P1 |

## Updated Findings

| Filename | What Changed |
|----------|--------------|
| hybrid-retrieval-pattern-semantic-lexical-graph.md | Added agentic RAG evidence from SDK vs Framework video; LlamaIndex study confirming file search > RAG for small corpora |

## Already Captured (corroboration)

These patterns from the new videos were already in the KB — the new sources provide independent corroboration:

- **Agent Teams** (from 5 Patterns video) → `agent-teams-shared-communication-channel.md` already exists
- **Headless mode / -p flag** (from 5 Patterns video) → `claude-p-headless-mode-as-openclaw-replacement.md` already exists
- **Ralph Loop** (from 5 Patterns + Archon videos) → `ralph-wiggum-execution-pattern.md` already exists
- **Tool Registry** (from Architecture video) → `tool-registry-with-metadata-first-design.md` already exists
- **Session Persistence** (from Architecture video) → `session-persistence-as-recoverable-state.md` already exists
- **Memory Compaction** (from Architecture video) → `dynamic-tool-pool-assembly-and-transcript-compaction.md` already exists
- **Hooks** (from Architecture video) → `ide-first-claude-code-with-deterministic-hooks.md` already exists
- **Karpathy LLM KB** (from both Karpathy videos) → `karpathy-llm-knowledge-base-obsidian-rag-alternative.md` already exists
- **Index-File Navigation** (from Karpathy videos) → `index-file-navigation-as-rag-replacement.md` already exists
- **Specialized Harness Engineering** (from Archon video) → `specialized-harness-engineering-deterministic-rails.md` already exists
- **Model Tier Routing** (from Advisor video) → `model-tier-routing-expensive-orchestrator-cheap-sub-agents.md` already exists

## Key Themes Across This Batch

1. **Harness engineering is maturing rapidly.** Archon (open-source harness builder), Stripe Minion (1,300 AI PRs/week), and the Claude Code leak (40% harness code) all converge on the same insight: orchestrating multiple agent sessions is the unlock, not improving single-session performance.

2. **Verification is the new frontier for evaluation.** Ultra Review's find→verify→dedup pipeline, cross-model verification (Claude + Codex), and the builder-validator chain all point toward independent verification as the critical quality differentiator.

3. **Platform persistence race is underway.** Conway, behavioral context portability, and proprietary extension layers signal that the competition is shifting from "best model" to "most sticky persistent agent layer." All three labs are converging on this.

4. **Brevity as a quality lever, not just a cost lever.** The research paper on verbosity-induced errors suggests that making models more concise doesn't just save tokens — it can improve correctness on certain problem types.

5. **SDK vs Framework bifurcation.** The ecosystem is splitting: SDKs for personal/prototype use, frameworks for production/multi-user deployment. The subscription ToS boundary is the hidden forcing function.

## Recommendations

### Priority 1 (High Impact, Low Effort)
- **Advisor-Executor pattern** — direct API feature, better results at lower cost
- **Worktree isolation** — already available in Claude Code, just needs adoption
- **Brevity constraints** — single line in CLAUDE.md could improve output quality

### Priority 2 (High Impact, Higher Effort)
- **Ultra Review verification pipeline** — adapt find→verify→dedup pattern for our own review workflows
- **Archon-style harness workflows** — evaluate for MetaSystem build pipeline
- **Behavioral context portability** — design a portable behavioral audit before lock-in solidifies

### Priority 3 (Monitor)
- **Conway launch** — will reshape the agent landscape; monitor for release
- **Proprietary extension ecosystems** — watch for MCP fragmentation across platforms
- **Managed Agents platform** — evaluate when visual workflow builder ships

## Dimension Gaps

No new dimensions needed. All findings fit existing dimensions. The Conway/behavioral context findings span Agent Design + Governance, which is expected for platform-level patterns.

## Next Scan Notes

- **Archon development** — monitor releases, especially visual workflow builder
- **Conway launch timing** — Anthropic has not announced this; watch for product announcements
- **Brevity constraints on frontier models** — the study used open-weight models; watch for replication on Claude/GPT
- **Stripe Minion details** — look for deeper technical breakdown of their harness architecture
- **Ultra Review general availability** — currently behind feature flag with 3 free uses
