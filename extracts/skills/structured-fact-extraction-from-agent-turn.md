---
title: "Structured Fact Extraction from Agent Turn"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "structured-fact-extraction-from-conversations"
identification_report: "session-persistence-and-memory.harvest-queue.md::structured-fact-extraction-from-conversations::skill::structured-fact-extraction-from-agent-turn"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent harnesses with persistent memory layers (cross-session preference stores, vector memories, fact graphs)"
    - "long-running agent sessions where compaction would otherwise discard decisions, preferences, or relationship context"
    - "memory pipelines that need typed, individually retrievable records rather than raw transcript blobs"
  platform_coupling: "general"
  autonomy: "all"
  stage: "operate"
  reversibility: "medium — emitted facts are append-only records; bad extractions can be filtered or deprecated downstream but propagate through any recall index built on top until reindexed"
  auditability: "high — every emitted fact carries provenance (source turn, timestamp, extracting model) and is individually inspectable; the extraction step itself is a discrete invocation that can be logged"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Multiple practitioner implementations exist (Hindsight, claude-code-vector-memory, Memongo). Not yet deployed in MetaSystem; current memory layer is prose in PROGRESS.md and MEMORY.md without typed extraction."
contract:
  preconditions: "An agent turn (user message + agent response, or a delimited conversation slice) is available as text. An LLM is available for extraction (the same provider already configured for the host harness suffices — no separate API needed). A target store for typed facts exists (vector store, JSON sidecar, or markdown frontmatter)."
  invariants: "Each emitted fact is typed against a closed enum (e.g., decision | preference | world | relationship | technical-context). Each fact carries source-turn provenance, extraction timestamp, and entities involved. Extraction runs out-of-band relative to the user-visible response — never blocks the agent's reply. The skill emits zero or more facts per turn; emitting nothing is valid output."
  governance: "Owner: agent harness operator. Writes go only to the configured fact store. Does not mutate the source turn or the conversation transcript. Operator chooses whether extraction runs synchronously after each turn or batched periodically; both modes preserve invariants."
  recovery: "If the LLM returns malformed JSON: retry once with a stricter schema-only prompt; if still malformed, log the raw output and emit zero facts for the turn (do not corrupt the store with partial records). If the fact store write fails: queue the facts to a local retry buffer and surface the error; do not drop facts silently. If extraction latency exceeds the configured budget: time out and skip extraction for that turn rather than blocking the next turn."
tags:
  - "extracted-artifact"
  - "skill"
  - "memory"
  - "context-engineering"
---

# Structured Fact Extraction from Agent Turn

**Source:** [[structured-fact-extraction-from-conversations]]
**Form:** skill
**Extraction date:** 2026-04-27

## Purpose

Convert a single agent turn (or a delimited conversation slice) into a set of discrete, typed, individually-retrievable fact records — so that decisions, preferences, world-state, and relationships survive transcript compaction and can be recalled by semantic relevance rather than recency. The unit of work is one turn; the unit of output is zero or more typed facts.

This is the post-turn extraction primitive used by Hindsight, Memongo, and claude-code-vector-memory. It is intentionally narrow: it does not aggregate long-form sources (see `multi-agent-proportional-content-summarization` for that), it does not gate writes on novelty (see `surprisal-novelty-as-memory-write-gate`), and it does not perform recall.

## Inputs

- **Turn payload:** A single agent turn (user message + agent response) or a delimited conversation slice. Plain text or chat-message JSON; whichever the host harness already produces.
- **Fact-type enum:** Closed list of allowed types. Default: `decision | preference | world | relationship | technical-context`. Operator may override.
- **Source identifier:** Stable handle for the turn (session id + turn index, or hash of payload) used as provenance on every emitted fact.
- **Extraction model:** LLM identifier. Default: reuse the host harness's configured provider so no separate API key is needed.
- **Output sink:** Target store handle (vector store collection, JSON file path, markdown sidecar, or frontmatter block).

## Procedure

1. **Parse the turn.** Normalize to a single text blob with role markers preserved (`USER:`, `AGENT:`). Strip tool-call traces unless the operator opts to include them.

2. **Prompt the extractor.** Send the parsed turn plus the fact-type enum and a strict JSON schema. The prompt instructs the model to emit a JSON array; each element has `{type, content, entities, confidence, evidence_span}` where:
   - `type` ∈ the configured enum
   - `content` is a single-sentence factual claim, written as a third-person assertion
   - `entities` is a list of named entities involved (people, projects, files, concepts)
   - `confidence` ∈ [0.0, 1.0] — the model's self-reported confidence
   - `evidence_span` is the verbatim substring of the turn that supports the claim (for audit)

3. **Classify into fact types.** The extractor performs classification inline — there is no separate classifier step. The schema enforces the closed enum; out-of-enum types are rejected and the fact is dropped.

4. **Validate.** For each candidate fact: (a) JSON parses; (b) `type` is in the enum; (c) `content` is non-empty; (d) `evidence_span` substring-matches the turn. Drop any fact that fails validation. Log drops for audit.

5. **Stamp provenance.** Add `source_turn_id`, `extracted_at` (extraction timestamp), and `extracted_by` (model identifier) to each surviving fact.

6. **Emit structured records.** Write to the output sink. Each fact is one record. The skill returns the count of facts emitted plus the list of validation drops. Emitting zero facts is a valid outcome — not every turn produces structured facts.

## Outputs

For each input turn, a list of zero or more fact records of the shape:

```json
{
  "type": "decision",
  "content": "MetaSystem adopts the fractal pattern for system organization.",
  "entities": ["MetaSystem", "DD-52"],
  "confidence": 0.92,
  "evidence_span": "we decided to use the fractal pattern...",
  "source_turn_id": "session-83:turn-14",
  "extracted_at": "2026-04-27T10:14:00Z",
  "extracted_by": "claude-opus-4.7"
}
```

Plus a per-turn extraction summary: `{turn_id, facts_emitted, facts_dropped, drop_reasons}`.

## Boundary

This skill does **one** thing: turn → typed facts. It does not:

- **Aggregate sources** — that is `multi-agent-proportional-content-summarization`'s contract (long-form content → single summary note + entity stubs).
- **Gate on novelty** — duplicate-fact filtering is the upstream surprisal-gate's job (see [[surprisal-novelty-as-memory-write-gate]]).
- **Recall facts** — retrieval is a separate capability (semantic search over the fact store).
- **Manage the fact store schema** — the sink is a dependency, not part of this skill.
- **Block the agent reply** — extraction runs out-of-band; the user-visible turn must complete first.

If the operator needs upstream novelty gating or downstream retrieval, compose this skill with the corresponding components — do not extend its scope.

## Failure Modes

- **Subtle multi-turn decisions are missed.** A decision reasoned across three turns may not surface in any single-turn extraction. Mitigation: operator may invoke the skill with a wider conversation slice as input, but each invocation still runs single-pass — there is no implicit cross-turn aggregation here.
- **Over-extraction crowds the store.** Without an upstream novelty gate, trivial facts ("the user said hi") accumulate. Mitigation: tune the prompt to skip greetings and meta-talk; rely on the surprisal gate as a separate pre-write filter.
- **Extraction-quality cliff at small models.** Cheap extraction models miss nuance. Mitigation: surface the `extracted_by` field so downstream consumers can weight or filter by extractor identity.
- **Hallucinated entities.** The model invents entities not present in the turn. Mitigation: the `evidence_span` substring-match validation catches most of these (the entity must appear in the cited span).
- **Latency cost on every turn.** Synchronous extraction adds tokens-per-turn cost. Mitigation: support batched mode — collect N turns, extract in one call. Operator picks sync vs batched based on the recall freshness they need.
- **Schema drift.** Operator edits the fact-type enum without reindexing the store. Mitigation: emit the enum hash with each fact; downstream readers can detect schema-version mismatch.

## Contract

### Preconditions
An agent turn (user message + agent response, or a delimited conversation slice) is available as text. An LLM is available for extraction (the same provider already configured for the host harness suffices — no separate API needed). A target store for typed facts exists (vector store, JSON sidecar, or markdown frontmatter).

### Invariants
Each emitted fact is typed against a closed enum (e.g., decision | preference | world | relationship | technical-context). Each fact carries source-turn provenance, extraction timestamp, and entities involved. Extraction runs out-of-band relative to the user-visible response — never blocks the agent's reply. The skill emits zero or more facts per turn; emitting nothing is valid output.

### Governance
Owner: agent harness operator. Writes go only to the configured fact store. Does not mutate the source turn or the conversation transcript. Operator chooses whether extraction runs synchronously after each turn or batched periodically; both modes preserve invariants.

### Recovery
If the LLM returns malformed JSON: retry once with a stricter schema-only prompt; if still malformed, log the raw output and emit zero facts for the turn (do not corrupt the store with partial records). If the fact store write fails: queue the facts to a local retry buffer and surface the error; do not drop facts silently. If extraction latency exceeds the configured budget: time out and skip extraction for that turn rather than blocking the next turn.
