---
notion_id: 32b1e08b-9b34-81a6-b4c5-cdcf0c67c22a
name: 'LLM Representation Bottleneck: Output Pressure on Latent Space'
summary: 'LLMs suffer a fundamental architectural constraint: their internal representations are shaped by the pressure to generate plausible next tokens, meaning all possible sentence continuations simultaneously
  influence the latent representation. JEPA avoids this by learning representations without generative output pressure.'
implementation_notes: null
category: Model Selection
evidence_strength: Weak (theoretical)
adoption_status: Not Yet Started
proposer_priority: Not Flagged
applicability:
- General
adopted_in: []
sources: []
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# LLM Representation Bottleneck: Output Pressure on Latent Space

## What It Is
In a transformer LLM, the model must generate output token by token. The internal representation at each layer is shaped by the need to produce a valid next token — every possible direction the sentence could go influences the representation being built. This creates what the presenter calls 'output pressure' that distorts the learned representation. In contrast, JEPA (Joint Embedding Predictive Architecture) learns to predict the representation of a masked portion of an image/video given the rest, with no requirement to reconstruct the original pixel values. The representations can be learned in a compact, low-dimensional space without generative output constraints.

## Why It Matters
If the core limitation of LLMs is that their representations are distorted by output pressure (making them good at token prediction but not necessarily at building accurate world models), then architectural alternatives that learn representations without this constraint may produce qualitatively different reasoning capabilities. This is the theoretical basis for Yann LeCun's argument that LLMs cannot reach AGI.

## Why People Are Using It
This is a research argument, not a deployed technique. The video's audience is theoretically curious practitioners and AI researchers interested in post-LLM architectures.

## Potential Alternatives
Chain-of-thought reasoning as a workaround for sequential output limitations; scratchpad/extended thinking features that give the model space to revise before committing to output; JEPA and other world-model approaches.

## Potential Improvements
The presenter notes they are actively working on integrating JEPA-style representations into text generation via 'explore tokens.' This is the practical research direction.

## Potential Failure Modes
JEPA representations, while structurally rich, are difficult to decode back into text or images — the very property that makes them clean for world modeling makes them hard to use for communication with humans.
