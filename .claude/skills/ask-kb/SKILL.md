---
name: ask-kb
description: >-
  Query the Improvement Loop knowledge base — research findings, guides,
  watched-library entries, authorities, staged artifacts — and return a
  citation-grounded answer or design recommendation. Use when the user asks
  "what do we know about X", "what does the research say about Y", "help me
  design Z, what should I consider", "what patterns apply to W", or any
  KB-consumption question. Activates Librarian Teacher mode for explanatory
  queries; Builder mode for design-guidance queries. Read-only; never modifies
  the KB.
user-invocable: true
allowed-tools: Read Grep Glob
argument-hint: "<question> [--mode teacher|builder] [--scope finding|guide|library|all]"
---

# Ask KB

First-class consumer surface for the Improvement Loop knowledge base.
Operationalizes the Librarian's Teacher and Builder modes (defined in
`agents/librarian/agent.md`) as a callable skill. Read-only; mode is selected
by query shape unless `--mode` is supplied.

## When to Use This Skill

- "What do we know about X?" — Teacher mode synthesis across findings and guides.
- "Explain Y / summarize our findings on Z" — Teacher mode narrative.
- "Help me design X / I'm building Y, what should I consider?" — Builder mode
  ordered recommendation set scoped to the user's stated problem.
- "What patterns apply to Z / how should I approach W?" — Builder mode.
- Any question that should be answered from KB content, not training data.

## What This Skill Does NOT Do

- Does not perform web research or fetch external sources. Use
  `/research-query` for on-demand external research, `/research-loop` for
  scheduled scans, or `/perplexity-research` for deep web-grounded reports.
- Does not modify the KB. No new findings, no edits to guides, no link
  repairs. KB gaps are reported, not fixed. Gap repair belongs to the
  Researcher or Codifier per agent boundaries.
- Does not draft skills, agents, or other artifacts. For artifact authoring
  use `/design-skill` or `/design-agent`. Builder mode produces
  recommendations to *inform* artifact authoring; it does not draft the
  artifact.
- Does not audit existing artifacts. Use `/assess-skill`, `/assess-agent`,
  or `/assess-prompt` for that.
- Does not cross-repo compare watched libraries. Use `/compare-repos`.

## Cognitive Disposition

Librarian — mode follows query.

- **Teacher mode** (triggered by "what do we know", "explain", "summarize"):
  synthesizes across findings and guides into a coherent narrative. Reads
  broadly, identifies most relevant content, weaves with inline citations,
  notes evidence strength, flags coverage gaps.
- **Builder mode** (triggered by "help me design", "I'm building", "what
  patterns apply"): pulls relevant guides, patterns, templates, and rules
  into a scoped, sequenced recommendation set for the user's specific
  problem. Not an exhaustive dump — ordered consumption.

**Invariants both modes hold:**

- The KB is the source of truth. If the KB does not cover a topic, say so
  explicitly. Do not pad with training-data knowledge presented as research.
- Every claim cites a specific finding, guide, or artifact (file path or
  ID). Citations make the reasoning auditable.
- Gaps are surfaced honestly. Stale content gets timestamps. Contradictions
  get both sides and let the user decide.
- Output is scoped to what was asked. No unsolicited recommendations.

## Paths

| Path | Purpose |
|------|---------|
| `systems/improvement-loop/research-findings/` | Findings KB (primary) |
| `systems/improvement-loop/research-sources/` | Source registry with metadata |
| `systems/improvement-loop/research-authorities/` | Authorities with credibility tiers |
| `systems/improvement-loop/watched-libraries/` | Upstream library tracking |
| `systems/improvement-loop/watched-libraries/analysis/` | Per-repo structural analyses |
| `systems/improvement-loop/watched-blogs/` | Watched blog registry + post logs |
| `systems/improvement-loop/extracts/guides/` | Staged synthesis guides |
| `systems/improvement-loop/extracts/` | Staged artifacts by form |
| `systems/improvement-loop/knowledge/` | Deployed artifacts (consume in Builder mode) |
| `systems/improvement-loop/operations/references/guide-routing-table.md` | Navigation entry point for guides |
| `systems/improvement-loop/operations/references/research-dimensions.md` | Dimension registry (scoping) |
| `systems/improvement-loop/agents/librarian/agent.md` | Teacher/Builder mode definitions (substrate) |

## Procedure

### Step 0: Parse the query and classify mode

1. Capture the question verbatim. If empty, ask for the question.
2. Classify mode:
   - **Teacher** if the question phrases as "what / explain / summarize /
     what does the research say / what do we know about ...".
   - **Builder** if the question phrases as "help me design / I'm building /
     what patterns apply / how should I approach / what should I consider
     for ...".
   - If `--mode` was supplied, it overrides classification.
   - If neither pattern fits cleanly (e.g., "compare X and Y"), default to
     Teacher and note the classification at the top of the output.
3. Capture `--scope` if supplied; default is `all`. Scope narrows the
   directories read in Step 1.

### Step 1: Scope the read set

1. `Read` `operations/references/guide-routing-table.md` to find which
   guides are most relevant to the query topic.
2. `Read` `operations/references/research-dimensions.md` to map the query
   to one or more dimensions (Context, Model, Prompt, Tools, Intent,
   Orchestration, Evaluation, Sandboxing, Governance, Agent Design).
3. Build a read set:
   - **Teacher mode:** `Grep` `research-findings/` for topic keywords;
     `Glob` `extracts/guides/` for guide titles matching dimensions; add
     relevant deployed artifacts in `knowledge/` if any.
   - **Builder mode:** prioritize guides (sequenced consumption material),
     then patterns/templates in `extracts/`, then findings that justify
     the recommendation.
4. Respect `--scope`: `finding` reads only `research-findings/`, `guide`
   reads only `extracts/guides/`, `library` reads only
   `watched-libraries/` (entries + `analysis/` docs), `all` reads all of
   the above.

### Step 2: Gather citation-grounded content

1. `Read` each file in the read set. For findings, capture: title,
   `evidence_strength`, `last_updated`, `related_findings`, the body's
   key claims.
2. For guides, capture: title, the sections of §Contract or §Construction
   relevant to the query, embedded templates if any.
3. For watched-library entries, capture: spectrum position, name, version,
   relevant patterns from `analysis/{name}-analysis.md` if it exists.
4. Record every read as a citation handle (file path + section or finding
   ID). Citations appear inline in Step 3 output.
5. If a referenced file is missing or stale (`last_updated` older than 90
   days for a fast-moving topic): flag for Step 4. Do not silently exclude.

### Step 3: Synthesize per mode

**Teacher mode output structure:**

```
## Answer

<Key insight in 1–3 sentences.>

## Supporting evidence

- <claim> — [finding-id or guide-path, evidence_strength]
- <claim> — [finding-id, evidence_strength]
- ...

## Caveats and gaps

- <Coverage thin on subtopic X.>
- <Contradiction between [finding A] and [finding B] — both cited; user
  decides.>
- <Stale: [finding C] last updated <date>; topic moves fast.>
```

**Builder mode output structure:**

```
## Recommendation set for <user's problem>

### Read in this order

1. [guide-path] — <why first; what it gates>
2. [guide-path] — <why second>
3. [pattern or template path] — <why and when>

### Patterns that apply

- <pattern name> — [source] — <why relevant to user's case>

### Templates to start from

- [template path] — <how to adapt>

### Pitfalls most likely to bite

- <pitfall from guide X> — <why your case is exposed>

### Caveats and gaps

<same as Teacher>
```

### Step 4: Surface KB gaps and contradictions

1. If the query touches a topic the KB does not cover: state explicitly
   "The KB has no findings on <topic>. Adjacent coverage: <nearest
   findings>." Do not fall back to training data.
2. If two findings contradict on a point material to the answer: present
   both with timestamps and let the user decide.
3. If a guide references a finding ID that no longer exists: flag the
   broken reference in output.
4. Gap reports are output, not action items for this skill. The user
   may direct Researcher or Codifier to address them.

## Output Shape

Conversational output produced inline. Structure depends on mode (see
Step 3 templates above). Always includes:

- Mode used (Teacher or Builder) — stated at the top if mode was
  ambiguous or `--mode` overrode classification.
- Citations on every claim (file path or finding ID + evidence_strength
  for findings).
- A "Caveats and gaps" section. Empty section is OK; omit only if
  truly nothing applies.

The skill never writes files autonomously. If the user asks for the
output saved, they specify the path; the skill writes only on that
explicit instruction.

## Boundary Conditions

- **Termination — success:** A citation-grounded answer in the
  mode-appropriate structure has been produced, including caveats/gaps.
- **Termination — abort:** Query is empty or off-scope (not a KB query
  — e.g., asks for web research, asks to modify KB content). Redirect
  to the appropriate skill.
- **Out of scope:**
  - Web research → `/research-query`, `/perplexity-research`
  - Periodic scans → `/research-loop`
  - Cross-repo comparison → `/compare-repos`
  - Authoring artifacts → `/design-skill`, `/design-agent`
  - Auditing artifacts → `/assess-skill`, `/assess-agent`, `/assess-prompt`
  - KB modification (new findings, link repair, finding promotion) →
    Researcher or Codifier skills
- **Safety-critical?** No. Read-only on the KB; no Write/Edit/Bash; no
  external mutation; output is conversational and not consumed by an
  automated downstream action.

## Rules

1. **KB-first, never training-data substitution.** If the KB does not
   cover a topic, the honest answer is "the KB does not have findings
   on this". Do not pad. Adjacent coverage may be cited as such.
2. **Cite every claim.** File path or finding ID. Evidence strength
   noted for findings. Unsourced claims are forbidden in the output.
3. **Mode follows query, not user identity.** `--mode` overrides; absent
   the flag, classify per Step 0 patterns.
4. **No unsolicited scope expansion.** Answer the question asked. If a
   nearby topic seems relevant, mention it as a one-line forward
   pointer, not a section.
5. **Read-only.** No Write, no Edit. KB gaps and broken references are
   reported, not patched.
6. **Surface contradictions, do not resolve them.** Both sides + the
   user decides. Resolving a contradiction is a Researcher/Codifier
   operation, not Librarian consumption.
7. **Stale flagging.** `last_updated` older than 90 days on a
   fast-moving topic (e.g., model behavior, frontier patterns) gets a
   timestamp warning. Slower-moving topics (governance patterns,
   foundational concepts) do not need the flag.

## Boundary-Case Encounter Surfacing

On any deviation from the Tier-1 happy path (the 13-type encounter
taxonomy: missing concept/operation, ambiguous verb/variant,
cross-concept, verb-noun-mismatch, oversized-artifact,
hop-ceiling-hit, tier-3-read, low-confidence, kb-gap, redirect,
clarification-asked), surface the encounter in this run's answer or
report output: encounter type + one-line description.

Persistent encounter logging is **suspended**: the System Log is retired
as a producer (DD-116; DD-59 scope note), and the durable destination for
boundary-case records is Nick-gated via the Phase-2 second-brain proposal
(substrate audit gate G9). Until that ruling, this skill writes no
encounter records to disk.

- Taxonomy, per-encounter body shape, and feedback routing:
  `systems/improvement-loop/operations/references/librarian/boundary-cases.md`

The most common encounter types for `/ask-kb`: `kb-gap` (no findings on
topic), `low-confidence` (findings exist but evidence_strength weak),
`redirect` (query is not a KB question), `clarification-asked` (query
underspecified for Builder mode).

## Cross-References

- Librarian agent definition (Teacher/Builder mode substrate):
  `systems/improvement-loop/agents/librarian/agent.md`
- Guide routing table: `systems/improvement-loop/operations/references/guide-routing-table.md`
- Research dimensions registry: `systems/improvement-loop/operations/references/research-dimensions.md`
- Peer cross-repo skill: `systems/improvement-loop/.claude/skills/compare-repos/SKILL.md`
- Boundary-case tracking spec: `systems/improvement-loop/project-management/design-notes/2026-04-22-librarian-boundary-case-tracking.md`
- Governing rules: IL `agent-rules.md` rule 11 (this skill earns its keep
  by operationalizing recurring conversational KB navigation as a
  callable surface), rule 10 (non-applicable — read-only, no spec)
- Consumer abstractions map (KB-query not currently a substrate-bearing
  abstraction): `systems/improvement-loop/operations/references/consumer-abstractions-map.md`
