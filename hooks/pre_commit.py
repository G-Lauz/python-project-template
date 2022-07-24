"""
Git Hook that trigger on pre-commit. It run Pylint on all changed files within the
repository and execute the tests if the user is about to commit on the branch dev or
main.
"""

import io
import sys
import subprocess

import pytest

from pylint import lint
from pylint.reporters import text

PYLINT_TRESHOLD_RATING = 8

def main():
    # Get changed files
    diff = str(subprocess.check_output(
        ("git", "diff", "--cached", "--diff-filter", "ACMRTUXB", "--name-only")
    ), "utf-8").strip().split()
    changed_files = list(filter(lambda word: word.endswith(".py"), diff))

    # Run Pylint on changed files
    if changed_files:
        print("Running Pylint...")

        pylint_output = io.StringIO()
        reporter = text.TextReporter(pylint_output)

        result = lint.Run(changed_files, reporter=reporter, do_exit=False)
        rating = result.linter.stats.global_note

        print(pylint_output.getvalue())

        if rating < PYLINT_TRESHOLD_RATING:
            print(
                f"Pylint failed, you must have a rating over {PYLINT_TRESHOLD_RATING}"
            )
            sys.exit(1)

    # Run tests if commiting on main or dev branch
    branch = str(subprocess.check_output(
        ["git", "symbolic-ref", "--short", "HEAD"]
    ).strip(), "utf-8").strip()

    if branch in ("main", "dev"):
        print(f"About to commit on {branch}. Running tests first...")
        exit_code = pytest.main()
        sys.exit(exit_code != 0)


if __name__ == "__main__":
    main()
    sys.exit(0)
