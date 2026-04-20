---
name: 'NotebookLM MCP + Claude Code: Cited Knowledge Layer for Agentic Workflows'
summary: Connect Claude Code to NotebookLM via MCP so agents can query a grounded knowledge base mid-workflow and receive citation-traceable answers. The combination turns a personal AI assistant into a
  research-grounded executor that can attribute every protocol recommendation back to a specific source timestamp.
implementation_notes: null
category: Agentic OS
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources:
- notebooklm-claude-code-expert-experiments.md
proposals: []
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
related_findings:
- file: notebooklm-as-external-knowledge-base-for-context.md
  rel: same-problem
- file: notebooklm-python-api-programmatic-access-beyond.md
  rel: companion
pipeline_status: raw
consumed_by: []
---
# NotebookLM MCP + Claude Code: Cited Knowledge Layer for Agentic Workflows

## What It Is

A Claude Code skill (downloadable, installable) that connects Claude Code to a personal NotebookLM instance via MCP. The connection enables:

- Listing all notebooks in a NotebookLM account
- Querying any notebook with a natural-language question and receiving grounded, citation-tagged answers
- Running multiple queries in parallel (the video shows 6 parallel sub-agents querying different health dimensions simultaneously)
- Saving responses — with their citations — directly to Obsidian for backtracking and dashboard display

The key property is **citation traceability**: every answer NotebookLM returns is tagged to a specific source (YouTube video + timestamp or document section). Claude Code can surface and verify citation quality (the practitioner demonstrates asking Claude to score 7 out of 8 citations as strong matches).

## Why It Matters

This is the integration layer that transforms NotebookLM from a web-UI chat tool into a queryable knowledge API that Claude Code can call as a tool. The "external KB as context on demand" architecture (already captured as a finding) becomes operational here: the MCP connection is the mechanism that makes on-demand retrieval possible without custom RAG infrastructure.

The parallel querying pattern (6 sub-agents, 6 health dimensions) demonstrates that this is not a one-question-at-a-time workflow — it supports batch knowledge extraction that would be impractical manually.

## Why People Are Using It

- Zero custom infrastructure: NotebookLM handles embedding, retrieval, and citation; Claude Code handles orchestration
- Grounded answers eliminate hallucination from the knowledge layer — the KB only knows what you fed it
- MCP skill is shareable and reusable across different expert knowledge bases (Huberman health, Lenny's product management, any YouTube channel)
- Citation verification is built in: Claude Code can score citation quality and surface discrepancies

## Potential Improvements

An official NotebookLM API (vs. the current browser-automation or undocumented-API approaches) would make this integration more stable. A structured response schema from NotebookLM would allow Claude Code to parse answers programmatically rather than as free text.

## Potential Failure Modes

- The MCP connection depends on unofficial/undocumented NotebookLM APIs that can break without notice
- NotebookLM has a source limit per notebook; very large expert corpora (500+ videos) may require multiple notebooks and routing logic
- Citation quality degrades when sources are poor transcripts or heavily paraphrased content
- Parallel queries against a single notebook may hit rate limits under heavy automated usage
