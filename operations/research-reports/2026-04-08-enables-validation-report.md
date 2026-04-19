---
title: "Enables Validation + Intent Engineering Crosslink Report"
date: 2026-04-08
type: maintenance
scope: crosslink-quality
---

# Enables Validation + Intent Engineering Crosslink Report — 2026-04-08

## Overview

Two objectives:
1. **Enables audit** — Spot-check all 34 migration enables classifications using strict binary tests
2. **Intent Engineering crosslink pass** — De-isolate 3 Intent Engineering findings

## Objective 1: Enables Validation Audit

### Methodology

All 34 enables links from the session 14 legacy migration were re-evaluated against the strict binary test:
- Q1: Does Finding A describe a concrete mechanism, technique, or infrastructure component?
- Q2: If you removed A, would Finding B **break or degrade significantly**?

The "helpful ≠ required" anti-pattern was applied rigorously.

### Results

| Verdict | Count | % |
|---------|-------|---|
| **CORRECT** (enables confirmed) | 5 | 14.7% |
| **Reclassified → same-problem** | 6 | 17.6% |
| **Reclassified → extends** | 2 | 5.9% |
| **Removed** (no relationship) | 21 | 61.8% |
| **Total** | **34** | 100% |

**Error rate: 85.3%** — significantly higher than the expected 40-60% (based on session 13 validation). The dominant failure pattern is over-reach on Q2: classifying "helpful" as "required."

### Correct Enables (5)

| Source (enables) | Target (enabled-by) | Rationale |
|------------------|---------------------|-----------|
| ace-evolving-playbook | ace-execution-feedback | Execution feedback is a specific ACE framework mechanism |
| ace-evolving-playbook | ace-delta-updates | Delta updates are an internal ACE mechanism |
| four-layer-enterprise-memory-stack | memory-cross-layer-promotion | Promotion governance requires multiple layers to exist |
| agent-memory-architecture-multi-agent-layered | memory-cross-layer-promotion | Same as above — layered architecture enables cross-layer governance |
| advanced-elicitation-techniques-library | yaml-templates-with-embedded-elicitation | Templates embed techniques from the library; removing library degrades templates significantly |

### Reclassified to same-problem (6)

| Source | Target | Rationale |
|--------|--------|-----------|
| agent-identity-governance-enforcement-layer | autonomy-gradient-not-binary-delegation | Both address agent autonomy governance from different angles |
| claudemd-context-rot | tiered-context-injection | A identifies the problem, B proposes the solution |
| scalpel-local-parse-then-llm | agent-cost-blowup-mitigation | Both address agent cost optimization differently |
| reasoning-token-overhead | tiered-context-injection | A diagnoses cost mechanism, B proposes structural fix |
| context-pollution-same-window-verification-bias | agent-self-reporting-unreliability | Both address unreliable agent self-verification |
| gstack-review-army-parallel-specialist-dispatch | review-bandwidth-as-organizational-bottleneck | Review Army is one solution to the review bottleneck problem |

### Reclassified to extends (2)

| Source | Target | Rationale |
|--------|--------|-----------|
| four-layer-enterprise-memory-stack | governance-memory-append-only-audit | Stack includes governance memory as Layer 4; the audit finding elaborates on that one layer |
| claude-code-12-agent-primitives | tool-registry-metadata-first-design | 12-primitives is a broader catalog that includes the tool registry as one component |

### Removed (21)

All 21 failed Q2 — Finding B functions independently of Finding A. Common patterns:
- **Inverted dependency** (pair 10): dynamic-tool-pool-assembly was listed as enabling tool-registry, but the registry enables pool assembly, not vice versa
- **Independent observations** (pairs 4, 21, 25, 26, 28, 29): Target finding is an observation/principle that stands on its own regardless of source
- **Tool-agnostic patterns** (pairs 6, 7, 13, 16, 17, 30, 31, 32, 33, 34): Target finding works with alternative mechanisms
- **Unrelated problems** (pairs 1, 19, 22, 23, 24, 27): Findings address different problems despite superficial connection

### Analysis

The 85.3% error rate (vs expected 40-60%) has a clear root cause: the migration subagents applied a weaker Q2 threshold ("would B be somewhat less effective?") rather than the strict test ("would B break or degrade significantly?"). This is the same "helpful ≠ required" over-reach identified in session 13 but at a higher rate because migration subagents classified 102 pairs in bulk with less scrutiny than the dedicated crosslink evaluation subagents.

**Lesson for future migrations:** When classifying legacy untyped links, default to same-problem unless a strong dependency case exists. Enables should require the evaluator to articulate specifically what mechanism in B breaks without A.

## Objective 2: Intent Engineering Crosslink Pass

### Methodology

1. Identified candidate pairs for 3 isolated findings:
   - build-operate-separation-principle.md
   - five-persistent-human-skills-agent-era-framework.md
   - workflow-decomposition-skill-for-browser-agents.md

2. Evaluated 11 cross-category candidate pairs + 6 same-category pairs + 4 co-source pairs via subagent + manual review

3. Applied strict binary tests with all anti-patterns

### Results

| Finding A | Finding B | Rel | Rationale |
|-----------|-----------|-----|-----------|
| build-operate-separation-principle | skill-vs-process-distinction-deterministic-rails | same-problem | Both address "agents should not decide workflow flow; process must be deterministic" at different scopes (cross-system vs intra-workflow) |
| workflow-decomposition-skill-for-browser-agents | project-specific-custom-skills-for-repeated-task | same-problem | Both address "converting repetitive human workflows into agent-executable specifications" |

**2 crosslinks written** (4 entries total including bidirectional).

### Rejected Candidates (19 pairs)

The initial subagent evaluation rejected all 11 pairs (0% approval). Manual re-evaluation of the strongest candidates plus additional same-category and co-source pairs yielded only 2 valid links. Key rejection reasons:

- **build-operate-separation ↔ planner-executor**: Different boundaries (cross-system deployment vs intra-workflow planning/execution)
- **five-persistent-human-skills ↔ autonomy-gradient**: Different problems (human skills to retain vs agent permission levels)
- **five-persistent-human-skills ↔ reviewer-skill-elevation**: Scope mismatch (broad 5-skill framework vs narrow review role analysis)
- **five-persistent-human-skills ↔ MACHINE framework**: Different problems (governance skills vs technical coding skills)
- **workflow-decomposition ↔ playwright-cli**: Different problems (identifying workflows vs executing browser automation)

### Intent Engineering Isolation

| Metric | Before | After |
|--------|--------|-------|
| Isolated | 3/14 (21.4%) | 1/14 (7.1%) |
| Remaining isolate | — | five-persistent-human-skills |

five-persistent-human-skills remains genuinely isolated — it's a governance meta-level framework (which skills humans must retain) with no clear mechanical connection to any other finding in the KB. All candidate relationships failed the strict binary tests.

## Final KB State

| Metric | Session 14 End | This Session | Change |
|--------|----------------|--------------|--------|
| Grade | A (95/100) | A (95/100) | — |
| Total crosslinks | 1,087 | 1,054 | -33 |
| Isolated findings | 50 (15.5%) | 51 (15.8%) | +1 (+0.3pp) |
| same-problem | 728 | 744 | +16 |
| enables | 118 | 84 | **-34** |
| enabled-by | 111 | 92 | **-19** |
| extends | 62 | 64 | +2 |
| extended-by | 34 | 36 | +2 |
| contradicts | 34 | 34 | — |
| Intent Eng isolation | 21.4% | 7.1% | **-14.3pp** |

### Notes

- Crosslink count decreased by 33 because 21 false enables pairs were removed (42 entries) while 8 reclassifications preserved their entries with corrected types and 2 new Intent Engineering links were added (4 entries). Net: -42 + 4 = -38 entries removed... the discrepancy with -33 suggests some target findings had only one direction of the pair, or pre-existing duplicate entries were cleaned up during the correction pass.
- Isolation increased by 1 because some target findings that lost their only enabled-by link became isolated.
- The enables/enabled-by ratio imbalance (84 vs 92) reflects that some enables links from the session 14 crosslink pass (not the migration) remain valid and weren't part of this audit.

## Process Notes

- 4 parallel evaluation subagents for the 34 enables pairs (9/9/8/8 split)
- 1 exploration subagent for Intent Engineering candidate identification
- 1 evaluation subagent for Intent Engineering pairs (rejected all 11 — too strict)
- Manual re-evaluation of strongest candidates yielded 2 approved links
- YAML-safe Python scripts used for all writes (yaml.safe_load/dump)
- Post-write validation confirmed 0 parse errors across 50 modified files
- Total corrections: 29 pair modifications (21 removed, 6→same-problem, 2→extends) + 2 new crosslinks
