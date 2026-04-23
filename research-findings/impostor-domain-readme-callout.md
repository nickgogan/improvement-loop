---
name: "Impostor-Domain Callout at README Top"
summary: "High-popularity open-source projects attract impostor domains that distribute malware under the project's name. Lead the README with a CAUTION block naming the known impostor domains, declaring the official surfaces (GitHub, package registry, docs site), and cross-linking to the retraction/correction log for timeline. Security-aware README pattern that runs before any branding or install instructions."
implementation_notes: null
category: "Governance"
evidence_strength: "Weak (single-practitioner)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: retraction-log-as-governance-artifact.md
    rel: enables
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-23"
pipeline_status: raw
consumed_by: []
---

## What It Is

A README structural pattern that places a security warning about impostor domains *before* the project branding, badges, or install instructions. The warning block names the domains known to be impersonating the project and distributing malware, then declares the three official surfaces where the real project lives: the GitHub repository, the package registry (PyPI, npm, etc.), and the official docs site. A cross-link to a retraction/correction log (see [[retraction-log-as-governance-artifact]]) points to the timeline of how the impostor domains were identified.

MemPalace's exact structure:

```markdown
> [!CAUTION]
> **Scam alert.** The only official sources for MemPalace are this
> [GitHub repository](...), the [PyPI package](...), and the docs
> site at **[mempalaceofficial.com](...)**. Any other domain — including
> `mempalace.tech` — is an impostor and may distribute malware.
> Details and timeline: [docs/HISTORY.md](docs/HISTORY.md).

<div align="center">
<img src="assets/mempalace_logo.png">
# MemPalace
...
```

The CAUTION block comes before the logo.

## Why It Matters

Popular OSS projects with fast-growing star counts attract typo-squatting and impostor sites that capitalize on user confusion. When the README is the user's first stop (from a GitHub link, a tweet, a blog post), the impostor-domain information is load-bearing — it must land before the user leaves the README and types a domain into their browser. Placing it after the install instructions is too late.

For MetaSystem: low immediate priority because MetaSystem isn't a public-OSS target yet. Worth registering for the eventual day the Household OS, Claude Build, or any public-facing surface achieves enough adoption to attract impostors. The pattern is also a useful datapoint for the KB's security / agent-boundary dimension — it shows how public projects that also function as agent-distributable artifacts (pip-installable plugins, MCP servers) handle the multi-surface trust problem.

This is a `Weak (single-practitioner)` evidence-strength finding — one repo observed so far. If similar callouts show up in other high-star memory or agent projects, the priority bumps up.

## Why People Are Using It

Observed in [MemPalace](https://github.com/MemPalace/mempalace) 3.3.2 — see [[mempalace-analysis]] for structural details. MemPalace reached ~49k GitHub stars within three weeks of launch. Community issues (#267, #326, #506) reported fake websites distributing malware; the README CAUTION block and the `docs/HISTORY.md` 2026-04-11 entry are the response. The CAUTION block is in the repo-level README *and* in the PyPI package description.

## Potential Alternatives

- **`SECURITY.md` only.** Standard GitHub security file. Users don't read it before install.
- **Banner on the docs site.** Helps users who reach the real docs site but misses users who typed a wrong domain and never arrive.
- **Twitter / Discord announcements.** Ephemeral; new users arriving via search engines miss them.
- **Automated package-registry scanning.** PyPI/npm may remove typo-squats after the fact. Doesn't address domain-level impersonation.
- **Trademark enforcement.** Legal channel; slow and only applicable to named-trademark projects.

## Potential Improvements

- **Standardize the block format** (badge-style rendering; machine-readable metadata for tooling that could scan README CAUTION blocks).
- **Link to a signed statement.** The impostor-domain claim carries trust weight; a GPG-signed advisory that the CAUTION block links to reduces the "impostor README" recursion (impostors could publish a fake CAUTION block of their own).
- **Machine-scannable official-source manifest.** A `security.txt`-style file at a known location listing the official surfaces, signed. The README could then say "verify against `/.well-known/official-surfaces.sig`."

## Potential Failure Modes

- **Impostor README duplication.** Impostors can copy the real README including the CAUTION block, substituting their own domain as "official." The real project must be discoverable enough that users can cross-verify.
- **Claim ossification.** If the real project later adds a new official surface (e.g., a new docs mirror), the CAUTION block's enumeration becomes incorrect. Requires active maintenance.
- **Alert fatigue.** Every README carrying a CAUTION block dilutes the signal. The pattern only works when scam incidents are real and specific.
- **Missed visibility in package metadata.** GitHub renders the CAUTION block; PyPI, npm, and other registries may render differently or not at all. The warning needs to land in every distribution surface.
