---
name: SOUL.md Agent Constitution Pattern
summary: SOUL.md defines agent identity — personality, core values, long-term instructions, and restrictions — as the first layer in the prompt stack (SOUL→tools→memory→skills→overlays). Separates WHO the
  agent is from WHAT it does. Acts as a soft constraint constitution, not security — delegate access control elsewhere.
implementation_notes: MetaSystem's CLAUDE.md + constitution.md partially implement this pattern. The explicit separation of identity (SOUL.md) from capabilities (skills/tools) and the layered prompt stack
  concept could inform a redesign of MetaSystem's context file architecture.
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- openclaw-soul-md-explained.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
related_findings:
- file: five-layer-agent-prompt-architecture.md
  rel: same-problem
- file: context-file-taxonomy-claudemd-soulmd-agentsmd.md
  rel: extends
pipeline_status: synthesized
consumed_by:
- agent-design-patterns.md
---
# SOUL.md Agent Constitution Pattern

## What It Is
A Markdown file loaded at every reasoning cycle that defines agent identity: personality (tone, style), core values (privacy, honesty, no unauthorized actions), long-term instructions (daily briefings, response formats), and restrictions (never give legal advice, disclose AI nature). First layer in prompt stack: SOUL.md → tools → memory → skills → overlays. Part of OpenClaw's memory system alongside USER.md, MEMORY.md, HEARTBEAT.md, AGENTS.md, TOOLS.md.

Four-section anatomy with specific names: (1) Core Truths — philosophical heuristics for resolving ambiguity, (2) Boundaries — an "operational immune system" with production lock protocol, (3) Vibe — explicit override of apologetic base behavior via negative constraints (e.g., "don't hedge, don't apologize"), (4) Continuity — temporal state management with memory poisoning defense. Session boot sequence: forced disk-read (not just "loaded" into context), deliberate 4-10K token upfront cost that prevents cold starts. Learn-first protocol: if encountering an unknown situation, the agent must search codebase and parse logs before asking the human. Explicit action bias: draft code blocks and run scripts rather than summarize intent. External communication gating: may compile data but never transmit to public internet without explicit confirmation. Human-in-the-loop proposal merge for self-modification: changes to the agent's own memory or config go through a proposal document requiring human approval.

## Why It Matters
Separates identity from capability — agent personality persists across tools and skills without being overridden. Creates consistent behavior without repeating instructions in every context file. Acts as a compliance firewall for sensitive use cases where agent behavior must be predictable.

## Why People Are Using It
OpenClaw (346K GitHub stars, most-starred project on GitHub) uses it as foundational architecture. Template-driven approach makes it accessible — users fill in sections rather than writing from scratch. The pattern has influenced Claude Code's own CLAUDE.md conventions.

## Potential Alternatives
MetaSystem's CLAUDE.md + constitution.md (combines identity and project rules). AGENTS.md context files (tool-agnostic but less identity-focused). Inline system prompts (no persistence across sessions).

## Potential Improvements
Dynamic personality overlays for different contexts (e.g., formal for governance work, casual for brainstorming). Auto-generated SOUL.md from user interaction patterns. Validation tooling to detect conflicts between SOUL.md values and skill-specific instructions.

## Potential Failure Modes
SOUL.md bloat — max ~20K chars before truncation risks losing critical identity instructions. Identity instructions can conflict with skill-specific requirements, creating unpredictable behavior. Not a security mechanism — should never be used for access control, only behavioral guidance.
