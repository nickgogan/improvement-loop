---
name: Skill Security Audit Obligation (Trust Boundary at Install Time)
summary: 'Anthropic''s skill documentation puts the trust boundary at install time, not run time. Skills are powerful precisely because they can invoke tools and execute code; that same property makes them
  a privileged-code surface. The recommended discipline: install only from trusted sources; audit the SKILL.md, scripts, and bundled resources before use; pay particular attention to instructions that fetch
  external content (which may carry injected instructions) and to code dependencies. The ''Principle of Lack of Surprise'' from skill-creator: a skill''s contents should not surprise the user in their intent
  if described.'
implementation_notes: 'Three distinct attack surfaces identified across sources: (1) instructions in SKILL.md that direct Claude to take harmful action (loaded into context, visible at audit time); (2)
  bundled scripts that execute with the user''s environment privileges (filesystem, network, etc.); (3) instructions that fetch external content which may carry injected instructions (dynamic — not visible
  at audit time). Defensive features in the harness: workspace trust dialog for project-level skills with allowed-tools; reserved-word ban on ''anthropic''/''claude'' to prevent impersonation; disableSkillShellExecution
  setting for managed environments; XML-tag ban in frontmatter. None of these substitute for human audit.'
category: Governance
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-equipping-agents-with-agent-skills.md
- anthropic-agent-skills-overview-docs.md
- anthropic-claude-code-skills-docs.md
- anthropic-skills-repo.md
related_findings:
- file: code-as-deterministic-tool-inside-skills.md
  rel: same-problem
- file: skill-invocation-control-side-effect-guard.md
  rel: same-problem
- file: skill-dynamic-context-injection-shell-prerender.md
  rel: same-problem
- file: skill-popularity-vs-measured-efficacy.md
  rel: same-problem
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-07-12'
pipeline_status: raw
consumed_by: []
---

# Skill Security Audit Obligation (Trust Boundary at Install Time)

## What It Is

Anthropic's canonical skill docs locate the trust boundary at install time, not run time. The user (or admin) is the audit authority; the harness provides defensive features but does not substitute for human review.

Stated obligation (across the engineering post and the docs):
- **"Install skills only from trusted sources"** — implies a provenance check before install.
- **"Thoroughly audit it before use"** — review SKILL.md, scripts, bundled resources.
- **"Pay particular attention to code dependencies and bundled resources like images or scripts"** — third-party dependencies expand the attack surface.
- **"Similarly, pay attention to instructions or code within the skill that instruct Claude to connect to potentially untrusted external network sources"** — fetched content can carry injected instructions.

The skill-creator skill's "Principle of Lack of Surprise" reinforces this from the authoring side: "A skill's contents should not surprise the user in their intent if described." Authoring discipline that matches install-time audit expectations.

Three distinct attack surfaces emerge:

1. **Static instructions in SKILL.md** — visible at audit time. A malicious skill that tells Claude to exfiltrate secrets is in the SKILL.md body.
2. **Bundled scripts** — executable code with the user's environment privileges. Visible at audit time but harder to evaluate (Python script in `scripts/foo.py` may be hundreds of lines).
3. **Dynamic instructions via fetched content** — NOT visible at audit time. A skill that fetches `https://x.example/instructions.md` brings whatever instructions that URL serves into context at activation time.

## Why It Matters

Skills are simultaneously a productivity feature and an attack surface. The same properties that make them useful — instructions in the system prompt, code that runs without context cost, dynamic context injection — are precisely the channels a malicious skill exploits.

The install-time audit model means harness-level controls are necessary but not sufficient. Workspace trust dialogs, `disableSkillShellExecution`, reserved-word bans on frontmatter, and XML-tag prohibitions all help, but the user remains the last line of defense. An organization shipping skills to its employees needs an audit process; an individual installing community skills needs to actually read them.

For MetaSystem consumers, this is governance-shaped: the autonomy tier of a skill installer (proposal-first, guarded, full-autonomy) maps directly to the install-time audit obligation.

## Why People Are Using It

The audit obligation is documented identically across all canonical sources — engineering post, platform.claude.com docs, Claude Code docs, anthropics/skills README disclaimer. The consistency suggests this is not a defensible-by-design property; the discipline is the defense.

The Claude Code docs explicitly extend the audit to workspace trust: "For skills checked into a project's .claude/skills/ directory, allowed-tools takes effect after you accept the workspace trust dialog for that folder. Review project skills before trusting a repository, since a skill can grant itself broad tool access."

## Potential Alternatives

Sandbox skills by default (heavier; defeats some of the on-filesystem benefit). Cryptographic signing for trusted skill sources (infrastructure cost; doesn't address all surfaces). Static analysis of skill scripts (catches some patterns; misses novel ones). Centralized skill repository with audit (Anthropic's `anthropics/skills` is one such; community needs more). LLM-as-auditor for skills (interesting but the LLM is itself a target — can be tricked).

## Potential Improvements

Signed skills with cryptographic provenance. Per-skill capability declaration (this skill needs network access; this skill writes to /tmp only). Audit tooling: a `skill-audit <skill-path>` CLI that surfaces the three attack surfaces explicitly. Project-wide skill manifest tracking which skills are present, who installed them, when audited.

## Potential Failure Modes

**Audit theater.** Users accept workspace trust without reading. The dialog exists; the obligation is on the user to actually look.

**Dynamic instruction injection.** A skill that fetches external content at activation time bypasses static audit. The fetched URL could serve benign content at audit time and malicious content later. The harness can't detect this; the user can't anticipate it.

**Bundled-dependency drift.** A skill that imports a Python package is only as safe as that package's current version. Audit at install time doesn't catch a package compromised after the fact.

**Audit fatigue.** Skills proliferate. Each one requires non-trivial review. Users develop heuristics ("Anthropic-published is fine") that don't generalize.

**Allowed-tools grant inflation.** A skill checked into a project with `allowed-tools: Bash(*) Read Write` grants itself broad authority. Project trust dialog accepts the broad grant. Users may not realize the grant is at skill-level, not per-invocation.

**Auditor != installer.** Enterprise deployments push skills to many users. The auditor is one role; the installer/runner is another. The audit needs to scale to the audience, and the audit results need to be communicated to runners.
