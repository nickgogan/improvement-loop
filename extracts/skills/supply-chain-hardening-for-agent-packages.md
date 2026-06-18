---
title: "Supply-Chain Hardening for Agent Packages"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "supply-chain-hardening-for-agent-packages"
extraction_date: "2026-05-24"
last_change_session: 92
last_change_sl: "session-92-codifier-identify-extract"
identification_report: "2026-05-24-identification-report.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Teams building CLI tools or agent harnesses that run with user-level OS permissions and execute commands or access secrets"
    - "Projects where a compromised transitive dependency could exfiltrate credentials, inject code, or alter agent behavior"
    - "Node.js packages distributed to end users where the full transitive dependency tree must be reproducible"
    - "Any npm-based project whose supply chain is a high-value attack target due to the permissions or trust level of the tool"
  platform_coupling: "specific:npm/Node.js"
  autonomy: "all"
  stage: "secure"
  reversibility: "medium — hardening settings can be removed from .npmrc and hooks can be disabled, but shrinkwrap removal exposes end users to tree variance; reverting exact pins requires range-policy decisions for each dep"
  auditability: "Fully auditable: .npmrc contents, package.json dependency versions, presence of npm-shrinkwrap.json, and pre-commit hook source are all committed to version control and inspectable in any code review. The verification script provides a machine-checkable compliance signal on every CI run."
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "The package is a Node.js/npm project distributed as a CLI or agent harness that runs with user-level permissions. A pre-commit hook runner (Husky or equivalent) is already installed or approved for installation. The team has write access to .npmrc, package.json, and the hooks directory."
  invariants: "All direct external dependencies remain at exact versions at all times. npm-shrinkwrap.json is regenerated and committed whenever package-lock.json changes. Lifecycle scripts are never silently enabled — every allowlist entry is documented with a rationale. The pre-commit lockfile guard remains active on the main branch."
  governance: "Owned by the team responsible for the agent CLI package. Modifications to the lifecycle-script allowlist require explicit review. Changes to .npmrc hardening settings require a documented rationale. The policy document in AGENTS.md is the authoritative source."
  recovery: "If a precondition is violated (e.g., hook runner absent), halt and install the hook runner before proceeding. If shrinkwrap drifts, regenerate immediately and open a priority PR. If an exact-pinned dependency has a critical CVE blocked by min-release-age, use the documented escape hatch, record the override, and re-enable the guard afterward."
tags:
  - "extracted-artifact"
  - "skill"
  - "security"
  - "supply-chain"
---

# Supply-Chain Hardening for Agent Packages

**Source:** [[supply-chain-hardening-for-agent-packages]]
**Form:** skill
**Extraction date:** 2026-05-24

## Inputs

- A Node.js/npm-based agent CLI package with a `package.json` and optionally an existing `package-lock.json`
- Write access to `.npmrc`, `.husky/pre-commit`, and `package.json` scripts
- An npm registry connection for shrinkwrap generation
- A list of any dependencies that require lifecycle scripts (may be empty)

## Outputs

- `.npmrc` updated with `save-exact=true` and `min-release-age=2`
- All direct external dependencies pinned to exact versions in `package.json`
- `npm-shrinkwrap.json` generated and committed alongside the package
- Pre-commit hook blocking unguarded `package-lock.json` changes
- `--ignore-scripts` set as the default install behavior; lifecycle-script allowlist documented
- `npm run check` script that validates pinned versions, TypeScript imports, and shrinkwrap freshness

## Steps

1. **Audit current dependencies.** Run `npm ls --depth=0` and identify all direct external dependencies. Flag any using semver ranges (`^`, `~`, `>=`, `*`).

2. **Pin exact versions.** In `package.json`, replace every range specifier on external direct dependencies with the exact version currently resolved. Internal workspace packages (`workspace:*`) may retain ranges.

3. **Configure `.npmrc`.** Add or set:
   - `save-exact=true` — ensures future `npm install <pkg>` calls record exact versions
   - `min-release-age=2` — blocks packages published within the last 2 days
   - `ignore-scripts=true` — disables lifecycle scripts by default

4. **Audit and allowlist lifecycle scripts.** Review every dependency that ships `preinstall`, `install`, or `postinstall` scripts. For each, judge whether the script is necessary and safe. Document approved scripts in a comment block in `.npmrc` or a `lifecycle-allowlist.md`. Run approved scripts manually or via a dedicated `npm run install-with-scripts` task.

5. **Generate shrinkwrap.** Run the shrinkwrap generation script or `npm shrinkwrap` directly. Commit the resulting `npm-shrinkwrap.json`. This locks the full transitive dependency tree for end users.

6. **Install pre-commit lockfile guard.** In `.husky/pre-commit` (or equivalent), add a check that fails the commit if `package-lock.json` is staged unless `PI_ALLOW_LOCKFILE_CHANGE=1` is set.

7. **Add verification script.** In `package.json` scripts, add `"check"` that: confirms all direct external deps have exact versions, validates shrinkwrap is present and not older than `package-lock.json`, and optionally validates TypeScript import correctness.

8. **Document the policy.** In `AGENTS.md` or equivalent, record: exact-pinning rationale, the `PI_ALLOW_LOCKFILE_CHANGE` escape hatch, lifecycle-script review requirement, and shrinkwrap regeneration obligation.

9. **Verify.** Run `npm run check`. Fix any reported violations before merging.

## Failure Modes

- **Maintenance burden from exact pinning.** Every dependency update requires a deliberate version bump. Mitigate with a scheduled dependency-update task (weekly sweep) so the burden is batched.

- **min-release-age delays security patches.** A critical vulnerability patch published today will be blocked for 2 days. Mitigate by monitoring advisories and using `.npmrc` override (`min-release-age=0`) as an escape hatch for emergency patches.

- **Shrinkwrap drift.** If a developer adds or updates a dependency without regenerating `npm-shrinkwrap.json`, end users receive an inconsistent tree. The `npm run check` script should detect this; CI must run `check` on every PR.

- **Lifecycle-script allowlist rot.** New versions of allowlisted packages may change their scripts without triggering re-review. Pin allowlisted packages to exact versions and document version scope in the allowlist.

- **Hook bypass.** Developers can set `PI_ALLOW_LOCKFILE_CHANGE=1` and forget to unset it, or use `--no-verify`. Make the escape hatch require a justification comment as a soft norm.

## Contract

### Preconditions
The package is a Node.js/npm project distributed as a CLI or agent harness running with user-level permissions. A pre-commit hook runner is installed or approved. The team has write access to `.npmrc`, `package.json`, and hooks directory.

### Invariants
All direct external dependencies remain at exact versions. Shrinkwrap is regenerated on every lockfile change. Lifecycle scripts are never silently enabled. The lockfile guard remains active on the main branch.

### Governance
Owned by the team responsible for the agent CLI package. Lifecycle-script allowlist changes require explicit review. `.npmrc` hardening changes require documented rationale.

### Recovery
If hook runner is absent: halt and install. If shrinkwrap drifts: regenerate immediately. If a CVE is blocked by min-release-age: use the escape hatch, record the override, re-enable afterward.
