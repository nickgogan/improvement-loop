---
id: "audit-system-skill-shipped-metasystem-smoke-test"
title: "/audit-system v1 SKILL.md shipped; MetaSystem smoke test surfaced G9.I6 self-violation + design gaps; SKILL.md and design contract patched"
date: "2026-06-12"
session: 114
system: "meta-system"
type: "milestone"
agents:
  - "Owner"
tags:
  - "step-g"
  - "audit-system"
  - "skill-shipped"
  - "first-real-audit"
  - "g9-i6"
  - "self-audit"
  - "rule-10"
  - "rule-11"
related_artifacts:
  - ".claude/skills/audit-system/SKILL.md"
  - "project-management/design-notes/2026-06-12-audit-system-design-contract.md"
  - "audit-reports/2026-06-12/manifest.md"
  - "audit-reports/2026-06-12/findings.md"
  - "audit-reports/2026-06-12/summary.md"
roadmap_step: "Cross-system Step G (in progress)"
---

# /audit-system v1 shipped; MetaSystem smoke test executed

Session 114 implemented `/audit-system` per the session-113 design contract, ran the MetaSystem smoke test as the first real audit, and patched the SKILL.md plus design contract from first-audit evidence. IL audit deferred to session 115 against the patched skill.

## What happened

### Six deferred questions resolved up front

All six implementation questions from the design contract resolved in a single up-front batch with Nick:

1. Spawn payload: structured task.
2. Output location: `audit-reports/<date>/` visible (non-dotfile).
3. CLAUDE.md ambiguity dispatch: `/assess-agent --variant prompt-based` default; `--variant` overrides.
4. Subagent concurrency: parallel, bin-packed, **250k token ceiling per subagent** (Nick: ceiling not floor, to avoid context rot). Variant-aware substrate constants: `{skill: 18k, agent-A: 22k, agent-B: 32k, agent-C: 28k, prompt: 20k}`. First-fit-decreasing packing.
5. Manifest schema versioning: `audit_version: v1` literal.
6. `--recurse`: omitted in v1.

The concurrency conversation evolved through three Nick interventions: (a) parallel-by-default with token bins; (b) ceiling-not-floor correction (anti-context-rot); (c) accounting for tool-call + analysis context not just file reads (250k chosen as the conservative ceiling).

### v1 SKILL.md written

`systems/meta-system/.claude/skills/audit-system/SKILL.md` shipped with 8-step procedure: parse input → discover (5 shapes) → size + variant-aware estimate → FFD bin-pack → build manifest → parallel Librarian dispatch → aggregate → write outputs.

### MetaSystem smoke test ran

`/audit-system systems/meta-system/` discovered 8 artifacts (1 skill, 2 agents, 5 CLAUDE.md), packed into 2 bins (212.5k + 187.0k), dispatched two Librarian subagents in parallel, aggregated 8 reports (with format anomalies — see gaps), and wrote `audit-reports/2026-06-12/{manifest,findings,summary}.md`.

## Critical findings the test surfaced

**1. `/audit-system` self-audited and caught its own G9.I6 violation.** The skill writes manifest/findings/summary files without an explicit human-approval gate — `/assess-skill` correctly flagged this as a deployment-blocking violation under G9.I6 (destructive/irreversible actions always require human approval regardless of trust level). The skill caught its own bug.

**2. `.claude/agents/owner.md` — harness write scope absent.** The MetaSystem Owner's "never modify another system's files" rule lives only in prose; `allowed_tools` doesn't path-restrict Write/Edit/Bash. A bug or hallucination could cross the boundary unobstructed.

## SKILL.md gaps surfaced and patched this session

1. **Default exclude set was missing.** Discovery would have audited 14+ vendored repos in `watched-libraries/_tmp/repo-cache/`. Codified excludes: `archive/`, `_tmp/`, `_cache/`, `node_modules/`, `.git/`, `reflections/`. Added `--exclude` flag.
2. **G9.I6 violation fix.** Added `--write` flag with **default-off**. Conversation-only output is now the safe default; on-disk persistence requires explicit consumer opt-in.
3. **Spawn-prompt format compliance was imperfect.** Bin 1 returned one report twice and dropped a path heading on the first artifact — `/assess-*` reports carry their own `##` headings which collide with the orchestrator's path heading. Patched: spawn payload now uses literal sentinel delimiters (`<<<AUDIT-REPORT-START path="..." ...>>>` ... `<<<AUDIT-REPORT-END>>>`).
4. **`Grep` was in `allowed-tools` but no step used it.** Trimmed.
5. **FAILURE SIGNAL section absent (G8.I19 Partial).** Added explicit §"FAILURE SIGNAL" with named failure modes.

## Design contract updates

`systems/meta-system/project-management/design-notes/2026-06-12-audit-system-design-contract.md` advanced `draft → stable-after-il-test`. All six original deferred questions resolved (documented inline with the choice). New §"Lessons from first real audit (session 114)" captures the 7 patched gaps plus the deferred-but-watched item (CLAUDE.md MOC shape mismatch).

## What was NOT patched (rule 11 deferrals)

- **MOC CLAUDE.md shape mismatch.** Three of five MetaSystem CLAUDE.md files (`governance/proposals/`, `app/`, `project-management/`) came back as all-guides-latent under `/assess-agent --variant prompt-based`. A discovery-time content classifier (skip if `type: index`) would prevent wasted subagent budget. **Not patched in v1** — one system's evidence isn't enough to commit (rule 11). IL audit in session 115 is the second instance test.
- **State tracking is in-conversation only (G3b Partial).** No on-disk checkpoint for resumability. Acknowledged as v1 limitation; defer to evidence of multi-bin context loss.
- **Whole-system invariants remain empty** per rule 11.

## IL audit deferred to session 115

Nick chose to defer IL audit (~9 bins, ~1.6M subagent tokens) until the SKILL.md and design contract were patched from MetaSystem evidence. Rule 11: don't burn compute against a skill with known v1 gaps; fix the gaps, then run IL fresh as the second canonical test against the patched skill.

## Telemetry

- Session 114 turns: ~30
- Subagents spawned: 2 (parallel)
- Subagent wall-clock: ~3 min
- Subagent total token consumption: ~340k (well under 2 × 250k ceiling)
- MetaSystem artifact count: 8 (1 skill, 2 agents, 5 CLAUDE.md)
- MetaSystem bin count: 2
- Format-compliance gaps from bin 1: 1 (duplicate report + missing heading); fixed via sentinel delimiters

## Next

Session 115 priorities (in order):
1. Run `/audit-system systems/improvement-loop/` against the patched skill. Surface any new design gaps; advance contract stage to `stable` if clean.
2. Address `/audit-system` audit-trail gap (finding #22: no SL entry on each run). Likely add a brief run-log append.
3. Decide on MOC CLAUDE.md classifier (rule-11 trigger: if IL also shows 3+ MOC mismatches, commit the heuristic).
4. Optional: harness `§Construction` backfill (Nick-gated; still queued).
