---
name: Distillator with Round-Trip Validation
summary: BMAD's Distillator skill performs lossless document compression for LLM consumption. Distinguished from summarization — "distillates are lossless compression." Verified by spawning a reconstruction
  subagent that rebuilds from the distillate alone, then diffs for semantic gaps.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
## What It Is

BMAD's Distillator skill compresses documents for LLM consumption while explicitly targeting lossless compression rather than summarization. The key distinction: "Summaries are lossy. Distillates are lossless compression."

The verification methodology is novel: after compression, a reconstruction subagent is spawned that attempts to rebuild the original document from the distillate alone. The reconstruction is then diffed against the original for semantic gaps and hallucinations. If the reconstruction fails to capture material content, the distillation is rejected.

The compression process uses a fan-out pattern: parallel compressor subagents each handle a semantic group from the source document, then a merge compressor combines them into the final distillate. This parallelization addresses the practical constraint that compressing a large document in a single pass may exceed the agent's effective processing capacity.

## Why It Matters

Context compaction is a universal need in agentic systems — long documents must be shortened to fit context windows without losing information that downstream agents need. Most compression approaches have no verification mechanism: you compress, you hope nothing important was lost, and you discover the gap (or don't) only when a downstream task fails.

The round-trip test (compress, reconstruct, diff) provides a concrete quality metric for compression. It makes the question "did we lose anything?" answerable before the distillate is used, rather than after. This is analogous to round-trip testing in serialization — if you can deserialize what you serialized and get the same thing back, your serialization is lossless.

## Why People Are Using It

Observed in [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.2.2 — see [[bmad-method-analysis]] for structural details.

The explicit distinction between summarization and distillation, combined with the reconstruction-based verification, indicates this was designed to solve a specific failure: compressed documents that lost critical details, discovered only when downstream agents failed. The fan-out pattern suggests the approach was also optimized for throughput on large documents.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Extractive summarization | Pull key sentences verbatim rather than rewriting | When preserving exact wording matters more than compression ratio |
| Hierarchical summarization | Summarize sections, then summarize summaries | When documents have clear hierarchical structure |
| Chunked retrieval (RAG) | Don't compress — retrieve relevant chunks at query time | When the full document is rarely needed and specific queries dominate |
| Human-authored abstracts | Human writes the compressed version | When the document is stable and quality is critical |

## Potential Improvements

- Define a quantitative threshold for the reconstruction diff — how much semantic gap is acceptable before rejecting a distillation?
- Explore whether the reconstruction subagent should use a different model than the compressor to avoid shared blind spots
- Test whether the round-trip validation adds sufficient value to justify the token cost (three passes: compress, reconstruct, diff)

## Potential Failure Modes

- **Shared blind spots**: If the compressor and reconstructor are the same model, they may share the same blind spots — both may ignore the same information, making the round-trip test pass despite actual information loss
- **Token cost multiplication**: Three passes (compress, reconstruct, diff) plus parallel subagents means the distillation process may cost 3-5x the tokens of a simple summarization
- **Semantic diff limitations**: Diffing two natural language documents for "semantic gaps" is itself an imprecise operation — the diff agent may miss subtle losses or flag stylistic differences as gaps
- **Fan-out merge artifacts**: Parallel compression of semantic groups followed by merging may introduce inconsistencies at group boundaries
- **Diminishing returns on short documents**: The overhead of round-trip validation may not be justified for documents that are already near the target length
