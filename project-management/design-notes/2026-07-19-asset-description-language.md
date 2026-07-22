---
title: "Asset-description language v0 — portable machine-readable self-description of engine assets"
id: "asset-description-language-2026-07-19"
type: "design-note"
category: "self-description"
target_system:
  - "improvement-loop"
stage: "stable"
created: "2026-07-19"
updated: "2026-07-22"
author: "claude"
source_dd:
  - "DD-124"
tags:
  - "design-note"
  - "owner"
  - "self-description"
  - "portability"
  - "E3"
---

# Asset-Description Language v0

**Status: RULED (DD-124, 2026-07-22).** Nick ruled the §7 questions in a
question-by-question interview: wiring rows ship now as
`governance/system-contract.yaml`; per-asset records defer to E3's build (schema
stays ruled here); all five `required` tiers stand; the record-layer questions
re-open at E3. §7 below records the rulings. Originally drafted autonomously under
the Nick-ruled queue (2026-07-18, item 1). Amended 2026-07-20 after an
adversarial review pass (fresh-context critic; verdict ACCEPT-WITH-AMENDMENTS): the
agent-class extension, two missing wiring rows, the Layer-2 staging honesty, and the
expanded §7 gate list all originate from that critique. This note is the spec-before-
build artifact for the portable JSON/YAML asset-description language. It pulls epic
E3 forward: E3's acceptance criteria (prd.md §E3) fix the end-state — a ruled
descriptor schema, one YAML per agent and per harness under a root descriptor, and a
deterministic check a seeded violation fails. This note proposes the language those
instances will be written in. Nothing here deploys; no DD is filed until Nick rules.

**Plain English.** Today, "what is the engine made of and what does it need from its
harness" lives in prose spread across CLAUDE.md files, governance docs, and Nick's
head. Anyone — a future harness port, a meta-skill, a foreign agent deciding whether
to adopt an engine export, or the Owner waking actors off work queues — must do
archaeology to answer it. The asset-description language turns that answer into
machine-readable files: every asset states where it lives, when it loads, what job it
does, who owns it, and what it demands of the harness — so a port becomes a checklist
with pass/fail semantics instead of a rewrite, and the E4 harness and E5 kernel
compiler get a substrate they can check mechanically.

---

## 1. What counts as an engine asset

Enumerated from the live filesystem (2026-07-19). The inventory is the *class* list —
v0 does not commit to describing every instance of every class (see §7 open
questions). Counts are deliberately absent (workspace Process Rule: no hardcoded
counts); the filesystem is the census.

| Asset class | `class` enum value | Where it lives today | Notes |
|---|---|---|---|
| Agents | `agent` | `agents/{owner,researcher,codifier,librarian}/` + workspace `.claude/agents/*.md` | dual materialization: definition dir + harness subagent stub |
| Skills | `skill` | `systems/improvement-loop/.claude/skills/` (engine, DD-109) + workspace `.claude/skills/` (cross-system) | |
| Rules | `rule` | `.claude/rules/governance.md`, `governance/*-rules.md` | harness-injected vs engine-law |
| Hooks | `hook` | git `pre-commit` (symlink → `operations/kb-maintenance-scripts/hooks/`), `settings.json` UserPromptSubmit → `capture_query.py` | two hook substrates: git and harness |
| Kernel docs | `kernel-doc` | `governance/constitution.md`, `prd.md`, `actors.md`, `FOUNDATIONS.md` (generated) | the export unit's core |
| Governance databases | `gov-db` | `project-management/design-decisions/`, `implementation-backlog/` | frontmatter is source of truth |
| Knowledge | `knowledge` | `knowledge/{guides,patterns,templates,reference,schematics}/` + `extracts/` (two bodies, DD-111) | |
| Session-ops spine | `ops-surface` | `PROGRESS.md`, `HISTORY.md`, git conventions | behavior enforced by pre-commit hook |
| Self-store | `ops-surface` | `operations/self/` (lessons, demand ledger, store checker) | shares the `ops-surface` class with the spine |
| Memory surfaces | `memory-surface` | harness auto-memory dir (`~/.claude/projects/…/memory/`) | **stubbed in v0** — E1 names these; the schema carries the field empty, mirroring E3's declared dependency on E1 |

Two observations drive the design. First, the engine is **already folder-shaped**
(DD-52 fractal; agent-as-directory DD-82): class membership is largely decidable from
path. Second, several description layers **already exist** and must be reused, not
duplicated: DD-78 ContractSpec and DD-92 ContextSpec on artifacts, skill frontmatter
(`name`/`description`/`allowed-tools`), DD/IB frontmatter, and `_schema.yaml`.

## 2. Prior art and the wiring-stance ruling (proposed)

The KB carries a flagged `contradicts` tension between two answers to "how do the
parts of a multi-file agentic system stay wired to their description":

- **Explicit wiring rows** — `machine-readable-system-contract-with-wiring-rows`
  (template: `system-contract-wiring-row-schema`). One row per harness-integration
  concern; row key `concern` plus five fields: `tier` (required|optional),
  `capabilities` (IDs from a controlled vocabulary), `purpose`, `degradation`,
  `invariant`. Hash manifest over wired files detects contract-vs-reality drift.
  YAML is generated by a gated skill, never hand-edited. Evidence: one production
  system's design-gate verdict; the per-row invariant column has no prior art in the
  A2A/MCPB/OASF survey.
- **Implicit folder discovery** — `agent-as-folder-compiled-to-manifest` (Vercel
  Eve; template: `agent-folder-skeleton`). Inclusion is structural — a file in the
  right folder — and a compile step produces one manifest; the entry point references
  nothing. Evidence: active multi-thousand-star framework. Known failure modes:
  silent misplacement, no drift surface, legibility loss at scale.
- **Named-registry declaration** — `declarative-agent-spec-with-serialization-registry`
  (pydantic-ai AgentSpec): every part declares a stable serialization name; parts that
  can't round-trip opt out honestly rather than failing at load.

**Proposed ruling — discover-then-declare hybrid, each stance at the layer where its
evidence is strong:**

1. **Inventory is discovered** (Eve's move) — *from v2, when the compile step
   exists*. A compile step walks the fractal folders and derives the asset inventory
   from path conventions; the engine should not hand-maintain a census of a skill
   corpus git already knows. **Staging honesty:** until that compiler ships, every
   record is hand-authored — v0/v1 records are *declared, compiler-verified later*.
   The Eve invariant ("the compiled manifest, not a re-read of the tree, is
   authoritative") activates at v2, not before. The judgment fields (`who_owns`,
   `misuse_risk`, `wiring_refs`) can never be discovered from paths at any version;
   their source of truth is a §7 ruling.
2. **Harness wiring is declared** (wiring-row move). What the engine *requires from a
   harness* cannot be discovered from folders — required-vs-optional, degradation
   paths, and invariants are judgments. These are explicit five-field rows, gated and
   versioned. Auditability is constitutional (Faithful reporting; DD-29 gates), and
   gated regeneration + drift hashing are established engine habits (FOUNDATIONS.md,
   `manifest-hash-drift-detection-for-derived-docs`).
3. **Registry honesty at the boundary** (AgentSpec's move). Anything the language
   cannot fully express (e.g. a hook's script behavior) declares itself
   `described: partial` with a mandatory `pointer` to where the rest lives, instead
   of pretending the YAML is complete.

This resolves the `contradicts` link deliberately: Eve is right about *inventory*,
the wiring canon is right about *requirements*, and the tension dissolves once the
two jobs are separated.

**The single-harness warning, answered.** The wiring-canon finding's own failure
mode — "for a single-harness system, canon + adapter is a layer without a second
consumer" — applies here and is not dodged: the engine runs on one harness today.
The named consumers that justify the layer anyway are not a hypothetical second
platform but committed epics: E3's AC consumes the schema directly, E4's enforcement
points are enumerated in the harness descriptor, E5 compiles from it, and the
port/reharness meta-skills are the Nick-ruled goal of this queue item (2026-07-18
expansion). If Nick rejects that reasoning, the fallback is Layer 3 alone (wiring
rows, no per-asset records) — see §7 Q1.

## 3. The language — three layers

YAML-authored, JSON-equivalent (no YAML-only features: no anchors, no tags), so
"JSON/YAML" is satisfied by one grammar with two serializations. Portability follows
the three-section canon split (`wiring-canon-abstract-then-adapt-doc-structure`):
every field is classified **canon** (harness-neutral, required everywhere),
**adapter-delegated** (per-harness value), or **harness-specific** (illustration,
never requirement).

### Layer 1 — root system descriptor (`engine.yaml`, one per system)

The card-over-manifest fusion from the KB finding, minus what the engine doesn't
need yet (Occam). Identity and trust are **pointers into the kernel docs**, never
restatements (route-then-compact) — only declared absences are stated inline,
because omission is exactly what a pointer can't express:

```yaml
system:
  id: improvement-loop
  schema_version: "0.1"        # canon — PRD names schema versioning as the lock-in mitigation
  identity_ref: governance/constitution.md          # canon — objective, constraints, stop rules live there
  trust_ref: governance/constitution.md             # canon — DD-29 human-gate boundary lives there
  declared_absences: []        # canon — inline by design: what the system does NOT enforce
composition:                   # v2: generated by the compile step; v1: declared per Layer 2
wiring:                        # declared — harness requirements, per Layer 3
harness:                       # adapter-delegated — one block per target; claude-code first
```

### Layer 2 — per-asset record (declared in v0/v1; compiler-verified from v2)

Seeded from the wave-4 per-control record (where-lives / when-loads / what-job /
who-owns / evidence / misuse-risk), which the triage report already named as the
candidate seed for this schema. Two deliberate deltas from the seed: the `evidence`
field is dropped (engine assets are not research artifacts — their evidence is git
history and the KB citations already on them), and `misuse_risk` is kept verbatim.

**Reuse-by-pointer rule (canon):** any field whose value already exists on the asset
(skill frontmatter description, DD-78/DD-92 blocks, DD frontmatter) is a `ref:`, not
a copy. Inline prose is permitted only for asset classes that lack a description
surface of their own (hooks, ops-surfaces). This keeps the record a thin
ownership-and-wiring sidecar, not a parallel corpus restating description semantics.

```yaml
asset:
  id: session-handoff            # stable slug
  class: skill                   # canon enum: agent|skill|rule|hook|kernel-doc|gov-db|knowledge|ops-surface|memory-surface
  where_lives: .claude/skills/session-handoff/SKILL.md   # adapter-delegated (path is harness-materialized)
  what_job: "ref:frontmatter.description"    # reuse-by-pointer — skills state their own job
  when_loads: "ref:frontmatter.description"  # skills carry their own triggers; inline only for classes that don't
  who_owns: owner                # canon — actor slug from actors.md, or nick | unassigned
  described: full                # canon enum: full | partial
  pointer: null                  # canon — required (non-null) when described: partial
  misuse_risk: "mid-session or manual PROGRESS edits bypass Process Rule 2"  # canon — no existing surface states this
  contract_ref: frontmatter      # pointer to the asset's DD-78/DD-92 blocks — never restated here
  wiring_refs: [skill-registry, session-spine, commit-gate]  # every Layer-3 row this asset depends on
  memory: null                   # stub — E1 fills the field; schema carries it now
```

**Class extension — `agent` (required when `class: agent`).** E3's acceptance
criteria require each actor's callable tools, resources held, access rights,
execution access, and memory system stated machine-readably, with the spot-check
"a reader given only the YAML can list each agent's tools and access." The common
record above cannot carry that; agents get an extension block, seedable from the
actors.md tables:

```yaml
  agent:
    tools: []                    # canon — callable skills/tools, by slug
    resources: []                # canon — data surfaces held (KB, governance DBs, …)
    access_rights: []            # canon — read/write scopes (DD-30/DD-80 boundaries)
    execution_access: ""         # canon — how it runs: default-disposition | subagent | scheduled
    memory: null                 # canon — per-actor memory surfaces; E1 fills
```

Other classes may earn extensions the same way (recurrence evidence first); none are
proposed in v0.

### Layer 3 — wiring rows (declared, one per harness-integration concern)

Adopted unchanged from the staged template `system-contract-wiring-row-schema`
(row key `concern` plus five fields: tier, capabilities, purpose, degradation,
invariant; a `required` row names its minimum satisfier inside the degradation
string and carries no fallback path). The controlled capability vocabulary starts
minimal — only IDs the engine actually uses (§4) — and grows by gated addition.

## 4. Worked instance A — the engine's own wiring rows

Per the source finding's implementation note ("start by enumerating the engine's own
wiring rows before formalizing YAML"). Enumerated from the live install. **Tiers
ruled 2026-07-22 (DD-124): all five `required` rows stand** — Nick kept
`commit-gate` and `skill-registry` as hosting preconditions despite their imaginable
degradations. The live rows are now canonical in `governance/system-contract.yaml`;
the block below is the design-time record.

```yaml
wiring:
  - concern: always-on-entry
    tier: required
    capabilities: [always-on-instruction-injection]
    purpose: "workspace + engine CLAUDE.md injected into every session"
    degradation: "none — minimum satisfier: the agents.md convention"
    invariant: "an agent in any session can state the human-gate rule (DD-29) without being asked to read a file"
  - concern: human-approval-channel
    tier: required
    capabilities: [human-approval-channel]
    purpose: "DD-29 human gate at every stage boundary — the engine recommends and stages; Nick promotes"
    degradation: "none — minimum satisfier: a blocking review turn in the primary session channel"
    invariant: "no artifact crosses a stage boundary into a live surface without a recorded human decision"
  - concern: scoped-rules
    tier: optional
    capabilities: [path-scoped-rule-injection]
    purpose: ".claude/rules/governance.md auto-applies workspace-wide"
    degradation: "fold rules into the always-on file; record the weaker guarantee"
    invariant: "governance process rules reach every session that touches governed paths"
  - concern: skill-registry
    tier: required
    capabilities: [named-skill-invocation]
    purpose: "system-scoped (DD-109) + workspace skills discoverable and invocable by slug"
    degradation: "none — minimum satisfier: by-name dispatch from a single prose skill index in the always-on file"
    invariant: "each pipeline stage is invocable by name and carries its own gate discipline"
  - concern: commit-gate
    tier: required
    capabilities: [pre-commit-hook-execution]
    purpose: "git pre-commit enforces frontmatter validity, FOUNDATIONS sync, PROGRESS line budget, self-store check"
    degradation: "none — minimum satisfier: any pre-write validation hook point (git hook or harness pre-tool hook)"
    invariant: "a schema-invalid governance file cannot enter the git history"
  - concern: prompt-capture
    tier: optional
    capabilities: [session-lifecycle-hooks]
    purpose: "UserPromptSubmit hook appends to the self-store query ledger"
    degradation: "manual /self-improve capture; demand signal gets sparser, not absent"
    invariant: "no silent capture gaps — a prompt lands in the ledger or the active degradation (manual capture) is the recorded state"
  - concern: external-connections
    tier: optional
    capabilities: [external-service-connections]
    purpose: "MCP servers (Perplexity research, Context7 docs, Notion ops) plus the settings.json permission allow/deny surface"
    degradation: "web-fetch/CLI equivalents or manual research; the permission surface degrades to prose rules"
    invariant: "external calls stay within the declared allow-list, whatever mechanism enforces it"
  - concern: memory-store
    tier: optional            # provisional — E1 may promote to required
    capabilities: [scoped-memory-store]
    purpose: "harness auto-memory persists user/feedback/project facts across sessions"
    degradation: "PROGRESS.md + memory-shaped files in-repo (structural-memory value)"
    invariant: "no learning lives only in conversation history"
  - concern: subagent-dispatch
    tier: optional
    capabilities: [subagent-spawn]
    purpose: "skill passes and audits run as subagents (session-137 ruling)"
    degradation: "inline execution; slower, context-heavier, same outputs"
    invariant: "generator-assessor separation survives — the generator never grades its own output"
  - concern: session-spine
    tier: required
    capabilities: [version-control-substrate]
    purpose: "git carries the atomic log; HISTORY.md + PROGRESS.md ride on it"
    degradation: "none — minimum satisfier: any content-addressed VCS with commit metadata"
    invariant: "shipped work is reconstructible from commits without conversation history"
```

## 5. Worked instance B — per-asset record

The `/session-handoff` skill record shown in §3 Layer 2 is real, verified against
`SKILL.md` frontmatter and workspace Process Rule 2. Under the reuse-by-pointer rule
it demonstrates the intended thinness: `what_job` and `when_loads` are refs into the
skill's own frontmatter (which already states both); the record's net-new content is
ownership, the three wiring dependencies (`skill-registry` to be invocable,
`session-spine` because the skill *is* the spine's reconciler, `commit-gate` because
the PROGRESS line budget it answers to is hook-enforced), and the misuse risk. Its
`who_owns: owner` is itself an instance of §7 Q6 — the skill is workspace-scoped
while the Owner is an engine actor; `nick | unassigned` exist in the domain for
assets no actor owns.

## 6. Deterministic check (contract sketch — v1 deliverable, not deferred)

E3's AC requires the check ("a deterministic check exists and a seeded schema
violation fails it"), so it ships with the v1 instances, not with the v2 compiler.
Mirrors E1's store-check pattern:

- `check_descriptors.py` validates: every Layer-2 record against the schema (closed
  enums, required fields); `described: partial` ⇒ non-null `pointer`;
  `class: agent` ⇒ the agent extension block present and non-empty; every wiring row
  carries the row key plus exactly five fields; every `required` row's degradation
  matches `none — minimum satisfier: …`; every capability ID is in the vocabulary;
  every `who_owns` is an actors.md slug or `nick`/`unassigned`; every `wiring_refs`
  entry resolves to a row; `schema_version` present at the root.
- **Seeded-violation test:** a fixture descriptor with a deliberate violation (e.g. a
  required row carrying a fallback degradation) must fail the check.
- Drift: a hash manifest over wired files (per the KB template's pairing) — deferred
  to the compile step (v2, E5 seam).

## 7. Rulings (interview 2026-07-22 — DD-124)

**Ruled roadmap:** v0 = `governance/system-contract.yaml` (root descriptor + ten
wiring rows) — **shipped with the ruling** → v1 = per-asset records + agent
extensions + `check_descriptors.py` with the seeded-violation fixture, built as
part of E3 (memory fields filled by E1) → v2 = compile step (inventory becomes
generated) + drift-hash manifest (E4/E5 seam).

1. **Stance — RULED: wiring rows now.** The hybrid is accepted at Layer-3 scope;
   the per-asset record layer (Layer 2, including the reuse-by-pointer rule and the
   agent class extension) stays ruled *schema* in this note but is not instantiated
   until E3's build. Rationale: queue item 1 asked to *begin* the language; the
   rows are the port-critical piece with near-zero maintenance, and records before
   a compiler exist would be a hand-maintained corpus without a consumer.
2. **Tier table — RULED: all five `required` rows stand** (always-on-entry,
   human-approval-channel, skill-registry, commit-gate, session-spine). Commit-gate
   stays a hosting precondition — mechanical governance enforcement is
   non-negotiable, bypassability aside. `memory-store` remains provisionally
   `optional` pending E1.
3. **Home — RULED: `governance/`.** The contract is kernel-shaped and part of the
   export unit E4/E5 consume.
4. **Naming — RULED: `system-contract.yaml`.** Name-agnostic across the open
   engine-rename question; matches the KB pattern vocabulary.
5. **Deferred to E3's build (re-asked then):** Layer-2 source of truth
   (record-as-canonical vs frontmatter extension vs sidecar); pointer-only vs
   self-contained records; the agent extension field set; workspace-root vs
   engine-scoped ownership; v1 instance scope.
