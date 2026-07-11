---
name: "arXiv 2605.12922 — When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction"
source_type: "Research Paper"
status: "Done"
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
authority:
  - "uiuc-conversational-ai-adobe-research.md"
findings:
  - "attention-closure-goal-accessibility-collapse.md"
  - "windowed-attention-parametric-failure-timing.md"
date_added: "2026-07-11"
date_processed: "2026-07-11"
---

Queued for `/research-loop` extraction by the 2026-07-11 link-intake triage
(`operations/research-reports/2026-07-11-link-intake-triage.md`, link #4).

Processed 2026-07-11 (Pass 1). Authors: Dongre, Hsieh, Lai, Yoon, Bui, Hakkani-Tür (UIUC +
Adobe Research), submitted 2026-05-13. Two findings extracted. IMPORTANT correction to the
triage takeaway: the paper does NOT demonstrate re-injection as a working countermeasure —
Appendix H reports periodic user-role goal re-injection as a NEGATIVE result ("repeating or
retaining text is not equivalent to preserving goal information"). The negative result is
recorded inside the attention-closure finding rather than as a standalone countermeasure
finding.
