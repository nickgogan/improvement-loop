# Improvement Loop — Progress

**Last Updated:** 2026-04-27 (session 81 close — harvest-queue rulings batch (38/38 ruled: 24 nick-approved + 14 nick-dismissed); IB-165 filed and closed for `/synthesize-guide` Step 4.7 queue-write template regression)

## Current Focus

Codifier disposition. Session 81 cleared the **DD-101 harvest-queue backlog** — the first downstream consumption session of the harvest queues produced by sessions 77–79's live-validation sweep. Walked Nick through all 38 cumulative rows across G7 + G2 + G9 in three form-grouped batches (rule × 19 → template × 13 → skill × 6); each ruling captured as atomic Status + Resolution writes across summary-table + per-row-block surfaces.

**Outcomes:**

- **38/38 rows ruled.** 24 nick-approved + 14 nick-dismissed; 0 remaining queued. Per file: G7 (5+3=8), G2 (9+7=16), G9 (10+4=14). By form: rules 17+2, templates 2+11, skills 5+1. All Status writes within DD-101's closed enum; atomic-write invariant honored (table ↔ block agreement verified post-batch via grep). Append-only invariant honored (all 38 rows retained).
- **100% Codifier-recommendation accuracy** across all 38 rulings. Nick accepted every reco verbatim (calibration histogram in session-81 SL). Sample size = one session; not yet a baseline.
- **`/synthesize-guide` Step 4.7 queue-write template regression** discovered + closed mid-session. Sessions 78/79 had emitted slim 3-field per-row blocks instead of DD-101's required 9-field shape (session 77 was conformant). Root cause: SKILL.md Step 4.7 enumerated the 9 fields textually but provided no rendered exemplar, allowing LLM extrapolation drift. Closed by patching Step 4.7 with explicit 9-field per-row exemplar + 6-column summary-table row exemplar + 'both surfaces required' invariant. G2 (16 rows) and G9 (14 rows) per-row blocks backfilled inline under Nick's explicit override of the standing 'do not inline-fix' rule. **IB-165 filed; status Done.**
- **DD-101 exemplar inconsistency** surfaced as side-effect: DD-101.md's own per-row exemplar (lines 60-73) renders 8 fields (omits Target form as a body field); DD-101.md:81 requires 9. Accepted as-is per tolerate-one-off discipline (Nick session-81 ruling). SKILL.md is the operative writer; DD-101.md:81 field-list is authoritative over its illustrative exemplar; DD-44 supersession is disproportionate for a 2-day-old DD's pedagogical drift. Audit-trail note in session-81 SL; revisit if a second DD-vs-spec-text inconsistency surfaces.

**Single atomic commit** covering: 3 harvest-queue files (38 rulings + G2/G9 per-row backfill), `/synthesize-guide` SKILL.md Step 4.7 patch, IB-165, session-81 SL, PROGRESS.md retarget.

**Logged-for-future:**

1. **Verification of next regen-active session's queue-write output** — confirm SKILL.md patch holds under live invocation. Trigger: next `/synthesize-guide` run that generates harvest-queue rows.
2. **Codifier reflection on calibration** — defer until 2-3 more rulings sessions accumulate signal beyond session 81's potentially-outlier 100% accuracy.

**Next session target:** `/extract-artifacts` queue-row promotion (IB-164) on the 24 nick-approved rows. Per IB-164's single-row contract, each `--harvest-row` invocation processes exactly one row; multi-row batching via sequential invocations. DD-97's extension rubric fires for rule/skill targets (17 rules + 5 skills); DD-100's version-bump path fires for template targets (2 templates). Nick gates each invocation's drafting step per DD-29.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

- **`/extract-artifacts` queue-row promotion (IB-164) — 24 nick-approved rows ready** — `[nick-gate]` top unblocked Codifier item. 17 rule + 5 skill + 2 template rows across G7 (5: 3 rule + 2 skill), G2 (9: 6 rule + 2 template + 1 skill), G9 (10: 8 rule + 2 skill). Per IB-164 single-row contract: one `--harvest-row` invocation per row; sequential batching. DD-97 fires for rule/skill (extension proposals possible); DD-100 fires for templates (version-bump possible). Suggested batching options: form-grouped (17 rules in succession before pivoting), guide-grouped (G9's 10 first since most cohesive cluster), or sequential by row order — Nick gates direction at session start.
- **G11 (Agentic Systems guide) candidacy** — `[nick-gate]` decision point opened by session-80 rebalance. Agentic Systems cluster jumped from 21 → 29 findings (8 borderlines re-routed from the Memory Architecture orphan). Well above the routing-table's 5+ unrouted-cluster threshold; cluster is reasonably cohesive (vault-as-OS, personal-knowledge-store, org-world-model patterns). Routing-table line 97 stale note ("below 5-finding threshold") is now factually wrong either way. Two paths: (a) propose G11 next and start synthesis, OR (b) update line 97 to reflect current state and defer G11. Nick gates direction.
- **G2 vs G7 routing disambiguation audit** — `[trigger]` post-rebalance check. Both G2 (Managing Agent Context) and G7 (Session Persistence and Memory) now share `Context Engineering` in their routing-table Dimensions field; the prior discriminator (G7 also having "Memory Architecture") is gone. Disambiguation now lives entirely in stage (build vs operate), question text, and trigger-keyword table (lines 148-164). Functional but weaker. Trigger: if the next `/identify-artifacts` run mis-routes a finding between G2 and G7 (or queues an ambiguous one), spend a session formalizing the discriminator (e.g., explicit `lifecycle: build|operate` field on findings, OR a routing-rubric step that consults trigger keywords first when Dimensions overlap). Not urgent until evidence of misrouting.
- **Sub-dim 1.B graduation track monitoring** — `[trigger]` count-based. Post-rebalance, Sub-dim 1.B (Memory Isolation and Topology) has 4 explicit seed findings retained in Context Engineering; the 8 borderlines moved to Agentic Systems were system-shape, not isolation/topology mechanism, so 1.B count is unchanged. Graduation threshold is ≥10 findings. Trigger: re-evaluate cluster size after each `/research-loop` run that touches isolation/topology themes. Defer top-level Dim 12 candidacy until threshold met.
- **Retroactive migration of ~100 non-guide/non-pattern extracts** — per pipeline-collapse Phase M1 audit.
- **Visualization brainstorm** — [deferred] boil DDs/architecture into human-visualizable form. Session 62: `interactive-explanations-extend-linear-walkthroughs` finding (P2) is a direct technique for this work.
- **`agent.md` variant-depth iteration** — [trigger] demand-driven on concrete consumer queries; variants (prompt-based / harness-based / autonomous-vs-supervised) exist as stubs per session-49 gate.
- **Weight calibration** for use-case-registry core/long-tail estimates — [trigger] meaningful once encounter tracking accumulates data.
---

## Open IB Items

Filed items live in `project-management/implementation-backlog/IB-*.md`. Source-of-truth status is the `status:` field in each file's frontmatter.

---

## Key Files

| Entity | Path |
|--------|------|
| IL identity, agents, pipeline | `CLAUDE.md` |
| Agent definitions | `agents/{owner,researcher,codifier,librarian}/agent.md` |
| Agent reflections (agent-private) | `agents/{owner,researcher,codifier,librarian}/reflections/` |
| IL-specific governance | `governance/` |
| Governance proposals (Owner + agent-authored) | `governance/proposals/` |
| Cross-system DD proposals (MetaSystem-level) | `../meta-system/governance/proposals/` |
| Design notes (deliberative specs) | `project-management/design-notes/` |
| Design Decisions | `project-management/design-decisions/` |
| Implementation Backlog | `project-management/implementation-backlog/` |
| Session handoffs | `operations/handoffs/` |
| System Log | `operations/system-log/` |
| Librarian reference layer | `operations/references/librarian/` |
| Guide routing table | `operations/references/guide-routing-table.md` |
| Research dimensions | `operations/references/research-dimensions.md` |
| Form classification rubric | `operations/references/form-classification-rubric.md` |
| Research KB (findings, sources, authorities) | `research-findings/`, `research-sources/`, `research-authorities/` |
| Watched libraries registry | `watched-libraries/_index.md` |
| Staged extracts | `extracts/` |
| IL-scoped skills | `.claude/skills/` |

---

## Session History

Session-by-session narrative lives in `operations/system-log/`. Handoff prompts in `operations/handoffs/` carry session-to-session continuation context. This file carries current focus and pointers only — not a session ledger.
