---
title: "Agent Rules — IL Governance"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-19"
updated: "2026-06-21"
author: "agent"
source_dd:
  - "DD-37"
source_governance:
  - "CHARTER.md"
  - "systems/improvement-loop/knowledge/reference/fractal-pattern.md"
  - "systems/improvement-loop/knowledge/reference/vocabulary.md"
source_sections:
  - "Design Philosophy (consumer feedback to producer)"
  - "The Agentic Layer"
  - "Agent & Skills vocabulary"
  - "DD-37 (five foundational design principles)"
  - "DD-91 (reflections-to-proposals pipeline)"
tags:
  - "governance"
  - "improvement-loop"
  - "agents"
  - "skills"
  - "reflections"
---

# Agent Rules — IL Governance

> Derived from: Charter (`CHARTER.md`), Fractal Pattern (`systems/improvement-loop/knowledge/reference/fractal-pattern.md`), Vocabulary (`systems/improvement-loop/knowledge/reference/vocabulary.md`), DD-37 (foundational design principles), DD-89 (four-zone architecture), DD-91 (reflections-to-proposals)
> Last reconciled: 2026-06-21

## Foundational Design Principles (DD-37)

> Apply these five heuristics **before** consulting any system-specific DD. They are the constitution-altitude design philosophy that governs the engine; the numbered Rules below operationalize agent structure and behavior on top of them. (Cached here per the DD-wisdom caching policy, DD-121 — cross-cutting, reference-shaped, engine self-knowledge, stable; `source_dd: DD-37`.)

1. **Spec before build.** Design the architecture before writing code or configuring anything. A spec precedes every implementation. (If this conflicts with "start lean," the resolution is: write a *lean* spec, then build.)
2. **Complementary tools, not redundant ones.** Every tool, skill, or abstraction serves a unique purpose; none should duplicate another's primary function. (Generalizes into rule 11 — abstractions earn their keep.)
3. **Knowledge serves expression.** Knowledge is captured to fuel action, not for its own sake. Every capture should have a plausible path to use.
4. **Start lean, refine later.** Deploy the simplest version that works; add complexity only when the simple version demonstrably fails.
5. **Shallow vs. deep thinking distinction.** Match tool/model power to task depth — shallow processing (triage, routing) vs. deep processing (architecture decisions, creative work).

## Rules

1. **Agent-as-directory.** Each agent is a directory under `agents/` containing at minimum an `agent.md` definition file. The directory can grow to include `skills/`, `workflows/`, `templates/`, and `hooks/` as needs emerge. This follows the fractal pattern's agentic layer.
   - *Source:* Fractal Pattern — The Agentic Layer

2. **Every agent has a constitution.** The `agent.md` file defines: Core Truths, Boundaries, Vibe, Continuity, Disposition, Scope, Autonomy Table, Skill Inventory, Communication, and Contract. These sections are mandatory — an agent without a constitution is not a deployed agent.
   - *Source:* Fractal Pattern — The Agentic Layer; DD-86 (Owner pattern)

3. **Skills define agent behavior.** An agent's capabilities are expressed through skills (SKILL.md files in `.claude/skills/`). Each skill has a cognitive disposition, procedure, rules, and allowed tools. When a skill is loaded, the agent's disposition shifts to match.
   - *Source:* Vocabulary — Cognitive Disposition, Access Model, Scope Boundary

4. **Read/write boundaries are per-agent.** Each agent has defined read and write scopes in its Communication section. The Researcher writes findings, sources, authorities, watched-libraries, watched-blogs, operations/, and its own reflections. The Codifier writes to extracts/, operations/, project-management/design-notes/, and its own reflections. The Librarian is read-only on the KB with a narrow write exception for its own reflections. The Owner writes governance/, docs, SL entries, audit reports, and its own reflections. Agents do not write outside their scope.
   - *Source:* Constitution — Boundary Rules; DD-30, DD-80, DD-89 (four-zone architecture — design-and-governance artifact placement by shape, not author role)

5. **Consumer feedback to producer.** When one agent consumes another's output and finds gaps, the consumer provides feedback — concrete gaps and natural language critique. Feedback goes to `feedback/` for the Owner to triage. This applies to both agent-to-agent and human-to-agent feedback.
   - *Source:* Constitution — Design Philosophy ("Consumer feedback to producer")

6. **Agents are peers, not hierarchical.** The Owner maintains agent constitutions (proposal-first) and system health, but does not supervise other agents at runtime. Each agent operates within its own scope and autonomy. No agent can modify another agent's constitution unilaterally.
   - *Source:* Owner Constitution — Boundaries ("NEVER promote your own autonomy tiers"); Out of Scope ("Runtime supervision")

7. **Engine definitions are subsets.** The `.claude/agents/` directory holds engine-facing subagent definitions (consumed by Claude Code). These are subsets of the full `agents/{name}/agent.md` definitions. Both coexist — the fractal `agents/` directory is canonical.
   - *Source:* Fractal Pattern — Relationship to Engine Directories

8. **Agent-private reflections boundary.** Each agent writes exclusively to its own `agents/{name}/reflections/` directory for self-reflection artifacts. Reflections are append-only (one file per reflection event) and privacy-restricted by convention — only the reflecting agent and the system's Owner read them during `/solicit-proposals` rounds. Cross-agent reflection reads are forbidden. Nick reads all. A reflection records the agent's self-assessment over a defined period: vision/mission/constitution review, effectiveness, efficiency, felt gaps, help needed, free-form commentary. Primarily free-form; a suggested scaffold exists but is not enforced.
   - *Source:* DD-91 (reflections-to-proposals) — implementation obligation 6

9. **Proposals flow to `governance/proposals/` via two pathways.** Agent-initiated proposals originate either from an Owner-run `/solicit-proposals` round (structured) or from an individual agent's own initiative (ad-hoc). Both flow to `governance/proposals/`; both face Nick's review at acceptance time (not mid-flow); both convert to IB items on acceptance. Owner + Nick collaborative governance work bypasses this path and writes DDs directly.
   - *Source:* DD-91 (reflections-to-proposals) — dual proposal pathways; DD-89 (four-zone architecture) — `governance/proposals/` zone definition

10. **Generator-assessor separation.** The agent or skill that generates an artifact must not be the same one that assesses it. Generation and assessment are distinct operations with distinct end-goals, motivations, and dispositions — a generator optimizes for "produce something that satisfies the spec," an assessor optimizes for "find where this fails the criteria." Conflating them collapses the epistemic gap that makes assessment meaningful. Operationally: any constructive skill that includes a quality check must delegate the check to the corresponding assess-* skill invoked as a separate subagent (fresh context, assessor disposition loaded cleanly). This applies symmetrically — an assessor must not also produce the artifact it is checking.
    - *Examples:* `design-skill` invokes `/assess-skill` as a subagent before presenting its draft; `design-agent` invokes `/assess-agent`; future `/extract-artifacts` runs that include quality verification delegate to the relevant assess-* skill rather than self-checking.
    - *Source:* Standing rule established session 106 (2026-05-30) during Owner skill design. Elaborates and specializes rule 5 (consumer feedback to producer) for the self-assessment case.

11. **Abstractions must earn their keep.** Every new abstraction or layer proposed within the IL system must be backed by strong evidence that it is needed. This includes new concept docs, agent roles, pipeline stages, composition layers, governance rules, tiers, taxonomies, or shared infrastructure. Abstractions justified only by elegance, symmetry, completeness, or "we might want this later" are rejected. Concrete duplication and one-off patterns are preferred to speculative abstraction — the cost of an unused or wrongly-shaped abstraction is paid every time someone reads the system, not just when it was written.
    - *What counts as evidence:* a recurring concrete problem observed at least 2–3 times; multiple consumers that demonstrably benefit; an observable cost of *not* having the abstraction (duplication that has actually caused drift, ambiguity that has actually caused mistakes, decisions that have actually been re-litigated).
    - *Operational guidance for all IL agents:* When proposing any new abstraction, lead with the evidence (occurrences, consumers, cost-of-absence). If evidence is thin, prefer tolerating the concrete duplication and flag for revisit rather than abstracting now. When in doubt: don't abstract.
    - *Source:* Standing rule established session 106 (2026-05-30). Architectural specialization of the broader minimum-viable-abstraction stance; complements rule 10 by constraining what gets built in the first place, not just how it gets validated.

12. **Audit-design symmetry.** For every artifact type the Librarian operates on (skill, agent, prompt, harness, etc.), the audit operation and the design operation compose against the same concept doc. Audit consumes §Composition (which guides' Contract sections form the rubric); design consumes §Construction (which authoring substrate forms the procedure). The two operations are bilingual readings of one substrate. When one operation is extended for an artifact type — adding a new concept doc, adding a §Construction subsection, adding a §Composition row — the symmetric operation's coverage of that artifact type must be evaluated in the same change.
    - *Why this matters:* a concept doc with §Composition but no §Construction is auditable-but-not-constructible (the Librarian can find faults but can't help you author); the inverse is constructible-but-not-auditable. Both gaps create asymmetric capability and silently drift the Librarian's coverage map.
    - *Operational guidance for all IL agents:* When proposing new concept docs or extending existing ones, build §Composition and §Construction together. When extending §Composition (adding a guide to a row, refining a precondition), check whether §Construction's Decision sequence references the same gate; if not, update both. When extending §Construction (adding a step, adding an anti-pattern), check whether §Composition's invariant set names the symmetric audit gate; if not, update both.
    - *Existing §Construction debt:* As of session 107, only `skill.md` and `agent.md` carry §Construction. Other concept files in `operations/references/librarian/` (`harness.md`, `second-brain.md`, `memory.md`, `context-rot.md`, `agentic-systems.md`, `prompt.md`, others) carry §Composition only and are in §Construction debt — auditable but not constructible. Filing a §Construction pass is tracked as IB work, not a blocker; existing concept docs do not need backfilling before unrelated work proceeds.
    - *Source:* Structural prerequisite for rule 10 to function correctly at the concept-doc level — audit and design can only achieve generator-assessor separation if both operations read from the same concept doc. Relates to rule 11 (abstractions must earn their keep): a concept doc that supports only one of the two Librarian operations has not fully earned its abstraction cost. Standing rule established session 107 (2026-06-11) during IL Stream 0 step A (design.md spec landing).

## Applicability Notes

These rules apply to all four IL agents. The Owner is responsible for maintaining agent constitutions and ensuring these rules are followed. Changes to agent constitutions are Proposal-First tier — the Owner drafts, Nick approves. The Owner also runs `/solicit-proposals` rounds per DD-91.
