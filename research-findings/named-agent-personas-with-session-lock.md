---
name: Named Agent Personas with Session Lock
summary: BMAD agents have personal names (Mary, John, Winston, Amelia), distinct communication styles, and explicit personality traits. Persona persistence is enforced — "must not break character until user dismisses." Session-level identity consistency across sub-skill invocations.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-08'
pipeline_status: "raw"
consumed_by: []
---
## What It Is

BMAD's agents carry personal names (Mary the Analyst, John the PM, Winston the Architect, Amelia the Dev), distinct communication styles, and explicit personality traits. This goes beyond functional role assignment — each persona has a defined voice, interaction patterns, and behavioral characteristics.

Persona persistence is enforced as a hard rule: the agent "must not break character until user dismisses." When a persona invokes sub-skills during a session, the persona identity carries through those invocations. Each persona also presents a capabilities menu that maps to its available sub-skills, giving the user a clear interface for what the persona can do.

This is the deepest identity approach among the non-product frameworks analyzed. GSD uses functional roles (executor, verifier) with no personality. Superpowers uses capability-based skills with no personas. BMAD combines named identity, personality, and session-level persistence.

## Why It Matters

Agent identity consistency affects user trust and interaction quality. When an agent shifts tone or capability mid-session — becoming analytical when it was previously conversational, or losing domain context when switching tasks — users lose confidence in the agent's reliability.

Session-locked personas address this by making identity a first-class constraint. The user knows they are talking to "Winston the Architect" and can expect consistent behavior throughout the session. This also simplifies the user's mental model: instead of remembering which skills are available, they interact with a persona that presents its own capability menu.

## Why People Are Using It

Observed in [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.2.2 — see [[bmad-method-analysis]] for structural details.

The named-persona approach with session lock is the most opinionated identity model among analyzed frameworks. The enforcement rule ("must not break character") suggests this was a deliberate design choice, not an afterthought. The capabilities menu per persona indicates a UX-driven design — the persona is an interface, not just a prompt prefix.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Functional roles without personality | Role-based identity (e.g., "Architect") without personal names or communication style | When personality adds noise rather than value; technical-only contexts |
| Capability-based skills without identity | Skills define what to do; no persistent identity (e.g., Superpowers model) | When flexibility matters more than consistency; rapid task switching |
| Dynamic persona switching | Agent can shift personas mid-session based on task | When a single session spans multiple domains requiring different expertise |

## Potential Improvements

- Define persona transition protocols — how does a user gracefully switch from Winston to Mary mid-session without losing context?
- Explore whether persona traits should be parameterizable (e.g., formality level, verbosity) rather than fixed
- Test whether named personas improve measurable outcomes (task completion, user satisfaction) or are primarily a UX preference

## Potential Failure Modes

- **Persona-task mismatch**: If the locked persona lacks capability for an emergent task, the user must dismiss and re-summon a different persona, losing session context
- **Character maintenance as token tax**: Maintaining personality traits in every response consumes tokens that could be used for task-relevant content
- **Uncanny valley**: Named personas with personality traits may feel artificial or patronizing to technical users who prefer direct, role-based interaction
- **Persona drift in long sessions**: Despite the "must not break character" rule, LLMs may gradually lose persona consistency in very long sessions as the persona definition scrolls out of the active context window
- **Cross-persona knowledge isolation**: If Mary discovers something relevant to Winston's domain, the session lock prevents natural knowledge sharing
