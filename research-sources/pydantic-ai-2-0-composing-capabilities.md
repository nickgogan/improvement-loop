---
name: "Cole Medin — Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities"
source_type: "Video"
status: "Done"
key_takeaways: |-
  Walkthrough of the Pydantic AI 2.0 release, whose center is a single new primitive —
  the "capability": instructions + tools + lifecycle hooks + guardrails + model settings
  packaged as one shareable, composable unit ("the layer above MCP"). Agents become sets
  of capabilities; a capability evolved once benefits every agent that mounts it.
  Capabilities support progressive disclosure (catalog of brief descriptions always
  visible; full instructions loaded only when the agent decides it needs them — the
  skills pattern migrated into a framework primitive). The framework also splits into two
  lanes: a lean core of capabilities considered critical to most agents (thinking, web
  search, tool search) versus a named "harness" lane for supported-but-not-critical
  capabilities (e.g., code mode running in Monty, Pydantic's own lightweight open-source
  sandbox). Industry convergence datapoint for the engine's harness-layer vocabulary and
  the portable-kernel / single-implicit-agent design direction.
relevance: "High"
added_by: "Nick"
tags:
  - "orchestration"
  - "skills"
  - "tools"
  - "context-engineering"
url: "https://www.youtube.com/watch?v=PY7xIxybYNc"
authority:
  - "cole-medin.md"
findings:
  - "capability-as-agent-composition-primitive.md"
  - "lean-core-vs-harness-two-lane-framework-layering.md"
  - "skill-as-directory-progressive-disclosure-three-levels.md"
date_added: "2026-07-13"
date_processed: "2026-07-13"
date_published: "2026-07-10"
---

# Cole Medin — Pydantic AI 2.0: Composing Capabilities

Session-144 Pass 2 deep extraction (link-intake wave 3, architecture/memory cluster).
Transcript: `app/transcript-fetcher/transcripts/PY7xIxybYNc.md`.

**Watched-library flags (Nick's call, per the wave-3 triage follow-up queue — no entries
created here):** `pydantic/pydantic-ai` is a watched-library candidate if the capability
primitive warrants dependency-grade tracking; **Monty** (Pydantic's lightweight
open-source sandbox backing the code-mode capability) is a candidate in its own right.

Context from the video: Medin frames 2.0 as Pydantic AI catching up to — and passing —
the coding-agent SDKs (Claude Agent SDK, Codex SDK) that had absorbed the personal-agent
use case; the capability primitive absorbs what the industry converged on (skills, hooks,
guardrails, MCP servers) into framework-native composition. His demo shows two agents
(support bot, FAQ widget) sharing a knowledge-base capability while only one mounts
escalation, and progressive disclosure loading the escalation capability's instructions
only when a refund complaint requires it. He recommends pointing a coding agent at the
capability docs rather than hand-writing agent code. Extends the existing SDK-vs-framework
finding cluster (`sdk-vs-framework-decision-for-agent-building`,
`sdk-to-framework-graduation-path`, `skills-portability-across-sdk-and-framework-boundaries`)
without contradicting it.
