---
name: Governance Registry — Classify Every Behavior-Shaping File by Edit Blast Radius
summary: One registry file classifies every behavior-shaping file in the workspace as governance (deliberate, human-in-the-loop edits) or working/notes (autonomous edits fine), with reasoning. It makes
  the side-effect guard executable — before editing, an agent looks up the file's tier instead of guessing — and gives audits a completeness target (every root doc classified). The registry classifies itself
  as governance (self-referential guard).
implementation_notes: The engine approximates this implicitly (DDs immutable, generated files, PROGRESS.md owned by /session-handoff) but has no single lookup an agent can consult before editing. A registry
  file in governance/ classifying the engine's behavior-shaping surfaces (CLAUDE.md files, rules, skills, agent definitions, FOUNDATIONS.md, PROGRESS/HISTORY, templates) would make the human-gate rule mechanically
  checkable and give /system-audit a completeness target. Low cost, direct adoption; also a natural wiring row (required tier) in the portable governance kernel.
category: Governance
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P1 (Direct Adoption)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-wiring-canon.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
tags:
- governance-registry
- blast-radius
- autonomy-tiers
- human-gate
---
# Governance Registry — Classify Every Behavior-Shaping File by Edit Blast Radius

## What It Is

A single registry file that classifies every behavior-shaping file in the workspace into
exactly two tiers — **governance** (deliberate, human-in-the-loop edits only) or
**working/notes** (autonomous agent edits fine) — with the reasoning per entry. It is
the lookup table that turns a prose autonomy rule ("governance files are
human-in-the-loop") into something an agent can actually execute before touching a file.

## Why It Matters

Plain English: agent autonomy is only safe when the blast radius of an edit is known
*in advance*. Most systems state the rule ("don't touch governance files without
approval") but never enumerate which files those are, so the agent guesses — and guesses
drift. A registry replaces guessing with lookup, and it converts "is our governance
surface complete?" into an auditable completeness check: every root doc must appear in
the registry, enforced by a script.

## How It Works

- **Two tiers, reasoning attached.** The governance side covers at minimum: the
  always-on entry file, path-scoped rules, skill packages, planning/vision docs
  (PRD, ARCHITECTURE), the durable ledgers, memory guardrails, and the wiring canon
  itself. The working side names the surfaces agents may edit autonomously — session
  control surfaces (PROGRESS/HISTORY tracks), draft artifacts, session memory.
- **Self-referential guard:** the registry is itself classified as governance, so the
  classification scheme cannot be loosened autonomously.
- **Executable pre-edit check:** the always-on side-effect guard points at the
  registry; before an autonomous edit, the agent checks the target file's tier rather
  than inferring risk from the file's name or content.
- **Audit completeness target:** a doc-audit script enforces "every root doc
  classified" — new behavior-shaping files that skip registration fail the audit, so
  the registry cannot silently fall behind the tree.
- **Portability:** the registry is harness-neutral prose that travels with the
  workspace as-is ("a pointer, not a copy"); only its path convention is
  platform-delegated. In the system contract it is a *required* wiring row — the
  human-approval channel it depends on has no fallback.
- Placeholder discipline: user-scoped entries use `{user-id}` path forms, keeping the
  registry itself exportable.

## How It Could Fail

A registry nobody consults is dead weight — the pre-edit lookup must be wired into the
always-on guard or an enforcement hook, not left as documentation. Binary tiers can be
too coarse (some files want "autonomous but reviewed"); resist adding tiers until
recurrence demands it. Without the completeness audit, the registry decays into a
partial list that gives false confidence — the audit is load-bearing, not optional.
