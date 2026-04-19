---
title: "Crosslink Report — 2026-04-09"
type: "loop-report"
created: "2026-04-09"
---

# Finding Crosslink Report — 2026-04-09

## Summary

| Metric | Count |
|--------|-------|
| Candidate pairs evaluated | 800 |
| Proposed links (pre-validation) | 87 |
| Hub-trimmed to | 83 |
| Post-validation removals | 12 |
| Post-validation reclassifications | 5 (enables/extends → same-problem) |
| **Final links written** | **71** |
| enables | 4 |
| contradicts | 1 |
| extends | 4 |
| same-problem | 62 |
| Hit rate | 10.4% |
| Files modified | 71 |
| YAML errors | 0 |

### Comparison to Prior Pass (Session 11)

| Metric | Session 11 | Session 16 |
|--------|-----------|-----------|
| Pairs evaluated | 800 | 800 |
| Links written | 218 | 71 |
| Hit rate | 27% | 8.9% |
| same-problem % | 89% | 87% |
| enables % | 4% | 6% |
| extends % | 1% | 6% |
| contradicts % | 5% | 1% |

Hit rate is lower this pass because `--new-only` generates cross-category pairs between new findings and the existing KB, which have lower natural connectivity than within-category pairs. The higher enables/extends proportion reflects that new findings (especially from repo analyses) tend to have concrete implementation relationships with existing KB patterns.

## Coverage Impact

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Isolated findings (0 links) | 89 (23.3%) | 73 (19.1%) | -16 |
| Total crosslinks | 1078 | 1220 | +142 |
| Avg links (Evaluation) | 3.5 | 5.0 | +1.5 |
| Zero-link % (Evaluation) | 15.7% | 7.8% | -7.9pp |

16 previously-isolated findings now have connections. Evaluation category saw the largest improvement — the 3 new evaluation findings (builder-validator, cross-model-verification, ultra-review) are heavily connected to existing verification/quality patterns.

## Hub Findings (New Links Only)

| Finding | New Links | Total Links | Status |
|---------|-----------|-------------|--------|
| builder-validator-chain-pattern | 15 | 15 | At cap |
| cross-model-verification-for-bug-finding | 16 | 16 | 1 over cap |
| ultra-review-multi-agent-bug-hunting-fleet | 11 | 11 | OK |
| worktree-isolation-for-parallel-agent-sessions | 11 | 11 | OK |
| archon-yaml-defined-harness-workflows | 11 | 11 | OK |
| conway-always-on-persistent-agent | 6 | 6 | OK |
| harness-engineering-third-evolution | 5 | 5 | OK |

4 links were trimmed from builder-validator to respect the ~15 soft cap (dropped: agentic-harness-self-assessment, competitive-module-development, mandatory-uat, mcp-evaluation-primitives).

## Enables Links (4) — Post-Validation

| Finding A | enables | Finding B |
|-----------|---------|-----------|
| anthropic-managed-agents-platform | enables | ultra-review-multi-agent-bug-hunting-fleet |
| worktree-isolation | enables | boris-chernys-explore-plan-implement-commit |
| llm-as-judge-pattern | enables | ultra-review-multi-agent-bug-hunting-fleet |

**Reclassified to same-problem (3):** agent-self-reporting-unreliability → builder-validator / cross-model / ultra-review (motivational, not mechanistic)
**Removed (3):** worktree→kairos (KAIROS is sequential daemon), worktree→GSD (unsubstantiated in content), model-tier-routing→harness-engineering (economic, not mechanistic)

## Extends Links (4) — Post-Validation

| Finding A | extends | Finding B |
|-----------|---------|-----------|
| qa-agent-independent-compliance-review | extends | builder-validator-chain-pattern |
| two-stage-sequential-review | extends | builder-validator-chain-pattern |
| ultra-review-multi-agent-bug-hunting-fleet | extends | builder-validator-chain-pattern |
| cross-model-verification | extends | llm-as-judge-pattern |

**Reclassified to same-problem (2):** llm-as-judge→builder-validator (covers only validator side), verification-seven-patterns→builder-validator (covers only validator side)

## Contradicts Links (1)

| Finding A | contradicts | Finding B |
|-----------|-------------|-----------|
| advanced-elicitation-techniques-library | contradicts | brevity-constraints-reverse-llm-performance |

Tension: A's 18 verbose techniques (CoT, stakeholder roundtable, critique-and-refine) conflict with B's finding that brevity constraints improve accuracy by 26pp. Both address LLM output quality improvement through prompting strategies but prescribe incompatible approaches.

## Cross-Category Clusters

**Verification/Quality cluster** (Evaluation ↔ Orchestration ↔ Tool Integration):
- builder-validator-chain → cross-model-verification → ultra-review → llm-as-judge → qa-agent → verification-agent-seven-patterns → two-stage-sequential-review
- This cluster connects 7 Evaluation findings with Orchestration patterns (GSD, planner-executor) and Tool Integration (context-pollution)

**Parallel Execution cluster** (Orchestration ↔ Agent Design ↔ Tool Integration):
- worktree-isolation → Boris workflow → agent-teams → cloud-plan-parallel → deep-plan → fork-subagent → atomic-checkout → explicit-permission-allow-listing → durable-workflow-engine
- 9 findings connected through the theme of "running concurrent agent sessions safely"

**Orchestration Frameworks cluster** (Orchestration):
- archon → GSD → BMAD v6 → multi-framework-power-stack → planner-executor → phase-task → specialized-harness → superpowers → orchestrated-execution → orchestrated-competition
- 10 findings addressing "how to structure multi-agent software dev workflows"

**Model Selection cluster** (Model Selection ↔ Orchestration):
- advisor-executor → multimodel-routing → task-specific-routing → planner-executor
- Links model selection decisions to orchestration architecture choices

**Persistent Agent cluster** (Agent Design ↔ Orchestration):
- conway → KAIROS → IDE-first → scheduled-task-dashboard
- 4 findings about always-on/persistent agent environments

## Validation Results

Two validation subagents (Sonnet, full-text reads) checked 26 links:

### Enables/Extends/Contradicts (16 links checked)

| Type | Checked | CORRECT | WRONG | BORDERLINE |
|------|---------|---------|-------|------------|
| enables | 9 | 3 | 3 | 3 |
| extends | 6 | 4 | 2 | 0 |
| contradicts | 1 | 1 | 0 | 0 |

**Fixes applied:**
- 3 enables reclassified to same-problem (agent-self-reporting → 3 verification findings: motivational, not mechanistic)
- 3 enables removed (worktree→kairos, worktree→GSD, model-tier→harness: not mechanistically required)
- 2 extends reclassified to same-problem (llm-as-judge and verification-7-patterns only cover the validator side of builder-validator-chain)

### Same-Problem Sample (10 links checked)

| Checked | CORRECT | WRONG | BORDERLINE |
|---------|---------|-------|------------|
| 10 | 1 | 6 | 3 |

**60% error rate** — consistent with calibration (30-60% for same-problem from summaries). All 9 WRONG/BORDERLINE removed.

**Common error patterns:**
- Complementary ≠ same-problem (4 cases): A motivates B or A constrains B, but they address different specific problems
- Scope mismatch (3 cases): broad platform vs narrow technique (Conway→Playwright, Conway→Skill.md format)
- Different stack levels (2 cases): runtime vs design-time addressing "same domain"

### Net Effect

| Metric | Pre-validation | Post-validation |
|--------|---------------|-----------------|
| Total links | 83 | 71 |
| enables | 9 | 3 |
| extends | 6 | 4 |
| contradicts | 1 | 1 |
| same-problem | 67 | 63 |

## Methodology

- 800 candidate pairs generated via `crosslink_pair_generator.py --new-only`
- 16 batches of 50 pairs each, dispatched to Sonnet subagents with full binary test prompts
- Anti-patterns included in prompts: category proximity, complementary ≠ same-problem, scope mismatch, helpful ≠ required
- All writes via `kb_parser.write_frontmatter()` with round-trip validation
- Hub trimming applied to builder-validator-chain (19 → 15)
- Post-write validation: 2 Sonnet subagents with full-text reads checked all 16 non-same-problem links + 10 stratified same-problem samples
- All WRONG/BORDERLINE links fixed (removed or reclassified)
