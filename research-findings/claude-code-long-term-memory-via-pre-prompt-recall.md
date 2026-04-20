---
notion_id: 3351e08b-9b34-819d-b639-fd7e8759973f
name: Claude Code long-term memory via pre-prompt recall + periodic post-turn retention windows
summary: Augment Claude Code's static project memory (e.g., CLAUDE.md) with a long-term conversational memory layer that (1) injects retrieved memories before each prompt and (2) periodically retains recent
  conversation windows as structured facts, using tunable cadence and recall budgets to control cost/latency.
implementation_notes: 'Pattern: add a memory plugin/hook that queries a memory store (semantic) before every prompt and injects top relevant facts into context; after responses, retain every N turns with
  overlap to extract structured decisions/preferences/context. Tune retainEveryNTurns/retainOverlapTurns for cost vs coverage; tune recallBudget/recallMaxTokens for latency/token budget. Add safety: avoid
  permission-bypass modes for remote channels.'
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- openclaude-build-a-claude-code-agent-with-long-ter.md
proposals: []
date_discovered: '2026-04-01'
last_updated: '2026-04-20'
related_findings:
- file: structured-fact-extraction-from-conversations.md
  rel: enables
- file: memory-cross-layer-promotion-governance.md
  rel: enables
- file: gsd-global-learnings-store-cross-session-persistence.md
  rel: same-problem
- file: agent-memory-architecture-multi-agent-layered.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
- file: memory-bank-isolation-per-agent-per-project.md
  rel: same-problem
- file: signal-capture-as-byproduct-of-work.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- session-persistence-and-memory.md
---
# Claude Code long-term memory via pre-prompt recall + periodic post-turn retention windows

Pattern details:
- Pre-prompt: semantic recall from memory store; inject into model context.
- Post-turn: retain conversation chunks every N turns with overlap, extracting discrete facts.
- Suggested knobs: retainEveryNTurns=10, retainOverlapTurns=2, recallBudget (low/mid/high), recallMaxTokens.
- Operational cautions: recall timeouts/latency; ensure at least one retain cycle before recall yields value; plugin requires active session; remote interfaces may hide permission prompts.

Source: https://hindsight.vectorize.io/blog/2026/03/23/claude-code-telegram
