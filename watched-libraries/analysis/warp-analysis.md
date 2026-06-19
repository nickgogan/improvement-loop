---
title: "Warp -- Structural Analysis"
id: "warp-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-05-24"
updated: "2026-05-24"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "warp"
  - "agentic-ide"
  - "skills-system"
  - "feature-flags"
  - "rust"
analyzed_version: "latest (commit a530563, 2026-05-24)"
analyzed_date: "2026-05-24"
repo_url: "https://github.com/warpdotdev/warp"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# Warp -- Structural Analysis

## Metadata
- **Repo:** https://github.com/warpdotdev/warp
- **Version analyzed:** latest (commit a530563, 2026-05-24 shallow clone)
- **Date:** 2026-05-24
- **Spectrum position:** study
- **Stars:** ~25k | Rust workspace (60+ crates)

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Rust source files | 3,299 |
| Total files | 5,317 |
| Cargo workspace members | 60+ crates |
| Agent skills | 15 (.agents/skills/) |
| Warp workflows | 10+ (.warp/workflows/) |

### Key Directories
```
app/              — Main binary (terminal, AI, auth, drive, workspace)
crates/
  warpui/         — Custom UI framework (MIT-licensed)
  warpui_core/    — Core UI primitives
  warp_core/      — Core utilities, feature flags, platform abstractions
  editor/         — Text editing
  ipc/            — Inter-process communication
  graphql/        — GraphQL client
  integration/    — Integration tests
.agents/skills/   — Agent skill definitions (SKILL.md per skill)
.claude/          — Claude Code config (settings.json, statusline.sh)
.warp/
  workflows/      — Terminal workflow definitions (YAML)
  skills/         — Warp-native skills
specs/            — Feature specifications
```

### Agent Skills Inventory
| Skill | Purpose |
|-------|---------|
| `triage-issue-local` | Repo-specific issue triage (specializes core `triage-issue`) |
| `review-pr-local` | Repo-specific PR review (specializes core `review-pr`) |
| `reproduce-bug-report-local` | Bug reproduction |
| `dedupe-issue-local` | Issue deduplication |
| `rust-unit-tests` | Rust test generation |
| `add-telemetry` | Telemetry instrumentation |
| `promote-feature` | Feature flag promotion (dogfood → preview → stable) |
| `remove-feature-flag` | Feature flag cleanup |
| `add-feature-flag` | New feature flag creation |
| `changelog-draft` | Changelog generation |
| `classify-changelog-pr` | PR changelog classification |
| `create-launch-modal` | UI modal generation |
| `warp-ui-guidelines` | UI component standards |
| `warp-integration-test` | Integration test generation |
| `onboarding-verification-skill` | New developer onboarding verification |

---

## 2. Context File Map

### Context Hierarchy
| File | Purpose | Scope |
|------|---------|-------|
| `WARP.md` | Development commands, architecture overview, platform setup | Repo-wide |
| `.claude/settings.json` | Claude Code configuration | Claude agent |
| `.claude/statusline.sh` | Status line script | Claude agent |
| `.mcp.json` | MCP server configuration (GitHub only) | All agents |

### WARP.md Architecture
WARP.md serves as the primary agent context file (like CLAUDE.md). Contains:
1. Build/run commands (cargo, nextest)
2. Running with local warp-server (env vars)
3. Testing instructions (nextest, doc tests)
4. Linting/formatting (presubmit, clippy, clang-format, wgslfmt)
5. Platform setup (bootstrap script, common-skills)
6. Architecture overview (WarpUI framework, Entity-Handle pattern)
7. Development guidelines (workspace structure, patterns, AI integration)

---

## 3. Workflow Topology

### Feature Flag Lifecycle (5 stages)
```
Add flag → Dogfood (DOGFOOD_FLAGS) → Preview (PREVIEW_FLAGS)
→ Stable (Cargo default features + lib.rs bridge) → Remove (cleanup)
```

Each stage has explicit:
- File changes required (1-3 files per stage)
- Validation steps (cargo fmt + clippy)
- Follow-up actions (Linear issue for cleanup)

### Skills-Lock Pattern
```
skills-lock.json  ← managed by `npx skills@1.5.6`
                  ← install_common_skills script reads it
                  ← bootstrap script triggers install
                  ← install target: --project or --global
```

Key properties:
- Lock file prevents silent overwrites across checkouts
- Errors if skills exist in both project and global
- Non-interactive flows fail without explicit target
- `WARP_COMMON_SKILLS_REF` env var for testing remote branches

### Core/Specialized Skill Pattern
Skills have a `specializes` frontmatter field:
```yaml
name: triage-issue-local
specializes: triage-issue
description: Repo-specific triage guidance for warp. Only the categories declared overridable by the core triage-issue skill may be specialized here.
```

Core skills define overridable categories. Local skills only override those specific categories. This enables:
- Shared logic in a central `common-skills` repo
- Repo-specific customization without forking
- Explicit contract about what can be specialized

---

## 4. Governance Model

### Presubmit Pipeline
```bash
./script/presubmit  # fmt → clippy → tests (all-in-one)
```

### PR Review Pattern (from review-pr-local skill)
- Visual evidence required for UI changes (screenshots/videos)
- At most 2 follow-up questions per triage response
- Label taxonomy managed in `.github/issue-triage/config.json`
- `ready-to-implement` requires reproducibility + narrow fix path
- Graceful degradation: prefer omitting absent data over empty/broken UI

### Oz for OSS
Partner program bringing agentic workflows to external repos. Thousands of Oz agents publicly visible at build.warp.dev triaging issues, writing specs, implementing changes, reviewing PRs.

---

## 5. Cross-Agent Protocol

### Oz Agent API (via oz-workspace reference)
- **Rooms**: Bounded contexts where agents collaborate
- **@mentions**: Agent-to-agent communication within rooms
- **Tasks**: Per-room kanban that agents self-manage
- **Artifacts**: PRs, plans, documents produced by agents
- **Notifications**: Inbox alerts (async coordination)
- **SSE**: Real-time event streaming for updates
- **Agent auth**: Token-based auth for agent callbacks

### Multi-Agent Coordination in Warp Repo
- build.warp.dev dashboard shows active agent sessions
- Oz agents handle: issue triage, spec writing, implementation, PR review
- Top contributors visible alongside agent contributions
- Agent sessions viewable in web-compiled Warp terminal

---

## Findings Candidates

| # | Pattern | Priority | Category | Evidence |
|---|---------|----------|----------|----------|
| 1 | **Core/Specialized Skill Inheritance Pattern** — Skills declare a `specializes` field linking to a core skill. Core skills define overridable categories; local skills only customize those slots. Enables shared skill logic with repo-specific behavior. | P1 | Agent Design | triage-issue-local, review-pr-local SKILL.md frontmatter |
| 2 | **Skills-Lock for Portable Agent Skills** — `skills-lock.json` managed by `npx skills` CLI. Install targets (project/global), version pinning, conflict detection (both locations), branch testing via env var. | P2 | Tool Integration | skills-lock.json, install_common_skills script, bootstrap |
| 3 | **Feature Flag Lifecycle as Deployment Governance** — 5-stage promotion (add → dogfood → preview → stable → remove) with explicit file-change recipes and follow-up issue creation. 1-2 release cycle buffer before removal. | P2 | Governance | promote-feature SKILL.md, remove-feature-flag SKILL.md |
| 4 | **Oz Multi-Agent Room Model** — Agents assigned to rooms, communicate via @mentions over SSE, self-manage kanban tasks, produce typed artifacts. Human observers see real-time work. | P2 | Orchestration | oz-workspace architecture, build.warp.dev |
| 5 | **Visual Evidence Gate for UI PRs** — Automated PR review requires screenshots/videos for any user-visible change. No exemptions for "headless" environments — suggests computer-use alternatives. Verdict is REJECT without evidence. | P3 | Evaluation | review-pr-local SKILL.md |
| 6 | **Follow-Up Question Budget in Agent Triage** — Hard limit of 2 follow-up questions per triage response. Each must be "high-value" (changes label, routing, or reproduction confidence). Prevents over-questioning. | P3 | Agent Design | triage-issue-local SKILL.md |
