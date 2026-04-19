---
name: Finding Crosslink Report
date: "2026-04-07"
type: crosslink-report
---

# Finding Crosslink Report — 2026-04-07

## Summary
| Metric | Count |
|--------|-------|
| Candidate pairs evaluated | 704 |
| Proposed links | 155 |
| Link entries written | 308 |
| enables | 57 |
| extends | 14 |
| same-problem | 81 |
| contradicts | 3 |
| Unique findings with links | 135 of 279 (48%) |

## Methodology

Pairs were generated using three tiers:
1. **Cross-category shared-source pairs** (350) — findings sharing a source but in different categories
2. **New-new same-category pairs** (179) — pairs among the 59 newly extracted findings
3. **New-to-top-existing same-category** (175) — new findings paired with keyword-similar existing findings

6 parallel Sonnet agents evaluated 118 pairs each using the 4 binary-testable relationship types.

## Contradictions Found

| Finding A | Finding B | Rationale |
|-----------|-----------|-----------|
| MCP N+M Integration Economics | CLI-First Tool Integration | MCP vs CLI for same integration need |
| Biomimetic Memory Auto-Recall | RLM Pattern External Prompt Environment | Auto-inject vs active-query memory retrieval |
| Agent Cost Blowup Mitigations | Competitive Module Development | Cost discipline vs deliberate parallel spawning |

## Top Hub Findings (most connections)

- `bmad-method-v6-multi-agent-sdlc.md` — enables 6+ findings (document sharding, QA agent, YAML templates, scrum master, business analyst, new-chat hygiene)
- `context-file-instruction-bloat-eth-zurich.md` — same-problem with 5+ findings (context rot, CLAUDE.md bloat, minimal rules, three-tier vault, context file taxonomy)
- `binary-eval-assertion-design-deterministic-plus-ll.md` — enables 4 findings (Karpathy loop, eval-driven dev, four-layer eval, same-problem with grading hierarchy)
- `ace-delta-updates-over-monolithic-rewrites.md` — connected to 5+ findings (ACE playbook, context rot, context curation, ACE execution feedback)
- `planner-executor-deterministic-guardrails.md` — connected to 5+ findings (tool gateway, durable workflow, orchestrated execution, cost blowup, workflow state)

## Category Cluster Map

| Category Pair | Links |
|---------------|-------|
| Evaluation ↔ Evaluation | 15 |
| Context Engineering ↔ Context Engineering | 18 |
| Orchestration ↔ Orchestration | 12 |
| Memory Architecture ↔ Memory Architecture | 8 |
| Context Engineering ↔ Orchestration | 6 |
| Tool Integration ↔ Tool Integration | 8 |
| Evaluation ↔ Orchestration | 5 |
| Intent Engineering ↔ Intent Engineering | 4 |
| Agent Design ↔ Context Engineering | 3 |
| Tool Integration ↔ Orchestration | 3 |
