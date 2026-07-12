---
name: External Ticket as Brainstorm Seed Input
summary: Pasting a Jira/Linear/GitHub ticket URL into the brainstorm skill provides structured scope (context, UX decisions, edge cases, acceptance criteria) as the seed for design exploration. The external
  ticket replaces freeform human description with pre-structured intent, and the brainstorm skill reads the ticket to extract scope, UX requirements, and edge cases before asking questions.
implementation_notes: null
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
- General
sources:
- claude-code-plus-superpowers-tutorial.md
related_findings:
- file: brainstorming-as-mandatory-design-gate.md
  rel: extends
- file: superpowers-plugin-spec-driven-sub-agent-orchestra.md
  rel: extends
- file: business-analyst-upstream-quality-gate.md
  rel: same-problem
- file: spec-first-agent-briefs-prompt-craft-context-inten.md
  rel: same-problem
- file: wayfinder-issue-tracker-decision-map.md
  rel: same-problem
adopted_in: []
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-07-12'
pipeline_status: classified
consumed_by: []
tags:
- session-95-reextract
---

# External Ticket as Brainstorm Seed Input

## What It Is

A pattern where the brainstorm phase of a spec-driven workflow is seeded with a URL to an external project management ticket (Jira, Linear, GitHub Issues) rather than a freeform human description. The brainstorm skill reads the ticket to extract pre-structured information: feature scope, UX decisions, technical context, edge cases, and acceptance criteria. It then uses this structured input as the starting point for design exploration.

In the observed Superpowers workflow (Eric Tech tutorial, BookZero.ai):
1. The practitioner had crafted a Jira ticket with: context for UX decisions, feature scope, the entire sync flow, and edge cases to consider
2. He copied the Jira ticket link and pasted it alongside the brainstorm skill invocation
3. The skill read the ticket, understood the scope, explored the existing codebase architecture, and then began asking focused follow-up questions

The composition insight is that the brainstorm skill acts as a **ticket-to-spec converter**: it reads structured project management input and transforms it into a development spec through interactive design exploration. The ticket provides the WHAT; the brainstorm provides the HOW.

## Why It Matters

Freeform brainstorm input ("I want to add a sync feature") leaves too much scope undefined. The agent must ask many questions to establish context, scope, and edge cases. A pre-structured ticket front-loads this information, letting the brainstorm phase focus on design decisions rather than scope discovery.

This also bridges the gap between project management tooling and development tooling. Teams that already use Jira/Linear for feature scoping can feed their existing artifacts directly into the development pipeline without re-describing the feature in a prompt.

The broader pattern: **external structured input raises the floor of brainstorm quality.** When the seed input already contains edge cases and acceptance criteria, the brainstorm skill can explore design space rather than basic requirements space.

For MetaSystem: this maps to how the IL could accept structured input from governance artifacts. A DD could serve as a "ticket" that seeds a build specification brainstorm — the DD provides scope and constraints, the brainstorm explores implementation approach.

## Why People Are Using It

Demonstrated in Superpowers' brainstorm skill (Eric Tech tutorial). The practitioner explicitly noted he "crafted a Jira ticket on exactly what's the feature scope" before pasting it into Claude Code. The skill's ability to read ticket URLs suggests this is a designed-for use case, not an accidental capability.

The business-analyst-upstream-quality-gate finding captures the broader principle: quality of agent output is bounded by quality of input specification. This finding is a specific mechanism for raising input quality by leveraging existing project management artifacts.

## Potential Improvements

- Template integration: brainstorm skills could have ticket-type-specific templates (bug ticket seeds a different exploration than feature ticket)
- Ticket gap detection: the brainstorm skill identifies what the ticket is MISSING (e.g., "this ticket has scope but no acceptance criteria — let me ask about that")
- Bidirectional sync: after the brainstorm produces a spec, update the original ticket with a link to the spec and key design decisions
- Multi-ticket input: some features span multiple tickets; the brainstorm should accept a list and synthesize

## Potential Failure Modes

- **Ticket quality ceiling.** If the Jira ticket is vague or wrong, the brainstorm inherits those problems. "Garbage in, garbage out" still applies — the ticket is not a substitute for clear thinking about scope.
- **Over-reliance on ticket as source of truth.** The brainstorm may treat ticket content as immutable constraints rather than starting points. If the ticket says "add a sync button" but a dropdown is better, the brainstorm should be free to propose the alternative.
- **Tool integration fragility.** Reading Jira/Linear tickets requires API access (MCP or web fetch). If the integration breaks, the workflow falls back to freeform description, which is a sharp degradation in input quality.
- **Security/access control.** Pasting ticket URLs into a coding agent may expose ticket content (including internal context, customer data, or security-sensitive information) to the model. Teams with sensitive tickets need to consider this exposure.
