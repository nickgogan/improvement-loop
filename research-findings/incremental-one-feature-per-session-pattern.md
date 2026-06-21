---
name: Incremental One-Feature-Per-Session Execution
summary: Strict prompting limits each agent session to implementing exactly one feature before leaving the codebase in a clean, mergeable state. Progress tracking via artifacts (progress file + git history)
  enables fresh-context sessions to pick up where the last left off.
implementation_notes: Directly applicable to MetaSystem's relay-race architecture. Each session should have a single focused objective with explicit clean-state criteria.
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- anthropic-effective-harnesses-long-running-agents.md
related_findings:
- file: ralph-wiggum-execution-pattern.md
  rel: same-problem
- file: progress-md-session-bridge.md
  rel: enables
- file: initializer-agent-scaffolding-pattern.md
  rel: enabled-by
- file: marathon-vs-relay-race-plugin-architecture.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
  - "agent-design-patterns.md"
  - "session-persistence-and-memory.md"
---

## What It Is

Each coding agent session is prompted to: (1) read the progress file and git history to understand current state, (2) select and implement exactly one feature from the feature list, (3) leave the codebase in a "clean state" -- defined as production-mergeable with no major bugs, orderly code, and documentation updated, and (4) update the progress file for the next session. Context is fully reset between sessions to prevent context anxiety and accumulation.

## Why It Matters

Agents overload sessions by tackling too much, exhausting context, or leaving unclean states that poison subsequent sessions. The one-feature constraint bounds scope per session, and the clean-state requirement ensures every session handoff is safe. This is the operational instantiation of the "relay race" architecture with explicit baton-passing.

## Why People Are Using It

Anthropic documents this as the core coding agent pattern in their harness for multi-hour autonomous builds. Combined with full context resets, it prevents the "context anxiety" behavior where models prematurely wrap up as the context window fills. The pattern yielded complete application builds (claude.ai clone) across many sequential sessions.

## Potential Improvements

Automatic feature selection based on dependency ordering rather than agent judgment. Validation that the codebase is actually in a clean state (automated tests, lint) before the session ends.

## Potential Failure Modes

Feature selection bias -- agents may repeatedly pick easy features, leaving hard ones for later where they compound. The "clean state" definition may be too vague without concrete verification criteria. Single-feature constraint may be too restrictive for tightly coupled features that must be implemented together.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[one-feature-per-session.md]] in `extracts/patterns/`
