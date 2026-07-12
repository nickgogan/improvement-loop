---
title: "Librarian Read-Contract — Query Execution Protocol"
type: "design-note"
target_system:
  - "improvement-loop"
created: "2026-04-21"
updated: "2026-04-21"
author: "claude"
stage: "draft"
source_dd:
  - "DD-77"
  - "DD-78"
  - "DD-80"
  - "DD-82"
  - "DD-86"
tags:
  - "design-note"
  - "librarian"
  - "read-contract"
  - "reference-layer"
aliases:
  - "Librarian read contract"
  - "Query execution protocol"
  - "Read protocol"
---

# Librarian Read-Contract — Query Execution Protocol

**Status:** Design note. Phase 5 of the session-49 plan. Formalizes how the Librarian turns a consumer query into substrate reads, escalates across tiers, surfaces confidence and provenance, and handles consumer-submitted inputs. Complements the Librarian agent definition (`agents/librarian/agent.md`) — the agent file states *what* the Librarian is; this note states *how* it executes under Option α' (concept + operation reference layer, three-tier access).

Nick gates any DD filing. No execution this session — this is the protocol spec; Phase 6 skills implement a narrow slice of it.

## Scope and non-goals

**In scope.**
- Query parsing (verb + noun decomposition).
- Load order — operation file first, concept file second, then substrate.
- Tier-1 default read shape — which guide sections load per operation × concept.
- Tier-2 and Tier-3 escalation signals, graph-traversal mechanics, stopping criteria.
- Confidence disclosure protocol — levels, triggers, display.
- Provenance surfacing — citation formats per tier.
- Consumer-input handling for audit, diagnose, whats-new, and meta queries.
- Boundary cases: missing concept file, missing operation file, ambiguous verb, oversized artifact input, cross-concept queries.
- Governance carry-through from the Librarian agent contract.

**Out of scope.**
- Rewriting the Librarian agent definition (that file states role; this one states execution).
- Authoring the remaining operation files (`diagnose`, `design`, `decide`, `fetch`, `explain`, `whats-new`, `coverage`, `plan`) — session 50+ per Phase 4 backlog.
- Implementing a Librarian-specific usage log. Per Nick's session-49 gate: **the IL System Log carries usage-record responsibility**; no separate log is warranted.
- Tier-3 repo-fetch orchestration beyond read mechanics (that belongs in a later operation spec).

## Operating premise

The consumer arrives with a natural-language query. The Librarian's job is to:

```
  parse → load → compose → read → assemble → cite
```

Each step is deterministic given the prior; the Librarian adds judgment only at variant selection, escalation decisions, and confidence calibration. Everything else is a mechanical walk over the reference layer and substrate tiers.

The reference layer (`operations/references/librarian/`) is the routing table that makes this mechanical. If the layer is incomplete, the Librarian falls back to runtime aggregation — graceful degradation, not failure.

---

## Step 1 — Query parsing

Every query decomposes into **(verb, noun(s))**. The Librarian's parser is a light classifier, not a grammar. Accuracy matters more than rigor.

### 1.1 Verb extraction

Canonical verb map. Alternate phrasings on the right resolve to the canonical verb on the left.

| Canonical verb | Aliases / triggers |
|---|---|
| `audit` | audit, review, assess, evaluate, critique, check (as in "check my …"), score |
| `diagnose` | diagnose, debug, "my agent is …-ing", "X keeps failing", "why is X erratic" |
| `design` | design, "how should I build", "how do I set up", "recommend an approach for", architect |
| `decide` | decide, "A or B", "should I use", "when would I pick", tradeoff |
| `explain` | explain, "why does", "what is", mechanism, "how does X work" |
| `fetch` | "give me a template / rule / scaffold", "show me the X for Y", fetch, get |
| `whats-new` | "what's new / recent / current", "what changed since …", "latest on" |
| `coverage` | "what does the KB cover", "do we have anything on", "how many findings" |
| `plan` | "sequence", "in what order", "phases", "roadmap for building" |

If a query blends verbs (e.g., "audit my agent and suggest a redesign"), the Librarian executes the primary verb first (audit), then asks whether the consumer wants the secondary operation (design) after — does not run both silently.

### 1.2 Noun extraction and variant selection

Nouns resolve against the concept files in `operations/references/librarian/`. Two cases:

**(a) Exact match.** Consumer names an existing concept file (e.g., "audit my agent.md" → `agent.md`). Load it.

**(b) Variant carrier.** Consumer names a term with variants (Agent, Memory, Second Brain). Run the concept file's variant-selection heuristics from the consumer's phrasing before loading — e.g., "the agent's accumulated KB" → `second-brain.md` variant B (AI). If selection is ambiguous, ask one disambiguating question (concept files contain the heuristics; the Librarian does not reinvent them).

**(c) No match.** No concept file resolves. Two sub-cases:
- **Planned but unauthored** (per `_index.md` planned list): Librarian states the gap and falls back to runtime aggregation using the guide routing table and dimension registry.
- **Unrecognized term**: ask the consumer one clarifying question. Never invent a concept mapping silently.

### 1.3 Meta / `*` detection

A query with no specific noun is a meta query — routes directly to the operation file with `*` concept. Examples: "what does the KB cover?" → (coverage, `*`). "Show me all templates." → (fetch, `*`). The operation file handles the `*` case; no concept file is loaded.

### 1.4 Cross-concept queries

Some queries combine concepts (UC-9.2: "I want an agent + hybrid second brain — in what order?"). Load both concept files. Operation file's procedure must support the join; if the operation is concept-agnostic, this is an appendable composition. If the operation defines noun-specific overrides only, the Librarian composes each concept separately and notes dependencies between them.

### 1.5 Size and urgency heuristics

- For audit queries, request artifact text or a path at parse time if not provided.
- For artifacts > ~500 lines, ask for a scoping clarification before loading.
- For diagnose queries, ask one qualifying question when the symptom is ambiguous ("Is the loss across turns in a single session or across sessions?").

---

## Step 2 — Load order

Fixed sequence. Operation file first, because the operation determines *which guide subsections* the concept's composition table should be read for.

1. **Operation file.** Read `operations/references/librarian/<verb>.md`. Obtain: default composition rule (which guide subsection kinds to read — Contract, Pitfalls, Key Concepts, Steps, Recovery), procedure, output shape, consumer-input expectations.
2. **Concept file(s).** Read `operations/references/librarian/<noun>.md` (and variant subsection if applicable). Obtain: composition table mapping aspect → Tier-1 guide references, Tier-2 patterns/findings, Tier-3 watched-library pointers. Plus the concept's Librarian read rule and depth-escalation default.
3. **Substrate — Tier 1.** For each relevant aspect, read the *operation-specified subsection kind* from the *concept-specified guide anchor*. Example: for (audit, agent), the operation says "read `### Contract` subsections"; the concept says "composed guides = {G1, G2, G3, G5, G6, G9, G10}"; the Librarian reads the `### Contract` subsection of each of those seven guides. Nothing else unless Tier-2 or Tier-3 escalates.
4. **Substrate — Tier 2 and Tier 3.** Deferred until an escalation signal fires (see Steps 4 and 5).

### Fallbacks when the layer is incomplete

| Missing | Behavior |
|---|---|
| Operation file absent | Librarian falls back to runtime aggregation using the guide routing table's lifecycle axis and practitioner questions, and states the degradation ("no `<verb>.md` file exists yet; producing a best-effort response"). |
| Concept file absent | Same pattern — use the guide routing table's dimension → guide mapping, state degradation. |
| Variant stub only (no full composition) | Proceed; note that the variant's full composition table is iterative ("stub guidance; deeper variant-specific composition is session-50+ backlog"). Per Nick's session-49 gate — variant stubs are enough to distinguish referents; depth iterates. |
| Concept file with unresolved anchor pointers | Read by heading-match (grep for `^## <heading>`) rather than by anchor. Flag to the consumer as a provenance caveat. |

Fallbacks are *graceful degradation* — the Librarian never refuses a query because the reference layer hasn't caught up.

---

## Step 3 — Tier-1 default read shape

Tier 1 = guides, section-addressable.

### 3.1 Which subsection kinds each operation reads

Operation files specify this. Summary for the authored + planned operations:

| Operation | Primary subsection kinds | Secondary (optional) |
|---|---|---|
| `audit` ✓ | `### Preconditions` (gates), `### Invariants` (rubric) | `### Recovery` (for findings' remediation pointers) |
| `diagnose` (planned) | `### Pitfalls` (symptom → cause), `### Recovery` | `### Key Concepts` (for mechanism explanation of why the symptom arises) |
| `design` (planned) | `### Step N` subsections (the authored build sequence) | `### Templates`, `### Examples`, `### Preconditions` (applicability gate) |
| `decide` (planned) | `### Key Concepts` (tradeoffs), `### Design debates` (if present), cross-cutting pattern files | `### Examples` |
| `explain` (planned) | `### Key Concepts`, `### Why this works` / `### Mechanism` | `### Pitfalls` when the explanation is "what goes wrong without this" |
| `fetch` (planned) | Specific anchored subsection named by consumer (`Template: …`, `Rule: …`, `Example: …`) | Per-guide `sections[]` manifest for catalog sub-op |
| `whats-new` (planned) | Date-filtered reads — Librarian applies `since: <date>` against artifact `created`/`updated` | — |
| `coverage` (planned) | `_index.md` files, guide routing table, dimension registry | — |
| `plan` (planned) | Lifecycle axis (specify → build → verify → secure → operate); per-step guide pointer | — |

The Librarian does **not** read full guide bodies for Tier-1 responses. Section-addressable reads are load-bearing for cost control.

### 3.2 Anchor vs heading-match

Preferred: anchor IDs from the guide's `sections[]` manifest (pipeline collapse proposal DD-NEW-1). Until the anchor manifest lands, fall back to heading-match: `Grep -n "^## <heading>"` to locate the section, then read the line range. Concept and operation files should carry heading text as a fallback alongside anchor IDs so this works in the interim.

### 3.3 Cross-guide stitching

When the operation reads the same subsection kind across multiple guides (canonical example: audit reading `### Contract` across 7 guides for agent audit), the Librarian:

1. Pools the invariants/steps/pitfalls.
2. Applies the operation's composition rules (for audit: precondition gating + de-duplication + hierarchical overlap annotation + file-verifiable vs system-verifiable split — all codified in `audit.md`).
3. Emits a pooled artifact (a rubric, a symptom map, a step list) — not a concatenation of per-guide snippets.

---

## Step 4 — Tier-2 escalation

Tier 2 = patterns + findings, using `related_findings` typed links.

### 4.1 Signals that fire Tier 2

The Librarian escalates to Tier 2 when **any** of:

1. **Consumer explicitly asks for depth** — "why does G2 say X?", "show me the evidence", "what's the debate on this?"
2. **Design-debate queries.** UC-5.2 style ("single-store vs. triple-storage memory"). The debate lives in the `related_findings: contradicts` edges, which guides typically flatten or summarize. Tier-2 surfaces the raw contradiction.
3. **Cross-finding rationale.** When a Tier-1 claim hinges on a pattern cited across multiple guides, Tier 2 surfaces the pattern directly so the consumer sees the shared mechanism once rather than three restatements.
4. **Tier-1 confidence is low.** Either because the aspect is sparsely covered in the named guide, or because the Tier-1 answer quotes a pattern by slug without unpacking. See §Step 6 for how "low confidence" is judged.
5. **Concept file's depth-escalation default instructs it.** `second-brain.md` variant B defaults to Tier-2 for single-store-vs-multi-store queries (surface the `contradicts` link proactively).

### 4.2 Graph traversal via `related_findings`

Typed edges exist on findings: `same-problem`, `contradicts`, `extends`, `enables`. Traversal rules:

| Edge type | When to follow | Depth limit |
|---|---|---|
| `contradicts` | Design-debate / decision queries; always when surfacing competing approaches | 1 hop (enough to show the pair; further hops rarely add signal) |
| `extends` | When the Tier-1 pattern is a specialization and the consumer's aspect is the general case | 1–2 hops, stop at first non-extending edge |
| `enables` | When the consumer asks "what unlocks when I adopt X?" — rare | 1 hop |
| `same-problem` | When the Tier-1 answer is one of several approaches to the same problem and the consumer benefits from the menu | 1 hop |

Hard ceiling: **3 hops total across any combination of types per query**. Prevents runaway traversal. If the Librarian hits the ceiling, it stops and reports "further related findings exist; ask if you want them listed."

### 4.3 Tier-2 reads are not narration

Tier-2 findings are attributed, not paraphrased. The Librarian quotes the finding's `Key insight` or `Mechanism` line and cites the finding slug. If the consumer asks for more, the Librarian offers to read the full finding body — explicit next step, not silent expansion.

### 4.4 Stopping criteria

Stop Tier-2 traversal when:
- 3-hop ceiling reached.
- The next hop would enter a different concept file's territory without the consumer asking (keeps queries scoped).
- The Tier-2 additions would not change the answer — diminishing returns.

---

## Step 5 — Tier-3 escalation

Tier 3 = watched-library repos (live GitHub content via `/watch-upstream` caches).

### 5.1 Signals that fire Tier 3

Tier 3 is **consumer-request-gated by default**. The Librarian does not reach Tier 3 on its own unless one of:

1. **Consumer explicitly asks for a reference-implementation comparison** — "how does Claude Code actually do this?", "what's Memongo's implementation look like?"
2. **Consumer is auditing their own artifact against a canonical example** and needs the canonical in view (UC-5.3 harness A-vs-B).
3. **A Tier-1 or Tier-2 answer names a specific mechanism** (hook API, permission config format, MCP handshake shape) and the consumer needs the exact shape to implement or verify.
4. **Concept file's composition table lists a specific watched-library path and the aspect is directly in scope** — even then, the Librarian still states cost and asks before pulling if the read is large.

### 5.2 Read mechanics

- **Cache first.** Read `/watch-upstream` local caches under `watched-libraries/`'s companion cache paths. Do not re-fetch from GitHub unless the cache is missing or the consumer asks for HEAD explicitly.
- **Scoped reads.** Specific file + line range (or directory + heading). Never clone a repo at read time; that's Researcher-side work during `/repo-analyzer`.
- **Attribute precisely.** Cite `watched-lib/path:line-start-line-end` so the consumer can navigate.

### 5.3 Stopping criteria and cost discipline

- One targeted read per consumer-ask. If the first read doesn't resolve the question, ask what the consumer needs specifically — don't keep digging.
- If the read would exceed ~100 KB, ask before reading.
- Tier-3 reads leave a trace in the rolling usage log at `operations/references/librarian/librarian-reads.md` (re-homed 2026-07-12 from `operations/system-log/` when the SL folder froze — DD-116, DD-59 scope note) (per Nick's session-49 gate: IL System Log carries usage-record responsibility; see Q2 resolution below). Append one bullet under the current `## YYYY-MM-DD (session N)` header: `` - `<watched-lib/path>:<range>` — <consumer-ask summary> ``. When the log exceeds ~300 lines, rotate to `archive/librarian-reads-YYYY-QN.md` and start fresh.

---

## Step 6 — Confidence disclosure

### 6.1 Confidence levels

Every substantive claim in the Librarian's response carries a confidence tag:

| Level | Fires when |
|---|---|
| **High** | Tier-1 or Tier-2 substrate directly supports the claim. Invariant / pattern / finding quoted; no interpolation. |
| **Medium** | Substrate supports the claim by inference (e.g., invariant applies to a general case; the consumer's case is a specialization). Librarian states the interpolation step. |
| **Low** | Substrate is thin or indirect. Librarian states the ambiguity reason and lists what additional information (from consumer, from substrate) would raise confidence. |
| **None / gap** | No substrate found. Stated as "the KB does not cover this — the closest-adjacent material is X." Never promoted to a claim. |

### 6.2 When low confidence triggers escalation

Low confidence is a signal to escalate tiers before delivering the answer:

- Low-confidence Tier-1 → try Tier-2 (maybe the mechanism lives in a pattern or finding the guide summarized away).
- Low-confidence Tier-1 + Tier-2 → ask the consumer whether they want a Tier-3 look, and why.

The Librarian never ships a low-confidence answer as if it were high. The confidence label is non-negotiable.

### 6.3 Display

Confidence is visible in the output shape of each operation. In `audit.md`, it's a per-finding column. In prose responses (explain, diagnose), it appears inline after the claim: `… [H | M | L]`. In tabular responses, it's a dedicated column. Concise, not ceremonial.

### 6.4 Gap reports

When the Librarian encounters a KB gap — missing finding, stale guide, broken reference — it produces a **gap report** as a trailing section of the response. Per the agent definition: gap reports are *reported, not fixed*. They are input for Researcher or Codifier work, not autonomous action.

---

## Step 7 — Provenance surfacing

Every claim cites its substrate. Citation format per tier:

| Tier | Format | Example |
|---|---|---|
| 1 | `<guide-file>#<anchor>` (or heading-match fallback) | `managing-agent-context.md#step-2-budget` |
| 2 | `<finding-slug>` or `<pattern-slug>` | `context-rot-attention-budget-depletion` |
| 3 | `<watched-lib>/<path>:<line-start>-<line-end>` | `anthropic-claude-code/src/hooks/registry.ts:42-78` |

Nick: Are we capturing exact links to the original parsed content? I think this would help if provenance. 

### 7.1 Rules

- **Every claim cites.** If there is no citation, the claim is either (a) a summary the Librarian constructed — state that explicitly — or (b) a gap that should be surfaced as such, not asserted.
- **Tier attribution is explicit.** The reader should be able to see at a glance whether a citation is Tier 1 (curated), Tier 2 (raw finding / pattern), or Tier 3 (external ground truth). Where layout permits, tag the tier (`[T1]`, `[T2]`, `[T3]`).
- **Inferred claims mark the inference.** "Based on G2.I2 applied to the case of X, the answer is …" — the reader sees that it's a derivation, not a verbatim quote.
- **Unverified → follow-up, never silent.** Per `audit.md`'s system/process-verifiable pattern — anything that can't be verified from available substrate becomes a follow-up question to the consumer, not a dropped claim.

---

## Step 8 — Consumer-input handling

What each operation expects the consumer to submit, and how size / ambiguity get handled.

### 8.1 Audit queries

- **Expected input.** The artifact itself (inline text) or a file path the Librarian can `Read`.
- **Size scoping.** If the artifact is > ~500 lines, ask for a scoping clarification before auditing the whole thing ("audit the full CLAUDE.md or specific sections?").
- **Missing input.** If the consumer asks "audit my agent" without providing the artifact, ask for it. Do not audit from imagined content.
- **Rejection case.** If the noun doesn't resolve to an agent-system artifact type (e.g., "audit this SQL query"), the operation file `audit.md` states the redirect — handed off to `/prompt-evaluator`, `/security-review`, or language-specific tools.

### 8.2 Diagnose queries

- **Expected input.** A symptom description. Ideally: the context it appears in (single session vs. across sessions, agent configuration, triggering conditions).
- **One qualifying question allowed.** If the symptom is ambiguous ("my agent is slow" — slow in what? latency, throughput, convergence?), ask one clarifying question. Do not chain interrogations.
- **Reproduction not required.** The Librarian diagnoses from symptom → likely cause → pointers. It does not ask for reproduction steps; the consumer may not have them.

### 8.3 whats-new queries

Per Nick's session-49 gate: consumer supplies a `since: <date>` (or equivalent natural-language: "since last week," "in the past month"). The Librarian:

1. Resolves the phrase to an absolute date.
2. Filters substrate by `created` (for findings) or `updated` (for guides) ≥ that date.
3. Returns a date-ordered listing, attributed by substrate.

If no `since` is provided, the Librarian asks — does not pick a default window silently. Removes the dependency on the lifecycle-spec staleness ledger: `whats-new` becomes consumer-parameterized rather than system-timestamped.

### 8.4 Meta / coverage queries

- **Expected input.** A scope (a dimension, a concept, a pattern class). If scope is omitted, ask for one; "everything" is not a serviceable scope.
- **No artifact consumed.** Coverage queries read indices, not substrate bodies. Output is a coverage map, not a synthesis.

### 8.5 Design, decide, explain, fetch, plan

- **Design.** Expect: what's being built + any constraints already fixed. If the consumer hasn't stated a constraint, ask before producing a recommendation.
- **Decide.** Expect: the options the consumer is weighing. If the options are named imprecisely, ask one clarifying question.
- **Explain.** Expect: the thing to explain. No input beyond that; explanation operates on substrate.
- **Fetch.** Expect: the name or description of what to fetch. For templates/rules not by name, the catalog sub-op runs first.
- **Plan.** Expect: the target artifact + any known constraints (timeline, team size). The plan composes over the lifecycle axis.

---

## Step 9 — Boundary and edge cases

Nick: Definitely capture these somewhere (lets explicitly think about where) so that way we can make sure the Librarian remains useful over time and tracks with what the world needs from it.


### 9.1 No concept file resolves

Stated openly: "There is no concept file for `<noun>` yet; falling back to the guide routing table." Proceed with dimension → guide mapping as the poor-man's concept table. Flag the gap in the gap report.

### 9.2 No operation file resolves

Stated openly: "There is no operation file for `<verb>` yet; producing a best-effort response." Derive the subsection kinds to read from the verb's closest canonical analog (for a novel verb, pick the most similar operation's subsection map). Flag the gap.

### 9.3 Ambiguous verb

Ask one disambiguating question: "Do you want to audit (evaluate against criteria) or diagnose (symptom → cause)?" Do not guess.

### 9.4 Oversized artifact (audit / diagnose input)

If the artifact exceeds ~500 lines or the Librarian's working context budget, ask for scope. Never chunk-audit silently (produces inconsistent findings).

### 9.5 Cross-concept queries

Load both concept files. The operation's procedure decides how to compose:
- For `plan`: sequencing across concepts; explicit dependency notes.
- For `audit`: separate rubrics with shared invariants collapsed per `audit.md`'s de-duplication rule.
- For `design`: composition table unions; flag aspects where the concepts disagree or interact.

### 9.6 Verb-noun mismatch

Some operations don't apply to some concepts. Example: `(decide, context-rot)` — decide between what? If the consumer's query is structurally sound but semantically odd, the Librarian asks for the two options being weighed rather than silently reformulating.

---

## Step 10 — Output shape

The operation file dictates output shape (`audit.md` has its own structured output table; `explain.md` will produce narrative-with-citations; etc.). The read-contract adds only these cross-operation elements:

1. **Query restatement.** One line at the top: "Interpreted as: (verb: `<v>`, noun(s): `<n>` [variant: `<var>`])". Lets the consumer catch misinterpretation immediately.
2. **Tier trace.** One line near the top or bottom: "Read: `<n>` Tier-1 sections; `<m>` Tier-2 findings; `<k>` Tier-3 reads." Makes the read-cost visible and auditable.
3. **Confidence tags per claim.** Per §Step 6.3.
4. **Citations per claim.** Per §Step 7.
5. **Gap report** (if any). Trailing section.
6. **Next-step suggestions** (optional, scoped). One or two pointers — "if you want depth on X, ask for the design-debate." Never a dump.

---

## Governance carry-through

All carried forward from `agents/librarian/agent.md`:

- **Read-only on the KB and on the submitted artifact.** The Librarian never rewrites anything.
- **No unsolicited recommendations.** If the operation's output is "audit findings," do not also offer redesign suggestions unless the consumer asked.
- **KB gaps are reported, not fixed.**
- **No general-knowledge padding.** If the KB is thin, state the gap; don't supplement from training data.
- **Stateless across sessions.** Each query re-reads; no cross-session Librarian memory.

Two additions from this read-contract:

- **Tier attribution is non-negotiable.** Every claim is tagged with its tier.
- **SL as usage record.** Per Nick's session-49 gate: the IL System Log carries Librarian-usage-record responsibility. Tier-3 reads append one bullet to the rolling log at `operations/references/librarian/librarian-reads.md` (see §5.3; re-homed 2026-07-12 — the SL folder is frozen read-only history per DD-116/DD-59 scope note). No per-read SL files; no separate usage-log infrastructure outside the SL folder.

---

## Token-budget awareness (meta-concern)

Per Nick's session-49 gate on the use-case registry Q2: reference-layer files have a token budget. When an operation or concept file exceeds a reasonable threshold, it should split — not silently bloat. Threshold is a judgment call, not a line count, but anchors:

- **Operation files** should rarely exceed ~600 lines. `audit.md` at the current size (~165 lines) is well within budget.
- **Concept files** should rarely exceed ~300 lines. `harness.md` (~98), `second-brain.md` (~130) are within budget.
- When a file approaches the threshold, consider splitting by variant (concept files) or by sub-operation (operation files — e.g., `fetch.md` → `fetch-template.md` / `fetch-rule.md` / `fetch-scaffold.md` only if the collapsed file grows too large).

This is a meta-concern of the reference layer's own lifecycle, not a query-time concern. The Librarian does not enforce token budgets at read time; the Codifier respects them at author time.

---

## Relationship to the Librarian agent definition

`agents/librarian/agent.md` states:
- The Librarian's **role** (consumption layer, Teacher / Builder modes).
- The Librarian's **contract** (preconditions, invariants, governance, recovery).
- The Librarian's **scope** (in / out).

This read-contract states:
- The Librarian's **execution protocol** — parse → load → compose → read → assemble → cite.
- The Librarian's **tier escalation rules** — when Tier 1 suffices, when Tier 2 fires, when Tier 3 fires.
- The Librarian's **output discipline** — confidence, provenance, query restatement, tier trace.

The two documents are complementary. If the agent definition ever absorbs this protocol, it should do so as a "how this agent executes" appendix — not as a replacement for the current concise constitution.

---

## Open questions for Nick

1. **Query restatement verbosity.** One line at the top of every response vs. only when the parser's interpretation is non-obvious. Default set here: always restate (cheap, catches silent misinterpretation early). Keep or relax? Nick: Keep.
2. **SL entry shape for Tier-3 reads.** ✓ Resolved session 55 (Owner best-judgment per Nick's standing directive). Shape: rolling file at `operations/references/librarian/librarian-reads.md` (original home `operations/system-log/`; re-homed 2026-07-12), free-form bullet-per-read grouped under `## YYYY-MM-DD (session N)` headers. No per-read frontmatter; no separate usage-log infrastructure outside the SL folder. Rationale: Tier-3 reads are sub-session events (not sessions); per-file SL entries would produce file-count proliferation for one-line content — Occam violation. Rolling file also makes cross-session audit trivial (single file to scan). §5.3 and the Governance carry-through §SL-as-usage-record are concretized accordingly. Rotation to `archive/librarian-reads-YYYY-QN.md` at ~300 lines.
3. **Tier-2 hop ceiling.** Set to 3 hops total. Too generous? Too restrictive? Change once we see actual assess-* traffic, or fix now? Nick: Keep as-is for now, but flag as something to pay attention to and refine with uses of the librarian. This has implications for the Librarian's operations log, which I believe will live in the IL system log for now.
4. **Cross-concept query discipline.** Many real queries will be (operation × concept₁ × concept₂). The read-contract handles it but doesn't formalize a "cross-concept file" artifact. Deferring that feels right; confirming. Nick: Lets leave it alone for now. As an initial thought, maybe part of query restatement is to showcase that the user provided a "compound query" that got decomposed into constituent queries. I think the protocol for something like this should be akin to how search engines like Apache Lucene work - each query is searched in parallel and the content that comes back is combined by the Librarian into the shape that answers the user's query. These queries should probably be done by subagents, which means that the librarian will need a subagent template that is high quality. 
5. **Output shape additions (§Step 10).** Five cross-operation output elements (query restatement, tier trace, confidence tags, citations, gap report, next-step suggestions). Anything to drop, anything to add? Nick: I like it. 

---

## Cross-References

- Librarian agent definition: `agents/librarian/agent.md`
- Use-case registry (Phase 4 output this builds on): `project-management/design-notes/2026-04-21-librarian-use-case-registry.md`
- Substrate audit (Option α', three-tier access model): `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`
- Contract-section spot check (audit composition mechanism): `project-management/design-notes/2026-04-21-contract-section-spotcheck-agent-audit.md`
- Pipeline collapse proposal (`sections[]` manifest, anchor stability): `project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md`
- Reference layer: `operations/references/librarian/` (`_index.md`, `harness.md`, `second-brain.md`, `audit.md`)
- Guide routing table: `operations/references/guide-routing-table.md`
- Research dimensions registry: `operations/references/research-dimensions.md`
- Governing DDs: DD-77, DD-78, DD-80, DD-82, DD-86
