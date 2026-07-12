---
name: Nine-Primitive Document-Agent Skeleton with Prepare-Don't-Submit Gate
summary: 'Plain English: one reusable agent skeleton covers all high-trust paperwork domains —

  build it once on low-stakes work, then re-point it at money-touching work with the same

  parts. Nine primitives: context pack (what the agent may read), ingest, chunk, normalize,

  store (local SQLite + folder), retrieve, cite, export, and gate. The gate is designed in

  from the start: the agent may read, organize, draft, and cite, but is never given the

  option to submit, pay, or sign — the terminal action stays human. Demonstrated three

  times with the same skeleton (email/calendar -> insurance appeal -> tax prep packet),

  each build faster than the last because the primitives are domain-agnostic

  ("mess-to-file organization first, structured insights out").'
implementation_notes: 'P2: the skeleton is a candidate schematic for the engine''s harness-layer library (the

  document-work analog of the work-ticket contract). The gate primitive is the same shape

  as the engine''s DD-29 human gate — an agent job description that excludes the terminal

  action rather than a bolt-on approval step. Learn-the-gate-where-mistakes-are-cheap is

  the recommended adoption sequence: validate the skeleton on low-stakes flows before

  pointing it at consequential ones.'
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- i-pointed-my-agent-at-the-bills.md
related_findings:
- file: advisory-only-for-persistent-mutations.md
  rel: same-problem
- file: human-on-the-loop-hotl-autonomy-tiering-framework.md
  rel: same-problem
- file: receipt-artifact-as-agent-trust-mechanism.md
  rel: enables
- file: data-normalization-as-cheap-model-enabler.md
  rel: enables
- file: claude-code-12-agent-primitives.md
  rel: same-problem
- file: structure-addressed-retrieval-for-cited-document-domains.md
  rel: enables
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: raw
---

# Nine-Primitive Document-Agent Skeleton with Prepare-Don't-Submit Gate

## What It Is

A domain-independent skeleton for agents that do high-trust document work:

1. **Context pack** — declares exactly what the agent is allowed to read, plus one goal
   phrased as *prepare* (e.g., "prepare a reply with a proposed calendar hold").
2. **Ingest** — documents to text with anchors back to the source.
3. **Chunk** — split into tagged, addressable pieces (a denial letter becomes date, denial
   reason, claim number, deadline, evidence-that-would-change-the-decision).
4. **Normalize** — dates become dates, amounts become amounts, people become people, and
   critically: missing documents become explicit missing-document records.
5. **Store** — locally (SQLite + a folder you can open); nothing leaves the machine; the
   model is never asked to "remember."
6. **Retrieve** — by structure where the domain cites addresses (see the
   structure-addressed-retrieval finding).
7. **Cite** — every claim points at its source; a citation guard blocks uncited claims
   (a deduction without a receipt gets flagged, not invented).
8. **Export** — a reviewable packet (case file, ledger, evidence map, open questions), not
   a fired-off action.
9. **Gate** — submit/pay/sign is excluded from the agent's action space from day one.

## Why It Matters

It answers the "stuck after the email demo" problem: practitioners get a low-stakes agent
working and see no path to consequential work. The bridge is recognizing that insurance,
taxes, and scheduling are the same problem to the agent, so every primitive built on cheap
mistakes is reusable on expensive ones — a flywheel where each build gets cheaper (the tax
build took a fraction of the insurance build's setup). The gate design also reframes
safety: not a permission prompt wrapped around a capable agent, but a job description that
never included the dangerous verb ("if an agent sends a bad appeal on its own, you now
have two problems: the denial and the mess the agent made").

## Why People Are Using It

Demonstrated three times in one session on progressively higher-stakes domains; the
runbooks and two open skills are published on the author's Substack. The value framing
resonates: the agent lifts the load (combing, structuring, drafting, citing); the human
keeps the click.

## Potential Improvements

Formalize the skeleton as a schematic/template with the nine primitives as checklist
sections; pair with the work-ticket contract (another Nate B Jones source) for multi-agent
handoff of the exported packet.

## Potential Failure Modes

Gate erosion — once the packet is reliably good, humans rubber-stamp (the receipt makes
review faster, "not optional"). Normalization errors propagate silently into every
downstream artifact. The skeleton's economy depends on domains actually sharing structure;
adversarial or free-form domains (negotiation, novel formats) break the ingest/chunk
assumptions. Local-store discipline can lapse into stale data masquerading as current.
