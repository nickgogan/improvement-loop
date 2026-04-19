---
name: Legitimate Multi-Agent Domains Taxonomy
summary: 'Agent orchestration works well for inherently parallelizable, lossy-tolerant tasks: research (many sources, discard irrelevant ones), debugging (try hypotheses, keep winners), mechanical operations
  (file renames, independent transforms), and review (need fresh perspective, not full history). Sequential reasoning tasks degrade 39-70% with multi-agent systems.'
implementation_notes: Provides a concrete task taxonomy for MetaSystem's agent architecture decisions. Research-loop extraction (many sources, independent findings) is a legitimate multi-agent domain. Build
  spec execution (sequential, context-dependent) is not. Use this taxonomy when evaluating any proposal to add subagent parallelism.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
proposer_priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- agent-orchestrators-are-bad.md
related_findings:
- file: competitive-module-development-parallel-teams.md
  rel: extended-by
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
- file: l-d-hypothesis-information-loss-across-agent-bound.md
  rel: extends
- file: capability-saturation-threshold-45-percent.md
  rel: same-problem
- file: sub-agent-context-isolation-for-parallel-complex.md
  rel: enables
- file: specialization-theater-anti-pattern.md
  rel: same-problem
- file: harness-engineering-third-evolution.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
---
# Legitimate Multi-Agent Domains Taxonomy

## What It Is
A task-characteristic-based taxonomy for when multi-agent orchestration is justified vs. harmful:

**Legitimate domains** (parallelizable, lossy-tolerant):
- **Research:** Many sources processed independently; irrelevant ones discarded. Information loss between agents is acceptable because you are selecting from abundance.
- **Debugging:** Multiple hypotheses tried in parallel; keep winners. Lossy handoffs between hypothesis-agents are fine because results are validated empirically.
- **Mechanical operations:** File renames, format conversions, independent data transforms. No context dependency between units of work.
- **Review:** Fresh perspective is valuable; not having full implementation history is a feature, not a bug.

**Harmful domains** (sequential, context-dependent):
- **Implementation:** Decisions in file A affect file B. Sequential reasoning degrades 39-70% when split across agents.
- **Planning:** Step dependencies require full context of previous decisions.
- **Integration:** Connecting components requires understanding both sides simultaneously.

## Why It Matters
Provides a principled alternative to both "always use agents" and "never use agents." The taxonomy is based on empirical task characteristics, not market hype or architectural preference. It operationalizes the L > D hypothesis into actionable guidance.

## Why People Are Using It
The "Agent Orchestrators Are Bad" essay synthesizes Google research (180 configurations, 39-70% degradation) with production experience. The taxonomy aligns with how MetaSystem's research-loop already works: parallel source processing with independent finding extraction.

## Potential Improvements
Quantitative scoring rubric for task characteristics (parallelizability score, information flow score, error sensitivity score) to make the taxonomy mechanically applicable rather than judgment-based.

## Potential Failure Modes
Misclassifying tasks as parallelizable when they have hidden dependencies. The taxonomy is binary (legitimate vs. harmful) but reality is a spectrum. Hybrid tasks that are partially parallelizable and partially sequential need more nuanced treatment.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[multi-agent-domain-taxonomy-task-routing.md]] in `extracts/patterns/`
