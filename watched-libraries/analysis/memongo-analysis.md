---
title: "Memongo -- Structural Analysis"
id: "memongo-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-22"
updated: "2026-04-22"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "memongo"
  - "mongodb"
  - "memory"
  - "benchmark-discipline"
analyzed_version: "latest (2026-04-22)"
analyzed_date: "2026-04-22"
repo_url: "https://github.com/romiluz13/Memongo"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "governance-model"
  - "research-dimension-mapping"
scope_note: "Targeted Pass-2 supplement on three companion docs (PRODUCTION-READY.md, benchmark-operating-contract.md, self-host.md) plus MAINTAINER-MAP.md and CLAUDE.md surfaced during clone. Workflow-topology and cross-agent-protocol dimensions recorded as N/A — Memongo is a memory library, not an agent framework."
---

# Memongo -- Structural Analysis

## Metadata
- **Repo:** https://github.com/romiluz13/Memongo
- **Version analyzed:** latest (clone 2026-04-22)
- **Date:** 2026-04-22
- **Spectrum position:** evaluating (per watched-library entry)
- **Scope this run:** three maintainer-tier companion docs (Pass 2), not a full structural pass. README-level architecture was analyzed in session 45 and is recorded via 6 related findings + 3 evidence-boosted findings; not re-scanned here.

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 363 |
| Total directories | 54 |
| Markdown files | 60 |
| TypeScript files | 237 |
| JSON / YAML / MDX / shell config | ~46 |
| MD-to-code ratio | ~0.25 (60 md : 237 ts) |
| Max directory depth | not measured this pass |

### Top-Level Structure

```
memongo/
  apps/            api (Hono), mcp (stdio), web (Next.js), docs
  packages/        memory-engine, memory-bridge, memongo-memory, client, tools, lib
  docs/            benchmarks, concepts, design, experiments, migration, plans, platform, reference, research, start, cli, assets
  docker/mongodb/  atlas-local + mongot compose stacks
  scripts/
  AGENTS.md        Bun-monorepo conventions
  CLAUDE.md        Memongo repository guidelines
  README.md
```

Monorepo substrate: Turborepo + Bun, TypeScript-only packages, Biome for lint/format, Vitest for tests. Runtime target: Node 20+ / Bun 1.2+.

### Markdown Composition (inferred from directory role)

| Purpose | Directory | Notes |
|---------|-----------|-------|
| Agent / repo context | `AGENTS.md`, `CLAUDE.md` (root) | Both exist at root; CLAUDE.md is the richer file (capability matrix + package-naming contract) |
| Human product docs | `apps/docs/` | Mix of `.mdx`; public product surface |
| Maintainer & release docs | `docs/platform/` | PRODUCTION-READY.md, MAINTAINER-MAP.md, PLATFORM-README.md, PACKAGE-STATUS.md, self-host.md |
| Benchmark docs | `docs/benchmarks/` | benchmark-operating-contract.md + others |
| Historical / compatibility | `docs/migration/` | Per MAINTAINER-MAP §docs-ownership |
| Internal analysis | `docs/research/`, `docs/experiments/`, `docs/plans/` | Explicitly labeled "internal analysis and planning only" in MAINTAINER-MAP |
| Reference / start / cli / concepts / design | `docs/{reference,start,cli,concepts,design}/` | Public-doc surface, not sampled this pass |

### Directory Naming Conventions
- kebab-case across packages, apps, docs. Scoped npm packages prefixed `@memongo/...`.

### Notable Structural Patterns
- **Explicit docs-ownership zones.** MAINTAINER-MAP.md declares separate zones for public docs (`apps/docs`), maintainer/release docs (`docs/platform`), historical (`docs/migration`), and internal planning (`docs/research`, `docs/experiments`, `docs/plans`). Distinct from the common "everything in `/docs`" pattern — each zone carries an audience and permission contract.
- **"Source of truth" table.** MAINTAINER-MAP.md names exactly one file per role (product shape = README.md, public docs = apps/docs, release truth = PRODUCTION-READY.md, package support = PACKAGE-STATUS.md). Avoids multi-file ambiguity common to large repos.
- **Companion-repo guardrail.** CLAUDE.md: *"This repository contains only the standalone memory product; do not import from vendored fork trees or local `archive/` copies."* Explicit fork-boundary enforcement in agent-addressed context.

---

## 2. Context File Map

Sampling note: full file-by-file audit not run this pass. Mapped only root-level context files and companion docs Nick flagged. A full context-map would require sampling across `apps/docs/`, `docs/concepts/`, `docs/design/`, `docs/reference/`.

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `CLAUDE.md` | LLM | Global | Auto-loaded | Identity/Constraints + Capability Map | Bun/Turborepo conventions, package naming contract, 6-capability × 6-layer matrix (Engine / Bridge / API / MCP / Client / AI SDK), fork-boundary warning |
| `AGENTS.md` | LLM | Global | Auto-loaded | Constraints/Rules | Coding style, test/build conventions, commit guidelines (not read in full this pass) |
| `docs/platform/MAINTAINER-MAP.md` | Human (primary) / LLM (secondary) | Global | Referenced (manual read) | Workflow/Process + Content Map | Ordered 5-file onboarding ladder, release-lane cheatsheet, docs-ownership zones, "source of truth" table |
| `docs/platform/PRODUCTION-READY.md` | Human | Task | Referenced | Workflow/Process | 6 release lanes, lane-specific env requirements, operational-honesty disclaimer |
| `docs/benchmarks/benchmark-operating-contract.md` | Human (primary) / LLM (secondary, operator-gated) | Task | Referenced | Constraints/Rules + Workflow | 5-lane benchmark taxonomy, publishable-claim invariants, report envelope, query-governance policy |
| `docs/platform/self-host.md` | Human | Task | Referenced | Workflow/Process | Stack components, config vars, canonical MongoDB stack, health-check endpoints, MCP spawn contract |

### Context Loading Strategy

Memongo runs a two-tier context pattern at the repo root: **CLAUDE.md is self-contained identity + capability map** (no `@`-chaining detected in the read pass); **AGENTS.md carries coding/workflow conventions** as a parallel peer file. MAINTAINER-MAP.md is human-addressed but functions as a **maintainer "chain-loader for humans"** — pointing to the 5 files that together establish release truth. Per `/repo-analyzer` classification, this is closer to `Auto-loaded`-parallel than a chain-loader pattern, but the maintainer-map functions as a narrative load order for onboarding (not enforced by the harness).

---

## 3. Workflow Topology

**N/A for this scope.** Memongo is a memory data-plane library, not an agent framework. It exposes HTTP + MCP interfaces; it does not orchestrate phases. Workflow-topology recorded as "no discernible workflow" per `/repo-analyzer` rule 9.

The closest workflow-like artifact is the **release lane sequence** in PRODUCTION-READY.md (see §4 Governance), which is a release-gate pipeline rather than an agent workflow.

---

## 4. Governance Model

Memongo's governance is concentrated in two documents that together express a release-and-benchmark discipline:

### Release Governance (PRODUCTION-READY.md + MAINTAINER-MAP.md)

**6 release lanes with distinct environment requirements:**

| Lane | Command(s) | Env requirement | Claim scope |
|------|-----------|-----------------|-------------|
| `repo-foundation` | `bun install / check-types / lint / build / test` | None beyond repo | Type + static + unit baseline |
| `api-contract` | `bun run proof-pack` | MongoDB reachable, `apps/api` running | HTTP contract shape |
| `package-publishability` | `bun run check-publishability` | None | Built dist + tarball + workspace-closure + install-smoke |
| `live-core` | vitest `production-readiness.e2e.test.ts` | `docker-compose.preview.yml` stack, Atlas Model key (`al-...`) | Vector-only + real MongoDB |
| `live-capability` | vitest `real-e2e-v2.e2e.test.ts`, `mongodb-e2e.e2e.test.ts` | Replica-set stack (`docker-compose.mongodb.yml` replicaset/fullstack) | Transactions, change streams, replica-set behavior |
| `real-agent` | `bun run agent-smoke` | GROVE key + preview stack + api running | "Closest supported proof that a real model can use Memongo as memory" |

Salient disciplines:
- **Explicit lane-environment binding.** "A direct Voyage `pa-...` key is not a valid preview auto-embed environment." Capability lanes require the environment they claim — not mocked.
- **Bounded-claim language.** The `real-agent` lane is described as "the closest supported proof that a real model can use Memongo as memory" — not a guarantee.
- **Operational honesty.** Explicit: "Passing these gates does not certify hosting SLAs, backups, monitoring, or org security review." Release-ready ≠ production-ready.

### Benchmark Governance (benchmark-operating-contract.md)

**Core rule:** *"Numbers are product claims only when the run proves the product path being claimed."* Internal diagnostics are valuable but must not be presented as official wins.

**5 benchmark lanes:**

| Lane | Purpose | Trigger | Publishable |
|------|---------|---------|-------------|
| Official retrieval | LongMemEval / LoCoMo retrieval quality | Release candidate, retrieval-algorithm changes, corpus changes | Yes (all dataset/build/topology/embeddings/command recorded) |
| Internal retrieval | Fast regression over legacy or custom query sets | Every retrieval / search / scoring change | No, unless explicitly labeled "internal diagnostic" |
| Conversation recall regression | Protect user-visible recall | Conversation recall / event schema / session-time-filter / citation / recall-plane changes | No — regression gate only |
| Query governance | Surface candidate MongoDB query-shape settings | Benchmark / operator-trace review | Advisory only |
| Proof pack | Confirm build, tests, live smoke readiness | Release candidate | Yes, as release evidence |

**Publishable-claim invariants (all must be true):**
1. `benchmarkReport.releaseGates` contains passing `official-retrieval` gate.
2. `officialMetrics` present, matches claimed dataset.
3. `corpus.cases > 0` and `corpus.scoredCases === corpus.cases` (partial coverage is warning, not a publishable win).
4. Commit/build id, dataset name/version, MongoDB topology, embedding model, and command all recorded.
5. Warnings and degradations reviewed and disclosed when material.
6. Conversation-recall regression test run for any recall-plane change.

**Report envelope (`benchmarkReport`):** `generatedAt`, `build`, `corpus`, `metrics.internal`, optional `metrics.official`, `releaseGates`, `warnings`, `degradations`. Build identity is set via env vars (`MEMONGO_BUILD_COMMIT`, `MEMONGO_BUILD_ID`, `MEMONGO_BUILD_LABEL`) with CI fallback to `GITHUB_SHA`, `GITHUB_RUN_ID`, `VERCEL_GIT_COMMIT_SHA`, `VERCEL_DEPLOYMENT_ID`.

**Query governance is advisory-only.** MongoDB query settings are cluster-scoped and persistent; the contract explicitly refuses to apply them automatically. Operator responsibilities: inspect query stats + explain output, apply manually, record setting + rollback command, remove with `removeQuerySettings` if degrading. This is a concrete instance of **advisory / gated-autonomy pattern** in an agent-adjacent system.

**Comparison discipline:** "Do not compare numbers from different corpora, embedding models, or MongoDB topologies without labeling the comparison as non-equivalent." Explicit anti-pattern guardrail against apples-to-oranges benchmark quotes.

### Permission Model
- No explicit allow/deny list for agent actions (Memongo is not an agent framework; it is memory infrastructure).
- CLAUDE.md sets **implicit repo-boundary enforcement**: "do not import from vendored fork trees or local `archive/` copies." Agent-read guardrail against cross-repo contamination.

### Constraint Expression

| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Release-lane checklist | `docs/platform/PRODUCTION-READY.md` | Soft (maintainer discipline; CI wiring not read this pass) | "Memongo is only release-ready when every release-blocking lane below is green" |
| Benchmark operating contract | `docs/benchmarks/benchmark-operating-contract.md` | Soft (contract doc; `releaseGates` gate is machine-checked in the envelope) | "If `datasetKind` is `legacy-query` or `officialMetrics` is absent, the result is an internal diagnostic, not a benchmark win" |
| Agent context guardrail | `CLAUDE.md` | Soft (agent-addressed prose) | "Never commit secrets"; "do not import from vendored fork trees" |

### Guardrail Patterns
- **Envelope-gated claims.** Publishable vs internal is a machine-checkable envelope state, not a human judgment call.
- **Operator-gated mutation.** Cluster-scoped settings require manual human action; the system only recommends.
- **Anti-equivalence labeling.** Comparing across corpora/models/topologies must be explicitly labeled non-equivalent.

---

## 5. Cross-Agent Protocol

**N/A for this scope.** Memongo is not multi-agent. Its "Dreamer" consolidation agent (`mongodb-consolidator.ts` → `POST /v1/consolidate`) is a single-agent process triggered via HTTP/MCP tool, not coordinated across peer agents. No agent roster; no handoff protocol. Recorded as "None" for coordination pattern.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | Medium | CLAUDE.md capability × layer matrix; maintainer-map onboarding ladder; source-of-truth table — all context-shaping patterns. Not a primary focus of the three docs. |
| Model | None | No model-selection or model-behavior patterns in-scope docs. |
| Prompt | None | No prompt scaffolds in-scope. |
| Tools | Medium | Per CLAUDE.md: 6 capabilities × 6 consumer layers (Engine / Bridge / API / MCP / Client / AI SDK) — tool-surface roll-up is a concrete context-compression pattern for tool inventories. |
| Intent | Low | Release lanes express intent ("prove the product path being claimed") but the framing is governance, not intent-engineering proper. |
| Orchestration | None | Memongo is memory infrastructure; no orchestration primitives in-scope. |
| Evaluation | **High** | benchmark-operating-contract.md is a full evaluation-discipline document: 5-lane taxonomy, publishable-claim invariants, report envelope, anti-equivalence comparison rule. Strong candidate for KB promotion. |
| Sandboxing | Low | self-host.md mentions TLS + API key + bind-address, but not sandboxing patterns proper. |
| Governance | **High** | PRODUCTION-READY.md (release-lane discipline) and benchmark-operating-contract.md (publish-discipline) together exemplify governance-as-checklist-invariants with operational-honesty disclaimers. |
| Agent Design | Low | CLAUDE.md fork-boundary guardrail is an agent-context pattern, but small surface. |

### Findings Candidates

Reviewed by Nick 2026-04-23. Plain-English restatements added post-review per new `feedback_findings_plain_english.md` discipline.

1. **Benchmark Operating Contract** (Evaluation, **likely P1**)
   - Multi-lane benchmark taxonomy with publishable-claim invariants, report envelope, and machine-checkable release gates.
   - Directly transferable: any system that publishes benchmark results can adopt the lane/claim-invariant pattern.
   - Complements Memongo's existing LongMemEval-S findings by capturing the **discipline** that produces them (vs the **numbers** themselves).
   - Would cross-link to the `surprisal-novelty-as-memory-write-gate.md` and `rank-fusion-hybrid-retrieval-mongodb-atlas.md` findings as an auditability overlay.
Nick: No idea what youre talking about. Please restate in plain English.
→ Promoted to [[benchmark-operating-contract]] on 2026-04-23 (plain-English restatement provided mid-session; Nick accepted).

2. **Environment-scoped release lanes with bounded-claim language** (Governance / Evaluation, **likely P2**)
   - 6 lanes each bound to the environment they claim. "Closest supported proof" language bounds the claim.
   - "Release-ready ≠ production-ready" operational-honesty disclaimer is a reusable governance pattern.
   - Transferable to any CI/release system for an agent framework.
Nick: Accepted.
→ Promoted to [[environment-scoped-release-lanes]] on 2026-04-23.

3. **Maintainer-map onboarding ladder + docs-ownership zones** (Context Engineering, **likely P2**)
   - Ordered 5-file reading path + distinct ownership zones (public / maintainer / historical / internal) + "source of truth" table.
   - Reduces new-contributor context-load and prevents cross-zone doc drift.
   - Overlaps with existing KB thinking on context-loading and codebase legibility; may extend an existing finding rather than stand alone.
Nick: Skip.
→ Skipped: Nick's directive on 2026-04-23.

4. **Capability × Layer roll-up in CLAUDE.md** (Context Engineering / Tools, **likely P2/P3**)
   - 6 memory-intelligence features × 6 consumer layers in a single table inside CLAUDE.md. Compresses a large tool inventory into a navigable grid.
   - Transferable pattern: any agent-addressed context file documenting a large tool/capability surface.
Nick: Accepted.
→ Promoted to [[feature-by-layer-capability-matrix]] on 2026-04-23.

5. **Query-governance advisory-only pattern** (Governance, **likely P2**)
   - Benchmark surfaces candidate DB settings; refuses to apply them. Cluster-scoped persistence → mandatory operator-gated human review.
   - Concrete instance of Human-Required autonomy tier mapped onto a backend-mutation boundary. Useful example for the Agent-Governance dimension.
Nick: I need this in plain English, I dont understand what youre talking about. Please keep in mind that I am looking to not have to thoroughly read/watch everything single thing I send to you.
→ Promoted to [[advisory-only-for-persistent-mutations]] on 2026-04-23 (plain-English restatement provided mid-session; Nick accepted). Finding generalized beyond cluster-scoped DB settings to the broader pattern of "advisory-only for broad-blast or persistent mutations," with Memongo's query-governance as the concrete instance.

6. **Named `proof-pack` artifact as a release-evidence label** (Evaluation / Governance, **likely P3**)
   - `bun run proof-pack` is both a release-lane step and a benchmark lane label.
   - Naming a bundled-evidence command creates a stable contract between maintainers and CI.
   - Low-novelty on its own; a supporting datapoint for the benchmark-contract finding.
Nick: Agreed.
→ Skipped: low-novelty standalone on 2026-04-23. Supporting content absorbed into [[benchmark-operating-contract]] (release-gate invariant #1 and the proof-pack lane description).
---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-22 | latest | structural-inventory (partial), context-file-map (partial), governance-model, research-dimension-mapping | Targeted Pass 2 on three companion docs (PRODUCTION-READY, benchmark-operating-contract, self-host) flagged at session 45. README-level patterns already in KB (6 related findings). Workflow-topology and cross-agent-protocol recorded as N/A. |
