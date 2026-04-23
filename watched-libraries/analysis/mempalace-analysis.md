---
title: "MemPalace -- Structural Analysis"
id: "mempalace-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-23"
updated: "2026-04-23"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "mempalace"
  - "chromadb"
  - "memory"
  - "benchmark-discipline"
  - "governance"
analyzed_version: "3.3.2 (2026-04-23)"
analyzed_date: "2026-04-23"
repo_url: "https://github.com/MemPalace/mempalace"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "governance-model"
  - "research-dimension-mapping"
scope_note: "Full pass on dimensions 1, 2, 4, 6. Dimensions 3 (workflow-topology) and 5 (cross-agent-protocol) recorded as N/A with rationale — MemPalace is memory infrastructure, not an agent framework. Python source modules (116 .py files) scanned only for module roles, not line-level review. One RFC (002) read in full; RFC 001 referenced but not opened."
---

# MemPalace -- Structural Analysis

## Metadata
- **Repo:** https://github.com/MemPalace/mempalace
- **Version analyzed:** 3.3.2 (clone 2026-04-23)
- **Date:** 2026-04-23
- **Spectrum position:** evaluating (per watched-library entry)
- **Scope this run:** Full 5-dimension pass. Dimensions 3 and 5 N/A with rationale.

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 260 |
| Total directories | 46 |
| Markdown files | 66 |
| Python files | 116 |
| JSON files | 28 |
| Vue files | 9 (website landing) |
| Shell scripts | 6 |
| YAML files | 4 |
| JSONL files | 4 (benchmark results) |
| MD-to-code ratio | ~0.57 (66 md : 116 py) |
| Max directory depth | 4 |

### Top-Level Structure

```
mempalace/
  mempalace/          core Python package (26+ modules)
    backends/         pluggable storage (base.py + chroma.py)
    instructions/     5 command instructions (help/init/mine/search/status)
    i18n/             localization
    sources/          (referenced in RFC 002, not yet present)
  .claude-plugin/     Claude Code plugin surface
    commands/         5 command markdown files
    hooks/            Stop + PreCompact hook scripts + hooks.json
    skills/mempalace/ agent-facing SKILL.md
  .codex-plugin/      Codex CLI plugin surface (parallel to .claude-plugin)
    hooks/, skills/*, plugin.json
  .agents/            cross-harness marketplace manifest
  hooks/              authoritative hook scripts (mempal_save_hook.sh + mempal_precompact_hook.sh)
  benchmarks/         reproducible runners + results JSONLs
  docs/               HISTORY.md, CLOSETS.md, schema.sql, rfcs/002-*.md
  integrations/       openclaw/SKILL.md (cross-harness integration SKILL)
  examples/           HOOKS_TUTORIAL.md, gemini_cli_setup.md, mcp_setup.md
  tests/              including tests/benchmarks/
  website/            VitePress docs site (landing/ + concepts/guide/reference)
  CLAUDE.md           primary agent context
  AGENTS.md -> CLAUDE.md   symlink (universal-harness pattern)
  MISSION.md          narrative founder-voice governance
  ROADMAP.md, CHANGELOG.md, SECURITY.md, CONTRIBUTING.md
  README.md           with impostor-domain CAUTION block at top
  pyproject.toml      Ruff + Vitest config; ChromaDB + PyYAML only
```

### Directory Naming Conventions

- snake_case for Python modules (`palace.py`, `knowledge_graph.py`, `convo_miner.py`).
- kebab-case for markdown and plugin artifacts (`mempal-stop-hook.sh`, `marketplace.json`).
- Dot-prefixed directories (`.claude-plugin`, `.codex-plugin`, `.agents`, `.github`, `.devcontainer`) for harness-specific configuration.

### Markdown Composition (classified by functional role)

| Purpose | Count | Directory |
|---------|-------|-----------|
| Agent/harness context | 4 | root (CLAUDE.md, AGENTS.md→CLAUDE.md, MISSION.md) + `.claude-plugin/README.md` + `.codex-plugin/README.md` |
| Commands/skills | 11 | `.claude-plugin/commands/*.md` (5) + `.codex-plugin/skills/*/SKILL.md` (5) + `integrations/openclaw/SKILL.md` |
| Shared instructions | 5 | `mempalace/instructions/*.md` (authored once, referenced by both plugin surfaces) |
| Governance / product truth | 7 | ROADMAP, CHANGELOG, SECURITY, CONTRIBUTING, MISSION, docs/HISTORY, docs/CLOSETS |
| RFCs | 1 (+1 referenced) | `docs/rfcs/002-source-adapter-plugin-spec.md` (RFC 001 referenced, not present yet) |
| Benchmarks | 3 | `benchmarks/BENCHMARKS.md`, `benchmarks/HYBRID_MODE.md`, `benchmarks/README.md` |
| Human docs | rest | `website/*`, `examples/*`, `hooks/README.md`, `.github/*`, `mempalace/README.md` |

### Notable Structural Patterns

- **AGENTS.md is a symlink to CLAUDE.md.** One file, two harnesses: Codex CLI and Claude Code both read the same identity + design principles + project structure without duplication. Zero maintenance overhead.
- **Three parallel plugin surfaces** (`.claude-plugin/`, `.codex-plugin/`, `.agents/`) wrap a **single authored-once content layer** (`mempalace/instructions/*.md`). Each plugin's commands/skills are thin shells that call `mempalace instructions <name>` at runtime; plugin configs declare hook wiring, MCP registration, and marketplace metadata.
- **Source-of-truth for hook scripts is `/hooks/`** (mempal_save_hook.sh, mempal_precompact_hook.sh); the plugin directories reference these via `${CLAUDE_PLUGIN_ROOT}/hooks/`. No duplication.
- **`docs/HISTORY.md` is distinct from `CHANGELOG.md`.** CHANGELOG records version-by-version changes. HISTORY records *corrections, retractions, and public notices* — a separate governance artifact.
- **Cross-harness SKILL** at `integrations/openclaw/SKILL.md` is authored for consumption by OpenClaw's runtime skill loader, not by MemPalace itself. Pattern: a watched-library ships a SKILL for a peer harness.
- **RFC-driven design surface** at `docs/rfcs/` with `spec_version: 1.0`, a full conformance-test contract, and cross-linking to 16+ issues/PRs that motivated the spec.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `CLAUDE.md` | LLM | Global | Auto-loaded | Identity/Persona + Constraints/Rules + Workflow/Process | Mission ("memory is identity"), 7 non-negotiable design principles, project structure, commands, conventions, architecture diagram. Self-contained (no `@`-chains). |
| `AGENTS.md` → `CLAUDE.md` | LLM | Global | Auto-loaded (via symlink) | Same as CLAUDE.md | Universal-harness: Codex CLI reads AGENTS.md; Claude reads CLAUDE.md; symlink resolves both to the same bytes. |
| `MISSION.md` | Both (primary Human; LLM-readable) | Global | Referenced (by CONTRIBUTING, website) | Identity/Persona + Narrative | First-person founder voice. Tells the design story of v4 (background hooks) and the $1.13→$0 observation. Declares user-facing invariants ("always remember, these are brand new tools…"). |
| `ROADMAP.md` | Human | Global | Referenced | Workflow/Process + Release Truth | v3.1.1 patch list, v4.0 alpha capabilities (swappable storage, local NLP, improved retrieval), branch model (`main`/`develop`/`release/3.x`). |
| `CONTRIBUTING.md` | Human | Global | Referenced | Constraints/Rules (negative-space) | Explicitly enumerates rejected PR classes ("We do not accept: summarization, cloud sync, telemetry, API-required core, bypass-verbatim shortcuts"). |
| `SECURITY.md` | Human | Global | Referenced | Workflow/Process | Private vulnerability reporting via GitHub Security tab. 48-hour acknowledgment target. |
| `docs/HISTORY.md` | Human (primary) / LLM (referenced from README) | Global | Referenced | Retraction/Correction Log | Dated, append-only record: 2026-04-14 benchmark-table rewrite, 2026-04-11 impostor-domain notice, 2026-04-07 founder retraction note. |
| `docs/rfcs/002-source-adapter-plugin-spec.md` | Human (architects) + LLM (future codegen) | Task | Referenced | Constraints/Rules + Workflow/Process (spec) | Formal adapter contract with spec_version, conformance-test suite, declared-transformations invariants, privacy classes. |
| `benchmarks/BENCHMARKS.md` | Human (primary) / LLM (secondary) | Task | Referenced | Evaluation / Methodology | Full score progression 96.6%→100%, benchmark-integrity section disclosing teaching-to-the-test, dev/held-out split CLI flags, reproduction commands. |
| `.claude-plugin/skills/mempalace/SKILL.md` | LLM | Task | Injected (when skill activates) | Tool Usage + Workflow/Process | SKILL wrapper that tells the model to run `mempalace instructions <command>` and follow the returned text. |
| `.claude-plugin/commands/*.md` (5) | LLM | Task | Injected | Tool Usage | Same wrapper pattern per command (init/help/mine/search/status). |
| `.codex-plugin/skills/*/SKILL.md` (5) | LLM | Task | Injected | Tool Usage | Codex CLI parallel to `.claude-plugin/commands/`. |
| `mempalace/instructions/*.md` (5) | LLM | Task | Runtime-fetched (via CLI) | Workflow/Process | Authored-once source. Ordered procedural steps with error-handling branches. Referenced by both plugin surfaces. |
| `integrations/openclaw/SKILL.md` | LLM (OpenClaw host) | Task | Referenced/Injected by OpenClaw | Identity/Persona + Tool Usage + Workflow/Process | Self-contained SKILL for the OpenClaw harness. Ships in MemPalace repo but targets a peer tool's runtime. |
| `hooks/README.md` | Human | Tool | Referenced | Workflow/Process + Tool Usage | Two-layer capture explanation (auto-mine + block-reason coercion), `stop_hook_active` infinite-loop guard, multi-harness hook install instructions. |

### Sampling Notes

Read in full: CLAUDE.md, MISSION.md, ROADMAP, SECURITY, CONTRIBUTING, docs/HISTORY.md, benchmarks/BENCHMARKS.md, README.md, docs/rfcs/002-source-adapter-plugin-spec.md, `.claude-plugin/skills/mempalace/SKILL.md`, `.claude-plugin/plugin.json`, `.claude-plugin/hooks/hooks.json`, `mempalace/instructions/init.md`, `integrations/openclaw/SKILL.md`, `hooks/README.md`.

Inferred from naming: remaining 4 command/skill files in `.claude-plugin/commands/` and `.codex-plugin/skills/` — same wrapper pattern as the init exemplar.

Not opened: Python source modules (116 files), `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, website files, CHANGELOG full text, the four benchmark JSONL result files.

### Context Loading Strategy

Two-tier at repo root: **CLAUDE.md carries identity + non-negotiable design principles + architecture** (self-contained, no `@`-chains); **AGENTS.md is a symlink alias** so Codex CLI users get identical content without a second file to maintain.

Plugin surfaces (`.claude-plugin/`, `.codex-plugin/`) are **harness-specific wrappers around a harness-agnostic instruction source** (`mempalace/instructions/*.md`). At runtime, each plugin command/skill tells the model: "Run `mempalace instructions <name>`, then follow what it tells you." This pattern decouples plugin-format churn from instruction content.

Hook context is **tool-provided at lifecycle events** — Stop and PreCompact are harness-level events; MemPalace receives them via `${CLAUDE_PLUGIN_ROOT}/hooks/`-rooted shell scripts and returns JSON decisions (`{"decision": "block", "reason": "..."}`) to coerce save behavior before termination.

---

## 3. Workflow Topology

**N/A for this repo.** MemPalace is a memory infrastructure library, not an agent framework. It exposes CLI commands, an MCP server with 29 tools, and a Python API; it does not orchestrate phases or agent transitions. Recorded as "no discernible workflow" per `/repo-analyzer` rule 9.

The closest workflow-shaped artifacts are:

1. **Release branch model** (ROADMAP.md): `main` (tagged releases) ← `develop` (active) ← `release/3.1`, `release/3.0` (hotfix lanes). This is a git-branching discipline, not an agent workflow.
2. **Two-hook lifecycle** (hooks/README.md): the Stop and PreCompact hooks define a *session-termination save sequence* — count human messages → auto-mine → block → let AI save → `stop_hook_active` flag flips → stop completes. This is a harness-lifecycle pattern (§5 captures it under Cross-Agent Protocol for cross-reference).

No multi-phase pipeline, no human-gate structure, no parallel-stage execution.

---

## 4. Governance Model

MemPalace's governance is distributed across multiple artifacts, each carrying a specific contract. This dimension is unusually dense.

### 4.1 Design-Principle Invariants (CLAUDE.md)

CLAUDE.md declares **seven non-negotiable design principles** explicitly bound to every PR/feature/refactor:

1. **Verbatim always** — never summarize, paraphrase, or lossy-compress user data.
2. **Incremental only** — append-only after initial build; crash mid-operation must leave existing palace untouched.
3. **Entity-first** — real names with disambiguation by DOB/ID/context; people matter more than topics.
4. **Local-first, zero API** — core features work without API keys; no cloud dependency for memory operations.
5. **Performance budgets** — hooks <500ms, startup injection <100ms.
6. **Privacy by architecture** — the system *physically cannot* send data because it never leaves the machine.
7. **Background everything** — filing, indexing, timestamps in hooks; zero tokens for bookkeeping in chat.

Framing as non-negotiable invariants (rather than aspirations) is explicit: "These are non-negotiable. Every PR, every feature, every refactor must honor them."

### 4.2 Negative-Space Contribution Boundaries (CONTRIBUTING.md)

Where CLAUDE.md tells the model what the system *is*, CONTRIBUTING.md tells humans what the system *will not accept*:

> We do not accept:
> - summarization of user content
> - cloud storage/sync features
> - telemetry or analytics
> - features requiring API keys for core memory
> - shortcuts that bypass verbatim storage

This is negative-space governance — the rejection list carries as much load as the acceptance list. "Palace structure is scoping, not magic" is a similar framing: explicit refusal to claim a novel retrieval mechanism where none exists.

### 4.3 Retraction-and-Correction Log (docs/HISTORY.md)

A first-class governance artifact distinct from CHANGELOG:

- **Purpose:** "canonical record of post-launch corrections, public notices, and retractions that affect MemPalace's public claims."
- **Shape:** dated entries, newest first, with audit trail of every file/surface where a retracted claim was removed.
- **Example (2026-04-14):** Community audit identified that MemPalace's R@5 was being compared directly against competitors' QA accuracy — different metrics, not comparable. The PR description enumerates: headline number rewrite, "100%" withdrawal rationale, held-out 98.4% framing, "+34% palace boost" removal locations, competitor-comparison-table deletion, reproduction-command branch correction, LoCoMo top-k=50 retraction.
- **Example (2026-04-11):** Impostor-domain (`mempalace.tech`) notice with community-reported issues #267, #326, #506 cross-linked.
- **Example (2026-04-07):** Founder note from Milla & Ben addressing community criticism of the 48h-post-launch README. Itemizes every claim, explicitly separates "what we got wrong" from "what's still true and reproducible," and commits to four corrective actions.

Self-incriminating disclosure is explicit: "In a peer-reviewed paper this would be a significant methodological problem. We're disclosing it here rather than letting it sit unexamined."

### 4.4 Benchmark Integrity (benchmarks/BENCHMARKS.md)

Formalizes evaluation discipline with three mechanisms:

1. **"Two honest numbers"** framing — the 96.6% R@5 (raw, no LLM) and 98.4% R@5 (hybrid held-out 450) are published as a pair. Neither is "the whole picture alone."
2. **Tool-enforced dev/held-out split** — `benchmarks/lme_split_50_450.json` (seed=42) is committed. CLI flags `--dev-only`, `--held-out`, `--create-split`, `--split-file` enforce the discipline. "50 dev questions — safe to use for iterative tuning. 450 held-out — final publishable score. Touch once. Any iteration after viewing held-out results contaminates them."
3. **Teaching-to-the-test self-disclosure** — the 99.4% → 100% step was developed by inspecting three specific wrong answers (question hashes `d6233ab6`, `4dfccbf8`, `ceb54acb`). Fixes itemized; classification as "teaching to the test" explicit; withdrawal from headline surfaces confirmed in HISTORY.md.
4. **Non-equivalent-comparison labeling** — tables comparing R@5 with QA accuracy carry a bold "read before quoting this table" block and have been removed from public surfaces per HISTORY.md entry.
5. **Independent-convergence validation** — two independent retrieval architectures (hybrid scoring, palace navigation) converged at exactly the same ceiling (99.4%). Framed as: "The ceiling is architectural, not a local maximum of any one approach." Novel meta-methodology.
6. **Full auditability** — every benchmark run's per-question result JSONL is committed under `benchmarks/results_*.jsonl`. Every retrieved document, every score, every answer inspectable.

### 4.5 RFC-Driven Design

`docs/rfcs/002-source-adapter-plugin-spec.md` is a 700+-line formal spec that:

- Declares `spec_version: 1.0` as a loadable-compatibility boundary.
- Enumerates **reserved transformation names** (§1.4: `utf8_replace_invalid`, `newline_normalize`, `line_trim`, `spellcheck_user`, `synthesized_marker`, etc.) with semantics.
- Requires adapters to declare `declared_transformations: ClassVar[frozenset[str]]` — the invariant being that **no transformation may be applied that is not in this set**.
- Ships a **conformance-test suite** (`AbstractSourceAdapterContractSuite`): byte-preserving round-trip test for `byte_preserving` adapters; declared-transformation round-trip test for `declared_lossy`; schema-conformance property test.
- Explicitly frames the machine-verification layer as superseding the social contract: "This replaces the MISSION.md promise of 'verbatim always' with a stronger one: every adapter publishes what it does to your data, and the conformance suite verifies it hasn't lied."
- Defines a **privacy-class taxonomy** (public / internal / pii_potential / sensitive / secrets_possible) with per-palace `privacy_floor` enforcement at write time.

### 4.6 Security Governance

README leads with a CAUTION block naming an impostor domain (`mempalace.tech`) that distributes malware, before the branding block. Cross-links to `docs/HISTORY.md` for timeline. SECURITY.md uses GitHub's private vulnerability reporting flow (not public issues). Supported versions clearly enumerated.

### 4.7 Permission / Constraint Summary

| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Design-principle invariants | `CLAUDE.md` | Soft (agent-addressed prose + "non-negotiable" framing) | "Hooks under 500ms. Startup injection under 100ms." |
| Contribution rejections | `CONTRIBUTING.md` | Soft (maintainer review) | "We do not accept summarization of user content…" |
| Retraction discipline | `docs/HISTORY.md` | Soft (governance discipline) | Full retraction of 2026-04-14 benchmark-table claims |
| Benchmark split | `benchmarks/lme_split_50_450.json` + CLI flags | Hard (tool-enforced via `--dev-only`/`--held-out`) | "Touch once. Any iteration after viewing held-out contaminates" |
| Declared transformations | RFC 002 + `AbstractSourceAdapterContractSuite` | Hard (test-suite-enforced, once spec lands) | `TransformationViolationError` on undeclared transform |
| Privacy floor | RFC 002 §6.2 | Hard (write-time rejection, post-spec) | Drawers below floor rejected with `rejected` surface |
| Agent-context guardrails | `CLAUDE.md` + README | Soft (agent-addressed) | Impostor-domain warning; "palace structure is scoping, not magic" |

### 4.8 Guardrail Patterns

- **Envelope-verified claims** — benchmark numbers are only headline-quotable if the mode is reproducible without teaching-to-the-test, on a held-out split.
- **Retraction as first-class output** — public claims that turn out to be wrong get removed from every surface with full audit trail, not quietly edited.
- **Negative-space acceptance** — the rejection list is as specific as the acceptance list.
- **Impossibility over prohibition** — "privacy by architecture" frames a governance property as a structural impossibility, not a policy.
- **Social contract → machine-verified property** — RFC 002 converts "verbatim always" from a MISSION statement into a test-suite-enforced invariant.

---

## 5. Cross-Agent Protocol

**Partial N/A for this repo.** MemPalace is single-agent internal (no multi-agent orchestration). However, the repo models two patterns worth recording:

### 5.1 Shared-Memory as Cross-Agent Substrate

The SKILL.md protocol declares the palace as the coordination surface for multiple external agents:

- Each specialist agent gets its own *wing* and *diary* in the palace (`mempalace_diary_write`, `mempalace_diary_read`).
- Runtime agent discovery via `mempalace_list_agents` — agents don't need to enumerate peers in static system prompts.
- Every agent follows the same session protocol: "On wake-up call `mempalace_status`; before responding about any person/project/past event call `mempalace_search` or `mempalace_kg_query` FIRST; after each session call `mempalace_diary_write`; when facts change call `mempalace_kg_invalidate` then `mempalace_kg_add`."

This is not orchestration — there is no controller and no handoff protocol. It is **shared-state coordination**: agents share the palace, each writes to its own diary/wing, all read from the same search surface. Analogous to a team sharing a filesystem rather than a workflow engine.

### 5.2 Harness-Lifecycle Coordination via Hooks

The `Stop` + `PreCompact` hooks implement a **harness-coerced save sequence** that coordinates between the harness (Claude Code / Codex CLI), the model, and the palace:

1. Harness fires `Stop` on model's stop-attempt.
2. Hook counts human messages in JSONL transcript; if ≥15 since last save, proceeds.
3. Hook auto-mines the transcript into the palace (captures raw tool output regardless of what the model said).
4. Hook returns `{"decision": "block", "reason": "save tool output verbatim..."}` — coerces the model back into the save turn.
5. Model writes diary/drawers to the palace.
6. Model tries to stop again.
7. `stop_hook_active` flag is now true → hook returns `{}` → stop completes.

The `stop_hook_active` infinite-loop guard is explicit. `PreCompact` is a simpler variant (no counting — compaction always warrants a save).

This is a cross-agent coordination pattern *between the harness and the model*, mediated by a filesystem side-channel (the palace) and a JSON response contract.

### 5.3 Coordination Classification

- **Within MemPalace internals:** single-agent. No roster, no handoff protocol.
- **As a memory substrate for multi-agent systems:** shared-state with per-agent scoping (wings, diaries). No orchestration primitives.
- **As a harness-lifecycle citizen:** hook-mediated coercion pattern (`{"decision":"block"}` response).

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | AGENTS.md↔CLAUDE.md symlink for universal harness; multi-harness plugin architecture wrapping single-source instructions; background hooks as token-economy pattern; L0–L3 layered wake-up stack (`layers.py`, referenced in ROADMAP). |
| Model | None | No model-selection or model-behavior patterns in focus here. |
| Prompt | Low | SKILL.md encodes a strong session-protocol prompt ("FOLLOW THIS EVERY SESSION…"). |
| Tools | Medium | 29 MCP tools organized by surface (search, KG, palace-graph, writes); single-adapter architecture (RFC 002) replacing if-chain branching with registry + capabilities. |
| Intent | Low | CONTRIBUTING.md's rejection list and MISSION.md's first-person framing declare intent clearly, but not "intent engineering" in the KB sense. |
| Orchestration | None | MemPalace is memory infrastructure. |
| Evaluation | **Very High** | Retraction log; tool-enforced dev/held-out split; teaching-to-the-test self-disclosure and withdrawal; independent-convergence validation; metric-incomparability labeling; full per-question result JSONLs committed; reproduction-from-README; founder retraction note addressing community audit. |
| Sandboxing | Low | Privacy-class taxonomy in RFC 002 §6; no sandbox primitives proper. |
| Governance | **Very High** | Non-negotiable design principles; negative-space contribution boundaries; retraction-as-first-class-artifact; performance-budget invariants; privacy-by-architecture framing; RFC-driven design with spec_version; declared-transformation contract; impostor-domain callout at README top; founder-voice narrative governance (MISSION.md); benchmark-integrity self-critique. |
| Agent Design | Medium | Per-agent wing/diary pattern (shared memory substrate, no orchestration); runtime agent discovery; SKILL-as-session-protocol; harness-lifecycle hook coordination (Stop/PreCompact with block-reason coercion). |

### Findings Candidates

Ten candidates surfaced. Each lead with a plain-English "what it is" + "why it matters for us" per `feedback_findings_plain_english.md`; dimension + priority hint second. Reviewed by Nick 2026-04-23; nine promoted, one skipped (candidate #5: negative-space framing declined — the negative set is countably infinite and would impose unbounded maintenance burden; standing principle saved as `feedback_positive_space_governance.md`).

1. **Retraction log as first-class governance artifact** (Governance, likely P1/P2) — → Promoted to [[retraction-log-as-governance-artifact]] on 2026-04-23.
   - **What it is:** A dated, append-only document (`docs/HISTORY.md`) that records every public claim the team retracted, every audit response, every impostor-domain notice — separate from the version-by-version CHANGELOG.
   - **Why it matters for us:** When a claim in our docs, DDs, or findings turns out to be wrong, we need a place to publish the correction that isn't hidden in git history. This gives MetaSystem a pattern for correction-as-product rather than silent edits. Directly transferable to any system that publishes claims (our KB, the guides, the research findings themselves).
   - **Technical restatement:** `docs/HISTORY.md` is an append-only retraction/correction register with per-entry audit trail of every file/surface where a retracted claim was removed. Distinct load-point from CHANGELOG.md. 2026-04-14 entry shows the full-surface retraction pattern: claim identification → root cause → list of removed locations → links to the community-reported issue that triggered the audit.

2. **Tool-enforced dev/held-out split with self-disclosed teaching-to-the-test** (Evaluation, likely P1) — → Promoted to [[tool-enforced-dev-heldout-split]] on 2026-04-23; links to [[benchmark-operating-contract]] as `extends`.
   - **What it is:** A benchmark pipeline that physically prevents you from overfitting to test data by splitting the test set into "dev" (tune freely) and "held-out" (touch once), enforced via CLI flags. When the authors did overfit, they disclosed it publicly and removed the inflated number from their headlines.
   - **Why it matters for us:** Most benchmark discipline is social contract. This turns it into tool-enforced property. Any retrieval benchmark, eval loop, or prompt-tuning round the IL runs later should bake this in from the start. Extends Memongo's `benchmark-operating-contract.md` finding from a written invariant to a tool-enforced one.
   - **Technical restatement:** `benchmarks/lme_split_50_450.json` (seed=42) committed in-repo; CLI flags `--dev-only`, `--held-out`, `--create-split`, `--split-file`. `benchmarks/BENCHMARKS.md` §"Benchmark Integrity" itemizes which 3 questions the 99.4%→100% step was tuned on. `docs/HISTORY.md` 2026-04-14 entry records the headline withdrawal. Tooling + discipline + retraction combined.

3. **Universal-harness context via AGENTS.md↔CLAUDE.md symlink** (Context Engineering, likely P2) — → Promoted to [[universal-harness-context-via-symlink]] on 2026-04-23; `extends` [[cross-platform-context-file-strategy]] as a fourth strategy (zero-drift).
   - **What it is:** One file holds the agent-context content; a symlink named `AGENTS.md` points at it. Codex CLI reads `AGENTS.md`, Claude reads `CLAUDE.md`, both get identical bytes with zero maintenance overhead.
   - **Why it matters for us:** Our incubator systems will eventually land in repos consumed by multiple harnesses. This is the smallest possible pattern for multi-harness compatibility without forking content.
   - **Technical restatement:** `AGENTS.md -> CLAUDE.md` via `ln -s`. Two harness auto-load paths resolve to the same file. Commits one bytes-identical content authoritatively in CLAUDE.md; AGENTS.md exists only as a pointer.

4. **Shared-instructions authored-once + multi-harness plugin wrappers** (Context Engineering, likely P2) — → Promoted to [[shared-instructions-multi-harness-plugin-wrappers]] on 2026-04-23.
   - **What it is:** Instruction content (how to run `init`, `mine`, `search`, etc.) is authored once in one directory. Claude Code and Codex CLI each get their own plugin folder, but the plugin's commands are thin shells that just call the CLI to fetch the shared instructions at runtime.
   - **Why it matters for us:** Decouples plugin-format churn (Anthropic's command schema vs OpenAI's SKILL schema) from instruction content. Our own skills already fall into this trap — when we build a cross-system skill, we need a way to author-once and wrap-per-harness.
   - **Technical restatement:** `mempalace/instructions/*.md` is the single content source. `.claude-plugin/commands/*.md` and `.codex-plugin/skills/*/SKILL.md` each delegate to `mempalace instructions <name>` at runtime via shell invocation. Plugin configs (`plugin.json`, `hooks.json`, `marketplace.json`) carry harness-specific packaging metadata only.

5. **Negative-space contribution boundaries** (Governance, likely P2) — → Skipped: Nick's directive on 2026-04-23 — negative set is countably infinite, maintaining rejection lists imposes unbounded maintenance burden; prefer positive-invariant framing. Standing principle saved as `feedback_positive_space_governance.md`.
   - **What it is:** The CONTRIBUTING document explicitly lists what kinds of PRs will be rejected — flip of the usual "how to contribute" framing. "We do not accept summarization of user content, cloud storage/sync features, telemetry or analytics, features requiring API keys for core memory, or shortcuts that bypass verbatim storage."
   - **Why it matters for us:** Our governance docs lean on positive invariants ("Design Decisions are immutable") but don't always enumerate the anti-patterns a contributor might propose. Negative-space framing prevents well-meaning PRs from wasting review cycles on rejected categories. Directly transferable to our own CONTRIBUTING-equivalent.
   - **Technical restatement:** `CONTRIBUTING.md` contains an explicit "We do not accept: X, Y, Z" block. Listed rejections are derived from the 7 non-negotiable design principles in `CLAUDE.md` but phrased as concrete PR categories. "Palace structure is scoping, not magic" is a similar framing in the Architecture Decisions section — refusal to overclaim.

6. **Background-hooks-as-token-economy (move memory ops out of chat window)** (Context Engineering / Tools, likely P1) — → Promoted to [[background-hooks-as-token-economy]] on 2026-04-23; `extends` [[claude-code-hooks-for-automatic-session-memory]] with cost-quantification and block-reason coercion framing.
   - **What it is:** All memory bookkeeping (filing, indexing, timestamp injection) moves from the chat window into two background hooks (`Stop`, `PreCompact`). Reported change in operating cost: ~$1.13 per session → $0. The founder's observation that triggered this: the model was writing the same save-block repeatedly in-window.
   - **Why it matters for us:** Anywhere the IL or Household OS adds "automatic" work (governance logging, audits, cross-references), the default temptation is to have the model do it in-band. This finding argues: move it to a hook, zero tokens. Token economy is a standing Nick-rule (`feedback_token_economy.md`).
   - **Technical restatement:** `Stop` hook counts human messages since last save (threshold 15), auto-mines transcript JSONL into palace, returns `{"decision":"block","reason":"save tool output verbatim..."}` to coerce a save turn, then releases on `stop_hook_active=true`. `PreCompact` hook is the simpler variant (compaction always warrants a save). Contains an infinite-loop guard via the `stop_hook_active` flag.

7. **Verbatim-storage thesis as baseline for long-term memory** (Memory Architecture, likely P1) — → Promoted to [[verbatim-storage-thesis-for-memory]] on 2026-04-23; `contradicts` [[triple-storage-memory-architecture]] and `same-problem` with [[mongodb-single-store-polymorphic-evidence-memory]] (three architectural poles).
   - **What it is:** Store the actual conversation words, don't extract facts. On the standard LongMemEval retrieval benchmark, this scores 96.6% R@5 using default ChromaDB and zero LLM calls — matching or beating every LLM-based extractor. The field's over-engineering is the finding: "Raw verbatim text with good embeddings is a stronger baseline than anyone realized."
   - **Why it matters for us:** The KB currently holds Memongo's single-store polymorphic evidence memory as one pole; this is a related-but-distinct thesis on the same axis. For any future design of our own memory layer, we want both on record as architectural options (along with mem0's triple-store pole). Directly relevant to Nick's active Memongo work.
   - **Technical restatement:** `benchmarks/BENCHMARKS.md` §"The Core Finding": 96.6% R@5 on LongMemEval with no summarization, no extraction, no LLM. Independently reproducible from the repo. Direct counter-stance to mem0's LLM-extraction; adjacent to Memongo's single-store-polymorphic thesis (both argue against multi-store extraction but land in different designs).

8. **Independent-convergence as retrieval-ceiling evidence** (Evaluation, likely P2/P3) — → Promoted to [[independent-convergence-retrieval-ceiling]] on 2026-04-23.
   - **What it is:** Two completely different retrieval architectures — hybrid scoring (keyword + temporal + LLM rerank) and palace navigation (hall routing) — happened to reach the same score (99.4%). The authors treat this convergence as evidence that the ceiling is structural, not an accident of one method.
   - **Why it matters for us:** Transferable meta-methodology for any future eval round we run: when two independent approaches hit the same ceiling, that's more load-bearing than either alone. Useful for prompt-engineering rounds, tool selection, and architecture comparisons.
   - **Technical restatement:** `benchmarks/BENCHMARKS.md` documents Hybrid v3 + Haiku rerank = 99.4% and Palace + Haiku rerank = 99.4% as "Parallel Approach… Built independently from the hybrid track. Different architecture, same ceiling." Framing: "The ceiling is architectural, not a local maximum of any one approach." Novel enough to be its own eval pattern.

9. **Declared-transformations with conformance test suite (social contract → machine-verified property)** (Governance / Evaluation, likely P2) — → Promoted to [[declared-transformations-contract-conformance]] on 2026-04-23; `extends` [[specification-as-governance-fourth-enforcement-philosophy]] with the specific declared-transformations mechanism.
   - **What it is:** The original "we never change your data" promise was a social contract — trust us. RFC 002 replaces it with a mechanical one: every data-ingesting adapter declares the set of transformations it applies, and a test suite rejects the adapter if it applies anything outside that set.
   - **Why it matters for us:** Any claim we make about the IL ("agents only write to X," "extraction is lossless," "pipeline preserves Y") has the same weakness — unverified social contract. This is a concrete pattern for converting that kind of promise into a tested invariant. Directly transferable to agent-boundary claims in our system.
   - **Technical restatement:** RFC 002 §1.4 reserves transformation names, declares `declared_transformations: ClassVar[frozenset[str]]` as a class attribute adapters must populate, and defines conformance tests (§7.2 byte-preserving round-trip, §7.3 declared-transformation round-trip) that verify the adapter's output is reproducible from source by applying *only* its declared transformations. `TransformationViolationError` is the failure mode. "This replaces the MISSION.md promise of 'verbatim always' with a stronger one: every adapter publishes what it does to your data, and the conformance suite verifies it hasn't lied."

10. **Impostor-domain callout at README top** (Governance / Security, likely P3) — → Promoted to [[impostor-domain-readme-callout]] on 2026-04-23; `enables` [[retraction-log-as-governance-artifact]] (the CAUTION block's timeline link points at the retraction log).
    - **What it is:** The README leads with a security warning naming an impostor website that distributes malware, before the project branding and badges. Cross-links to the retraction log for a timeline.
    - **Why it matters for us:** Lower-priority than the others — MetaSystem is not a 49k-star public OSS target yet — but worth registering as a pattern for the eventual day the Household OS surface is public. Also a useful datapoint for the KB's security dimension.
    - **Technical restatement:** README.md begins with a `> [!CAUTION]` block naming `mempalace.tech` and declaring the three official surfaces (GitHub, PyPI, mempalaceofficial.com). Cross-link to `docs/HISTORY.md` 2026-04-11 entry. Impostor-domain awareness baked into the read-first surface.

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-23 | 3.3.2 | structural-inventory, context-file-map, governance-model, research-dimension-mapping | Initial evaluation (session 57). Dimensions 3 and 5 recorded as N/A with rationale — MemPalace is memory infrastructure, not an agent framework. 10 finding candidates surfaced; promotion pending Nick's gate. Scam-domain correction noted in watched-library entry. |
