---
name: Skill Cross-Surface Portability — Same Format, Different Constraints
summary: A skill folder works across Claude.ai, Claude Code, the Claude API, the Claude Agent SDK, and any standard-conformant client — but the runtime environment differs by surface. Claude.ai (per-user, varying network), Claude API (workspace-shared, no network, pre-installed packages only), Claude Code (filesystem-based custom only, full network, local installs). Custom skills do not sync across surfaces — separate upload per surface. The same skill behaves differently depending on where it runs.
implementation_notes: "Constraint matrix from the docs: Claude.ai — network access depends on user/admin settings; individual upload via Settings; not shared org-wide. Claude API — no network, no runtime package installs, only pre-installed packages, workspace-shared; requires three beta headers (code-execution-2025-08-25, skills-2025-10-02, files-api-2025-04-14). Claude Code — full network access (same as user's computer); local package installs preferred over global; filesystem-based (no API upload); shared via plugins or .claude/skills/ commit. Skills targeting one surface's capabilities may not work elsewhere — authors should test on target surfaces or use the compatibility frontmatter field to declare requirements."
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-agent-skills-overview-docs.md"
related_findings:
  - file: "skills-as-open-portable-standard.md"
    rel: "extends"
  - file: "skill-frontmatter-validation-rules.md"
    rel: "extends"
  - file: "claude-code-skill-frontmatter-extensions.md"
    rel: "same-problem"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skill Cross-Surface Portability — Same Format, Different Constraints

## What It Is

The SKILL.md format is portable; the runtime is not. A skill folder runs identically across Anthropic surfaces in terms of file shape, but the available capabilities differ:

| Surface | Network | Package Install | Sharing Model | Notes |
|---|---|---|---|---|
| Claude.ai | Varying (admin policy) | N/A (managed) | Per-user upload | Not centrally managed for orgs |
| Claude API | No network | Pre-installed only | Workspace-shared | Requires 3 beta headers; `code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14` |
| Claude Code | Full network | Local installs preferred | Filesystem-based, custom only | Shared via plugins or `.claude/skills/` |

Custom skills do NOT sync across surfaces. A skill uploaded to claude.ai is not available via the API. The same skill folder can be deployed to each surface, but each deployment is independent.

## Why It Matters

The portability promise of the Agent Skills standard is at the file-shape level. The runtime promise is per-surface. A skill that fetches `https://api.example.com/data` works on Claude Code, succeeds on claude.ai (depending on admin settings), and fails on the Claude API.

For skill authors, this is a non-trivial constraint:

- **Network-dependent skills** are not API-portable.
- **Runtime-package-installing skills** are not API-portable.
- **Filesystem-permission-dependent skills** behave differently across surfaces.

The `compatibility` field in skill frontmatter is the spec-level mechanism for declaring these requirements (e.g., `compatibility: Requires network access and git`). Without it, surface mismatches surface as runtime failures.

For consumers building skill libraries, the practical implication is to design for the most restricted target surface (typically the Claude API) and use the `compatibility` field to declare when a skill expects more.

## Why People Are Using It

The constraint matrix is documented across all canonical Anthropic skill sources. The beta-header requirement on the API is a hard gate. The Claude Code freedom (full network, local installs) is also documented; sample skills in `anthropics/skills` exercise it.

## Potential Alternatives

Surface-specific skills (one folder per surface — defeats the portability claim). Skill manifests that adapt to surface (skill detects environment and switches behavior — fragile and harder to audit). API-only design (lowest common denominator — restrictive). Claude Code-only design (rich but not portable).

## Potential Improvements

Per-surface conformance levels in the spec ("API-conformant" vs. "harness-conformant"). Standard environment detection so skills can adapt cleanly. Cross-surface skill testing tooling. Improved error messages when a skill fails because of surface mismatch.

## Potential Failure Modes

**Skill author tests on Claude Code, ships to API.** The fetch call works in dev, fails in production. The skill `compatibility:` field is the cure; testing on target surface is the prevention; neither is enforced.

**Beta-header drift.** The three required beta headers on the API can change. Skills baked against today's headers may need re-enablement against tomorrow's headers.

**Cross-surface sync drift.** A skill maintained on Claude Code and uploaded periodically to the API drifts between updates. There's no automatic sync.

**Workspace-shared API skills as governance surface.** API skills are workspace-shared, which means uploads affect all workspace members. The deployment authority is workspace-scoped — different from claude.ai's per-user model. Governance for "who can upload" lives outside the skill format.

**Runtime constraints invisible at install.** A skill installed on the API doesn't fail until run; users don't know they've installed something incompatible until they try to use it. Pre-flight surface compatibility checks would help; they don't exist.
