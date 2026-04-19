---
notion_id: 32b1e08b-9b34-817d-8c73-d8ae35a8feca
name: Agent Onboarding via Interview-Style Context File Generation
summary: Instead of manually writing agents.md/CLAUDE.md context files, users should instruct their agent to interview them with questions and then generate the file from the answers. This ensures comprehensive
  context coverage without requiring the user to know in advance what information matters.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- building-ai-agents-that-actually-work-full-course.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Agent Onboarding via Interview-Style Context File Generation

## What It Is
To initialize a new AI agent role (executive assistant, head of marketing, CFO), the practitioner opens a fresh session and tells Claude or their preferred harness: 'Ask me interview-style questions to extract all the context you need to build out an agents.md file for [role].' Claude asks structured questions about business context, tools, preferences, tone, and processes, then synthesizes the answers into a well-structured context file ready to deploy.

## Why It Matters
Most users don't know what information their agents need until the agents fail on tasks that require that information. The interview approach flips this: the model, which understands what agents need, drives the discovery. This produces more comprehensive context files than users would write from scratch.

## Why People Are Using It
Non-technical users building their first agent deployments benefit most — they don't need to understand agent architecture to provide good context when guided by structured questions. Even experienced practitioners use it to avoid blank-page paralysis.

## Potential Alternatives
Manually writing context files from scratch using templates; importing an existing project README or business document and asking Claude to restructure it as an agents.md; using a pre-built agents.md template library.

## Potential Improvements
Role-specific interview templates (executive assistant vs. marketing head vs. developer) that probe domain-specific context would yield more targeted context files than a generic interview.

## Potential Failure Modes
Users may give imprecise or incomplete answers during the interview, resulting in a context file that sounds comprehensive but is missing critical operational detail. The interview must be done thoughtfully, not rushed.
