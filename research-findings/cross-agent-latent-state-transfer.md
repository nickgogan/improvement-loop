---
name: "Cross-Agent Latent State Transfer"
summary: |-
  Research result: multi-agent pipelines that pass raw latent states between agents
  instead of decoded text — no tokenize/decode round-trip at each hand-off — raised
  competition-math accuracy from 73% to 86% on sub-10B models while cutting token usage
  75%, at ~$4 training cost. A controlled same-teacher comparison shows the architecture
  (not distillation) drives the gain. Optimal latent thought length ~80 steps; small-model
  scale only so far; code/models released.
implementation_notes: |-
  Plan → critique → solve pipeline where each agent forwards undecoded hidden states
  ("brain linking") to the next. Suggests a new scaling axis (more refinement rounds →
  better results). Reported via Two Minute Papers; primary paper not yet read — chase it
  before citing quantitative claims downstream. Not applicable to text/file-mediated
  harnesses (Claude Code) today; relevant as a frontier direction for the harness layer
  and for interpreting where inter-agent text protocols pay an avoidable tax.
category: "Orchestration"
evidence_strength: "Medium (peer-reviewed claims via secondary summary — primary unread)"
adoption_status: "Not Applicable (watch)"
priority: "P3"
applicability:
  - "General"
adopted_in: []
sources:
  - "scientists-found-a-better-language-for-ai-agents.md"
related_findings:
  - file: "l-d-hypothesis-information-loss-across-agent-bound.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

Multi-agent systems conventionally communicate in natural language: each agent decodes its
reasoning into tokens, and the next agent re-reads and re-encodes it. This work removes the
round-trip — agents pass **raw, undecoded latent states** directly ("cross-agent latent
state transfer"). In a three-agent plan/critique/solve pipeline on competition-level math,
sub-10B models went from 73% to 86% accuracy with **75% fewer tokens**, trained for about
$4. The killer control: giving the same giant-model teacher to baseline architectures does
not close the gap, so the mechanism (not distillation quality) carries the result.

## Why It Matters for Us

Our KB already holds the problem statement — information loss at agent boundaries
(`l-d-hypothesis-information-loss-across-agent-bound`) — and this is the first remedy in
the corpus that attacks the *encoding channel itself* rather than the protocol on top of
it. Nothing here is adoptable in a file-mediated Claude Code harness today, but it bounds
our mental model: text hand-offs between agents are a lossy, expensive channel by
construction, which strengthens the case for artifact-as-contract hand-offs (pass the
structured file, not a prose retelling) at our scale.

## Caveats

Small models only; unknown whether gains hold at frontier scale. ~80-step optimal latent
length caps per-round thinking. Secondary source — the primary paper (linked from the
video) must be read before any downstream artifact cites the numbers.
