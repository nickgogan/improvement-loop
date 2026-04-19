---
name: Upstream Library Finding Extraction Report
date: "2026-04-07"
type: delta-report
---

# Upstream Library Finding Extraction Report -- 2026-04-07

## Summary

| Metric | Value |
|--------|-------|
| Libraries processed | 3 |
| Source entries created | 3 |
| New findings created | 13 |
| Existing findings updated (upstream) | 3 |
| Existing findings updated (Pass 2 deferred) | 17 |
| New crosslinks written | 42 |
| KB total findings (before) | 305 |
| KB total findings (after) | 318 |
| KB total sources (before) | 73 |
| KB total sources (after) | 76 |
| KB total crosslinks (before) | 155 |
| KB total crosslinks (after) | 197 |

## Goal 1: Upstream Extraction

### GSD v1.33.0 → v1.34.2 (6 new findings)

| Finding | Category | Priority |
|---------|----------|----------|
| gsd-global-learnings-store-cross-session-persistence | Context Engineering | P2 |
| gsd-queryable-codebase-intelligence-store | Tool Integration | P2 |
| gsd-gates-taxonomy-four-canonical-types | Evaluation | P2 |
| gsd-execution-context-profiles-mode-switching | Agent Design | P2 |
| gsd-stall-detection-revision-loop-escalation | Orchestration | P2 |
| gsd-prompt-injection-scanner-hardening | Sandboxing | P2 |

Source: `gsd-v1340-v1342-changelog.md`

### BMAD Method v6.1.0 → v6.2.2 (3 new + 1 update)

| Finding | Category | Priority |
|---------|----------|----------|
| bmad-outcome-based-skill-rewrite-pattern | Prompt Craft | P2 |
| bmad-dependency-graph-module-ordering | Orchestration | P3 |
| bmad-deterministic-skill-validator | Evaluation | P2 |
| skills-as-markdown-sop-files-encode-processes (updated) | Prompt Craft | -- |

Source: `bmad-v610-v622-changelog.md`

Update: Added BMAD v6.1.0 full-framework migration evidence (68 workflows converted, 91% package size reduction) to existing skills-as-markdown finding.

### gstack v0.15.9.0 → v0.15.16.0 (4 new + 2 updates)

| Finding | Category | Priority |
|---------|----------|----------|
| gstack-review-army-parallel-specialist-dispatch | Evaluation | P2 |
| gstack-four-layer-prompt-injection-defense | Sandboxing | P1 |
| gstack-tabsession-per-tab-state-isolation | Orchestration | P3 |
| gstack-dx-review-developer-experience-audit | Evaluation | P3 |
| session-persistence-crash-resilient (updated) | Context Engineering | -- |
| self-evolving-loop-pattern (updated) | Orchestration | -- |

Source: `gstack-v01590-v015160-changelog.md`

Updates: Added Session Intelligence Layer details to session-persistence finding. Added recursive self-improvement + ClawHub publishing to self-evolving-loop finding.

### Priority Distribution of New Upstream Findings

| Priority | Count |
|----------|-------|
| P1 (Implement Now) | 1 |
| P2 (Design Required) | 10 |
| P3 (Monitor) | 2 |

### Category Distribution of New Upstream Findings

| Category | Count |
|----------|-------|
| Evaluation | 4 |
| Orchestration | 3 |
| Sandboxing | 2 |
| Context Engineering | 1 |
| Tool Integration | 1 |
| Agent Design | 1 |
| Prompt Craft | 1 |

## Goal 2a: Deferred Finding Updates (17 updates)

### Video 4 (Stop Using Terminal) -- 2 updates
- `goal-first-agent-management-abstraction.md` -- Added last-two-messages summary view, output gallery, memory continuity
- `human-on-the-loop-hotl-autonomy-tiering-framework.md` -- Added per-task permission selection evidence

### Video 13 (Agent 100x) -- 5 updates
- `autonomy-gradient-not-binary-delegation.md` -- Added Jones's 5th deployment commandment, `dangerously-skip-permissions` warning
- `build-operate-separation-principle.md` -- Added "clarity of intent" prerequisite, "generic average" output warning
- `iterative-refinement-loop-with-quality-gate.md` -- Added "build observability from day one" commandment
- `qa-agent-independent-compliance-review.md` -- Added $14K voice agent cautionary tale
- `planner-executor-deterministic-guardrails.md` -- Added railroad analogy, agents-within-steps principle

### Video 2 (Claude Leak) -- 5 updates
- `verification-agent-seven-prompt-patterns.md` -- Added pattern #6 binary pass/fail priority, pattern #7 laziness targeting
- `fork-subagent-parallel-trajectory-exploration.md` -- Added "trajectory engineering" formal definition, `/btw` production proof
- `git-status-context-injection-token-hygiene.md` -- Added IDE-specific detail (VS Code/JetBrains silent streaming)
- `micro-compact-stale-tool-call-removal.md` -- Added feature-flag warning, 18% duplicate read stat, 2.6% fleet savings
- `claude-code-12-agent-primitives.md` -- Added concrete primitive examples, "80% infrastructure" thesis reinforcement

### Video 11 (Ultra Plan) -- 1 update
- `claude-code-ultra-plan-three-mode-planning.md` -- Added blast-radius task heuristic, binary readable strings discovery

### Video 7 (RAG-Anything) -- 2 updates
- `rag-anything-multimodal-document-processing.md` -- Added GPT-5.4 nano model, Ollama local substitution
- `mineru-local-document-parsing-for-rag.md` -- Added LaTeX equation handling detail

### Video 5 (Karpathy) -- 2 updates
- `karpathy-llm-knowledge-base-obsidian-rag.md` -- Added Claude raw/ folder bypass detail
- `claudemd-as-knowledge-base-traversal-guide.md` -- Added structural consistency instruction detail

## Goal 2b: Finding Crosslinks

42 new crosslinks written across 3 parallel batches.

### By Relationship Type

| Type | Count |
|------|-------|
| same-problem | 24 |
| enables | 12 |
| extends | 5 |
| contradicts | 0 |
| upgrade (same-problem → extends) | 1 |

### Notable Clusters

- **Review bottleneck cluster** -- review-bandwidth-as-organizational-bottleneck became a hub with 5+ inbound links (trust-calibration enables, llm-as-judge enables, gstack-review-army enables, compound-review-debt same-problem, reviewer-skill-elevation same-problem)
- **Prompt injection cluster** -- Both new sandboxing findings (GSD scanner, gstack 4-layer) extend the existing prompt-injection-risk finding and link to each other as same-problem
- **Cross-session persistence cluster** -- gsd-global-learnings-store links to 4 existing findings (extends progress-md-session-bridge, same-problem with four-tier-memory, long-term-memory, queryable-codebase-intelligence)
- **Parallel execution cluster** -- cloud-plan-parallel links to fork-subagent, cloud-local-teleport, and gstack-tabsession as same-problem variants of per-context state isolation

### Cross-Category Links (highest value)

| Finding A (Category) | rel | Finding B (Category) |
|----------------------|-----|----------------------|
| ide-context-streaming (Context Eng) | enables | gsd-execution-context-profiles (Agent Design) |
| bmad-outcome-based-skill-rewrite (Prompt Craft) | same-problem | context-curation-over-context-stuffing (Context Eng) |
| gsd-gates-taxonomy (Evaluation) | enables | gstack-review-army (Evaluation) |
| gsd-gates-taxonomy (Evaluation) | enables | compound-review-debt (Governance) |
| context-pollution (Evaluation) | enables | agent-self-reporting-unreliability (Evaluation) |

## KB State After This Session

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Findings | 305 | 318 | +13 |
| Sources | 73 | 76 | +3 |
| Authorities (updated) | ~60 | ~60 | 3 updated |
| Crosslinks | 155 | 197 | +42 |
| Watched libraries | 7 | 7 | 3 updated |
