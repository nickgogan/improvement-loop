---
name: "Human Partner Framing"
summary: "Superpowers deliberately uses 'human partner' instead of 'user' throughout all skills, documented as a design decision that should not be changed. Frames the agent-human relationship as collaborative rather than service-oriented, influencing how the agent conceptualizes its own role."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: null
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: "2026-04-08"
last_updated: "2026-04-08"
pipeline_status: "raw"
consumed_by: []
---
# Human Partner Framing

## What It Is
Superpowers consistently uses the term "human partner" instead of "user" across all skills and documentation. This is not incidental — it is documented as an intentional design decision that should not be changed. The framing is part of the broader persuasion engineering approach, specifically applying the liking and unity principles from Meincke et al. (2025). "User" implies a service relationship (the agent serves the user). "Human partner" implies a collaborative relationship (the agent and human think together). This is deliberate persona engineering that shapes how the agent frames its own role.

## Why It Matters
Language shapes behavior — in humans and, the evidence suggests, in LLMs. An agent primed to think of the human as a "partner" is more likely to push back constructively, surface concerns, and engage in genuine collaboration. An agent primed to think of the human as a "user" is more likely to comply uncritically. The distinction is subtle but affects the quality of agent-human interaction, particularly in design and planning phases where the agent's independent judgment is most valuable.

## Why People Are Using It
Observed in [Superpowers](https://github.com/obra/superpowers) v5.0.7 — see [[superpowers-analysis]] for structural details. The terminology is enforced across all skill files in the framework. Compare: GSD uses "user" but frames the relationship as "founder/visionary + builder" (role-based framing rather than terminology-based). BMAD uses standard "user" terminology throughout.

## Potential Alternatives
Role-based framing without terminology changes (GSD's "founder + builder" approach). Standard "user" terminology with explicit collaboration instructions. "Operator" or "developer" for technical contexts. No explicit framing — let the model's default behavior determine the interaction style.

## Potential Improvements
Context-dependent framing — "human partner" for design/planning phases where collaboration matters, "human reviewer" for verification phases where the human's role is evaluative. Measuring the actual behavioral impact of terminology changes on agent output quality. Combining terminology framing with explicit behavioral instructions for stronger effect.

## Potential Failure Modes
The behavioral effect of terminology changes may be small or model-dependent — some models may not meaningfully change behavior based on whether the prompt says "user" or "human partner." Over-familiarity — an agent that treats the human too much as a peer may push back excessively or fail to defer on matters of user preference. The framing may create false expectations about the depth of the collaborative relationship.
