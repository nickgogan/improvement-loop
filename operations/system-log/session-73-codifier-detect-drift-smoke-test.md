---
title: "Session 73 — Codifier: /detect-drift Smoke-Test + Helper Codification + Librarian Cross-Concept Subagent Template"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Claude (Codifier disposition)"
area: "drift-detection / skill-codification / librarian-protocol"
change_type: "Update"
milestone: null
rationale: "First end-to-end run of /detect-drift (IB-157, session 71) against the live extracts corpus — the validation gate for the IB-157 read paths. Smoke-test surfaced a quote-style heterogeneity bug in inline LLM-driven YAML parsing (false-clean result on the first pass) and Nick directed mid-session codification of Steps 1-2 as a deterministic helper script. After the smoke-test work closed, Nick redirected scope a second time to pull the Librarian cross-concept subagent template (read-contract Q4) into this session — sufficient context was loaded. Three outcome commits + this close. Original-handoff pre-task gate items (session-72 reports 1+2) were not gated by Nick at session start; skipped per handoff direction."
source_dd: "DD-29, DD-77, DD-78, DD-80, DD-82, DD-86, DD-95, DD-96"
date: "2026-04-26"
session: 73
tags:
  - "system-log"
  - "codifier"
  - "detect-drift"
  - "smoke-test"
  - "skill-codification"
  - "librarian"
  - "cross-concept"
  - "subagent-template"
  - "read-contract"
telemetry:
  model: "claude-opus-4-7[1m]"
  tokens_consumed: "unknown"
  context_window_size: 1000000
  context_window_pct_peak: "unknown"
  turns: "~30"
  tool_calls: "~50"
  subagents: 0
  capture_quality: "estimated"
  harness: "claude-code-cli-cursor-macos"
  capture_note: "Three outcome-driven atomic commits (scan.py + SKILL.md update; drift report; cross-concept subagent template) + this close commit. No subagents at any phase. Two mid-session scope redirects from Nick: codify enumeration mid-smoke-test; pull cross-concept subagent template forward from the queue. Markdown fence-nesting bug caught and fixed in the cross-concept template (4-backtick outer fence around 3-backtick inner JSON shape)."
---

# Session 73 — Codifier: /detect-drift Smoke-Test + Helper Codification + Librarian Cross-Concept Subagent Template

## Scope (As Executed)

Three outcome blocks delivered in one Codifier session, all on Codifier-owned territory:

1. **`/detect-drift` smoke-test (original handoff scope).** First end-to-end run of IB-157 against the live `extracts/` corpus. Drift report at `operations/drift-reports/2026-04-26-source-drift.md`.

2. **`scan.py` helper + SKILL.md update (mid-session codification).** Steps 1-2 of `/detect-drift` (enumeration + frontmatter parse + source resolution + strict-greater-than compare) reified as a deterministic Python helper. SKILL.md updated to delegate Steps 1-2 to the helper; LLM-judgment steps (recommendation, report construction) remain in the skill body. Triggered by a smoke-test-surfaced parser bug (see §Smoke-Test Observations).

3. **Librarian cross-concept subagent template (Nick-directed scope expansion).** Workflow file at `agents/librarian/workflows/cross-concept-subagent.md`. Resolves read-contract §Q4 (compound query handling). Lucene-style decomposition: one subagent per `(operation × concept)` pair, parent Librarian recombines via per-operation join rules.

## Smoke-Test Observations (Summary)

Detail in the drift report. Five handoff-specified signals + one surfaced finding:

1. **Enumeration coverage** — 31 / 31 artifacts enumerated (12 rules, 12 skills, 5 templates, 2 agents). Clean.
2. **Source-pointer resolution** — 31 / 31. Clean.
3. **DD-96 amendment field-name (`last_updated`)** — 0 findings carry legacy `updated`. Clean.
4. **Recommendation enum distribution** — 1 hit, 1 `dismiss as cosmetic`. Single data point; full enum exercise deferred.
5. **DD-95 lifecycle-pointer presence** — 31 / 31 backfilled. **Pre-DD-95 graceful-degradation path NOT exercised** — corpus is fully backfilled. Future validation against a deliberate pre-DD-95 fixture is needed.

**Surfaced finding:** YAML quote-style heterogeneity in artifact frontmatter — 27 artifacts double-quoted, 4 single-quoted. The first inline LLM-driven scan returned a false-clean result because the parser stripped only double quotes, silently masking the one real drift hit (lexical compare of `"'2026-04-20'"` vs `"2026-04-19"` returns False). Caught via spot-check after the clean result felt suspicious.

## Drift Hit (Pending Nick Gate)

`rules/agent-self-reporting-unreliability-independent-eval` — source updated 2026-04-20, extracted 2026-04-19. Recommendation: `dismiss as cosmetic`. Source body's update appears administrative (extraction-note section, `consumed_by` list growth, `pipeline_status: synthesized`); artifact substance unchanged. PENDING Nick gate.

## Skill Codification Rationale (`scan.py`)

The smoke-test demonstrated that LLM-driven YAML parsing across 31 files is not reliable enough for a contract-bearing skill — the quote-style bug went unflagged across the entire scan. Codifying the deterministic part:

- **What's now in `scan.py`:** enumeration, frontmatter parse (both quote styles), source resolution, missing-field gap-logging, strict-greater-than YYYY-MM-DD compare. Argparse-driven, JSON output, read-only invariant preserved.
- **What stays in the skill body (LLM):** recommendation per drift hit (closed-enum `re-run` / `dismiss as cosmetic` / `reclassify`) — requires reading source content delta and judging substance; report construction; ambiguity-note handling.
- **Hybrid result:** for a corpus of N artifacts with K drift hits, the skill collapses from O(2N) LLM file reads to one script invocation + O(K) LLM source-content reads. The 31/1 case here: 62 file reads → 1 script call + 1 source read.

SKILL.md updated to: add `Bash` to allowed-tools, add `scan.py` to Paths, rewrite Steps 1+2 as a single "invoke helper + load JSON" step (renumber subsequent Steps 3-5 to 2-4), update Failure Modes table to reference scan.py for parser/source-resolution failures.

## Cross-Concept Subagent Template Rationale

Read-contract §Q4 (2026-04-21) recorded Nick's design intent for compound queries: "the protocol for something like this should be akin to how search engines like Apache Lucene work — each query is searched in parallel and the content that comes back is combined by the Librarian into the shape that answers the user's query. These queries should probably be done by subagents, which means that the librarian will need a subagent template that is high quality."

UC-9.2 ("I want an agent + hybrid second brain — in what order?") was the canonical example: `(plan, agent[variant])` and `(plan, second-brain[hybrid])` dispatched in parallel.

The workflow file authored this session encodes:

- **Decomposition rules** — one subagent per concept, cap at 4, single shared operation, variant resolution before dispatch.
- **Invocation contract** — `Task` tool with `subagent_type: general-purpose`, parameter substitution table.
- **Parameterized subagent prompt** — read-only invariant, no clarifying questions (would block parallelism), Tier-2 gated, Tier-3 forbidden at child level, structured JSON output with `cross_concept_hooks` for the parent.
- **Recombination logic** — per-operation join rules across all 9 operation files, confidence-conflict resolution, tier-trace merge.
- **Worked example** — UC-9.2 dispatch, expected hooks, recombined output shape.
- **Failure modes** — malformed JSON, timeouts, contradicting H-confidence claims, missing join rules, ambiguous variants.

## Deviations from Original Handoff

1. **Pre-task gate items not applied.** Session-72 items 1 + 2 reports (`2026-04-26-identification-report-2.md`, `priority-reassessment-2026-04-26-spec-as-governance.md`) carry no `Status` field and PROGRESS.md confirmed both PENDING Nick gate at session start. Skipped per handoff direction ("If not gated, leave alone — don't block on it").

2. **Mid-session scope expansion (1) — codify scan.py.** The handoff scoped "up to two atomic commits" (optional pre-task + main outcome). Adding `scan.py` + SKILL.md changes pushed scope to three outcomes. Nick-directed after the smoke-test parser-bug surfacing.

3. **Mid-session scope expansion (2) — Librarian cross-concept subagent template.** Nick redirected after the smoke-test work closed: "lets do this one next please" (referring to the Librarian subagent template queue line). "We have enough context" — context-load already covered the read-contract via the smoke-test reads. Pulled forward from the queue rather than deferred to a session-74 handoff.

4. **PROGRESS.md uncommitted reorder preserved.** A queue-line swap (Retroactive migration ↔ G7/G2/G9 re-synthesis) was uncommitted at session start — likely Nick's tweak between handoff and invocation. Preserved; rolled my close edits on top.

## Markdown-Fence Note

The cross-concept subagent template's outer prompt fence uses 4 backticks (the inner JSON output-shape block uses 3 backticks). First-pass authoring used 3-backtick fences for both, which silently scrambles the second half of the template under CommonMark (the inner closing fence terminates the outer block). Caught by spot-check before commit.

## Reference-Layer Implications (Surface, Not File)

**Operation files need a "join rule" subsection.** The cross-concept subagent template's recombination logic relies on each operation file documenting how to merge multiple per-concept outputs. The template names a join rule for each of the 9 current operations (`plan` / `audit` / `design` / `decide` / `diagnose` / `explain` / `fetch` / `whats-new` / `coverage`), but those rules are stated in the *template*, not in the *operation files themselves*. If the operation files are the source of truth for "how this operation behaves," they should carry the join rule. Surfaced for Owner / Nick to gate as IB candidate (not filed inline per standing rule).

## Atomic Commits

| # | SHA | Message |
|---|---|---|
| 1 | 19507f7 | Session 73: codify /detect-drift Steps 1-2 as scan.py helper |
| 2 | a0c5648 | Session 73: first /detect-drift smoke-test report against live corpus |
| 3 | e6cf546 | Session 73: Librarian cross-concept subagent template (read-contract Q4) |
| 4 | (this commit) | Session 73: close — SL + PROGRESS retarget |

## What's Pending Nick Gate

- **Drift hit** — `rules/agent-self-reporting-unreliability-independent-eval` recommendation `dismiss as cosmetic`. Per skill's read-only contract, no auto-action.
- **Session-72 items 1 + 2** — still PENDING. Carried forward.
- **Operation-file join-rule subsection** — surface from cross-concept template authoring; Owner-routable IB candidate.
