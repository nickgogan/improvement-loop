# Handoff: Session 63 — Codifier Guide-Routing + /extract-artifacts

## IDENTITY AND SOUL

You are the **Codifier** agent in the Improvement Loop. Your disposition: precise, form-aware, completeness-driven. You treat classification and routing as disciplines — rubric first, exceptions flagged, co-occurrences noted but not acted on. You don't rubber-stamp skill-contract text when it conflicts with evidence; you surface the tension and let Nick rule. You are methodologically transparent — when you deviate from a skill's stated procedure, you name the deviation rather than hide it.

Nick is the bridge between Claude Build and Household OS, and the architect of MetaSystem. He files Design Decisions; you execute rubric-driven mechanics within them. He gates content, you run procedure.

**Project context:** The Improvement Loop is a research intelligence layer. Findings flow Extract → Identify → Extract (artifacts) → Deploy. Session 62 closed IB-149 (2 priority bumps), evolved research-dimensions.md with a Memory Decay sub-dimension, and classified 18 null-priority findings inline (17 pattern + 1 rule). Your job now is the routing + drafting follow-through.

## YOUR TASK

**Primary:** Guide-routing check (DD-81) over **all newly-P2 pattern findings** from session 62. For each pattern, match `category:` → research dimension → guide cluster per `operations/references/guide-routing-table.md`. Routed findings need no change. Unrouted findings go into the table's **Unrouted Bucket**. If 5+ same-problem-linked findings accumulate there, flag a candidate guide cluster (do not create the guide — surface for Nick).

Routing scope — 12 findings:

| # | Filename | Category | Notes |
|---|---|---|---|
| 1 | `external-benchmark-hosting-as-trust-mechanism.md` | Governance | session-62 auto |
| 2 | `benchmark-dataset-deprecation-lifecycle.md` | Governance | session-62 auto |
| 3 | `experimental-sandbox-labeling-discipline.md` | Governance | session-62 guided |
| 4 | `ensemble-eval-majority-required-for-success.md` | Evaluation | session-62 guided |
| 5 | `production-configuration-baseline-discipline.md` | Evaluation | session-62 guided |
| 6 | `personal-knowledge-hoard-as-agent-substrate.md` | Context Engineering | session-62 auto |
| 7 | `interactive-explanations-extend-linear-walkthroughs.md` | Context Engineering | session-62 auto |
| 8 | `subagent-scope-priority-ladder.md` | Governance | session-62 guided |
| 9 | `inline-scoped-mcp-servers-per-subagent.md` | Context Engineering | session-62 auto |
| 10 | `subagent-persistent-memory-directory.md` | Memory Architecture | session-62 auto |
| 11 | `capability-restricted-agent-spawning-via-allowlist.md` | Governance | session-62 auto |
| 12 | `subagent-isolation-contract.md` | Agent Design | session-62 auto |
| 13 | `foreground-vs-background-subagent-permission-models.md` | Governance | session-62 auto |
| 14 | `cross-platform-context-file-strategy.md` | Context Engineering | **IB-149 primary bump; form not yet verified — verify pattern-shape first** |
| 15 | `memory-bank-isolation-per-agent-per-project.md` | Memory Architecture | **IB-149 primary bump; form not yet verified — verify pattern-shape first** |

*(Table is 15 rows because #7 in session-62's list — `confirm-failure-first-tdd` — is a rule and does not route per DD-81. Included here for completeness are the 13 session-62 patterns + 2 IB-149 primary bumps = 15.)*

**Secondary (if time permits):** `/extract-artifacts` on the APPROVED set from session 62. Draft artifacts per DD-78 ContractSpec and stage in `extracts/`. This includes the 1 rule (`confirm-failure-first-tdd`) since rules extract too, just outside the routing table.

## RULES

- **Routing first, extraction second.** Don't dive into `/extract-artifacts` before the routing sweep is complete.
- **Pattern-only routing per DD-81.** Rule/skill/template/agent forms don't participate in the routing table.
- **Form verification for pre-existing findings.** Entries #14 and #15 were not run through `/identify-artifacts`; confirm pattern-shape before adding to the routing table. If ambiguous, defer to Nick with a short rationale.
- **Do not route the DEFERRED findings.** `agentic-search-memory-retrieval-architecture` and `agent-native-app-store-emerging-category` are held on evidence grounds; out of scope.
- **Do not route the 7 P3 findings.** Scope is P2 only.
- **Unrouted accumulation is a signal, not a bug.** 5+ same-problem-linked unrouted findings → candidate guide cluster. Flag in the report; don't create the guide.
- **Staged artifacts only** (DD-39 / DD-80). `/extract-artifacts` writes to `extracts/`, never to `meta-system/knowledge/` or `.claude/`.
- **No body edits to findings.** Only frontmatter (and only `pipeline_status` / `consumed_by` on extraction).
- **No new DDs without Nick's gate.** Surface governance questions; don't file Binding DDs.
- **Inline-vs-subagent decision for `/extract-artifacts` is Nick's call.** Session 62 ran `/identify-artifacts` inline; mention the same deviation option if going inline again.

## KEY REFERENCES

| Entity | Path |
|---|---|
| Session-62 SL (full context) | `systems/improvement-loop/operations/system-log/session-62-codifier-ib-149-reassess.md` |
| Session-62 identification report (Nick-annotated) | `operations/pattern-identification-reports/2026-04-24-identification-report.md` |
| Session-62 reassessment report (Nick-annotated) | `operations/research-reports/priority-reassessment-2026-04-23.md` |
| Guide routing table (DD-81 target) | `operations/references/guide-routing-table.md` |
| Research dimensions (with new sub-dimension 1.A) | `operations/references/research-dimensions.md` |
| Form classification rubric | `operations/references/form-classification-rubric.md` |
| `/extract-artifacts` skill | `systems/improvement-loop/.claude/skills/extract-artifacts/SKILL.md` |
| `/identify-artifacts` skill | `systems/improvement-loop/.claude/skills/identify-artifacts/SKILL.md` |
| Codifier agent definition | `systems/improvement-loop/agents/codifier/agent.md` |
| IL PROGRESS (current focus + queue) | `systems/improvement-loop/PROGRESS.md` |
| Workspace PROGRESS | `PROGRESS.md` |
| IL CLAUDE.md | `systems/improvement-loop/CLAUDE.md` |
| Governance rules | `.claude/rules/governance.md` |

## CONTEXT FROM PRIOR SESSION (62)

### Resolved

- **IB-149 closed.** 2 priority bumps applied (`cross-platform-context-file-strategy` P3→P2; `memory-bank-isolation-per-agent-per-project` P3(Monitor)→P2). 2 holds confirmed (`specification-as-governance-fourth-enforcement-philosophy` stays P2 per skill rubric; decay cluster unchanged per Nick's hold).
- **Taxonomy evolved.** `research-dimensions.md` now carries Sub-dimension 1.A (Memory Decay, Forgetting, and Compaction) with graduation criteria. Side-fix: stale hardcoded count in `operations/references/CLAUDE.md` softened.
- **Drift §1 + §2 classification complete.** 18 null-priority findings classified inline (deviation from subagent-batch contract — flagged in report). 16 APPROVED, 2 DEFERRED on evidence. 11 × P2 + 7 × P3 priorities applied. All 18 moved `raw → classified`.
- **Skill-contract tension surfaced** on Candidate 2: IB-149's "P2→P1" claim vs rubric's 5+ threshold. Rubric governed; Nick ruled hold.

### Unresolved (carry into session 63)

1. **Guide-routing check** (this session's primary task).
2. **`/extract-artifacts` on 16 APPROVED** (secondary task — scheduled after routing).
3. **Candidate 2 re-evaluation** at 4th–5th independent-repo surfacing.
4. **Decay cluster cluster-normalization** if decay becomes a near-term build target.
5. **Upstream `/promote-findings` drift:** priority-assignment ownership gap (which skill owns initial-priority assignment?). Owner-level governance work. Flagged in SL; not for this session unless Nick redirects.
6. **G7 / G2 / G9 re-synthesis** still blocked on Lifecycle-spec Phase-1 DDs (DD-X1, DD-X3, DD-X4).

### Deferred

- Re-evaluate `agentic-search-memory-retrieval-architecture` (#6) when 2nd production source arrives.
- Re-evaluate `agent-native-app-store-emerging-category` (#17) when evidence matures.
- DD-78 amendment (Contract triple-role) — reference layer not yet exercised.
- First `/solicit-proposals` round — six-times-deferred; Owner scope.
- Librarian subagent template for cross-concept queries (IL queue #3).
- DD-65 full supersession (skill-inventory drift).

## OUTPUT REQUIREMENTS

1. **Routing report** at `operations/research-reports/guide-routing-check-{date}.md`. Include: patterns scanned, routed/unrouted split per pattern, any candidate guide clusters detected, verification notes on #14 and #15 form-shape.
2. **Routing table updates** applied after Nick's approval of the report's findings.
3. **If `/extract-artifacts` runs:** staged artifacts in `extracts/` per form. Back-annotate `pipeline_status: extracted` and `consumed_by:` on consumed findings. Human gate before writing unless `--auto`.
4. **SL entry** at session end logging decisions, deviations, and follow-ups.
5. **Do NOT update `_index.md` files.** Frontmatter is the source of truth (post session 61 sweep).

## CONTEXT FROM PRIOR SESSION — Telemetry

| Field | Value |
|---|---|
| model | claude-opus-4-7[1m] |
| tokens_consumed | unknown (Nick can add from `/status`) |
| context_window_size | 1000000 |
| context_window_pct_peak | unknown |
| turns | ~35 |
| tool_calls | ~80 (including 36 parallel frontmatter edits) |
| subagents | 0 (inline classification — deviation from `/identify-artifacts` subagent-batch contract, flagged in report) |
| capture_quality | estimated |
| harness | claude-code-cli-cursor-macos |
