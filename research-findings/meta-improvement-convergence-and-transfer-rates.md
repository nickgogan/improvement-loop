---
name: Meta-Improvement Convergence Patterns and Transfer Rates
summary: 'HyperAgents empirically quantify how self-improvement converges: plateau at 8-12 iterations, early volatility (days 1-5, +/-5-8%), stabilization (days 6-10, +/-1-2%), maturity (day 11+, <0.5%
  variance). Cross-domain transfer rates measured: error recovery 72%, tool strategies 65%, memory management 70%, formatting 45%.'
implementation_notes: When iterating on MetaSystem skill procedures, expect diminishing returns after 8-12 revision cycles. Focus early iterations on high-signal changes, then shift to cross-domain transfer
  (reusing patterns from one skill in another).
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- hyperagents-arxiv-260319461.md
related_findings:
- file: cross-domain-transfer-of-meta-improvements.md
  rel: extends
- file: metacognitive-self-modification-hyperagents.md
  rel: extends
- file: ace-execution-feedback-no-labels-required.md
  rel: extends
- file: metacognitive-self-modification-hyperagents.md
  rel: extends
proposals: []
date_discovered: '2026-04-07'
last_updated: 2026-04-08
pipeline_status: raw
consumed_by: []
---
## What It Is

Empirical data from HyperAgents on how agent self-improvement progresses over time, and which improvement types transfer best across domains.

**Convergence timeline:**
- **Days 1-5 (domain-specific):** High volatility (+/-5-8% variance). Meta-agent discovers domain-specific optimizations. Forced rollbacks peak here (8-22% of modifications).
- **Days 6-10 (abstraction discovery):** Convergence begins (+/-1-2% variance). Meta-agent transitions from surface-level to abstract strategy improvements.
- **Days 11-14 (cross-domain validation):** Stability (<0.5% variance). Diminishing returns on in-domain gains. Remaining improvements come from cross-domain transfer.
- **After iteration 12-15:** Exploration exhaustion. Meta-agent converges to local optima. Requires manual intervention or curriculum reset.

**Transfer rates by improvement type:**
| Improvement Type | Transfer Rate | Example |
|------------------|---------------|---------|
| Error recovery heuristics | 72% | Failure classification, differentiated recovery |
| Memory management | 70% | Summarization, hierarchical retention, pruning |
| Tool strategy optimization | 65% | Call reduction, sequencing, cost-aware ordering |
| Decomposition patterns | 60% | Subtask validation gates, dependency tracking |
| SWE-bench to Polyglot | 52% | Coding-specific patterns |
| Formatting preferences | 45% | Output structure, verbosity levels |

**Economic viability heuristic:** Meta-optimization is profitable for tasks with complexity >1000 tokens, reuse >100 instances, and where 2-3% improvement offsets the optimization cost.

## Why It Matters

This is the first quantified data on how many iterations of agent self-improvement are worthwhile and which improvement types generalize. The practical takeaway: invest 8-12 iterations in improvement, expect diminishing returns after that, and prioritize improvements that transfer (error recovery, memory management) over domain-specific ones (formatting).

## Why People Are Using It

ICLR 2026-accepted paper with specific benchmark data across SWE-bench, Polyglot, mathematical reasoning, and writing/editing domains.

## Potential Improvements

Meta-learning curricula: start optimization in a high-transfer domain (coding) and seed meta-improvements into new domains, rather than starting from scratch in each domain.

## Potential Failure Modes

Transfer rates may vary significantly depending on domain similarity. The 14-day timeline assumes current model capabilities — more capable models may converge faster or unlock additional improvement tiers. The economic viability heuristic is based on current API pricing and may shift.
