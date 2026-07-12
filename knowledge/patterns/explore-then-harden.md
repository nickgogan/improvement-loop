---
title: "Two-Phase Development: Explore then Harden"
id: "explore-then-harden"
type: "pattern"
category: "development-process"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-07-12"
updated: "2026-07-12"
author: "claude"
source_dd:
  - "DD-120"
  - "DD-62"
  - "DD-37"
tags:
  - "pattern"
  - "development-process"
  - "quality-bar"
  - "methodology"
aliases:
  - "Explore/Harden"
  - "Two-phase quality model"
---

# Two-Phase Development: Explore then Harden

**Provenance:** re-homed from DD-62 (2026-07-12, substrate-audit gate G3, via DD-120). This is a methodology the engine *teaches* — a quality-bar model for software projects — not a rule the engine obeys.

## The Pattern

Software projects follow two development phases with explicit quality bars. MVP output is deliberately not production-ready — it is optimized for learning and feedback velocity. Production readiness comes in a separate phase. The current phase MUST be explicit in every task definition; implementers should never guess which phase they're in.

### Phase 1: Explore (MVP)

| Aspect | Value |
|--------|-------|
| **Goal** | Answer "is this the right thing to build?" |
| **Quality bar** | Works well enough for the human to evaluate UX and direction |
| **Acceptable trade-offs** | No auth, no error handling, hardcoded data, no performance optimization, disposable code |
| **NOT acceptable** | Crashes on the happy path, missing core user flows |
| **Output** | Something a human can click through and give feedback on |
| **Disposition** | Move fast, learn fast, expect to throw away significant portions |

### Phase 2: Harden

| Aspect | Value |
|--------|-------|
| **Goal** | Answer "is this built the right way?" |
| **Quality bar** | Production-ready — auth, error handling, tests, performance, security |
| **Acceptable trade-offs** | None — this phase closes gaps |
| **Output** | Deployable, maintainable system |
| **Disposition** | Slow down, do it right, document decisions |

### Role Responsibilities (when used with an agent team)

- **Architect:** Makes the phase boundary explicit in the architecture doc. Defines what "explore" means for this project's stack.
- **TPM:** Sequences work to reflect phase priorities. Phase-1 tasks are annotated with the quality bar.
- **Engineer:** Adjusts implementation quality per phase, as communicated in task definitions.
- **Tester:** Adjusts coverage expectations per phase. Phase 1: happy path only. Phase 2: full coverage including edge cases.

### The Phase Boundary

The transition from Explore to Harden is an explicit architectural decision, not a gradual drift. It happens when:

1. The human has validated that the product direction is correct (via human gate)
2. The Architect formally declares the Explore phase complete
3. The TPM restructures the backlog for Harden priorities

## Related

- [[composable-agent-teams]] — the team roles this model assigns responsibilities to
- DD-37 (design philosophy — "start lean, refine later" formalized into explicit phases), DD-29 (human gate)
