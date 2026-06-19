---
log_entry: "DD-47 through DD-51 created: Workspace Filesystem Architecture restructure (5 DDs)"
actor: "Nick + Agent: Claude"
area: null
change_type: "Design Decision"
milestone: "M3"
rationale: "Perplexity research synthesized Nx monorepo patterns, OMG meta-model theory, Claude Code best practices, and agentic platform architecture into a workspace restructure proposal. After iterative review, 5 new DDs were created to formalize the three-peer model (meta-system, systems, incubator), governance database promotion to root, incubator lifecycle, skill placement strategy, s1-schema as read-only mirror, and single repository policy."
source_dd: null
target_system: "Cross-System"
timestamp: "2026-04-04T00:00:00.000Z"
---

# DD-47 through DD-51 created: Workspace Filesystem Architecture restructure

## Change Summary
5 Design Decisions created based on Perplexity research synthesis, defining the target filesystem architecture for MetaSystem.

## Affected Items

| DD | Title | Target System | Scope |
|----|-------|---------------|-------|
| DD-47 | Workspace Filesystem Architecture (Three-Peer Model + PARA mapping) | Cross-System | Structure |
| DD-48 | Incubator and Promotion Lifecycle | Cross-System | Flow |
| DD-49 | Skill Placement Strategy (lean root) | S3: Claude Code Build | Structure |
| DD-50 | s1-schema as Read-Only Notion Mirror | Cross-System | Principle |
| DD-51 | Single Repository | Cross-System | Principle |

## DD-38 Amendment
DD-38 amended to include filesystem container mapping for the four architecture sections per DD-47.

## Research Sources
- Nx monorepo folder structure patterns
- OMG meta-model theory (M2 defines M1 through reference, not containment)
- Claude Code CLAUDE.md hierarchy best practices (Anthropic docs)
- Agentic platform architecture patterns (HuggingFace, Anthropic Trends Report)

## Key Design Choices Made During Review
1. Semantic directory names (incubator, systems, meta-system) over literal PARA names
2. Governance databases promoted to root (not behind a governance/ directory)
3. Improvement Loop stays as root-level peer (not nested in meta-system) to respect DD-38
4. Workspace root keeps "MetaSystem" name (workspace IS the meta-system)
5. PARA mapping documented in CLAUDE.md, not encoded in directory names
