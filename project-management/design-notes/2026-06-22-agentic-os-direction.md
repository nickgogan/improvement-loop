---
title: "Agentic-OS direction — IL as a governance-first agentic-system factory"
id: "agentic-os-direction"
type: "design-note"
category: "architecture-direction"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-06-22"
updated: "2026-06-22"
author: "claude"
tags:
  - "design-note"
  - "direction"
  - "agentic-os"
  - "harness"
  - "governance"
  - "scope"
---

# Agentic-OS direction

> **Status: direction capture, not a decision.** Nick's session-129 brain-dump, organized.
> No DD, no IB, no artifact is created on this note. It records where the engine is heading so
> the next session (the **user manual**) can pin scope. The vision will be ground-truthed against
> external research (named below) before any of its abstractions are committed (DD-36, Rule 11).

## The thesis

IL is being formalized from "research engine + per-artifact assess/design advisory layer" toward
**something closer to an agentic OS**: a system with a formal **harness** layer that helps **audit,
specify, and create whole agentic systems** — governance-first — not just individual skills/agents.

This is the promotion of an item that was already **Logged-for-future #1** ("place the engine on an
actual harness, not just relying on the agent to invoke the right skills in the right order every
time") to active direction, and the naming of its endpoint. It aligns with the **supervised-autonomy
trajectory in DD-108**.

Nick's own caveat: the term "agentic OS" is used provisionally ("I think I'm using this term
correctly") — validating/defining it is one of the open research questions below.

## Expanded mission of the advisory layer

The engine should help **audit, specify, and possibly create** the full agentic-system surface, not
only skill/agent/prompt:

- skills, agents, **workflows**, whole **agentic systems**
- components: **memory structures**, **harnesses**, **loops between harnessed agents**, **evals for
  skills**, **rules**, **templates**
- much of this is partly captured today in **extracts**, schematics, and the `/design-*` / `/assess-*`
  / `/audit-artifacts` skills — the work is unification + elevation, not greenfield

## Governance-first creation model

When IL creates something, it should **start with a governance layer**, because *everything we build
is an agentic system* — even a coding agent producing traditional software:

- **vision + mission** → the *what*
- **mission + purpose + values** → the *why* (values are pursued for their own sake)
- **principles** → the *how*
- this high-level governance flows down to every agent in the system being created
- *[resolved 2026-07-16, Phase 4 interview Block 0: the "Division, to a degree" fragment was
  garbled transcription noise — nothing intended. The governance stack is complete as listed:
  vision/mission/purpose/values/principles.]*
- **`actors.md`** (in the governance directory of the target repo) is therefore always present: it
  specifies the **LLM actors** — agents, task boundaries, permission sets, skills, **souls**,
  dispositions. (Much of this content already lives in agent templates / agent.md Constitution.)

## Formal assets repository / catalog

IL should have a **formal assets repository/catalog** of its own reusable components — a registry, not
just folders. It catalogs the full asset set: **skills, agents**, and (per the expanded mission)
workflows, memory structures, harnesses, evals, rules, templates. This is the structural home for:

- the **skills directory** and **agents directory** (see skill model below);
- the **skill↔model-coupling metadata** (creation/update dates, authoring/validated model version) —
  a catalog is where that metadata stays queryable and where model-drift risk becomes visible;
- **provenance** for extracts/schematics (the what+how pairing below), so a consumer can find, compare,
  and reuse an asset rather than re-deriving it.

The catalog is the retrieval/reuse surface of the agentic OS. Open: is it a directory convention, a
frontmatter-indexed registry (like the DD/IB corpus), or a generated view? Resolve against the #8
taxonomy/clustering repo before committing a form (Rule 11).

## Skill model refinements (today's narrower thread, folded in)

- **Skills belong to a governed agent.** A skill within a system should always belong to an agent that
  is aligned with and governed by that system. The skills/agents directories above make this
  structural.
- **Model coupling is real.** Skills carry structural-functional metadata, including the **model
  version** a skill was authored/validated against — changing models can drastically change skill
  behavior. This skill↔model coupling must be tracked (creation/update dates + model version).
- **Skills have named clauses**, and different LLMs respond to different structuring/formatting of
  them: name, description, purpose, workflow/procedure, examples, success criteria, things-to-watch,
  permission boundaries, reference files.
- This supersedes the narrow "fold capability-type-selection into DD-109" plan from earlier in the
  session — the agent-vs-skill routing question is now a sub-question of this larger model. **The
  DD-109 fold is on hold** (do not edit that foundational DD until the larger model settles).

## What + how delivery model (extract minimum-structure clue)

Each IL output pairs a **"what"** (a **schematic** of the desired artifact) with a **"how"** (an
**excerpt** from guides / patterns / templates that guides construction). Extracts are consumable
three ways, which suggests a **minimum structure** for extracts:

1. imported and used **as-is**
2. **adapted** to the consumer's context
3. **reconstructed** from a template

## Research dependencies (must ground before committing structure)

Per DD-36 (evolution via research) and Rule 11 (abstractions earn their keep), ground the above in:

- **[NEED REPO NAME from Nick]** — a repo to examine for **directory taxonomy / clustering** (how to
  structure the skills/agents/components directories).
- **BMAD** (already a watched library) high-level skills, possibly augmented with **superpowers** and
  **taches** (*"attachés" resolved 2026-07-16, Phase 4 Block 0: transcription of `taches` — the
  `taches-cc-resources` watched library, already tracked and analyzed*); **critical-thinking skills**
  for generating high-level agentic-system *governance* and *product* layers (PRD, architecture). May
  need modification to fit our needs. The agentic system should always have a workflow **similar to
  Archon**.
- **Nate B Jones' "open skills framework"** (newly released) — introduces the same abstraction we'd be
  learning from.

## Open conceptual questions

- Define and distinguish: **agentic layer** vs **orchestration layer** vs **agentic OS**.
- Are **governance** and **permissions** their own layers, or cross-cutting features that fold into
  governance and show up across multiple layers?

### Sharpening from the Databricks comparison (session 129, post-compact)

Nick asked how to think about **Databricks' agent orchestration (Agent Bricks)** vs an **agentic OS**
vs an **agent with a second brain**. The frame that emerged — three answers to three different
questions, discriminated by **unit of governance**:

| | Unit of governance | Time of action | Center of gravity |
|---|---|---|---|
| Second-brain agent (Letta, mem0) | one agent's state | runtime | the agent's memory |
| Orchestration platform (Agent Bricks) | data + tool **access** | runtime/ops | the lakehouse |
| Agentic OS (IL direction) | agent **identity & intent** | design-time + runtime | constitution + asset catalog |

Implications adopted into this direction:

1. **Orchestration is a subsystem of an agentic OS** (the scheduler, in the OS metaphor), not a peer
   layer. Databricks shows the scheduler + access-security model ships commercially *without* the
   constitution — access governance (Unity Catalog: permissions, lineage, audit, rate limits) has no
   home for intent governance (vision/mission/values/principles, actors, souls, dispositions). That
   gap is the layer IL's model occupies. Partially resolves the first open question above.
2. **Compositional, not competing.** An agentic OS could deploy onto an orchestration substrate:
   actors.md compiles to permission sets, the assets catalog registers into their MCP tool catalog,
   specified memory structures provision as managed memory (their Lakebase). Nesting: second brain ⊂
   agent ⊂ agentic OS ⊂ (optionally) enterprise orchestration substrate.
3. **External validation of the asset list.** Databricks independently converged on nearly the same
   component inventory — catalog, evals, governance, memory, orchestration, harness (their Omnigent
   "runs your agents above the harnesses you already use — Claude Code, Codex"). Rule-11-grade
   evidence that these abstractions are real, and that intent-governance is the differentiator.

Sources (not yet in KB; Databricks has **zero KB coverage** as of this note — no watched-library,
source, or finding entries): databricks.com/product/artificial-intelligence/agent-bricks (2026-06),
docs.databricks.com/aws/en/generative-ai/agent-bricks (2026-03), makerpulse.ai GA analysis (2026-02),
databricks.com supervisor-architecture blog (2026-03). Note: Agent Bricks is a proprietary product,
not an open repo — intake fits **research-source / watched-blog**, not `/repo-analyzer`.

## Next step

**Session 130: write the user manual for this system.** Nick's rationale: the manual will force scope
and direction to crystallize — it is the cheapest instrument for bounding everything above before any
of it is built.
