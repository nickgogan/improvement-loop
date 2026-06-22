#!/usr/bin/env python3
"""
Frontmatter YAML linter — validates that every markdown file's frontmatter block
parses as YAML. Prevents the session-127 defect class (unquoted prose containing
colons/quotes, soft-wrapped multi-line scalars, mixed-indent lists) from entering
git history at the source.

Authoring contract: see `_schema.yaml` → "Frontmatter authoring rules (YAML safety)".

Usage:
    python3 validate_frontmatter.py <file> [<file> ...]   # validate specific files
    python3 validate_frontmatter.py --all                 # scan the whole vault
    git diff --cached --name-only -- '*.md' | python3 validate_frontmatter.py  # stdin (pre-commit)

Exit code 0 = all valid; 1 = one or more parse failures.
"""
import re
import subprocess
import sys
from pathlib import Path

import yaml

from kb_parser import ROOT  # centralizes the vault-root path; gives kb_parser a consumer

# Files exempt from the frontmatter contract (per _schema.yaml header).
SKIP_NAMES = {"CLAUDE.md", "_index.md"}
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def validate_file(path):
    """Return an error string if the file's frontmatter is invalid, else None."""
    p = Path(path)
    if p.name in SKIP_NAMES or p.suffix == ".template" or p.name.endswith(".template.md"):
        return None
    try:
        text = p.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None  # staged deletion / moved file — nothing to validate
    except (OSError, UnicodeDecodeError) as e:
        return f"{path}: cannot read ({e})"
    if not text.startswith("---\n"):
        return None  # no frontmatter block — nothing to validate
    m = FM_RE.match(text)
    if not m:
        return f"{path}: opening '---' without a closing '---' delimiter"
    try:
        yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return f"{path}: frontmatter YAML parse error — {str(e).replace(chr(10), ' ')}"
    return None


def iter_all_md():
    """Yield git-tracked *.md files — the committed corpus this contract governs.
    Excludes gitignored paths (e.g. watched-libraries/_tmp/ repo-cache clones)."""
    out = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "*.md"],
        capture_output=True, text=True, check=True,
    ).stdout
    for rel in out.splitlines():
        if rel.strip():
            yield ROOT / rel.strip()


def main(argv):
    args = argv[1:]
    if args == ["--all"]:
        targets = list(iter_all_md())
    elif args:
        targets = args
    else:
        targets = [line.strip() for line in sys.stdin if line.strip()]

    errors = [e for e in (validate_file(t) for t in targets) if e]
    if errors:
        sys.stderr.write("Frontmatter YAML validation FAILED:\n")
        for e in errors:
            sys.stderr.write(f"  ✗ {e}\n")
        sys.stderr.write(
            f"\n{len(errors)} file(s) with invalid frontmatter. Fix prose fields with "
            "literal block scalars (|-) — see _schema.yaml 'Frontmatter authoring rules'.\n"
            "To commit anyway (not recommended): git commit --no-verify\n"
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
