---
notion_id: 32b1e08b-9b34-8102-b12c-d807f57b3e49
name: Skills + CLI Tools as Mobile-Triggerable Modules
summary: When Claude Code Channels receives a message, it resolves and executes the relevant locally-installed skill (e.g., 'thumbnail repurposing skill', 'Apify lead scraping skill'), treating each skill
  as a named capability that can be invoked by natural language from any device.
implementation_notes: null
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- claude-codes-leak-changes-everything.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: claude-dispatch-native-mobile-to-local-agent-orch.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Skills + CLI Tools as Mobile-Triggerable Modules

## What It Is
Nick demonstrates two skills triggered via Telegram: (1) a thumbnail repurposing skill that takes a YouTube thumbnail URL, extracts design elements, and generates a new version with the user swapped in; (2) an Apify lead scraping skill that searches for business leads and returns a CSV. Both are Claude Code skills (markdown files) installed in the `.claude` directory on the local machine. The Telegram message functions as the task prompt; the skill provides the procedural instructions; the agent executes locally and sends results back via Telegram.

## Why It Matters
This pattern separates capability definition (the skill, defined once) from capability invocation (the message, sent anytime from anywhere). It's the agent equivalent of a phone shortcut — one natural-language message triggers a complex multi-step workflow without re-specifying the procedure.

## Why People Are Using It
Skills persist across sessions and are reusable across interfaces (desktop and mobile). Once a skill is built and tested, it can be triggered with minimal input, reducing the barrier to delegating complex tasks while mobile.

## Potential Alternatives
Hardcoded scripts triggered by specific command keywords, n8n/Make webhooks with fixed workflows, voice-triggered agent pipelines.

## Potential Improvements
Skill discovery: if the user's message matches an available skill by intent rather than explicit name, the agent should surface it. Status updates during long-running skills (e.g., 'scraping in progress: 45/100') would improve async UX.

## Potential Failure Modes
Skill invocation ambiguity if multiple skills could match the request. Skills that require interactive clarification are awkward over async messaging. Long-running skills may time out or be interrupted by machine sleep.
