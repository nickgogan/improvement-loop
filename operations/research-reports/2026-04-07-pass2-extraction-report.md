---
name: Pass 2 Video Transcript Extraction Report
date: "2026-04-07"
type: delta-report
---

# Pass 2 Video Transcript Extraction Report -- 2026-04-07

## Summary

| Metric | Value |
|--------|-------|
| Videos processed | 6 |
| New findings created | 21 |
| Existing findings to update | 15 |
| KB total (before) | 284 |
| KB total (after) | 305 |

## Per-Video Results

### Video 4: "Stop Using Claude Code in Terminal" (Simon Scrapes) -- 85.7% miss rate
| Outcome | Count |
|---------|-------|
| New findings | 2 |
| Updates to existing | 2 |

**New findings:**
1. `scheduled-task-dashboard-observability-layer.md` -- Orchestration, P3
2. `agent-management-tool-landscape-2026.md` -- Orchestration, P3

**Updates recommended:**
- `goal-first-agent-management-abstraction.md` -- Add last-two-messages summary view, output gallery, memory continuity
- `human-on-the-loop-hotl-autonomy-tiering-framework.md` -- Add per-task permission selection evidence

**Misattribution resolved:** `ide-first-claude-code-with-deterministic-hooks.md` is correctly sourced to Nate B Jones, NOT this video. No KB correction needed.

**Calibration reassessment:** Original 12 missed patterns reduced to 2 net-new findings. The video is a product demo of one tool built on one thesis (goal-first > session-first). Most "patterns" are features of that tool, not separable generalizable findings.

---

### Video 13: "Agent Produces at 100x, Org Reviews at 3x" (Nate B Jones) -- 68.8% miss rate
| Outcome | Count |
|---------|-------|
| New findings | 5 |
| Updates to existing | 5 |

**New findings:**
1. `review-bandwidth-as-organizational-bottleneck.md` -- Governance, P1
2. `trust-calibration-progressive-autonomy-ramp.md` -- Governance, P2
3. `compound-review-debt-from-deferred-inspection.md` -- Governance, P2
4. `reviewer-skill-elevation-for-agentic-output.md` -- Governance, P2
5. `staged-delivery-for-review-digestibility.md` -- Orchestration, P2

**Updates recommended:** 5 existing findings should be updated with new details from transcript.

---

### Video 2: "Claude Code's Leak Changes Everything" (Agentic Lab) -- 53.3% miss rate
| Outcome | Count |
|---------|-------|
| New findings | 4 |
| Updates to existing | 5 |

**New findings:**
1. `context-pollution-same-window-verification-bias.md` -- Evaluation, P1
2. `llm-as-judge-pattern-for-verification-agents.md` -- Evaluation, P2
3. `post-session-hooks-autonomous-version-control.md` -- Tool Integration, P2
4. `ide-context-streaming-silent-token-tax.md` -- Context Engineering, P2

**Updates recommended:** 5 existing findings should be updated with new details from transcript.

---

### Video 11: "Anthropic Just Dropped Ultra Plan" (Ray Amjad) -- 47.1% miss rate
| Outcome | Count |
|---------|-------|
| New findings | 2 |
| Updates to existing | 1 |

**New findings:**
1. `cloud-plan-parallel-multitasking-pattern.md` -- Orchestration, P3
2. `cloud-local-plan-handoff-teleport-pattern.md` -- Orchestration, P2

**Updates recommended:**
- `claude-code-ultra-plan-three-mode-planning.md` -- Add blast-radius task heuristic, binary readable strings discovery

---

### Video 7: "Claude Code + RAG-Anything = LIMITLESS" (Chase AI) -- 44.4% miss rate
| Outcome | Count |
|---------|-------|
| New findings | 5 |
| Updates to existing | 2 |

**New findings:**
1. `scalpel-local-parse-then-llm-cost-optimization.md` -- Memory Architecture, P2
2. `knowledge-graph-merge-by-entity-matching.md` -- Memory Architecture, P3
3. `oneshot-infrastructure-setup-prompt-pattern.md` -- Prompt Craft, P2
4. `skill-as-script-wrapper-for-complex-pipelines.md` -- Tool Integration, P2
5. `architecture-literacy-as-ai-dev-differentiator.md` -- Agent Design, P3

**Updates recommended:**
- `rag-anything-multimodal-document-processing.md` -- Add GPT-5.4 nano model, Ollama local substitution
- `mineru-local-document-parsing-for-rag.md` -- Add LaTeX equation handling detail

---

### Video 5: "Karpathy's Obsidian RAG + Claude Code" (Chase AI) -- 38.5% miss rate
| Outcome | Count |
|---------|-------|
| New findings | 3 |
| Updates to existing | 2 |

**New findings:**
1. `dual-ingestion-funnel-human-clip-plus-llm-research.md` -- Memory Architecture, P2
2. `obsidian-as-transparent-frontend-vs-rag-black-box.md` -- Memory Architecture, P3
3. `start-simple-migrate-when-forced-pragmatic-architecture.md` -- Agent Design, P3

**Updates recommended:**
- `karpathy-llm-knowledge-base-obsidian-rag.md` -- Add Claude bypass of raw/ folder
- `claudemd-as-knowledge-base-traversal-guide.md` -- Add structural consistency instruction detail

---

## Priority Distribution of New Findings

| Priority | Count |
|----------|-------|
| P1 (Implement Now) | 2 |
| P2 (Design Required) | 12 |
| P3 (Monitor) | 7 |

## Category Distribution of New Findings

| Category | Count |
|----------|-------|
| Orchestration | 6 |
| Governance | 4 |
| Memory Architecture | 4 |
| Evaluation | 2 |
| Tool Integration | 2 |
| Agent Design | 2 |
| Prompt Craft | 1 |
| Context Engineering | 1 |

## Deferred Work

- **15 existing finding updates** identified but not yet executed. These are enrichments (adding transcript-derived details to existing findings), not corrections. Can be batched in a future session.
- **Finding cross-links** for the 21 new findings. Run `/finding-crosslink` in a future session.
- **_index.md updates** for findings directory. Deferred per governance rules (optional, not blocking).
