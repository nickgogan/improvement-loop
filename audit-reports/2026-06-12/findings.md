---
title: "IL audit per-artifact findings"
audit_target: "systems/improvement-loop/"
audit_date: "2026-06-12"
audit_session: "115"
audit_version: "v1"
---

# Per-artifact findings — IL audit (session 115)

Reports below are produced by IL `/assess-skill` and `/assess-agent` via Librarian subagents in parallel-dispatched fresh contexts. All subagents ran in `mode: in-context-rubric` (Skill tool unavailable to the workspace Librarian configuration; rubric applied directly via SKILL.md reads — same operational pattern as session 114).

## Coverage

- **24 artifacts** with full verbatim assessor reports (persisted bins 1, 5, 6, 7, 8).
- **12 artifacts** with structured digests (visible-stream bins 3, 9, plus singles captured from partial bins 2 and 4). Verbatim reports preserved in session 115 conversation transcript.
- **7 artifacts** with `report-missing` flag — bins 2 and 4 each emitted only 1 of N expected sentinel blocks. This is a v1-skill format-compliance regression (see summary §"Design contract refinement candidates from this run").

---

## Skills

### Skill: `systems/improvement-loop/.claude/skills/ask-kb/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 6, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

**mode: in-context-rubric**
**Artifact:** `systems/improvement-loop/.claude/skills/ask-kb/SKILL.md`
**Classification: non-safety-critical.** `allowed-tools: Read Grep Glob` — all read-only. No Write, Edit, Bash, or MCP mutating tools. Skill explicitly declares "Safety-critical? No." in its Boundary Conditions section.

**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger description)
**Rubric size:** 14 file-verifiable invariants, 4 system/process-verifiable invariants, 1 latent

**G3b Precondition check:** G3b requires "side effects or runs longer than a single interactive turn." This skill has no side effects (read-only) and is designed for a single conversational turn. G3b.I2 (state tracking), G3b.I5 (delivery chunk size), G3b.I6 (cost controls) are partially latent — however G3b.I3 (termination) and G3b.I4 (degradation) remain applicable as the skill has explicit procedure steps. G3b fires partially.

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Spec completeness — stop rules | G1.I5: stop rules include halt condition, escalation trigger, completion criterion | G1 §Invariants | Partial | "Termination — success" and "Termination — abort" are explicitly defined in Boundary Conditions. However, no escalation trigger is named (i.e., when should the skill escalate vs. redirect). The two stop-rule types present (completion criterion, abort) are solid; escalation is absent. | G1 §Recovery | 1 | Medium |
| 2 | Acceptance criteria — third-party evaluable | G1.I4: acceptance criteria evaluable by third party | G1 §Invariants | Satisfied | "Termination — success: a citation-grounded answer in the mode-appropriate structure has been produced, including caveats/gaps" is concrete and third-party evaluable — the output shape templates provide the checkable structure. | — | 1 | High |
| 3 | Hard constraints enforcement | G1.I3: hard constraints have enforcement outside prompt layer | G1 §Invariants | Partial | The "Read-only" constraint (Rule 5) is structurally enforced by the allowed-tools list (Read, Grep, Glob — no Write/Edit). This is a genuine structural enforcement. The "KB-first, never training-data substitution" constraint (Rule 1) is prompt-only — there is no structural mechanism to prevent training-data padding. | G1 §Recovery | 1 | Medium |
| 4 | Autonomy levels | G1.I1: spec includes autonomy levels per decision type | G1 §Invariants | Missing | No autonomy table or autonomy classification per decision type. The skill describes Teacher and Builder modes but does not classify decisions by blast radius or autonomy tier. For a read-only skill this is lower severity, but the field is required by the spec template. | G1 §Recovery | 1 | Medium |
| 5 | Context supply plan | G1.I1: context supply plan (when context gap exists) | G1 §Invariants | Partial | Steps 1-2 of the procedure define a read set and scope it to the query. This functions as a context supply plan but is embedded in procedure prose rather than a declared context-supply section. | G1 §Recovery | 1 | Low — the procedure text effectively serves the purpose; the absence is structural, not substantive |
| 6 | Termination condition for iterative patterns | G3b.I3: every iterative pattern has termination condition | G3b §Invariants | Satisfied | The skill is single-pass (no loops). The Teacher/Builder mode selection and read-set scoping are deterministic decision branches, not iterative loops. Termination is defined in Boundary Conditions. | — | 1 | High |
| 7 | Degradation modes | G3b.I4: degradation modes defined before go-live | G3b §Invariants | Partial | Step 4 defines KB-gap handling ("state explicitly 'The KB has no findings…'") and contradiction handling ("present both"). Broken reference handling is defined ("flag the broken reference"). However, no degradation for empty Glob/Grep results (technical failure vs. KB gap) is distinguished. | G3b §Recovery | 1 | Low |
| 8 | Tool loading discipline | G5.I4: only tools needed loaded | G5 §Invariants | Satisfied | allowed-tools is minimal: Read, Grep, Glob. No extraneous tools. `--scope` parameter narrows which directories are read. | — | 1 | High |
| 9 | Tool descriptions | G5.I3: descriptions persuade, disambiguate, explain when not to use | G5 §Invariants | Satisfied | No tool table is included, but the allowed-tools are Read/Grep/Glob — standard tools with well-understood behavior. The "What This Skill Does NOT Do" section and "Out of scope" in Boundary Conditions substitute for per-tool guidance by pointing to the correct skills for adjacent queries. | — | 1 | High |
| 10 | Permissions tiered | G6.I1: permissions tiered by risk | G6 §Invariants | Satisfied | Read-only tool set is the minimum required. The skill's own Boundary Conditions declares "Safety-critical? No." and explains why (no Write/Edit/Bash; no external mutation). This constitutes an explicit risk classification. | — | 1 | High |
| 11 | Safety-critical structural enforcement | G6.I2: safety-critical constraints enforced structurally | G6 §Invariants | Satisfied | The "read-only" constraint is structurally enforced by the allowed-tools list. No Write or Edit present. | — | 1 | High |
| 12 | Trigger description quality | G8 trigger description | G8 §Invariants | Satisfied | Description uses consumer phrasings verbatim: "what do we know about X", "help me design Z, what should I consider", "what patterns apply to W". argument-hint is explicit. When to Use section is comprehensive. Negative trigger list in "What This Skill Does NOT Do" adds effective disambiguation. | — | 1 | High |
| 13 | ROLE/AUTHORITY/CONSTRAINT/FAILURE SIGNAL | G8.I6 | G8 §Invariants | Partial | ROLE is declared ("Librarian — mode follows query"). CONSTRAINT is distributed across Rules section. AUTHORITY is implicit (KB-grounded only). FAILURE SIGNAL is missing — no explicit statement of what constitutes a failure signal the model should surface to the caller. | G8 §Recovery | 1 | Medium |
| 14 | DD-92 ContextSpec | DD-92 | DD-92 | Skipped | DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here. | — | — | — |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | G8.I7: prompt changes versioned and tested | G8 §Invariants | Are changes to the mode-classification rules (Step 0 pattern matching) version-controlled and tested? | Commit history or test cases covering Teacher vs. Builder classification |
| b | G3b.I2: workflow state independent of conversation history | G3b §Invariants | If the skill is invoked mid-session where the conversation already contains KB content, does the step 1-2 read set still execute from scratch? Or does it rely on already-read context? | Runtime behavior attestation |
| c | G1.I1: health metrics defined | G1 §Invariants | The spec does not define health metrics (e.g., citation density, gap-flag rate). Are these tracked anywhere? | Health metrics definition or monitoring setup |
| d | G5.I7: skill versioned and locked | G5 §Invariants | Is the `ask-kb` skill versioned? Is there a lock file? | Lock file or version manifest |

---

### Aspects out of scope

| Guide | Why latent |
|-------|-----------|
| G3b.I2 (state tracking independent of conversation) | Latent — skill has no side effects and runs in a single pass. State tracking is not applicable. |
| G3b.I5 (delivery chunk calibrated to reviewer capacity) | Latent — output is conversational, not chunked delivery. Not applicable. |
| G3b.I6 (cost controls before autonomous execution) | Latent — skill is interactive (user-gated per invocation), not autonomous. Cost controls not a structural requirement here. |
| G9 (governance/HITL) | Latent — skill correctly classified non-safety-critical. G9 does not fire. |

---

### Summary

No G9.I6 issue — skill is non-safety-critical and correctly self-classified. The strongest elements are the tool-surface discipline (minimal allowed-tools, structurally enforced read-only), the trigger description quality (consumer-phrasing, disambiguation, negative-trigger list), and the output shape templates. The load-bearing gaps are: missing autonomy table (G1 — lower severity for read-only skill but still required by spec template), absent escalation trigger in stop rules (G1.I5 — partial), and missing FAILURE SIGNAL property (G8.I6 — partial). These are all Partial or Missing findings at medium confidence — not blocking for deployment, but should be addressed for full spec conformance.

---

### Skill: `systems/improvement-loop/.claude/skills/assess-agent/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 8, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

mode: in-context-rubric (assess-skill SKILL.md loaded; rubric applied directly per procedure)

**Artifact:** `systems/improvement-loop/.claude/skills/assess-agent/SKILL.md`
**Classification:** safety-critical (trigger: `allowed-tools` includes Write — the skill writes boundary-case encounter logs to `operations/system-log/`)
**Composed guides:** G1 (spec quality), G3b (workflow/termination), G5 (tool use), G6 (safety/permissions), G8 (prompt/trigger quality), G9 (governance — G9.I6 forced for safety-critical)
**Rubric size:** 13 file-verifiable invariants, 5 system/process-verifiable invariants, 1 latent (out-of-scope)

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | G9.I6 — HITL gate for destructive actions | Destructive or irreversible actions always require human approval regardless of trust level. | G9 §Invariants | Satisfied | The only Write operation is boundary-case encounter logging to `operations/system-log/`, narrowly scoped by the "Boundary-Case Encounter Logging" section: "Write scope is narrowed to `operations/system-log/` only — do not write elsewhere." The primary output (audit report) is produced as a conversation message, not a file write. The log write is append-only to a specific directory — a low-blast-radius, auditable, non-reversibility-critical action. The classification of this skill as safety-critical is technically correct (Write is in allowed-tools) but the Write is scope-constrained, append-only, and non-destructive in practice. G9.I6 is satisfied because the Write is bounded and auditable. | — | 1 | High |
| 2 | G1 — Spec completeness: objective, constraints, autonomy, stop rules | Spec includes objective, desired outcomes, constraints classified by enforcement layer, autonomy levels, stop rules | G1 §Invariants | Satisfied | Objective: "Audit a consumer-submitted agent artifact… against Contract-derived criteria." Constraints: "Read-only; never modifies the artifact or the KB." Autonomy: implicit (read-only disposition). Scope boundaries: strong ("Does not rewrite the artifact," "Does not propose a redesign," "Does not write to the KB"). The "Boundaries" section handles the reject-path. | — | 1 | High |
| 3 | G1 — Stop rules: halt condition | Stop rules include at least one halt condition | G1 §Invariants | Satisfied | "Boundaries" section: "If the submitted artifact is not an agent artifact, state that and redirect." Artifact > ~500 lines: "ask for scoping clarification before proceeding." These are explicit halt conditions. | — | 1 | High |
| 4 | G1 — Stop rules: escalation trigger | Stop rules include at least one escalation trigger | G1 §Invariants | Satisfied | "If the consumer asks for a redesign, stop and hand off to a `design` operation (planned)." Boundary escalation is explicit. | — | 1 | High |
| 5 | G1 — Acceptance criteria evaluable by third party | Acceptance criteria are evaluable by a third party without access to the prompter's intent | G1 §Invariants | Missing | No explicit acceptance criteria section. The "Output Shape" defers to `audit.md §"Output shape"` which defines the table structure, but success of this skill's invocation is not defined as a pass/fail condition. | Add: "Success: audit report produced per audit.md output shape with N file-verifiable findings, M system-verifiable follow-ups, and K latent aspects declared; tier trace attached to each finding." | 1 | Medium |
| 6 | G3b — Termination conditions | Every iterative pattern has a termination condition | G3b §Invariants | Satisfied | Steps 0–5 are sequential with explicit phase boundaries. The rubric-building (Phase 2) and rubric-application (Phase 3) iterate over invariants from a finite composed guide set. Termination is implicit on set exhaustion. | — | 1 | High |
| 7 | G3b — Explicit state tracking independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b §Invariants | Partial | The audit report is produced as a conversation message ("See `audit.md` §'Output shape'"). No persistent file write of the audit report is specified. If the session ends before the user copies the report, the audit output is lost. The boundary-case log is persisted (Write), but the primary output is not. | Consider specifying an optional `--save` flag or a default output path for audit reports. | 1 | Medium |
| 8 | G5 — Minimal tool surface | Only tools needed for the current task are loaded | G5 §Invariants | Satisfied | `allowed-tools: Read Grep Glob Write` — minimal and justified. Read for artifact and guide loading; Grep for section targeting; Glob for directory scanning; Write narrowly for SL logging. | — | 1 | High |
| 9 | G5 — Intermediate results management | Intermediate tool results stay outside context window when agent only needs final output | G5 §Invariants | Partial | The procedure reads `audit.md`, `agent.md`, and all Contract subsections of the composed guide set (up to 10 guides for Variant B). For a harness-based agent audit, this is a large context load. The procedure does not specify reading only the Contract subsection (even though Step 1.3 says "Use heading-match ... then read the line range"). Without explicit line-range reads, full guide bodies may be loaded. | Step 1.3 ("read the line range") is the right instinct; enforce this by specifying that only the `## Contract` section (from its heading to the next `##`) should be read, not the full guide file. | 1 | Medium |
| 10 | G6 — Permissions tiered by risk | Permissions tiered by risk, not binary allow/deny | G6 §Invariants | Satisfied | Read/Grep/Glob are read-only; Write is narrowly scoped to `operations/system-log/`. Effective tier separation. | — | 1 | High |
| 11 | G6 — Safety-critical constraints enforced structurally | Safety-critical constraints enforced structurally, not via prompt instructions alone | G6 §Invariants | Partial | "Write scope is narrowed to `operations/system-log/` only — do not write elsewhere" is a prose constraint, not a structural one. No harness-level path restriction enforces this. | System-verifiable: confirm harness enforces path restriction for Write operations from this skill. | 1 | Medium |
| 12 | G8 — Trigger description quality | Description phrases the trigger the way a consumer would ask | G8 §Invariants | Satisfied | "Audit a consumer-submitted agent artifact (agent.md, CLAUDE.md, system prompt for an agent) against Contract-derived criteria from the relevant IL guides." Consumer-phrasing-aligned. "When to Use" states concrete trigger conditions. "What This Skill Does NOT Do" provides negative-space disambiguation. | — | 1 | High |
| 13 | G8 — ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | G8 §Invariants | Partial | ROLE: "The Librarian's Audit disposition — read-only, citation-grounded, gap-honest." — present. Constraints: present ("Read-only; never modifies"). AUTHORITY: implied (Librarian) but not explicitly declared as a property. FAILURE SIGNAL: partially present ("If the submitted artifact is not an agent artifact, state that and redirect") but no explicit failure signal for what happens when the audit cannot be completed (e.g., guide file unavailable). | Add explicit FAILURE SIGNAL: "If a required guide Contract section cannot be read, report which guide is missing and produce a partial audit covering only the available guides; do not silently skip." | 1 | Medium |
| 14 | DD-92 ContextSpec | `context:` block absent | DD-92 | N/A (skipped) | No `context:` block in frontmatter. DD-92 ContextSpec audit skipped — DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here. | — | — | — |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|------------------|
| a | Write path restriction structurally enforced | G6 §Invariants | Is the `operations/system-log/` path restriction for Write enforced at the harness level, or only by prose instruction in the skill? | Evidence: harness settings.json path restriction for Write tool in assess-agent invocation context |
| b | Context budget for large guide sets | G5 §Invariants | For Variant B (harness-based), the composed guide set is {G1, G2a, G2b, G3, G3b, G5, G6, G9, G10} — 9 guides. Has the skill been tested to confirm it reads only Contract sections (not full guide bodies) and stays within context budget? | Evidence: test audit session showing line-range reads, not full-guide reads |
| c | Audit report persistence | G3b §Invariants | When audit reports are produced as conversation messages only, how are they retained for later reference (e.g., as evidence that a skill was audited before deployment)? | Evidence: documented session practice for saving audit outputs; or addition of `--save` flag |
| d | agent.md concept file availability | (Skill-internal) | If `operations/references/librarian/agent.md` is unavailable, the skill says to "fall back to runtime aggregation against the guide routing table." Has this fallback been tested? | Evidence: fallback test or confirmation that agent.md exists and is maintained |
| e | Variant selection reliability | (Skill-internal) | When no `--variant` flag is provided and the variant cannot be inferred from the artifact, the skill says to "ask one disambiguating question." Is this behavior tested across ambiguous agent artifacts? | Evidence: test session with an ambiguous agent artifact |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G9 (beyond I6) | This skill is read-only (modulo the narrowly scoped SL Write). G9 broader invariants apply to agentic systems with trust ladders and multi-decision-type configurations. G9.I6 fires for the Write; remaining G9 invariants are latent. |

---

### Summary

G9.I6: **Satisfied.** The Write operation is narrowly scoped to `operations/system-log/` (append-only encounter logging), which is low-blast-radius and auditable. The primary audit output is read-only. No HITL gate is required for the log write given its scope.

This is a structurally sound skill with strong procedure design. The compositions table reference and guide-set selection per variant are clear.

Load-bearing findings:
- Finding #5: Missing explicit acceptance criteria — a third party cannot verify audit success without them.
- Finding #9: Context budget risk — if guide files are read in full rather than by section, a 9-guide Variant B audit may exceed context limits.
- Finding #7: Primary audit output is ephemeral (conversation-only) — no persistent state without `--save` option.

Finding #13 (FAILURE SIGNAL missing for guide-read failure) is an important robustness gap: the skill should declare what to do when a required guide is unavailable rather than leaving the behavior undefined.

No DD-92 ContextSpec findings — `context:` block absent; check not applicable.

---

### Skill: `systems/improvement-loop/.claude/skills/assess-prompt/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 7, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

**mode: in-context-rubric** (assess-skill SKILL.md loaded; rubric applied directly)

**Classification: safety-critical (trigger: allowed-tools includes Write and Skill)**

Note: `Skill` tool can invoke arbitrary skills including those with Write/Edit access, which mutates external state. `Write` is also listed directly. Safety-critical classification applies on both triggers.

**Artifact:** `systems/improvement-loop/.claude/skills/assess-prompt/SKILL.md`
**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — safety-critical; G9.I6 forced)
**Rubric size:** 17 file-verifiable invariants, 4 system/process-verifiable invariants, 0 latent

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Spec completeness | Every spec includes objective, desired outcomes, health metrics, constraints, autonomy levels, acceptance criteria, stop rules, context supply plan | G1.I1 | Partial | Objective (IL-KB extension over `/prompt-evaluator`) and "What This Skill Does NOT Do" constraints are clear. No health metrics, no explicit acceptance criteria, no stop rules (halt/escalation/completion). "Boundaries" section partially covers scope constraints but not failure termination | G1 §Recovery | 1 | High |
| 2 | Hard constraints have enforcement outside prompt layer | Hard constraints must have enforcement mechanisms outside prompt layer | G1.I2 | Partial | "Does not duplicate `/prompt-evaluator`'s 4-discipline rubric" and precondition gating are stated as hard constraints. The precondition gate (Step 3 extension path checks Preconditions) provides structural enforcement for the guide-firing rules. However "Read-only" constraint has no structural enforcement — `Write` in `allowed-tools` means the model could write if instructed | G1 §Recovery | 1 | High |
| 3 | Acceptance criteria evaluable by third party | Acceptance criteria are evaluable by a third party | G1.I3 | Missing | No acceptance criteria section. The early-exit path and integrated-output shape are defined, but no pass/fail criteria for audit quality (e.g., "every IL finding must cite a guide section and evidence quote") are explicitly stated as acceptance criteria | G1 §Recovery | 1 | High |
| 4 | Stop rules: halt + escalation + completion | Stop rules include at least one halt, escalation trigger, completion criterion | G1.I4 | Partial | Completion: early-exit path (Step 3) and full-output (Step 4) both terminate cleanly. Halt: none defined for failures (e.g., prompt-evaluator invocation fails, guide file unreadable). Escalation: none. | G1 §Recovery | 1 | Medium |
| 5 | Explicit state tracking independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b.I1 | Satisfied | The skill is primarily a single-turn audit operation. Step 1 obtains the baseline (either reads a prior file or invokes the skill), Steps 2-3 load and apply the rubric, Step 4 assembles the integrated report. The report itself is the stateful artifact. For a read-dominated skill this is adequate | G3b §Recovery | 1 | High |
| 6 | Iterative pattern has termination condition | Every iterative pattern has a termination condition | G3b.I2 | Satisfied | The iteration over "firing triggers" (Step 3) is bounded to at most 4 triggers (context, tool-directives, spec-document, harness-specific). Explicit early-exit path for zero-trigger case. No unbounded loops | G3b §Recovery | 1 | High |
| 7 | Degradation modes defined | Degradation modes defined before going live | G3b.I3 | Partial | One degradation is defined: consumer declines `/prompt-evaluator` baseline → proceed without it, note the coverage gap. No degradation defined for: `/prompt-evaluator` skill invocation failure, guide file unreadable, prompt text too large for context | G3b §Recovery | 1 | Medium |
| 8 | Only tools needed loaded | Only tools needed for the current task are loaded | G5.I1 | Violated | `allowed-tools: Read Grep Glob Skill Write` — `Write` is listed. The procedure body is entirely read-only (audit operation). The skill's "What This Skill Does NOT Do" section explicitly states "Does not rewrite the prompt. Read-only." The only write path is the Boundary-Case Encounter Logging section, which writes to `operations/system-log/`. `Write` should be scoped to that narrow use case, but the skill lists it flatly alongside the read tools — over-granting for the primary operation | G5 §Recovery: audit interface for poka-yoke | 1 | High |
| 9 | Skill tool usage — non-deterministic consumer design | Tool descriptions designed for non-deterministic consumers; disambiguate | G5.I2 | Partial | `Skill` tool purpose is implicit (invoking `/prompt-evaluator`). Step 1 names the specific skill invoked and the condition. However there is no disambiguation of when the `Skill` tool should be preferred over reading a prior output file (both paths exist in Step 1) | G5 §Recovery | 1 | Medium |
| 10 | Skills scoped to workspaces and task types, not loaded globally | Skills are scoped appropriately; surface exceeding five capabilities uses workspace routing | G5.I3 | Satisfied | The skill invokes only `/prompt-evaluator` via Skill tool — a single, named delegation. No broad skill surface is loaded | G5 §Recovery | 1 | High |
| 11 | Permissions tiered by risk | Permissions tiered by risk, not binary | G6.I1 | Partial | No explicit risk-tiering of the tool surface. `Read`/`Glob`/`Grep` (read-only), `Skill` (delegated execution, medium risk), and `Write` (state mutation, high risk) are listed flatly | G6 §Recovery | 1 | Medium |
| 12 | Safety-critical constraints enforced structurally | Safety-critical constraints enforced structurally | G6.I2 | Partial | Read-only constraint is stated in prose. `Write` in allowed-tools structurally permits writing, which contradicts the stated read-only constraint. The only narrowing is the prose instruction "Read-only" and the fact the procedure has no Write steps (except encounter logging). Structural mismatch between allowed-tools and stated constraint | G6 §Recovery | 1 | High |
| 13 | Defense is layered | Defense is layered — no single mechanism is sole protection | G6.I4 | Violated | The read-only constraint has only one layer: prose instruction. `allowed-tools` does not restrict Write to the encounter-logging path only. If the model writes to a non-encounter-log path, there is no structural second layer to intercept it | G6 §Recovery | 1 | High |
| 14 | Destructive/irreversible actions require human approval | G9.I6: destructive or irreversible actions always require human approval | G9.I6 | Partial | The primary skill operation is read-only; there is no intended destructive action. The incidental Write path (encounter logging to `operations/system-log/`) is a benign append operation. However the mismatch between `Write` in allowed-tools and the "read-only" stated constraint means there is latent capability for unintended writes without any approval gate. G9.I6 is not violated by design intent but is at risk due to over-broad tool grant | G9 §Recovery | 1 | Medium |
| 15 | Trigger description fires reliably | Description phrased as consumer would ask; triggers reliably | G8.I1 | Partial | The description is accurate but may under-fire. It is phrased from a technical perspective ("Extend a /prompt-evaluator run with IL-KB-grounded additions...") rather than from a consumer question perspective ("when should I use this?"). The "When to Use This Skill" section compensates with better consumer-facing language, but the frontmatter description is the primary trigger surface | G8 §Recovery | 1 | Medium |
| 16 | Prompt carries explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | G8.I2 | Partial | ROLE (Librarian Audit) is explicit. CONSTRAINTS ("Does not duplicate," "precondition gating is non-negotiable") are explicit. AUTHORITY is implied (Librarian). FAILURE SIGNAL is absent — no definition of what an invalid or insufficient audit output looks like | G8 §Recovery | 1 | Medium |
| 17 | High-priority behavioral rules as negative constraints | G8.I3 | Satisfied | "What This Skill Does NOT Do" uses negative form for all three load-bearing constraints. "Cognitive Disposition" uses "bias is toward reporting 'no IL additions apply' rather than inventing redundant findings" — a strong negative-space framing | G8 §Recovery | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|---|---|---|---|
| a | Shared skills are versioned and locked | G5 governance | Is there a lock or version reference for the `/prompt-evaluator` skill that `/assess-prompt` delegates to? If `/prompt-evaluator` changes its output format, does `/assess-prompt` detect the mismatch? | Skill version lock file or interface contract |
| b | Tool output format matches the consumer | G5.I5 | The integrated output (Step 4) is a structured markdown report. Is this format tested against the downstream consumer's actual reading behavior (Nick reviewing inline in conversation vs. reading a file)? | Consumer review; output format test |
| c | Encounter logging Write path — is it tested in dry-run? | G9.I6 | The only Write call in this read-only skill is encounter logging. Is there a test that verifies encounter logging writes only to `operations/system-log/` and not to KB or skill files? | Integration test or manual verification record |
| d | Approval rates for Skill-tool invocations monitored | G6 governance | Is the `/prompt-evaluator` sub-invocation tracked in the encounter log or session audit trail? If `/prompt-evaluator` silently fails, is that surfaced? | SL entry review; sub-skill failure detection |

---

### Aspects out of scope

| Guide | Why latent |
|---|---|
| G2a/G2b | Skill does not embed context directives into the assessed prompt; it reads and evaluates the prompt's context characteristics. G2a/G2b Preconditions not satisfied for the skill itself (though they may fire within the IL extension when the assessed prompt contains context directives) |

---

### DD-92 ContextSpec audit

DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

---

### Summary

**G9.I6 outcome: Partial — over-broad tool grant creates latent write risk in a declared read-only skill.** The primary design intent is read-only and the procedure body does not contain intended destructive actions. However listing `Write` in `allowed-tools` for a skill that declares itself "Read-only" is a structural contradiction (G5.I1 Violated, G6.I2 Partial, G6.I4 Violated). The fix is to either remove `Write` from `allowed-tools` entirely (if encounter logging can be done via a separate call) or to explicitly scope and document the Write path as a named exception with its own HITL consideration. Additional load-bearing gaps: acceptance criteria missing (G1.I3), FAILURE SIGNAL absent (G8.I2), trigger description under-fires for consumer phrasing (G8.I1 Partial).

---

### Skill: `systems/improvement-loop/.claude/skills/assess-skill/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 8, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md (meta-circular self-assessment)

mode: in-context-rubric (assess-skill SKILL.md loaded; rubric applied directly per procedure; artifact and assessor are the same file — meta-circular self-assessment per orchestrator instruction)

**Artifact:** `systems/improvement-loop/.claude/skills/assess-skill/SKILL.md`
**Classification:** safety-critical (trigger: `allowed-tools` includes Write — narrowly scoped to `operations/system-log/` boundary-case encounter logging, same pattern as `assess-agent`)
**Composed guides:** G1 (spec quality), G3b (workflow/termination), G5 (tool use), G6 (safety/permissions), G8 (prompt/trigger quality), G9 (governance — G9.I6 forced for safety-critical)
**Rubric size:** 13 file-verifiable invariants, 5 system/process-verifiable invariants, 1 latent (out-of-scope)

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | G9.I6 — HITL gate for destructive actions | Destructive or irreversible actions always require human approval regardless of trust level. | G9 §Invariants | Satisfied | Same pattern as `assess-agent`: Write is narrowly scoped to `operations/system-log/` for boundary-case encounter logging. "Write scope is narrowed to `operations/system-log/` only — do not write elsewhere." The primary audit output is conversation-only. The scope constraint is explicit and the Write operation is append-only and auditable. G9.I6 is satisfied. | — | 1 | High |
| 2 | G1 — Spec completeness: objective, constraints, stop rules, autonomy | Spec includes objective, desired outcomes, constraints, stop rules | G1 §Invariants | Satisfied | Objective: clear. Constraints: "Read-only. Does not rewrite the skill. Does not deploy or activate the skill." Stop rules via "Boundaries" section: reject non-skill artifacts, halt for variant ambiguity. Strong spec discipline. | — | 1 | High |
| 3 | G1 — Stop rules: halt condition | Stop rules include at least one halt condition | G1 §Invariants | Satisfied | "Boundaries: If the submitted artifact doesn't have skill frontmatter (`name`, `description`, `allowed-tools`), reject." Explicit halt/reject on malformed input. | — | 1 | High |
| 4 | G1 — Stop rules: escalation trigger | Stop rules include at least one escalation trigger | G1 §Invariants | Partial | "If `allowed-tools` includes destructive tools but the procedure body does not describe the destructive operations, flag as a follow-up (the skill may be misconfigured)." This is an escalation-to-follow-up, not a pause-for-human. No explicit "ask user to confirm before proceeding" escalation trigger. The skill proceeds to full audit regardless of input complexity. | Add: "If the submitted skill is longer than ~300 lines, ask for scoping clarification before full audit (parallel to `assess-agent`'s 500-line limit)." The skill specifies this limit for `assess-agent` but not for itself. | 1 | Medium |
| 5 | G1 — Acceptance criteria evaluable by third party | Acceptance criteria evaluable by a third party without access to the prompter's intent | G1 §Invariants | Missing | No explicit acceptance criteria. "Output Shape: See `audit.md` §'Output shape'" defers to the external doc but does not specify when this skill has succeeded. A third party cannot verify skill completion without reference to `audit.md`. | Add: "Success: report produced with classification note, file-verifiable findings table, follow-ups table, out-of-scope table, and summary. Every finding cites a source guide and has a tier and confidence label." | 1 | Medium |
| 6 | G3b — Termination conditions | Every iterative pattern has a termination condition | G3b §Invariants | Satisfied | Steps 0–5 are sequential phases. Rubric-building and rubric-application iterate over finite invariant sets. Termination implicit on exhaustion. | — | 1 | High |
| 7 | G3b — Explicit state tracking independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b §Invariants | Partial | Primary output is conversation-only. Boundary-case log write is the only persistent output. An audit run that completes but is not copied by the user is lost. Same gap as `assess-agent` (finding #7 above). | Consider specifying optional `--save` flag or output path. | 1 | Medium |
| 8 | G5 — Minimal tool surface | Only tools needed for the current task are loaded | G5 §Invariants | Satisfied | `allowed-tools: Read Grep Glob Write` — identical to `assess-agent`. Minimal and justified. | — | 1 | High |
| 9 | G5 — Intermediate results management | Intermediate results outside context window when only final output needed | G5 §Invariants | Partial | Step 1.4: "Read the `### Contract` subsection of each guide in the set." The Contract sections are required for rubric-building, so they must be in context. However, the guide files (G1, G3b, G5, G6, G8, G9) are large (34k–80k characters). If full files are read rather than targeted Contract sections, context bloat is significant. Step 3 of the procedure instructs "`Read` the `### Contract` subsection of each guide" — the instruction is correct but the anchor-targeting mechanism is fragile: guides do not have consistent `### Contract` headings (as confirmed by the grep results during this audit, which found `## Contract` rather than `### Contract`). This creates a latent risk that the Grep-and-line-range mechanism fails and full files are read instead. | Audit Note: The guides use `## Contract` (H2), not `### Contract` (H3). The `assess-skill` procedure says "Read the `### Contract` subsection" — this heading level is wrong, which means the Grep used to locate the section will fail unless the reader adjusts for H2. This is a concrete procedure bug. | 1 | High |
| 10 | G6 — Permissions tiered by risk | Permissions tiered by risk | G6 §Invariants | Satisfied | Read/Grep/Glob are read-only; Write narrowly scoped to SL. Effective separation. | — | 1 | High |
| 11 | G6 — Safety-critical constraints enforced structurally | Safety-critical constraints enforced structurally, not via prompt instructions alone | G6 §Invariants | Partial | Write-path restriction to `operations/system-log/` is prose-only. Same gap as `assess-agent`. | System-verifiable: confirm harness enforces path restriction. | 1 | Medium |
| 12 | G8 — Trigger description quality | Description phrases the trigger the way a consumer would ask | G8 §Invariants | Satisfied | "Audit a consumer-submitted SKILL.md against Contract-derived criteria from IL guides G1, G3b, G5, G6, G8 — plus G9.I6 for safety-critical skills." Highly specific, consumer-phrasing-aligned, names the guides and safety-critical gate. "When to Use This Skill" adds concrete trigger conditions. | — | 1 | High |
| 13 | G8 — ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | G8 §Invariants | Partial | ROLE: "Librarian Audit — read-only, citation-grounded, safety-aware." — present. Constraints: present ("Read-only"). The G9.I6 gate is effectively a CONSTRAINT declaration. AUTHORITY: implied (Librarian) but not explicitly named. FAILURE SIGNAL: "Boundaries: If the submitted artifact doesn't have skill frontmatter, reject" is a failure signal — but no FAILURE SIGNAL for guide-read failures (same gap as `assess-agent` finding #13). | Add FAILURE SIGNAL for guide unavailability: "If a required guide Contract section cannot be read, declare which guide is missing, note it as a KB gap in the report, and produce a partial audit over available guides." | 1 | Medium |
| 14 | DD-92 ContextSpec | `context:` block absent | DD-92 | N/A (skipped) | No `context:` block in frontmatter. DD-92 ContextSpec audit skipped — DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here. | — | — | — |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|------------------|
| a | Guide heading level correctness | (Procedure correctness) | Step 1.4 says to read the `### Contract` subsection (H3) but the actual guides use `## Contract` (H2). Has this discrepancy been noted and does the executor-in-practice adjust for H2? Is there a test case verifying the Grep-then-read-range mechanism works against actual guide files? | Evidence: test invocation showing successful Contract section targeting in a guide file |
| b | Write path restriction structurally enforced | G6 §Invariants | Same question as `assess-agent` follow-up (a): is `operations/system-log/` Write restriction enforced at harness level? | Evidence: harness settings.json path restriction |
| c | Context budget for 6-guide audit | G5 §Invariants | A full audit reads Contract sections from {G1, G3b, G5, G6, G8, G9} plus the skill file plus `audit.md` plus `skill.md`. If Contract sections are ~30–60 lines each across 6 guides, the total is manageable. But if full guide files are read (due to heading-level mismatch noted in finding #9), the budget is at risk. | Evidence: confirmed section-targeted reads in a prior audit session |
| d | Audit report persistence | G3b §Invariants | Same question as `assess-agent` follow-up (c): how are conversation-only audit reports retained? | Evidence: session practice or `--save` flag |
| e | Meta-circular self-assessment validity | (Audit-integrity) | This audit is a meta-circular self-assessment (assess-skill applied to itself). Is there a separation-of-concerns policy for the generator-assessor rule (memory note: "Generator-assessor separation — Standing rule: the generator must not assess its own output")? This skill was generated before this session; the assessor is applying the rubric now. However, future uses where a just-designed assess-skill is immediately self-audited without a separate assessor would violate the generator-assessor rule. | Evidence: policy or convention specifying that assess-skill self-audits are only permitted when the skill is stable (not freshly authored in the same session) |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G9 (beyond I6) | Same as other Librarian skills — single-purpose read-mostly skill; G9.I6 fires for Write; remaining G9 invariants latent. |

---

### Summary

G9.I6: **Satisfied.** Write is narrowly scoped to `operations/system-log/` (append-only encounter logging). Primary output is conversation-only. No HITL gate required given the scope.

The most significant finding in this self-audit is finding #9 (High confidence, Tier 1): **the procedure references `### Contract` (H3) but the actual guide files use `## Contract` (H2).** This is a concrete procedure bug that causes the Grep-then-line-range mechanism for section targeting to fail against real guide files. Every invocation of this skill that relies on Grep for Contract section targeting is at risk of falling back to full-file reads, with attendant context budget impact and potential missed-section errors. This should be corrected in the procedure to reference `## Contract`.

Other load-bearing findings:
- Finding #5: Missing acceptance criteria.
- Finding #4: No oversize-input escalation trigger (the 500-line limit that `assess-agent` specifies is absent here).
- Finding #7: Primary output is ephemeral.

Finding #13 (missing FAILURE SIGNAL for guide-read failures) is shared with `assess-agent` and reflects a systematic gap across the Librarian skill family — both skills leave guide-unavailability behavior undefined.

No DD-92 ContextSpec findings — `context:` block absent; check not applicable.

---

### Skill: `systems/improvement-loop/.claude/skills/cleanup-cache/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 9, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** safety-critical (Bash with rm -rf under --purge)

**Critical:** **G9.I6 SATISFIED** — Step 4 explicit confirmation gate ("Do not proceed without a 'yes'") before any rm -rf execution.

**G9.I6 outcome:** Satisfied — confirmation gate is structural and unambiguous.

**Top findings:**
- F#1 Satisfied G9.I6: explicit confirmation before destructive deletion.
- F#3 Missing: no `## Boundary conditions` section.
- F#4 Partial: "Never delete outside known temp paths" is prose-only — should pass paths as Bash allowlist.

---

### Skill: `systems/improvement-loop/.claude/skills/compare-repos/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 5, fresh context, mode: in-context-rubric)*

## Audit — skill (compare-repos)

**mode: in-context-rubric**

**Artifact:** `systems/improvement-loop/.claude/skills/compare-repos/SKILL.md`
**Classification:** Safety-critical (trigger: `allowed-tools` includes Write).
**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — G9.I6 forced)
**Rubric size:** 22 file-verifiable invariants, 3 system-verifiable invariants, 1 latent

**DD-92 ContextSpec audit:** No `context:` block in frontmatter. DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Contract presence | All required spec fields present. | G1.I1 | Satisfied | Skill includes objective (cross-repo synthesis), acceptance criteria (comparison report with citation-grounded matrix), stop rules (abort conditions in §Boundary Conditions), constraints (read-only on KB, no auto-promotion, cite-every-cell), autonomy levels (write gated on `--write` + explicit approval), context supply plan (Paths table). | — | 1 | High |
| 2 | Templates filled completely — no TBD/TODO placeholders | G1.I2 | Satisfied | No placeholder fields. All body sections populated. Output shape includes complete report structure templates. | — | 1 | High |
| 3 | Hard constraints enforced outside prompt layer | G1.I3 | Partial | Rule 7 ("Write is opt-in and approval-gated") and Rule 8 ("Existing report preserved via Version Log") are prose-only. No structural enforcement. | G1 §Recovery | 1 | Medium |
| 4 | Acceptance criteria evaluable by third party | G1.I4 | Satisfied | "citation-grounded comparison report," cite-every-cell rule (Rule 2), pattern-threshold rules (Rule 3: "shared" = 3+ repos), and write-path spec are all third-party verifiable. | — | 1 | High |
| 5 | Stop rules include halt, escalation, completion | G1.I5 | Satisfied | §Boundary Conditions: "Termination — abort: Working set < 2 repos; stop..." and "Working set has missing inputs that the user must fill; stop and request /repo-analyzer runs first." Completion: "A citation-grounded comparison report has been produced." | — | 1 | High |
| 6 | Planning probabilistic; execution deterministic. State tracking independent of conversation. | G3b.I1/I2 | Partial | No explicit intermediate state tracking. If session is interrupted between Step 2 (matrix) and Step 6 (report assembly), the work is lost. No temp-file pattern for in-progress matrix data. | G3b §Recovery | 1 | Medium |
| 7 | Every iterative pattern has a termination condition. | G3b.I3 | Satisfied | Step 2 iterates over dimension tables (bounded by dimensions-in-scope list). Step 3 iterates over dimensions from Step 2 (bounded). No unbounded loops. | — | 1 | High |
| 8 | Degradation modes defined before go-live. | G3b.I4 | Satisfied | §Boundary Conditions — abort conditions for missing inputs and insufficient repo count. Step 0 validation catches argument errors before execution begins. | — | 1 | High |
| 9 | Only tools needed loaded into context. | G5.I4 | Satisfied | `Read Grep Glob Write` — Read loads analysis docs, Glob enumerates `*-analysis.md` files, Grep searches KB findings, Write creates/updates the comparison report. All four are demonstrably needed. | — | 1 | High |
| 10 | Tool descriptions designed for non-deterministic consumers. | G5.I3 | Satisfied | Description frontmatter captures multiple consumer phrasings: "compare the watched libraries," "what patterns are emerging across the ecosystem," "which of our watched libraries handles X best." | — | 1 | High |
| 11 | Intermediate tool results stay outside context window. | G5.I5 | Partial | Analysis docs can be large (up to 67k chars observed in the codebase); all are loaded via Read into context in Step 1. No progressive-loading or summarization strategy is specified for large analysis docs. This could bloat context on a full-set comparison. | G5 §Recovery — "If context is bloated with tool definitions: implement deferred loading" | 1 | Medium |
| 12 | Complex tools include usage examples. | G5.I6 | Satisfied | Step 2 specifies dimension shapes and example column structures. Step 3 provides named pattern threshold rules. Sufficient for non-deterministic consumer guidance. | — | 1 | High |
| 13 | Skills framework-agnostic. | G5.I11 | Satisfied | Plain markdown, no SDK coupling. | — | 1 | High |
| 14 | Permissions tiered by risk. | G6.I1 | Partial | Write is tiered: `--write` flag required, then explicit `y` approval after inline presentation. No explicit risk-tier table for Read vs. Write operations. The write path is described as "mild on write" in §Safety-critical. | G6 §Recovery | 1 | Medium |
| 15 | Safety-critical constraints enforced structurally. | G6.I2 | Violated | Write-gate is model-prose-only ("Write only on explicit `y`"). No harness hook or permission entry prevents writing outside the designated path without approval. | G6 §Recovery | 1 | High |
| 16 | Agent cannot modify its own permission configuration. | G6.I3 | Satisfied | No self-modification path present. | — | 1 | High |
| 17 | Defense is layered. | G6.I4 | Violated | Write-gate is a single layer (prose). No second protective mechanism. | G6 §Recovery | 1 | High |
| 18 | Prompts tell model what to produce, not how to think. | G8.I1 | Satisfied | Procedure steps specify outputs (matrix tables, pattern clusters, recommendation set, report) without prescribing CoT. | — | 1 | High |
| 19 | High-priority rules as negative constraints. | G8.I3 | Satisfied | Key constraints negatively stated: "Does not analyze individual repos," "Does not promote findings," "Does not modify per-repo analysis docs," "Does not perform web research." Rules section uses "never" and "no" framing. | — | 1 | High |
| 20 | ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL properties. | G8.I6 | Partial | ROLE (Librarian — Teacher/Builder modes) explicit in Cognitive Disposition. CONSTRAINT pervasive. AUTHORITY implicit. FAILURE SIGNAL absent — no specification of what consumers should observe if the skill fails (e.g., if `/index.md` is missing, if all analysis docs are stale). | G8 §Recovery | 1 | Medium |
| 21 | **G9.I6 — Destructive or irreversible actions require human approval.** | G9.I6 | **Satisfied** | The write to `cross-repo-comparison.md` requires both (a) the `--write` flag and (b) explicit `y` approval after seeing the inline report. Previous version is preserved via Version Log — not destructive. Rule 8 explicitly prohibits silent overwrites. | — | 1 | High |
| 22 | No decision type defaults to full autonomy. | G9.I5 | Satisfied | No unchecked autonomous decision paths. Pattern-clustering uses explicit thresholds (Rule 3). Builder mode activates only on `--focus` signal. | — | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | Structural enforcement on write gate. | G6.I2 | Is there a harness hook or permission restriction preventing writes outside `watched-libraries/analysis/` without the explicit `y` approval? Or is the gate solely model-prose? | Hook configuration entry; or acknowledgment of the structural gap. |
| b | Context bloat on large analysis docs. | G5.I5 | In practice, how many analysis docs are loaded simultaneously? Have large-doc comparisons (5+ repos with large analysis files) been tested? If context limits are hit, is progressive loading or summarization planned? | Test run evidence; or acknowledgment of a known gap and mitigation plan. |
| c | Audit trail for writes. | G9.I2 | Is the write to `cross-repo-comparison.md` logged in the IL system log? | System-log entry pattern or explicit acknowledgment. |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G2a/G2b | No context directives or caching behavior — G2 Preconditions unsatisfied. |
| G3b.I6 (cost controls) | Skill is on-demand and single-session; no autonomous recurring execution — cost control invariant not load-bearing here. |
| G7 | Single-session, no cross-session state management. |

---

### Summary

Classification: safety-critical (trigger: `allowed-tools` includes Write).

**G9.I6 outcome:** Satisfied — the write is double-gated (`--write` flag + explicit `y` after inline presentation), and the write is non-destructive (Version Log preserves prior content). This is the strongest write-gate implementation among the five audited skills.

**What the skill does well:** The skill has clear abort conditions, complete boundary conditions, and well-specified output shape with explicit citation rules and pattern-threshold contracts. The Teacher/Builder mode separation is cleanly implemented (Builder mode activates only on `--focus`). The deprecation of `/repo-analyzer --compare` mode with a clean handoff to this skill is correctly documented.

**Risks that remain:** (1) Structural enforcement gap on write gate (G6.I2, G6.I4 — findings 15, 17) — the same pattern observed across all design skills. (2) No intermediate state persistence for long multi-repo comparisons (G3b.I2 — finding 6); this is a real risk for full-set comparisons. (3) Context bloat on large analysis-doc loads (G5.I5 — finding 11). (4) No FAILURE SIGNAL property (G8.I6 — finding 20). None of these are hard-blocking.

---

### Skill: `systems/improvement-loop/.claude/skills/design-agent/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 5, fresh context, mode: in-context-rubric)*

## Audit — skill (design-agent)

**mode: in-context-rubric**
(The Skill tool invoked /assess-skill but the skill body runs in-context per the assess-skill SKILL.md procedure. All rubric steps executed below.)

**Artifact:** `systems/improvement-loop/.claude/skills/design-agent/SKILL.md`
**Classification:** Safety-critical (trigger: `allowed-tools` includes Write; `Task` spawns subagents that may perform writes).
**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — G9.I6 forced)
**Rubric size:** 22 file-verifiable invariants, 4 system-verifiable invariants, 0 latent

**DD-92 ContextSpec audit:** No `context:` block in frontmatter. DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Contract presence | Every agent spec produced includes at minimum: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, stop rules (all three types), and a context supply plan. | G1.I1 | Satisfied | Procedure Steps 0–6 specify variant selection, intent capture, Decision record, risk surfacing, draft, audit delegation, and report assembly — all load-bearing spec sections are authored. | — | 1 | High |
| 2 | Templates filled completely — no TBD/TODO placeholders | G1.I2 | Satisfied | §Step 4 instructs: "The draft must be complete: frontmatter populated, common-core sections present, declared variant's overlay sections present, no `<placeholder>` text remaining for required fields." | — | 1 | High |
| 3 | Hard constraints have enforcement mechanisms outside the prompt layer | G1.I3 | Partial | G9.I6 and autonomy-envelope gates are stated as "hard gates" in prose, but enforcement is solely declarative prose — no harness-level enforcement mechanism is referenced (no hook, no permission restriction). | §Procedure Step 7 and §Boundaries; G1 §Recovery | 1 | Medium |
| 4 | Stop rules include halt condition, escalation trigger, completion criterion | G1.I5 | Partial | §Boundaries names write-blocking conditions and inline-only default. No explicit abort/halt criterion for mid-procedure failures (e.g., subagent invocation failure in Step 5). | G1 §Recovery | 1 | Medium |
| 5 | Planning is probabilistic; execution is deterministic. Every workflow has explicit state tracking independent of conversation history. | G3b.I1/I2 | Partial | The Decision record (Phase 2) provides state tracking. However, state is embedded in conversation context only — no explicit durable state mechanism is referenced for multi-step execution. | G3b §Recovery | 1 | Medium |
| 6 | Every iterative pattern has a termination condition (loop limit, stall detection, or both). | G3b.I3 | Satisfied | The Decision sequence walk (Step 2) has explicit gate conditions per variant; Step 6 defines write-or-no-write terminal conditions. No open-ended iteration loops in the procedure. | — | 1 | High |
| 7 | Cost controls (budgets, termination rules) are in place before autonomous execution. | G3b.I6 | Not Applicable | This skill is designer-interactive, not autonomously executing long workflows. G3b Precondition (side-effects longer than a single turn) is marginally satisfied due to Task invocation; however, no budget/cost controls are specified for the subagent delegation in Step 5. | G3b §Recovery | 1 | Low |
| 8 | Only tools needed for the current task are loaded into context. | G5.I4 | Satisfied | `allowed-tools: Read Grep Glob Write Task` — all five tools are used in the procedure (Read loads substrate, Grep/Glob navigate KB, Write creates temp draft for audit, Task invokes subagent). Minimal for the operation's scope. | — | 1 | High |
| 9 | Tool descriptions are designed for non-deterministic consumers — they persuade, disambiguate, and explain when not to use the tool. | G5.I3 | Satisfied | `description` frontmatter is consumer-phrasing-oriented and names both positive trigger ("Draft a new agent specification") and scope boundaries. | — | 1 | High |
| 10 | Skills are framework-agnostic markdown files — portable across SDKs and agent frameworks. | G5.I11 | Satisfied | The SKILL.md is plain markdown with no SDK-specific dependencies. | — | 1 | High |
| 11 | Skills are scoped to workspaces and task types, not loaded globally, when surface exceeds five capabilities. | G5.I12 | Satisfied | Declared as `user-invocable: true`; scoped to IL workspace. | — | 1 | High |
| 12 | Permissions are tiered by risk, not binary allow/deny. | G6.I1 | Partial | The write gate (§Boundaries: "Writing to `--target-path` requires explicit per-invocation approval AND clean audit findings on hard gates") tiered by approval condition, but no explicit risk-tier classification for each allowed tool is stated. | G6 §Recovery | 1 | Medium |
| 13 | Safety-critical constraints are enforced structurally, not via prompt instructions alone. | G6.I2 | Violated | The write-gate constraint ("do NOT offer the write" when hard-blocking issues found) is enforced only by prose instructions to the executing model. No structural enforcement (hook, harness permission restriction, or code-level gate) is referenced. | G6 §Recovery — "enforce structurally" | 1 | High |
| 14 | The agent cannot modify its own permission configuration. | G6.I3 | Satisfied | No mechanism in the procedure allows self-modification of permissions. | — | 1 | High |
| 15 | Defense is layered — no single mechanism is sole protection. | G6.I4 | Violated | The write-gate is solely the model's own conditional logic in Step 6. No second layer (hook, harness-level restriction, human confirmation step separate from the model's judgment) is present. | G6 §Recovery | 1 | High |
| 16 | Prompts tell the model what to produce, not how to think. | G8.I1 | Satisfied | Procedure steps specify outputs (Decision record, risk surface, draft, audit report, assembled report) without prescribing CoT or reasoning path. | — | 1 | High |
| 17 | High-priority behavioral rules expressed as negative constraints, not positive aspirations. | G8.I3 | Satisfied | Key constraints are stated as "do NOT": "Do not write to a file at this phase," "Do not inspect the draft against G1/G2a…," "Do not pre-decide between variants." | — | 1 | High |
| 18 | Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, and FAILURE SIGNAL properties. | G8.I6 | Partial | ROLE (Librarian Builder mode) is explicit. CONSTRAINT is present throughout. AUTHORITY is implicit (derives from IL rule 12). FAILURE SIGNAL — what the consumer should observe if the skill fails — is absent. | G8 §Recovery | 1 | Medium |
| 19 | **G9.I6 — Destructive or irreversible actions always require human approval regardless of trust level.** | G9.I6 | **Partial** | The write to `--target-path` is gated on explicit `y` after presenting the report ("Write only on explicit `y`. Default is inline-only"). This satisfies the spirit of G9.I6. However: (a) the temp file write in Step 5 (`/tmp/design-agent-draft-<timestamp>.md`) is not gated on approval; (b) the enforcement is model-instructed, not structural. The temp-file write is low-blast-radius but the absence of structural enforcement on `--target-path` means a model drift could bypass the gate. | G9 §Recovery — enforce destructive-action gates architecturally | 1 | Medium |
| 20 | Audit trail maintained for all agent actions — append-only, immutable, queryable. | G9.I2 | Not addressed | No audit trail mechanism is specified for writes performed by this skill (temp file, target-path file). | G9 §Recovery | 1 | Medium |
| 21 | No decision type defaults to full autonomy without explicit classification. | G9.I5 | Satisfied | Every decision in the procedure requires either designer input or explicit approval gates; no unchecked autonomous decision paths. | — | 1 | High |
| 22 | Comprehension maintained for shipped work — agent-generated artifacts that no human has read are governance debt. | G9.I7 | Partial | The write-gate requires explicit approval AND clean audit findings, which partially satisfies comprehension. But comprehension of the audit report itself (Step 5 output from `/assess-agent`) is not explicitly required before the approval prompt. | G9 §Recovery | 1 | Low |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | Every workflow has explicit state tracking independent of conversation history. | G3b.I2 | Is the Decision record persisted outside conversation context (e.g., written to a file before the subagent invocation in Step 5)? If the session is interrupted between Step 4 and Step 6, is the Decision record recoverable? | Description of state-persistence mechanism or acknowledgment that single-session assumption is intentional. |
| b | Cost controls are in place before autonomous execution. | G3b.I6 | The Task invocation in Step 5 spawns a subagent. Is there a timeout or token-budget limit on the subagent invocation? | Harness configuration or explicit timeout parameter documented. |
| c | Safety-critical constraints are enforced structurally. | G6.I2 | Is there a harness-level hook or permission restriction that prevents writing to `--target-path` without an explicit approval signal? Or is the gate solely in the model's procedure? | Hook configuration, CI check, or harness permission entry. |
| d | Audit trail maintained for agent actions. | G9.I2 | Is the write to `--target-path` (and the temp file) logged anywhere outside the conversation? Does the IL system log capture skill invocations? | System-log entry, hook, or session-log reference showing writes are traced. |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G2a/G2b (context management) | Skill does not embed context directives or specify context-caching behavior — G2 Preconditions unsatisfied. |
| G7 (session persistence) | Skill is single-session by design; no cross-session state management specified — G7 Preconditions not triggered. |
| G10 (agentic systems orchestration) | Skill delegates to a subagent via Task but does not define a multi-agent topology with its own coordination contract — G10 not load-bearing here. |

---

### Summary

Classification: safety-critical (trigger: `allowed-tools` includes Write; Task spawns a subagent that may write).

**G9.I6 outcome:** Partial — the `--target-path` write is gated on explicit per-invocation approval (`y/N`), satisfying the letter of the invariant. The temp-file write in Step 5 is ungated. More critically, both gates are model-instruction-enforced only (findings 13, 15, 19); no structural enforcement layer exists. This does not block deployment for a read/draft skill, but the absence of structural enforcement is a known risk if model behavior drifts.

**What the skill does well:** The variant-aware Decision sequence (10 steps) is thorough and well-structured. The generator-assessor separation (rule 10) is correctly implemented — Step 5 explicitly delegates to `/assess-agent` as a fresh subagent and prohibits self-assessment. Write-blocking on hard-gate audit findings (Step 6) is the right gate condition. Negative-constraint framing (G8.I3) is consistent throughout.

**Risks that remain:** (1) Structural enforcement gap on the write gate (G6.I2, G6.I4 — findings 13, 15). (2) No explicit FAILURE SIGNAL property for consumers (G8.I6 — finding 18). (3) No audit trail for writes (G9.I2 — finding 20). (4) Mid-procedure abort path undefined (G1.I5 — finding 4). These are medium-severity gaps addressable in a revision; none individually block the skill's core function.

---

### Skill: `systems/improvement-loop/.claude/skills/design-skill/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 5, fresh context, mode: in-context-rubric)*

## Audit — skill (design-skill)

**mode: in-context-rubric**

**Artifact:** `systems/improvement-loop/.claude/skills/design-skill/SKILL.md`
**Classification:** Safety-critical (trigger: `allowed-tools` includes Write; Task spawns subagent).
**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — G9.I6 forced)
**Rubric size:** 22 file-verifiable invariants, 4 system-verifiable invariants, 0 latent

**DD-92 ContextSpec audit:** No `context:` block in frontmatter. DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Contract presence | Every spec includes objective, desired outcomes, constraints, autonomy levels, acceptance criteria, stop rules, and context supply plan. | G1.I1 | Satisfied | Skill includes: objective (draft SKILL.md from intent), acceptance criteria (draft complete, no placeholders, audit findings embedded), stop rules (§Boundaries: no-deploy default, write blocked on hard gates, redirect if not-a-skill), constraints (no self-assessment, no substrate modification, no deploy), context supply plan (Paths table). | — | 1 | High |
| 2 | Templates filled completely — no TBD/TODO placeholders | G1.I2 | Satisfied | No placeholder fields in frontmatter or body. All required sections populated. | — | 1 | High |
| 3 | Hard constraints enforced outside the prompt layer | G1.I3 | Partial | Safety-critical gate (Step 4) and write-blocking (Step 6) are prose-only. No harness enforcement outside the model's own conditional logic. | G1 §Recovery | 1 | Medium |
| 4 | Stop rules include halt, escalation, completion | G1.I5 | Partial | §Boundaries names write-blocking (hard gate violations → no write offer). No explicit abort path for Step 5 subagent invocation failure. No escalation path when the designer provides intent that cannot be scoped to a single skill. | G1 §Recovery | 1 | Medium |
| 5 | Planning probabilistic; execution deterministic. State tracking independent of conversation. | G3b.I1/I2 | Partial | Decision record (Phase 2) provides state, but it is embedded in conversation context only. No external file written until the temp scratch file in Step 5. If session is interrupted between Steps 2–4, Decision record is lost. | G3b §Recovery | 1 | Medium |
| 6 | Every iterative pattern has a termination condition. | G3b.I3 | Satisfied | Decision sequence walk (Steps 1–7 in Step 2) is bounded and sequential, not looping. No open-ended iteration. | — | 1 | High |
| 7 | Degradation modes defined before system goes live. | G3b.I4 | Partial | §Boundaries covers redirect conditions and oversized-partial handling. Step 4 safety-critical gate is a degradation handler. However, no explicit degradation mode for Step 5 subagent invocation failure (what happens if `/assess-skill` returns an error). | G3b §Recovery | 1 | Medium |
| 8 | Only tools needed for the current task are loaded. | G5.I4 | Satisfied | `Read Grep Glob Write Task` — Read loads substrate, Grep/Glob navigate KB, Write creates temp scratch file for audit, Task invokes subagent. All five are needed. | — | 1 | High |
| 9 | Tool descriptions designed for non-deterministic consumers. | G5.I3 | Satisfied | `description` frontmatter uses consumer phrasing: "Draft a new SKILL.md from designer intent using IL substrate." | — | 1 | High |
| 10 | Skills are framework-agnostic markdown files. | G5.I11 | Satisfied | Plain markdown, no SDK coupling. | — | 1 | High |
| 11 | Permissions tiered by risk. | G6.I1 | Partial | Write is tiered to "explicit per-invocation designer approval AND clean audit findings." No explicit risk classification for Bash-equivalent tools. Task spawning is not risk-classified. | G6 §Recovery | 1 | Medium |
| 12 | Safety-critical constraints enforced structurally. | G6.I2 | Violated | Write-gate ("Write only on explicit `y`") is model-prose-enforced only. No harness hook or permission entry prevents writes to `--target-path` absent the `y` signal. | G6 §Recovery | 1 | High |
| 13 | Agent cannot modify its own permission configuration. | G6.I3 | Satisfied | No permission self-modification path in the procedure. | — | 1 | High |
| 14 | Defense is layered. | G6.I4 | Violated | Write-gate is a single layer (prose instruction). No second layer. | G6 §Recovery | 1 | High |
| 15 | Prompts tell model what to produce, not how to think. | G8.I1 | Satisfied | Procedure steps specify outputs (Decision record, authoring-time risks, draft, audit output, assembled report) without prescribing CoT. | — | 1 | High |
| 16 | High-priority rules as negative constraints. | G8.I3 | Satisfied | Key constraints use negation: "Does not deploy," "Does not internally assess the draft," "Do not write the draft to a file at this phase," "The skill must not internally inspect the draft against G1/G3b…" | — | 1 | High |
| 17 | Prompts carry ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL. | G8.I6 | Partial | ROLE (Librarian Builder mode) explicit. CONSTRAINT pervasive. AUTHORITY implicit (IL rule 12). FAILURE SIGNAL absent — no guidance for what consumers should observe if the skill fails or produces an incomplete draft. | G8 §Recovery | 1 | Medium |
| 18 | **G9.I6 — Destructive or irreversible actions require human approval.** | G9.I6 | **Partial** | `--target-path` write is gated on explicit `y` (Step 6: "Write only on explicit `y`. Default is inline-only"). This satisfies the spirit. However: (a) temp scratch file write (`/tmp/design-skill-draft-<timestamp>.md`) in Step 5 is ungated; (b) enforcement is model-prose-only, not structural. Temp write is low-blast-radius but the structural gap (G6.I2) is the same as in design-agent. | G9 §Recovery | 1 | Medium |
| 19 | Audit trail for all agent actions. | G9.I2 | Not addressed | No audit trail mechanism for writes (temp file, target-path file) or Task subagent invocations. | G9 §Recovery | 1 | Medium |
| 20 | No decision type defaults to full autonomy. | G9.I5 | Satisfied | Every decision requires designer input (Steps 1–7) or explicit approval gate (Step 6 write). No unchecked autonomous paths. | — | 1 | High |
| 21 | Comprehension maintained for shipped artifacts. | G9.I7 | Partial | Write-gate requires explicit approval + clean audit findings. Comprehension of the embedded audit report before approval is not explicitly required — the designer could approve the write without reading the `/assess-skill` output. | G9 §Recovery | 1 | Low |
| 22 | Generator-assessor separation (rule 10) encoded in procedure. | G5 / IL rule 10 | Satisfied | Step 5: "Do not inspect the draft against rubric criteria inside this skill's context. The epistemic gap rule 10 protects is exactly the boundary the fresh-context subagent invocation preserves." Rule is explicit and non-negotiable in the Boundaries section. | — | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | State tracking independent of conversation history. | G3b.I2 | Is the Decision record written to a file before the subagent invocation in Step 5, or does it live only in conversation context? If the session is interrupted, is the Decision record recoverable? | Description of persistence mechanism or acknowledgment that single-session assumption is intentional. |
| b | Safety-critical constraints enforced structurally. | G6.I2 | Is there a harness-level hook or permission restriction preventing writes to `--target-path` without the explicit `y` approval signal? | Hook configuration or explicit acknowledgment of the structural gap. |
| c | Audit trail for writes and Task invocations. | G9.I2 | Are write operations and Task (subagent) invocations logged in the IL system log or any external audit trail? | System-log reference or session-log entry pattern. |
| d | Comprehension gate before write approval. | G9.I7 | Is the designer required to acknowledge the `/assess-skill` audit findings before the write approval prompt is presented? Or can they skip to `y` without reading the report? | Procedure or UX description confirming audit findings are surfaced before the `y/N` prompt. |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G2a/G2b | No context directives or caching behavior specified — G2 Preconditions unsatisfied. |
| G7 | Single-session by design — G7 not triggered. |
| G10 | Task invocation is a single subagent delegation, not a multi-agent topology — G10 not load-bearing. |

---

### Summary

Classification: safety-critical (trigger: `allowed-tools` includes Write; Task spawns a subagent).

**G9.I6 outcome:** Partial — the `--target-path` write is gated on explicit `y`, satisfying the letter of the invariant. The temp-file write in Step 5 is ungated (low blast radius). Both gates are model-instruction-only; no structural enforcement exists (findings 12, 14).

**What the skill does well:** The design-skill SKILL.md is the structural sibling of design-agent, and shares its strengths: explicit Decision sequence walk, generator-assessor separation (rule 10 explicitly stated and enforced in Step 5), negative-constraint framing, and write-blocking on hard-gate audit failures. The safety-critical classification gate at Decision step 4 is correctly positioned as a hard gate before procedure drafting.

**Risks that remain:** The findings are near-identical to design-agent: (1) structural enforcement gap on write gate (G6.I2, G6.I4 — findings 12, 14); (2) no audit trail for writes/Task invocations (G9.I2 — finding 19); (3) no FAILURE SIGNAL property (G8.I6 — finding 17); (4) Decision record state is conversation-only (G3b.I2 — finding 5). Since design-agent and design-skill share the same architecture, these gaps should be addressed as a pair. No hard-blocking issues for the skill's core design-and-present function.

---

### Skill: `systems/improvement-loop/.claude/skills/detect-drift/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 5, fresh context, mode: in-context-rubric)*

## Audit — skill (detect-drift)

**mode: in-context-rubric**

**Artifact:** `systems/improvement-loop/.claude/skills/detect-drift/SKILL.md`
**Classification:** Safety-critical (trigger: `allowed-tools` includes Write and Bash).
**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — G9.I6 forced)
**Rubric size:** 22 file-verifiable invariants, 4 system-verifiable invariants, 0 latent

**DD-92 ContextSpec audit:** No `context:` block in frontmatter. DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Contract presence — all required spec fields present | G1.I1 | Satisfied | Skill includes objective (source-drift scanning), acceptance criteria (per-run report at specified path), stop rules (Rules 1–7, Failure Modes table), constraints (read-only invariant, no autonomous re-extraction), autonomy levels (Nick gates all re-extraction), and context supply plan (Paths table). | — | 1 | High |
| 2 | Templates filled completely — no TBD/TODO placeholders | G1.I2 | Satisfied | No placeholder fields observed in frontmatter or body. All required sections are populated. | — | 1 | High |
| 3 | Hard constraints have enforcement mechanisms outside the prompt layer | G1.I3 | Partial | Rule 1 states "The scan never modifies any artifact's frontmatter, body, pipeline_status, or any other state outside operations/drift-reports/." Rule 6 references procedural violation detection ("Abort the run; surface in next governance audit"). Enforcement is procedural prose + a governance-audit surface; no harness-level hook prevents writes outside the designated path. | G1 §Recovery | 1 | Medium |
| 4 | Acceptance criteria evaluable by a third party | G1.I4 | Satisfied | Acceptance criteria are concrete: drift report written to `operations/drift-reports/<YYYY-MM-DD>-source-drift.md`, specific frontmatter schema, closed-enum Recommendation field, per-section conditions. All verifiable without access to original authorial intent. | — | 1 | High |
| 5 | Stop rules include halt condition, escalation trigger, completion criterion | G1.I5 | Satisfied | Failure Modes table provides: halt conditions (argument validation errors, abort on out-of-scope write), escalation (surface in governance audit), completion criterion (report written + summary reported to user). | — | 1 | High |
| 6 | Planning is probabilistic; execution is deterministic. | G3b.I1 | Satisfied | Step 1 invokes a deterministic Python helper (`scan.py`) for all file enumeration and comparison logic. LLM judgment is confined to Step 2 (recommendation per hit) — explicitly bounded to a closed three-value enum. | — | 1 | High |
| 7 | Every workflow has explicit state tracking independent of conversation history. | G3b.I2 | Satisfied | The helper script writes to a JSON file at `/tmp/drift-scan-<date>.json`. State is external to conversation context and readable across steps. | — | 1 | High |
| 8 | Every iterative pattern has a termination condition. | G3b.I3 | Satisfied | Step 2 iterates over `drift_hits` from the JSON (bounded array). Step 3 constructs the report from the bounded set. No open-ended loops. | — | 1 | High |
| 9 | Degradation modes are defined before the system goes live. | G3b.I4 | Satisfied | Failure Modes table covers 8 specific failure scenarios with detection and recovery actions. | — | 1 | High |
| 10 | Cost controls in place before autonomous execution. | G3b.I6 | Satisfied | The skill is invoked on-demand (DD-96 §Why selects on-demand over periodic). No autonomous recurring execution. Write is confined to one report file. | — | 1 | High |
| 11 | Only tools needed for the current task are loaded into context. | G5.I4 | Partial | `allowed-tools: Bash Read Grep Glob Write`. Bash is needed to invoke `scan.py`. Read is needed to load the JSON and findings files. Write is needed for the report. Grep/Glob are needed to enumerate files if the script helper needs supplementation. However, Glob may be redundant if the Python script handles all enumeration — the procedure does not make explicit which steps use Glob vs. the script. | G5 §Recovery | 1 | Medium |
| 12 | Tool descriptions designed for non-deterministic consumers. | G5.I3 | Satisfied | The description frontmatter uses consumer-oriented phrasing that captures multiple valid invocation contexts ("After a large research-finding intake", "After /dimension-rebalance", "As a precondition to a planned /extract-artifacts run"). | — | 1 | High |
| 13 | Intermediate tool results stay outside context window when agent only needs final output. | G5.I5 | Satisfied | The Python helper writes JSON to a temp file; the skill reads the JSON path (not raw file lists) into context. This keeps intermediate enumeration data out of the LLM context. | — | 1 | High |
| 14 | Skills are framework-agnostic markdown files. | G5.I11 | Satisfied | Plain markdown; no SDK-specific dependencies. | — | 1 | High |
| 15 | Permissions tiered by risk, not binary allow/deny. | G6.I1 | Partial | The skill self-describes as "Read-only by contract" and confines writes to `operations/drift-reports/`. However, no explicit permission-tier table for the allowed tools (Bash, Write) is present. The read-only invariant is stated but not enforced structurally — the same Write tool that creates reports could write elsewhere. | G6 §Recovery | 1 | Medium |
| 16 | Safety-critical constraints enforced structurally, not via prompt alone. | G6.I2 | Violated | Rule 1 ("The scan never modifies any artifact outside operations/drift-reports/") is enforced only by prose instruction. The Failure Modes table says "Procedural violation — read-only invariant breached. Abort the run; surface in next governance audit." — this is a detect-after-violation response, not structural prevention. No harness hook or permission restriction prevents writes outside the designated path. | G6 §Recovery | 1 | High |
| 17 | Defense is layered — no single mechanism is sole protection. | G6.I4 | Violated | Read-only enforcement is a single layer (prose instruction). No second layer exists. | G6 §Recovery | 1 | High |
| 18 | Prompts tell the model what to produce, not how to think. | G8.I1 | Satisfied | Procedure steps specify outputs (JSON-loaded data, recommendation per hit, report structure) without prescribing CoT. | — | 1 | High |
| 19 | High-priority behavioral rules expressed as negative constraints. | G8.I3 | Satisfied | Rules are stated as negatives: "never modifies any artifact," "never invokes /extract-artifacts," "Does not invoke /identify-artifacts," "never overwritten across runs." | — | 1 | High |
| 20 | Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, and FAILURE SIGNAL properties. | G8.I6 | Partial | ROLE ("Codifier / Drift Detector" via Cognitive Disposition). CONSTRAINT is pervasive. AUTHORITY is implicit. FAILURE SIGNAL — what the consumer should observe if the skill fails — is absent. The Failure Modes table covers procedural failures but not failure signals to the consumer (e.g., "if the report is not present at the expected path, the skill failed"). | G8 §Recovery | 1 | Medium |
| 21 | **G9.I6 — Destructive or irreversible actions always require human approval.** | G9.I6 | **Satisfied** | The only write action (report creation at `operations/drift-reports/`) is not destructive — it is additive (per-run report accumulation, no overwrites on prior runs). Re-extraction (the irreversible-adjacent action) explicitly requires Nick's ruling on the report; the skill never auto-invokes `/extract-artifacts`. The `--auto` flag does not exist in this skill. | — | 1 | High |
| 22 | No decision type defaults to full autonomy without explicit classification. | G9.I5 | Satisfied | Every non-trivial decision (recommendation per hit, report write) is either bounded by the closed enum or produces a report for Nick's ruling. No unchecked autonomous decisions. | — | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | Safety-critical constraints enforced structurally. | G6.I2 | Is there a harness-level permission restriction or hook that prevents Bash and Write from accessing paths outside `systems/improvement-loop/operations/drift-reports/`? Or is the read-only constraint solely enforced by model instruction? | Hook or permission configuration entry; or explicit acknowledgment that structural enforcement is a known gap. |
| b | Defense is layered. | G6.I4 | What is the second layer of protection (beyond prose instruction) that prevents the skill from writing outside `operations/drift-reports/`? | Description of a harness hook, CI check, or filesystem permission that independently enforces the write scope. |
| c | Audit trail maintained for agent actions. | G9.I2 | Is the execution of `/detect-drift` (invocation, arguments, output file path) logged in the IL system log? | System-log entry pattern or session-log reference. |
| d | Glob tool use justified. | G5.I4 | Does the procedure actually use the Glob tool directly, or is all file enumeration performed by `scan.py`? If Glob is not used, it should be removed from `allowed-tools` to reduce the safety envelope. | Code review of `scan.py`; or explicit step that calls Glob. |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G2a/G2b | No context directives or caching behavior specified — G2 Preconditions unsatisfied. |
| G7 | Single-session, on-demand; no cross-session state management — G7 not triggered. |
| G9 (full, except G9.I6) | G9 Preconditions require "human oversight required" and "decision taxonomy for the domain." G9.I6 fires unconditionally as a safety-critical invariant; remaining G9 invariants are latent because the skill is not an autonomous agent system. |

---

### Summary

Classification: safety-critical (trigger: `allowed-tools` includes Write and Bash).

**G9.I6 outcome:** Satisfied — the only write is additive (dated report), not destructive; re-extraction (the consequential action) is explicitly gated on Nick's ruling and never invoked autonomously.

**What the skill does well:** The deterministic/LLM split (Python helper for enumeration, LLM for judgment) is exemplary G3b practice. The closed-enum Recommendation field prevents free-form ambiguity. The Failure Modes table is thorough. The read-only-by-contract identity is clearly stated and consistently referenced throughout. On-demand-only cadence (DD-96) respects the human-gate principle.

**Risks that remain:** (1) Read-only constraint is prose-enforced only — no structural protection against writes outside `operations/drift-reports/` (G6.I2, G6.I4 — findings 16, 17). This is the primary residual risk; severity depends on harness enforcement outside the skill. (2) Glob tool may be unused and could be removed from `allowed-tools` to reduce the safety envelope (G5.I4 — finding 11). (3) No explicit FAILURE SIGNAL property for consumers (G8.I6 — finding 20). These are addressable without redesign.

---

### Skill: `systems/improvement-loop/.claude/skills/dimension-rebalance/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 9, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** safety-critical (Edit; Step 5B calls Write)

**Critical:** F#3 Violated — `Write` called in Step 5B but absent from `allowed-tools`; will fail execution for the Type B (split) path which is the core use case.

**G9.I6 outcome:** Partial — Step 4 human gate present, but no per-operation confirmation for Type B splits after bulk approval.

**Top findings:**
- F#3 Violated G5.I4: `allowed-tools` missing `Write` despite procedure calling it.
- F#11 Missing G3b.I2: no workflow state checkpoint between approval and multi-split execution.
- F#1 Missing: no `## Output shape` section.
- F#2 Missing: no `## Boundary conditions` section.

---

### Skill: `systems/improvement-loop/.claude/skills/extract-artifacts/SKILL.md`
*Dispatched to bin 2 — **report MISSING**.*

Bin 2 emitted only 1 of N expected sentinel-delimited reports (format-compliance failure per `/audit-system` SKILL.md §FAILURE SIGNAL — individual-report-missing, not whole-bin-unparseable). Cause: subagent message-budget or instruction-following drift between dispatch payload and assessor invocation. Artifact unassessed in this run.

**Resolution:** invoke the IL `/assess-skill` (or `/assess-agent --variant prompt-based`) skill directly on this path, or re-audit via `/audit-system systems/improvement-loop/ --scope skills`.

---

### Skill: `systems/improvement-loop/.claude/skills/finding-crosslink/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 4, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** safety-critical (Edit)

**Critical:** **G9.I6 SATISFIED** — `--dry-run` default + explicit Step 5 Human Gate + YAML round-trip validation = three-layer defense. Strongest-governance skill in audit.

**G9.I6 outcome:** Satisfied — multiple layers, explicit named gate, dry-run default.

**Top findings:**
- F#1 Satisfied G9.I6: dry-run default + human gate + structural YAML guard.
- F#2 Missing: safety-critical declaration absent from boundary conditions.
- F#3 Missing: no `## Boundary conditions` section per template skeleton.
- F#20 Partial: framework coupling via `kb_parser.py` and generator scripts.

---

### Skill: `systems/improvement-loop/.claude/skills/identify-artifacts/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 2, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** safety-critical (Write, Agent)

**Critical:** G5.I2/I4 Violated — `allowed-tools` omits Edit but Step 7 needs Edit on finding frontmatter; runtime error path.

**G9.I6 outcome:** Partial — Step 4 identification report is the pre-gate artifact (intended), but Steps 6.a/6.b proposals and Step 7 priority back-annotation write without prior human approval.

**Top findings:**
- F#1 Violated: `allowed-tools` missing Edit; Step 7 requires it.
- F#5 Missing: no cost controls / Agent invocation caps for parallel Sonnet subagents.
- F#8 Partial: subagent prompt lacks AUTHORITY and FAILURE SIGNAL.
- F#12 Missing: no `version:` field; inter-skill contract with `/extract-artifacts` is unversioned.

---

### Skill: `systems/improvement-loop/.claude/skills/linkage-repair/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 8, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

mode: in-context-rubric (assess-skill SKILL.md loaded; rubric applied directly per procedure)

**Artifact:** `systems/improvement-loop/.claude/skills/linkage-repair/SKILL.md`
**Classification:** safety-critical (trigger: `allowed-tools` includes Edit)
**Composed guides:** G1 (spec quality), G3b (workflow/termination), G5 (tool use), G6 (safety/permissions), G8 (prompt/trigger quality), G9 (governance — G9.I6 forced for safety-critical)
**Rubric size:** 14 file-verifiable invariants, 6 system/process-verifiable invariants, 2 latent (out-of-scope)

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | G9.I6 — HITL gate for destructive actions | Destructive or irreversible actions always require human approval regardless of trust level. | G9 §Invariants | Satisfied | Step 6 "Human Gate: Present the report. Wait for approval before executing repairs." is explicit HITL before any Edit is invoked. | — | 1 | High |
| 2 | G1 — Spec completeness: objective/desired outcomes | Spec includes objective and desired outcomes | G1 §Invariants | Satisfied | "Audit and repair bidirectional links between research sources and findings in the Improvement Loop KB. Detects unlinked findings, orphaned sources, and broken references." — present in description and body. | — | 1 | High |
| 3 | G1 — Stop rules: halt condition | Stop rules include at least one halt condition | G1 §Invariants | Partial | `--dry-run` stops after Step 5 ("Stop here if `--dry-run` was specified") and Step 3 stops before Step 6 for dry-run. However there is no explicit abort/halt condition for the non-dry-run path if the script is unavailable or produces malformed JSON. The Pre-step says "fall back to manual procedure" but no halt criterion is defined for when that also fails. | Add an explicit halt condition: "If both the script-based and manual paths fail to produce the source/findings maps, abort and report to user before any Edit step." | 1 | Medium |
| 4 | G1 — Stop rules: escalation trigger | Stop rules include at least one escalation trigger | G1 §Invariants | Missing | No escalation trigger is specified. The skill has completion criteria (Step 8 summary) and a dry-run abort, but no point at which it explicitly says "pause and ask the user" outside of Step 6's approval gate. | Add an escalation trigger for medium-confidence matches: "If medium-confidence matches exceed N, ask the user whether to proceed before presenting the full report." | 1 | Medium |
| 5 | G1 — Acceptance criteria evaluable by third party | Acceptance criteria are evaluable by a third party without access to the prompter's intent | G1 §Invariants | Missing | No explicit acceptance criteria section. The skill has a "Calibration Notes" section with calibration heuristics but these are not framed as pass/fail acceptance criteria. A third party cannot determine when this skill has succeeded. | Add an "Acceptance Criteria" section: e.g., "All asymmetric links detected in Check C are either repaired or documented as requiring manual review." | 1 | High |
| 6 | G3b — Termination condition for iterative steps | Every iterative pattern has a termination condition (loop limit, stall detection, or both) | G3b §Invariants | Satisfied | Steps 1–4 iterate over source/finding maps. The iteration terminates on list exhaustion (implicit boundary: all files in Glob result processed). The Pre-step script alternative has no loop; the manual path iterates over fixed lists. Acceptable. | — | 1 | Medium |
| 7 | G3b — Explicit state tracking independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b §Invariants | Partial | The skill produces a structured report (Step 5) that persists state, but the report destination is described only in the markdown template — no explicit file path for the report is given. If the skill is interrupted after building maps but before producing the report, the state is lost. | Specify a report file path (e.g., `operations/research-reports/{date}-linkage-repair.md`) to make state externally persistent. | 1 | Medium |
| 8 | G5 — Only tools needed loaded | Only tools needed for the current task are loaded into context | G5 §Invariants | Satisfied | `allowed-tools: Read Grep Glob Edit` — the four tools used are the four declared. No over-grant. | — | 1 | High |
| 9 | G5 — Tool descriptions for non-deterministic consumers | Tool descriptions designed for non-deterministic consumers | G5 §Invariants | Satisfied | This is a SKILL.md, not a tool definition file. G5.I3 applies to tool definitions authored for agent use. The skill's own tool use instructions are concrete and step-bound. Not applicable in the strict tool-definition sense; no finding raised. | — | 1 | Low (applicability marginal) |
| 10 | G6 — Permissions tiered by risk | Permissions tiered by risk, not binary allow/deny | G6 §Invariants | Partial | The skill correctly separates Read/Grep/Glob (safe, read-only) from Edit (mutating). The `--dry-run` flag is an effective soft tier gate. However, there is no structural enforcement of the dry-run flag — the same Edit calls exist in the procedure unconditionally from Step 7 onward; dry-run is enforced by a prose "stop here" instruction, not by a structural gate (e.g., a separate dry-run vs. execute code path). | Consider restructuring so that Steps 6–7 are only reachable after explicit user approval, making the tiering structurally enforced rather than prose-enforced. | 1 | Medium |
| 11 | G6 — Defense is layered | Defense is layered — no single mechanism is sole protection | G6 §Invariants | Partial | The HITL gate (Step 6) is the sole protective layer. There is no dry-run-mode structural enforcement, no preview-before-edit pattern beyond the report, and no rollback guidance. If the user accidentally approves all repairs, there is no undo path documented. | Add a "Safety" note: "Edit operations modify living KB files. Recommended: run with `--dry-run` first. If repairs are applied in error, use git to revert `research-sources/` and `research-findings/` changes." | 1 | Medium |
| 12 | G8 — Trigger description quality | Description phrases the trigger the way a consumer would ask; skill triggers reliably | G8 §Invariants (description as UX trigger) | Satisfied | Description is concrete and invocation-condition-aligned: "Audit and repair bidirectional links… Use after bulk extraction, backfill sessions, or when the source quality audit flags linkage gaps." Trigger conditions named explicitly in "When to Use." | — | 1 | High |
| 13 | G8 — ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | G8 §Invariants | Partial | The skill body provides implicit role framing ("Calibration Notes" contains constraint-like guidance). However no explicit ROLE, AUTHORITY, CONSTRAINT, or FAILURE SIGNAL declarations are present as structural sections. The "Calibration Notes" section functions as constraint/boundary material but is not labeled as such. This is partial compliance — the constraints exist but are not explicitly surfaced as prompt policy properties. | Low-impact finding; the skill functions but formal audit of prompt-policy properties finds them informal. | 1 | Medium |
| 14 | DD-92 ContextSpec | `context:` block absent | DD-92 | N/A (skipped) | No `context:` block in frontmatter. DD-92 ContextSpec audit skipped — DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here. | — | — | — |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|------------------|
| a | Degradation modes defined before go-live | G3b §Invariants | If the `linkage_analyzer.py` script is unavailable (missing, broken, wrong Python env), is the manual fallback procedure tested and known to work on the current KB size? | Evidence: manual-path test run on a subset of the KB; documented fallback path |
| b | Cost controls in place before autonomous execution | G3b §Invariants | For large KBs (hundreds of sources + findings), has the skill been tested for context-window budget? The manual path reads every source and finding file individually. | Evidence: session transcript or benchmark showing the skill completes under context budget for current KB size |
| c | Safety-critical constraints enforced structurally | G6 §Invariants | Is the dry-run flag enforced structurally (i.e., the agent cannot accidentally invoke Edit when `--dry-run` is set), or is enforcement purely prose-based ("Stop here if `--dry-run`")? | Evidence: harness configuration or arg-parsing logic that gates Edit tool use behind flag state |
| d | Agent cannot modify its own permission configuration | G6 §Invariants | Is this skill invoked with a tool allowlist that limits Edit to KB paths only (not to skill files, governance docs, etc.)? | Evidence: harness settings.json showing path-scoped permissions for this skill's invocation context |
| e | Audit trail maintained for all agent actions | G9 §Invariants | Are the Edit operations performed by this skill logged (e.g., via git commit, system log entry) so that repairs can be audited after the fact? | Evidence: git history or SL entry created after repair session |
| f | Prompt changes versioned and tested | G8 §Invariants | Is there a version record for this skill? The skill has no `version` frontmatter field and no changelog. Changes to the procedure (e.g., new confidence tiers, new check types) are undetectable from the artifact alone. | Evidence: git history entry or version field added to frontmatter |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G9 (beyond I6) | G9 Preconditions require a decision taxonomy and per-decision-type autonomy configuration. This skill is a single-purpose KB maintenance operation, not a multi-decision-type agent system. G9.I6 fires unconditionally as safety-critical; remaining G9 invariants are latent. |
| G5 tool-definition sub-invariants (I6–I12) | These apply to tool *definitions* authored for agent consumption, not to a skill that *uses* tools. The skill's tool use (Read/Grep/Glob/Edit) is sufficiently described in the procedure steps. |

---

### Summary

G9.I6: **Satisfied.** The HITL gate at Step 6 is explicit and positioned before all Edit calls. This skill is deployable from a destructive-action governance perspective.

Load-bearing issues to fix before treating this skill as production-complete:
1. **Missing acceptance criteria** (finding #5, High confidence) — without them, success is not third-party verifiable.
2. **Defense layering** (finding #11) — the HITL gate is the only protective layer; a rollback/undo note and a structural dry-run gate would provide defense in depth.
3. **Incomplete stop rules** (finding #3, #4) — no halt condition for tool/script failure, no escalation trigger for medium-confidence match overflow.

State persistence (finding #7) is a medium-priority improvement: naming the report output path makes interrupted sessions recoverable.

Prompt-policy properties (finding #13) are a low-priority polish item.

No DD-92 ContextSpec findings — `context:` block absent; check not applicable at this stage.

---

### Skill: `systems/improvement-loop/.claude/skills/maintain-docs/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 7, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

**mode: in-context-rubric** (assess-skill SKILL.md loaded; rubric applied directly)

**Classification: safety-critical (trigger: allowed-tools includes Write and Edit)**

**Artifact:** `systems/improvement-loop/.claude/skills/maintain-docs/SKILL.md`
**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — safety-critical; G9.I6 forced)
**Rubric size:** 17 file-verifiable invariants, 4 system/process-verifiable invariants, 0 latent

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Spec completeness | Every spec includes objective, desired outcomes, health metrics, constraints, autonomy levels, acceptance criteria, stop rules, context supply plan | G1.I1 | Partial | Two complete procedure branches (Update/Create) are fully specified with steps. Rules section covers autonomy tiers. No health metrics, no explicit acceptance criteria, no stop rules (halt/escalation/completion). "Calibration Notes" is informal guidance | G1 §Recovery | 1 | High |
| 2 | Hard constraints have enforcement outside prompt layer | Hard constraints must have enforcement mechanisms outside prompt layer | G1.I2 | Partial | Rule 6 ("Cross-system docs are out of scope") is a hard constraint stated in prose. No structural enforcement restricts Write/Edit to the IL system path — a model could write to `meta-system/` without structural interception. Rule 4 ("Don't rewrite docs for style") similarly relies on prose compliance | G1 §Recovery | 1 | High |
| 3 | Acceptance criteria evaluable by third party | Acceptance criteria evaluable by third party | G1.I3 | Missing | No acceptance criteria. Success is described by output reports (Step 6: "Fixes applied," "Gaps flagged"), but these are output descriptions, not pass/fail criteria. A third party cannot determine from the skill whether a given run's output constitutes a successful update | G1 §Recovery | 1 | High |
| 4 | Stop rules: halt + escalation + completion | Stop rules include halt, escalation trigger, completion criterion | G1.I4 | Partial | Completion criterion implicit from Step 6 report (update mode) and Step 5 write (create mode). Halt condition: absent — what happens if `Glob` returns no files in a system that should have many? No escalation trigger — what triggers escalation to Nick beyond the "propose" language in Step 5? | G1 §Recovery | 1 | Medium |
| 5 | Explicit state tracking independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b.I1 | Partial | Update mode: Drift Report (Step 4) is the state artifact. Create mode: no intermediate state before final Write (Step 5). If a multi-document create run is interrupted, there is no partial-state recovery path | G3b §Recovery | 1 | Medium |
| 6 | Iterative pattern has termination condition | Every iterative pattern has a termination condition | G3b.I2 | Satisfied | Update mode's iteration over surfaces (Step 1 table) is bounded by a fixed list of five surface types. Create mode iterates over identified gaps — bounded by the CLAUDE.md and index file reads (finite). No unbounded loops | G3b §Recovery | 1 | High |
| 7 | Degradation modes defined | Degradation modes defined before going live | G3b.I3 | Partial | Update mode Step 5 defines one degradation: "Flag broken paths if referenced artifact is missing (not just renamed)." No degradation for: Write failures in create mode, Glob returning unexpected zero results, Edit failing mid-update on a multi-section document | G3b §Recovery | 1 | Medium |
| 8 | Only tools needed loaded | Only tools needed for the current task | G5.I1 | Satisfied | `Read`, `Grep`, `Glob`, `Write`, `Edit` — all five are in the "Available Tools" table with explicit purpose. No extraneous tools. The split between `Write` (create new files) and `Edit` (update existing) is correctly specified | G5 §Recovery | 1 | High |
| 9 | Tool descriptions designed for non-deterministic consumers | Tool descriptions persuade, disambiguate, explain when not to use | G5.I2 | Satisfied | Available Tools table maps each tool to a concrete purpose. Write vs. Edit disambiguation is present and captures the "preserve git history" rationale for using Edit on existing files | G5 §Recovery | 1 | High |
| 10 | Tool interface makes common errors structurally impossible | Poka-yoke tool interface design | G5.I3 | Partial | Write vs. Edit split is a form of poka-yoke (prevents accidental clobber of existing files). However the constraint "cross-system docs are out of scope" (Rule 6) has no structural poka-yoke — Write/Edit could be called on `meta-system/` paths without the tool blocking it | G5 §Recovery | 1 | Medium |
| 11 | Permissions tiered by risk | Permissions tiered by risk, not binary | G6.I1 | Partial | Rules 1 and 2 distinguish Guarded tier (update mode, factual fixes) from Proposal-First tier (create mode, new docs). This is an explicit risk-tier distinction. However within Guarded-tier, Write and Edit are not further differentiated by risk — both are treated as equivalent in the tool listing | G6 §Recovery | 1 | Medium |
| 12 | Safety-critical constraints enforced structurally | Safety-critical constraints enforced structurally | G6.I2 | Partial | Two tiers of human gating are defined: Guarded (act-then-report) for updates, Proposal-First (draft-then-approve) for new docs. Create mode Step 4 ("Present for Review… Wait for approval before writing") is a structural gate on the highest-risk operation (creating new docs). Update mode's Guarded tier relies on prose compliance alone for factual fixes | G6 §Recovery | 1 | Medium |
| 13 | Agent cannot modify its own permission configuration | G6.I3 | Satisfied | The skill does not write to harness configuration, allowed-tools declarations, or governance tier assignments | G6 §Recovery | 1 | High |
| 14 | Destructive/irreversible actions require human approval | G9.I6: destructive or irreversible actions always require human approval | G9.I6 | Partial | Create mode has explicit human approval gate (Step 4: "Proposal-First tier — structural documentation shapes how agents understand the system. Wait for approval before writing"). Update mode applies factual fixes without pre-approval ("Act then report"). The boundary between "factual fix" (Guarded) and "structural description rewrite" (requires proposing) is defined in Step 5 but left to model judgment to apply. This boundary is the G9.I6 risk — a model may misclassify a structural change as a factual fix and apply it without a gate | G9 §Recovery | 1 | High |
| 15 | Trigger description fires reliably | Description fires reliably on intended use cases | G8.I1 | Satisfied | Description names two modes explicitly (update/create). "When to Use" section names five concrete trigger conditions. "When NOT to Use" provides four clear exclusions. The `argument-hint` (`--update | --create [target]`) disambiguates invocation | G8 §Recovery | 1 | High |
| 16 | Prompt carries explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | G8.I2 | Partial | ROLE (Owner, system steward) is explicit. CONSTRAINTS (Rules 1-6) are explicit and well-formed. AUTHORITY is implied (DD-86 Owner responsibility) but not formally declared in the skill text. FAILURE SIGNAL is absent — no statement of what invalid documentation output looks like | G8 §Recovery | 1 | Medium |
| 17 | High-priority behavioral rules as negative constraints | G8.I3 | Satisfied | Rules use negative form for load-bearing constraints: "Never fabricate system state," "Don't rewrite docs for style," "Cross-system docs are out of scope" | G8 §Recovery | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|---|---|---|---|
| a | Write path restricted to system-scoped paths | G6.I2 / G1.I2 | Is there any harness-level restriction (settings.json, permission config) that prevents Write/Edit from targeting `meta-system/` paths? Rule 6 bans cross-system writes in prose; is there structural enforcement? | settings.json `permissions` config; harness write-path restriction |
| b | Factual vs. structural boundary calibrated | G9.I6 | Has the "factual fix" vs. "structural description" boundary (Step 5) been tested against real drift scenarios? Is there a set of examples that anchors which changes require proposing? | Worked examples in skill or design note |
| c | Audit trail for update-mode writes | G9 governance | Update-mode writes occur without pre-approval. Are these captured in git history with sufficient granularity (per-file commits, not bulk commits) to reconstruct what changed in a run? | Git commit convention; hook config |
| d | Nick-authored docs — preservation of voice | G1 governance (spec retained alongside output) | Rule 5 says "some docs are authored by Nick — update factual details but don't change voice." Is there a documented list of Nick-authored docs, or does this rely entirely on the model recognizing authorship from prose style? | Authorship registry or frontmatter `author: "nick"` convention |

---

### Aspects out of scope

| Guide | Why latent |
|---|---|
| G2a/G2b | Skill does not embed context directives in its prompt — G2a/G2b Preconditions unsatisfied |

---

### DD-92 ContextSpec audit

DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

---

### Summary

**G9.I6 outcome: Partial — the factual/structural boundary in update mode is the load-bearing risk.** Create mode correctly gates new doc writes on human pre-approval. Update mode intentionally applies factual fixes without pre-approval (Guarded tier), which is a sound design choice for low-risk corrections. The risk is that the boundary between "factual fix" and "structural description rewrite" is defined by prose guidance and model judgment, not a structural check — a sufficiently large diff could slip through as "factual." The fix is to add an explicit size/scope heuristic to Step 5 (e.g., "if more than N lines change in a single section, propose rather than apply"). Additionally: acceptance criteria are absent (G1.I3), stop rules are incomplete (G1.I4), and FAILURE SIGNAL is undefined (G8.I2 Partial). Rule 6's cross-system write prohibition lacks structural enforcement (G6.I2 Partial, G1.I2 Partial).

---

### Skill: `systems/improvement-loop/.claude/skills/perplexity-research/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 6, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

**mode: in-context-rubric**
**Artifact:** `systems/improvement-loop/.claude/skills/perplexity-research/SKILL.md`
**Classification: safety-critical (trigger: allowed-tools includes Write; procedure writes reports to `operations/research-reports/`).**

**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger description), G9 (governance — safety-critical forced)
**Rubric size:** 16 file-verifiable invariants, 8 system/process-verifiable invariants, 0 latent

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Spec completeness — stop rules | G1.I5: stop rules include halt condition, escalation trigger, completion criterion | G1 §Invariants | Missing | No "Boundary Conditions" section. No explicit halt, escalation, or completion criterion stated anywhere in the skill body. | G1 §Recovery: review spec for missing stop-rule types | 1 | High |
| 2 | Spec completeness — acceptance criteria | G1.I4: acceptance criteria evaluable by third party | G1 §Invariants | Missing | No acceptance criteria stated. The "Rules" section states behavioral invariants but not a testable completion signal. | G1 §Recovery | 1 | High |
| 3 | Spec completeness — context supply plan | G1.I1: spec includes context supply plan when context gap exists | G1 §Invariants | Partial | The skill reads existing KB findings in Step 2 of each mode, but no explicit context supply plan is declared as a section. The reading steps are embedded in procedure prose rather than a named context-supply declaration. | G1 §Recovery | 1 | Medium |
| 4 | Spec completeness — autonomy levels per decision type | G1.I1: autonomy levels per decision type | G1 §Invariants | Missing | No autonomy table or autonomy classification. The skill describes a "Research Intelligence Analyst" persona but does not classify decisions (e.g., report write, KB dedup, query crafting) by autonomy level or blast radius. | G1 §Recovery | 1 | High |
| 5 | Workflow state tracking | G3b.I2: explicit state tracking independent of conversation history | G3b §Invariants | Missing | No state tracking mechanism defined. The skill relies on procedure step ordering within a single conversational turn; no checkpoint or re-entrant state is described. | G3b §Recovery: implement workflow state separation | 1 | Medium |
| 6 | Termination condition | G3b.I3: every iterative pattern has termination condition | G3b §Invariants | Partial | Mode 1 Step 4 describes optional follow-up queries (iterative) but names no termination condition. "Do not combine discover and compare in a single run" (Rule 8) is a scope limit but not a loop-termination invariant for the follow-up query cycle. | G3b §Recovery | 1 | Medium |
| 7 | Tool loading discipline | G5.I4: only tools needed for current task loaded into context | G5 §Invariants | Partial | `allowed-tools` lists all Perplexity MCP tools (`perplexity_research`, `perplexity_reason`, `perplexity_search`, `perplexity_ask`) plus Read/Grep/Glob/Write/Agent. The "Calibration Notes" section explains when each Perplexity tool is preferred, but no per-mode restriction is enforced — all tools are loaded regardless of whether `--discover` or `--compare` is active. Both modes use the same full tool surface. | G5 §Recovery: implement deferred loading | 1 | Medium |
| 8 | Tool descriptions for non-deterministic consumers | G5.I3: tool descriptions designed to persuade, disambiguate, explain when not to use | G5 §Invariants | Satisfied | The "Available Tools" table and "Calibration Notes" section clearly explain preferred usage for each Perplexity tool, including when to prefer each and when not to rely on it as primary. | — | 1 | High |
| 9 | HITL gate for destructive action | G9.I6: destructive or irreversible actions always require human approval | G9 §Invariants | Violated | Write to `operations/research-reports/` is a side effect the skill performs autonomously. Rule 3 states "Reports are standalone artifacts. No side effects on KB entries" — but the report write itself is a side effect on the file system performed without explicit user approval step. No confirm-before-write or dry-run mode is offered. The skill does explicitly forbid KB modification, which partially mitigates blast radius, but the file write itself is unchecked. | G9 §Recovery: add approval gate or dry-run mode for file writes | 1 | High |
| 10 | Prompt: ROLE/AUTHORITY/CONSTRAINT/FAILURE SIGNAL | G8.I6: prompts carry ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | G8 §Invariants | Partial | "Cognitive Disposition" section establishes ROLE (Research Intelligence Analyst). CONSTRAINT is present in the Rules section. AUTHORITY and FAILURE SIGNAL are not explicitly declared in the system-prompt schema. The `perplexity_research` system message fragments provide partial context, but there is no named FAILURE SIGNAL (what happens when Perplexity returns thin results is addressed in Rule 9 as a prose instruction, not a structured property). | G8 §Recovery | 1 | Medium |
| 11 | Prompt: negative constraints for high-priority rules | G8.I3: high-priority rules expressed as negative constraints | G8 §Invariants | Satisfied | Rules 1, 3, 7, 8 are framed as explicit prohibitions ("Never create findings or sources", "Do not include KB content in Perplexity queries"). | — | 1 | High |
| 12 | Trigger description quality | G8 (description must trigger reliably) | G8 §Invariants | Satisfied | Description uses consumer phrasing: "Use when you want to explore a topic deeply via web-grounded research, or validate the KB's coverage." The `argument-hint` is explicit. "When to Use" section names concrete invocation contexts. | — | 1 | High |
| 13 | Hard constraints via structural enforcement | G6.I2: safety-critical constraints enforced structurally, not prompt-only | G6 §Invariants | Violated | The prohibition on KB modification (Rules 1, 3) is enforced by prose instruction only. No structural enforcement (no tool restriction to read-only, no hook). The skill has `Write` in allowed-tools but the prohibition on writing to KB is trust-the-prompt. | G6 §Recovery | 1 | High |
| 14 | Defense in layers | G6.I4: defense is layered | G6 §Invariants | Violated | Related to #13: the sole safeguard against KB writes is the prose "Rules" section. No second layer (tool restriction, harness hook, path guard) is present. | G6 §Recovery | 1 | Medium |
| 15 | DD-92 ContextSpec | DD-92 ContextSpec audit | DD-92 | Skipped | DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here. | — | — | — |
| 16 | Output shape described | G1.I1: spec includes output shape | G1 §Invariants | Satisfied | Both modes include explicit report templates (Discovery Report Template, Comparison Report Template) with named file paths and section structure. | — | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | G3b.I4: degradation modes defined before go-live | G3b §Invariants | Rule 9 mentions "If Perplexity returns thin results, say so" — is this the complete degradation specification? What happens if Perplexity MCP is unavailable, rate-limited, or returns an error mid-mode? | Degradation paths for MCP failure, timeout, and empty-response documented in skill or harness config |
| b | G3b.I6: cost controls in place before autonomous execution | G3b §Invariants | `perplexity_research` is described as "slow (30s+), thorough." Is there a per-invocation token budget or latency gate? | Documented per-invocation budget or harness-level cost guard |
| c | G5.I7: shared skills versioned and locked | G5 §Invariants | Is the `perplexity-research` skill versioned? Is there a lock file or version pin? | Lock file or version manifest in `.claude/skills/` |
| d | G6.I1: permissions tiered by risk, not binary | G6 §Invariants | Is there a risk classification for the `Write` permission in this skill's deployment context? Is it classified as mutating? | Permission tier registry or harness settings.json entry for this skill |
| e | G8.I7: prompt changes versioned and tested | G8 §Invariants | Are changes to the `perplexity_research` system message fragments version-controlled and tested against acceptance criteria? | Commit history or test harness records |
| f | G9.I6 (partial mitigation): human approval for report writes | G9 §Invariants | Is the report write surfaced to the user before execution, or is it silent? If silent, is a dry-run mode or explicit approval step planned? | Skill update or harness hook adding user confirmation before Write |
| g | G1.I3: hard constraints have enforcement outside prompt layer | G1 §Invariants | The prohibition on KB writes is prompt-only. Is there a harness-level tool restriction or path guard that prevents the `Write` tool from targeting `research-findings/`? | Harness settings.json path restriction or tool-intercept hook |
| h | G3b.I2: workflow state persists across session interruption | G3b §Invariants | If the skill is interrupted mid-mode (after Step 3, before Step 6 write), is the partial research recoverable? | Checkpoint mechanism or documented abort/resume path |

---

### Aspects out of scope

| Guide | Why latent |
|-------|-----------|
| G1 Precondition: "non-trivial autonomous work (3+ tool calls)" | Satisfied — skill uses multiple Perplexity calls plus Read/Grep/Write. G1 fires fully. |
| G3b Precondition: "side effects or longer than single turn" | Satisfied — Write tool is a side effect. G3b fires fully. |
| G9 Precondition: "destructive or irreversible action" | Satisfied — file Write is a side effect. G9.I6 fires. |

---

### Summary

G9.I6 outcome: **Violated.** The skill writes report files autonomously without a human approval gate or dry-run mode. This is the load-bearing finding for deployment readiness — the skill is safety-critical by the Write-in-allowed-tools trigger and the file-write procedure, but no HITL gating is present for the write action.

Additional load-bearing gaps: missing stop rules (G1.I5), missing acceptance criteria (G1.I4), missing autonomy classification (G1.I1), and KB-write prohibition enforced by prompt-only rather than structurally (G6.I2, G6.I4). The trigger description and negative-constraint framing of rules are the strongest elements of the skill. The skill should add a Boundary Conditions section with explicit success/abort/halt criteria, add a user-confirmation step before the Write action, and either structurally restrict the Write tool to the `operations/research-reports/` path or document that restriction as a harness-level enforcement.

---

### Skill: `systems/improvement-loop/.claude/skills/process-feedback/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 8, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

mode: in-context-rubric (assess-skill SKILL.md loaded; rubric applied directly per procedure)

**Artifact:** `systems/improvement-loop/.claude/skills/process-feedback/SKILL.md`
**Classification:** safety-critical (triggers: `allowed-tools` includes Write and Edit — Write creates triage reports; Edit updates feedback item frontmatter)
**Composed guides:** G1 (spec quality), G3b (workflow/termination), G5 (tool use), G6 (safety/permissions), G8 (prompt/trigger quality), G9 (governance — G9.I6 forced for safety-critical)
**Rubric size:** 13 file-verifiable invariants, 5 system/process-verifiable invariants, 1 latent (out-of-scope)

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | G9.I6 — HITL gate for destructive actions | Destructive or irreversible actions always require human approval regardless of trust level. | G9 §Invariants | Partial | The skill's "Rules" section explicitly scopes to "Guarded" tier: "Apply fixes only for items clearly within Guarded tier (stale references, doc updates)." Rule 1 states: "Autonomy tier: Guarded. Investigate and report. Apply fixes only for items clearly within Guarded tier." This is a meaningful constraint. However, the procedure (Step 7) specifies using Edit to update feedback item frontmatter (`triage_status`, `triage_date`, `triage_action`) as part of normal execution — not as an optional step. No human approval gate is required before these Edit calls. The Edit operations are low-blast-radius (frontmatter metadata on feedback items), but they are still mutations executed without a gate. Step 6 writes the triage report (Write) also without a gate. The partial rating reflects that the autonomy constraint is well-designed but the Edit gate is missing for the frontmatter updates. | Add an explicit prompt: "Before updating feedback item frontmatter (Step 7), confirm with user: 'Ready to mark N items as processed — proceed?'" This is low-friction given the low blast radius but would satisfy G9.I6. | 1 | Medium |
| 2 | G1 — Spec completeness: objective, constraints, stop rules | Spec includes objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels, stop rules | G1 §Invariants | Satisfied | The skill has: clear objective (feedback triage), outcome (triage report with proposed actions), autonomy tier classification (Guarded/Proposal-First/Human-Required taxonomy in Step 4), constraints (Rules section with 6 explicit constraints). Strong spec structure. | — | 1 | High |
| 3 | G1 — Stop rules: halt condition | Stop rules include at least one halt condition | G1 §Invariants | Satisfied | Rule: "If a feedback item needs a DD, say so in the report. DD creation is Human-Required." The skill explicitly halts (defers to human) for architectural decisions. Implicit halt: "Empty `feedback/` is a valid state — it means no feedback has been filed. Report that and exit." | — | 1 | High |
| 4 | G1 — Stop rules: escalation trigger | Stop rules include at least one escalation trigger | G1 §Invariants | Satisfied | Rule 5: "If feedback references other systems, flag for human routing." Step 4 taxonomy includes "Human-Required" tier with examples (DD creation, cross-system change). | — | 1 | High |
| 5 | G1 — Acceptance criteria evaluable by third party | Acceptance criteria are evaluable by a third party without access to the prompter's intent | G1 §Invariants | Missing | No explicit acceptance criteria. The report template (Step 6) and the frontmatter update (Step 7) together imply success, but no pass/fail acceptance criteria section exists. A third party cannot determine whether the skill succeeded without the original author's intent. | Add: "Success: triage report written or reported, all feedback items have triage_status updated, Systemic Patterns section contains at least one entry if N > 3 items." | 1 | Medium |
| 6 | G3b — Termination condition for iterative steps | Every iterative pattern has a termination condition | G3b §Invariants | Satisfied | Steps 1–3 iterate over feedback items (finite list from Glob). Step 3 processes items "prioritized by blast radius x urgency" — finite list, terminates on exhaustion. | — | 1 | High |
| 7 | G3b — Explicit state tracking independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b §Invariants | Partial | The triage report (Step 6) can be written to `operations/feedback-triage-reports/{date}-triage.md` — but this is presented as optional ("for formal processing"). The default is "Write the report to conversation." Conversation-only reporting provides no state persistence if the session ends. | Make the file write non-optional, or explicitly specify that conversation-reporting is only for `--quick` mode. | 1 | Medium |
| 8 | G5 — Minimal tool surface | Only tools needed for the current task are loaded | G5 §Invariants | Satisfied | `allowed-tools: Read Grep Glob Write Edit` — all five are used as described in the "Available Tools" table. No over-grant. | — | 1 | High |
| 9 | G5 — Tool definitions data-first | Tool definitions are data first — metadata exists before implementation | G5 §Invariants | Satisfied | The "Available Tools" table explicitly lists each tool with its purpose — a clear tool manifest. | — | 1 | High |
| 10 | G6 — Permissions tiered by risk | Permissions tiered by risk, not binary allow/deny | G6 §Invariants | Satisfied | The autonomy tier taxonomy in Step 4 directly maps to risk levels: Full Autonomy → read-only; Guarded → reference fixes; Proposal-First → structural changes; Human-Required → DDs. This is a well-designed permission tier system. | — | 1 | High |
| 11 | G6 — Safety-critical constraints enforced structurally | Safety-critical constraints enforced structurally, not via prompt instructions alone | G6 §Invariants | Partial | The autonomy tier constraints are enforced via prose rules ("Don't create DDs. If a feedback item needs a DD, say so in the report.") rather than structural enforcement. There is no harness-level gate preventing DD creation — only the skill's own prose instruction. This is a common limitation of SKILL.md-based enforcement. | Flag as system-verifiable: "Is there a structural gate (e.g., harness rule) that prevents this skill from invoking DD-creation commands?" | 1 | Medium |
| 12 | G8 — Trigger description quality | Description phrases the trigger the way a consumer would ask | G8 §Invariants | Satisfied | Description is consumer-phrasing-aligned: "Read the feedback/ folder, triage items by blast radius and urgency, investigate root causes, and propose actions." "When to Use" and "When NOT to Use" sections are exemplary boundary marking. | — | 1 | High |
| 13 | G8 — ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | G8 §Invariants | Partial | Explicit ROLE: "You are the Owner — investigating problems with analytical rigor" — present and well-framed. Constraints: present in Rules section (6 rules). AUTHORITY and FAILURE SIGNAL: not explicitly labeled. The "Cognitive Disposition" section functions as authority framing but is not labeled as such. | Low-priority polish: formally label AUTHORITY ("Owner agent, DD-86 scope") and FAILURE SIGNAL ("If a feedback item can't be root-caused, flag it with confidence=Low in the report"). | 1 | Low |
| 14 | DD-92 ContextSpec | `context:` block absent | DD-92 | N/A (skipped) | No `context:` block in frontmatter. DD-92 ContextSpec audit skipped — DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here. | — | — | — |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|------------------|
| a | Safety-critical constraints enforced structurally | G6 §Invariants | Is there a harness-level constraint preventing this skill from creating DDs or modifying cross-system files, beyond the prose rule? | Evidence: harness settings.json path restrictions; or confirmation that IL scope boundary is enforced at the tool level |
| b | Degradation modes defined before go-live | G3b §Invariants | If the `feedback/` directory is empty on first invocation, the skill says "Report that and exit" — is this behavior tested? | Evidence: test invocation on empty feedback/ |
| c | Audit trail for agent actions | G9 §Invariants | Are the Edit operations on feedback items logged in the system log? Is there a SL entry pattern for "feedback triage run"? | Evidence: SL entry from a prior process-feedback run |
| d | State persistence across interruptions | G3b §Invariants | If the skill is interrupted after Step 6 (report written) but before Step 7 (frontmatter updated), feedback items will be triaged but not marked as processed. Is re-run idempotent? | Evidence: behavior tested when items already have triage_status set |
| e | Prevention outputs tracked | (Skill-internal) | The skill's highest-value output is the "Prevention" field per feedback item. Is there a downstream process that converts "can a linter/hook prevent this class?" answers into actual IB items? Without it, prevention insights accumulate in reports but don't flow to implementation. | Evidence: IB item creation pattern or SL reference to feedback-prevention follow-ups |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G9 (beyond I6) | G9 broader invariants apply to multi-decision-type agent systems with trust ledgers. This is a bounded triage skill with a well-defined autonomy taxonomy. G9.I6 fires for the Edit operations; remaining G9 invariants are latent. |

---

### Summary

G9.I6: **Partial.** The Edit operations on feedback item frontmatter (Step 7) execute without an explicit human approval gate. This is a low-blast-radius mutation (triage metadata only, no KB content changes), and the skill's autonomy taxonomy (finding #10) is excellent. However, strictest G9.I6 compliance requires a gate. A simple confirmation prompt before Step 7 would close this gap without meaningful friction.

This is otherwise a well-structured skill. The "When NOT to Use" and "Cognitive Disposition" sections are exemplary. The autonomy tier taxonomy in Step 4 is the strongest governance design of the five audited skills.

Findings worth addressing:
- Finding #5: Missing acceptance criteria (medium confidence — adds audit verifiability).
- Finding #7: Triage report state is conversation-only by default — sessions that end without explicit file write lose state.

No DD-92 ContextSpec findings — `context:` block absent; check not applicable.

---

### Skill: `systems/improvement-loop/.claude/skills/promote-findings/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 5, fresh context, mode: in-context-rubric)*

## Audit — skill (promote-findings)

**mode: in-context-rubric**

**Artifact:** `systems/improvement-loop/.claude/skills/promote-findings/SKILL.md`
**Classification:** Safety-critical (trigger: `allowed-tools` includes Write and Edit; procedure performs KB writes and analysis-doc edits that directly modify the IL knowledge base).
**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — G9.I6 forced)
**Rubric size:** 22 file-verifiable invariants, 4 system-verifiable invariants, 0 latent

**DD-92 ContextSpec audit:** No `context:` block in frontmatter. DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Contract presence — all required spec fields present | G1.I1 | Partial | Objective (promote findings candidates into KB) is present. Acceptance criteria are implicit but not stated as explicit pass/fail conditions. Stop rules: no explicit halt condition (e.g., what stops the skill if the research-findings directory is unreadable). Escalation path absent. Autonomy level is provided via the candidate-selection gate (Step 3) and `--auto` flag documentation. Context supply plan: Paths table present. The missing explicit acceptance criteria and stop-rule set is a gap. | G1 §Recovery | 1 | Medium |
| 2 | Templates filled completely — no TBD/TODO placeholders | G1.I2 | Satisfied | No placeholder fields in frontmatter or body. Schema reference, body structure template, and triage rules are all populated. | — | 1 | High |
| 3 | Hard constraints enforced outside prompt layer | G1.I3 | Violated | Rule 1 ("Never auto-promote without `--auto` flag") and Rule 6 ("Do not modify existing findings without user approval") are prose-only constraints. No harness-level enforcement prevents Write/Edit from executing without user approval. The `--auto` flag bypasses the user-selection gate entirely, and only a prose instruction gates it ("Use only when the user has pre-reviewed"). | G1 §Recovery | 1 | High |
| 4 | Acceptance criteria evaluable by third party | G1.I4 | Partial | "How many candidates were promoted" is evaluable. "Every promoted finding links back to its source analysis doc" (Rule 5) is evaluable. However, no formal acceptance criteria statement; criteria are scattered across Rules and Procedure sections rather than consolidated. | G1 §Recovery | 1 | Medium |
| 5 | Stop rules include halt, escalation, completion | G1.I5 | Violated | No explicit halt condition (what stops if analysis doc is missing? — Step 1 says "Read" without a missing-file handler). No escalation path. Completion criterion: Step 7 Summary lists what to report but is not framed as a completion criterion. The skill can complete Steps 1–6 and then fail silently at Step 7. | G1 §Recovery | 1 | High |
| 6 | Planning probabilistic; execution deterministic. State tracking independent of conversation. | G3b.I1/I2 | Violated | The candidate-selection step (Step 3) is a user interaction gate embedded mid-procedure. If the user closes the session after viewing the candidate table (Step 3) but before providing selections, all previous steps' work is lost — no intermediate state is persisted outside conversation context. The dedup results (Step 2), candidate table (Step 3), and category mappings (Step 4) are conversation-state only. | G3b §Recovery | 1 | High |
| 7 | Every iterative pattern has a termination condition. | G3b.I3 | Satisfied | Step 1 iterates over identified analysis docs (bounded). Step 2 iterates over candidates (bounded). Step 5 iterates over selected candidates (bounded). No open-ended loops. | — | 1 | High |
| 8 | Degradation modes defined before go-live. | G3b.I4 | Partial | `--auto` behavior documented. Dedup classification (No match / Partial match / Full match) covers a key decision branch. However, no degradation mode for Step 1 missing-file scenario or Step 2 Grep returning unexpected results. | G3b §Recovery | 1 | Medium |
| 9 | Cost controls in place before autonomous execution. | G3b.I6 | Partial | `--auto` flag enables promotion of all non-duplicate candidates without user selection. This is the closest the skill comes to autonomous execution. No token budget or write-count limit is specified for `--auto` mode runs. If all analysis docs have many candidates, `--auto` could produce dozens of KB writes in one run. | G3b §Recovery | 1 | Medium |
| 10 | Only tools needed loaded into context. | G5.I4 | Satisfied | `Read Grep Glob Write Edit` — Read loads analysis docs and existing findings, Grep deduplicates, Glob enumerates analysis docs, Write creates new finding files, Edit annotates analysis doc candidates. All five are demonstrably needed. | — | 1 | High |
| 11 | Tool descriptions designed for non-deterministic consumers. | G5.I3 | Satisfied | Description uses concrete trigger phrasing: "After /repo-analyzer has produced analysis docs," "After /repo-analyzer --compare," "When the user asks to promote specific patterns." Negative-trigger cases listed: "Do NOT use this skill for…" | — | 1 | High |
| 12 | Intermediate tool results stay outside context window. | G5.I5 | Partial | Multiple analysis docs can be large; all are Read into context in Step 1. Grep searches `research-findings/` directory which may contain hundreds of findings. No progressive-loading strategy for large finding directories. | G5 §Recovery | 1 | Medium |
| 13 | Skills framework-agnostic. | G5.I11 | Satisfied | Plain markdown. No SDK coupling. | — | 1 | High |
| 14 | Permissions tiered by risk. | G6.I1 | Partial | Candidate selection (Step 3) gates Write/Edit on user approval for the default path. `--auto` mode bypasses this gate. No explicit risk-tier table distinguishing Write (new KB file) from Edit (annotation on existing file). | G6 §Recovery | 1 | Medium |
| 15 | Safety-critical constraints enforced structurally. | G6.I2 | Violated | Rule 1 (no auto-promote without `--auto`), Rule 6 (no modifying existing findings without approval) are prose-only. The `--auto` flag itself is documentation-level, not harness-enforced. Nothing structurally prevents Write/Edit from executing without going through the candidate-selection gate. | G6 §Recovery | 1 | High |
| 16 | Agent cannot modify its own permission configuration. | G6.I3 | Satisfied | No self-modification path present. | — | 1 | High |
| 17 | Defense is layered. | G6.I4 | Violated | Write/Edit protection is a single layer (prose instruction + user approval gate in Step 3). No second structural enforcement layer. `--auto` further reduces this to zero layers for non-duplicate candidates. | G6 §Recovery | 1 | High |
| 18 | Prompts tell model what to produce, not how to think. | G8.I1 | Satisfied | Procedure steps specify outputs (candidate table, dedup classification, finding files, analysis doc annotations, summary) without prescribing CoT. | — | 1 | High |
| 19 | High-priority rules as negative constraints. | G8.I3 | Satisfied | Rules section uses negation: "Never auto-promote without `--auto` flag," "Do not create research sources," "Do not modify existing findings without user approval." | — | 1 | High |
| 20 | ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL. | G8.I6 | Partial | ROLE (Researcher / Promoter) explicit in Cognitive Disposition. CONSTRAINT pervasive. AUTHORITY implicit. FAILURE SIGNAL absent — no specification of what consumers should observe if the skill fails or produces incorrect KB entries. | G8 §Recovery | 1 | Medium |
| 21 | **G9.I6 — Destructive or irreversible actions require human approval.** | G9.I6 | **Violated** | **This is a HARD-BLOCKING finding.** The `--auto` flag enables autonomous promotion of all non-duplicate candidates without user selection. Per G9.I6, "destructive or irreversible actions always require human approval regardless of trust level." Writing new findings into the IL KB is irreversible in practice (requires manual deletion to undo). The `--auto` path removes the human gate entirely. The prose caveat ("Use only when the user has pre-reviewed") is the only gate — which is a prompt instruction, not structural enforcement. This violates G9.I6. | G9 §Recovery — "Destructive or irreversible actions always require human approval" | 1 | High |
| 22 | Audit trail maintained for all agent actions. | G9.I2 | Partial | Step 6 "links back to analysis doc" creates a forward reference from each analysis doc candidate. This provides partial traceability. However, no system log entry or audit trail for the Write operations (new finding files created, existing findings modified). | G9 §Recovery | 1 | Medium |
| 23 | No decision type defaults to full autonomy without explicit classification. | G9.I5 | Violated | `--auto` mode assigns full autonomy to the promotion decision for all non-duplicate candidates without explicit per-candidate classification. "Non-duplicate" is a technical criterion (Grep returns no match), not a quality or relevance judgment. An `--auto` run can produce low-quality findings at full autonomy with no human in the loop. | G9 §Recovery | 1 | High |
| 24 | Comprehension maintained for shipped artifacts. | G9.I7 | Violated | `--auto` mode writes KB findings that no human has read or approved before they enter the KB. Per G9.I7: "agent-generated artifacts that no human has read are governance debt, not throughput gains." The `--auto` flag explicitly creates this debt. | G9 §Recovery | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | `--auto` mode governance. | G9.I6 | Has the use of `--auto` mode been explicitly authorized as a governance exception (i.e., is there a DD or explicit Nick approval for autonomous KB promotion)? If not, `--auto` should be removed or require a post-promotion human review gate. | DD reference or explicit authorization; or removal of `--auto` from the skill. |
| b | Structural enforcement on Write/Edit. | G6.I2 | Is there a harness hook or permission restriction preventing Write/Edit to `research-findings/` without user approval? Or are Rules 1 and 6 solely model-prose enforced? | Hook configuration entry; or explicit acknowledgment of structural gap. |
| c | Session-state resilience. | G3b.I2 | If the user closes the session after Step 3 (candidate selection) but before Step 5 (writes), is any work recovered? Is there a temp-file pattern planned for the dedup results and candidate table? | Description of state persistence mechanism; or acknowledgment that single-session assumption is intentional. |
| d | `--auto` write-count limit. | G3b.I6 | Is there a maximum number of findings the `--auto` mode will write in a single run? Without a limit, a large intake could produce unbounded KB writes. | Cost-control specification or limit parameter documentation. |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G2a/G2b | No context directives or caching behavior — G2 Preconditions unsatisfied. |
| G7 | Single-session design; no cross-session state management specified. |

---

### Summary

Classification: safety-critical (trigger: `allowed-tools` includes Write and Edit; procedure writes directly to the IL KB and edits analysis docs — both irreversible in practice without manual intervention).

**G9.I6 outcome: VIOLATED — HARD-BLOCKING.** The `--auto` flag enables autonomous KB promotion without human approval for all non-duplicate candidates (finding 21). Writing to `research-findings/` is irreversible in practice. G9.I6 states "destructive or irreversible actions always require human approval regardless of trust level." The prose caveat ("Use only when the user has pre-reviewed") is not structural enforcement and can be bypassed by model drift or direct invocation with `--auto`. Additionally, G9.I5 and G9.I7 are violated by the same `--auto` mechanism (findings 23, 24).

**What the skill does well:** Deduplication rigor (Step 2 with three-valued classification), evidence calibration defaults (Medium for analysis-doc-sourced candidates), candidate table presentation before writes, backward link annotation (Step 6), and the Priority Re-evaluation Check (Step 5b) are all well-designed. The negative-constraint framing in the Rules section is clear.

**Hard-blocking issues that must be resolved before deployment:**
1. **G9.I6 violation (finding 21):** Remove `--auto` mode or add a mandatory post-promotion human review gate that Nick must complete before the findings are treated as KB-canonical. Autonomous KB writes without human approval are governance debt by G9.I7 definition.
2. **G1.I5 violation (finding 5):** Add explicit halt conditions and completion criteria — minimally, a missing-file handler in Step 1 and a formal "skill succeeded" criterion in Step 7.
3. **G3b.I2 violation (finding 6):** State explicitly persisted state between Steps 3 and 5. The user interaction gate at Step 3 creates a session-interruption risk for a multi-step KB-modification skill.

---

### Skill: `systems/improvement-loop/.claude/skills/reassess-priorities/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 7, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

**mode: in-context-rubric** (assess-skill SKILL.md loaded; rubric applied directly — Skill tool delegated back to Librarian for in-context execution)

**Classification: safety-critical (trigger: allowed-tools includes Write)**

**Artifact:** `systems/improvement-loop/.claude/skills/reassess-priorities/SKILL.md`
**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — safety-critical; G9.I6 forced)
**Rubric size:** 17 file-verifiable invariants, 4 system/process-verifiable invariants, 0 latent (all guide Preconditions satisfied)

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Spec completeness | Every agent spec includes objective, desired outcomes, health metrics, constraints, autonomy levels, acceptance criteria, stop rules, context supply plan | G1.I1 | Partial | Skill has clear objective and procedure but lacks explicit acceptance criteria, health metrics, and a context supply plan section. "When to Use" and "Rules" are present but do not surface evaluable acceptance criteria | G1 §Recovery: fix spec before investigating behavior | 1 | High |
| 2 | Hard constraints have enforcement outside prompt layer | Hard constraints must have enforcement mechanisms outside the prompt layer | G1.I2 | Partial | Rule 1 ("Never auto-change priorities — Human gate is mandatory") is stated in prose but no structural enforcement (hook, gate step with explicit confirm-before-act) is present in the procedure. Step 5 says "Present the candidates table to the user" but the gate is informally described, not a structured pre-condition check | G1 §Recovery | 1 | High |
| 3 | Acceptance criteria evaluable by third party | Acceptance criteria are evaluable by a third party without access to the prompter's intent | G1.I3 | Missing | No explicit acceptance criteria section. The only success signals are output counts in Step 6 (how many scanned, flagged, updated) — these are metrics, not pass/fail acceptance criteria | G1 §Recovery | 1 | High |
| 4 | Stop rules: halt + escalation + completion | Stop rules include at least one halt condition, one escalation trigger, one completion criterion | G1.I4 | Partial | Step 5 says "Present candidates for approval" (completion) but no halt condition (e.g., "abort if KB unreachable") and no escalation trigger (e.g., "if > N upgrades would result from a single run, escalate") are defined | G1 §Recovery | 1 | Medium |
| 5 | Explicit state tracking independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b.I1 | Missing | The skill writes a report file (Step 4) which provides partial state, but there is no checkpoint or state artifact documenting progress through the findings scan. If the skill is interrupted mid-scan, no recovery path is defined | G3b §Recovery: add observability first | 1 | High |
| 6 | Iterative pattern has termination condition | Every iterative pattern has a termination condition (loop limit, stall detection, or both) | G3b.I2 | Partial | Steps 1-3 iterate over all findings in the KB. No loop limit or stall detection is specified. For a large KB this is an unbounded scan | G3b §Recovery | 1 | Medium |
| 7 | Degradation modes defined | Degradation modes are defined before the system goes live, not after first failure | G3b.I3 | Missing | No degradation modes defined. What happens if a finding file is malformed, if `Glob` returns zero results, or if `Edit` fails mid-update? Only Step 5 notes `--dry-run` as a mode change; no error handling for partial failures | G3b §Recovery | 1 | High |
| 8 | Only tools needed for current task loaded | Only tools needed for the current task are loaded into context | G5.I1 | Satisfied | `allowed-tools: Read Grep Glob Write` — all four are used: Read (Step 1-2), Grep (Step 2), Glob (Step 1), Write (Step 4). Edit is used in Step 5 but not listed in allowed-tools | G5 §Recovery | 1 | High |
| 9 | Edit tool used but not listed in allowed-tools | allowed-tools lists the minimum set; all tools used in procedure should appear | G5.I1 (tool surface alignment) | Violated | Step 5 explicitly uses `Edit` to update finding frontmatter, but `Edit` is not in `allowed-tools: Read Grep Glob Write`. This is a configuration mismatch — the skill will fail when it reaches Step 5 | G5 §Recovery: audit interface for poka-yoke opportunities | 1 | High |
| 10 | Tool descriptions designed for non-deterministic consumers | Tool descriptions are designed for non-deterministic consumers — they persuade, disambiguate, and explain when not to use the tool | G5.I2 | Partial | The "Paths" table clearly describes tool-to-purpose mapping. However there is no disambiguating guidance about when to prefer `Grep` over `Read` for evidence counting (Step 2 uses both) | G5 §Recovery | 1 | Low |
| 11 | Permissions tiered by risk, not binary | Permissions are tiered by risk, not binary allow/deny | G6.I1 | Partial | The skill acknowledges a human gate (Rule 1) but does not classify Write as a higher-risk operation than Read within its own permission model. All tools are listed flatly | G6 §Recovery | 1 | Medium |
| 12 | Safety-critical constraints enforced structurally | Safety-critical constraints are enforced structurally, not via prompt instructions alone | G6.I2 | Violated | Rule 1 ("Never auto-change priorities. Always present proposals for user approval. Human gate is mandatory.") is enforced via prose instruction only. No structural hook, confirmation step, or dry-run-by-default mechanism prevents the skill from calling `Edit` without explicit approval | G6 §Recovery | 1 | High |
| 13 | Destructive/irreversible actions require human approval regardless of trust level | G9.I6 invariant: destructive or irreversible actions always require human approval | G9.I6 | Partial | Step 5 requires user approval per Rule 1 before calling `Edit`. This is procedurally correct. However the gate is described informally ("Present the candidates table to the user… For each approved change, use `Edit`") rather than as a structured confirm-before-act that cannot be skipped. `--dry-run` is a mitigation but not a gate on the non-dry-run path | G9 §Recovery | 1 | High |
| 14 | Trigger description fires reliably | Description is phrased as consumer would ask; triggers reliably on intended use cases | G8.I1 | Satisfied | Description names the concrete trigger conditions (after batch repo analyses, large research-loop sessions, periodically). "When Nick asks 'what findings have gotten stronger since we last looked?'" is a concrete consumer phrasing | G8 §Recovery | 1 | High |
| 15 | Prompt carries explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL properties | G8.I2 | Partial | Cognitive Disposition section establishes ROLE (evidence auditor) and some CONSTRAINTS (conservative on upgrades, never downgrade). AUTHORITY (Curator authority) is named. FAILURE SIGNAL is absent — no explicit statement of what output shape or content indicates the skill produced an incorrect result | G8 §Recovery | 1 | Medium |
| 16 | High-priority behavioral rules as negative constraints | High-priority behavioral rules expressed as negative constraints, not positive aspirations | G8.I3 | Satisfied | Rules section uses negative form for load-bearing constraints: "Never auto-change priorities," "Never downgrade," "Do not modify finding body content" | G8 §Recovery | 1 | High |
| 17 | Output format control explicit | Output format control is explicit and user-overridable where interactive | G8.I4 | Satisfied | Report format is fully specified in Step 4 with YAML frontmatter template and markdown body template. `--dry-run` argument provides overridability | G8 §Recovery | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|---|---|---|---|
| a | Stable context is cached separately from ephemeral turn state | G8 (prompt caching) | Is the findings scan prompted in a way that caches stable KB context separately from per-finding evaluation? | Harness caching config; observed cache-hit rate |
| b | Complexity tiering and context-aware routing implemented | G3b.I5 | Is there routing logic that routes small (<10 findings) scans differently from full-KB scans? | Routing config or skill variant documentation |
| c | Cost controls in place before autonomous execution | G3b.I6 | What is the maximum number of Edit calls this skill can make in a single run, and is there a budget cap? | Per-step budget documentation |
| d | Tool risk classifications reviewed when capabilities change | G6 governance | Has the Write/Edit tool access been reviewed relative to the finding-frontmatter mutation risk? | Risk classification record |

---

### Aspects out of scope

| Guide | Why latent |
|---|---|
| G2a/G2b | No context directives or context-loading in the skill prompt — G2a/G2b Preconditions unsatisfied |

---

### DD-92 ContextSpec audit

DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

---

### Summary

**G9.I6 outcome: Partial — deployment gate not fully satisfied.** The human-approval gate for Write/Edit actions is procedurally specified (Rule 1, Step 5) but is enforced via prose instructions only, not a structural confirm-before-act mechanism. The skill also has a configuration defect (Edit used in Step 5 but absent from `allowed-tools`) that will cause runtime failure. Load-bearing fixes before deployment: (1) add `Edit` to `allowed-tools`, (2) add a structural HITL gate in Step 5 (explicit confirm prompt that cannot be bypassed, or `--dry-run` as default requiring explicit opt-in), (3) add acceptance criteria evaluable by a third party, (4) define degradation modes for malformed findings and partial-scan interruption.

---

### Skill: `systems/improvement-loop/.claude/skills/repo-analyzer/SKILL.md`
*Dispatched to bin 4 — **report MISSING**.*

Bin 4 emitted only 1 of N expected sentinel-delimited reports (format-compliance failure per `/audit-system` SKILL.md §FAILURE SIGNAL — individual-report-missing, not whole-bin-unparseable). Cause: subagent message-budget or instruction-following drift between dispatch payload and assessor invocation. Artifact unassessed in this run.

**Resolution:** invoke the IL `/assess-skill` (or `/assess-agent --variant prompt-based`) skill directly on this path, or re-audit via `/audit-system systems/improvement-loop/ --scope skills`.

---

### Skill: `systems/improvement-loop/.claude/skills/research-loop/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 3, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** safety-critical (Write, Edit)

**Critical:** **G9.I6 VIOLATED** — writes to KB (sources, findings, authorities) without any HITL gate in the procedure; external post-run review is unenforced.

**G9.I6 outcome:** Violated — skill can complete dozens of writes before a human sees anything.

**Top findings:**
- F#20 Violated G9.I6: no HITL gate for KB writes.
- F#14 Violated G6.I2: write-scope boundary prose-only.
- F#22 Violated: no autonomy classification per decision type.
- F#8 Partial: `WebSearch` in `allowed-tools` is never invoked in the procedure (over-grant).
- F#6 Missing: no degradation modes defined.

---

### Skill: `systems/improvement-loop/.claude/skills/research-proposer/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 3, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** safety-critical, DEPRECATED (DD-80)

**Critical:** F#25 Violated — deprecated skill retains a fully executable procedure with no halt-at-procedure-start sentinel; `user-invocable: false` alone is insufficient against subagent invocation.

**G9.I6 outcome:** Partial — proposals do not trigger system changes (intended post-write gate), but writes proceed without in-procedure approval.

**Top findings:**
- F#25 Violated: deprecation incomplete — no halt sentinel inside procedure.
- F#15 Violated G6.I2: write-scope boundary prose-only.
- F#17 Violated G6.I4: single-layer defense.
- F#24 Violated: write operations default to autonomous with no per-decision classification.

---

### Skill: `systems/improvement-loop/.claude/skills/research-query/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 6, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

**mode: in-context-rubric**
**Artifact:** `systems/improvement-loop/.claude/skills/research-query/SKILL.md`
**Classification: safety-critical (trigger: allowed-tools includes Write, Edit, Agent; procedure writes finding entries, source entries, and research reports to KB paths; Agent spawns parallel research subagents).**

**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — safety-critical forced)
**Rubric size:** 17 file-verifiable invariants, 7 system/process-verifiable invariants, 0 latent

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Stop rules | G1.I5: halt/escalation/completion | G1 §Invariants | Missing | No "Boundary Conditions" section. No explicit halt condition, escalation trigger, or abort path. The persistence gate (Step 5) is a user decision point but is not framed as a stop rule. | G1 §Recovery | 1 | High |
| 2 | Acceptance criteria | G1.I4: third-party evaluable | G1 §Invariants | Missing | No acceptance criteria stated. The report template is an output shape, not a testable completion condition. A third party cannot determine from the skill body what constitutes a correctly completed research query. | G1 §Recovery | 1 | High |
| 3 | Autonomy classification | G1.I1: autonomy levels per decision type | G1 §Invariants | Missing | No autonomy table. The skill performs a range of autonomy levels: read-only (Steps 1-3), user-gated write (Step 5 persistence gate), and autonomous write (Step 6 when user opts in). These differ by blast radius but are not classified. | G1 §Recovery | 1 | High |
| 4 | HITL gate for persistence writes | G9.I6: destructive/irreversible actions require human approval | G9 §Invariants | Satisfied | Step 5 (Persistence Gate) is an explicit human approval step: "Persistence is always user-gated. Never autonomously write findings from on-demand queries. DD-29 + DD-83." Rule 1 is an explicit prohibition. This is the strongest G9.I6 implementation in this audit batch — the gate is named, rationale cited (DD-29, DD-83), and the default is no write. | — | 1 | High |
| 5 | HITL gate for report write | G9.I6: report write is autonomous | G9 §Invariants | Violated | Rule 2 states "Even if the user declines persistence, the report goes to `operations/research-reports/`." This report write is autonomous — no user approval step. The report write has lower blast radius than KB writes, but it is still a file-system mutation performed without the user's explicit approval for that specific action. | G9 §Recovery | 1 | Medium |
| 6 | State tracking | G3b.I2: explicit state independent of conversation | G3b §Invariants | Partial | The report is written to a file (Step 4), which provides a form of state persistence. The `persist_findings` frontmatter field tracks persistence status. However, no checkpoint mechanism is defined for partial failures (e.g., 3 of 5 finding files written before interruption). | G3b §Recovery | 1 | Medium |
| 7 | Termination condition for parallel agents | G3b.I3: iterative pattern has termination condition | G3b §Invariants | Partial | Step 3 mentions "Parallel research via Agent if the topic has clearly independent sub-questions." No termination condition, timeout, or convergence criterion is specified for the parallel agent invocation. The parent step implicitly waits for all agents to return, but no timeout or partial-result handling is described. | G3b §Recovery | 1 | Medium |
| 8 | Degradation modes | G3b.I4: degradation modes defined | G3b §Invariants | Partial | The dimension-check gate (Step 1) handles the "topic doesn't fit dimensions" case with two explicit options. The persistence gate (Step 5) handles the "user declines" case. However, no degradation for Perplexity MCP failure, WebFetch timeout, or empty research results is defined. | G3b §Recovery | 1 | Medium |
| 9 | Tool loading discipline | G5.I4: only needed tools loaded | G5 §Invariants | Partial | `allowed-tools: Read Grep Glob Write Edit Agent WebFetch`. All Perplexity MCP tools are listed in the "Available Tools" table but `perplexity_research`, `perplexity_reason`, `perplexity_search`, `perplexity_ask` are not in the `allowed-tools` frontmatter. This is an inconsistency: the procedure calls these tools but they are not declared. The declared tool surface includes WebFetch and Agent even for simple queries that will not require parallel research. | G5 §Recovery | 1 | High |
| 10 | Tool descriptions | G5.I3: descriptions designed for non-deterministic consumers | G5 §Invariants | Satisfied | The "Available Tools" table explains the purpose and preference order for each tool. The procedure describes when to use each Perplexity variant (primary vs. follow-up). "When NOT to Use" section redirects to appropriate alternatives. | — | 1 | High |
| 11 | Usage examples | G5.I6: complex tools include usage examples | G5 §Invariants | Satisfied | Step 3 provides the system message template for `perplexity_research`. Step 4 provides a complete report template. Step 6 provides the finding and source entry templates with all schema fields. | — | 1 | High |
| 12 | Structural enforcement of scope constraints | G6.I2: safety-critical constraints enforced structurally | G6 §Invariants | Partial | The persistence gate is enforced by explicit procedural instruction (strong for a prompt layer). However, the prohibition on authority-entry creation (Rule 7) is prose-only with no structural enforcement. The Edit permission could be used to edit any file; restriction to `research-findings/` is prose-only. | G6 §Recovery | 1 | Medium |
| 13 | Defense in layers | G6.I4: defense layered | G6 §Invariants | Partial | The persistence gate adds a meaningful second layer for KB writes. The report write lacks a second layer. The Edit scope restriction is single-layer (prose). | G6 §Recovery | 1 | Medium |
| 14 | Trigger description quality | G8 trigger | G8 §Invariants | Satisfied | Description uses exact consumer phrasings. "When to Use" and "When NOT to Use" sections are both present and name concrete contrasts with peer skills (`/research-loop`, `/perplexity-research`). The DD-83 reference provides governance grounding. | — | 1 | High |
| 15 | ROLE/AUTHORITY/CONSTRAINT/FAILURE SIGNAL | G8.I6 | G8 §Invariants | Partial | ROLE is explicit ("Researcher — same persona as /research-loop"). CONSTRAINT is distributed across Rules. AUTHORITY is partially stated via DD-83 citation. FAILURE SIGNAL is absent — no explicit declaration of what the model should signal when the research yields insufficient evidence. | G8 §Recovery | 1 | Medium |
| 16 | Negative constraints for high-priority rules | G8.I3 | G8 §Invariants | Satisfied | Rules 1 ("Never autonomously write"), 7 ("Do not create authorities entries") are explicit prohibitions. The persistence gate framing ("Never autonomously write findings") is a strong negative constraint. | — | 1 | High |
| 17 | DD-92 ContextSpec | DD-92 | DD-92 | Skipped | DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here. | — | — | — |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | G9.I6: report write confirmation | G9 §Invariants | Is the report write (Step 4) surfaced to the user before execution, or is it silent? If silent, is there a rationale for why it is exempt from the persistence gate? | Skill update clarifying report-write policy, or harness hook |
| b | G5.I4: Perplexity tool declarations | G5 §Invariants | The Perplexity MCP tools are used in the procedure but absent from `allowed-tools` frontmatter. Are they loaded through a different mechanism (MCP server auto-availability)? Or is the frontmatter declaration incomplete? | MCP server config or skill frontmatter update |
| c | G3b.I2: finding write checkpointing | G3b §Invariants | If the skill is interrupted after writing 2 of 5 finding files in Step 6, is there a recovery path? Or does re-running risk duplicate finding entries? | Checkpoint mechanism or documented idempotency guarantee |
| d | G3b.I6: cost controls for parallel agents | G3b §Invariants | Step 3 allows spawning parallel agents. Is there a limit on concurrency or a total token budget for the parallel research phase? | Documented concurrency limit or harness-level budget |
| e | G8.I7: prompt changes versioned and tested | G8 §Invariants | The system message template in Step 3 is the primary research prompt. Are changes to this template versioned and tested against acceptance criteria? | Commit history or acceptance test |
| f | G1.I1: health metrics | G1 §Invariants | Are metrics tracked for on-demand research quality (e.g., finding rejection rate after persistence, evidence_strength distribution of persisted findings)? | System log or KB analytics |
| g | G5.I7: skill versioned | G5 §Invariants | Is the `research-query` skill versioned and locked? | Lock file or version manifest |

---

### Aspects out of scope

| Guide | Why latent |
|-------|-----------|
| G1 Precondition: "non-trivial autonomous work" | Satisfied — multiple Perplexity calls, optional KB writes, optional parallel agents. G1 fires fully. |
| G3b Precondition: "side effects or longer than single turn" | Satisfied — file writes to `research-reports/` and optionally `research-findings/`. G3b fires fully. |
| G9 Precondition: "destructive/irreversible actions" | Satisfied — Write/Edit to KB paths. G9.I6 fires. |

---

### Summary

G9.I6 outcome: **Partially satisfied.** The persistence gate (Step 5) is the strongest HITL implementation seen across this audit batch — it is explicit, user-gated by default, and cites governing DDs. However, the autonomous report write (Rule 2) is an unchecked G9.I6 violation at lower blast radius. The overall G9 posture is good for KB writes, needs improvement for the report write.

The critical missing elements are stop rules (G1.I5), acceptance criteria (G1.I4), and autonomy classification (G1.I1). A significant tool-declaration inconsistency exists: the Perplexity MCP tools are used in the procedure but absent from the `allowed-tools` frontmatter — this should be resolved to clarify whether they are loaded via MCP server or require frontmatter declaration. The trigger description, negative-constraint framing, and usage examples are strong.

---

### Skill: `systems/improvement-loop/.claude/skills/solicit-proposals/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 7, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

**mode: in-context-rubric** (assess-skill SKILL.md loaded; rubric applied directly)

**Classification: safety-critical (trigger: allowed-tools includes Write and Bash)**

**Artifact:** `systems/improvement-loop/.claude/skills/solicit-proposals/SKILL.md`
**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — safety-critical; G9.I6 forced)
**Rubric size:** 17 file-verifiable invariants, 4 system/process-verifiable invariants, 0 latent

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Spec completeness | Every spec includes objective, desired outcomes, health metrics, constraints, autonomy levels, acceptance criteria, stop rules, context supply plan | G1.I1 | Partial | Objective is clear (reflection round orchestration). Rules section covers autonomy tier and constraints. No health metrics section, no explicit acceptance criteria, no context supply plan section. "Calibration Notes" is informal rather than structured health metrics | G1 §Recovery | 1 | High |
| 2 | Templates filled completely — no TBD or TODO | Templates are filled in completely — no placeholder fields left as "TBD" or "TODO" | G1.I2 | Satisfied | The procedure step templates (e.g., the status table in Step 1, proposal naming convention in Step 3) are complete with no unresolved placeholders | G1 §Recovery | 1 | High |
| 3 | Acceptance criteria evaluable by third party | Acceptance criteria are evaluable by a third party without access to the prompter's intent | G1.I3 | Missing | No acceptance criteria section. Success is described implicitly (proposals land in `governance/proposals/`, SL entry written) but no pass/fail criteria for round quality are specified | G1 §Recovery | 1 | High |
| 4 | Stop rules: halt + escalation + completion | Stop rules include at least one halt, escalation trigger, completion criterion | G1.I4 | Partial | Completion criterion implicit (Step 5 summary = round done). Halt condition: Step 2 says "Do NOT retry autonomously" for failed agents — this is a halt signal but not a halt criterion for the overall round. No escalation trigger defined (e.g., "if all 4 agents fail to reflect, escalate to Nick before proceeding") | G1 §Recovery | 1 | Medium |
| 5 | Explicit state tracking independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b.I1 | Partial | Step 4 writes an SL entry that captures round state. However there is no checkpoint between Steps 1-3 — if the skill is interrupted after reflecting two agents but before the third, the SL entry is not written until Step 4 and partial work is unrecoverable without conversation history | G3b §Recovery | 1 | Medium |
| 6 | Iterative pattern has termination condition | Every iterative pattern has a termination condition | G3b.I2 | Satisfied | Step 1 iterates over a bounded agent list (four agents maximum). The list is finite and explicit. Stale/fresh classification per agent terminates the inner loop cleanly | G3b §Recovery | 1 | High |
| 7 | Degradation modes defined | Degradation modes are defined before going live | G3b.I3 | Partial | Step 2 handles one degradation: agent refuses/errors → log, skip, don't retry. No degradation defined for: Write failures (reflection file not written), `Glob` returning unexpected results, Bash date-math failures in freshness check | G3b §Recovery | 1 | Medium |
| 8 | Only tools needed loaded into context | Only tools needed for the current task are loaded | G5.I1 | Satisfied | `Read`, `Write`, `Glob`, `Grep`, `Bash` — each is accounted for in the "Available Tools" table with explicit purpose mapping. No extraneous tools listed | G5 §Recovery | 1 | High |
| 9 | Tool descriptions designed for non-deterministic consumers | Tool descriptions persuade, disambiguate, explain when not to use | G5.I2 | Satisfied | Available Tools table maps each tool to a concrete purpose ("Directory listings, date math for freshness checks" for Bash). Disambiguation is present for Read vs. Grep (Read = content, Grep = freshness timestamps) | G5 §Recovery | 1 | High |
| 10 | Permissions tiered by risk | Permissions are tiered by risk, not binary allow/deny | G6.I1 | Partial | Rules section establishes "Guarded" autonomy tier for the overall skill and names the two human gates (focus-area approval at Step 0; proposal acceptance downstream). However Write operations (reflection files, proposal files, SL entry) are not individually risk-tiered — all Write calls have the same implicit permission level | G6 §Recovery | 1 | Medium |
| 11 | Safety-critical constraints enforced structurally | Safety-critical constraints are enforced structurally, not via prompt instructions alone | G6.I2 | Partial | Step 0 gates focus areas on Nick's approval (structural gate). Proposal acceptance is Nick-gated downstream. However the reflection write and SL entry write are not gated — they occur autonomously between the two human gates. Given that reflections are identified as "agent-private," the un-gated write of reflection files is an acceptable design choice if documented, but the design rationale is not stated | G6 §Recovery | 1 | Medium |
| 12 | Agent cannot modify its own permission configuration | The agent cannot modify its own permission configuration | G6.I3 | Satisfied | The skill does not write to harness configuration, permission manifests, or governance tier assignments | G6 §Recovery | 1 | High |
| 13 | Defense is layered | Defense is layered — no single mechanism is the sole protection | G6.I4 | Partial | Gate 1 (focus-area approval) + Gate 2 (proposal acceptance) form a two-layer defense for the proposal pathway. However the reflection write path has no defense layer — it runs between gates with only the "no coercion" rule as a soft constraint | G6 §Recovery | 1 | Low |
| 14 | Destructive/irreversible actions require human approval | G9.I6: destructive or irreversible actions always require human approval regardless of trust level | G9.I6 | Partial | Proposal files (output of primary concern) are gated on Nick's acceptance (Step 5). Reflection files are intermediate artifacts with `stage: "superseded"` marking of prior reflections. The superseding write of prior reflections (marking `stage: "superseded"`) is an irreversible state change on existing files that is not explicitly gated — it occurs in Step 2 automatically. This is the load-bearing G9.I6 gap | G9 §Recovery | 1 | High |
| 15 | Trigger description fires reliably | Description phrased as consumer would ask; triggers on intended use cases | G8.I1 | Satisfied | "Run an IL reflection round" is concrete. The description names three trigger conditions (periodic, Nick-invokes, post-significant-change). The "When NOT to Use" section provides clear negative disambiguation | G8 §Recovery | 1 | High |
| 16 | Prompt carries explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | G8.I2 | Partial | ROLE (Owner, orchestrator) and CONSTRAINTS (no coercion, privacy boundary, no IB filing) are explicit. AUTHORITY is implied (Owner-owned skill per DD-86) but not stated as a formal authority declaration. FAILURE SIGNAL is absent — no definition of what an invalid round output looks like | G8 §Recovery | 1 | Medium |
| 17 | High-priority behavioral rules as negative constraints | G8.I3 | Satisfied | Rules use negative form for load-bearing constraints: "No coercion of reflection depth," "No IB filing inside this skill," "Do NOT retry autonomously" | G8 §Recovery | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|---|---|---|---|
| a | Cost controls in place before autonomous execution | G3b.I6 | What is the token/time budget for a full four-agent round (all stale)? Is there a hard cutoff if one agent's reflection loop stalls? | Per-run budget documentation or harness timeout config |
| b | Workflow state separation from conversation | G3b governance | Is the SL entry written incrementally (one entry per agent step) or only at Step 4? If Step 4 is never reached, is round state recoverable? | SL entry structure review; recovery test |
| c | Approval rates monitored | G6 governance | Is there tracking of how often Nick approves focus-area proposals vs. modifies them? Rates above 90% auto-approval may indicate the gate is being rubber-stamped | Approval rate data |
| d | Agent reflection privacy — read access control | G6.I2 | The skill states reflections are agent-private. Is this enforced at the harness level (separate file permissions, directory scoping) or only by disposition convention? | Harness file-permission config |

---

### Aspects out of scope

| Guide | Why latent |
|---|---|
| G2a/G2b | Skill does not embed or load context material into a prompt layer — G2a/G2b Preconditions unsatisfied |

---

### DD-92 ContextSpec audit

DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

---

### Summary

**G9.I6 outcome: Partial — one unreviewed irreversible write.** The primary proposal pathway is properly gated (focus-area approval at start, proposal acceptance at end). The load-bearing gap is in Step 2: prior reflection files are marked `stage: "superseded"` automatically without a human gate — this is an irreversible state change on existing files. Additionally, acceptance criteria are absent (G1.I3 Missing) and the FAILURE SIGNAL property is undefined (G8.I2 Partial). These are the three load-bearing items. The overall architecture is sound; the gaps are authoring omissions rather than structural failures.

---

### Skill: `systems/improvement-loop/.claude/skills/source-triage/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 6, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

**mode: in-context-rubric**
**Artifact:** `systems/improvement-loop/.claude/skills/source-triage/SKILL.md`
**Classification: safety-critical (trigger: allowed-tools includes Write; allowed-tools includes Agent — spawns subagents with WebFetch; Step 4 writes triage report to `operations/research-reports/`; Step 5 optionally writes to source files).**

**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — safety-critical forced)
**Rubric size:** 17 file-verifiable invariants, 7 system/process-verifiable invariants, 0 latent

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Stop rules — halt/escalation/completion | G1.I5: stop rules include all three types | G1 §Invariants | Missing | No "Boundary Conditions" section present. No explicit halt condition, escalation trigger, or completion criterion is stated. The `--dry-run` flag prevents Step 5 writes but is not framed as a stop-rule. | G1 §Recovery | 1 | High |
| 2 | Acceptance criteria | G1.I4: third-party evaluable | G1 §Invariants | Missing | No explicit acceptance criteria. The triage report template's Summary table is an output shape, not an acceptance criterion. A third party cannot determine from the skill body alone what "correct" triage output looks like. | G1 §Recovery | 1 | High |
| 3 | Autonomy classification | G1.I1: autonomy levels per decision type | G1 §Invariants | Missing | No autonomy table. The "Cognitive Disposition" text ("Full Autonomy tier — read-only analysis" in a related skill) is absent; this skill has no autonomy declaration at all. Yet it spawns subagents (Agent tool) and writes files — these are higher-autonomy actions. | G1 §Recovery | 1 | High |
| 4 | HITL gate for Write | G9.I6: destructive/irreversible actions require human approval | G9 §Invariants | Violated | Step 4 writes triage report autonomously. Step 5 writes triage notes to source files. The `--dry-run` flag at Step 5 is opt-in (default is write). No user confirmation step before either write action. G9.I6 requires explicit human approval; `--dry-run` as an opt-out is inverted from the required pattern. | G9 §Recovery | 1 | High |
| 5 | HITL gate for Agent spawning | G9.I6 (compound: Agent spawning with WebFetch) | G9 §Invariants | Violated | The skill spawns subagents (Step 2) with WebFetch capability without a human approval gate. Subagent scope is bounded (triage verdict output), but spawning itself is unchecked. This is a safety-critical composition: Agent + WebFetch produces external network calls without human confirmation. | G9 §Recovery | 1 | High |
| 6 | Termination condition for iterative subagent loop | G3b.I3: iterative patterns have termination condition | G3b §Invariants | Partial | Step 2 batches sources 5-8 per subagent. The number of batches is bounded by the source list size (finite), so the iteration terminates by exhaustion. However, no explicit loop limit or stall-detection is stated. If a subagent hangs, there is no timeout or abort path defined. | G3b §Recovery | 1 | Medium |
| 7 | State tracking | G3b.I2: explicit state tracking independent of conversation history | G3b §Invariants | Missing | The skill runs subagents in parallel and then collects results (Step 3). No checkpoint or resumption path is defined for the case where some subagents complete and others fail. If interrupted, partial results are not persisted. | G3b §Recovery | 1 | Medium |
| 8 | Degradation modes | G3b.I4: degradation modes defined before go-live | G3b §Invariants | Partial | DEFER verdict handles inaccessible sources. "If Perplexity returns thin results" is not referenced here (different skill), but the decision tree handles paywall/dead-link cases. However, no degradation for subagent failure, WebFetch timeout, or malformed JSON response from a subagent is defined. | G3b §Recovery | 1 | Medium |
| 9 | Tool loading discipline | G5.I4: only needed tools loaded | G5 §Invariants | Partial | `allowed-tools: Read Grep Glob WebFetch Agent` — WebFetch is loaded at the top-level skill even though it is only used inside subagents. The subagent prompt includes WebFetch as an instruction; the top-level skill could restrict WebFetch to subagent scope only. This is a minor over-grant at the top level. | G5 §Recovery | 1 | Low |
| 10 | Tool descriptions for non-deterministic consumers | G5.I3 | G5 §Invariants | Satisfied | The subagent prompt template in Step 2 provides detailed instructions for WebFetch usage (read first 3000 chars for articles, abstract/intro for papers) and decision tree. The top-level skill's "Calibration Notes" section explains how to use verdicts. | — | 1 | High |
| 11 | Usage examples for complex tools | G5.I6: complex tools include usage examples | G5 §Invariants | Satisfied | The JSON output format for subagents is fully specified with field names, types, and a concrete example row. The decision tree is a working example of how to apply the verdicts. | — | 1 | High |
| 12 | Tool output format matches consumer | G5.I8: format matches consumer | G5 §Invariants | Satisfied | Subagent output is strict JSON consumed by Step 3's parse step. Top-level output is a markdown report consumed by humans (Nick). Both formats are appropriate for their consumer. | — | 1 | High |
| 13 | Structural enforcement of KB write prohibition | G6.I2: safety-critical constraints enforced structurally | G6 §Invariants | Partial | Step 5 is scoped to "source file body (not frontmatter)" and triage note format. The prohibition on modifying finding files is stated in "What This Skill Does NOT Do" as prose only. The `Write` permission is not restricted by path in the allowed-tools declaration. | G6 §Recovery | 1 | Medium |
| 14 | Defense in layers | G6.I4: defense layered | G6 §Invariants | Violated | The sole safeguard against scope-creep writes is the prose "What This Skill Does NOT Do" section. No second layer (path guard, hook, harness restriction) is present. | G6 §Recovery | 1 | Medium |
| 15 | Trigger description quality | G8 trigger description | G8 §Invariants | Satisfied | Description uses concrete consumer phrasing referencing the source quality audit and research-loop investment decision. "When to Use" section names four specific use cases. "When NOT to Use" is absent (minor gap). | — | 1 | High |
| 16 | ROLE/AUTHORITY/CONSTRAINT/FAILURE SIGNAL | G8.I6 | G8 §Invariants | Partial | ROLE is implied by context ("Source Triage" persona in subagent prompt). CONSTRAINT is embedded in Rules. No explicit AUTHORITY or FAILURE SIGNAL declared. | G8 §Recovery | 1 | Medium |
| 17 | DD-92 ContextSpec | DD-92 | DD-92 | Skipped | DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here. | — | — | — |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | G9.I6: human approval for writes | G9 §Invariants | Is the triage report write (Step 4) surfaced to the user before execution? Is a confirm-before-write step planned? Or is --dry-run the only protection? | Skill update or harness hook adding explicit user confirmation before any Write |
| b | G3b.I6: cost controls | G3b §Invariants | Subagent spawning with WebFetch can produce unbounded external calls across large source batches. Is there a per-batch or per-invocation WebFetch budget? | Documented per-invocation call budget or harness-level rate limit |
| c | G3b.I2: state checkpointing | G3b §Invariants | If the skill is interrupted after 2 of 5 subagent batches complete, can the partial results be recovered? | Checkpoint file or documented resume path |
| d | G5.I7: skill versioning | G5 §Invariants | Is the `source-triage` skill versioned? | Lock file or version manifest |
| e | G6.I1: risk classification of Write permission | G6 §Invariants | Is the Write permission in this skill classified as mutating in the harness permission tier configuration? | Permission tier registry or settings.json |
| f | G1.I1: health metrics | G1 §Invariants | Are triage accuracy metrics tracked (e.g., EXTRACT decisions that yield 0 findings after full extraction — false EXTRACT rate)? | Health metrics definition or system log entries tracking triage-to-extraction yield |
| g | G3b.I3: subagent timeout | G3b §Invariants | If a subagent hangs indefinitely on a WebFetch call, is there a timeout or abort mechanism in the Agent invocation? | Harness timeout config or Agent invocation timeout parameter |

---

### Aspects out of scope

| Guide | Why latent |
|-------|-----------|
| G1 Precondition: "non-trivial autonomous work" | Satisfied — multi-subagent parallel execution, file writes. G1 fires fully. |
| G3b Precondition: "side effects or longer than single turn" | Satisfied — file writes, WebFetch external calls. G3b fires fully. |
| G9 Precondition: "destructive or irreversible actions" | Satisfied — file writes to source files and reports. G9.I6 fires. |

---

### Summary

G9.I6 outcome: **Violated (two instances).** The report write (Step 4) and source-file write (Step 5) both execute autonomously without a human approval gate. The `--dry-run` flag at Step 5 is opt-in rather than opt-out, which inverts the required HITL pattern. Subagent spawning with WebFetch is an additional safety-critical path without confirmation. These are the load-bearing findings for deployment readiness.

Additional critical gaps: missing stop rules and acceptance criteria (G1), missing autonomy classification (G1), and structural defense (G6.I4) enforced only by prose. The skill has strong elements in subagent prompt design (decision tree, JSON output spec, usage calibration notes), but the safety and spec-completeness gaps should be addressed before use in an automated pipeline context.

---

### Skill: `systems/improvement-loop/.claude/skills/synthesize-guide/SKILL.md`
*Dispatched to bin 2 — **report MISSING**.*

Bin 2 emitted only 1 of N expected sentinel-delimited reports (format-compliance failure per `/audit-system` SKILL.md §FAILURE SIGNAL — individual-report-missing, not whole-bin-unparseable). Cause: subagent message-budget or instruction-following drift between dispatch payload and assessor invocation. Artifact unassessed in this run.

**Resolution:** invoke the IL `/assess-skill` (or `/assess-agent --variant prompt-based`) skill directly on this path, or re-audit via `/audit-system systems/improvement-loop/ --scope skills`.

---

### Skill: `systems/improvement-loop/.claude/skills/system-audit/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 6, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

**mode: in-context-rubric**
**Artifact:** `systems/improvement-loop/.claude/skills/system-audit/SKILL.md`
**Classification: safety-critical (trigger: allowed-tools includes Bash and Write; procedure writes an audit report to `operations/audit-reports/`; Step 10 creates a directory if needed).**

**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — safety-critical forced)
**Rubric size:** 16 file-verifiable invariants, 6 system/process-verifiable invariants, 0 latent

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Stop rules | G1.I5: halt/escalation/completion | G1 §Invariants | Partial | Rule 2 states "Write the report" — this functions as a completion criterion (report written = done). Rule 4 states "No fixes during audit" — this is an implicit abort/scope constraint but not a formal halt condition. No escalation trigger is defined (e.g., when to escalate a Critical finding vs. proceed). | G1 §Recovery | 1 | Medium |
| 2 | Acceptance criteria | G1.I4: third-party evaluable | G1 §Invariants | Partial | The report template includes an "Overall status: Clean / N findings" field and severity classification (Critical/Warning/Info). These are evaluable by a third party. However, no quantitative threshold or acceptance gate is stated (e.g., "audit passes if zero Critical findings"). | G1 §Recovery | 1 | Medium |
| 3 | Autonomy classification | G1.I1: autonomy levels per decision type | G1 §Invariants | Partial | Rule 1 states "Full Autonomy tier — read-only analysis producing a written report." This is a named autonomy classification. However, Step 10 (directory creation) is also autonomous and not separately classified. The Bash tool can execute arbitrary commands — no autonomy distinction is drawn between read-only Bash vs. mutating Bash use. | G1 §Recovery | 1 | Medium |
| 4 | HITL gate for Write (report) | G9.I6: destructive/irreversible actions require human approval | G9 §Invariants | Violated | The audit report write (Step 9) and directory creation (Step 10) are performed autonomously. Rule 1 states "Full Autonomy tier" — but "Full Autonomy" producing a persistent file write is still a G9.I6-triggering action. No user confirmation or dry-run mode exists for the Write step. | G9 §Recovery | 1 | High |
| 5 | HITL for Bash tool use | G9.I6: Bash with potential destructive flags | G9 §Invariants | Partial | Bash is used for "directory listings, structural analysis." All described Bash uses are read-only (`ls`, pattern matching). However, the `allowed-tools` declaration does not restrict Bash to read-only flags; the restriction is prose-only. | G9 §Recovery | 1 | Medium |
| 6 | State tracking | G3b.I2: explicit state independent of conversation | G3b §Invariants | Partial | The 9-step procedure is sequential. Steps 1-8 are read-only; the state is implicitly accumulated in working memory. The report (Step 9) is the only persistence artifact. No checkpoint for partial failure (e.g., Steps 1-5 complete, Steps 6-8 fail). | G3b §Recovery | 1 | Medium |
| 7 | Termination condition | G3b.I3: iterative patterns have termination condition | G3b §Invariants | Satisfied | The audit procedure is linear (Steps 1-10 in sequence, each finite). No iterative loop is present — each step processes a finite, enumerable set. Termination is bounded by the IL system's finite file structure. | — | 1 | High |
| 8 | Degradation modes | G3b.I4: degradation modes defined | G3b §Invariants | Partial | The "Calibration Notes" acknowledge that the first audit will have many findings (expected state). However, no degradation path is defined for: missing agent definition files, unreadable files, or Bash command failures. The procedure assumes all reads succeed. | G3b §Recovery | 1 | Medium |
| 9 | Tool loading — minimal surface | G5.I4: only needed tools loaded | G5 §Invariants | Satisfied | `allowed-tools: Read Grep Glob Bash Write` — a minimal surface for a structural audit. Each tool is used in specific steps: Read (agent/skill files), Grep (cross-reference search), Glob (file enumeration), Bash (directory listings), Write (report). | — | 1 | High |
| 10 | Tool descriptions | G5.I3: descriptions for non-deterministic consumers | G5 §Invariants | Satisfied | The "Available Tools" table lists each tool with its specific purpose in this skill. The descriptions disambiguate tool roles effectively. | — | 1 | High |
| 11 | Structural enforcement of audit-only constraint | G6.I2: safety-critical constraints enforced structurally | G6 §Invariants | Violated | Rule 4 ("No fixes during audit") is the most critical safety constraint. It is enforced by prose instruction only. The Write and Edit tools could be used to fix findings during audit — no structural mechanism prevents this. | G6 §Recovery | 1 | High |
| 12 | Defense in layers | G6.I4: defense layered | G6 §Invariants | Violated | The audit-only constraint (no fixes) has a single layer: the prose Rule 4. No structural enforcement (tool restriction, harness hook, path guard to write-only `audit-reports/`) provides a second layer. | G6 §Recovery | 1 | Medium |
| 13 | Permissions tiered | G6.I1: permissions tiered by risk | G6 §Invariants | Partial | Write is present in allowed-tools. The skill explicitly scopes Write to `operations/audit-reports/` (Step 9). However, this scoping is prose-only and not expressed as a risk tier or enforced by path restriction in the harness. Bash is the higher-risk tool here (arbitrary command execution) but its risk tier is not classified. | G6 §Recovery | 1 | Medium |
| 14 | Trigger description quality | G8 trigger | G8 §Invariants | Satisfied | Description uses concrete consumer phrasings ("Full consistency check for IL system"). "When to Use" and "When NOT to Use" sections are both present and explicit. The NOT-to-use cases redirect to specific peer skills (`/system-health`, `/maintain-docs --update`). | — | 1 | High |
| 15 | ROLE/AUTHORITY/CONSTRAINT/FAILURE SIGNAL | G8.I6 | G8 §Invariants | Partial | ROLE is explicit ("Owner performing a thorough inspection"). CONSTRAINT is distributed across Rules. AUTHORITY is implicit (Owner agent's responsibility per DD-86, but FAILURE SIGNAL is not declared. No explicit statement of what signals a failed audit execution (vs. a completed audit with findings). | G8 §Recovery | 1 | Medium |
| 16 | DD-92 ContextSpec | DD-92 | DD-92 | Skipped | DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here. | — | — | — |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | G9.I6: report write confirmation | G9 §Invariants | Is the report write (Step 9) surfaced to the user before execution? The skill claims "Full Autonomy tier" but that designation does not exempt Write from G9.I6. Is there a rationale for why no confirmation is required? | Policy statement or skill update with explicit exemption rationale |
| b | G6.I2: structural enforcement of audit-only constraint | G6 §Invariants | Is there a harness-level restriction that prevents Write/Edit from targeting files outside `operations/audit-reports/`? Or is Rule 4 the sole enforcement? | Harness settings.json path restriction or tool-intercept hook |
| c | G3b.I2: state recovery | G3b §Invariants | If the audit is interrupted after Step 6 (mid-procedure), can it resume from Step 7, or must it restart from Step 1? | Documented resume path or checkpoint mechanism |
| d | G3b.I6: cost controls for Bash | G3b §Invariants | Bash can produce large output (e.g., deep directory listings). Is there a context-budget guard on Bash output consumed within the audit? | Harness-level Bash output limit or documented size-cap convention |
| e | G8.I7: prompt versioning | G8 §Invariants | Are changes to the audit procedure (which functions as the skill's "prompt") version-controlled and tested against a known system state? | Commit history or acceptance criteria for audit output |
| f | G5.I7: skill versioned | G5 §Invariants | Is the `system-audit` skill versioned and locked? | Lock file or version manifest |

---

### Aspects out of scope

| Guide | Why latent |
|-------|-----------|
| G1 Precondition: "non-trivial autonomous work" | Satisfied — 10-step procedure, multiple Bash + Glob + Grep + Read calls, Write. G1 fires fully. |
| G3b Precondition: "side effects or longer than single turn" | Satisfied — Write to `audit-reports/`, Bash with directory creation. G3b fires fully. |
| G9 Precondition: "destructive/irreversible actions" | Satisfied — Write and Bash (structural) in allowed-tools. G9.I6 fires. |

---

### Summary

G9.I6 outcome: **Violated.** The report write (Step 9) and directory creation (Step 10) are performed autonomously under the "Full Autonomy tier" designation, but this designation does not satisfy G9.I6 — which requires explicit human approval for destructive/irreversible actions regardless of trust level. The Write action produces a persistent file without user confirmation.

The most dangerous gap is the structural-enforcement finding (G6.I2, #11): Rule 4 ("No fixes during audit") is the skill's own most important safety constraint, but it is enforced only by prose. A Bash command that writes or an inadvertent Edit call during audit would violate this constraint without any structural backstop. This should be addressed by either removing Edit from the tool surface (it is not listed in allowed-tools — confirmed; Write and Bash are the concern) or adding a harness-level path restriction limiting Write to `operations/audit-reports/`.

Strong elements: trigger description quality, tool-surface discipline, "When NOT to Use" section, severity classification in the report template, and the explicit "no fixes during audit" principle.

---

### Skill: `systems/improvement-loop/.claude/skills/system-health/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 9, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** NON-safety-critical (Bash constrained to read-only by Rule 1)

**Critical:** F#3 Missing — no `## Boundary conditions` section per template skeleton; F#4 Partial — Bash scope (read-only constraint) is prose-only.

**G9.I6 outcome:** n/a — non-safety-critical.

**Top findings:**
- F#3 Missing: no `## Boundary conditions` section.
- F#4 Partial: Bash read-only constraint is prose-only (Rule 1), no structural enforcement.
- F#7 Satisfied: trigger description is well-formed.

---

### Skill: `systems/improvement-loop/.claude/skills/transcript-fetcher/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 9, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** safety-critical (Bash, Write)

**Critical:** F#4 Missing — safety-critical classification undeclared in boundary conditions section (which is also absent, F#3).

**G9.I6 outcome:** Partial — no explicit gate, but clobber-prevention structural (Step 1 dedup), low blast radius (additive transcript writes).

**Top findings:**
- F#3 Missing: no `## Boundary conditions` section.
- F#4 Missing: safety-critical declaration absent.
- F#10 Partial: FAILURE SIGNAL is the strongest in the batch (covers 404, network issues).
- F#11 Partial: transcript files themselves serve as durable state (strongest state story in batch).

---

### Skill: `systems/improvement-loop/.claude/skills/translate-governance/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 7, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

**mode: in-context-rubric** (assess-skill SKILL.md loaded; rubric applied directly)

**Classification: safety-critical (trigger: allowed-tools includes Write and Edit)**

**Artifact:** `systems/improvement-loop/.claude/skills/translate-governance/SKILL.md`
**Composed guides:** G1 (spec quality), G3b (workflow/execution), G5 (tool use), G6 (safety/permissions), G8 (prompt craft/trigger), G9 (governance — safety-critical; G9.I6 forced)
**Rubric size:** 17 file-verifiable invariants, 4 system/process-verifiable invariants, 0 latent

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Spec completeness | Every spec includes objective, desired outcomes, health metrics, constraints, autonomy levels, acceptance criteria, stop rules, context supply plan | G1.I1 | Partial | Objective is clear (translate governance into IL-specific docs). Rule 1 states autonomy tier (Guarded). No health metrics, no explicit acceptance criteria, no stop rules (halt/escalation/completion). "Calibration Notes" is informal guidance, not a structured spec section | G1 §Recovery | 1 | High |
| 2 | Hard constraints have enforcement outside prompt layer | Hard constraints must have enforcement mechanisms outside the prompt layer | G1.I2 | Partial | Rule 2 ("Never modify source governance — Read from meta-system/governance/ only") is a hard constraint stated in prose. There is no structural enforcement (e.g., allowed-tools does not scope Write/Edit to IL paths only; the constraint depends entirely on the model's compliance with Rule 2) | G1 §Recovery | 1 | High |
| 3 | Acceptance criteria evaluable by third party | Acceptance criteria are evaluable by a third party | G1.I3 | Missing | No acceptance criteria section. Completion is implied by Step 7 output (N created, N updated, drift detected/none), but no pass/fail criteria for translation quality or coverage are specified | G1 §Recovery | 1 | High |
| 4 | Stop rules: halt + escalation + completion | Stop rules include at least one halt, escalation trigger, completion criterion | G1.I4 | Missing | No stop rules defined. Neither halt conditions (e.g., "abort if `constitution.md` is unreadable") nor escalation triggers (e.g., "if source governance has changed fundamentally, escalate before translating") are specified. Completion is implied but not stated | G1 §Recovery | 1 | High |
| 5 | Explicit state tracking independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b.I1 | Missing | No state artifact is written until Step 6 (`_index.md` update) and Step 7 (conversation report). If the skill is interrupted after translating some documents but before others, there is no checkpoint. No intermediate state file is produced | G3b §Recovery | 1 | High |
| 6 | Iterative pattern has termination condition | Every iterative pattern has a termination condition | G3b.I2 | Partial | Steps 2-4 iterate over source governance files and existing translations. The iteration is bounded (finite file sets). However Step 3's extraction loop ("for each source document, identify clauses") is unbounded — no limit on the number of clauses to extract per source | G3b §Recovery | 1 | Low |
| 7 | Degradation modes defined | Degradation modes are defined before going live | G3b.I3 | Missing | No degradation modes defined. What happens when a source governance file has changed substantially and the translation would require a near-total rewrite? What happens if `Glob` returns zero existing translations on a non-empty `governance/` directory? These failure paths are unspecified | G3b §Recovery | 1 | High |
| 8 | Only tools needed loaded | Only tools needed for the current task are loaded | G5.I1 | Satisfied | `Read`, `Grep`, `Glob`, `Write`, `Edit` — all five are accounted for in the "Available Tools" table with explicit purpose mapping. No extraneous tools | G5 §Recovery | 1 | High |
| 9 | Tool descriptions designed for non-deterministic consumers | Tool descriptions persuade, disambiguate, explain when not to use | G5.I2 | Satisfied | Available Tools table maps each tool to a precise purpose. `Write` (create new translation documents) vs. `Edit` (update existing translations) is explicitly disambiguated — this is strong poka-yoke for a common error (recreating files and losing git history) | G5 §Recovery | 1 | High |
| 10 | Intermediate tool results outside context window when only final output needed | G5.I3 | Partial | Step 1 reads five governance source documents. For large constitutions, all five are held in context during the extraction phase. No strategy for progressive or staged reading is defined | G5 §Recovery | 1 | Low |
| 11 | Permissions tiered by risk | Permissions tiered by risk, not binary | G6.I1 | Partial | Rule 1 names "Guarded" autonomy tier for writes. However Write (create new files) and Edit (update existing, preserving git history) are not distinguished by risk tier within the skill. Edit on existing governance docs is lower-risk than Write (new files), but they carry the same implicit permission level | G6 §Recovery | 1 | Medium |
| 12 | Safety-critical constraints enforced structurally | Safety-critical constraints enforced structurally, not via prompt instructions alone | G6.I2 | Violated | Rule 2 ("Never modify source governance") is enforced via prose only. The `allowed-tools` declaration includes Write and Edit without path scoping. Nothing in the harness configuration restricts these tools to `systems/improvement-loop/governance/` paths. The structural enforcement is entirely absent | G6 §Recovery | 1 | High |
| 13 | Defense is layered | No single mechanism is the sole protection | G6.I4 | Violated | For the source-governance protection constraint, there is only one layer: Rule 2 prose. No structural layer (path-scoped permissions, hook, or pre-condition check against source paths) backs it up | G6 §Recovery | 1 | High |
| 14 | Destructive/irreversible actions require human approval | G9.I6: destructive or irreversible actions always require human approval | G9.I6 | Violated | Rule 1 states "Guarded tier — act then report. Do not wait for approval before writing governance translations." This is an explicit design choice to skip human approval before writing governance files. While the Guarded tier is a valid autonomy classification, the key G9.I6 concern is that governance translations are not trivially reversible in practice (they shape agent behavior). No dry-run option or diff-before-write step exists. The procedure writes files, then reports — the human sees the output after the fact, not before | G9 §Recovery: trust violation protocol | 1 | High |
| 15 | Trigger description fires reliably | Description phrased as consumer would ask; triggers reliably | G8.I1 | Satisfied | Description names five concrete trigger conditions (governance/ empty, source docs updated, new DD, periodic drift check, pre-system-audit). "When NOT to Use" section provides four clear exclusion cases | G8 §Recovery | 1 | High |
| 16 | Prompt carries explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | G8.I2 | Partial | ROLE (Owner, system steward) is explicit. CONSTRAINTS (never modify source, never create DDs, provenance is mandatory) are explicit. AUTHORITY is implied (DD-86) but not formally declared. FAILURE SIGNAL is absent — no statement of what invalid translation output looks like (e.g., "a translation that cannot cite its source section is a failure signal") | G8 §Recovery | 1 | Medium |
| 17 | High-priority behavioral rules as negative constraints | G8.I3 | Satisfied | Rules use negative form for load-bearing constraints: "Never modify source governance," "Never create DDs," "Preserve existing translations" | G8 §Recovery | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|---|---|---|---|
| a | Changes to permission configurations require review | G6 governance | Is there a review record for the Guarded-tier write decision (Rule 1) — specifically a documented rationale for why governance translations should bypass human pre-approval? | DD or design note with rationale |
| b | Audit trail maintained for all agent actions | G9 governance | Are writes made by this skill captured in git history with sufficient commit granularity to reconstruct what changed in a given run? | Git log review; commit message convention |
| c | Policy bundle versions are immutable once active | G9 governance | When a governance translation is updated, is the prior version preserved (git history + no in-place clobber of content)? Rule 4 says "Preserve existing translations — Update in place via Edit. Don't delete and recreate." Is this enforced beyond prose? | Git-history review; hook or CI check |
| d | Specs retained alongside agent output as audit records | G1 governance | Is there a governance snapshot (what the source docs said at translation time) stored alongside the translations, enabling future drift detection to compare against a known baseline rather than re-reading source docs that may have changed again? | Snapshot file in `governance/` |

---

### Aspects out of scope

| Guide | Why latent |
|---|---|
| G2a/G2b | No context-loading directives in skill prompt — G2a/G2b Preconditions unsatisfied |

---

### DD-92 ContextSpec audit

DD-92 ContextSpec audit skipped — no `context:` block in frontmatter. DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here.

---

### Summary

**G9.I6 outcome: Violated — act-then-report design skips human pre-approval for governance file writes.** This is the most significant finding. Rule 1 explicitly encodes "do not wait for approval before writing governance translations" — this is a deliberate design choice that conflicts with G9.I6's requirement that destructive or irreversible actions receive human approval. The secondary critical finding is G6.I2/G6.I4 Violated: Rule 2 ("never modify source governance") is enforced by prose only, with no structural path-scope restriction in `allowed-tools` or harness config. Additionally, acceptance criteria, stop rules, state tracking, and degradation modes are absent. The skill needs a `--dry-run` or diff-before-write step to satisfy G9.I6, and path-scoped Write/Edit permissions to satisfy G6.

---

### Skill: `systems/improvement-loop/.claude/skills/watch-blogs/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 8, fresh context, mode: in-context-rubric)*

## Audit — SKILL.md

mode: in-context-rubric (assess-skill SKILL.md loaded; rubric applied directly per procedure)

**Artifact:** `systems/improvement-loop/.claude/skills/watch-blogs/SKILL.md`
**Classification:** safety-critical (triggers: `allowed-tools` includes Write, Edit, Agent — Write creates new files; Edit mutates watched-blog entries; Agent spawns subagents with WebFetch and external-search access)
**Composed guides:** G1 (spec quality), G3b (workflow/termination), G5 (tool use), G6 (safety/permissions), G8 (prompt/trigger quality), G9 (governance — G9.I6 forced for safety-critical)
**Rubric size:** 14 file-verifiable invariants, 7 system/process-verifiable invariants, 1 latent (out-of-scope)

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | G9.I6 — HITL gate for destructive actions | Destructive or irreversible actions always require human approval regardless of trust level. | G9 §Invariants | Violated | Steps 4 and 5 execute Write (create new research-source entries) and Edit (update watched-blog entries, post log) **without a human approval gate**. The procedure flow is: Step 3 produces report → Step 4 auto-creates sources → Step 5 auto-updates blog entries. The only gate is `--dry-run` ("Stop here if `--dry-run` was specified" after Step 3), but dry-run is not the default when no flag is given ("--all: Check all active blogs in the registry. This is the default if no args are given"). The default execution path is fully autonomous Write+Edit. | Insert a human approval step between Step 3 (triage report) and Step 4 (Write). Restructure dry-run to be the default unless `--execute` is passed, or require explicit confirmation before any Write/Edit. Per G9 §Recovery: if an agent acts before approval, treat as governance incident. | 1 | High |
| 2 | G1 — Spec completeness: objective/desired outcomes | Spec includes objective and desired outcomes | G1 §Invariants | Satisfied | Description and "When to Use" together define the objective clearly. "Does not extract findings" and "Does not create authorities" are good negative-space scoping. | — | 1 | High |
| 3 | G1 — Stop rules: halt condition | Stop rules include at least one halt condition | G1 §Invariants | Missing | No halt condition for the non-dry-run path. No abort criterion defined if subagent execution fails for a blog (e.g., all three fetch methods fail). The skill says "blog_status: dead" updates `status` to `retired` but there is no explicit procedure for when a majority of blogs are unreachable. | Add: "If all three discovery methods fail for a blog (RSS, Perplexity, WebFetch), log that blog as `fetch-failed` in the triage report and skip without modifying the blog entry." | 1 | High |
| 4 | G1 — Stop rules: escalation trigger | Stop rules include at least one escalation trigger | G1 §Invariants | Missing | No escalation trigger is defined. If EXTRACT count is unusually high (e.g., 30 new posts across blogs), the skill will attempt to create 30 research-source files without pausing. | Add: "If EXTRACT count exceeds a threshold (e.g., 10 posts), surface the full report and ask the user to confirm before creating all source files." | 1 | Medium |
| 5 | G1 — Acceptance criteria evaluable by third party | Acceptance criteria are evaluable by a third party without access to the prompter's intent | G1 §Invariants | Missing | No acceptance criteria section. The "Calibration Notes" section contains judgment heuristics ("lean toward EXTRACT when uncertain") but no pass/fail criteria. | Add: "Success: triage report written to operations/research-reports/, all EXTRACT-verdict posts have corresponding research-source entries, all checked blog entries have updated last_checked_date." | 1 | High |
| 6 | G3b — Termination condition for iterative patterns | Every iterative pattern has a termination condition | G3b §Invariants | Partial | Parallel subagent dispatch (Step 2: "batches of 3-4") iterates over the blog list. Termination is implicit (list exhausted). However, the subagent prompt template itself has an iterative loop ("try in order, stop when you have results") — this has an explicit stop ("stop when you have results") which is good. The outer blog loop has no explicit count or timeout limit. | Acceptable for current KB size; flag as system-verifiable for large blog registries. | 1 | Medium |
| 7 | G3b — Explicit state tracking independent of conversation | Every workflow has explicit state tracking independent of conversation history | G3b §Invariants | Partial | The triage report (Step 3) is saved to a named path: `systems/improvement-loop/operations/research-reports/{date}-watch-blogs-triage.md`. This is good state persistence. However, if the skill is interrupted after Step 4 (sources created) but before Step 5 (blog entries updated), the state is inconsistent — sources exist without the blog's post log being updated. No recovery from partial execution is described. | Add an idempotency note: "If interrupted after Step 4, Step 5 can be re-run; duplicate post-log entries should be avoided by checking existing entries before appending." | 1 | Medium |
| 8 | G5 — Minimal tool surface | Only tools needed for the current task are loaded | G5 §Invariants | Partial | `allowed-tools: Read Grep Glob Edit Write WebFetch Agent`. The Agent tool is broad — it spawns subagents that in turn use WebFetch (and by the subagent prompt template, Perplexity search). The Agent tool grants the subagent the full tool surface available to the parent. This is a tool over-grant risk: the subagent prompt template only needs WebFetch and Perplexity search, but the spawned Agent inherits the parent's full allowed-tools. | Specify that subagent spawning is scoped to WebFetch + search only. If possible, use the Agent tool with a restricted tool list. | 1 | Medium |
| 9 | G5 — Skill scoped to workspace and task type | Skills scoped to workspaces/task types, not loaded globally, when surface exceeds 5 capabilities | G5 §Invariants | Satisfied | This skill is IL-scoped, not globally loaded. | — | 1 | High |
| 10 | G6 — Permissions tiered by risk | Permissions tiered by risk, not binary allow/deny | G6 §Invariants | Partial | Read/Grep/Glob are correctly separated from Write/Edit. The `--dry-run` flag provides a soft tier gate. However, as noted in finding #1, the default execution path is not dry-run — Write and Edit are default-on, not default-off. Risk tiering should default to the less-destructive path. | Invert default: require `--execute` flag (or explicit confirmation prompt) to proceed past the triage report. | 1 | High |
| 11 | G6 — Defense is layered | Defense is layered — no single mechanism is sole protection | G6 §Invariants | Violated | The sole protective layer is the `--dry-run` flag, which is not the default. The subagent path (Agent tool) adds a second vector where external fetch results are written to KB files without secondary review. No rollback guidance, no partial-run recovery, no dedup check for Write operations (what happens if the same post is processed twice?). | Add: (a) explicit dedup check before Write in Step 4, (b) rollback note referencing git revert, (c) consider making `--dry-run` the default and requiring `--execute` for file-mutating operations. | 1 | High |
| 12 | G8 — Trigger description quality | Description phrases the trigger the way a consumer would ask | G8 §Invariants | Satisfied | "Monitor watched blogs for new posts relevant to the research pipeline" — clear, action-verb-fronted, consumer-phrasing-aligned. Trigger conditions in "When to Use" are concrete. | — | 1 | High |
| 13 | G8 — ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, FAILURE SIGNAL | G8 §Invariants | Partial | The subagent prompt template has implicit role ("You are checking a blog/publication...") and implicit constraints (the "Filter" step). However no explicit AUTHORITY, CONSTRAINT, or FAILURE SIGNAL are declared in the parent skill body. The subagent template is better structured than the parent skill in this regard. | Low-impact: the subagent template has sufficient role/constraint framing. The parent could benefit from an explicit constraints section. | 1 | Low |
| 14 | DD-92 ContextSpec | `context:` block absent | DD-92 | N/A (skipped) | No `context:` block in frontmatter. DD-92 ContextSpec audit skipped — DD-92 binds extracted and deployed artifacts; consumer-submitted artifacts without ContextSpec are not flagged here. | — | — | — |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|------------------|
| a | Degradation modes defined before go-live | G3b §Invariants | If Perplexity search is unavailable (rate limit, API failure) and WebFetch returns 403s for a blog, does the skill degrade gracefully, or does it silently produce no results for that blog? | Evidence: test run with a mocked unavailable blog; confirmed behavior |
| b | Cost controls before autonomous execution | G3b §Invariants | The Agent tool spawns parallel subagents (batches of 3-4). For an `--all` run across 20+ blogs, what is the estimated token cost? Is there a per-run budget? | Evidence: cost estimate per blog; harness budget configuration |
| c | Agent cannot modify its own permission configuration | G6 §Invariants | Are the subagents spawned in Step 2 constrained to IL paths only for any write operations? Can a subagent write to paths outside `research-sources/` and `watched-blogs/`? | Evidence: harness tool-path restrictions for the Agent subagent invocation |
| d | Audit trail for agent actions | G9 §Invariants | Are the Write and Edit operations logged (system log entry or git commit) after each run, so that post-hoc audit is possible? | Evidence: SL entry or git commit created after watch-blogs run |
| e | Subagent tool surface restriction | G5 §Invariants | Is the Agent tool invocation in Step 2 restricted to WebFetch + Perplexity search only, or does the spawned subagent inherit the full parent tool surface (including Write/Edit)? | Evidence: harness subagent configuration or Agent tool call with explicit tool restrictions |
| f | Stable prompt layers cached | G8 §Invariants | Is the stable part of the subagent prompt template (blog metadata, relevance filter) cached to avoid re-tokenizing it for each of the 3-4 parallel subagents? | Evidence: caching configuration or observed cache-hit rate |
| g | Prompt versioning and testing | G8 §Invariants | Is the subagent prompt template versioned? If the relevance filter heuristics or verdict definitions change, is there a test to confirm the subagents still produce correct JSON output? | Evidence: version field or changelog entry; test transcript |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G9 (beyond I6) | G9 broader invariants require a multi-decision-type agent system with a trust ledger. This is a single-purpose monitoring skill. G9.I6 fires unconditionally; remaining G9 invariants are latent. |

---

### Summary

G9.I6: **Violated.** This is the load-bearing finding. Steps 4 and 5 execute Write and Edit without a human approval gate on the default execution path. The `--dry-run` flag provides an opt-out, but the default execution is autonomous mutation of the KB. This skill **must not be used against production KB data** until a HITL gate is inserted between Step 3 (triage report review) and Step 4 (source creation), or until dry-run is made the default and `--execute` is required for file-mutating operations.

Additional high-priority findings:
- Finding #3: No halt condition for fetch failures.
- Finding #5: No acceptance criteria — success is not third-party verifiable.
- Finding #11: Defense is single-layer; no rollback guidance, no Write dedup guard.

Tool surface (finding #8) and permission default (finding #10) are medium-priority design corrections.

No DD-92 ContextSpec findings — `context:` block absent; check not applicable.

---

### Skill: `systems/improvement-loop/.claude/skills/watch-upstream/SKILL.md`
*Assessed via /assess-skill (Librarian subagent bin 9, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** safety-critical (Write, Edit, Agent)

**Critical:** **G9.I6 VIOLATED** — Step 4 executes `Edit` on watched-library entries automatically after triage with no HITL gate between subagent output (Step 2) and file mutation (Step 4); `--dry-run` is the only guard.

**G9.I6 outcome:** Violated — no human approval between automated triage and execution path.

**Top findings:**
- F#1 Violated G9.I6: no HITL between triage and Edit execution.
- F#3 Missing: no `## Boundary conditions` / stop rules / GH rate-limit halt.
- F#11 Violated G6.I1: flat `allowed-tools` list with no risk tiering.
- F#4 Partial: subagent `Agent` tool grants unrestricted subagent tool access.

---

## Agents (fractal)

### Agent (fractal): `systems/improvement-loop/agents/codifier/agent.md`
*Assessed via /assess-agent (Librarian subagent bin 1, fresh context, mode: in-context-rubric)*

## Audit — Agent

**Artifact:** `systems/improvement-loop/agents/codifier/agent.md`
**mode:** in-context-rubric
**Interpreted as:** verb: audit, noun: agent, variant: A+B (prompt-based + harness-based — the Codifier has an enumerated skill inventory with write operations and bounded workflow, placing it in Variant B territory alongside the base Variant A prompt-based spec).
**Tier trace:** Read 7 Tier-1 Contract sections (G1, G2a, G2b, G3, G3b, G5, G10); 0 Tier-2 findings consulted; 0 Tier-3 reads. G6 and G9 read for partial applicability.

**Composed guides (Variant A+B):** G1 `writing-agent-specifications.md`, G2a `structuring-agent-context.md`, G2b `defending-agent-context.md`, G3 `agent-architecture-decisions.md`, G3b `agent-workflow-and-execution.md`, G5 `designing-agent-tools.md`, G10 `agent-design-patterns.md`. G6 and G9 applied with Precondition notes.

**Rubric size:** 26 file-verifiable invariants checked; 8 system/process-verifiable invariants → follow-ups; 1 guide latent (G7 — no multi-session persistence requirement; G9 partially applicable for destructive-action check).

**DD-92 ContextSpec audit:** No `context:` block present in frontmatter. DD-92 ContextSpec audit skipped — DD-92 binds extracted and deployed artifacts; artifacts without ContextSpec are not flagged here. The frontmatter carries IL classification metadata (`confidence: "HIGH"`, `tier: "auto"`, `reason_codes`, `co_occurrence: null`) — informational finding below.

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Spec completeness — objective and outcomes | Every agent spec includes at minimum: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, stop rules, context supply plan | G1.Invariants | Partial | Objective present (§Scope). Constraints stated (Boundaries section). Autonomy levels: no explicit Autonomy Table in spec (unlike Owner). Acceptance criteria: absent. Stop rules: absent. Health metrics: absent. Context supply plan: §Continuity names three boot reads but no tiered supply plan. | G1 §Recovery | 1 | High |
| 2 | Hard constraint enforcement outside prompt layer | Hard constraints have enforcement mechanisms outside the prompt layer | G1.Invariants | Missing | Write boundaries ("NEVER write outside extracts/, operations/, project-management/design-notes/, agents/codifier/reflections/") stated in prompt only. No harness-level file permission enforcement described. | G1 §Recovery | 1 | High |
| 3 | Templates filled completely | No placeholder TBD/TODO fields | G1.Invariants | Satisfied | No placeholder fields found across all sections. | — | 1 | High |
| 4 | Acceptance criteria evaluable by third party | Acceptance criteria are evaluable by a third party without access to the prompter's intent | G1.Invariants | Missing | No acceptance criteria section. Contract §Invariants states behavioral invariants but not testable pass/fail criteria. | G1 §Recovery | 1 | High |
| 5 | Context elements justifiable | Every context element has a justifiable reason for being there | G2a.Invariants | Partial | §Continuity states three boot reads (guide routing table, last identification report, PROGRESS.md). No justification distinguishing always-on vs. on-demand; no token budget consideration stated. | G2a §Recovery | 1 | Medium |
| 6 | Tiered loading | Tiered loading preserves token budget | G2a.Invariants | Missing | No tiered context loading strategy described. Three boot reads are listed as always-on without a minimal-upfront architecture. | G2a §Recovery | 1 | Medium |
| 7 | Session boundary reset | Session boundaries reset degradation | G2b.Invariants | Partial | State persistence is via identification reports and guide reports (§Continuity). Sessions are bounded by report artifacts. However, no explicit compaction strategy or session discipline for long classification runs. | G2b §Recovery | 1 | Medium |
| 8 | Single-agent default respected | Single-agent is the default until empirical evidence justifies multi-agent | G3.Invariants | Satisfied | The Codifier is a single-agent with no sub-agent delegation. | — | 1 | High |
| 9 | Four-zone decomposition | Every agent decomposes into four zones (trigger, context, tools, output/memory) | G3.Invariants | Partial | Trigger: §Disposition (invoked by skill). Context: §Continuity. Tools: §Skill Inventory (3 skills). Output/Memory: §Communication §Output artifacts. Zones present but not explicitly labeled; memory zone is thin (session records in operations/ only). | G3 §Recovery | 1 | Medium |
| 10 | Model selection stated | Model selection is task-based, not provider-based | G3.Invariants (merged G3.I4/G8.I4) | Missing | No model selection statement in spec. The CLAUDE.md notes "67% Sonnet accuracy" in memory context but the agent spec itself is silent on model routing. | G3 §Recovery | 1 | High |
| 11 | Every workflow has explicit state tracking | Every workflow has explicit state tracking independent of conversation history | G3b.Invariants | Partial | Identification reports and guide reports in operations/ serve as session records. §Continuity: "Identification reports and guide reports in operations/ are the session records." This covers state tracking but is implicit — no explicit checkpoint mechanism described. | G3b §Recovery | 1 | Medium |
| 12 | Every iterative pattern has termination condition | Every iterative pattern has a termination condition (loop limit, stall detection, or both) | G3b.Invariants | Missing | No termination conditions stated for classification loops, extraction runs, or synthesis cycles. | G3b §Recovery | 1 | High |
| 13 | Cost controls before autonomous execution | Cost controls (budgets, termination rules, caching, fast-fail) in place before autonomous execution | G3b.Invariants | Missing | No cost control mechanisms described. All three skills are "Guarded" (human review before deployment) but no per-step budget or stall detection described. | G3b §Recovery | 1 | Medium |
| 14 | Delivery chunk size calibrated | Delivery chunk size calibrated to reviewer capacity, not agent production speed | G3b.Invariants | Partial | §Disposition: "Intent-dependent gaps (ask Nick): 'Should this guide be split given 25+ findings?'" — suggests chunk-size awareness but not a specified calibration. | G3b §Recovery | 1 | Low (implied by check-in behavior, not explicit) |
| 15 | Tool definitions are data first | Tool definitions are data first — metadata exists before implementation | G5.Invariants | Partial | Skills are listed in §Skill Inventory with purpose, autonomy, pipeline stage. Metadata present. However, the skills are procedural skill documents, not tool definitions in the function-calling sense. G5 applies at the level of the skill contract, not at the level of harness tools. | G5 §Recovery | 1 | Low (G5 applicability borderline for skill-based agents vs. API-tool-using agents) |
| 16 | Only tools needed for current task loaded | Only tools needed for the current task are loaded into context | G5.Invariants | Partial | §Skill boundary rules state each skill reads only its needed inputs ("reads findings but does NOT modify their content"). This implies scoped tool use. But the spec does not state a tool-loading mechanism — skills are loaded via invocation, not explicitly scoped at the context level. | G5 §Recovery | 1 | Low |
| 17 | Skills are framework-agnostic | Skills are framework-agnostic markdown files portable across SDKs | G5.Invariants | Satisfied | Skills are defined as SKILL.md files per IL convention. Framework-agnostic. | — | 1 | High |
| 18 | Identity defined separately from capabilities | Agent identity (constitution) is defined in a separate, stable layer from capabilities | G10.Invariants | Satisfied | §Constitution is a distinct section from §Skill Inventory. Clear separation. | — | 1 | High |
| 19 | Clarification behavior distinguishes resolvable from intent-dependent | Clarification behavior distinguishes resolvable gaps from intent-dependent gaps | G10.Invariants | Satisfied | §Disposition explicitly distinguishes "Resolvable gaps (fill autonomously)" from "Intent-dependent gaps (ask Nick)" with concrete examples for each. | — | 1 | High |
| 20 | No agent exists solely to review another's output | No agent exists solely to review another agent's output | G10.Invariants | Satisfied | The Codifier is a classification and extraction agent, not a review agent. | — | 1 | High |
| 21 | All five prompt layers addressed | All five prompt layers addressed — skipped layers documented | G10.Invariants | Partial | Five-layer architecture not explicitly mapped in the spec. Sections present (Constitution, Disposition, Scope, Skill Inventory, Communication, Contract) but not mapped to the five-layer framework; no intentional omissions documented. | G10 §Recovery | 1 | Medium |
| 22 | Autonomy table present | No decision type defaults to full autonomy without explicit classification | G10.Invariants / agent.md template | Missing | No explicit Autonomy Table in this spec (unlike the Owner agent). Skill Inventory lists autonomy per skill ("Guarded") but the template's Autonomy Table covering all action types is absent. | agent.md concept §Template skeleton | 1 | High |
| 23 | Agent-level constraints enforced structurally | Safety-critical constraints enforced structurally, not via prompt instructions alone (G6 — partially applicable: Codifier writes files) | G6.Invariants | Missing | Write boundaries are stated only in the prompt (§Boundaries). No structural enforcement at harness/OS layer described. Codifier has write access to multiple directories — structural gating of this write access is not documented. | G6 §Recovery | 1 | High |
| 24 | Agent cannot modify its own permission configuration | The agent cannot modify its own permission configuration | G6.Invariants | Satisfied | §Governance in Contract: "Codifier cannot modify its own skill definitions or CLAUDE.md." Explicit stated constraint. | — | 1 | High |
| 25 | Frontmatter carries IL classification metadata (informational) | IL pipeline metadata should be stripped at deploy boundary | Informational | Informational | Frontmatter contains `confidence: "HIGH"`, `tier: "auto"`, `reason_codes`, `co_occurrence: null`. `deployed: false` — deployment gate has not fired. Pre-deploy state is acceptable but metadata must be stripped before deployment. | DD-92 §Check 3 (analogous) | 1 | High |
| 26 | Recovery section present and addresses write failures | Contract §Recovery covers write-related failures | G1.Invariants | Partial | Recovery covers form misclassification, low-quality extraction, guide synthesis misses. Does not address: filesystem write failure, partial batch completion, tool unavailability. | G1 §Recovery | 1 | Medium |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | Hard constraints enforced outside prompt layer | G1.Invariants | Is there a harness-level permission configuration (e.g., `.claude/settings.json`, filesystem ACLs) that enforces the Codifier's write boundaries at runtime? | Harness settings config showing path restrictions |
| b | Stable context is cached | G2b.Invariants | Is the stable portion of context (guide routing table, last identification report) loaded with prompt caching? What is the cache-hit rate? | Caching config; cache-hit telemetry |
| c | Workflow state tracked independently of conversation | G3b.Invariants | For long classification or extraction runs, is workflow state checkpointed to a file before each major step, independently of Claude Code's conversation history? | Checkpoint file examples or session records |
| d | Cost controls in place | G3b.Invariants | Are there per-step token budgets or batch-size limits governing identification or extraction runs? What triggers a cost escalation alert? | Budget config; batch size definition |
| e | Termination conditions for iterative patterns | G3b.Invariants | What is the loop limit for /identify-artifacts runs over large finding sets? What stall detection exists if a finding cannot be classified? | Documented termination logic in skill SKILL.md |
| f | Architecture decision documented | G3.Governance | Is there a DD documenting the decision to keep the Codifier as a single-agent with three skills vs. decomposing into separate classifier and extractor agents? | DD reference |
| g | Model routing | G3.Invariants | What model is used for classification vs. extraction vs. synthesis? Is model selection task-based per the skill (e.g., Sonnet for classification, Opus for synthesis)? | Skill SKILL.md or harness config showing model routing |
| h | Tool permission enforcement | G6.Preconditions | Are the Codifier's skills run with OS-level or harness-level sandboxing that prevents writes outside the allowed directories? | Sandbox config or filesystem permission audit |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G7 (`session-persistence-and-memory.md`) | Codifier produces session records (identification reports) but does not span multiple sessions with persistent memory. G7 Preconditions require an agent that persists beyond a single prompt-response cycle in a stateful sense. The Codifier restarts from scratch each session. G7 latent. |
| G9 (`agent-governance-and-trust.md`) | G9.I6 (destructive-action check) was evaluated: Codifier does not perform destructive actions (it stages, not deploys; it does not delete). Full G9 audit scope is Variant C only. G9 latent except for G9 governance cross-check which is reflected in findings #2 and #23 above. |

---

### Summary

**Solid:** Clarification behavior is explicitly defined and well-structured (#19), identity-capability separation is clean (#18), write boundaries are stated (#24 — "cannot modify own skill definitions"), the Codifier cannot modify its own governance (#24), and the three-skill inventory is coherently scoped with autonomy levels per skill.

**Load-bearing to fix:** No Autonomy Table in the spec (#22), missing acceptance criteria (#21/finding #4), no model selection statement (#10), no termination conditions for iterative classification loops (#12), and no structural enforcement of write boundaries (#2, #23). These represent the most significant gaps relative to the template skeleton and G1/G6 invariants.

**Hinges on consumer follow-up:** Whether harness-level write enforcement exists (follow-up a, h), whether workflow checkpointing is in place (follow-up c), and model routing decisions (follow-up g) are the open questions. The IL classification metadata in frontmatter (#25) must be stripped before deployment.

---

### Agent (fractal): `systems/improvement-loop/agents/librarian/agent.md`
*Assessed via /assess-agent (Librarian subagent bin 1, fresh context, mode: in-context-rubric)*

## Audit — Agent

**Artifact:** `systems/improvement-loop/agents/librarian/agent.md`
**mode:** in-context-rubric
**Interpreted as:** verb: audit, noun: agent, variant: A (prompt-based).
**Tier trace:** Read 5 Tier-1 Contract sections (G1, G2a, G2b, G3, G10); 0 Tier-2 findings consulted; 0 Tier-3 reads.

**Composed guides (Variant A):** G1 `writing-agent-specifications.md`, G2a `structuring-agent-context.md`, G2b `defending-agent-context.md`, G3 `agent-architecture-decisions.md`, G10 `agent-design-patterns.md`

**Rubric size:** 21 file-verifiable invariants checked; 7 system/process-verifiable invariants → follow-ups; 4 guides latent (G3b, G5, G6, G9 — Preconditions unsatisfied for this prompt-only agent)

**DD-92 ContextSpec audit:** No `context:` block present in frontmatter. DD-92 ContextSpec audit skipped — DD-92 binds extracted and deployed artifacts; artifacts without ContextSpec are not flagged here. However, the frontmatter carries IL classification metadata (`confidence: "MED"`, `tier: "guided"`, `reason_codes`, `co_occurrence: null`) which is IL-internal pipeline metadata and should be stripped at the deploy boundary. This is not a DD-92 gate violation (no `context:` block present to trigger Check 3) but is surfaced as an informational finding below.

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Spec completeness — objective and outcomes | Every agent spec includes at minimum: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, stop rules (all three types), and a context supply plan | G1.Invariants | Partial | Objective present (§Scope). Desired outcomes implied. Health metrics: absent. Acceptance criteria: absent. Stop rules (halt/escalation/completion): absent. Context supply plan: implicit (§Continuity mentions session boot reads). | G1 §Recovery — if spec was adequate and agent fails, review for missing fields | 1 | High |
| 2 | Hard constraint enforcement outside prompt layer | Hard constraints have corresponding enforcement mechanisms outside the prompt layer | G1.Invariants | Missing | Read-only invariant is stated in the Constitution ("NEVER write to any IL directory") and frontmatter Contract but no structural enforcement mechanism is identified — no harness-level permission config, no hook, no runtime guard described | G1 §Recovery | 1 | High |
| 3 | Templates filled completely | Templates are filled in completely — no placeholder fields left as TBD or TODO | G1.Invariants | Satisfied | No TBD/TODO placeholders detected across all sections | — | 1 | High |
| 4 | Context structure — justifiable elements | Every context element loaded into the agent's window has a justifiable reason for being there | G2a.Invariants | Partial | §Continuity specifies guide routing table and PROGRESS.md at session boot. §Communication enumerates input artifacts. No explicit justification for which elements are always-on vs. on-demand; tiering not specified. | G2a §Recovery | 1 | Medium |
| 5 | Tiered loading preserves token budget | Tiered loading preserves token budget — always-on context is minimal, everything else loaded on demand | G2a.Invariants | Missing | No tiered loading strategy described. §Continuity states "session boot: read guide routing table and PROGRESS.md" as always-on, but no explicit tier architecture distinguishing minimal upfront from on-demand. | G2a §Recovery | 1 | Medium |
| 6 | Context for sub-agents is scoped | Sub-agents receive scoped context appropriate to their task, not the parent's full window | G2a.Invariants | Latent | The Librarian does not spawn sub-agents. Invariant not applicable. | — | 1 | High |
| 7 | Memory files have hard ceilings | Memory files have hard ceilings with tiered hot/warm/cold architecture | G2a.Invariants | Satisfied (partial) | §Continuity states "stateless across sessions — no persistent Librarian-specific state." No memory files to ceiling. The narrow exception (`agents/librarian/reflections/`) has no ceiling stated, but this is agent-private and the scope is limited. | — | 1 | Medium |
| 8 | Context quality defense — degradation acknowledged | Context quality degrades over time unless actively defended | G2b.Invariants | Missing | No mention of context degradation defense strategy. The Librarian is declared stateless, which implicitly prevents accumulation, but no explicit defense mechanism is described. | G2b §Recovery | 1 | Low (agent is stateless so degradation is structurally mitigated; but the spec does not explain this reasoning) |
| 9 | Session boundary reset | Session boundaries reset degradation — strongest defense is not letting degradation accumulate | G2b.Invariants | Satisfied | §Continuity: "The Librarian is stateless across sessions — it re-reads the KB each time." Session boundary reset is the operational model. | — | 1 | High |
| 10 | Architecture decision — single vs. multi-agent | Single-agent is the default until empirical evidence justifies multi-agent | G3.Invariants | Satisfied | The Librarian is a single-agent with no sub-agent spawning. No multi-agent decomposition proposed without justification. | — | 1 | High |
| 11 | Four-zone decomposition | Every agent decomposes into four zones (trigger, context, tools, output/memory); zones are specified, not hidden | G3.Invariants | Partial | Trigger: §Disposition (Teacher/Builder activation by query type — present). Context: §Continuity (partially). Tools: §Skill Inventory (listed). Output/memory: §Communication (outputs = conversational, no files). Zones present but not explicitly labeled as zones; output/memory zone is thin (no memory zone at all). | G3 §Recovery | 1 | Medium |
| 12 | Model selection is task-based, not provider-based | Model selection is task-based and tier-aware, not provider-based or prestige-based | G3.Invariants (merged G3.I4/G8.I4) | Missing | No model selection statement anywhere in the spec. | G3 §Recovery | 1 | High |
| 13 | Agent identity defined separately from capabilities | Agent identity (constitution) is defined in a separate, stable layer from capabilities (skills/tools), and survives context compaction via structural pinning | G10.Invariants | Partial | Constitution section exists and is separate from Skill Inventory. However, no explicit statement about structural pinning for context compaction survival. | G10 §Recovery | 1 | Medium |
| 14 | All five prompt layers addressed | All five prompt layers are explicitly addressed — skipped layers are documented as intentional omissions | G10.Invariants | Partial | Not all five layers are named or mapped. The spec has Constitution, Disposition, Scope, Skill Inventory, Communication, Contract — but does not trace these to the five-layer architecture or document which layers are intentionally omitted. | G10 §Recovery | 1 | Medium |
| 15 | Clarification behavior distinguishes resolvable from intent-dependent gaps | Clarification behavior distinguishes resolvable gaps from intent-dependent gaps | G10.Invariants | Partial | §Vibe specifies "don't pad" and "answer what was asked" but no explicit clarification protocol distinguishing resolvable from intent-dependent. No check-in rate guidance. | G10 §Recovery | 1 | Medium |
| 16 | No agent exists solely to review another's output | No agent exists solely to review another agent's output — quality is at the source | G10.Invariants | Satisfied | The Librarian is a consumption-layer query agent, not a review-only agent. | — | 1 | High |
| 17 | Subagent variants honor isolation | Subagent variants honor isolation by default — every dependency is explicit in frontmatter or prompt body | G10.Invariants | Not applicable | Librarian does not spawn subagents. | — | 1 | High |
| 18 | Autonomy table present and covers decision types | No decision type defaults to full autonomy without explicit classification (G9 analog — latent for Variant A, but the G10 autonomy envelope applies) | G10.Invariants | Missing | No Autonomy Table present. The spec defines read-only invariant and "Output artifacts produced: None" but does not enumerate decision types with autonomy classifications. The concept template requires an Autonomy Table even for common-core agents. | agent.md concept §Template skeleton | 1 | High |
| 19 | Recovery section present and concrete | Contract §Recovery present with concrete recovery paths | G1.Invariants (contract completeness) | Partial | Contract §Recovery present but brief: covers KB-miss, stale content, broken references. Does not address tool failure, context exhaustion, or session interruption. | G1 §Recovery | 1 | Medium |
| 20 | Frontmatter carries IL classification metadata (informational) | IL pipeline metadata (confidence, tier, reason_codes) should be stripped at deploy boundary | Informational — DD-92 context absent; not a gated violation | Informational | Frontmatter contains `confidence: "MED"`, `tier: "guided"`, `reason_codes: [...]`, `co_occurrence: null`. These are IL-internal pipeline fields. The artifact is marked `deployed: false` so deployment gate has not fired yet, but the metadata signals this is a raw extraction, not a deploy-ready artifact. | DD-92 §Check 3 (analogous) | 1 | High |
| 21 | Acceptance criteria evaluable by third party | Acceptance criteria are evaluable by a third party without access to the prompter's intent | G1.Invariants | Missing | No acceptance criteria section. Contract §Invariants states behavioral invariants but not testable acceptance criteria. | G1 §Recovery | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | Hard constraints enforced outside the prompt layer | G1.Invariants | Is there a harness-level permission configuration (e.g., `.claude/settings.json` allowlist/denylist, hook script) that enforces the Librarian's read-only boundary at runtime, not just in the prompt? | Harness settings config; hook script that intercepts write operations |
| b | Stable context is cached | G2b.Invariants | Is the stable portion of context (guide routing table, PROGRESS.md) loaded with prompt caching enabled? What is the observed cache-hit rate for the Librarian's session-boot reads? | Caching config; observed cache-hit rate |
| c | Token usage is measurable | G2a.Preconditions | Is token usage per Librarian call measured? Has context size at session boot been audited against the token budget? | Token count telemetry or spot-check |
| d | Compaction timing defined | G2b.Invariants | For long Librarian sessions spanning many KB reads, is there a compaction trigger defined? What is the session-length threshold before proactive compaction? | Session discipline config or documented threshold |
| e | Architecture decision documented | G3.Governance | Is there a DD or equivalent record documenting the decision to keep the Librarian as a single non-delegating agent rather than decomposing into sub-agents? | DD reference or design note |
| f | Harness-determinism position is deliberate | G3.Invariants | Is the Librarian's harness position (generic Claude Code) a deliberate decision tied to an explicit reliability requirement, or a default? | Design note or DD |
| g | Complexity audit cadence | G10.Governance | Is there a scheduled audit comparing the Librarian's harness configuration against current model capabilities, to detect over-engineering? | Audit record or schedule |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G3b (`agent-workflow-and-execution.md`) | Preconditions require a workflow with side effects or multi-turn execution. The Librarian is stateless, read-only, and produces no persistent output. G3b Preconditions unsatisfied. |
| G5 (`designing-agent-tools.md`) | Preconditions require tools the agent invokes via function calling/MCP/CLI. The Librarian uses Read/Glob/Grep navigational tools; these are harness-native read tools, not custom tool definitions. G5 Preconditions are borderline — latent pending confirmation that no custom tool definitions exist. |
| G6 (`agent-safety-and-permissions.md`) | Preconditions require an agent system that executes actions with side effects. The Librarian is read-only. G6 Preconditions unsatisfied. |
| G9 (`agent-governance-and-trust.md`) | Variant A agent. G9 is load-bearing for Variant C (autonomous agents with HITL gates). The Librarian has no autonomy envelope beyond passive read queries. G9 latent for this variant. |

---

### Summary

**Solid:** Single-agent design is justified (finding #10), session-boundary-based context defense is structurally implemented via statelessness (finding #9), identity/capability separation is present (finding #13), and boundary constraints are explicitly stated in the Constitution (finding #3).

**Load-bearing to fix:** The spec is missing an Autonomy Table (#18), acceptance criteria (#21), health metrics and stop rules (#1), and a model selection statement (#12). These are template-mandatory sections per the agent concept's common-core skeleton. The read-only hard constraint relies solely on the prompt layer — no structural enforcement identified (#2).

**Hinges on consumer follow-up:** Whether harness-level read-only enforcement exists (follow-up a) is the most consequential open question. Context caching efficiency (follow-ups b, c) affects operating cost. The IL classification metadata in frontmatter (#20) should be stripped before deployment.

---

### Agent (fractal): `systems/improvement-loop/agents/owner/agent.md`
*Assessed via /assess-agent (Librarian subagent bin 1, fresh context, mode: in-context-rubric)*

## Audit — Agent

**Artifact:** `systems/improvement-loop/agents/owner/agent.md`
**mode:** in-context-rubric
**Interpreted as:** verb: audit, noun: agent, variant: A+C (prompt-based + autonomous-vs-supervised — the Owner has an explicit Autonomy Table with tiered HITL gating across all action types, and spans sessions as the default persona).
**Tier trace:** Read 7 Tier-1 Contract sections (G1, G2a, G2b, G3, G9, G10); G7 read for partial applicability; 0 Tier-2 findings; 0 Tier-3 reads.

**Composed guides (Variant A+C):** G1 `writing-agent-specifications.md`, G2a `structuring-agent-context.md`, G2b `defending-agent-context.md`, G3 `agent-architecture-decisions.md`, G7 `session-persistence-and-memory.md`, G9 `agent-governance-and-trust.md`, G10 `agent-design-patterns.md`

**Rubric size:** 27 file-verifiable invariants checked; 8 system/process-verifiable invariants → follow-ups; 2 guides latent (G3b, G5 — Owner's workflow is advisory/proposal-only, no automated execution pipelines; no custom tool definitions).

**DD-92 ContextSpec audit:** No `context:` block present in frontmatter. Frontmatter schema is clean (`title`, `type`, `target_system`, `tags`, `created`, `updated`, `source_dd`) — no IL classification metadata (`confidence`, `tier`, `reason_codes`) detected. DD-92 ContextSpec audit skipped. No informational metadata leak to flag.

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Spec completeness — objective and outcomes | Every agent spec includes: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, stop rules, context supply plan | G1.Invariants | Partial | Objective: present (§Scope). Constraints by enforcement layer: present in Autonomy Table (Full Autonomy/Guarded/Proposal-First/Human-Required). Health metrics: absent. Acceptance criteria: absent. Stop rules (halt/escalation/completion): absent. Context supply plan: §Continuity lists session boot reads but no tiered supply plan. | G1 §Recovery | 1 | High |
| 2 | Hard constraint enforcement outside prompt layer | Hard constraints have enforcement mechanisms outside the prompt layer | G1.Invariants | Partial | "NEVER modify another system's files", "NEVER create or modify Design Decisions autonomously" stated in §Boundaries. Governance constraint: "Codifier cannot modify its own skill definitions or CLAUDE.md" — analogous here. The Autonomy Table's Human-Required tier provides a governance constraint, but structural enforcement (harness-level, hook-level) is not described. | G1 §Recovery | 1 | High |
| 3 | Templates filled completely | No placeholder TBD/TODO fields | G1.Invariants | Satisfied | No TBD/TODO placeholders detected. | — | 1 | High |
| 4 | Acceptance criteria evaluable by third party | Acceptance criteria evaluable by third party | G1.Invariants | Missing | No acceptance criteria section. Contract §Invariants states behavioral invariants ("Structural changes are proposal-first") but not testable pass/fail criteria. | G1 §Recovery | 1 | High |
| 5 | Context elements justifiable | Every context element has a justifiable reason | G2a.Invariants | Partial | §Continuity: five session boot reads (constitution, CLAUDE.md, PROGRESS.md, SL entries, feedback/). Justifications partially implied but not documented. No tiered loading architecture. | G2a §Recovery | 1 | Medium |
| 6 | Tiered loading | Tiered loading preserves token budget | G2a.Invariants | Missing | No tiered loading strategy. Five boot reads are stated as always-on without a minimal-upfront architecture. The Owner's boot reads are substantial (constitution, CLAUDE.md, SL entries, feedback/ folder). | G2a §Recovery | 1 | Medium |
| 7 | Session boundary reset | Session boundaries reset degradation | G2b.Invariants | Satisfied | §Continuity: "The Owner is stateless across sessions. It re-reads system state each time." Session boundary explicitly cited as the model. | — | 1 | High |
| 8 | Single-agent default respected | Single-agent is the default until empirical evidence justifies multi-agent | G3.Invariants | Satisfied | Owner is a single-agent system steward. No sub-agent decomposition. | — | 1 | High |
| 9 | Four-zone decomposition | Four zones specified (trigger, context, tools, output/memory) | G3.Invariants | Partial | Trigger: §Disposition §When Active (four activation conditions). Context: §Continuity + §Communication Input Artifacts. Tools: §Skill Inventory. Output/memory: §Communication §Output artifacts with gates. Zones present but not labeled as zones; memory zone limited to filesystem state (SL entries, proposals). | G3 §Recovery | 1 | Medium |
| 10 | Model selection stated | Model selection is task-based, not provider-based | G3.Invariants (merged G3.I4/G8.I4) | Missing | No model selection statement in the spec. | G3 §Recovery | 1 | High |
| 11 | Autonomy table present | No decision type defaults to full autonomy without explicit classification | G9.Invariants / agent.md template | Satisfied | §Autonomy Table present and covers 11 action types across Full Autonomy, Guarded, Proposal-First, Human-Required tiers. All action types classified. | — | 1 | High |
| 12 | Human retains override authority | Human retains override authority at all autonomy levels | G9.Invariants | Satisfied | Human-Required tier for DDs and cross-system changes. Proposal-First for structural changes. No tier removes human ability to intervene. | — | 1 | High |
| 13 | Audit trail maintained | Audit trail maintained for all agent actions — append-only, immutable, queryable | G9.Invariants | Partial | §Core Truths: "Authority requires auditability. Every action the Owner takes that modifies the system is logged." §Communication: SL entries in operations/system-log/ with Guarded gate. However, no specification of append-only / immutable / queryable properties for the SL. | G9 §Recovery | 1 | Medium |
| 14 | Trust promotion requires demonstrated track record | Trust promotion requires demonstrated track record; trust demotion is immediate on failure | G9.Invariants | Missing | The Owner's Autonomy Table is static — no trust promotion/demotion mechanism described. Tier changes are gated ("Tier changes require human authorization" in §Boundaries) but no track record criterion for tier promotion is defined. | G9 §Recovery | 1 | High |
| 15 | Destructive/irreversible actions require human approval | Destructive or irreversible actions always require human approval | G9.Invariants | Satisfied | Human-Required tier covers "Create/modify DD" and "Cross-system changes." "NEVER run destructive commands without explicit approval" is in the global CLAUDE.md (inherited). | — | 1 | High |
| 16 | Agent outputs carry explicit fact-vs-judgment classification | Agent outputs that reach human decision-makers carry explicit fact-vs-judgment classification | G9.Invariants | Missing | No fact-vs-judgment classification described for drift reports, structural proposals, or feedback triage reports. | G9 §Recovery | 1 | Medium |
| 17 | Permissions narrow monotonically across delegation | Permissions narrow monotonically across delegation chains | G9.Invariants | Not applicable | Owner does not delegate to sub-agents. Invariant not applicable. | — | 1 | High |
| 18 | Agent cannot modify its own autonomy tiers | Autonomy tier assignments are governed — agents cannot modify their own tier | G9.Invariants | Satisfied | §Boundaries: "NEVER promote your own autonomy tiers." §Autonomy Table: "Modifying its own autonomy tiers" is absent from Full Autonomy actions — implicitly Human-Required. §Contract §Invariants: "The Owner cannot modify its own autonomy tiers." | — | 1 | High |
| 19 | Memory organized into explicit tiers | Memory is organized into explicit tiers with defined read/write policies per tier | G7.Invariants | Partial | §Continuity: "The Owner is stateless across sessions." §Boundaries: MAY write to `agents/owner/reflections/`. §Communication Output: five output types with gates. But no explicit memory tier architecture (hot/warm/cold or equivalent). The Owner's memory model is implicit filesystem state. | G7 §Recovery | 1 | Medium |
| 20 | Sessions leave system in clean, resumable state | Sessions leave the system in a clean, resumable state verified by automated checks | G7.Invariants | Partial | §Continuity: "State persistence: Proposals are written as files. System modifications go through git." Session close → git commit as state persistence. No automated clean-state verification described. | G7 §Recovery | 1 | Medium |
| 21 | Memory writes are policy-governed | Memory writes are policy-governed AND novelty-gated AND contradiction-checked | G7.Invariants | Partial | SL entries have a Guarded gate (act-then-report). Doc updates have a Guarded gate. Proposals have Proposal-First. But no novelty gate or contradiction-check mechanism described for SL entries or reflections. | G7 §Recovery | 1 | Medium |
| 22 | Identity defined separately from capabilities | Agent identity separate from capabilities, survives context compaction | G10.Invariants | Satisfied | §Constitution is a distinct section from §Skill Inventory. Clear separation. | — | 1 | High |
| 23 | All five prompt layers addressed | All five prompt layers addressed | G10.Invariants | Partial | Five-layer framework not mapped. Sections present but not traced to the layer architecture; no intentional omissions documented. | G10 §Recovery | 1 | Medium |
| 24 | Clarification behavior distinguishes resolvable from intent-dependent | Clarification behavior distinguishes resolvable gaps from intent-dependent gaps | G10.Invariants | Partial | §Disposition §Cognitive Approach lists 5 steps (read, compare, surface drift, propose, scope narrowly) but does not explicitly distinguish resolvable from intent-dependent gaps. No check-in rate guidance. | G10 §Recovery | 1 | Medium |
| 25 | No agent exists solely to review another's output | No agent exists solely to review another agent's output | G10.Invariants | Satisfied | The Owner is a system steward, not a review-only agent. | — | 1 | High |
| 26 | Autonomy envelope section present (Variant C overlay) | Variant C overlay: HITL gates, escalation thresholds, trust-promotion criteria in Autonomy Envelope section | agent.md concept §Variant C overlay | Partial | An Autonomy Table is present (#11) which covers HITL gating. However, the agent.md concept requires a distinct "Autonomy Envelope" section between Scope and Autonomy Table covering "HITL gates, escalation thresholds, trust-promotion criteria." This is not present as a named section; trust-promotion criteria are missing (#14). | agent.md concept §Template skeleton §Variant C | 1 | High |
| 27 | Recovery section covers scope | Contract §Recovery covers system-state inconsistency, governance gaps, cross-scope feedback | G1.Invariants | Satisfied | Recovery covers: inconsistent system state (drift report), missing governance docs (flag and propose), out-of-scope feedback (flag for human routing). Concrete and actionable. | — | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | Hard constraints enforced outside prompt layer | G1.Invariants | Is "NEVER modify another system's files" enforced at the harness level (e.g., `.claude/settings.json` path restrictions), or only in the prompt? | Harness settings config |
| b | Stable context cached | G2b.Invariants | Is the Owner's session boot context (constitution, CLAUDE.md) loaded with prompt caching? What is the cache-hit rate for these stable reads? | Caching config; cache-hit telemetry |
| c | Audit trail is append-only and queryable | G9.Invariants | Are SL entries stored in a format that is provably append-only and supports querying by date/agent/action-type? | SL storage schema; query capability |
| d | Trust track record measurement | G9.Invariants | Is there a mechanism to track the Owner's decision quality over time as evidence for future autonomy tier changes? What constitutes a "demonstrated track record"? | Track record criteria; evaluation cadence |
| e | Fact-vs-judgment classification in outputs | G9.Invariants | Do drift reports and structural proposals explicitly label which assertions are observed facts vs. the Owner's judgment calls? | Example report showing classification |
| f | Session clean-state verification | G7.Invariants | Is there an automated check (or standard checklist) run at session close to verify proposals are filed, git is committed, and SL is updated? | Session close checklist or hook |
| g | Memory tier documentation | G7.Invariants | Is there a documented memory tier architecture for the Owner's persistent outputs (SL entries, proposals, reflections), with read/write policies per tier? | Memory architecture doc or policy |
| h | Comprehension coverage tracked | G9.Invariants | For Owner-generated artifacts that reach Nick as decision-maker (drift reports, proposals), is there a comprehension gate tracking that each artifact has been read and understood before actioning? | Comprehension gate record or process |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G3b (`agent-workflow-and-execution.md`) | G3b Preconditions require a workflow with side effects that runs longer than a single turn with identified "done" criteria. The Owner's work is advisory and proposal-based — it does not execute multi-step automated workflows with checkpoint requirements. G3b latent. |
| G5 (`designing-agent-tools.md`) | G5 Preconditions require tools the agent invokes via function calling/MCP/CLI with custom definitions. The Owner uses Read/Glob/Grep/Write for filesystem operations — harness-native tools, not custom tool definitions. G5 latent. |

---

### Summary

**Solid:** The Owner's Autonomy Table is the strongest governance surface among the four IL agents — it covers 11 action types across four tiers, explicitly prevents self-promotion (#18), and correctly places DDs and cross-system changes at Human-Required (#12, #15). Session-boundary statelessness provides effective context defense (#7). Recovery section is concrete and covers the most likely failure modes (#27).

**Load-bearing to fix:** Missing acceptance criteria (#4), health metrics, and stop rules (#1) are template gaps. Model selection is absent (#10). The Variant C overlay requires a distinct "Autonomy Envelope" section with trust-promotion criteria — currently the Autonomy Table covers HITL gating but trust-promotion criteria are absent (#26, #14). Fact-vs-judgment classification in outputs (#16) is missing and load-bearing for governance integrity.

**Hinges on consumer follow-up:** Whether structural enforcement exists for cross-system write restrictions (follow-up a), whether the audit trail is genuinely append-only (follow-up c), and whether trust track records are measured (follow-up d) are the most significant open questions.

---

### Agent (fractal): `systems/improvement-loop/agents/researcher/agent.md`
*Assessed via /assess-agent (Librarian subagent bin 1, fresh context, mode: in-context-rubric)*

## Audit — Agent

**Artifact:** `systems/improvement-loop/agents/researcher/agent.md`
**mode:** in-context-rubric
**Interpreted as:** verb: audit, noun: agent, variant: A+B (prompt-based + harness-based — the Researcher has an enumerated 11-skill inventory with write operations, guarded workflow runs, and autonomous KB maintenance tasks that place it in Variant B territory).
**Tier trace:** Read 7 Tier-1 Contract sections (G1, G2a, G2b, G3, G3b, G5, G10); G6 read for partial applicability (file-writing agent); 0 Tier-2; 0 Tier-3.

**Composed guides (Variant A+B):** G1 `writing-agent-specifications.md`, G2a `structuring-agent-context.md`, G2b `defending-agent-context.md`, G3 `agent-architecture-decisions.md`, G3b `agent-workflow-and-execution.md`, G5 `designing-agent-tools.md`, G10 `agent-design-patterns.md`. G6 applied with Precondition note.

**Rubric size:** 27 file-verifiable invariants checked; 8 system/process-verifiable invariants → follow-ups; 2 guides latent (G7, G9 — Researcher does not span sessions with stateful memory; no HITL autonomy envelope for high-blast-radius autonomous actions beyond G3b scope).

**DD-92 ContextSpec audit:** No `context:` block present in frontmatter. DD-92 ContextSpec audit skipped. Frontmatter carries IL classification metadata (`confidence: "HIGH"`, `tier: "auto"`, `reason_codes`, `co_occurrence: null`) — informational finding below.

---

### Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|--------|-----------|--------|---------|----------|--------------------|------|------------|
| 1 | Spec completeness — objective and outcomes | Every agent spec includes: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, stop rules, context supply plan | G1.Invariants | Partial | Objective: present (§Scope). Constraints: present (§Boundaries). Autonomy per skill: present in §Skill Inventory. Health metrics: absent. Acceptance criteria: absent. Stop rules: absent. Context supply plan: §Continuity lists session boot reads (PROGRESS.md, last delta report) but no tiered supply plan. | G1 §Recovery | 1 | High |
| 2 | Hard constraint enforcement outside prompt layer | Hard constraints have enforcement mechanisms outside prompt layer | G1.Invariants | Missing | Write boundaries ("NEVER write outside IL-owned directories") stated in §Boundaries and Contract §Invariants — prompt only. No harness-level permission enforcement described. | G1 §Recovery | 1 | High |
| 3 | Templates filled completely | No placeholder TBD/TODO fields | G1.Invariants | Satisfied | No placeholder fields found. | — | 1 | High |
| 4 | Acceptance criteria evaluable by third party | Acceptance criteria evaluable by third party | G1.Invariants | Missing | No acceptance criteria section. Contract §Invariants states behavioral invariants but not testable pass/fail criteria. | G1 §Recovery | 1 | High |
| 5 | Context elements justifiable | Every context element has a justifiable reason | G2a.Invariants | Partial | §Continuity: two boot reads (PROGRESS.md, last delta report). Justification implied but not documented. No tiered loading strategy. | G2a §Recovery | 1 | Medium |
| 6 | Tiered loading | Tiered loading preserves token budget | G2a.Invariants | Missing | No tiered context loading strategy. Two boot reads are listed as always-on without minimal-upfront architecture. | G2a §Recovery | 1 | Medium |
| 7 | Session boundary reset | Session boundaries reset degradation | G2b.Invariants | Satisfied | §Continuity: "Each research session produces a delta report. The delta report IS the session record." Session scoping is explicit. Session boundaries are the primary defense mechanism. | — | 1 | High |
| 8 | Single-agent default respected | Single-agent is the default until empirical evidence justifies multi-agent | G3.Invariants | Satisfied | The Researcher is a single-agent. No sub-agent delegation. | — | 1 | High |
| 9 | Four-zone decomposition | Four zones specified (trigger, context, tools, output/memory) | G3.Invariants | Partial | Trigger: invoked by skill or user URL provision. Context: §Continuity. Tools: §Skill Inventory (11 skills across 3 categories). Output/Memory: §Communication (delta reports, findings, sources, authorities). Zones present but not explicitly labeled; memory zone is limited to delta reports as session records. | G3 §Recovery | 1 | Medium |
| 10 | Model selection stated | Model selection is task-based, not provider-based | G3.Invariants (merged G3.I4/G8.I4) | Missing | No model selection statement in spec. CLAUDE.md memory note references "Sonnet" but not in the agent spec. | G3 §Recovery | 1 | High |
| 11 | Every workflow has explicit state tracking | Every workflow has explicit state tracking independent of conversation history | G3b.Invariants | Satisfied | §Continuity: "Each research session produces a delta report." Delta reports in operations/research-reports/ are the explicit state record independent of conversation. | — | 1 | High |
| 12 | Every iterative pattern has termination condition | Every iterative pattern has a termination condition | G3b.Invariants | Missing | No termination conditions stated for source-processing loops, watch-list scans, or batch extraction runs. The Researcher's "expansive intake" disposition does not define when a session ends or what constitutes completion. | G3b §Recovery | 1 | High |
| 13 | Cost controls before autonomous execution | Cost controls before autonomous execution | G3b.Invariants | Missing | No cost controls, per-source budgets, or fast-fail conditions described. Skills marked "Guarded" for monitoring tasks but no budget mechanism. | G3b §Recovery | 1 | Medium |
| 14 | Delivery chunk size calibrated | Delivery chunk size calibrated to reviewer capacity | G3b.Invariants | Partial | §Clarification behavior: "Intent-dependent: 'Is this source worth a deep transcript extraction?'" — chunk-size awareness implied for source depth. But no explicit calibration rule. | G3b §Recovery | 1 | Low (implied, not specified) |
| 15 | Tool definitions are data first | Tool definitions are data first — metadata before implementation | G5.Invariants | Partial | §Skill Inventory lists skills with purpose and autonomy level. Metadata present at the skill level. G5 applicability is borderline (same as Codifier — skills vs. API-function tools). | G5 §Recovery | 1 | Low |
| 16 | Only tools needed for current task loaded | Only tools needed for current task loaded | G5.Invariants | Not specified | No tool-loading mechanism described. 11 skills are listed but no scoping mechanism prevents all skills from being in context simultaneously. | G5 §Recovery | 1 | Medium |
| 17 | Skills are framework-agnostic | Skills are framework-agnostic markdown files | G5.Invariants | Satisfied | Skills are SKILL.md files per IL convention. Framework-agnostic. | — | 1 | High |
| 18 | Identity defined separately from capabilities | Identity separate from capabilities, survives compaction | G10.Invariants | Satisfied | §Constitution is distinct from §Skill Inventory. Clear separation. | — | 1 | High |
| 19 | All five prompt layers addressed | All five prompt layers addressed | G10.Invariants | Partial | Five-layer architecture not mapped. Sections present but not traced to the layer framework; no intentional omissions documented. | G10 §Recovery | 1 | Medium |
| 20 | Clarification behavior distinguishes resolvable from intent-dependent | Clarification behavior distinguishes resolvable from intent-dependent gaps | G10.Invariants | Satisfied | §Disposition explicitly distinguishes "Resolvable gaps (fill autonomously)" from "Intent-dependent gaps (ask Nick)" with concrete examples. Check-in rate triggers defined ("check-in rate increases with: unfamiliar research dimensions, contradictory evidence across sources, potential P1 reclassifications"). | — | 1 | High |
| 21 | No agent exists solely to review another's output | No agent exists solely to review another agent's output | G10.Invariants | Satisfied | The Researcher is a research intake agent, not a review agent. | — | 1 | High |
| 22 | Autonomy table present | No decision type defaults to full autonomy without explicit classification | G10.Invariants / agent.md template | Missing | No explicit Autonomy Table in the spec. Skill Inventory lists autonomy per skill (Full Autonomy / Guarded / Proposal-First) but the template's decision-type Autonomy Table covering all action types is absent. | agent.md concept §Template skeleton | 1 | High |
| 23 | Hard-constraint enforcement — write boundaries | Safety-critical constraints enforced structurally (G6 — partially applicable) | G6.Invariants | Missing | Write boundaries stated in prompt only. No structural enforcement at harness or OS layer. The Researcher writes to six directories — structural gating is not documented. | G6 §Recovery | 1 | High |
| 24 | Agent cannot modify own permission config | Agent cannot modify own permission configuration | G6.Invariants | Satisfied | §Governance in Contract: "Researcher cannot modify its own skill definitions or CLAUDE.md." | — | 1 | High |
| 25 | One canonical finding per pattern | One canonical finding per pattern — updates, never duplicates | G1.Invariants (data integrity invariant from KB maintenance scope) | Satisfied | §Core Truths: "Deduplication is intellectual honesty. One canonical entry per pattern. Update existing findings with new evidence; never create a second entry with different framing." §Boundaries: "If uncertain whether a pattern duplicates an existing finding: search KB before creating." | — | 1 | High |
| 26 | Frontmatter carries IL classification metadata (informational) | IL pipeline metadata should be stripped at deploy boundary | Informational | Informational | Frontmatter: `confidence: "HIGH"`, `tier: "auto"`, `reason_codes: ["durable-scope", "cognitive-disposition", "11-skill-inventory"]`, `co_occurrence: null`, `deployed: false`. Pre-deploy state acceptable; metadata must be stripped before deployment. | DD-92 §Check 3 (analogous) | 1 | High |
| 27 | Recovery section concrete | Contract §Recovery covers key failure modes | G1.Invariants | Satisfied | Recovery covers: duplicate finding creation (merge + linkage-repair), mid-batch source failure (delta report + resume), KB integrity issue (linkage-repair + crosslink). Concrete and actionable. | — | 1 | High |

---

### Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|-----------|--------|----------|-------------------|
| a | Hard constraints enforced outside prompt layer | G1.Invariants | Is there a harness-level permission configuration enforcing the Researcher's write boundaries at runtime (restricted to `research-findings/`, `research-sources/`, `research-authorities/`, `watched-libraries/`, `watched-blogs/`, `operations/`)? | Harness settings config showing path restrictions |
| b | Stable context is cached | G2b.Invariants | Is the stable portion of context (PROGRESS.md, last delta report) loaded with prompt caching? What is the observed cache-hit rate for Researcher sessions? | Caching config; cache-hit telemetry |
| c | Workflow state checkpointed independently | G3b.Invariants | For long research-loop or watch-upstream runs (multi-source batches), is workflow state checkpointed to a file after each source, independently of conversation history? If Claude Code crashes mid-batch, what is the resume mechanism? | Checkpoint examples; delta report partial-progress format |
| d | Termination conditions defined per skill | G3b.Invariants | What is the session-length limit for a /research-loop run? What stops a /watch-upstream scan — source count, time budget, or explicit end signal? | Termination conditions in SKILL.md files |
| e | Cost controls per source | G3b.Invariants | Are there per-source token budgets or batch-size limits for research-loop runs? What triggers escalation for unexpectedly deep sources (e.g., 10,000-word papers)? | Budget config or skill SKILL.md |
| f | Source authority distribution tracked | G1.Invariants (Core Truth: source diversity is first-class) | Is there an active mechanism to measure authority distribution across the KB (e.g., count of findings per authority)? What threshold triggers a diversity alert? | Authority distribution report; diversity check in /research-loop |
| g | Model routing per skill | G3.Invariants | What model is used for different Researcher skills (e.g., Perplexity integration vs. transcript extraction vs. finding authoring)? Is model selection task-based? | Skill SKILL.md or harness config |
| h | KB deduplication search enforced at runtime | G1.Invariants / §Boundaries | Is the "search KB before creating" deduplication rule enforced by the /research-loop or /promote-findings skill procedures, or only by prompt-layer instruction? | SKILL.md deduplication procedure |

---

### Aspects out of scope

| Guide | Why latent |
|-------|------------|
| G7 (`session-persistence-and-memory.md`) | The Researcher does not span multiple sessions with stateful in-context memory. Delta reports provide session records but the agent re-reads state from scratch each session. G7 Preconditions (agent persists beyond a single cycle with persistent state) are not satisfied in the statefulness sense. G7 latent. |
| G9 (`agent-governance-and-trust.md`) | G9 is Variant C primary — the Researcher's autonomy envelope is covered by the skill-level Guarded/Full Autonomy/Proposal-First assignments in §Skill Inventory, not by an autonomous HITL governance architecture. G9.I6 (destructive action check): the Researcher does not perform destructive or irreversible actions (it creates/updates, not deletes or deploys). G9 latent. |

---

### Summary

**Solid:** The Researcher has the strongest clarification behavior of the four IL agents — the resolvable/intent-dependent split with check-in rate triggers is explicit and complete (#20). Session-boundary-based context defense via delta reports is well-specified (#7, #11). Deduplication discipline is articulated as a Core Truth and in the Boundaries (#25). Recovery section covers the three most likely failure modes (#27). The 11-skill inventory is coherently categorized (Intake, Monitoring, KB Maintenance) with per-skill autonomy levels.

**Load-bearing to fix:** No Autonomy Table (#22), missing acceptance criteria (#4), no model selection statement (#10), no termination conditions for iterative runs (#12), and no structural write-boundary enforcement (#2, #23). The absence of termination conditions is particularly notable for an agent whose disposition is "expansive intake" — without a session-end criterion, the Researcher could run indefinitely. The 11-skill inventory (the largest of any IL agent) amplifies the cost of unspecified tool-loading scope (#16).

**Hinges on consumer follow-up:** Whether harness-level write enforcement exists (follow-up a), whether per-source cost controls are defined (follow-up e), and whether source authority distribution is actively monitored (follow-up f) are the key open questions. The IL classification metadata in frontmatter (#26) must be stripped before deployment.

---

## CLAUDE.md files

### CLAUDE.md: `systems/improvement-loop/CLAUDE.md`
*Dispatched to bin 2 — **report MISSING**.*

Bin 2 emitted only 1 of N expected sentinel-delimited reports (format-compliance failure per `/audit-system` SKILL.md §FAILURE SIGNAL — individual-report-missing, not whole-bin-unparseable). Cause: subagent message-budget or instruction-following drift between dispatch payload and assessor invocation. Artifact unassessed in this run.

**Resolution:** invoke the IL `/assess-skill` (or `/assess-agent --variant prompt-based`) skill directly on this path, or re-audit via `/audit-system systems/improvement-loop/ --scope skills`.

---

### CLAUDE.md: `systems/improvement-loop/docs/CLAUDE.md`
*Assessed via /assess-agent (Librarian subagent bin 3, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** REJECTED / REDIRECT — shape mismatch (MOC)

**Critical:** Artifact is a folder-level directory README. No frontmatter, no agent-spec shape. Per `/assess-agent` §Boundaries: rejected.

**G9.I6 outcome:** n/a — shape mismatch precludes rubric application.

**Top findings:**
- Outcome: shape-mismatch latent — MOC, not an agent spec.

---

### CLAUDE.md: `systems/improvement-loop/extracts/CLAUDE.md`
*Dispatched to bin 4 — **report MISSING**.*

Bin 4 emitted only 1 of N expected sentinel-delimited reports (format-compliance failure per `/audit-system` SKILL.md §FAILURE SIGNAL — individual-report-missing, not whole-bin-unparseable). Cause: subagent message-budget or instruction-following drift between dispatch payload and assessor invocation. Artifact unassessed in this run.

**Resolution:** invoke the IL `/assess-skill` (or `/assess-agent --variant prompt-based`) skill directly on this path, or re-audit via `/audit-system systems/improvement-loop/ --scope skills`.

---

### CLAUDE.md: `systems/improvement-loop/extracts/guides/CLAUDE.md`
*Dispatched to bin 4 — **report MISSING**.*

Bin 4 emitted only 1 of N expected sentinel-delimited reports (format-compliance failure per `/audit-system` SKILL.md §FAILURE SIGNAL — individual-report-missing, not whole-bin-unparseable). Cause: subagent message-budget or instruction-following drift between dispatch payload and assessor invocation. Artifact unassessed in this run.

**Resolution:** invoke the IL `/assess-skill` (or `/assess-agent --variant prompt-based`) skill directly on this path, or re-audit via `/audit-system systems/improvement-loop/ --scope skills`.

---

### CLAUDE.md: `systems/improvement-loop/extracts/patterns/CLAUDE.md`
*Dispatched to bin 4 — **report MISSING**.*

Bin 4 emitted only 1 of N expected sentinel-delimited reports (format-compliance failure per `/audit-system` SKILL.md §FAILURE SIGNAL — individual-report-missing, not whole-bin-unparseable). Cause: subagent message-budget or instruction-following drift between dispatch payload and assessor invocation. Artifact unassessed in this run.

**Resolution:** invoke the IL `/assess-skill` (or `/assess-agent --variant prompt-based`) skill directly on this path, or re-audit via `/audit-system systems/improvement-loop/ --scope skills`.

---

### CLAUDE.md: `systems/improvement-loop/governance/proposals/CLAUDE.md`
*Assessed via /assess-agent (Librarian subagent bin 3, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** REJECTED / REDIRECT — shape mismatch (MOC)

**Critical:** Artifact is a folder-level index (`type: "index"`) — proposal lifecycle catalog. No agent-spec shape. Rejected per `/assess-agent` §Boundaries.

**G9.I6 outcome:** n/a — shape mismatch.

**Top findings:**
- Outcome: shape-mismatch latent — MOC (frontmatter `type: "index"`).

---

### CLAUDE.md: `systems/improvement-loop/operations/references/CLAUDE.md`
*Assessed via /assess-agent (Librarian subagent bin 3, fresh context, mode: in-context-rubric). Verbatim report in session 115 transcript; structured digest below.*

**Classification:** REJECTED / REDIRECT — shape mismatch (MOC)

**Critical:** Plain-markdown folder README. No frontmatter, no agent-spec shape. Rejected per `/assess-agent` §Boundaries.

**G9.I6 outcome:** n/a — shape mismatch.

**Top findings:**
- Outcome: shape-mismatch latent — folder README, not an agent spec.

---

