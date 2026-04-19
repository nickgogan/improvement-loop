---
notion_id: 32b1e08b-9b34-81f3-bdc4-c7c4ee7185f2
name: First-Principles Context Management Taxonomy
summary: All novel LLM memory architectures (RLMs, RAG, sub-agents, REPL loops) reduce to three storage locations and two constraints. Understanding this framework allows practitioners to design custom
  context solutions rather than adopting off-the-shelf architectures wholesale.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: gsd-queryable-codebase-intelligence-store.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: context-type-taxonomy-structural-vs-operational-vs.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# First-Principles Context Management Taxonomy

## What It Is
Roman's unifying framework: there are exactly three places a model can 'remember' information: (1) the context window (in-context, ephemeral), (2) external memory queried at inference time (RAG, vector stores, file systems), and (3) model weights (fine-tuning, RLHF -- persistent but expensive). All architectures exist because of two constraints: models have limited context windows that degrade with fill (context rot), and models forget everything between calls.

## Why It Matters
The AI architecture landscape is noisy with new frameworks released weekly. Practitioners who understand the underlying constraints and the three-storage-location taxonomy can evaluate any new architecture quickly and design purpose-fit solutions.

## Why People Are Using It
Roman presents this as the core insight that allows the Agentic Lab community to build bespoke solutions.

## Potential Alternatives
Framework-specific documentation (LangChain, LlamaIndex) which provides implementations without the underlying mental model.

## Potential Improvements
Extending the taxonomy to address the time dimension (when to retrieve vs. pre-load vs. cache) would complete the framework for production system design.

## Potential Failure Modes
The framework is accurate but may oversimplify -- the choice between architecture approaches also depends on latency requirements, cost, and team expertise.
