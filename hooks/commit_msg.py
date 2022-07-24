"""
Git Hook that trigger on commit-msg. It force the user to link the commit with a JIRA
issue.
"""

import sys
import re


def main():
    issue_key_regex = "[A-Z]{2,}-\\d+"

    commit_msg = None
    with open(sys.argv[1], "r", encoding="utf8") as commit_file:
        commit_msg = commit_file.read().strip()

    if re.search(issue_key_regex, commit_msg) is None:
        print("A JIRA issue must be linked with the commit.")
        sys.exit(1)

    print("Commit message is validated.")


if __name__ == "__main__":
    main()
    sys.exit(0)
