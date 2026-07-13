# Audit — SKILL.md (`self-improve`)

Classification: **safety-critical** (trigger: `allowed-tools` includes Write, Edit,
Bash; skill self-declares "writes cross-file ops state; promote mode edits live
surfaces" — SKILL.md:148-149).

**Artifact:** `/Users/nickgogan/MetaSystem/systems/improvement-loop/.claude/skills/self-improve/SKILL.md`
**Design of record:** `project-management/design-notes/2026-07-13-memory-system-design.md` (IB-176)
**Requested by:** Nick — newly authored skill, pre-deployment IL audit
**Composed guides:** G1 `writing-agent-specifications` (spec quality) · G3b
`agent-workflow-and-execution` (state/termination) · G5 `designing-agent-tools`
(tool surface) · G6 `agent-safety-and-permissions` (permissions) · G8
`model-resilient-prompt-engineering` (trigger/prompt craft) · **G9
`agent-governance-and-trust` — G9.I6 forced by safety-critical classification**
**Rubric size:** 14 file-verifiable invariants, 3 system-verifiable follow-ups,
remaining composed-guide invariants latent (listed below)

DD-92 ContextSpec audit skipped — no `context:` block in frontmatter (SKILL.md:1-18
carries only `name`, `description`, `user-invocable`, `allowed-tools`,
`argument-hint`). DD-92 binds extracted and deployed artifacts; consumer-submitted
artifacts without ContextSpec are not flagged here.

## Findings (file-verifiable)

| # | Aspect | Invariant | Source | Outcome | Evidence | Recovery reference | Tier | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Contract section presence | Skill missing any of When-to-use / Procedure / Output-shape / Boundary-conditions fires G1.I1 | G1.I1 via skill.md §Template skeleton | **Partial** | No `## When to use`, `## Output shape`, or `## Boundary conditions` heading anywhere in the file (headings present: Standing rules, Dispatch table, Mode: capture/scan/promote/status, Edge cases, Constraints, SKILL.md:20-154). Equivalent content exists but is scattered — trigger conditions live only in frontmatter `description` (:3-14), output shapes are named inline per mode, and `## Constraints` (:146-154) covers safety-critical/termination substance without the canonical labels | skill.md §Template skeleton — add the four canonical headings or explicitly map existing sections to them | 1 | High |
| 2 | Hard constraints enforced outside prompt layer | G1.I3 (umbrella) ⊃ G6.I2 (specialization: safety-critical constraints enforced structurally) — both fired, overlap annotated | G1.I3, G6.I2 | Satisfied | `store_check.py` runs in the repo pre-commit hook (verified: `.git/hooks/pre-commit` calls `operations/kb-maintenance-scripts/store_check.py`, blocking on schema violations) and the promote-mode shadow sandbox is explicitly fail-closed: "any validator failure kills the proposal at this stage" (:113-115) | — | 1 | High |
| 3 | Acceptance criteria evaluable by a third party | G1.I4 | Satisfied | Fresh-context grade uses a binary rubric assessed by a separate subagent, not the generator: "grounded / minimal / effective / non-regressive. Any `no` → revise or decline" (:116-118) | — | 1 | High |
| 4 | Stop rules — halt, escalation, completion | G1.I5 | **Partial** | Substance exists but is not consolidated: halt = shadow-sandbox fail-closed (:113-115); escalation = "Nick gate... per-proposal ruling" (:120-121); completion = "Log: append a `P-<seq>` entry... update the lesson's status" (:122-125). No single Boundary-conditions/Termination field states all three together | Same fix as #1 — a consolidated Boundary-conditions section would make this directly verifiable | 1 | Medium |
| 5 | Context-isolated dispatch carries its own contract (global constraints copied verbatim, Consumes/Produces interface) | G1.I6 | **Partial** | Promote-mode Step 3 dispatches to "a separate assessor subagent (generator-assessor rule) with the binary rubric" (:116-117) but does not state what context/constraints are copied to that subagent, nor an explicit Consumes/Produces interface | G1 §Recovery / §Contract — name what the assessor subagent receives (lesson, diff, owning-surface constraints) explicitly in the procedure step | 1 | Medium |
| 6 | State tracking independent of conversation history | G3b.I2 | Satisfied | The four store files (`lessons.md`, `query-log.md`, `proposal-log.md`, `retro-latest.md`) at `operations/self/` are the durable state, explicitly separated from conversation (:22-24, design note §2) | — | 1 | High |
| 7 | Every iterative pattern has a termination condition | G3b.I3 | **Partial** | The fresh-context grade "revise or decline" cycle (:118) has no stated bound — "revise" could loop draft→sandbox→grade indefinitely with no cap or stall-detection rule | G3b §Recovery ("add loop termination rules") — cap revise attempts (e.g., 2) before forcing a decline | 1 | Medium |
| 8 | Delivery chunk size calibrated to reviewer capacity | G3b.I5 | Satisfied | "**Per-proposal Nick gate, never batch**" (:44, :121) — one lesson per pipeline pass, never batched to the reviewer | — | 1 | High |
| 9 | Destructive/irreversible actions human-gated | Destructive or irreversible actions always require human approval regardless of trust level | **G9.I6** (forced) | **Partial** | The gate exists and is per-proposal ("Nick gate: present the proposal... for a per-proposal ruling. Governance surfaces stop here always," :120-121) but the procedure never states the mechanical transition — nowhere does it say "if Nick rules `applied`, write the diff to the owning surface via Edit; if `declined`, no live file is touched." Step 5 ("Log," :122-125) only records the outcome, it doesn't name who/what performs the apply | Add an explicit clause: apply happens only on `applied` ruling, via Edit/Write to the owning surface, immediately before the logging + commit step | 1 | Medium |
| 10 | Permissions tiered by risk, not binary allow/deny | G6.I1 | **Partial** | `allowed-tools: Read Grep Glob Write Edit Bash Agent` (:16) is one flat grant across all four modes, even though only promote mode reaches live/deploy-boundary edits (capture/scan/status touch only `operations/self/`). Risk tiering exists solely in prose (`## Constraints`, :148-151), not structurally differentiated per mode | G6 §Recovery — consider a per-mode tool note in Boundary conditions, or accept flat grant as scoped-by-convention and say so explicitly | 1 | Medium |
| 11 | Defense is layered | G6.I4 | Satisfied | Five independent layers stack: append-only store (:31-35), fail-closed shadow sandbox (:113-115), separate-context assessor grading (:116-118), per-proposal Nick gate (:120-121), and git-reversibility of every write (:151) | — | 1 | High |
| 12 | High-priority behavioral rules as negative constraints | G8.I3 | Satisfied | All 7 standing rules are phrased as prohibitions, not aspirations: "never edited or deleted," "Untraceable lesson = invention," "never share a bucket," "never silently lowered," "never batch," "never whole-store rewrites" (:32-48) | — | 1 | High |
| 13 | Minimal tool surface — no over-granting | G5 authoring anti-pattern, skill.md §Anti-patterns | **Partial** | `Grep` is listed in `allowed-tools` (:16) but no procedure step in the body explicitly names a grep-based operation (identity matching in capture mode, :70-71, is described as "check `lessons.md` for an existing entry" without naming the tool) | Either name the Grep-using step explicitly (e.g., lesson-identity lookup) or trim the grant | 1 | Medium |
| 14 | Skill scope vs. Split heuristic | skill.md §Scoping heuristics ("Split when... description needs 'and' or two trigger conditions joined by 'or'"; DD-80 identify/extract precedent for this exact shape) | **Partial** (advisory) | The frontmatter `description` lists four distinct trigger conditions joined by "or" (:11-14: "noticed... for the periodic retro... when `store_check.py` flags PROMOTE... or to check store health") — the same shape skill.md names as its own splitting signal, and structurally analogous to the identify/extract precedent it cites. The design note rules "one skill, four modes" deliberately (§2), but the skill body itself doesn't cross-reference or re-justify against this heuristic | Not necessarily wrong — but add one line to Boundary conditions/Out-of-scope citing why the four modes share one skill (shared store substrate, not independent end-shapes) so future audits don't re-raise it from scratch |  1 | Low |

## Follow-ups (system/process-verifiable — consumer must attest)

| # | Invariant | Source | Question | Evidence expected |
|---|---|---|---|---|
| a | Model selection is task-based, not provider-based; Advisor-Executor considered before defaulting to the most expensive model | G8.I4 / G8 §Advisor-Executor | What model runs the fresh-context assessor subagent in promote-mode Step 3 — is it cost-tiered relative to the drafting step, or does it default to the most expensive available model? | Model assignment for the assessor dispatch, and the rationale if it matches the drafting model |
| b | Permissions narrow monotonically across delegation chains | G9 (delegation-chain invariant) | Does the `Agent` tool dispatch to the fresh-context assessor subagent (promote Step 3) grant a strict subset of `self-improve`'s own tool access, or the same/broader set? | The assessor subagent's actual tool grant, compared against `Read Grep Glob Write Edit Bash Agent` |
| c | Degradation modes are defined before the system goes live | G3b.I4 | Capture mode and status mode both invoke `store_check.py` (:78, :129) — what happens if the script itself errors (not just reports a PROMOTE flag)? Is there a defined fallback distinct from the pre-commit blocking path? | The runtime behavior of capture/status modes on a non-zero, non-PROMOTE `store_check.py` exit |

## Aspects out of scope (latent)

| Guide / invariant group | Why latent |
|---|---|
| DD-92 ContextSpec | No `context:` frontmatter block present (see skip note above) |
| G8 model-routing tables, prompt caching, code-snippet extraction, user-overridable output format | Skill performs no multi-model routing, no cached multi-turn prompt layers, and produces no code-snippet or interactive-format output |
| G5 tool-*design* invariants (poka-yoke schemas, tool descriptions-as-UX, interceptors, registries, CLI-vs-MCP) | Skill consumes built-in tools (Read/Grep/Glob/Write/Edit/Bash/Agent); it designs and ships none |
| G9 invariants beyond I6 (trust ledgers, policy-bundle versioning, cross-system correlation IDs, spawning allowlists) | Single-agent (Owner), single-system scope; substance of several (audit trail, autonomy-per-decision-type, locality-aware governance) is already evidenced directly in the dispatch table and store contracts, but the deeper multi-agent/cross-system machinery these invariants target doesn't apply here |
| G3b explicit cost/budget controls | Not evidenced either way at the file level; folded into follow-up (c) rather than flagged as Missing, since scan mode's read scope (feedback/, open lessons, recent reports) is bounded by "since last scan," not unbounded |

## Summary

**G9.I6: Partial, not blocking, but the single highest-value fix.** The human
gate exists in the right place (per-proposal, governance surfaces always stop
there, fail-closed shadow sandbox ahead of it) — but the procedure never
explicitly states the mechanical link between "Nick rules `applied`" and "the
diff is written to the live owning surface." That's the exact seam a
safety-critical-skill audit exists to press on; closing it is a small, high-leverage
edit (finding #9). Two other medium-severity gaps compound around the same
promote-mode pipeline: the revise/decline cycle has no bounded escape (#7), and
the dispatch to the fresh-context assessor subagent lacks an explicit
context-contract (#5) — both tighten the same safety-critical surface. The
Contract-section restructuring (#1, #4) is real per skill.md's own hard rule
but cosmetic relative to the promote-mode gaps. On the positive side: the
standing rules are exemplary negative-constraint framing (#12), and defense is
genuinely layered five-deep (#11) — this skill is closer to audit-clean than
most first-draft safety-critical skills.

---

*Produced by `/assess-skill` (Librarian, fresh context), 2026-07-13. Report
homed in `operations/artifact-audits/` per DD-110 (per-artifact contract
conformance) — following the `assess-skill--session-handoff.md` (2026-07-12)
precedent for report location and shape; the `/assess-skill` contract emits the
`audit.md` §Output-shape report but names no file destination. Not an
`/audit-artifacts` run; `runs.md` not appended.*
