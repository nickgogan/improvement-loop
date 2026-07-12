---
term: context-rot
type: concept
variants: []
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-concept"
  - "context-rot"
  - "symptom-carrier"
aliases:
  - "Context rot"
  - "Attention budget depletion"
  - "Context decay"
---

# Context Rot

## Short definition

**Context rot** is the gradual, often silent degradation of an agent's attention over a session — the agent produces output that *looks plausible* but increasingly deviates from the task's constraints, goals, or accumulated decisions. The immediate mechanism is attention-budget depletion: as the context window grows, the model allocates less effective attention per token, and load-bearing but undistinguished details (hard constraints, prior decisions, numeric invariants) get underweighted. The second-order mechanism is *noise accumulation* — conversation history, stale files, indiscriminate rule accretion, and IDE-streamed content crowd out the signal the task needs.

Single referent. No variants. The failure looks the same whether the agent is a one-shot code writer or an autonomous long-running supervisor; scale and urgency differ, but the mechanism does not.

## Not to be confused with

| Not context rot | What it is instead |
|---|---|
| **Hallucination** | The model inventing content that has no basis in its input. Context rot is the opposite — the content *is* in input but the model attends to it less effectively. |
| **Intent drift** | The model shifting off-task because the prompt's intent was under-specified from the start. Intent drift is an authoring problem (G1); context rot is an operational decay over time. |
| **Prompt injection** | Adversarial content in retrieved or tool-returned context. That is a safety concern (G6). Context rot is a benign attention problem with malicious-looking symptoms. |
| **Model-capability limit** | Sometimes the task exceeds the model's capability outright. Context rot is *recoverable*: the same model handles the same task cleanly with a leaner context. |
| **Working memory** | The in-context tier of memory (see `memory.md` Variant A). Context rot is the *failure mode* operating on that tier; working memory is the tier itself. |

## Mechanism (one layer down)

Two forces compound:

1. **Attention-budget depletion.** Larger contexts mean less effective attention per token. Load-bearing details become indistinguishable from boilerplate. Effect scales nonlinearly: output quality often drops after a characteristic turn count (~50 is a common practitioner report, though the curve varies by model and task shape — `context-rot-attention-budget-depletion`).
2. **Noise accumulation.** Conversation history, stale files, indiscriminate rules in CLAUDE.md, and IDE-streamed open files accrete into the context over a session. Each individually looks cheap; in aggregate they crowd signal. G2b Step 5 (line 242) names the five production-tested defenses; `claudemd-context-rot-from-indiscriminate-rule-accu` is the worked example for the CLAUDE.md-specific case.

The two forces reinforce each other — a larger context has both a thinner attention budget *and* a lower signal-to-noise ratio.

## Composition

Substrate pointers for the core Librarian operations on context rot. Smaller table than variant-carrying concepts because the substrate is tightly clustered around G2b.

| Aspect | Tier 1 (guides, default) | Tier 2 (patterns / findings) | Tier 3 (watched-libraries) |
|---|---|---|---|
| Mechanism / "why this happens" | G2b `defending-agent-context.md` §Key Concepts, §"Detecting Context Degradation" | `context-rot-attention-budget-depletion`, `context-rot-silent-killer-and-mitigations` | — |
| Symptoms and failure mode (for diagnose) | G2b §Pitfalls | `context-rot-silent-killer-and-mitigations`, `claudemd-context-rot-from-indiscriminate-rule-accu` | — |
| Defenses — explicit state object, contract validation, delta updates | G2b §Session Discipline, §Compaction Timing | `ace-delta-updates`, patterns under Context dimension on structured-state-object discipline | — |
| Defenses — proactive compaction | G2b §Step 5 item 3 + G2b §Step 4 "Manage Dynamic Context" | `proactive-compaction-before-intelligence-degradation`, `memory-decay-compaction-convergence`, `dynamic-tool-pool-assembly-transcript-compaction` | — |
| Defenses — cross-session learnings persistence | G2b §Step 5 item 4 | `gsd-global-learnings-store-cross-session-persistence`, `claude-code-long-term-memory-via-pre-prompt-recall` — cross-ref `memory.md` Variant D | — |
| Defenses — natural reset points | G2b §Step 5 item 5 | — | — |
| Cost-side amplifier (hidden context tax) | G2b §Step 6 "Optimize for Cost" (line 258), specifically "Account for Hidden Costs" | Patterns on prompt caching and stable-context discipline | Anthropic caching docs |
| Audit surface — rule accretion in CLAUDE.md / spec files | G2b §Step 5; G1 §Pitfalls | `claudemd-context-rot-from-indiscriminate-rule-accu` | — |

## Librarian read rule

**Default (Tier 1).** For `(explain, context-rot)` queries (UC-6.1), read G2b §Key Concepts plus §Step 5 — those two sections together carry mechanism + defenses. For `(diagnose, context-rot)` queries (UC-4.1, UC-4.4), read G2b §Pitfalls and §Step 5 (defenses are the recovery pointers). For `(fetch, context-budget-worksheet)` (UC-2.1), point at G2b §Templates (line 294) where the Context Budget template is authored.

**Escalate to Tier 2 when:**
- Consumer asks "why does this happen" and a Tier-1 answer feels mechanistic-but-shallow — pull `context-rot-attention-budget-depletion` for the attention-budget specifics.
- Consumer is debugging a sustained-session quality drop — pull `proactive-compaction-before-intelligence-degradation` as the production-tested mitigation.
- Consumer's symptom is specifically "my CLAUDE.md is getting bloated" — `claudemd-context-rot-from-indiscriminate-rule-accu` is the worked example.

**Escalate to Tier 3 when:**
- Consumer is comparing harness-level caching implementations (Claude Code vs Cursor vs raw API) — Tier 3 for actual settings file / source.
- Consumer asks for the attention-budget curve empirics (rare; research-grade questions).

**Do not:**
- Conflate context rot with hallucination or intent drift when producing a diagnosis. The recovery paths are different.
- Skip G2b §Step 5 when authoring a defense plan. The five defenses are load-bearing together; picking one in isolation usually loses signal.

## Provenance surfacing

Tier-1 citations: `<guide>.md#<anchor>` with line-range appendix until the section manifest lands. Tier-2 citations: finding file path + slug. Tier-3 citations: `watched-lib/<path>:<line-range>`. When the Librarian surfaces a symptom→mechanism map (diagnose queries), attribute the symptom to the pattern finding and the mechanism to the guide — make the tier split explicit.

## Cross-references

- Related concepts: `memory.md` (Variant A cross-refs context-rot as the working-tier failure mode), `agent.md`, `harness.md`.
- Related operations: `diagnose.md`, `explain.md` (planned), `fetch.md` (planned for UC-2.1 context-budget template), `audit.md`.
- Use-case registry (UC-2.1, UC-4.1, UC-4.4, UC-6.1): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role), DD-82 (IL 4-agent architecture).
