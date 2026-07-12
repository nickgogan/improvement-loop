---
name: Push vs Pull Context Loading
summary: Two opposing approaches to agent context assembly — push model (GSD) where the harness pre-assembles everything via @-reference chains, and pull model (Superpowers) where the harness loads one
  bootstrap skill and the agent self-activates others on demand. BMAD's 3-level progressive disclosure splits the difference. No convergence across 7 analyzed repos.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: three-layer-context-chain-loading.md
  rel: same-problem
- file: memory-file-to-skill-migration.md
  rel: extended-by
- file: two-axis-parallel-code-review-standards-vs-spec.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-07-12'
pipeline_status: raw
consumed_by: []
---
# Push vs Pull Context Loading

## What It Is
Two fundamentally opposing approaches to assembling an agent's working context. **Push model** (GSD): the harness resolves a chain of `@`-references before the agent starts, delivering a complete context package. The agent receives everything it needs without requesting anything. **Pull model** (Superpowers): the harness loads ONE bootstrap skill, and the agent decides what else to load based on task analysis. The "1% chance → invoke" heuristic means agents err toward loading rather than guessing. **Progressive disclosure** (BMAD): a middle path with three levels — L1 metadata (always loaded), L2 instructions (loaded on activation), L3 resources (loaded on demand).

## Why It Matters
This is a fundamental architectural tradeoff with no clear winner. Push guarantees completeness — the agent cannot miss context it does not know exists. But push risks context bloat, consuming token budget with material irrelevant to the current task. Pull scales better to large skill libraries and preserves token budget, but depends entirely on the agent's judgment about what to load — and agents can misjudge. The fact that seven independently developed repos have not converged on a single approach suggests both have legitimate use cases.

## Why People Are Using It
Observed in [Superpowers](https://github.com/obra/superpowers) v5.0.7 — see [[superpowers-analysis]] for structural details. Observed in [GSD](https://github.com/gsd-build/get-shit-done) v1.33.0 — see [[gsd-analysis]] for structural details. GSD's push model reflects a philosophy that context completeness is more important than token efficiency. Superpowers' pull model reflects a philosophy that agent autonomy and scalability matter more. BMAD's progressive disclosure reflects a philosophy that different context has different urgency.

## Potential Alternatives
Hybrid push-pull where critical context is pushed and optional context is pulled. Context profiles that pre-define which skills load for which task types. RAG-based context retrieval where the agent queries a vector store. Negotiated loading where the agent requests context and the harness decides what to provide based on budget.

## Potential Improvements
Token-budget-aware loading that dynamically adjusts push depth or pull aggressiveness based on remaining context capacity. Telemetry on what context agents actually use — over time, this reveals which pushed context is wasted and which pulled context is missed. Task-type routing that selects push or pull based on task complexity (simple tasks get push, complex tasks get pull).

## Potential Failure Modes
Push: context window exhaustion on complex tasks with deep reference chains. Pull: missed context that the agent did not know to request, leading to incorrect or incomplete work. Progressive disclosure: the boundary between levels is a design decision that may not match actual task needs. All approaches: stale context if loaded files have changed since last read.
