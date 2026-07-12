# Audit — SKILL.md (Rule-10 assess pass)

Classification: **safety-critical** (trigger: `allowed-tools` includes Write, Edit, Bash; procedure performs cross-file writes and git commits).

**Artifact:** `/Users/nickgogan/MetaSystem/.claude/skills/session-handoff/SKILL.md` (rewritten 2026-07-12, session 138, restructure-program Phase 0 item 3; adaptation record `ADAPTATION.md` beside it)
**Requested by:** session-138 main thread — Rule-10 fresh-context audit after rewrite
**Composed guides:** G1 `writing-agent-specifications` (spec quality) · G3b `agent-workflow-and-execution` (state/termination) · G5 `designing-agent-tools` (tool surface) · G6 `agent-safety-and-permissions` (permissions) · G8 `model-resilient-prompt-engineering` (trigger/prompt craft) · **G9 `agent-governance-and-trust` — G9.I6 forced by safety-critical classification**
**Rubric size:** 14 file-verifiable invariants, 2 system-verifiable follow-ups, remaining composed-guide invariants latent (listed below)

DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

## Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | **Destructive/irreversible actions human-gated** | Destructive or irreversible actions always require human approval regardless of trust level | **G9.I6** (forced) | **Satisfied** | HITL gate sits at the irreversibility boundary: "Local commits at checkpoints are full autonomy; **push is Nick-gated**" (SKILL.md:113). All lower-layer writes (PROGRESS/HISTORY rewrites, local commits) are git-reversible with an append-only trail. The removed draft-approval loop (SKILL.md:117) is a documented trust *promotion* per Nick's standing ruling (ADAPTATION.md item 4), consistent with G9.I4 (track-record-based promotion) | — | 1 | High |
| 2 | Required-section completeness | Skill missing any of When-to-use / Procedure / Output-shape / Boundary-conditions fires G1.I1 | G1.I1 via skill.md §Template skeleton | Satisfied | §When to Use (:27), §Procedure at Session Close (:115), output shape carried by the PROGRESS/HISTORY target-shape specs (:46, :89) + report line (:136), boundary conditions across §Constraints/§Edge Cases/§System Log Boundary (:150–169) | — | 1 | High |
| 3 | Safety-critical self-declaration | Boundary conditions name "Safety-critical? Yes/No + HITL gate" (Construction step 4) | skill.md §Template skeleton / G9 | **Missing** | Body names the Nick-gated push but never explicitly self-classifies as safety-critical or labels the push gate as *the* HITL gate in a boundary section | Add one line to §Constraints or §Edge Cases: "Safety-critical: yes — HITL gate is the Nick-gated push." | 1 | Medium |
| 4 | Hard constraints enforced outside prompt layer | G1.I3 (umbrella) ⊃ G6.I2 (specialization: safety-critical constraints enforced structurally) — both fired, overlap annotated | G1.I3, G6.I2 | Satisfied | Line budget (soft 150 / hard 250) enforced by live repo pre-commit hook — verified present: `.git/hooks/pre-commit` → `operations/kb-maintenance-scripts/hooks/pre-commit`, caps implemented at lines 29–37 | — | 1 | High |
| 5 | Permissions tiered by risk | Permissions are tiered by risk, not binary allow/deny | G6.I1 | Satisfied | Autonomy gradient: reversible local operations full autonomy; irreversible push human-gated (:113) | — | 1 | High |
| 6 | No self-loosening of enforcement | The agent cannot modify its own permission configuration | G6.I3 | Satisfied | "The remedy for a failing check is route-then-compact — **never** raising the cap" (:87–88) | — | 1 | High |
| 7 | State independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b.I2 | Satisfied | The three-artifact spine (PROGRESS.md / HISTORY.md / git) *is* the durable state; cold-start contract is explicit (:17–19) | — | 1 | High |
| 8 | Termination conditions | Every iterative pattern has a termination condition (loop limit, stall detection, or both) | G3b.I3 | **Partial** | Success (commit + 1–3 sentence report, :133–136), skip ("nothing meaningful changed", :165), and abort ("user says stop → last consistent state", :168) all defined. But the over-budget remediation loop ("Over budget → route-then-compact again", :131) has no bounded escape — no rule for the pathological case where compaction cannot get under the 250 hard cap | G3b §Recovery ("add loop termination rules"); add an escape hatch: after N compaction passes still over cap → surface to Nick as a question | 1 | Medium |
| 9 | Trigger description quality | Description phrased as consumer phrasing, not feature label | G8 via skill.md §Decision sequence 2 | Satisfied | Frontmatter enumerates literal trigger phrases ("handoff", "close the session", "wrap up", "reconcile progress") + a negative trigger ("Do not use when nothing meaningful changed", :32) | — | 1 | High |
| 10 | Behavioral rules as negative constraints | High-priority behavioral rules expressed as negative constraints, not positive aspirations | G8.I3 | Satisfied | §Constraints (:150–160) is five negative invariants (no hardcoded counts, no fake precision, no session log, no contradictions, no context dumping) | — | 1 | High |
| 11 | Minimal tool surface | Only tools needed for the current task are loaded; tool over-granting is an authoring anti-pattern | G5.I4, skill.md §Anti-patterns | **Partial** | `allowed-tools: Read Grep Glob Write Edit Bash` — no procedure step uses Grep or Glob (procedure names git status/diff via Bash, Read/Write/Edit of PROGRESS/HISTORY). Mitigation: this exact bundle is the house default across 6 workspace skills; space-separated format matches workspace convention | Trim to `Read Write Edit Bash` unless a reconcile step is expected to search (e.g., Grep to locate routed content) — if so, name that step | 1 | Medium |
| 12 | Stop rules (all three types) | Stop rules include at least one halt condition, one escalation trigger, one completion criterion | G1.I5 | Satisfied | Halt: user stop (:168); escalation: "surface anything genuinely ambiguous as a question rather than blocking" (:118–119); completion: commit + summary report (:133–136); plus DoD-not-met ⇒ don't ship (:166) | — | 1 | High |
| 13 | Declarative spec, no placeholders | Prompts tell the model what to produce, not how to think; no TBD/TODO fields | G8.I1, G1.I2 | Satisfied | Target shapes for PROGRESS.md and HISTORY.md fully specified as output contracts (:46–101); no placeholder fields anywhere | — | 1 | High |
| 14 | Framework-agnostic portability | Skills are framework-agnostic markdown, portable without modification | G5.I11 | Satisfied | Plain markdown, no SDK/framework coupling; §Provenance records the upstream re-derive path (:171–174); ADAPTATION.md confirms upstream `metadata`/`compatibility` apparatus was dropped in favor of native Claude Code capabilities | — | 1 | High |

## Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|---|---|---|---|
| a | Prompt changes are versioned and tested before deployment | G8.I7 | Has the rewritten skill been exercised end-to-end since the rewrite (a real or dry-run session close)? The session-138 close is the natural first run | A skill-produced reconciled PROGRESS.md + `docs(pm)` commit; note any procedure friction back into the SKILL.md |
| b | Completed specs/audits retained as audit records | G1 §Governance; ADAPTATION.md §Pending | ADAPTATION.md still lists this Rule-10 pass as pending — will its dispositions be recorded there per its own instruction? | ADAPTATION.md §Pending updated with this report's path and the disposition of findings #3, #8, #11 |

## Aspects out of scope (latent)

| Guide / invariant group | Why latent |
|---|---|
| G8 model-routing, Advisor-Executor, caching, metaprompt invariants | Skill selects no models, assembles no cached prompt layers, runs no optimization loops |
| G5 tool-*design* invariants (poka-yoke, descriptions-as-UX, registries, interceptors, deferred loading) | Skill consumes built-in tools; it designs/ships none |
| G9 invariants other than I6 (autonomy taxonomies, trust ledgers, policy bundles, delegation chains) | System-level governance machinery; only I6 is forced by the safety-critical classification. Audit-trail substance is nonetheless evidenced by the git spine |
| G3b cost controls, delivery-chunk calibration, degradation-mode engineering | Single-turn, negligible-cost workflow; degradation substance is covered by the Edge Cases section |
| G2a/G2b | Not in the skill composition set (no embedded context directives) |

## Summary

**G9.I6: Satisfied — the skill is deployment-ready from a governance standpoint.** The HITL gate is placed exactly at the irreversibility boundary (Nick-gated push); everything beneath it is git-reversible with an append-only trail, and the removal of the draft-approval loop is a documented, Nick-ruled trust promotion rather than a silent gate deletion. The hard line-budget constraint has live structural enforcement (pre-commit hook verified). Three non-blocking gaps: the skill never *self-declares* its safety-critical classification (one-line fix), the over-budget compaction loop lacks a bounded escape, and Grep/Glob are granted but unused. Closure of follow-up (a) lands naturally with the session-138 close; follow-up (b) is the ADAPTATION.md disposition record.

---

*Produced by `/assess-skill` (Librarian, fresh context), 2026-07-12. Report homed in `operations/artifact-audits/` per DD-110 (per-artifact contract conformance); the /assess-skill contract emits the audit.md §Output-shape report but names no file destination — this dated folder is the workspace convention. Not an `/audit-artifacts` run; `runs.md` not appended.*
