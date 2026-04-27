---
name: Model-Native Context Window Awareness
summary: Claude Sonnet 4.5, Sonnet 4.6, and Haiku 4.5 track their own remaining context-window headroom throughout a conversation and can reason about it inline — a distinct architectural pattern from harness-side pre-turn projection gating. The model self-measures instead of the harness pre-calculating. This complements, rather than replaces, pre-turn budget projection — the two operate at different layers (model vs orchestrator) and catch different failure modes.
implementation_notes: MetaSystem uses Opus 4.7 (1M context); IL agents currently rely on user-reported stop or harness-measured peak. If/when IL sessions migrate to model-native-aware models, Researcher/Codifier/Owner agents could self-pace compaction/stop decisions instead of waiting for harness triggers.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-context-windows-docs.md
- arxiv-token-budget-aware-llm-reasoning.md
related_findings:
- file: token-budget-pre-turn-projection.md
  rel: extends
- file: context-usage-status-line-visual-budget-tracking.md
  rel: same-problem
- file: two-threshold-compaction-strategy.md
  rel: enables
- file: claude-code-long-term-memory-via-pre-prompt-recall.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-04-23'
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---

# Model-Native Context Window Awareness

## What It Is

Anthropic's Claude Sonnet 4.5, Sonnet 4.6, and Haiku 4.5 are documented as tracking remaining context-window headroom internally — the model can reason about "how much room do I have left?" inline, without the harness injecting a separate usage figure. A parallel research track (the ACL 2025 "Token-Budget-Aware LLM Reasoning" paper) shows that telling a model its token budget up front compresses the reasoning trace to fit, reducing overhead for the same answer.

This is architecturally distinct from the harness-side "pre-turn projection" pattern (already in the KB): pre-turn projection runs *before* the model is called and gates the call; native awareness lets the model *during* its own response decide to cut reasoning short, summarize, or ask for compaction.

## Why It Matters for Us

Plain English: historically the harness has been the only actor that knew how full the context window was — the model itself was "driving blind." Now some models can see their own fuel gauge. For IL, this matters because our current loops (research-loop, /extract-artifacts) stop either when the user interrupts or when the harness signals. Model-native awareness adds a third escape hatch: the model itself saying "I have 10% left, let me wrap up" — catching the failure mode where the harness's projection was wrong and the user was inattentive.

Does not replace pre-turn projection — catches a different failure mode. Layered defense.

## Why People Are Using It

Anthropic ships it by default on 4.5+ models; no opt-in required. The ACL 2025 paper shows measurable reasoning-token savings when the budget is surfaced to the model explicitly.

## Potential Alternatives

- Harness-side pre-turn projection only (existing MetaSystem state)
- External "context usage status line" visualized for the user (Claude Code's `/context` command)
- Periodic compaction on wall-clock intervals (cruder)

## Potential Improvements

An IL `research-loop` variant that explicitly surfaces remaining-budget into the model's context ("you have N tokens left; wrap up if below threshold") — trivial to add once we move to a 4.5+ default.

## Potential Failure Modes

- Model-reported headroom drifts from harness-reported headroom; which one wins?
- Overly conservative self-stop — model gives up usable budget
- Not all models in MetaSystem's mix have this capability; mixed-model loops lose the guarantee
- Opus 4.7 (current IL default) behavior not explicitly documented in the same terms; verify before relying on it
