# Handoff: Session 67 — Codifier IB-152 (/assess-skill + /assess-agent ContextSpec audit extension)

## IDENTITY AND SOUL

You are the **Codifier** agent in the Improvement Loop. Disposition: precise, form-aware, completeness-driven. You treat the pipeline like a contract — what it promises is what it must deliver, every time. You propose-first on governance-adjacent work, execute within ratified governance on operational mechanics. You surface ambiguity rather than resolve it silently. You are concise; you flag deviations explicitly; you do not over-narrate.

Nick is the bridge between Claude Build and Household OS, and the architect of MetaSystem. He files Design Decisions; you execute rubric-driven mechanics within them. **He gates content, you run procedure.**

**Project context.** Session 66 PASSED the IB-150 acceptance test (5/5 criteria) — `/extract-artifacts` now generates DD-92-conformant ContextSpec by default and the Step 2.5 guards work as designed. The 4 newly-staged artifacts (2 rules, 1 skill, 1 template) are the first DD-92-native artifact set. Your job in session 67 is **IB-152**: extend the **consumer-side** audit tooling (`/assess-skill` and `/assess-agent`) so that ContextSpec conformance is checkable downstream — closing the loop on DD-92 enforcement.

## YOUR PRIMARY TASK — IB-152

**Goal.** Extend `/assess-skill` and `/assess-agent` so that they validate DD-92 ContextSpec conformance on the artifacts they audit. Audit tooling must catch what extractor tooling now produces.

**The two skills to extend:**
- `.claude/skills/assess-skill/SKILL.md` — audits a consumer-submitted SKILL.md against Contract-derived criteria from IL guides G1, G3b, G5, G6, G8 (+G9.I6 for safety-critical skills).
- `.claude/skills/assess-agent/SKILL.md` — audits a consumer-submitted agent artifact (agent.md, CLAUDE.md, system prompt) against Contract-derived criteria from the relevant IL guides.

**What to add (per skill):**

1. **ContextSpec presence check.** Detect whether the audited artifact (or any artifacts it directly references in `extracts/{rules,skills,templates}/`) carries a `context:` block with all 8 required fields (`applies_to`, `platform_coupling`, `autonomy`, `stage`, `reversibility`, `auditability`, `evidence_strength`, `adoption.status`; `adoption.notes` optional). Missing field → emit a finding.

2. **Universal-vocabulary scan.** Scan ContextSpec field values for forbidden tokens (same scan as `/extract-artifacts` Step 2.5):
   - MetaSystem scope labels: `S2`, `S3`, `General`, `Perplexity Skills`
   - IL-internal skill names: `/identify-artifacts`, `/extract-artifacts`, `/assess-skill`, `/assess-agent`, `/research-loop`, `/promote-findings`, `/synthesize-guide`, `/reassess-priorities`
   - IL-specific paths: `systems/improvement-loop/`, `extracts/`, `research-findings/`, `research-sources/`, `research-authorities/`
   - Hit → emit a finding with the specific token and field location.

3. **IL-meta leak check.** Detect presence of `confidence`, `tier`, `reason_codes`, or `co_occurrence` in artifact frontmatter. These are IL-internal classification metadata and MUST be stripped at deploy boundary per DD-92. Hit → emit a finding (the artifact has crossed the deploy boundary with classification meta intact).

4. **Composition with existing rubric.** ContextSpec checks compose with the existing Contract-derived criteria — they do NOT replace them. Existing audit logic stays; the new checks are an additional dimension.

**Acceptance (verify before close):**

| Test | Expected behavior |
|---|---|
| Dry-run on `extracts/rules/confirm-failure-first-tdd.md` (DD-92-native) | Audit passes ContextSpec checks cleanly; existing Contract-derived criteria still report as before |
| Dry-run on a synthetic non-conformant artifact (e.g., `applies_to` containing `"S3"`) | Specific universal-vocabulary finding emitted naming the violating field and token |
| Dry-run on a synthetic artifact missing `adoption.status` | Specific presence-check finding emitted naming the missing field |
| Dry-run on a synthetic artifact with `confidence: HIGH` in frontmatter | IL-meta leak finding emitted |
| Dry-run on the 4 session-66 staged artifacts | All 4 pass ContextSpec checks (regression sanity — they were drafted under the IB-150 contract) |

You do NOT need to deploy these audited skills anywhere — `/assess-skill` and `/assess-agent` are themselves IL-scoped and stay in `.claude/skills/`.

## YOUR SECONDARY TASKS — Optional, Context-Dependent

If IB-152 closes cleanly with budget remaining, advance the queue:

- **Vocabulary ratification (ACCEPTED vs APPROVED).** Nick used `ACCEPTED` in the session-66 report review where `/identify-artifacts` Status enum reads `APPROVED`. If he wants ACCEPTED as the contract term, file a small skill-contract amendment (one-character change × 2 skills: `/identify-artifacts` Step 4 Status field and `/extract-artifacts` Step 1 filter table). **Propose-first** — draft the deltas, surface to Nick, do not edit without his ruling.

- **Guide re-synthesis (G4 / G10).** Both unblocked since session 63. G3 specifically should fold in the entry-15 reflection from session 66 ("harnesses lie on a spectrum from entirely LLM-initiated & driven via just prompts to mostly deterministic where workflows are instantiated and wired together with code") when re-synthesized.

If IB-152 surfaces blocking ambiguity (e.g., the existing `/assess-*` skills have a structural assumption that conflicts with the ContextSpec dimension), **stop and propose**. Do not freelance the design.

## RULES

- **Propose-first on contract amendments.** If the IB-152 extension requires non-trivial restructuring of `/assess-skill` or `/assess-agent` (more than additive checks), draft the proposed deltas as literal OLD/NEW diffs and surface to Nick before applying.
- **DD-92 is binding.** ContextSpec presence + universal-vocab + IL-meta-stripped are non-negotiable invariants. The audit must check what the contract requires.
- **Read-only audits.** `/assess-skill` and `/assess-agent` are read-only — they emit findings, they do not modify the audited artifact or the KB. Preserve this.
- **Composition over replacement.** New checks add to the existing audit dimensions; they do not replace Contract-derived criteria.
- **Findings format consistency.** Match the finding format already used by `/assess-skill` / `/assess-agent` so consumers don't see two parallel report styles.

## KEY REFERENCES

| Entity | Path |
|---|---|
| `/assess-skill` skill | `.claude/skills/assess-skill/SKILL.md` |
| `/assess-agent` skill | `.claude/skills/assess-agent/SKILL.md` |
| `/extract-artifacts` Step 2.5 (canonical scan logic) | `.claude/skills/extract-artifacts/SKILL.md` lines ~207–222 |
| Reference DD-92-native artifact | `extracts/rules/confirm-failure-first-tdd.md` |
| Session-66 staged artifacts (regression set) | `extracts/rules/claudemd-minimum-viable-rule-only-add-globally-true-lines.md`, `extracts/rules/explicit-permission-allow-listing-for-agent-resource-access.md`, `extracts/skills/iterative-refinement-loop-with-quality-gate.md`, `extracts/templates/task-to-file-routing-table-in-context-files.md` |
| DD-92 (ContextSpec contract) | `project-management/design-decisions/DD-92.md` |
| DD-78 (ContractSpec companion) | `project-management/design-decisions/DD-78.md` |
| IB-152 (queued; this session's target) | `project-management/implementation-backlog/IB-152.md` |
| IB-150 (closed; acceptance criterion validated session 66) | `project-management/implementation-backlog/IB-150.md` |
| Session 66 SL (full IB-150 acceptance log) | `operations/system-log/session-66-codifier-ib-150-acceptance-test.md` |
| Session 65 SL (precedent for skill-contract edit + propose-first) | `operations/system-log/session-65-codifier-ib-150-extract-artifacts-dd92-update.md` |
| IL active queue + status markers | `PROGRESS.md` (at IL root) |
| IL CLAUDE.md (pipeline + agent definitions) | `CLAUDE.md` (at IL root) |
| Codifier agent definition | `agents/codifier/agent.md` |

## CONTEXT FROM PRIOR SESSION

### Resolved (session 66)

- **IB-150 acceptance test PASSED (5/5).** Pipeline ran end-to-end on 17 fresh P1 findings: 13 patterns routed to guide synthesis (DD-81), 4 non-pattern artifacts written. Step 2.5 firing log: 4 validated, 0 flagged, 0 re-drafts. The new prompt language (DO-NOT-COPY warnings, reference-impl pointer, source-applicability passed with explicit warning) prevented mechanical-copy and forbidden-vocab failure modes upstream of the guards. No bugs, no contract amendments.
- **4 staged artifacts written** to `extracts/{rules,skills,templates}/`. Awaiting Nick's deployment review.
- **Bookkeeping fix.** 10 stale-status findings (raw despite existing extracts) back-annotated to extracted with `consumed_by` populated. Single 2026-04-19 batch failure of `/extract-artifacts` Step 5; not recurring, no hardening proposed.
- **Vocabulary delta surfaced.** Nick wrote `ACCEPTED` (10×) where the contract reads `APPROVED`. Normalized inline to unblock the test.
- **Session 66 commit.** `a83dac0`.

### Unresolved (carry into session 67)

1. **IB-152** — your primary task this session.
2. **4 session-66 staged artifacts await Nick's deployment review.** Standard staged-artifact lifecycle (DD-39 / DD-80). Not for Codifier this session unless Nick redirects.
3. **Vocabulary ratification (ACCEPTED vs APPROVED).** Nick-gate. If he prefers ACCEPTED, file the small contract amendment.
4. **Entry-15 reflection (harness spectrum).** Carried as input to G3 re-synthesis. Not for this session unless G3 work is undertaken.
5. **Lifecycle-spec Phase-1 DDs (DD-X1, DD-X3, DD-X4)** — Nick-gated; blocks G7/G2/G9 re-synthesis. Not for Codifier this session.

### Pre-session queue state (snapshot, 2026-04-26 close)

| pipeline_status | Count |
|---|---|
| raw | 291 |
| classified | 53 + 13 (mixed quote style) |
| extracted | 36 |
| synthesized | 165 |

The 4 session-66 staged artifacts are the first DD-92-native set in `extracts/`. Use them as a regression sanity for IB-152 audit checks.

## OUTPUT REQUIREMENTS

1. **Updated `/assess-skill` skill** with ContextSpec audit dimension added (additive, composes with existing checks).
2. **Updated `/assess-agent` skill** with ContextSpec audit dimension added (additive, composes with existing checks).
3. **Acceptance dry-runs** documented in your end-of-session report — at minimum the 5 acceptance tests in the table above.
4. **SL entry at session end** at `operations/system-log/session-67-codifier-ib-152-assess-contextspec-extension.md`. Logs the deltas applied, dry-run outcomes, any deviations.
5. **PROGRESS.md retargeted at session end.** If IB-152 closes: strike from queue, retarget Next session at the next-priority queue item (likely vocabulary ratification if Nick rules, or guide re-synthesis). If IB-152 surfaces blocking ambiguity: keep at top with status note.
6. **IB-152 close** — update `project-management/implementation-backlog/IB-152.md` `status: Done` + close-out note (matching IB-150's closure style).
7. **Do NOT update `_index.md` files.** Frontmatter is the source of truth.
8. **Do NOT add session-history block to PROGRESS.md.** SL carries session tracking.

## TELEMETRY (prior session)

| Field | Value |
|---|---|
| model | claude-opus-4-7[1m] |
| tokens_consumed | unknown (Nick can add from `/status`) |
| context_window_size | 1000000 |
| context_window_pct_peak | unknown |
| turns | ~22 |
| tool_calls | ~35 |
| subagents | 4 (3 parallel Sonnet for /identify-artifacts batches of 6/6/5; 1 Sonnet for /extract-artifacts drafting batch of 4) |
| capture_quality | estimated |
| harness | claude-code-cli-cursor-macos |
