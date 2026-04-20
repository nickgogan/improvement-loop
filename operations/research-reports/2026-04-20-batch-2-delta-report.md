# Delta Report — 2026-04-20

## Scan Summary
- **Sessions covered:** 41 (OB1 repo analysis) + 42 (Batch 2 extraction)
- **Sources processed:** 13 Batch 2 sources (11 videos + 2 articles)
- **New findings added to KB:** 26
- **Existing findings updated:** 21
- **Crosslinks written:** 28 (from 800 candidate pairs, 4% hit rate)
- **Previous report:** 2026-04-19 (Batch 1 delta report)

## KB State Change

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Findings | 507 | 533 | +26 |
| Sources | 121 | 131 | +10 |
| Authorities | 61 | 67 | +6 |
| Watched Libraries | 15 | 15 | 0 |
| Dimensions | 11 | 11 | 0 |
| Null-priority findings | 0 | 0 | 0 |

Note: Source count increased by 10 (not 13) because Anthropic managed agents article (#18) was already processed, and OB1 repo analysis in session 41 added 0 new source entries.

## Session 41: OB1 Repo Analysis

Completed before Batch 2 extraction. Results:
- 15th watched library added (OB1)
- 5-dimension analysis at `watched-libraries/analysis/ob1-analysis.md`
- Cross-repo comparison updated to 15 repos across 6 matrices
- 7 new findings, 2 updated findings from cross-repo analysis

See commit `1988838` for full details.

## Session 42: Batch 2 Extraction

### Wave 1 — Agent/OS Patterns (3 sources)

| Source | Video ID | New | Updated |
|--------|----------|-----|---------|
| Agent cold start — tacit knowledge elicitation | 2PWJu6uAaoU | 3 | 2 |
| Karpathy Skills CLAUDE.md — four principles | d8BGxfW3Vj4 | 2 | 2 |
| Claude Code for life — daily briefs, Obsidian memory | aghRgs7KoyI | 3 | 2 |

**Subtotal:** 8 new, 6 updated

### Wave 2 — Automation/Dark Patterns (3 sources)

| Source | Video ID | New | Updated |
|--------|----------|-----|---------|
| Dark Code — spec-driven dev, comprehension gates | E1idsrv79tI | 2 | 2 |
| Dark Factory — Archon autonomous coding | Xg0tNz9pICI | 2 | 2 |
| Claude Routines — scheduled automations, webhooks | j3aXJNu9804 | 2 | 2 |

**Subtotal:** 6 new, 6 updated

### Wave 3 — Org/Strategy (3 sources)

| Source | Video ID | New | Updated |
|--------|----------|-----|---------|
| Unbundling management — routing/sensemaking/accountability | zhXgkQ3nYeE | 2 | 2 |
| GStack planning — multi-persona spec review | 6kM27uGP4n4 | 2 | 2 |
| World models for orgs — 3 architectures | fm6mYqFAM5c | 3 | 1 |

**Subtotal:** 7 new, 5 updated

### Wave 4 — Tools/Articles (4 sources)

| Source | Video/Article | New | Updated |
|--------|---------------|-----|---------|
| TasteMatter — concept graph, MCP-accessible | ZIS_okcwQ-Q | 2 | 2 |
| Interactive HTML artifacts — Bun hot reload | ASAaKhK1B5w | 2 | 1 |
| Anthropic Managed Agents (article) | anthropic.com | 0 | 0 |
| Steve Yegge — Beads memory system (article) | medium.com | 3 | 1 |

**Subtotal:** 7 new, 4 updated. Anthropic article already fully extracted (good dedup).

## New Findings

| Finding | Priority | Category | Source |
|---------|----------|----------|--------|
| tacit-knowledge-as-agent-delegation-barrier | P2 | Agent Design | #25 |
| openclaw-wrapper-ecosystem-survey-2026 | P3 | Orchestration | #25 |
| open-brain-personal-knowledge-store-pattern | P2 | Memory Architecture | #25 |
| surgical-change-constraint-agent-scope | P2 | Prompt Craft | #23 |
| declarative-goal-driven-agent-prompting | P2 | Prompt Craft | #23 |
| claude-code-daily-brief-multi-source-inbox-obsidian | P2 | Agentic OS | #29 |
| multi-agent-proportional-content-summarization | P2 | Agentic OS | #29 |
| ai-managed-vault-separate-from-human-vault | P2 | Agentic OS | #29 |
| dark-code-organizational-capability-problem | P2 | Governance | #15 |
| self-describing-codebase-structural-semantic-context | P2 | Context Engineering | #15 |
| holdout-validation-pattern-blind-regression | P2 | Evaluation | #19 |
| github-label-as-workflow-state | P2 | Orchestration | #19 |
| claude-routines-webhook-triggered-pipeline-chaining | P1 | Orchestration | #27 |
| hands-off-routine-prompt-precision-pattern | P2 | Prompt Craft | #27 |
| management-unbundling-routing-sensemaking-accountability | P2 | Governance | #16 |
| dri-rotation-pattern-time-bounded-sensemaking-ownership | P2 | Governance | #16 |
| gstack-office-hours-socratic-discovery-pipeline | P2 | Prompt Craft | #22 |
| gstack-spec-team-parallel-research-agents | P2 | Orchestration | #22 |
| org-world-model-three-architecture-patterns | P2 | Context Engineering | #30 |
| interpretive-boundary-layer-fact-vs-judgment | P1 | Context Engineering | #30 |
| signal-capture-as-byproduct-of-work | P2 | Memory Architecture | #30 |
| concept-graph-support-contradiction-detection | P2 | Memory Architecture | #24 |
| mcp-accessible-concept-graph-domain-context | P2 | Tool Integration | #24 |
| html-artifact-as-skill-output-design-variations | P2 | Tool Integration | #26 |
| bun-hot-reload-interactive-html-artifact-feedback-loop | P2 | Tool Integration | #26 |
| issue-based-agent-orchestration-replacing-markdown-plans | P1 | Orchestration | #28 |
| work-disavowal-failure-mode-context-limit-cheating | P1 | Agent Design | #28 |
| session-atomicity-single-issue-scope-quadratic-cost-reduction | P2 | Context Engineering | #28 |

**Priority distribution:** P1: 4, P2: 23, P3: 1

### P1 Highlights

1. **claude-routines-webhook-triggered-pipeline-chaining** — Event-driven multi-routine pipelines via webhooks. Directly applicable to MetaSystem scheduled workflows.
2. **interpretive-boundary-layer-fact-vs-judgment** — Separating facts from AI judgments at every output surface. Immediately applicable to IL output design.
3. **issue-based-agent-orchestration-replacing-markdown-plans** — Git-backed JSONL issue graphs for multi-agent coordination. Production-validated (Yegge's Wyvern project, 5+ concurrent agents).
4. **work-disavowal-failure-mode-context-limit-cheating** — Named failure mode where agents delete tests/disable assertions near context limits. Critical awareness for any autonomous pipeline.

## Updated Findings

| Finding | What Changed |
|---------|-------------|
| agent-onboarding-via-interview-style-context | 5-layer elicitation structure added (#25) |
| context-gap-task-vs-job | Linked to tacit knowledge barrier (#25) |
| agent-clarification-over-assumption-pattern | Karpathy evidence + tweet provenance (#23) |
| agent-context-kiss-commandments-minimum-viable | Training-data root cause for overbuilding (#23) |
| scheduled-tasks-for-real-time-context-maintenance | Living news digest sub-pattern (#29), evidence upgraded Medium→Strong |
| file-over-app-philosophy-for-knowledge-permanence | Vendor-independence rationale (#29) |
| spec-as-source-of-truth-for-agent-construction | "Spec becomes the eval" mechanism, Amazon Kira (#15) |
| eval-driven-development-autonomous-quality | Spec→eval flywheel (#15) |
| dark-factory-ai-only-codebase-management | Dan Shapiro 5-level framework, StrongDM production ref (#19) |
| archon-yaml-defined-harness-workflows | Provider model aliasing, VPS pattern (#19) |
| anthropic-managed-agents-platform | Routines: schedules, webhooks, API triggers (#27) |
| scheduled-task-dashboard-observability-layer | Anthropic ships this natively, P3→P2 (#27) |
| five-persistent-human-skills-agent-era-framework | Sensemaking/accountability mapping, Kimi failure mode (#16) |
| org-redesign-for-agentic-throughput-high-speed-rail | Kimi PM case validation (#16) |
| autoplan-auto-decision-pipeline | GStack concrete implementation, priority Not Flagged→P2 (#22) |
| planning-session-bias-separate-context-windows | GStack 600k token quantification (#22) |
| compounding-knowledge-loop-internal-data | Outcome encoding corroboration (#30) |
| programmatic-tool-calling-code-orchestrated-tool-use | TasteMatter ~90% token reduction (#24) |
| mcp-as-code-api-progressive-tool-discovery | Generalization to structured data stores (#24) |
| claude-code-channels-telegramdiscord-as-agent-inte | HTML artifact as live frontend (#26) |
| memory-decay-compaction-convergence | Corrected Beads misattribution (#28) |

## Crosslink Pass

- 800 candidate pairs evaluated across 4 parallel batches
- 32 proposed, 4 rejected as false positives → 28 written
- Distribution: 25 same-problem, 2 enables, 1 contradicts
- Hit rate: 4% (below 27% baseline — expected for summary-only eval with strict anti-patterns)

## Recommendations

### P1 — Act on These
- **Interpretive boundary layer** — immediate application: every IL delta report and finding should separate factual extraction from editorial judgment
- **Claude Routines webhooks** — evaluate for MetaSystem scheduled workflow replacement
- **Work disavowal failure mode** — add to agent design checklist; consider session-kill-at-boundary in autonomous pipelines
- **Issue-based orchestration** — evaluate for replacing markdown-based plan tracking in GSD or similar

### P2 — Design Required
- **Tacit knowledge elicitation** — agent-first interview pattern for new system onboarding
- **Self-describing codebases** — module manifests + behavioral contracts for MetaSystem fractal units
- **Signal capture as byproduct** — design knowledge-capture hooks that don't add workflow friction
- **Concept graph + MCP** — evaluate for making IL KB queryable via MCP

### P3 — Monitor
- **OpenClaw wrapper ecosystem** — watch for consolidation; no action needed

## Dimension Gaps

No new dimension gaps detected. All 26 new findings categorized cleanly into existing 11 dimensions. Agentic OS (DD-87) absorbed the personal/business OS patterns as intended. Governance dimension absorbed the org-redesign findings well.

## Next Scan Notes

- Steve Yegge's Beads system is worth monitoring — issue-based orchestration and work-disavowal are novel patterns with production evidence
- GStack continues to evolve — watch for new planning phases beyond office-hours + spec-team
- Claude Routines is a fast-moving Anthropic feature — recheck after next release cycle
- Dark Code channel identity unconfirmed — update authority entry when channel name is identified
