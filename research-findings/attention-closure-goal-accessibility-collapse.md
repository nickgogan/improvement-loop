---
name: "Attention Closure — Goal Tokens Become Unreachable, Not Gone"
summary: |-
  A mechanistic explanation for why agents drift off-instruction in long conversations: the
  model's attention to the original goal/system-prompt tokens decays below a per-model
  threshold and "closes," even though the goal information still exists in residual-stream
  representations — the instructions are not gone, they are unreachable. Crucially for us, the
  paper's own tested countermeasure of periodically re-injecting the goal as a user message was
  a NEGATIVE result: repeating text is not the same as preserving usable goal information.
  Practical implication: prefer fresh-session handoffs at task boundaries over ever-longer
  conversations patched with reminders.
implementation_notes: |-
  Design implications for our long-running sessions and skills: (1) do not rely on periodic
  instruction repetition as the fix for drift — the paper tested user-role goal re-injection
  and reports it as a negative result; (2) session length itself is the risk variable — our
  /session-handoff fresh-context pattern is better aligned with the mechanism than in-place
  reminders; (3) failure is architecture-dependent (post-closure recall: Mistral 45%, Mixtral
  19%, LLaMA 0%), so drift tolerance observed on one model does not transfer; (4) the Goal
  Accessibility Ratio (GAR) offers a white-box diagnostic, but only for self-hosted models
  where attention weights are inspectable.
category: "Context Engineering"
evidence_strength: "Medium (empirical benchmarks)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "arxiv-when-attention-closes-goal-accessibility.md"
related_findings:
  - file: "context-rot-attention-budget-depletion.md"
    rel: "extends"
  - file: "windowed-attention-parametric-failure-timing.md"
    rel: "extended-by"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "defending-agent-context.md"
---

## What It Is

arXiv 2605.12922 ("When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction", Dongre, Hsieh, Lai, Yoon, Bui, Hakkani-Tür — UIUC + Adobe Research, May 2026) gives a channel-transition account of multi-turn instruction loss. Two pathways carry goal information: an **attention channel** (direct attention from generated tokens back to the goal-defining system-prompt tokens) and a **residual channel** (goal information distributed across residual-stream representations). As conversations lengthen, attention to goal tokens declines monotonically — positional decay in rotary embeddings plus competition for attention budget — and when it falls below a per-model threshold, the attention channel closes. Behavior then depends entirely on what the residual channel happens to preserve.

Evidence: the **Goal Accessibility Ratio (GAR)** quantifies attention mass flowing from response tokens to goal tokens across all layers and heads. Linear probes on residual representations predict recall outcomes at AUC up to 0.99 across four architectures (Mistral-7B, LLaMA-3.1-8B, Qwen-2.5 at multiple scales, Mixtral-8x7B). Causal ablation of the attention channel on Mistral collapses a 20-fact retention task from near-perfect to 11%. Goal encoding depth varies from layer 2 to 27 across models, and post-closure recall diverges sharply by architecture (Mistral 45%, Mixtral 19%, LLaMA 0%).

## Why It Matters

This mechanizes "context rot": degradation is not uniform blurring but a threshold event on a specific channel, with the instructions still physically present in context and even still encoded internally — just no longer reachable through attention. Two design consequences follow. First, "the instructions are in the context window" is not the same as "the instructions are usable"; longer context windows delay closure but do not prevent it. Second — the paper's negative result — periodically re-injecting the goal as a user-role message did **not** restore goal-conditioned behavior in their tests, undercutting the most common practitioner remedy. The paper concludes that reliability requires maintaining goal representations that stay usable after direct token access fades, i.e., architectural or session-structural solutions rather than repetition.

## Why People Are Using It

Academic empirical work (probing, causal ablation, cross-architecture benchmarks), not yet a production practice — its use is as design grounding. It extends our existing context-rot finding (attention-budget depletion) from a resource framing to a mechanism with a threshold, a metric, and measured architecture-specific failure profiles.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Treat drift as uniform rot | The prior attention-budget framing | Back-of-envelope context hygiene; no mechanism needed |
| Empirical drift evals | Black-box multi-turn instruction-retention tests | Hosted frontier models where internals are inaccessible |

## Potential Improvements

- Track whether follow-up work validates GAR-style diagnostics or successful re-anchoring variants (e.g., system-role vs user-role re-injection, structural pinning)
- Test whether the negative re-injection result replicates on frontier hosted models via black-box evals

## Potential Failure Modes

- **Overgeneralizing from 7B–8x7B open models to frontier hosted models** — closure thresholds, layer profiles, and the re-injection negative result may not transfer
- **Negative-result overreach:** the paper tested one re-injection scheme (user-role, periodic); other re-anchoring designs are untested, not disproven
- **GAR impracticality:** the diagnostic requires attention-weight access unavailable through commercial APIs
