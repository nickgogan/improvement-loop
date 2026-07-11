---
name: "arXiv 2605.12922 — When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction"
source_type: "Research Paper"
status: "Not started"
key_takeaways: |-
  Mechanistic account of context rot / instruction drift: goal tokens become attention-
  inaccessible while persisting in residual representations — instructions are not gone, they
  are unreachable, so periodic re-injection/re-anchoring restores them; failure timing is
  parametrically predictable for windowed attention. Introduces the Goal Accessibility Ratio
  (attention flow from generated tokens to task instructions); linear probes on residuals
  predict recall outcomes at AUC up to 0.99 across four architectures; causal ablation on
  Mistral drops a 20-fact retention task from near-perfect to 11%. Extends
  context-rot-attention-budget-depletion (crosslink as extends). Est. 2-3 novel findings.
relevance: "High"
added_by: "Agent (Link-Intake Triage)"
tags:
  - context-engineering
  - context-rot
  - attention
url: "https://arxiv.org/abs/2605.12922"
authority: []
findings: []
date_added: "2026-07-11"
date_processed: null
---

Queued for `/research-loop` extraction by the 2026-07-11 link-intake triage
(`operations/research-reports/2026-07-11-link-intake-triage.md`, link #4).
