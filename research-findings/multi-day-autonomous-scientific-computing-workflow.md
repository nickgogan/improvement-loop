---
name: Multi-Day Autonomous Scientific Computing Workflow
summary: 'A four-component workflow for deploying Claude as an autonomous agent team for multi-day scientific computing: CLAUDE.md as iterative plan, CHANGELOG.md as persistent lab notes, test oracle against
  reference implementation, and git for crash recovery. Compresses months of domain work into days.'
implementation_notes: Validates and extends MetaSystem's existing patterns (PROGRESS.md, Ralph loop, ground-truth feedback). The shift from tight conversational oversight to high-level objective specification
  is the key design insight.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- anthropic-long-running-claude-scientific-computing.md
related_findings:
- file: session-persistence-crash-resilient.md
  rel: same-problem
- file: ralph-wiggum-execution-pattern.md
  rel: enables
- file: ground-truth-environmental-feedback-loops.md
  rel: enables
- file: progress-md-session-bridge.md
  rel: extends
- file: conway-always-on-persistent-agent.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---
# Multi-Day Autonomous Scientific Computing Workflow

## What It Is
A production workflow from Anthropic (by Siddharth Mishra-Sharma) for deploying Claude Opus 4.6 as an autonomous agent on multi-day scientific computing tasks. The workflow shifts from tight conversational oversight to high-level objective specification. Four components:

1. **CLAUDE.md as iterative plan**: Placed in the project root, articulates high-level goals (e.g., full feature-parity with CLASS, 0.1% accuracy on CMB angular power spectra), design decisions, deliverables, and context. Claude references it continuously and edits it iteratively, refined via human-Claude consultation.

2. **CHANGELOG.md as long-term memory**: Acts as "lab notes" logging current status, completed tasks, failed approaches (e.g., "Tried Tsit5 for perturbation ODE; too stiff, switched to Kvaerno5"), accuracy tables at checkpoints, and limitations. Prevents re-attempting dead ends across sessions.

3. **Test oracle against reference implementation**: Uses a reference implementation (CLASS C source) for unit tests that the agent constructs, expands, and runs continuously. Essential for deeply coupled pipelines where errors propagate causally. Claude bisects discrepancies against the reference.

4. **Git for coordination and monitoring**: Claude commits and pushes after every meaningful work unit, providing recoverable history, visible progress, and resilience to compute interruptions (e.g., SLURM HPC cluster timeouts).

The example project: implementing a fully differentiable cosmological Boltzmann solver matching CLASS to sub-percent accuracy, from scratch, over a few days.

## Why It Matters
This pattern compresses months or years of scientific computing work into days. The human role shifts from line-by-line coding to occasional oversight and plan refinement. It demonstrates that agentic workflows are viable for deeply technical, domain-specific work — not just generic software engineering. The git commit history also serves as "fast, hyper-literal postdoc lab notes," enabling human osmosis of domain knowledge outside the developer's expertise.

## Why People Are Using It
Anthropic uses this internally. The workflow draws from their prior C compiler project, which spanned ~2,000 sessions to compile the Linux kernel. The scientific computing application demonstrates generalization beyond pure software engineering to numerical/physics domains. The workflow is compute-agnostic (works on SLURM HPC, local machines, etc.).

## Potential Improvements
The workflow currently uses sequential work with subagents for causal debugging. Parallelization of independent physics modules (e.g., recombination vs. perturbations) could accelerate completion. The CLAUDE.md + CHANGELOG.md dual-file pattern could be formalized into a template for research-oriented agent work.

## Potential Failure Modes
Not production-grade — fails acceptable accuracy in some edge-case regimes. The workflow requires a high-quality reference implementation to serve as test oracle; domains without established reference implementations cannot use this approach. The Ralph loop scaffolding combats "agentic laziness" but adds overhead that may become unnecessary as models improve. Cost of multi-day Opus sessions is significant.
