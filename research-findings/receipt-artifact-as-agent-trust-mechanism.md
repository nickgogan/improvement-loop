---
name: "Receipt Artifact as Agent Trust Mechanism"
summary: |-
  Plain English: what makes a human trust an agent's draft isn't the draft — it's a small
  companion artifact that says what the agent used, what it changed, and what still needs
  approval. When the agent stops at the prepare-don't-submit gate, it leaves three things:
  the draft, the proposed action (e.g., a calendar hold), and a receipt listing (1) the
  sources it used, (2) what it changed, and (3) what still needs human approval. The
  receipt is the difference between "AI handled it" and "I know what happened here and I
  can trust the AI" — it makes human review fast enough to be sustainable, which is the
  precondition for pointing agents at work where real money is on the line.
implementation_notes: |-
  P2: direct enrichment candidate for how engine skills and subagents report at human
  gates — a standard sources-used / changes-made / needs-approval triplet is cheap to emit
  and maps onto the engine's auditability rule ("if it can't be audited, it shouldn't
  happen"). Related but distinct: the work-ticket claim receipt (proof-of-done vs agent
  self-report) from the multi-agent lane covers cross-agent trust; this one covers
  agent-to-human trust at the gate.
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "IL (skill/subagent gate reporting)"
  - "General"
adopted_in: []
sources:
  - "i-pointed-my-agent-at-the-bills.md"
related_findings:
  - file: "nine-primitive-document-agent-skeleton.md"
    rel: "enabled-by"
  - file: "agent-self-reporting-unreliability-independent-eval.md"
    rel: "same-problem"
  - file: "human-on-the-loop-hotl-autonomy-tiering-framework.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

# Receipt Artifact as Agent Trust Mechanism

## What It Is

A standardized artifact the agent emits whenever it stops at a human gate, answering three
questions: **what sources did I use** (with addresses back into the stored, chunked
originals), **what did I change**, and **what still needs your approval**. In the
insurance-appeal build the receipt generalizes into a case file: a timeline (service date,
claim date, denial date, appeal deadline), a denial map quoting the exact policy language,
an evidence checklist split into have/missing, and the draft letter — with the packet, not
the letter, framed as the real product.

## Why It Matters

Trust is the actual bottleneck between toy agents and consequential agents, and trust is
built from inspectability, not accuracy claims. The receipt converts review from
re-derivation ("is this draft right?") into verification ("do these three listed changes
match these three cited sources?"). The source is explicit that citations make review
faster, not optional — the receipt is a review accelerant, not a review replacement.
"Build for trust from day one if you ever want your AI to do high-value delicate work."

## Why People Are Using It

Demonstrated across all three builds in the source (email, insurance, taxes); the pattern
also names why viral send-it demos fail to transfer to real life: they optimize the
action, not the auditability of the preparation.

## Potential Improvements

A standard receipt schema (sources/changes/needs-approval) embedded in skill output
contracts; receipts accumulated as an audit log rather than discarded after each gate;
diff-shaped "what changed" sections for file-mutating agents.

## Potential Failure Modes

Receipt theater — an agent can emit a confident receipt whose citations don't actually
support the draft; spot-checking citations must stay in the review loop. Verbose receipts
recreate the review burden they were meant to remove. Self-reported "what I changed" is
still self-reporting; for adversarial settings pair with independent verification.
