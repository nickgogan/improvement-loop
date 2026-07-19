---
name: Five-Pattern Multi-Agent Communication Taxonomy (Delegation / Creator-Verifier / Direct / Negotiation / Broadcast)
summary: |-
  Alvoeiro (Factory): a five-pattern classification of how agents can communicate,
  offered against the field's terminology sprawl. Delegation — one agent spawns another,
  gets a response back; simplest, most common. Creator-verifier — one agent builds, a
  separate stakeless agent checks; same cost-bias logic as human code review. Direct
  communication — agents message each other with no central coordinator; hard to get
  right because state fragments across conversations with no single source of truth.
  Negotiation — agents communicate over a shared resource (same API, same code region);
  not inherently adversarial, best case is positive-sum. Broadcast — one agent sends
  information to many (status, new context, constraints); unglamorous but critical for
  coherence over long-running tasks. Factory's own production system (Missions) composes
  four of the five — delegation, creator-verifier, broadcast, negotiation — deliberately
  omitting direct communication as the coordination primitive.
implementation_notes: |-
  Directly useful as a design-review lens for agents/handoff-protocol.md and any future
  IL multi-agent skill — worth an explicit pass classifying the Owner/Researcher/
  Codifier/Librarian handoff protocol against these five patterns to surface which one it
  actually is (currently reads as delegation plus broadcast via file-mediated
  pipeline_status, with no direct communication).
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- multi-agent-architecture-that-actually-ships.md
related_findings:
- file: legitimate-multi-agent-domains-taxonomy.md
  rel: same-problem
- file: agent-teams-shared-communication-channel.md
  rel: same-problem
- file: agent-management-tool-landscape-2026.md
  rel: same-problem
- file: builder-validator-chain-pattern.md
  rel: extends
- file: missions-three-role-architecture-serial-targeted-parallelization.md
  rel: enables
- file: flat-parentless-cross-model-agent-communication.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
---

## What It Is

A five-pattern classification of how agents can communicate in a multi-agent system,
offered as a response to the field's terminology sprawl ("everyone has their own
framework, their own terminology, their own opinions of what works and doesn't work").
**Delegation** — one agent spawns another with a task and gets a response back; the
simplest form, and what most people implement first (standard sub-agent usage).
**Creator-verifier** — one agent builds something, a separate agent with no stake in the
outcome checks it; motivated by the same cost-bias logic as human code review — the
builder wants its own code to work, so a fresh agent is more likely to find issues.
**Direct communication** — agents message each other without a central coordinator;
explicitly flagged as hard to get right because state fragments across conversations
with no single source of truth. **Negotiation** — agents communicate over a *shared
resource* (the same API, the same portion of the codebase); not inherently adversarial —
the best case is a net-positive-sum, win-win interaction. **Broadcast** — one agent sends
information to many (status updates, new context that applies to everyone, shared
constraints); framed as less flashy than the others but critical for maintaining
coherence over long-running tasks. Factory's own production system, Missions, composes
four of the five — delegation, creator-verifier, broadcast, and negotiation — into a
single workflow, deliberately not using direct communication as its coordination
primitive.

## Why It Matters

The KB already has a task-characteristic taxonomy (legitimate-multi-agent-domains-taxonomy.md:
which *tasks* suit multi-agent orchestration) and one named communication mechanism
(agent-teams-shared-communication-channel.md: a specific direct-communication
implementation). This finding supplies the missing orthogonal axis — not "should this
task use multiple agents" but "given multiple agents, which of five structurally
distinct ways should they talk to each other" — and gives each option a named failure
mode, which the existing shared-channel finding lacks (its own failure-modes section is
speculative; this taxonomy explains *why* direct communication specifically is hard: no
coordinator means no single agent holds cross-conversation state). Any future IL
multi-agent design has a vocabulary to reason about which pattern a given interaction
actually needs, rather than defaulting to whichever is easiest to implement (delegation).

## Why People Are Using It

Offered as Factory's own working vocabulary, arrived at "when you start researching
multi-agent frameworks and systems you quickly realize the field's a bit of a mess" — a
practitioner's synthesis rather than an academic taxonomy, validated by being the design
vocabulary underneath a system (Missions) running 16-30 day production workloads for real
customers.

## Potential Alternatives

- **Task-characteristic taxonomy alone** (legitimate-multi-agent-domains-taxonomy.md):
  answers whether to use multiple agents, not how they should talk; complementary to this
  taxonomy, not a substitute for it.
- **No named taxonomy, ad hoc per-system design:** the default across most of the
  ecosystem per this source's own framing; loses the ability to reason about why a given
  interaction is failing (e.g., recognizing "this is failing because we're doing direct
  communication without a coordinator" rather than treating it as an unnamed bug).

## Potential Improvements

- A decision rubric mapping interaction shape to recommended pattern (e.g., "two agents
  sharing a mutable resource → negotiation, not direct communication") — the taxonomy
  names the options but doesn't yet prescribe selection criteria beyond the Missions
  example.
- An explicit cost/complexity ranking across the five patterns (delegation and broadcast
  read as cheapest; direct communication and negotiation read as most expensive) —
  implied in the talk but not stated as a ranked list.

## Potential Failure Modes

- **Under-fit categories:** real systems may need a pattern that blends two (e.g.,
  negotiation with an occasional broadcast escalation), and forcing a single label
  obscures that.
- **Unproven exhaustiveness:** the taxonomy is descriptive of what Factory built, not
  proven exhaustive — a sixth pattern (e.g., auction/market-based allocation) may exist
  and simply not have come up in this talk's framing.
