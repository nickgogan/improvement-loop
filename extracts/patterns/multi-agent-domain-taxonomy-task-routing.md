---
title: "Multi-Agent Domain Taxonomy — Task-Characteristic Routing"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "legitimate-multi-agent-domains-taxonomy"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The L > D single-agent default pattern is adopted. Task classification criteria (parallelizability, loss tolerance, context independence) are defined and documented. The four legitimate domains and three harmful domains are understood by all agents and operators."
  invariants: "Task routing decisions are based on empirical task characteristics, not architectural preference or market hype. Sequential-dependent tasks are never routed to multi-agent execution. The taxonomy is the sole authority for spawn-vs-single decisions."
  governance: "Owned by Meta-System knowledge layer. Adding or removing domains from either list requires a Design Decision backed by empirical evidence. The taxonomy is reviewed when new task types emerge or when foundational model capabilities shift."
  recovery: "If a task classified as legitimate-multi-agent produces degraded results, reclassify it as harmful and re-execute single-agent. If a task classified as harmful is discovered to be genuinely parallelizable, propose a taxonomy amendment via Design Decision."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Multi-Agent Domain Taxonomy — Task-Characteristic Routing

**Source:** [[legitimate-multi-agent-domains-taxonomy]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

The single-agent default (L > D hypothesis) tells teams *when not* to use multi-agent systems, but does not tell them *when to*. Without a positive taxonomy of legitimate multi-agent domains, teams either avoid parallelization entirely (leaving performance on the table for genuinely parallelizable work) or fall back to intuition and hype when deciding which tasks to split. The result is inconsistent architectural decisions — some tasks are over-parallelized (degrading quality) while others are under-parallelized (wasting time).

## Forces

- **Blanket rules vs. task-specific judgment.** "Never use multi-agent" is simple but sacrifices legitimate speedups. "Sometimes use multi-agent" requires a principled decision boundary that teams struggle to define.
- **Parallelizability vs. hidden dependencies.** Tasks that appear parallelizable (e.g., editing multiple files) may have hidden dependencies (e.g., file A's changes constrain file B). Misclassification is costly — it introduces boundary loss on tasks that cannot tolerate it.
- **Binary taxonomy vs. continuous spectrum.** Tasks are not cleanly "parallelizable" or "sequential" — many are hybrids with parallelizable subtasks embedded in sequential workflows. A binary taxonomy is actionable but imprecise.
- **Static taxonomy vs. evolving capabilities.** As models improve and inter-agent protocols mature, the boundary between legitimate and harmful domains may shift. A taxonomy that does not anticipate change becomes stale.

## Solution

Classify tasks into **legitimate** and **harmful** multi-agent domains based on three empirical characteristics: parallelizability (can subtasks run independently?), loss tolerance (can the result survive lossy handoffs?), and context independence (does each subtask require the full history of other subtasks?).

**Legitimate domains** (parallelizable, loss-tolerant, context-independent):

1. **Research.** Many sources processed independently; irrelevant ones discarded. Information loss between agents is acceptable because the task selects from abundance — missing one source among many is survivable.

2. **Debugging.** Multiple hypotheses tried in parallel; winners kept, losers discarded. Lossy handoffs between hypothesis-testing agents are acceptable because results are validated empirically against the actual failure.

3. **Mechanical operations.** File renames, format conversions, independent data transforms. No context dependency between units of work — each subtask is self-contained.

4. **Review.** Fresh perspective is valuable. Not having full implementation history is a feature, not a bug — reviewers who lack the implementer's context are more likely to spot assumptions and blind spots.

**Harmful domains** (sequential, context-dependent, loss-intolerant):

1. **Implementation.** Decisions in file A affect file B. Sequential reasoning degrades 39-70% when split across agents because each agent lacks the constraint context established by prior decisions.

2. **Planning.** Step dependencies require full context of previous decisions. A planner who does not know what was decided in step 3 cannot make a coherent step 4.

3. **Integration.** Connecting components requires understanding both sides simultaneously. Splitting integration across agents guarantees that each agent sees only half the interface.

The taxonomy is applied via the pre-spawn checklist from the single-agent default pattern. When a task matches a legitimate domain, multi-agent execution is authorized. When it matches a harmful domain, single-agent execution is enforced.

## Consequences

**Positive:**
- Provides a principled positive criterion for multi-agent use, complementing the L > D negative criterion.
- Based on empirical task characteristics (Google's 180-configuration study, production playbooks), not architectural fashion.
- Aligns with how MetaSystem already operates — research-loop extraction (many sources, independent findings) uses parallel subagents while build spec execution (sequential, context-dependent) runs single-agent.
- Actionable without quantitative measurement — the four legitimate domains can be identified by inspection of task structure.

**Negative:**
- Binary classification (legitimate vs. harmful) oversimplifies reality. Hybrid tasks with both parallelizable and sequential components need decomposition before routing, adding complexity.
- The taxonomy is based on current empirical evidence. As inter-agent communication improves, some "harmful" domains may become legitimate — the taxonomy requires periodic reassessment.
- Misclassifying a task as parallelizable when it has hidden dependencies produces degraded results with no warning signal until output quality is evaluated.
- No quantitative scoring rubric — classification currently depends on judgment about parallelizability, loss tolerance, and context independence.

## Known Uses

- **"Agent Orchestrators Are Bad" essay.** Synthesizes Google research (180 configurations, 39-70% degradation) with production experience to derive the four legitimate domains. The originating reference for this taxonomy.
- **MetaSystem research loop.** Parallel source processing with independent finding extraction — a textbook "research" domain where loss tolerance is high and parallelizability is inherent.
- **MetaSystem build spec execution.** Sequential, context-dependent implementation runs single-agent — consistent with "implementation" being a harmful domain.
- **Google empirical study (2512.08296).** Provides the quantitative basis: independent agents amplify errors 17.2x on sequential tasks, confirming the harmful-domain classification.
- **Competitive module development pattern.** Multiple teams building competing implementations of the same spec — a "debugging" domain variant where parallel hypothesis-testing produces better outcomes through selection.

## Contract

### Preconditions

- The L > D single-agent default pattern is adopted as the baseline architectural stance.
- Task classification criteria (parallelizability, loss tolerance, context independence) are defined and documented in the system's agent governance.
- All agents and operators understand the four legitimate domains and three harmful domains before making routing decisions.

### Invariants

- Task routing decisions are based on the taxonomy's empirical criteria, not on architectural preference, market hype, or desire for parallelism.
- Sequential-dependent tasks (implementation, planning, integration) are never routed to multi-agent execution regardless of time pressure.
- The taxonomy is the sole authority for spawn-vs-single decisions — no ad-hoc exceptions without Design Decision amendment.

### Governance

- Owned by Meta-System knowledge layer.
- Adding or removing domains from either list requires a Design Decision backed by empirical evidence (production measurements or rigorous benchmarks).
- The taxonomy is reviewed when new task types emerge in MetaSystem's operations or when foundational model capabilities shift significantly.
- A future improvement (quantitative scoring rubric for task characteristics) is tracked as an IB item, not a blocking requirement.

### Recovery

- If a task classified as legitimate-multi-agent produces degraded results (error amplification, missing context, inconsistent outputs), reclassify it as harmful and re-execute single-agent immediately.
- If a task classified as harmful is discovered to be genuinely parallelizable through operational experience, propose a taxonomy amendment via Design Decision with supporting evidence.
- If the taxonomy itself becomes stale (new task types not covered, empirical basis outdated), trigger a review cycle rather than making ad-hoc routing exceptions.
