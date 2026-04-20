---
notion_id: 3351e08b-9b34-81d3-b6f3-c9bc4d7d112e
name: Claude Code Auto Mode -- AI-Driven Permission Classification
summary: 'March 24, 2026 Research Preview. Two-layer safety architecture: (1) Prompt injection probe scans tool output before it enters Claude''s context; (2) Sonnet 4.6 transcript classifier evaluates
  every action before execution -- fast single-token filter (Stage 1) -> CoT reasoning only on flagged actions (Stage 2). Classifier is reasoning-blind (sees user messages + tool calls only, not Claude''s
  own reasoning). Anthropic data: users approve 93% of prompts anyway, making auto mode objectively safer than rubber-stamping.'
implementation_notes: 'Resolves the core autonomy-safety tension in agentic coding. The reasoning-blind classifier design is the key security innovation. Currently Team plan only (rolling to Enterprise/API).
  17% false-negative rate on overeager actions (Anthropic published). Source: https://techcrunch.com/2026/03/24/anthropic-hands-claude-code-more-control-but-keeps-it-on-a-leash/'
category: Sandboxing
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-codes-leak-changes-everything.md
- anthropic-claude-code-auto-mode.md
- anthropic-claude-code-sandboxing.md
- anthropic-trustworthy-agents-in-practice.md
proposals: []
date_discovered: '2026-04-01'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- agent-safety-and-permissions.md
related_findings:
- file: tiered-permission-system-bash-safety.md
  rel: same-problem
- file: human-on-the-loop-hotl-autonomy-tiering-framework.md
  rel: same-problem
- file: explicit-permission-allow-listing-for-agent-resou.md
  rel: same-problem
---
# Claude Code Auto Mode -- AI-Driven Permission Classification

## What It Is
A "middle path" between full manual approval and `--dangerously-skip-permissions`. Two-layer architecture:
1. **Prompt Injection Probe** -- Scans all tool output before it enters Claude's context
2. **Sonnet 4.6 Transcript Classifier** -- Evaluates every proposed action before execution, reasoning-blind design

**Key design insight**: Claude cannot "talk the classifier into" allowing a dangerous action because the classifier cannot read Claude's reasoning.

## Why It Matters
Users approve 93% of prompts anyway (rubber-stamping). Auto mode is a safety upgrade over rubber-stamping.

## Why People Are Using It
Directly addresses the "constant supervision" bottleneck. 460 Reddit upvotes day-of announcement. Anthropic's own internal data: users approve 93% of prompts without close attention (approval fatigue).

### Three-Tier Permission Filtering (2026-04-09, Anthropic primary source)
Actions pass through three tiers; only risky ones reach the classifier:
- **Tier 1: Built-in safe-tool allowlist + user settings** -- Non-modifying tools auto-allowed. On auto mode entry, drops rules enabling arbitrary code execution (blanket shell, wildcarded interpreters) so classifier always sees high-risk commands.
- **Tier 2: In-project file operations** -- File writes/edits inside the project directory auto-allowed (reviewable via version control). No classifier latency cost.
- **Tier 3: Transcript Classifier** -- Shell commands, web fetches, external tools, subagent spawns, out-of-project filesystem ops. Stage 1 single-token filter -> Stage 2 CoT only if flagged.

### Deny-and-Continue Pattern (2026-04-09)
Blocked actions return as tool results with instructions to find safer paths, not bypass. Backstop: stop after 3 consecutive or 20 total denials, escalate to human. In headless `claude -p` mode, terminates instead.

### Multi-Agent Handoffs (2026-04-09)
Classifier runs at both ends of subagent delegation: outbound (catches unintended delegations, since subagent sees orchestrator instruction as "user message") and inbound (results return).

### Classifier Decision Criteria (2026-04-09)
Fixed prompt template with 3 customizable slots for policy. >20 block rules grouped as: cross trust boundaries (external repo code, credential stores, unmentioned services) and bypass review/affect others (push to main, production deploys, shared resources). Mandatory allow exceptions for benign patterns: install repo-declared packages, standard credential flows, push to working branch.

## Potential Failure Modes
17% false-negative rate on overeager actions. Reasoning-blind design means classifier misses prior approvals as patterns (one approval does not equal consent for larger blast radius). Stage 2 CoT adds cost when triggered frequently.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[reasoning-blind-permission-classifier]] in `extracts/patterns/`
