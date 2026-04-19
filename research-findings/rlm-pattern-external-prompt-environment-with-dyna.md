---
notion_id: 32b1e08b-9b34-8142-9eab-dcb70d4b474e
name: 'RLM Pattern: External Prompt Environment with Dynamic Sub-LLM Search'
summary: Instead of loading large documents into the context window, an RLM places them in an external environment that the root model can interact with via code (search, chunk, peek). Sub-LLMs process
  retrieved chunks and return answers, keeping the root model's context lean throughout.
implementation_notes: null
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources: []
proposals: null
date_discovered: '2026-03-22'
last_updated: 2026-04-08
related_findings:
- file: biomimetic-memory-auto-recall-over-tool-based.md
  rel: contradicts
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# RLM Pattern: External Prompt Environment with Dynamic Sub-LLM Search

## What It Is
An RLM architecture consists of: (1) a root LLM with a lean context (task description + tool instructions + sub-LLM outputs only), (2) an external environment containing the large document/codebase/prompt (500+ files, millions of tokens), (3) the root model writing code to interact with the environment (peek at first 1000 chars, grep for keywords, split by sections), (4) spawning sub-LLM calls when relevant content is found (each sub-LLM processes a chunk and writes its answer), and (5) the root model assembling sub-LLM outputs into a final answer. The root model never directly sees the full content — it only sees the results of its search operations.

## Why It Matters
Standard RAG loads retrieved chunks into the context window, which still grows with each retrieval. RLM keeps the root model's context lean throughout the entire inference by externalizing all content and only bringing in processed sub-LLM outputs. For brownfield codebases (500+ files), this enables data flow tracing that would be impossible with standard context-window loading.

## Why People Are Using It
Published as an academic paper (mentioned as notable at NeurIPS context). Roman notes it is structurally identical to agentic file search in Claude Code (repository = environment, bash/grep = code execution, sub-agents = sub-LLMs). This means the pattern is already implementable in Claude Code today without special infrastructure.

## Potential Alternatives
Standard RAG (retrieval into context), full context loading (only works for small codebases), chunking + summarization pipelines.

## Potential Improvements
The paper notes that reinforcement learning to improve the model's recursive search actions is a promising research direction — training the model to be better at deciding when to spawn sub-LLMs and what search operations to run.

## Potential Failure Modes
The paper notes that multiple layers of recursion (sub-LLMs spawning their own sub-LLMs) were explored but found unnecessary in practice. Coordination overhead between root and sub-LLMs adds latency. Sub-LLMs may miss relevant content if the root model's search strategy is poorly designed.
