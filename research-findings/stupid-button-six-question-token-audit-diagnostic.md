---
name: 'Stupid Button: Six-Question Token Waste Self-Audit Diagnostic'
summary: 'A six-question rapid self-assessment for token waste: (1) raw file formats, (2) conversation freshness, (3) model-task matching, (4) context pre-load audit, (5) prompt caching status, (6) search
  routing efficiency. Implemented as a prompt, a skill, and automated guardrails.'
implementation_notes: The three-tier implementation (prompt for beginners, skill for intermediate, guardrails for advanced) maps to MetaSystem's skill architecture. The guardrails tier -- automatic markdown
  conversion, index-first retrieval, minimum viable context scoping -- is directly implementable.
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- your-claude-limit-burns-in-90-minutes.md
date_discovered: '2026-04-07'
last_updated: '2026-07-12'
related_findings:
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: seven-rung-minimal-code-decision-ladder.md
  rel: same-problem
pipeline_status: extracted
consumed_by:
- skills/stupid-button-token-audit-diagnostic.md
---

## What It Is

A diagnostic tool built by Nate B Jones with three implementation tiers, centered on six questions that identify the most common token waste patterns:

**The Six Questions:**
1. Do you feed Claude raw PDFs and images when all you need is text? (Screenshots are "terribly inefficient" -- copy-paste text instead.)
2. When was the last time you started a fresh conversation? (Each turn resends the entire conversation history.)
3. Are you using the most expensive model for everything? ("Don't bring a Ferrari to the grocery store.")
4. Do you know what's loading in context before you type? (Run /context in Claude Code. Some users have 50K+ tokens loaded before typing a word.)
5. Are you caching stable context? (Cache hits on Opus cost $0.50/M vs $5/M standard -- a 90% discount.)
6. How are you handling web search? (Perplexity MCP burns 10-50K fewer tokens per search than native Claude search, is 5x faster, and returns structured citations.)

**Three Implementation Tiers:**
1. **Prompt** -- A diagnostic prompt you run against recent conversations that identifies specific waste patterns in your actual usage. Any plan, no setup required.
2. **Skill** -- An invocable skill that audits Claude Code or desktop environment, measures per-session token overhead, flags system prompt bloat, checks plugin/skill loading, and gives before/after comparisons. "Like a gas tank for tokens."
3. **Guardrails** -- Infrastructure-level automation: automatic markdown conversion for documents hitting the knowledge store, index-first retrieval instead of dump-and-search, context scoping to minimum viable context per query. Sits on Open Brain knowledge store.

## Why It Matters

Extends the Token Waste Taxonomy finding with a concrete, actionable diagnostic tool. The taxonomy identifies what waste patterns exist; the Stupid Button tells you which ones you are personally committing. The three-tier implementation path (prompt -> skill -> guardrails) provides a progression from manual awareness to automated prevention -- "where token management stops being a personal discipline and becomes infrastructure."

## Why People Are Using It

With Claude usage limits dominating discourse and next-gen models (Mythos) expected to be significantly more expensive ($50+/M input tokens speculated), token efficiency is becoming a job skill. Jones's specific cost comparison: sloppy session = $8-10 in compute; clean session = ~$1 for the same work. At team scale (10 people on API), that is $2,000/month vs $250/month.

## Potential Improvements

The skill tier could be adapted for MetaSystem's simplify-context skill, which already audits context files for bloat. The guardrails tier (automatic markdown conversion, index-first retrieval) could be implemented as pre-processing hooks. The diagnostic prompt could be integrated into session-handoff to produce a token efficiency score per session.

## Potential Failure Modes

The diagnostic may create anxiety about token usage that leads to under-specification -- users who are so worried about tokens that they provide insufficient context. The guardrails tier requires integration infrastructure (Open Brain or equivalent) that not all users have. The six questions are biased toward API/power users; casual users may not understand questions 4-6.

## Extraction Note — 2026-04-19
Extracted as **skill**: [[stupid-button-token-audit-diagnostic]] in `extracts/skills/`
