---
title: "Agent Safety and Permissions"
type: "guideline"
category: "Sandboxing"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-19"
updated: "2026-07-16"
author: "claude"
source_findings:
  - "claude-code-auto-mode-ai-driven-permission-classif"
  - "gstack-four-layer-prompt-injection-defense"
  - "os-level-agent-sandboxing-filesystem-network-isolation"
  - "tiered-permission-system-bash-safety"
  - "independent-eval-and-scoped-authority-commandments"
  - "credential-isolation-bundled-auth-vault-proxy"
  - "shell-injection-vector-taxonomy-agent-bash-security"
  - "gsd-prompt-injection-scanner-hardening"
  - "sandbox-architecture-by-threat-model-microvm-vs-container"
  - "prompt-injection-risk-from-trusted-vs-untrusted"
  - "credential-setup-outside-llm-context-window"
  - "mcp-tool-description-prompt-injection-attack"
  - "scoped-environment-network-allowlist-governance"
  - "skill-security-audit-obligation"
  - "supply-chain-hardening-for-agent-packages"
  - "explicit-permission-allow-listing-for-agent-resou"
source_dd:
  - "DD-81"
  - "DD-78"
tags:
  - "guide"
  - "sandboxing"
  - "safety"
  - "permissions"
contract:
  preconditions: "You have an agent system that executes actions with side effects (file writes, shell commands, API calls, network requests). You can classify tools by risk level. You have or can build enforcement mechanisms at the OS or orchestration layer. You control (or can audit) what skills, MCP servers, and packages the agent loads."
  invariants: "Permissions are tiered by risk — not binary allow/deny. Safety-critical constraints are enforced structurally, not via prompt instructions. The agent cannot modify its own permission configuration. Credentials never enter the model's context window. Isolation strength follows the threat model, not convenience. Defense is layered — no single mechanism is the sole protection."
  governance: "Permission configurations, network allowlists, and skill installs are governed artifacts. Changes require review. Sandbox boundaries are documented per environment. The trust boundary for skills and dependencies is install time — audit before adoption. This guide is owned by the Improvement Loop knowledge layer."
  recovery: "If a safety boundary is violated: halt, log, escalate. Investigate the enforcement mechanism, not just the agent's behavior. If approval fatigue is observed (>90% approval rate): add sandboxing or auto-classification to reduce prompt volume. If a credential enters agent context: rotate it. If a dependency or skill is found compromised: pin back, audit blast radius via the permission grant log."
---

# Agent Safety and Permissions

How to make your agent system safe — from tiered permission systems through threat-model-matched sandboxing, network allowlists, credential isolation, and prompt injection defense, to install-time trust for skills and dependencies. This guide is about structural enforcement, not prompt-based instructions. If a constraint matters, enforce it; if a decision is risky, gate it; if a secret exists, keep it out of the model's context.

## When to Use This Guide

- You are deploying an agent that executes shell commands, writes files, or makes API calls
- You need to prevent agents from accessing resources outside their scope
- You are designing a permission system for a multi-agent pipeline
- You want to reduce permission prompt fatigue without sacrificing safety
- You are exposing agents to untrusted content (web browsing, user-provided files, third-party MCP servers)
- You are choosing between sandbox providers or isolation architectures
- You are installing third-party skills, MCP servers, or packages into an agent harness

## Key Concepts

**1. Permissions are tiered, not binary.** Three trust tiers — built-in tools (highest trust), plug-in tools (medium), user-defined skills (lowest). Within each tier, commands are classified as safe (read-only), mutating, or destructive. Different classifications get different oversight levels.

**2. Structural enforcement beats prompt compliance.** An agent told "never access files outside the project directory" in a prompt may comply most of the time. An agent sandboxed via OS-level filesystem isolation (bubblewrap/seatbelt) physically cannot access files outside the project. Use both, but trust the structural layer.

**3. Define the negative space first.** Specify what agents explicitly cannot do before expanding what they can do. Start with minimal permissions and expand deliberately. Every permission expansion is a conscious decision, not a default — and each novel resource access should surface for explicit approval, creating an audit trail as a side effect.

**4. Approval fatigue is a real safety risk.** Anthropic data: users approve 93% of permission prompts without close attention. Rubber-stamping is objectively less safe than an AI classifier with a 17% false-negative rate. Sandboxing reduces prompt volume by 84%. Permissive-by-default DIY stacks have leaked tens of thousands of API keys.

**5. Isolation strength follows the threat model, not pricing.** "Which sandbox?" is a safety question, not a cost comparison. Code the model generated on the fly is untrusted and needs hardware isolation (microVM). Code you wrote that needs persistent state fits a shared-kernel container. A supervised local coding agent is served by OS primitives. Picking by latency or price means paying for isolation you don't need — or not getting the isolation you do need.

**6. The attack surface includes your tooling, not just content.** Prompt injection arrives through web pages and files, but also through MCP tool descriptions (model-readable metadata is a live injection vector), skill instructions and bundled scripts, and compromised npm dependencies. Tool access is a security boundary, not a feature toggle.

**7. Credentials never enter the model's context.** Anything pasted or read into an agent session is sent to the API, logged in history, and extractable via prompt injection. Enter credentials in a separate process, inject scoped tokens at sandbox init, or route calls through a vault proxy — the model should only ever see the tool's response, never the secret.

**8. Defense is layered.** No single mechanism — classifier, sandbox, allowlist, scanner, or audit — is sufficient alone. Defense-in-depth ensures that bypass of one layer is caught by the next.

---

## Procedure

### Step 1: Classify All Tools by Risk

| Risk Level | Description | Examples | Oversight |
|-----------|-------------|---------|-----------|
| **Safe** | Read-only, no side effects | File reads, grep, glob, git status | Auto-allow |
| **Mutating** | Creates or modifies within project scope | File writes, edits within project directory | Auto-allow with audit trail |
| **Destructive** | Irreversible or out-of-scope effects | rm -rf, drop table, git push --force, production deploys | Require approval or block |

Cross this with the three trust tiers: built-in tools → plug-in tools → user-defined skills. A "safe" operation from a low-trust skill deserves more scrutiny than the same operation from a built-in tool.

For shell commands, build a safety module that pre-classifies commands before execution — Claude Code runs 23 numbered security checks on every bash command, covering pre-approved patterns, destructive command detection, and named injection-vector defenses (Step 6).

**Novel resources require explicit approval.** Beyond command classification, gate first-time access to each resource (file path, API endpoint, system service). When the agent touches a resource not on the allowlist, surface a permission prompt; the grant persists so repeat access doesn't re-prompt. This mirrors the mobile-OS permission model users already understand, and produces an audit trail of everything the agent has ever been allowed to touch.

### Step 2: Implement the Permission Architecture

Layer three tiers of enforcement, from bottom (structural) to top (intelligent):

```
┌──────────────────────────────────┐
│ Tier 3: AI Classifier            │ ← Smart filter for ambiguous cases
│   Reasoning-blind transcript     │    (Stage 1: single-token filter,
│   classifier evaluates actions   │     Stage 2: CoT only if flagged)
├──────────────────────────────────┤
│ Tier 2: Project Scope Rules      │ ← Auto-allow within project boundary
│   File ops within project dir    │    Reviewable via version control
│   auto-allowed                   │
├──────────────────────────────────┤
│ Tier 1: OS Sandbox               │ ← Structural enforcement floor
│   Filesystem isolation           │    Cannot be bypassed by the agent
│   Network isolation via proxy    │    Credential proxy for secrets
│   (bubblewrap / seatbelt)        │
└──────────────────────────────────┘
```

**Key design insight for the AI classifier:** Make it reasoning-blind — the classifier sees user messages and tool calls but NOT the agent's reasoning. This prevents the agent from "talking the classifier into" allowing dangerous actions.

**Strip permissive rules on entry to autonomous mode.** When the system shifts to higher autonomy, drop any user rules that enable arbitrary code execution (blanket shell allowances, wildcarded interpreters) so the classifier always sees high-risk commands. Autonomy and permissiveness must not stack.

**Classify at delegation boundaries too.** In multi-agent systems, run the classifier at both ends of subagent delegation: outbound (a subagent sees the orchestrator's instruction as its "user message" — catch unintended delegations) and inbound (results returning to the orchestrator).

**Deny-and-continue pattern:** When an action is blocked, return the denial as a tool result with instructions to find a safer approach. Don't terminate the session. Backstop: stop after 3 consecutive or 20 total denials and escalate to human.

### Step 3: Choose the Isolation Architecture by Threat Model

The isolation decision is determined by one question — *whose code runs, and how untrusted is it?* — not by latency or pricing.

```
Is the agent executing model-generated code
against systems you can't afford to lose?
├── YES → microVM (Firecracker / E2B class)
│         Dedicated kernel per session; hardware isolation;
│         ~150ms cold start. The boundary is a syscall
│         boundary, not a namespace.
└── NO → Does the workflow need state to persist
         across sessions (packages, files, env)?
         ├── YES → Shared-kernel container (Docker / Daytona class)
         │         27–90ms cold start; persistent workspaces;
         │         adequate when the code is yours.
         └── NO → Is this a supervised local coding agent?
                  ├── YES → OS primitives (bubblewrap / seatbelt)
                  │         Filesystem + network isolation without
                  │         container overhead; covers subprocesses.
                  └── NO → Worktree isolation (file-level only)
                           NOT a security boundary — no process or
                           network containment. Parallelism tool only.
```

Whatever architecture you pick, enforce both dimensions:

| Isolation Type | What It Enforces | Mechanism |
|---------------|-----------------|-----------|
| **Filesystem** | Read/write restricted to project directory | Linux bubblewrap, macOS seatbelt, container/VM boundary |
| **Network** | Outbound traffic restricted to allowed domains | Proxy with domain allowlist (Step 4) |
| **Credentials** | Secrets stay outside the sandbox | Credential proxy / bundled auth (Step 5) |

Both filesystem AND network isolation are essential. Without network isolation, a compromised agent exfiltrates files (SSH keys). Without filesystem isolation, an agent escapes to gain network access. A correctly sandboxed agent that suffers a successful prompt injection still cannot steal keys or contact attacker servers.

**Graduated sandboxing** is a legitimate middle path: default to containers, escalate to microVMs when a task classifier flags untrusted code.

### Step 4: Enforce the Network Boundary

Network access control is orthogonal to execution isolation: the sandbox prevents the agent from affecting the host; the allowlist prevents it from reaching services it shouldn't — regardless of what code it runs.

1. **Default deny-all.** The environment type starts "highly limited": only declared endpoints are reachable.
2. **Declare exact endpoints, not wildcards.** `mcp.clickup.com`, not `*.clickup.com` and never `*.googleapis.com`-style breadth — overly broad allowlists undermine the boundary.
3. **Gate MCP access as a separate flag.** Whether the environment can speak MCP at all is a distinct permission from which hosts it can reach.
4. **Route new-domain requests through approval.** When the agent needs an endpoint not on the list, surface it for human confirmation rather than failing silently or allowing silently.
5. **Log network traffic per agent.** The allowlist controls *which* endpoints — it does not inspect *what data* flows through them. Exfiltration through an allowed endpoint (e.g., encoding stolen data into task descriptions on an allowed SaaS) remains possible; egress logging is your detection layer.

The allowlist is per-environment configuration, inspectable at audit time: you can open any environment and see exactly what it can reach. This is the same model as firewall rules and security groups, applied to agent environments — and it is the property that makes agent systems presentable to enterprise security review.

### Step 5: Keep Credentials Out of the Model's Context

Any text that enters an agent session becomes model context: sent to the API, logged in conversation history, and extractable via prompt injection. Token *scoping* helps but assumes model limitations; architectural *isolation* — the secret physically never present — is more robust. Three patterns, in ascending infrastructure cost:

| Pattern | How It Works | When to Use |
|---------|-------------|-------------|
| **Separate-process entry** | Setup flow spawns a separate terminal for credential entry; the agent guides setup but never sees the keys, then validates connections without reading them | Interactive setup wizards; zero infrastructure |
| **Bundled auth** | Inject a scoped token at sandbox initialization (e.g., clone the repo with a repo-specific token wired to the local git remote); the agent pushes/pulls without ever handling the token | Git operations; per-session scoped resources |
| **Vault proxy** | A dedicated proxy fetches credentials from a vault using a session-associated token and calls the external service on the agent's behalf; the agent sees only the tool's response | Custom/MCP tool integrations at scale |

Make the pattern *architectural*, not a user discipline — enforce it in the tool flow so the safe path is the only path. Watch for: tokens cached in git config persisting across sandbox reuse; the vault proxy as a single point of failure; users bypassing the wizard and pasting keys directly into the session (if that happens, rotate the key).

### Step 6: Harden Shell Access Against Injection Vectors

A pattern allowlist of known-safe commands is not a bash security layer. Shells offer expansion and parsing tricks that defeat literal matching — a production guard needs an *enumerated injection-vector list*, maintained over time:

| Vector | Attack | Defense |
|--------|--------|---------|
| **Zsh equals expansion** | `=curl` resolves to the full path of curl, bypassing a literal `curl` allowlist | Block `=cmd` expansion forms |
| **Unicode zero-width insertion** | `c\u200Burl` renders as "curl" visually but doesn't match the literal | Normalize/reject zero-width and confusable characters in command names |
| **IFS null-byte injection** | Splits a blocked command name across safe-looking tokens | Validate post-tokenization command identity |
| **Shell builtins** | Aliases, functions, eval variants re-bind command names after the check | Block the builtin layer (18 of Claude Code's 23 checks target Zsh builtins) |
| **Malformed-token parsing** | Parser edge cases produce a different command than the checker saw | Fuzz the guard; track disclosure channels — this class was found via bug bounty |

Two operational rules: (1) audit any proposed bash hook or shell guard against each named vector, not just against a list of "dangerous commands"; (2) treat the taxonomy as a point-in-time snapshot — the vector list grows, so subscribe to disclosure channels. Every shell path must run the guard; a hook that bypasses it silently defeats the guarantee.

If your agent doesn't truly need a shell, structured-tool-only operation eliminates this entire class.

### Step 7: Defend Against Prompt Injection at Every Input Boundary

Untrusted content is any text the agent reads that you didn't write: web pages, user files, external API responses — *and tool metadata*.

**7a. Content defense-in-depth** for agents reading untrusted web/file content:

| Layer | Defense | Purpose |
|-------|---------|---------|
| 1 | **Content envelope** | Bracket untrusted content with explicit markers; inject zero-width spaces to prevent marker spoofing |
| 2 | **Hidden element stripping** | Remove CSS-hidden content and ARIA label injection from web pages |
| 3 | **Datamarking** | Session-scoped watermarks (zero-width chars) for content leakage tracing |
| 4 | **Content filter hooks** | URL blocklist (requestbin, pipedream, webhook.site) + custom filters |

**7b. Proactive scanning** before content enters the context window (as a pre-processing hook, not a post-hoc audit): invisible-Unicode detection, encoding-obfuscation detection (base64/hex payloads), structural validation, and entropy analysis for statistically anomalous blocks. Expect false positives from entropy analysis on code and non-Latin text; tune with a feedback loop. A scanner catches known vector classes — it is one layer, not the defense.

**7c. Probe tool output.** Scan tool results before they enter the agent's context (the injection may arrive via a "trusted" tool reading an untrusted source).

**7d. MCP tool descriptions are an injection vector.** Tool metadata is model-readable, and MCP enforces no access control at the protocol level — malicious instructions embedded in a tool description redirect agent behavior ("tool poisoning"). Mitigations: audit the descriptions of every MCP server you connect (they flow into context unvalidated); scope tool visibility per task rather than exposing everything; require approval flows for sensitive operations; keep audit trails of tool calls and parameters.

**7e. Session hygiene.** Don't combine untrusted browsing with sensitive channels in one session: a prompt-injected page plus an open email tool equals an exfiltration path. Quarantine sensitive capabilities (email, banking, production access) from general-web sessions; browse arbitrary sites only from sessions with nothing worth stealing.

### Step 8: Secure the Supply Chain — Install-Time Trust

For skills, plugins, and packages, the trust boundary is **install time, not run time**. The harness can provide guardrails (trust dialogs, shell-execution kill switches, frontmatter restrictions), but none substitute for human audit before adoption.

**Skill audit — three attack surfaces:**

1. **Static instructions** in the skill body — visible at audit time; read them.
2. **Bundled scripts and resources** — execute with your environment's privileges; visible but effortful to review; pay particular attention to code dependencies.
3. **Dynamic fetched content** — instructions that pull external URLs at activation time are NOT visible at audit time; the URL can serve benign content when you audit and malicious content later. Treat network-fetching instructions inside skills as the highest-risk feature.

Apply the *Principle of Lack of Surprise*: a skill's contents should never surprise you relative to its description. Watch for allowed-tools grant inflation — a skill granting itself broad tool access rides in on a single workspace-trust acceptance. In organizations, remember auditor ≠ installer: the audit must scale to the audience, and results must reach the people running the skill.

**Package hardening** (agent harnesses are high-value supply-chain targets — they run with user permissions and execute commands):

- Exact-pin direct external dependencies (no semver ranges)
- Set a minimum release age (e.g., 2 days) to dodge same-day compromised releases
- Ship a generated shrinkwrap/lockfile that locks the full tree for end users
- Guard lockfile changes behind an explicit pre-commit escape hatch
- Install with lifecycle scripts disabled by default; allowlist exceptions after review
- Run a verification script (pinning, imports, shrinkwrap freshness) in CI

Accepted costs: manual update burden, delayed patches, shrinkwrap regeneration. They are the price of treating dependency changes as reviewed code changes.

### Step 9: Instrument and Monitor

Build observability from day one — it is expensive to retrofit, and you must never rely on the agent's own reports of whether it behaved:

- **Permission grant log:** Every approval, denial, and auto-allow with the action, risk classification, and tier that handled it
- **Sandbox violation log:** Every blocked filesystem or network access attempt
- **Network egress log:** Per-agent traffic to allowed endpoints (your exfiltration detection layer)
- **Credential proxy log:** Every credential use through the proxy — anomalous usage patterns indicate compromise
- **Classifier decision log:** What the classifier saw, what it decided, why (Stage 1 vs Stage 2)
- **Approval rate tracking:** If approval rate exceeds 90%, investigate for fatigue
- **Skill/dependency manifest:** Which skills and packages are installed, who installed them, when last audited

---

## Templates

### Permission Architecture Worksheet

```markdown
## Permission Architecture — {{SYSTEM_NAME}}

### Threat Model
- Whose code executes: {{OURS/MODEL-GENERATED/MIXED}}
- Blast radius if compromised: {{DESCRIPTION}}
- Isolation architecture chosen: {{OS-PRIMITIVES/CONTAINER/MICROVM/GRADUATED}}

### Tool Risk Classification
| Tool / Command | Trust Tier | Risk Level | Oversight |
|---------------|-----------|-----------|-----------|
| {{TOOL}} | {{built-in/plug-in/skill}} | {{safe/mutating/destructive}} | {{auto/approve/block}} |

### Sandbox Configuration
- Filesystem boundary: {{PATH}}
- Network allowlist (exact endpoints): {{DOMAINS}}
- MCP access: {{ENABLED/DISABLED}}
- Credential handling: {{SEPARATE-PROCESS/BUNDLED-AUTH/VAULT-PROXY/NONE}}

### Classifier Configuration (if using AI classification)
- Reasoning-blind: {{YES/NO}}
- Block rules: {{LIST}}
- Allow exceptions: {{LIST}}
- Denial backstop: {{N}} consecutive, {{M}} total
- Classify subagent delegations: {{OUTBOUND/INBOUND/BOTH}}

### Monitoring
- Approval rate target: < {{PERCENT}}%
- Permission log location: {{PATH}}
- Egress log location: {{PATH}}
- Review frequency: {{SCHEDULE}}
```

### Install-Time Audit Checklist

```markdown
## Install Audit — {{ARTIFACT_NAME}} ({{skill/MCP server/package}})

- Source / provenance: {{URL_OR_REGISTRY}} — trusted publisher? {{YES/NO}}
- Static instructions reviewed: {{YES/NO}} — surprises vs description? {{NOTES}}
- Bundled scripts reviewed: {{YES/NO/N-A}} — dependencies: {{LIST}}
- Fetches external content at run time: {{YES/NO}} — if YES: {{URLS + RISK ACCEPTANCE}}
- Tool descriptions audited for embedded instructions: {{YES/NO/N-A}}
- Tools/permissions it grants itself: {{LIST}} — narrowest viable? {{YES/NO}}
- Version pinned: {{EXACT_VERSION}} — release age: {{DAYS}}
- Lifecycle scripts required: {{NO/ALLOWLISTED: LIST}}
- Auditor: {{NAME}} — date: {{DATE}} — verdict: {{ADOPT/REJECT/ADOPT-WITH-CONSTRAINTS}}
```

**Worked example (checklist):**

```markdown
## Install Audit — notion-mcp (MCP server)

- Source / provenance: claude.ai connector registry — trusted publisher? YES (first-party)
- Static instructions reviewed: YES — surprises vs description? None
- Bundled scripts reviewed: N/A (hosted server)
- Fetches external content at run time: YES — serves workspace page content;
  RISK ACCEPTED: workspace is self-authored, low injection exposure
- Tool descriptions audited for embedded instructions: YES — descriptive only
- Tools/permissions it grants itself: read/write pages, query databases —
  narrowest viable? NO (write enabled; acceptable for Household OS ops only)
- Version pinned: hosted (provider-managed) — release age: N/A
- Lifecycle scripts required: NO
- Auditor: Nick — date: 2026-07-16 — verdict: ADOPT-WITH-CONSTRAINTS
  (Notion MCP only for Household OS operational work, never governance data)
```

---

## Worked Example: MetaSystem Safety Architecture

```
Permission Architecture — MetaSystem (improvement-loop engine)

THREAT MODEL:
- Whose code executes: OURS + agent-authored scripts (supervised)
- Blast radius: local vault corruption; git history is the recovery net
- Isolation architecture: OS primitives tier appropriate (supervised
  local coding agent; no untrusted model-generated code against
  production systems)

CURRENT STATE:
- CLAUDE.md rules (prompt-layer) ← primary constraint mechanism
- "Never modify files outside system boundary" ← prompt instruction, not enforced
- Human gate (DD-29) ← procedural, not structural
- Pre-commit hooks ← structural enforcement (frontmatter validity,
  PROGRESS line budget)
- bypassPermissions mode ← Nick's ruling: no permission prompts;
  compensating control is upfront external-surface validation

GAPS:
- No OS-level sandboxing (filesystem or network)
- Destructive command safety is prompt-based, not structural
- No permission grant or egress logging
- MCP tool descriptions (Notion, Perplexity, Context7) enter context
  unaudited — bounded today by first-party server trust
- No skill-install audit checklist (imported skills adopted by review
  convention, not recorded audit)

RECOMMENDED NEXT INCREMENTS:
1. Enable Claude Code sandboxing — filesystem: MetaSystem/ directory;
   network allowlist: github.com, api.anthropic.com, perplexity.ai,
   mcp.notion.com (exact endpoints, deny-all default)
2. Bash-hook hardening audited against the Step 6 injection-vector
   taxonomy (not a hand-rolled pattern list)
3. Install-Time Audit Checklist for every imported skill / MCP server
   (record auditor + date; Notion MCP constraint already codified)
4. Credentials: keep API keys in shell profile / keychain, never pasted
   into sessions (separate-process pattern; zero infrastructure)
```

---

## Pitfalls

### 1. All safety in the prompt layer
"Never access files outside the project" is a prompt instruction that the agent may fail to follow. If the constraint matters, enforce it structurally — filesystem isolation, pre-tool-use hooks, API authentication gates.

### 2. Binary permissions (allow everything or ask everything)
Users rubber-stamp 93% of prompts. Binary permission systems either bottleneck the agent or create dangerous approval fatigue. Tier the permissions by risk.

### 3. Reasoning-visible classifiers
If the classifier can read the agent's reasoning, the agent can craft reasoning that convinces the classifier to allow dangerous actions. Make classifiers reasoning-blind.

### 4. Filesystem isolation without network isolation (or vice versa)
Either isolation alone is insufficient. Without network: agent exfiltrates files. Without filesystem: agent escapes to gain network access. Both are needed.

### 5. Permission expansion by default
Every tool starts with maximum permissions. The safe approach: start with minimum and expand deliberately. Define what the agent cannot do before what it can do.

### 6. Choosing a sandbox by price or latency
MicroVM vs container is a threat-model decision. Untrusted code routed to a shared-kernel container makes container escape a realistic compromise path; trusted stateful workflows forced onto microVMs destroy the persistence the workflow needs. Ask "is the code untrusted?" first.

### 7. Allowlist theater
A network allowlist with broad wildcard entries, or one nobody maintains, provides the audit story without the security. And even an exact allowlist does not inspect egress content — data can be exfiltrated *through* an allowed endpoint. Pair the allowlist with egress logging.

### 8. Credentials in the context window
An API key pasted into a session is logged, cached, and extractable by injection for the rest of that session's life. Enter secrets in a separate process, or proxy them. If a secret does enter context, rotate it — don't hope.

### 9. Install-time audit theater
Accepting the workspace trust dialog without reading the skill, or adopting "popular" skills on reputation, defeats the trust boundary. The dialog exists; the audit is on you. Skills that fetch external content at run time can pass a static audit and turn malicious later — flag them explicitly.

### 10. Fresh dependencies and lifecycle scripts
Same-day npm releases and install-time lifecycle scripts are the classic agent-harness supply-chain vectors. Pin exact versions, enforce a minimum release age, and install with scripts disabled by default.

### 11. Scanner as the whole defense
Injection scanners catch known vector classes (invisible Unicode, encoded payloads, anomalous entropy). Novel techniques pass through. A scanner that lulls you into skipping the content envelope, tool-output probing, and session hygiene made you less safe.

### 12. Shell allowlists without vector defenses
An allowlist of safe commands is defeated by `=curl`, zero-width characters, IFS injection, and builtin re-binding. Audit any shell guard against the enumerated vector taxonomy, and treat the taxonomy as living — at least one production bypass was found via bug bounty after release.

---

## Related Guides

- **Risk classification → tool registries:** The risk levels in Step 1 map to the metadata-first tool registry in *Designing Agent Tools* (G5), Step 1. G5 also covers tool-gateway design, which is where Step 7d's MCP scoping mechanically lives.
- **Hard constraint enforcement → boundary design:** Hard constraints that need structural enforcement are defined in *Writing Agent Specifications* (G1), Step 3a.
- **Untrusted content → context curation:** When agents read untrusted web content, context curation principles from the context guides (G2a/G2b) apply alongside the injection defenses in Step 7.
- **Oversight and autonomy tiers → governance:** Who approves what, autonomy gradation, change-approval tiering, and kill switches are governance concerns — *Agent Governance and Trust* (G9). This guide supplies the enforcement mechanics beneath those policies.
- **Sandbox isolation → state durability:** The sandbox/microVM isolation this guide covers shares its infrastructure with the disk-level persistence substrate in *[[session-persistence-and-memory]]* (G7), Step 3.7 (incremental snapshotting, always-on POSIX storage, lineage-aware scheduling). G6 covers the isolation/threat-model side; G7 covers what the same sandbox buys for crash recovery and durable state.

---

## Contract

### Preconditions
- You have an agent system that executes actions with side effects.
- You can classify tools by risk level (safe/mutating/destructive) and by trust tier (built-in/plug-in/skill).
- You have or can build enforcement mechanisms at the OS or orchestration layer.
- You control, or can audit, the skills, MCP servers, and packages the agent loads.

### Invariants
- Permissions are tiered by risk, not binary allow/deny.
- Safety-critical constraints are enforced structurally, not via prompt instructions alone.
- The agent cannot modify its own permission configuration.
- Credentials never enter the model's context window.
- Isolation strength follows the threat model — untrusted code gets hardware isolation.
- Network access is deny-all by default; endpoints are declared exactly.
- The trust boundary for skills and dependencies is install time; audit precedes adoption.
- Defense is layered — no single mechanism is the sole protection.

### Governance
- Permission configurations, network allowlists, and install decisions are governed artifacts. Changes require review.
- Sandbox boundaries are documented per environment and inspectable at audit time.
- Approval rates are monitored — rates above 90% trigger investigation.
- A manifest tracks installed skills/packages, installer, and audit date.

### Recovery
- If a safety boundary is violated despite structural enforcement: treat as a security incident — halt, log, escalate. Investigate the enforcement mechanism failure, not just the agent's behavior.
- If approval fatigue is observed: add sandboxing or auto-classification to reduce prompt volume rather than telling users to "pay more attention."
- If prompt injection is detected: activate content filter hooks, review the content source, and add the source to blocklists if necessary.
- If a credential enters agent context: rotate it immediately; audit the session transcript for exfiltration.
- If a skill or dependency is found compromised post-install: remove/pin back, then use the permission grant log and egress log to bound the blast radius.
