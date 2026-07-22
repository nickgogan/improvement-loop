#!/usr/bin/env python3
"""Red/green fixture test for eval_runner sync mode (MV46 S3 DoD item).

Seeds a temp corpus + skills-dir fixture and asserts both directions:
  green — every corpus row covered by a case `source` or a waiver → exit 0
  red   — a seeded uncovered corpus row (drift) → exit 1 with a DRIFT line

Hermetic: never touches the live corpus, skills tree, or ledger. Run:
  .venv/bin/python .github/skills/meta-skill-eval/scripts/test_sync_drift.py
Exit 0 = both directions pass; 1 = test failure.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

RUNNER = Path(__file__).resolve().parent / "eval_runner.py"

CORPUS_GREEN = """# eval-candidates (fixture)

## fixture-skill

- "run the fixture thing" — triggered, correct (session deadbeef, 2026-07-20)
- "fixture me a widget" — triggered, correct (session cafe0001, 2026-07-20)
"""

# Same corpus plus one row no case or waiver covers → must drift.
CORPUS_RED = CORPUS_GREEN + """- "uncovered phrasing" — missed (session 0badf00d, 2026-07-20)
"""

EVAL_CASES = """skill: fixture-skill
version: 1
updated: 2026-07-20
class: objective
corpus_waivers: [cafe0001]  # fixture: deliberate waiver leg
cases:
  - id: t01
    tier: trigger
    query: "run the fixture thing"
    should_trigger: true
    source: "corpus deadbeef"
    note: fixture
"""


def run_sync(corpus: Path, skills_dir: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(RUNNER), "sync",
         "--corpus", str(corpus), "--skills-dir", str(skills_dir)],
        capture_output=True, text=True, timeout=30,
    )


def main() -> int:
    failures = []
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        skills_dir = tmp / "skills"
        evals = skills_dir / "fixture-skill" / "evals"
        evals.mkdir(parents=True)
        (evals / "eval-cases.yaml").write_text(EVAL_CASES)

        green_corpus = tmp / "corpus-green.md"
        green_corpus.write_text(CORPUS_GREEN)
        green = run_sync(green_corpus, skills_dir)
        if green.returncode != 0:
            failures.append(f"GREEN leg: expected exit 0, got {green.returncode}\n{green.stdout}{green.stderr}")

        red_corpus = tmp / "corpus-red.md"
        red_corpus.write_text(CORPUS_RED)
        red = run_sync(red_corpus, skills_dir)
        if red.returncode != 1:
            failures.append(f"RED leg: expected exit 1, got {red.returncode}\n{red.stdout}{red.stderr}")
        elif "DRIFT" not in red.stdout or "0badf00d" not in red.stdout:
            failures.append(f"RED leg: exit 1 but no DRIFT line naming 0badf00d\n{red.stdout}")

        # Empty-corpus leg (MV48 portability): a fresh host — new user/machine —
        # has no real-phrasing corpus yet; sync must pass cleanly, not error.
        empty = run_sync(tmp / "corpus-absent.md", skills_dir)
        if empty.returncode != 0:
            failures.append(f"EMPTY leg: expected exit 0 on absent corpus, got {empty.returncode}\n{empty.stdout}{empty.stderr}")
        elif "fresh host" not in empty.stdout:
            failures.append(f"EMPTY leg: exit 0 but no fresh-host notice\n{empty.stdout}")

    if failures:
        print("test_sync_drift: FAIL")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("test_sync_drift: PASS (green exit 0, red exit 1 with DRIFT row, absent corpus clean pass)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
