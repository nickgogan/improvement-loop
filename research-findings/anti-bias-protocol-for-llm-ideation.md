---
name: Anti-Bias Protocol for LLM Ideation
summary: BMAD's brainstorming skill includes an explicit anti-bias protocol — "consciously shift creative domain every 10 ideas" and "aim for 100+ ideas before organization." Addresses LLM semantic clustering,
  a known failure mode no other analyzed repo mitigates explicitly.
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---
## What It Is

BMAD's brainstorming skill includes an explicit anti-bias protocol with two concrete rules:

1. **Domain shift every 10 ideas**: "Consciously shift creative domain every 10 ideas" — forces the LLM to break out of the semantic neighborhood it has been generating within.
2. **Volume before organization**: "Aim for 100+ ideas before organization" — prevents premature convergence where the LLM clusters around the first few ideas and refines them rather than exploring broadly.

This protocol acknowledges LLM sequential bias as a known failure mode: when generating lists, LLMs tend to produce ideas in narrow semantic neighborhoods, with each idea priming the next to stay close. The domain-switching rule is a concrete mitigation that forces exploration across conceptual spaces.

Cross-repo context: among the analyzed repos (GSD, Superpowers, OpenClaw, Paperclip, gstack, mem0), no other framework explicitly addresses this failure mode. Superpowers' "one question at a time" implicitly reduces clustering by constraining generation scope. BMAD's protocol is the only explicit mitigation.

## Why It Matters

LLM-generated ideation is increasingly used for brainstorming features, architectures, test cases, and creative work. Without mitigation, the output tends to cluster around a narrow conceptual space — the first few ideas establish a semantic attractor that subsequent ideas orbit. This produces lists that feel diverse but actually explore a small region of the solution space.

The anti-bias protocol is simple and concrete enough to be applied in any system that uses LLMs for ideation. It does not require architectural changes — it is a prompt-level intervention that acknowledges a model-level limitation.

## Why People Are Using It

Observed in [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.2.2 — see [[bmad-method-analysis]] for structural details. Cross-repo context from [[cross-repo-comparison]].

The protocol's specificity (every 10 ideas, 100+ before organizing) suggests it was tuned through iteration, not invented from first principles. The fact that it is embedded in a brainstorming skill rather than a general guideline indicates it was solving a recurring problem.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Temperature/top-p tuning | Increase randomness parameters to diversify generation | When API-level control is available and domain-shifting prompts are insufficient |
| Multi-prompt parallel generation | Run multiple brainstorming prompts with different seed framing, then merge | When diversity is critical and cost is not a constraint |
| Human-in-the-loop domain seeding | Human provides domain shifts explicitly rather than relying on the LLM to self-correct | When the LLM's self-directed domain shifts are too shallow |
| Structured category matrices | Pre-define categories/dimensions and generate ideas within each | When the problem space is well-understood and can be decomposed in advance |

## Potential Improvements

- Test whether the "every 10 ideas" interval is optimal or if different intervals work better for different domains
- Explore whether providing explicit domain categories (rather than relying on the LLM to choose) produces better diversity
- Measure clustering quantitatively — embed generated ideas and compute pairwise similarity to validate that the protocol actually reduces clustering

## Potential Failure Modes

- **Forced domain shifts that don't stick**: The LLM may acknowledge the domain shift instruction but continue generating in the same semantic space with superficially different framing
- **Quality-diversity tradeoff**: Forcing breadth may reduce the depth of exploration in any single domain, missing the best ideas that require deeper drilling
- **Domain shift overhead**: Every domain shift requires the LLM to reorient, which may consume tokens and produce transitional ideas of lower quality
- **100+ ideas threshold may be wasteful**: For narrow, well-defined problems, generating 100 ideas before organizing may produce diminishing returns well before the threshold
- **No validation mechanism**: The protocol instructs the LLM to shift domains but provides no way to verify that the shift actually occurred at a semantic level
