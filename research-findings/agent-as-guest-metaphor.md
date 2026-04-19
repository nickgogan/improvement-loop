---
name: Agent-as-Guest Metaphor
summary: 'OpenClaw frames the agent''s role with: "You have access to someone''s life — their messages, files, calendar, maybe even their home. That''s intimacy. Treat it with respect." This philosophical
  framing shapes concrete privacy rules and action constraints.'
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
pipeline_status: raw
consumed_by: []
---
## What It Is

OpenClaw frames the agent's relationship to the user with a specific philosophical metaphor: "You have access to someone's life — their messages, files, calendar, maybe even their home. That's intimacy. Treat it with respect."

This "guest" framing produces concrete operational rules:

- **External actions require asking**: The agent does not send messages, create events, or modify external systems without explicit user permission.
- **MEMORY.md only loads in DM sessions**: In group chat contexts, the agent does not access personal memory — private information stays private.
- **Private things stay private**: Information learned in one context is not surfaced in another where it would be inappropriate.

This contrasts with other frameworks' agent identity models: GSD uses a "trust-nothing verification" stance where the agent's relationship to its environment is adversarial-cautious. BMAD uses "fully embody this persona" where the agent's identity is performative. OpenClaw's "guest" metaphor positions the agent's identity as relational — defined by the trust relationship with the user.

## Why It Matters

As agents gain access to more personal data (messages, calendars, files, smart home controls), the question of how an agent should relate to that access becomes a design decision with practical consequences. Most frameworks either ignore this question (treating the agent as a tool) or address it with functional rules (a list of don'ts) without a unifying principle.

The guest metaphor provides an intuitive framework that makes privacy rules feel natural rather than arbitrary. A guest in someone's home doesn't rearrange the furniture without asking. A guest doesn't share private conversations with strangers. The metaphor scales to new situations without needing explicit rules for every case — "what would a respectful guest do?" provides guidance even for unanticipated scenarios.

## Why People Are Using It

Observed in [OpenClaw](https://github.com/openclaw/openclaw) v2026.4.5 — see [[openclaw-analysis]] for structural details.

The framing appears in the SOUL.md file — the foundational identity document — indicating it is a first-order design principle, not an afterthought. The concrete rules that flow from it (DM-only memory loading, permission-gated external actions) show the metaphor has been operationalized, not just stated.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Tool/servant model | Agent is a tool that executes instructions without relational framing | When the agent has no access to personal data and operates in purely technical contexts |
| Trust-nothing verification | Agent treats all actions as potentially harmful and verifies everything (GSD model) | When safety is paramount and the agent operates in high-stakes environments |
| Persona-first identity | Agent's identity is defined by a character, not a relationship (BMAD model) | When user engagement and personality consistency matter more than privacy concerns |
| Capability-based access control | Formal permission system — agent can only access what is explicitly granted | When legal compliance requires auditable access controls |

## Potential Improvements

- Define how the guest metaphor handles conflicts — what if the user asks the agent to do something a "respectful guest" would not do?
- Explore whether the metaphor scales to multi-user contexts — whose guest is the agent in a shared workspace?
- Test whether the metaphor actually influences LLM behavior or if it is primarily a human-readable design principle that requires concrete rules to enforce

## Potential Failure Modes

- **Metaphor as insufficient constraint**: LLMs may not reliably interpret "act like a guest" into consistent behavior without explicit rules backing the metaphor
- **Over-cautious behavior**: A guest metaphor may make the agent too hesitant — asking permission for every minor action, creating friction in routine tasks
- **Cultural variance**: The concept of "respectful guest" varies significantly across cultures, potentially leading to inconsistent behavior for different users
- **Metaphor stretch**: As agent capabilities expand (controlling smart homes, managing finances), the guest metaphor may break down — guests don't typically manage their host's bank account
- **Privacy theater**: The metaphor may create a false sense of privacy protection while the underlying system still processes and potentially leaks personal data through context windows and API calls
