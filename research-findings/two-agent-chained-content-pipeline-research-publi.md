---
notion_id: 32b1e08b-9b34-8111-b005-f2b31b001877
name: 'Two-Agent Chained Content Pipeline: Research -> Publish'
summary: 'Two Notion custom agents can work in sequence: a research agent (Carly) populates a trends database weekly, and a publishing agent (Stan) reads from that database and pushes content to social
  media via a make.com MCP connector. This two-agent chain extends custom agents beyond Notion''s native boundaries.'
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S2 (Notion Operations)
adopted_in: null
sources:
- notion-custom-agents-the-best-new-ai-for-all.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-07'
pipeline_status: "raw"
consumed_by: []
---
# Two-Agent Chained Content Pipeline: Research -> Publish

## What It Is
Agent 1 (Carly the Clever Seeker): runs every Tuesday, researches trending topics in the user's content niche via web search, populates a Notion weekly trends database with 20+ trending topics. Agent 2 (Stan): reads from the trends database and triggers posts to LinkedIn and Twitter/Instagram by calling a make.com MCP scenario. The make.com integration is the novel piece — it enables custom agents to push content to external platforms Notion doesn't natively integrate with, using a make.com custom MCP endpoint as the bridge.

## Why It Matters
This demonstrates that custom agents are not limited to Notion-internal operations. By connecting to make.com's MCP, the agent gains access to any automation make.com can execute — which covers hundreds of external tools and platforms. The pattern of Agent 1 (gather/process) -> Agent 2 (act/publish) is a reusable pipeline architecture for content and marketing workflows.

## Why People Are Using It
Content creators and marketers who want trend-reactive social posting without manual research-to-publish workflows. The chain separates the intelligence work (research) from the execution work (publishing), allowing each agent to be optimized for its specific job.

## Potential Alternatives
Single-agent pipeline doing research and publishing in one run (simpler but harder to troubleshoot); Zapier/n8n workflows that trigger independently of Notion's agent framework; manual research-to-scheduled-posts workflow.

## Potential Improvements
Agent 2 could include a human-in-the-loop approval step (sending a Slack notification with draft posts for review before publishing) to prevent low-quality or off-brand posts from going live automatically.

## Potential Failure Modes
The make.com MCP connection is described as 'currently being tested' — production reliability is unproven. Agent 2 publishing based on Agent 1's research without human review risks posting inaccurate or inappropriate content.
