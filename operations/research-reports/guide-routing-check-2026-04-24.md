---
name: "Guide-Routing Check — Session 63"
description: >-
  Guide-routing check (DD-81) over newly-P2 pattern findings from session 62.
  Routes 12 P2 patterns via the Dimension → Guide mapping in
  operations/references/guide-routing-table.md. Flags scope filter (P3
  findings excluded), verifies pattern-shape for two IB-149 primary bumps,
  and surfaces a subagent-governance co-occurrence cluster that is interesting
  but not unrouted.
type: "routing-report"
target_system:
  - "improvement-loop"
created: "2026-04-24"
session: 63
agent: codifier
source_dd:
  - "DD-81"
---

# Guide-Routing Check — Session 63

## Scope and Filter

The handoff table listed 15 finding rows. Applying the "P2 only" rule yields **12 P2 pattern findings in scope**. Three findings in the handoff table carry `priority: P3` in frontmatter and are therefore excluded from routing per the rule, though listed here for traceability.

| Handoff # | Finding | Category | Priority | In Scope? |
|-----------|---------|----------|----------|-----------|
| 1 | `external-benchmark-hosting-as-trust-mechanism` | Governance | P3 | No |
| 2 | `benchmark-dataset-deprecation-lifecycle` | Governance | P3 | No |
| 3 | `experimental-sandbox-labeling-discipline` | Governance | P3 | No |
| 4 | `ensemble-eval-majority-required-for-success` | Evaluation | P2 | Yes |
| 5 | `production-configuration-baseline-discipline` | Evaluation | P2 | Yes |
| 6 | `personal-knowledge-hoard-as-agent-substrate` | Context Engineering | P2 | Yes |
| 7 | `interactive-explanations-extend-linear-walkthroughs` | Context Engineering | P2 | Yes |
| 8 | `subagent-scope-priority-ladder` | Governance | P2 | Yes |
| 9 | `inline-scoped-mcp-servers-per-subagent` | Context Engineering | P2 | Yes |
| 10 | `subagent-persistent-memory-directory` | Memory Architecture | P2 | Yes |
| 11 | `capability-restricted-agent-spawning-via-allowlist` | Governance | P2 | Yes |
| 12 | `subagent-isolation-contract` | Agent Design | P2 | Yes |
| 13 | `foreground-vs-background-subagent-permission-models` | Governance | P2 | Yes |
| 14 | `cross-platform-context-file-strategy` | Context Engineering | P2 | Yes (form verified — see §2) |
| 15 | `memory-bank-isolation-per-agent-per-project` | Memory Architecture | P2 | Yes (form verified — see §2) |

**Note on the 7 vs 3 P3 accounting.** The handoff rule says "Do not route the 7 P3 findings." Session 62 classified 18 findings yielding 11 × P2 + 7 × P3 priorities. Of the 7 P3s, only 3 appear in the handoff table (the other 4 were non-patterns or otherwise not routing candidates). This report filters on the P3 marker directly rather than rely on count reconciliation.

## Form Verification for IB-149 Primary Bumps (#14, #15)

Both findings carry `pipeline_status: raw` — they were P3→P2 bumped via IB-149 but never run through `/identify-artifacts`. Pattern-shape verification inline:

### #14 `cross-platform-context-file-strategy`
- **Body shape.** Describes three reusable *strategies* (platform-specific mirroring, chain-loader indirection, content duplication) for a single architectural concern (multi-tool context portability).
- **Not a rule.** No enforceable "always/never" constraint; presents options.
- **Not a skill.** No procedure or step sequence.
- **Not a template.** No fill-in scaffold.
- **Not an agent spec.** No identity/disposition definition.
- **Verdict: pattern.** Reusable architectural approach with multiple realizations. Routes per Context Engineering.

### #15 `memory-bank-isolation-per-agent-per-project`
- **Body shape.** Describes a memory-architecture principle with one canonical realization (Hindsight's bankId/channel primitives) and several related realizations via same-problem links.
- **Not a rule.** Closest to one, but phrased as design principle rather than binding constraint. The MetaSystem-specific `implementation_notes` read as adoption guidance, not enforcement.
- **Not a skill / template / agent.** As above.
- **Verdict: pattern.** Reusable memory-topology approach. Routes per Memory Architecture (which the routing table admits under G7's dimensions list).

## Routing Decisions (12 P2 Patterns)

Using `operations/references/guide-routing-table.md` (Dimension → Guide Mapping) and the `category:` field on each finding:

| # | Finding | Category (frontmatter) | Primary Guide | Secondary | Status |
|---|---------|------------------------|---------------|-----------|--------|
| 4 | `ensemble-eval-majority-required-for-success` | Evaluation | **G4** (Evaluation Suites) | G6 (Safety) | Routed |
| 5 | `production-configuration-baseline-discipline` | Evaluation | **G4** | G6 | Routed |
| 6 | `personal-knowledge-hoard-as-agent-substrate` | Context Engineering | **G2** (Managing Context) | G7 (Session/Memory) | Routed |
| 7 | `interactive-explanations-extend-linear-walkthroughs` | Context Engineering | **G2** | G7 | Routed |
| 8 | `subagent-scope-priority-ladder` | Governance | **G9** (Governance and Trust) | — | Routed |
| 9 | `inline-scoped-mcp-servers-per-subagent` | Context Engineering | **G2** | G7 | Routed |
| 10 | `subagent-persistent-memory-directory` | Memory Architecture | **G7** | — | Routed |
| 11 | `capability-restricted-agent-spawning-via-allowlist` | Governance | **G9** | — | Routed |
| 12 | `subagent-isolation-contract` | Agent Design | **G10** (Agent Design Patterns) | — | Routed |
| 13 | `foreground-vs-background-subagent-permission-models` | Governance | **G9** | — | Routed |
| 14 | `cross-platform-context-file-strategy` | Context Engineering | **G2** | G7 | Routed |
| 15 | `memory-bank-isolation-per-agent-per-project` | Memory Architecture | **G7** | — | Routed |

**Per-guide inflow from this session (P2 only):**
- G2 (Managing Context): +4 (#6, #7, #9, #14)
- G4 (Evaluation Suites): +2 (#4, #5)
- G7 (Session/Memory): +2 (#10, #15)
- G9 (Governance and Trust): +3 (#8, #11, #13)
- G10 (Agent Design Patterns): +1 (#12)

## Unrouted Bucket — Status

**No additions from this sweep.** All 12 P2 patterns route cleanly to existing active clusters. The Unrouted Bucket in `guide-routing-table.md` remains at its prior state (2 Agentic Systems findings from session 43, below the 5-finding graduation threshold).

**No candidate guide clusters to flag.** The graduation trigger (5+ unrouted same-problem-linked findings) is not met.

## Observation — Subagent-Governance Theme (Routed, Not Unrouted)

Findings #9, #10, #11, #12, #13 all derive from the Anthropic Claude Code subagents documentation and cluster via `same-problem` around `subagent-isolation-contract` (#12). Five findings hub on this concept. They route cleanly to four different guides (G2, G7, G9, G10), so this is **not** an unrouted cluster signal. But the theme is dense enough that cross-guide synthesis may matter when G9 and G10 are next re-synthesized: a reader asking "how should I govern subagent boundaries?" will land on at least three guides. Worth noting for future `/synthesize-guide` runs; not action-forcing now.
- Nick: Good point, it's worth keeping an eye on.

## Side Findings (Flagged, Not Actioned)

### S1. `pipeline_status: raw` on #14 and #15
Both IB-149 primary bumps carry `pipeline_status: raw` in frontmatter, despite being form-verified here as patterns and routed to guides. Conventional pipeline state would be `classified`. Two options:
- **A.** Advance both to `classified` now (small frontmatter edits, consistent with their actual state).
- **B.** Leave as-is; let the next `/identify-artifacts` run reclassify them formally.

Recommendation: **A**, gated on Nick's approval of this report. Cost is trivial; consistency benefit is real for future `/extract-artifacts` filters that key on `pipeline_status`.
- Nick: Agreed, lets clean this up please. 

### S2. "Memory Architecture" as a category
Findings #10 and #15 carry `category: Memory Architecture`, which is not a top-level research dimension. The routing table accommodates it (G7's Dimensions field lists "Context, Orchestration, Memory Architecture"), so routing works, but there's a taxonomy mismatch between `research-dimensions.md` (Dimension 1 Context Engineering → Sub-dimension 1.A Memory Decay) and how these findings self-describe. Neither #10 nor #15 is about decay — they're about memory *isolation* and *persistence topology*.

Two cleanup options, both outside this session's scope:
- **Reclassify** #10 and #15 into Context Engineering (parent dimension) and drop "Memory Architecture" as a category.
- **Add a sub-dimension 1.B** (Memory Isolation / Topology) under Context Engineering to give these findings a registered home.
- Nick: I like the idea of enriching the research taxonomy's context engineering dimension with sub-dimension(s). Please create a proposal. Based on that, we may need to queue a Research re-run over the KB to re-classify properly. This is a good and expected thing though.

Surfaced for Nick; not blocking routing.

### S3. Hardcoded counts in the routing table
The Active Clusters table in `guide-routing-table.md` has a "Finding Count (P1)" column that will drift from reality with each routing sweep. Per the feedback-memory standing on no-hardcoded-counts, this report deliberately does **not** bump those numbers — they drift, they require per-session maintenance, and they're better sourced by ripgrep on frontmatter at read time. If the routing table's counts matter to downstream readers, proper fix is mechanism (script or Dataview), not manual updates. Flag for Owner-scope later.
- Nick: Great catch! Yes, let's remove this enumeration please.

## Deviations from Skill Contract

None substantive. This session was invoked via a handoff, not a direct `/identify-artifacts` subagent batch. The routing logic follows DD-81's spec in `guide-routing-table.md` §Routing Rules "For `/identify-artifacts`". No subagent parallelization was needed since the scope is 12 findings and the routing decisions are deterministic lookups.

## Proposed Next Actions

1. **Nick gates this report.** Confirm P3 filter interpretation, form verifications, and the two side-finding recommendations (S1 action; S2 and S3 deferred).
2. **Routing-table updates.** None required for the Active Clusters or Dimension → Guide mapping. The Unrouted Bucket is unchanged.
3. **`pipeline_status` cleanup (S1).** If approved, advance #14 and #15 from `raw` to `classified` (two frontmatter edits).
4. **Proceed to `/extract-artifacts`** (secondary task per handoff) on the APPROVED set from session 62 — 16 findings including the 1 rule (`confirm-failure-first-tdd-agent-discipline`). Nick's call on inline vs subagent-batch execution (session 62 ran `/identify-artifacts` inline as a flagged deviation; same option available here).

## Telemetry

| Field | Value |
|---|---|
| model | claude-opus-4-7[1m] |
| session | 63 |
| agent | Codifier |
| findings_in_scope | 12 |
| findings_out_of_scope | 3 (P3) |
| routed | 12 |
| unrouted | 0 |
| candidate_clusters_flagged | 0 |
| form_verifications_performed | 2 (#14, #15) |
| subagents | 0 (deterministic routing — no parallelization required) |
| harness | claude-code-cli-cursor-macos |
