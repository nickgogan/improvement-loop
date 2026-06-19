---
title: "/audit-system Design Contract"
id: "audit-system-design-contract"
type: "design-note"
category: "capability-design"
target_system:
  - "improvement-loop"
stage: "stable"
created: "2026-06-12"
updated: "2026-06-12"
author: "owner"
source_dd: []
superseded_in_part_by: "DD-110"
tags:
  - "design-note"
  - "audit-system"
  - "step-g"
  - "capability"
  - "rule-10"
  - "rule-11"
aliases:
  - "audit-system v1 spec"
---

# `/audit-system` Design Contract

> **Superseded in part by DD-110 (2026-06-19).** The skill was renamed `/audit-system` → **`/audit-artifacts`**, and its on-disk output moved from `<target>/audit-reports/<date>/` to **`<target>/operations/artifact-audits/<date>/`**. This note is preserved as the v1 design record *as of 2026-06-12* (including the historical meta-system smoke-test output paths, now archived) — for current name/paths see DD-110 and `.claude/skills/audit-artifacts/SKILL.md`.

Design substrate for step G's first build target. Drafted session 113 after capability-roadmap acceptance. **This is not a SKILL.md.** It is the design contract that seeds session 114+ implementation.

---

## Plain-English purpose

"Point this at a folder. Tell me whether the agentic system inside it is well-formed."

The user provides a local path. `/audit-system` discovers what agentic abstractions live there (skills, agents, prompts), dispatches each to the appropriate IL `/assess-*` skill via fresh subagent context, aggregates the results, and emits three deliverables: a structural manifest, per-artifact findings, and a whole-system summary.

It does not modify the audited system. It does not deploy anything. It does not propose changes — that's `/design-harness`'s job. Read-only by contract.

---

## Why MetaSystem owns this (vs. IL)

IL owns the per-artifact assessment substrate (`/assess-skill`, `/assess-agent`, `/assess-prompt`). MetaSystem owns the **whole-system composition** — the act of looking at a folder and treating it as a harness rather than a bag of artifacts. Whole-system invariants (cross-references, structural completeness, fractal compliance, audit/design symmetry) are MetaSystem-shaped concerns, not IL ones.

Per the consumer-abstractions-map: IL maintains §Composition + §Construction for skill and agent. MetaSystem composes those into a whole-system view; the consumer-abstractions-map analog for MetaSystem covers harness-level shapes.

---

## Input contract

| Field | Type | Required | Notes |
|---|---|---|---|
| `<path>` | local filesystem path | yes | Path to the root of the system being audited. Must be a directory. |
| `--scope <list>` | comma-separated artifact types | no | Limit discovery to specific types (e.g., `--scope skills,agents`). Default: all known shapes. |
| `--variant <hint>` | passthrough to `/assess-agent` | no | If the system has agents of a known variant, pass `prompt-based\|harness-based\|autonomous`. Defaults to per-artifact inference. |
| `--manifest-only` | flag | no | Produce the manifest only; skip per-artifact dispatch and summary. Useful for fast structural inventory. |
| `--diff <prior-manifest>` | path | no | Re-audit mode: compare against a prior manifest, surface drift. |

Defaults are tuned for the plain-English case: `audit-system ./some-folder` runs the full audit with auto-detection.

---

## Discovery contract (auto-detect by known shapes)

`/audit-system` walks the input path and looks for artifacts matching known shapes. Detection is **shape-based, not manifest-based** — the audited system needs no precondition.

### v1 shape table

| Shape | Detection | Dispatched to | Variant inference |
|---|---|---|---|
| Skill | `.claude/skills/*/SKILL.md` (any depth) | `/assess-skill` | n/a |
| Subagent file | `.claude/agents/*.md` (any depth) | `/assess-agent` | per-artifact, from content |
| Fractal agent | `agents/*/agent.md` (any depth) | `/assess-agent` | per-artifact, from content |
| System CLAUDE.md | `CLAUDE.md` in folder root or in any system subfolder | `/assess-agent` (variant A, spec-doc fork) OR `/assess-prompt` (if predominantly procedural) | content classifier |
| Standalone prompt | `prompts/*.md` or `system-prompts/*.md` (any depth) | `/assess-prompt` | n/a |

### Discovery rules

1. **Glob from the input path root recursively.** Do not follow symlinks beyond the target tree (avoid loops; safer for repos with workspace-root → fractal-home symlinks like the `meta-system-owner` mirror).
2. **De-duplicate by absolute resolved path** — if two glob hits resolve to the same inode, count once.
3. **Classify ambiguous artifacts.** A `CLAUDE.md` at a system root is typically a spec-doc + agent-disposition hybrid. v1 default: dispatch to `/assess-agent` (variant A); flag as ambiguous in the manifest so the human can override.
4. **Record what was NOT discovered.** If the input path contains a known structural marker (e.g., `agents/` folder per fractal pattern, but no `agent.md` files inside), note the gap in the manifest's `not_discovered` section. This is information, not a finding.

### Shape table extensibility

The shape table is the load-bearing surface. New shapes (e.g., hooks, workflows, MCP server configs) get added here as the consumer-abstractions-map promotes them from weak to strong demand. v1 covers the three abstractions IL maintains today (skill, agent, prompt).

---

## Composition model (subagent spawn per artifact)

### The pattern

For each discovered artifact, `/audit-system` invokes the appropriate IL `/assess-*` skill via the IL Librarian as a subagent in fresh context.

- IL `/assess-*` skills are SKILLS (Skill-tool invocable), not subagents (Agent-tool invocable).
- The IL Librarian agent is invocable as a subagent (`.claude/agents/librarian.md`, `name: librarian`).
- `/audit-system` spawns Librarian per artifact; tells Librarian "invoke `/assess-skill` on this path" (or `/assess-agent` or `/assess-prompt`).
- Librarian runs the skill in its own context, returns the assessment report.

### Why this shape

- **Rule 10 inverted application:** the orchestrator (`/audit-system`) is MetaSystem; the assessors are IL. Each assessor runs in fresh context — no cross-artifact leak, no orchestrator-task-leak.
- **Parallelizable.** Independent subagents can run concurrently. For an N-artifact system, the audit fan-out is bounded by harness concurrency limits, not orchestrator turn count.
- **Composable with existing substrate.** Librarian is already the home for `/assess-*`; reusing it costs nothing.
- **Clean context isolation.** /audit-system never loads /assess-* skill content into its own context; it stays focused on orchestration, manifest authoring, and summary synthesis.

### Trade-off accepted

Subagent spawn has per-artifact latency overhead. For small systems (≤5 artifacts) this is fine. For large systems (50+ artifacts) the overhead could matter — but rule 11 says: don't optimize until evidence demands. v1 commits to subagent-per-artifact unconditionally.

### Open implementation question (defer to session 114)

What does the spawn payload look like? Options:
- Librarian receives a structured task: `{skill: assess-skill, target: <path>}`.
- Librarian receives a natural-language prompt: "Run `/assess-skill` on `<path>` and return the report."

Both work. The NL form is more flexible (Librarian can interpret ambiguous targets); the structured form is more deterministic. Decide during build.

---

## Output contract: three artifacts

### Artifact 1 — Manifest

Structural inventory of what was discovered. YAML-fronted markdown. The audited system's surface area, declared by `/audit-system`.

```yaml
---
title: "<system-name> audit manifest"
audit_target: "<absolute or relative path>"
audit_date: "YYYY-MM-DD"
audit_session: "<session id if available>"
audit_version: "v1"
discovery_mode: "auto-detect"  # or "manifest-only"
---
```

Body:

```markdown
# Discovered artifacts

## Skills (N)
| Path | Name | Safety-critical | Assessed | Findings |
|---|---|---|---|---|
| `.claude/skills/foo/SKILL.md` | foo | no | yes | 3 (1 violated, 2 partial) |
| ... | | | | |

## Agents (N)
| Path | Name | Variant | Assessed | Findings |
|---|---|---|---|---|
| `.claude/agents/owner.md` | owner | B (harness-based) | yes | 5 |

## Prompts (N)
| Path | Type | Assessed | Findings |
|---|---|---|---|
| `prompts/example.md` | spec-doc | yes | 0 |

## Not discovered (structural gaps)
- `agents/` folder present but empty (expected per fractal pattern)
- No `governance/` folder (system may not follow fractal pattern)

## Ambiguous classifications
- `CLAUDE.md` at system root classified as agent (variant A) — content mix could justify prompt classification. Human override available.
```

### Artifact 2 — Per-artifact findings

Concatenation of each `/assess-*` report, with provenance.

```markdown
# Per-artifact findings

## Skill: `.claude/skills/foo/SKILL.md`
*Assessed via /assess-skill (Librarian subagent, fresh context)*

<full /assess-skill report verbatim>

---

## Agent: `.claude/agents/owner.md`
*Assessed via /assess-agent --variant B (Librarian subagent, fresh context)*

<full /assess-agent report verbatim>

---

## ...
```

### Artifact 3 — Whole-system summary

Top-level synthesis. NOT a score (per Nick's ruling). NOT a verdict. A scannable executive summary the audience archetypes 1–5 can consume at different depths.

```markdown
# Whole-system summary

## At a glance
- **N artifacts assessed** across M shapes (skills, agents, prompts)
- **K critical findings** (G9.I6 safety-critical violations, ContextSpec violations)
- **J structural gaps** (missing expected shapes per discovery)
- **Z ambiguous classifications** requiring human override

## Critical findings (deployment-blocking)
<list of safety-critical violations from /assess-skill G9.I6 and DD-92 ContextSpec from any assess-*>

## Common findings (cross-artifact patterns)
<de-duplicated themes — e.g., "3 of 5 skills missing argument-hint">

## Whole-system invariants (empty in v1 — see Future Work)
<placeholder>

## Re-audit guidance
<if --diff <prior> was passed, drift summary here>
```

### Output locations

| Artifact | Destination | Notes |
|---|---|---|
| Manifest | `<audit-target>/.audit/manifest-<date>.md` if writable, else conversation | Writable: creates `.audit/` if absent. Read-only target: conversation only. |
| Per-artifact findings | `<audit-target>/.audit/findings-<date>.md` if writable, else conversation | Same logic. |
| Whole-system summary | conversation always; mirrored to `<audit-target>/.audit/summary-<date>.md` if writable | Summary is the consumer-facing artifact. |

**Open question (defer to session 114):** Is `.audit/` the right convention? Alternatives: `.metasystem-audit/`, `audit-reports/`, or no on-disk output by default and require an explicit flag to write. Likely defer to first real use.

---

## Whole-system invariants (rule 11 — start empty)

Per Nick's ruling: v1 ships as pure composition. Whole-system invariants get added as recurring concrete evidence demands.

### Candidate list (deferred, not committed)

For reference only — these are what we *might* add when 2-3+ concrete instances surface:

| Candidate | Source | Trigger to commit |
|---|---|---|
| Cross-reference integrity (CLAUDE.md → agents/ contents match) | Drift detection during multiple audits | 2-3+ audits reveal drift |
| Fractal-pattern compliance (DD-52) | MetaSystem audits of incubator/graduated systems | 2-3+ audits surface fractal gaps that per-artifact checks miss |
| Audit/design symmetry (rule 12) | IL audit of MetaSystem; cross-system instance | Second instance after this session's application |
| Governance-source freshness (constitution last-updated vs derived rule docs) | Cross-system drift detection | 2-3+ instances |
| Engine subagent discoverability (sub-task 1's empirical concern, captured generically) | Recurring discovery-topology drift | 2-3+ systems with broken discoverability |

Rule 11 gates each: "Every check `/audit-system` adds beyond IL `/assess-*` composition needs concrete evidence (an observable invariant the per-artifact skills can't see)."

---

## Boundaries

- `/audit-system` does NOT modify the audited system. Read-only by contract.
- `/audit-system` does NOT propose changes — `/design-harness` is the constructive peer.
- `/audit-system` does NOT audit code logic, security, or runtime behavior. It audits agentic-system *structure* and per-artifact substrate.
- `/audit-system` does NOT audit systems that don't follow conventional shapes — the discovery contract is opinionated. Unknown shapes get noted as `not_discovered` and the human decides.
- `/audit-system` does NOT cross system boundaries by spawning across nested systems unprompted. If `<path>` is the workspace root, /audit-system audits the workspace; if `<path>` is `systems/improvement-loop/`, it audits IL only. Recursive sub-system audit is an `--recurse` flag for v2+.

---

## Audience archetypes (1–5)

| Archetype | What they consume | How |
|---|---|---|
| 1 — Nick-builder | Manifest + per-artifact findings + summary | Full depth; uses summary as scan, manifest as inventory, findings as detail |
| 2 — Portfolio-presenter | Summary | Citable: "X audited Y artifacts; Z critical findings" |
| 3 — Practitioner-friend | Summary + per-artifact findings | Selects relevant artifacts; reads /assess-* output |
| 4 — Builder-friend | Manifest + summary | Reuses shape detection; learns the discovery contract |
| 5 — Employer-evaluator | Summary + manifest | Inspects system structure; reads critical findings |

Output is layered to serve all five at different consumption depths. No archetype-specific output mode in v1.

---

## What v1 does NOT do (out of scope)

- **No re-audit baselining UI.** `--diff` works mechanically but v1 doesn't offer richer drift visualization.
- **No remediation suggestions.** `/audit-system` reports; `/design-harness` constructs; v2+ may pair them.
- **No cross-system aggregation.** Each invocation audits one path. Multi-system aggregation is a v2+ candidate (rule 11: evidence first).
- **No deployment gating.** `/audit-system` does not block deployment. Its output may inform a deployment check, but enforcement is upstream.
- **No assessment of IL substrate.** /audit-system uses IL `/assess-*`; it does not audit IL itself. (IL has `/system-audit` for that.)
- **No custom check authoring.** Whole-system invariants are gated through this design contract's deferred list, not authored ad-hoc per invocation.

---

## Implementation sequencing (for session 114+)

Suggested order of decisions in the build conversation:

1. **Resolve the spawn-payload shape** (structured vs. NL prompt to Librarian subagent).
2. **Decide `.audit/` output convention** (or alternative; or conversation-only default).
3. **Write the SKILL.md** — `argument-hint: "<path> [--scope <types>] [--variant <hint>] [--manifest-only] [--diff <prior>]"`; allowed-tools likely `Read Glob Grep Skill Agent Write`.
4. **Implement discovery** — glob-based scan with the shape table.
5. **Implement dispatch** — Librarian-subagent spawn per artifact.
6. **Implement aggregation** — concatenate /assess-* reports, build manifest, synthesize summary.
7. **Test against IL** — first real audit target. Surface gaps as design evidence.
8. **Test against MetaSystem itself** — second target. Surface fractal-pattern check candidacy if drift emerges.
9. **Rule-10 self-audit:** invoke a hypothetical `/audit-system` audit on itself once shipped — but the rule-10 binding for `/audit-system` itself is *future* (`/audit-system` is the assessor in the rule-10 chain; it doesn't have a constructive peer that delegates back to it on its own SKILL.md).

---

## Open design questions — RESOLVED in session 114

All six deferred questions resolved at build start:

1. **Spawn payload shape:** Structured task ("Run /assess-skill on <path>").
2. **Output location convention:** `<target>/audit-reports/<date>/` (visible, non-dotfile), **conversation-only by default**; `--write` opts in to persist. The opt-in default is the G9.I6 mitigation surfaced by session 114 self-audit.
3. **CLAUDE.md ambiguity:** `/assess-agent --variant prompt-based` by default; `--variant` overrides. Flag ambiguous in manifest.
4. **Subagent concurrency:** Parallel, bin-packed. **250k token ceiling per subagent.** Variant-aware substrate constants: `{skill: 18k, agent-A: 22k, agent-B: 32k, agent-C: 28k, prompt: 20k}`. First-fit-decreasing packing. Per-artifact overhead: 25k.
5. **Manifest schema versioning:** `audit_version: v1` literal; no compat scaffolding (rule 11).
6. **`--recurse` for nested systems:** Omitted in v1. Single-target audit only.

## Lessons from first real audit (session 114, MetaSystem)

The MetaSystem smoke test surfaced these gaps in the v1 SKILL.md, all patched
this session:

1. **Default exclude set was missing.** Discovery would have pulled in
   `watched-libraries/_tmp/repo-cache/*` vendored content. Codified excludes:
   `archive/`, `_tmp/`, `_cache/`, `node_modules/`, `.git/`, `reflections/`.
   Added `--exclude` flag for ad-hoc additions.

2. **G9.I6 self-audit catch.** `/audit-system` audited itself and flagged the
   Write step as missing a human-approval gate. Patched: `--write` flag with
   default-off. Conversation-only output is now the safe default.

3. **Spawn-prompt format compliance was imperfect.** Bin 1's Librarian
   subagent returned one report twice and dropped a path heading on the first
   artifact, because `/assess-*` reports carry their own `##` headings that
   collide with the orchestrator's path heading. Patched: spawn payload now
   uses literal sentinel delimiters (`<<<AUDIT-REPORT-START path="..." ...>>>`
   ... `<<<AUDIT-REPORT-END>>>`) which are robust against assessor heading
   hygiene.

4. **Three of five MetaSystem CLAUDE.md files came back as shape-mismatch
   latents.** `governance/proposals/CLAUDE.md`, `app/CLAUDE.md`, and
   `project-management/CLAUDE.md` are MOC/orientation docs, not agent specs.
   `/assess-agent --variant prompt-based` correctly returns "all guides
   latent" but a subagent is still spawned. **Not patched in v1** (rule 11:
   one system's evidence is not enough to commit to a discovery-time
   classifier). Watch for recurrence in IL audit; if pervasive, add a
   pre-dispatch heuristic on CLAUDE.md frontmatter (`type: index` →
   manifest-only, no dispatch).

5. **`Grep` was in `allowed-tools` but no step used it.** Trimmed.

6. **FAILURE SIGNAL section was absent (G8.I19 Partial).** Added explicit
   §"FAILURE SIGNAL" with named failure modes.

7. **State tracking is in-conversation only (G3b Partial).** Acknowledged
   as a v1 limitation; resumability deferred to v2 evidence.

## Original open questions (kept for traceability, all resolved above)

1. **Spawn payload shape.** ✅ Structured task.
2. **Output location convention.** ✅ `audit-reports/<date>/`; conversation default; `--write` opts in.
3. **CLAUDE.md ambiguity.** ✅ Variant A default; `--variant` overrides.
4. **Subagent concurrency.** ✅ Parallel, bin-packed, 250k ceiling.
5. **Manifest schema versioning.** ✅ Literal `v1`; no compat scaffolding.
6. **`--recurse` for nested systems.** ✅ Omitted in v1.

---

## Cross-references

- Capability roadmap: `systems/meta-system/project-management/capability-roadmap.md`
- IL `/assess-skill`: `systems/improvement-loop/.claude/skills/assess-skill/SKILL.md`
- IL `/assess-agent`: `systems/improvement-loop/.claude/skills/assess-agent/SKILL.md`
- IL `/assess-prompt`: `systems/improvement-loop/.claude/skills/assess-prompt/SKILL.md`
- IL Librarian agent: `systems/improvement-loop/agents/librarian/agent.md` + `.claude/agents/librarian.md`
- IL `audit.md` operation: `systems/improvement-loop/operations/references/librarian/audit.md`
- Consumer abstractions map: `systems/improvement-loop/operations/references/consumer-abstractions-map.md`
- Rule 10 (generator-assessor separation), Rule 11 (abstractions earn keep), Rule 12 (audit/design symmetry): `systems/improvement-loop/governance/agent-rules.md`
- Sub-task 1 SL entry (session 113 — harness discovery): `systems/meta-system/operations/system-log/` (this session)

---

## Status

**Stable.** Session 113 produced the draft; session 114 resolved
all six deferred questions, wrote the SKILL.md, ran the MetaSystem smoke
test, patched the SKILL.md and this contract per first-audit evidence.
Session 115 ran the second canonical audit (IL — 43 artifacts, 9 bins) and
landed two more patches: (a) audit-trail one-line append to
`audit-reports/runs.md` on `--write` (resolves session-114 finding #22);
(b) discovery-time MOC pre-filter for CLAUDE.md with `--include-mocs`
override (resolves session-114 candidate #3 after IL surfaced 3 confirmed +
3 suspected MOC latents — cumulative ≥6 across two systems, rule-11 threshold).

Stage advances `stable-after-il-test → stable` per session-115 outcome.

**One unresolved v2 candidate**: bins 2 and 4 of the IL audit each emitted only
1 of N expected sentinel-delimited reports (large-skill bins; subagent likely
hit single-message output budget and emitted progress per artifact, with only
the final message reaching the orchestrator). 7 of 43 artifacts went
unassessed. The substantive v2 fix likely requires a per-bin total-output
budget (not just total-input), constraining packing to keep total expected
report volume under the subagent's response budget. Spawn-payload tweaks alone
are unlikely to close this. Not patched in v1 — logged as v2 candidate, watch
for recurrence on the next audit target.

SKILL.md: `systems/meta-system/.claude/skills/audit-system/SKILL.md`.
First-run outputs (MetaSystem): `systems/meta-system/audit-reports/2026-06-12/`.
Second-run outputs (IL): `systems/improvement-loop/audit-reports/2026-06-12/`.
