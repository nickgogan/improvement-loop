---
notion_id: 32b1e08b-9b34-81b0-8426-d28a0f315cab
name: 'memory.md: Cross-Session Preference Persistence via Self-Updating File'
summary: Adding a memory.md file alongside CLAUDE.md and instructing the agent to read it at session start and update it when corrections or new preferences are stated gives agents persistent cross-session
  memory without relying on any built-in harness memory system.
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- building-ai-agents-that-actually-work-full-course.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-27'
related_findings:
- file: context-engineering-supersedes-prompt-engineering.md
  rel: enabled-by
- file: memory-bank-isolation-per-agent-per-project.md
  rel: same-problem
- file: memory-cross-layer-promotion-governance.md
  rel: enabled-by
- file: agent-memory-architecture-multi-agent-layered.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
pipeline_status: "synthesized"
consumed_by:
  - "session-persistence-and-memory.md"
  - artifact: agent-must-read-and-update-memory-md-on-startup
    type: extracted-artifact
    form: rule
    date: 2026-04-27
    session: 83
---
# memory.md: Cross-Session Preference Persistence via Self-Updating File

## What It Is
A memory.md file is a plain markdown file that the agent reads at the start of every session and writes to whenever the user makes a correction or states a preference. The CLAUDE.md/agents.md is updated with an instruction like: 'Read memory.md on startup. When you learn something new or are corrected, update the relevant section in memory.md immediately. Keep memory.md current.' Over time, the memory file accumulates role-specific preferences (tone, formatting, tooling preferences, don't-do-this rules) and reduces errors in subsequent sessions through compounding improvement.

## Why It Matters
All major agent harnesses by default have no cross-session memory — a fresh session has no knowledge of previous corrections or stated preferences. Without memory.md, users repeat the same corrections endlessly. With it, the agent gets progressively better at the specific role over time.

## Why People Are Using It
Anyone building a persistent role-based agent (especially one that will be used daily for weeks or months) benefits from compounding improvement rather than constant reteaching. The open/transparent file also gives users full control over what the agent remembers, unlike opaque cloud memory systems.

## Potential Alternatives
Auto-memory in OpenClaw and Manis (built-in but opaque); Claude's project memory feature (also cloud-managed and not fully user-visible); embedding memory into the main CLAUDE.md (but risks bloating it beyond the 200-line best-practice limit).

## Potential Improvements
Periodic memory.md pruning rules (e.g., remove entries older than 90 days that haven't been referenced) would prevent memory files from growing indefinitely. Structured sections within memory.md (preferences, corrections, learned facts) would improve retrieval accuracy.

## Potential Failure Modes
If the agent writes incorrect or hallucinated information to memory.md without user verification, false memories compound over time. Memory files can grow to a size where they themselves cause context bloat (the same problem as oversized CLAUDE.md files). Best practice noted: keep CLAUDE.md under 200 lines.

## Extraction Note — 2026-04-27

Extracted as **rule**: [[agent-must-read-and-update-memory-md-on-startup]] in `extracts/rules/`. Harvested from the G7 (session-persistence-and-memory) queue per IB-164 / DD-101 promotion path.
