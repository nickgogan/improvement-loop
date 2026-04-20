---
name: "GStack Office Hours — Socratic Discovery Pipeline"
summary: "Multi-phase Socratic interrogation protocol that forces wedge identification, user behavioral evidence, future-fit analysis, and competitive landscape research before any MVP scope is committed. AI agents push back on over-scoped requests and demand smallest-possible deployable slice."
implementation_notes: null
category: "Prompt Craft"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General / Cross-System"
adopted_in: []
sources:
  - "gstack-planning-multi-persona-spec-review.md"
related_findings:
  - file: bidirectional-prompting-for-spec-creation.md
    rel: same-problem
  - file: gstack-specialist-role-architecture.md
    rel: enabled-by
  - file: autoplan-auto-decision-pipeline.md
    rel: extended-by
  - file: planning-session-bias-separate-context-windows.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: raw
consumed_by: []
---

# GStack Office Hours — Socratic Discovery Pipeline

## What It Is

GStack's "Office Hours" (Phase 1 of its planning pipeline) is a structured Socratic interrogation protocol that runs before any spec is written. Rather than accepting a feature request at face value, the AI conducts multi-phase discovery:

1. **Context calibration** — Sub-agents scan codebase, data models, and services while collecting project context: startup stage, revenue status, paying-customer count.
2. **Wedge forcing** — Rejects multi-feature requests. Asks: "What is the smallest possible version a paying customer will actually use this week?" Forces human to select a single word-of-mouth-generating feature.
3. **User behavioral evidence** — Asks PM-style observation questions: "Have you watched users without helping them? What surprised you?" Anchors scope to real usage anomalies (e.g., users exporting CSV to answer questions the platform should answer natively).
4. **Future-fit analysis** — Projects the feature 3 years out: "If AI gets cheaper and competitors copy this, does this feature become more or less central?" Forces differentiation thesis.
5. **Competitive landscape research** — Sub-agents research the space in 3 layers: mainstream adoption, key concerns, and positional differentiation.
6. **Premise challenge** — Surfaces 5-6 explicit premises derived from the session and demands agree/disagree on each before proceeding. Catches misalignments before they propagate into spec.
7. **Cross-model second opinion (Phase 3.5)** — A fresh sub-agent with no conversation history reviews the problem statement, answers, premises, and landscape to produce an independent verdict.

Token cost for Office Hours phase: ~170k tokens.

## Why It Matters

Most feature specs are written from the requester's perspective — what they want — not from user behavioral evidence. GStack's discovery protocol is anti-sycophancy enforcement: the AI is explicitly prompted to push back on over-scoped requests, demand evidence, and force a smallest-deployable-slice commitment. The cross-model second opinion (Phase 3.5) introduces a structurally independent reviewer who cannot have been biased by the conversation — a different form of the "separate context window" principle applied to spec validation rather than implementation.

The premise-challenge step is particularly high-leverage: it forces the AI to surface its own working assumptions before they calcify into design decisions, giving the human a final gate to catch misalignments.

## Why People Are Using It

Demonstrated live on a brownfield SaaS project (BookZero) with paying customers. The Office Hours phase transformed a vague 5-feature wish list into a single scoped MVP (spending query + anomaly detection, tables only, no charts, no save, credit-based pricing). Real user evidence (CSV-export workaround) was the deciding signal.

## Potential Improvements

The Socratic questions are currently baked into GStack's skills — they could be parameterized as a reusable "discovery template" applied to any planning session, independent of GStack. The premise-challenge step could use structured YAML for machine-readable alignment (vs. prose agree/disagree). The cross-model second opinion could be extended to include a domain-expert sub-agent (e.g., security, compliance) rather than a generic reviewer.

## Potential Failure Modes

The Socratic protocol consumes ~170k tokens before any spec exists — high upfront cost that teams may shortcut under time pressure. User behavioral evidence is self-reported; there is no verification that the "surprise" observations are representative or unbiased. The future-fit analysis is speculative — prompting an AI to predict 3-year feature durability introduces false confidence. Premise agreement does not prevent scope creep after the office hours phase ends.
