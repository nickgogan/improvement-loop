---
notion_id: 32b1e08b-9b34-815d-af34-e28fefa69f7c
name: Domain-Specific Intelligence from Historical Business Data
summary: The most effective domain knowledge for skills comes from extracting and synthesizing actual business artifacts (historical support tickets, training videos, Slack/ClickUp comments) using AI —
  not from prompting Claude to research the topic online.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- Perplexity Skills
adopted_in: null
sources:
- most-people-build-claude-skills-wrong-heres-what-w.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Domain-Specific Intelligence from Historical Business Data

## What It Is
For domain-specific intelligence skills, Bart argues against leaving Claude to 'do its own research' and instead recommends: (1) gather all existing institutional knowledge artifacts (historical support tickets, staff training documents and videos, internal Slack/ClickUp threads), (2) run those through AI to extract, categorize, and synthesize into clean knowledge files, (3) attach those files to the skill as domain context. This is the T1 support automation pattern: 20 years of founder knowledge captured in voice notes -> transcribed and categorized -> skill that responds exactly as the founder would.

## Why It Matters
Claude's generic internet knowledge cannot replicate company-specific institutional knowledge. For support, compliance, or operational tasks, the nuances that matter (specific failure modes, edge cases, escalation thresholds) only exist in internal historical data. Skills built on generic knowledge give generic answers.

## Why People Are Using It
Directly addresses the common failure mode of domain skills that produce plausible but wrong answers for company-specific questions. The voice note -> transcript -> skill pipeline makes implicit knowledge explicit and persistent.

## Potential Alternatives
Live RAG against a knowledge base, periodic re-extraction from updated ticket databases, fine-tuning (higher cost, less flexible).

## Potential Improvements
Setting up a pipeline to continuously pull new support tickets and update the domain knowledge files keeps the skill current over time.

## Potential Failure Modes
Historical data may contain outdated information, wrong answers from earlier in the company's history, or PII/sensitive data that shouldn't be included. Quality of the extracted knowledge depends heavily on the quality of source artifacts.
