---
name: 'Operational Quirks Discipline — Recurrence-to-Guard, Harness Labels, Permissioning Honesty'
summary: 'A standing discipline for runtime sharp edges: an environment failure that recurs is promoted to a standing guard (in the always-on file if it can fire on any request, otherwise the relevant memory scope), stated as the durable rule plus the failure it prevents. Every such guard is labeled harness-specific so a future port re-derives rather than copies it, and a new install starts with an empty quirk list plus the discipline. Paired with permissioning honesty: where the platform lacks native enforcement, the guard is carried as prose and the install report must say which guards are prose-only.'
implementation_notes: 'The engine accumulates quirk knowledge informally (e.g. the retired read-guard hook, zsh/tool quirks in memory). Adoptable directly: (1) the recurrence threshold — first occurrence is tolerated, recurrence earns a guard — matches Nick''s standing tolerate-one-off rule and gives it a promotion path; (2) the harness-specific label keeps the portable kernel clean, since quirks never port; (3) permissioning honesty belongs in the kernel''s trust declaration — the engine currently runs bypassPermissions, so nearly all its guards are prose-only and should be declared as such.'
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
pipeline_status: raw
consumed_by: []
tags:
- operational-quirks
- standing-guards
- permissioning-honesty
- harness-specific
---
# Operational Quirks Discipline — Recurrence-to-Guard, Harness Labels, Permissioning Honesty

## What It Is

The pattern for handling runtime-specific sharp edges — tool bugs, shell quirks,
permissioning gaps — as a *discipline* rather than a list. The canon is explicit that
the pattern is portable and the quirks are not: "quirks are inherently harness-specific
and never port." Four rules: recurrence→guard promotion, harness-specific labeling,
permissioning honesty, and portable workspace tooling.

## Why It Matters

Plain English: every runtime has sharp edges, and they are discovered by bleeding on
them — left unrecorded, the same edge cuts every future session. But recording them
naively creates two opposite failures: guard bloat (a rule per one-off) and false
portability (copying another platform's quirk guards into a new install where they are
noise). The discipline threads both: only recurring failures earn guards, every guard
names the failure it prevents, and every guard is labeled as harness-specific so a port
starts clean. The honesty rule adds a third protection: never let prose guards
masquerade as enforcement.

## How It Works

- **Recurrence → guard:** an environment failure that recurs gets promoted to a
  standing guard — placed in the always-on file if it can fire on any request, in the
  relevant memory scope otherwise — stated as the durable rule *plus the failure it
  prevents* (so future sessions can judge whether it still applies).
- **Label discipline:** every such guard is marked harness-specific so a future adapter
  knows to re-derive rather than copy it. A new install starts with an **empty** quirk
  list plus this discipline — the list never ports, the pattern always does.
- **Permissioning honesty:** where the platform lacks native enforcement (per-skill
  side-effect gates, tool restrictions), the equivalent guard is carried as prose in
  the always-on file and skill bodies — and the install report must state which guards
  are prose-only on this platform. In the system contract this is promoted to a
  first-class `trust` declaration: boundary, threat non-goals, containment menu
  (containers/VMs, restricted remotes, native gates where available), and declared
  absences. This is also the contract's one *upgrade-direction* wiring row: a host with
  native permission gates may replace prose guards with enforcement — never the
  reverse.
- **Portable tooling:** validation/audit scripts are plain local scripts (no network,
  no platform APIs) and move with the repo; only *what invokes them* is platform
  business.
- Concrete examples of promoted guards (from the source's VS Code Copilot install):
  single-line terminal commands only (multi-line quoting mangled); repo-memory
  stranding on workspace rename → mandatory memory check in every rename/clone step.

## How It Could Fail

Without the recurrence threshold, the quirk list becomes the context-rot rule pile.
Guards recorded without their triggering failure become unfalsifiable superstition no
session dares delete. Skipping the honesty declaration is the dangerous failure: a
receiving installer assumes enforcement exists, grants autonomy accordingly, and the
prose guard fails exactly when it matters.
