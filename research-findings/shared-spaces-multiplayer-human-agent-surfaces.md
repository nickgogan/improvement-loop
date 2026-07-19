---
name: "Shared Spaces — Multiplayer Human+Agent Collaboration Surfaces"
summary: |-
  Plain English: give a team one shared, commentable surface where humans AND agents
  both show up, instead of everyone running private 1:1 chats with their own agent
  instance and manually relaying what they learned. Geoffrey Litt (Notion) describes two
  shapes — multiplayer chat threads where a teammate can pull in a different agent
  mid-conversation and everyone sees it, and planning docs where a comment thread
  attached to the artifact replaces a side-channel discussion — and frames it as the
  team-scale version of "going from one-on-one conversations to Slack channels." Notion
  shipped coding agents living inside Notion pages the week of the talk specifically
  because of this benefit — his own team builds code there now. The underlying claim:
  shared understanding is what lets a team communicate and generate ideas together, and
  that is bottlenecked by each person's context being invisible to everyone else by
  default.
implementation_notes: |-
  Requires a persistent, commentable, multi-party surface — not a private 1:1 chat —
  where both human and agent turns are visible to every participant and comments attach
  to the artifact rather than a side channel. Notion's own implementation (HTML blocks
  plus coding agents inside pages) is one concrete substrate, not the only viable one.
  No current MetaSystem surface provides this; adopting it would require deliberately
  choosing a host (shared doc tool, wiki, or equivalent) before it becomes actionable
  rather than aspirational.
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (Owner/Nick review-gate collaboration surface)"
  - "General"
adopted_in: []
sources:
  - "understanding-is-the-new-bottleneck.md"
related_findings:
  - file: "html-pr-explainer-with-margin-annotations.md"
    rel: "same-problem"
  - file: "visual-recap-post-execution-mirror-artifact.md"
    rel: "same-problem"
  - file: "microworlds-ephemeral-interactive-debuggers.md"
    rel: "same-problem"
  - file: "quiz-as-comprehension-gate-before-forwarding.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "synthesized"
consumed_by:
  - "building-agentic-systems.md"
---

# Shared Spaces — Multiplayer Human+Agent Collaboration Surfaces

## What It Is

A pattern for *team*-scale (not solo) understanding: give humans and agents a shared,
persistent, commentable surface instead of each person running private 1:1 chats with
their own agent instance. Two concrete shapes from Geoffrey Litt's (Notion) talk:

1. **Multiplayer chat threads.** Multiple humans *and* multiple agents share one
   thread. Litt's example: he asks a question, his PM says "let's ask a different
   agent," that agent joins and answers in the same visible thread — "instead of me and
   my PM both talking to our own agents, we're in a shared space, we can see each
   other's communication... it's kind of like going from one-on-one conversations to
   Slack channels."
2. **Commentable planning documents.** An agent-authored plan lives in a shared doc, not
   a local chat log. A human leaves an inline comment with a question; a teammate can
   "chime in" in the same thread — discussion happens attached to the artifact, not in a
   side channel.

Concretely shipped in Notion: coding agents (Claude, Cursor) can now live inside Notion
pages/workspaces, explicitly *because* of this shared-space benefit — "our team actually
builds a lot of our code in Notion itself, mainly because of these benefits."

## Why It Matters

Names the collaborative, team-scale generalization of the talk's core thesis
("understanding to participate," not just to verify): shared understanding between
teammates is what enables them to communicate and "jam" effectively, and that shared
understanding is bottlenecked by each person's context being invisible to the others by
default. Multiplayer surfaces make agent-human and human-human exchanges about the same
work mutually visible instead of siloed per-person, so the team's collective model of
"what's going on" stays synchronized without someone manually relaying it.

Directly relevant to the engine's own producer-to-consumer and Owner/Nick review-gate
patterns, where review currently happens in a single chat thread rather than a surface
attached to the artifact itself and visible to whoever else might need to weigh in.

## Why People Are Using It

Presented by a design engineer at Notion, building the pattern for his own team's
workflow, with a concrete recently-shipped feature (coding agents living in Notion
pages, launched the week of the talk) as evidence it moved from concept to production
inside Notion itself, not just a demo.

## Potential Alternatives

- **Private 1:1 agent chats plus manual relay.** The status quo; cheap, but loses shared
  context and creates staleness the moment someone doesn't copy-paste the relevant part.
- **Async PR/doc comments without live agent participation in the thread.** Partial —
  comments are shared, but re-invoking the agent is still a private action outside the
  shared surface.
- **Team-chat-plus-bot integrations** (e.g., Slack with an agent bot). Similar shape,
  different substrate — Litt's own framing explicitly reaches for the Slack-channel
  analogy.

## Potential Improvements

- Structured provenance in shared threads: when multiple agents (possibly different
  models or instances) contribute to one thread, tag which agent said what and when, so
  understanding-drift stays traceable.
- Comment-to-task routing: a teammate's inline comment on a plan should be able to
  generate a scoped follow-up for the agent, closing the loop — the same unimplemented
  idea already flagged as a "Potential Improvement" on
  `visual-recap-post-execution-mirror-artifact.md` ("recap-comment routing"), arrived at
  independently from a different source.

## Potential Failure Modes

- Multiplayer visibility without access control raises the same scope questions as any
  shared workspace — who can invoke which agent, on whose behalf, with what authority.
  This is a governance boundary question, not only a UX one.
- Shared threads can dilute the "one canonical author" clarity that makes a plan
  reviewable; more voices in one thread can mean less legible provenance, not more,
  without deliberate discipline.
- The concrete tooling (Notion HTML blocks, coding agents in pages) ties the pattern to
  one vendor's surface; the general shape — a shared, commentable artifact with
  multi-party live agent access — is vendor-neutral, but the implementation isn't.
