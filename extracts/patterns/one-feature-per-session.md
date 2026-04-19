---
title: "One Feature Per Session"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "incremental-one-feature-per-session-pattern"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A progress file (PROGRESS.md or equivalent) exists and is current. A feature list or backlog with discrete, independently implementable items is available. Clean-state criteria are defined — the agent knows what 'mergeable with no major bugs' means concretely (tests pass, linter clean, documentation updated)."
  invariants: "Each session implements exactly one feature — no scope creep, no 'while I'm here' additions. The codebase is in a clean, mergeable state at session end — verified by automated checks, not self-assessment. The progress file is updated at session end with what was done and what comes next. Context is fully reset between sessions — no carryover state."
  governance: "Nick owns the feature list and priority ordering. The agent selects the next feature from the list but does not reorder priorities or skip items without authorization. Clean-state verification criteria are defined by Nick and enforced automatically."
  recovery: "If the agent cannot complete the feature within the session's context budget, it leaves the codebase in a clean state with the partial work either committed behind a feature flag or reverted — never in a broken intermediate state. If clean-state verification fails at session end, the agent fixes the violations before closing — the session does not end until the codebase is clean. If feature selection proves wrong mid-session (blocked by a dependency), the agent documents the blocker in the progress file and selects an alternative, rather than attempting a partial implementation."
tags:
  - "extracted-artifact"
  - "pattern"
---

# One Feature Per Session

**Source:** [[incremental-one-feature-per-session-pattern]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent sessions that attempt to implement multiple features exhaust their context window, leave the codebase in inconsistent intermediate states, and produce handoff points that are difficult for subsequent sessions to resume from. As context fills, agents exhibit "context anxiety" — prematurely wrapping up or rushing through remaining work. The result is fragile, partially complete implementations that poison downstream sessions.

## Forces

- **Scope vs. progress.** Implementing more per session feels like faster progress, but overloading sessions produces lower-quality output and harder handoffs.
- **Feature coupling vs. independence.** Some features are tightly coupled and feel like they "should" be done together. But attempting coupled features in one session risks both being half-done rather than one being fully done.
- **Context freshness vs. continuity.** Full context reset between sessions prevents context rot and anxiety, but requires a reliable handoff mechanism to avoid losing progress knowledge.
- **Clean state cost vs. speed.** Leaving the codebase in a verified clean state at session end takes time — running tests, updating docs, cleaning up experiments. Skipping this is faster but creates technical debt for the next session.

## Solution

Constrain each agent session to implementing exactly one feature, with explicit clean-state requirements and progress tracking for session continuity.

**Session protocol:**

1. **Read the progress file and git history.** The agent orients itself by reading PROGRESS.md (or equivalent) and recent commits to understand current state. No carryover context from previous sessions — everything needed is in these artifacts.

2. **Select exactly one feature.** From the feature list or backlog, the agent picks one discrete item. If dependencies block the intended feature, select an alternative rather than attempting partial work.

3. **Implement the feature.** Full implementation including tests, documentation updates, and integration with existing code.

4. **Leave the codebase in a clean state.** Clean state is defined concretely: all tests pass, linter is clean, documentation is updated, code is production-mergeable. This is verified by automated checks (running the test suite, linter), not by self-assessment.

5. **Update the progress file.** Record what was completed, what was deferred, any blockers encountered, and what the next session should tackle. This is the baton in the relay race.

6. **Full context reset.** The next session starts fresh with zero carryover context. The progress file and git history are the sole bridge between sessions.

**Key mechanics:**

- The one-feature constraint is a prompt-level instruction reinforced by the session structure — the agent is told to select one item and stop.
- Clean-state verification must be automated (test suite, linter, type checker) to avoid the agent self-assessing its own output quality.
- The progress file is a structured artifact, not free-form notes. It should contain: completed items, next items, blockers, and any context the next session needs.
- Feature selection should follow dependency ordering from the backlog, not agent preference. Agents left to choose freely will pick easy features, leaving hard ones to compound.

## Consequences

**Positive:**
- Bounded scope per session prevents context exhaustion and the quality degradation that accompanies it.
- Clean-state guarantee at every handoff means no session inherits a broken codebase.
- Full context reset prevents context rot and "context anxiety" behavior.
- Relay-race architecture scales to arbitrarily long projects across many sequential sessions.
- Each session produces a discrete, reviewable, mergeable unit of work.

**Negative:**
- Single-feature constraint may be too restrictive for tightly coupled features that must be implemented together.
- Feature selection bias — agents may repeatedly select easy features, deferring hard ones where they compound.
- Clean-state verification takes time at the end of every session — this is a real cost, not overhead to be optimized away.
- The progress file becomes a critical single point of failure — if it's incomplete or inaccurate, the next session starts with a wrong understanding of state.

## Known Uses

- **Anthropic harness for long-running coding agents** (April 2026): Core pattern for multi-hour autonomous builds. Combined with full context resets, yielded complete application builds (claude.ai clone) across many sequential sessions.
- **MetaSystem relay-race architecture:** The session-handoff skill and PROGRESS.md are the operational instantiation of this pattern. Each session reads PROGRESS.md, does focused work, and updates it for the next session.
- **Ralph Wiggum Execution Pattern** (related finding): A variant where the agent is instructed to "do one thing and do it well" with explicit completion criteria.

## Contract

### Preconditions

- A progress file (PROGRESS.md or equivalent) exists and is current.
- A feature list or backlog with discrete, independently implementable items is available.
- Clean-state criteria are defined — the agent knows what "mergeable with no major bugs" means concretely (tests pass, linter clean, documentation updated).

### Invariants

- Each session implements exactly one feature — no scope creep, no "while I'm here" additions.
- The codebase is in a clean, mergeable state at session end — verified by automated checks, not self-assessment.
- The progress file is updated at session end with what was done and what comes next.
- Context is fully reset between sessions — no carryover state.

### Governance

- Nick owns the feature list and priority ordering.
- The agent selects the next feature from the list but does not reorder priorities or skip items without authorization.
- Clean-state verification criteria are defined by Nick and enforced automatically.

### Recovery

- If the agent cannot complete the feature within the session's context budget, it leaves the codebase in a clean state with partial work either committed behind a feature flag or reverted — never in a broken intermediate state.
- If clean-state verification fails at session end, the agent fixes the violations before closing — the session does not end until the codebase is clean.
- If feature selection proves wrong mid-session (blocked by a dependency), the agent documents the blocker in the progress file and selects an alternative rather than attempting a partial implementation.
