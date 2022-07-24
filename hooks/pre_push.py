"""
Git Hook that trigger on pre-push. It protect defined branch from push.
"""

import sys
import subprocess

PROTECTED_BRANCH = (
    "main",
    "dev"
)

def main():
    branch = str(subprocess.check_output(
        ["git", "symbolic-ref", "--short", "HEAD"]
    ).strip(), "utf-8").strip()

    if branch in PROTECTED_BRANCH:
        print(f"{branch} is a protected branch, create a PR to merge.")
        sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
