#!/usr/bin/env python3
"""Deterministic consistency checks for the agent operating contract.

Every failure this script reports has occurred at least once in review. The
defects share a shape: nothing is broken, no link is dead, CI is green — two
documents simply stopped agreeing, and only a side-by-side reading revealed it.
This makes that reading a command.

Checks:

  1. Mirror parity      Every rule AGENTS.md states reaches each tool that
                        needs its own copy of it.
  2. Parity completeness Every AGENTS.md section is classified as mirrored or
                        deliberately not, so a new section cannot be added
                        without deciding which it is.
  3. References         Every relative path a document names resolves.
  4. ADR range          Every stated process-ADR range matches the ADR files.
  5. Version claims     No document claims a released version that has no tag.

Usage:
  scripts/check-contract-consistency.py [--repo PATH]

Exits non-zero on the first category with failures, after reporting all of
them. Stdlib only, so it runs anywhere python3 does.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

# --------------------------------------------------------------------------
# Configuration. Edit these when the contract gains a rule or a tool.
# --------------------------------------------------------------------------

# Files that must carry a full copy of the contract's effective content.
# `.cursor/rules/*` is deliberately absent: ADR 0006 records that Cursor loads
# root AGENTS.md natively, so the Cursor set carries complements only.
FULL_MIRRORS = {
    "CLAUDE.md": ["CLAUDE.md"],
    "copilot": [".github/copilot-instructions.md"],
    # A rule set is satisfied by the union of its files.
    "grok": [
        ".grok/rules/01-quickstart.md",
        ".grok/rules/02-architecture-boundaries.md",
        ".grok/rules/03-collaboration-and-completion.md",
    ],
}

# AGENTS.md sections that must be reflected in every full mirror, each with a
# pattern that identifies the rule wherever a mirror chose different headings.
MIRRORED_SECTIONS = {
    "Prime Directive": r"No execution without a recorded design agreement",
    "The Three Invariants": r"[Ee]very decision produces a document",
    "Personas": r"personas\.md",
    "Expected Workflow": r"agent-quickstart\.md",
    "Session Entry": r"no prior chat context|session-start-and-resume",
    "Phase Discipline": r"Phase 1|Phase Gate|Phase Discipline",
    "Reopening the Design Agreement": r"[Rr]eopening",
    "Clean Architecture Dependency Rule": r"Domain|dependency rule|Dependency Rule",
    "External Resources Must Be Ports": r"[Pp]orts",
    "Design Intake": r"DESIGN CHECK",
    "Approval Model": r"[Cc]ontext separation",
    "Source Code Quality": r"cognitive load|source-code-quality",
    "Completion": r"definition-of-done",
}

# Sections that are intentionally not mirrored, with the reason.
AGENTS_ONLY_SECTIONS = {
    "Project Boundaries": "target-fill placeholder; each tool file carries its own",
    "Current Non-Decisions": "target-fill placeholder; each tool file carries its own",
}

# Rules that live outside AGENTS.md's section headings but still must reach
# every full mirror. Add a row when a new cross-cutting rule is introduced.
EXTRA_MIRRORED_RULES = {
    "Minor Fix Path": r"Minor Fix Path",
    "Preflight Validation": r"Preflight",
    "Review record location": r"docs/collaboration/reviews/",
    "Design agreement location": r"docs/collaboration/agreements/",
    "External resource adoption contract":
        r"external-resource-adoption-contract\.md",
    "AI failure recovery": r"ai-failure-recovery\.md",
    "Runner CLI contract": r"runner-cli-contract\.md",
}

# Reference targets that legitimately do not resolve in this repository.
REFERENCE_ALLOWLIST = {
    # Example contract files meant to be placed inside a target project, where
    # their relative paths resolve.
    "docs/templates/examples/rust-agent-instructions.md",
    "docs/templates/examples/frontend-agent-instructions.md",
}

# Directories holding records rather than contract. Their contents are dated
# statements about the past and are not held to present-tense consistency.
RECORD_DIRS = (
    "docs/collaboration/traces/",
    "docs/collaboration/reviews/",
    "docs/collaboration/agreements/",
    "docs/issues/",
    "docs/work-plans/",
)

SCANNED_SUFFIXES = (".md", ".mdc", ".sh", ".yml", ".py")

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
CODE_PATH = re.compile(r"`([^`\s]+\.(?:md|mdc|sh|py|yml|yaml|toml|json))`")


class Failures:
    def __init__(self) -> None:
        self.items: list[tuple[str, str]] = []

    def add(self, category: str, message: str) -> None:
        self.items.append((category, message))

    def report(self) -> int:
        if not self.items:
            print("contract consistency: all checks passed")
            return 0
        current = None
        for category, message in self.items:
            if category != current:
                print(f"\n{category}:", file=sys.stderr)
                current = category
            print(f"  {message}", file=sys.stderr)
        print(
            f"\ncontract consistency: {len(self.items)} failure(s)",
            file=sys.stderr,
        )
        return 1


def read(repo: str, rel: str) -> str:
    with open(os.path.join(repo, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def read_optional(repo: str, rel: str) -> str | None:
    """Read a file that exists in the template but not in every adopting project.

    `README.md`, the QUICKSTART pair, and `CHANGELOG.md` are not distributed —
    a target project owns its own. Checks over them are skipped there rather
    than failing.
    """
    if not os.path.exists(os.path.join(repo, rel)):
        return None
    return read(repo, rel)


def scanned_files(repo: str) -> list[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(repo):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in filenames:
            if name.endswith(SCANNED_SUFFIXES):
                out.append(os.path.relpath(os.path.join(dirpath, name), repo))
    return sorted(out)


def check_mirror_parity(repo: str, failures: Failures) -> None:
    """Every rule AGENTS.md states must reach each full mirror."""
    rules = dict(MIRRORED_SECTIONS)
    rules.update(EXTRA_MIRRORED_RULES)

    for mirror_name, files in FULL_MIRRORS.items():
        text = "\n".join(read(repo, f) for f in files)
        for rule, pattern in sorted(rules.items()):
            if not re.search(pattern, text):
                failures.add(
                    "mirror parity",
                    f"{mirror_name} does not state {rule!r} "
                    f"(no match for /{pattern}/)",
                )


def check_parity_completeness(repo: str, failures: Failures) -> None:
    """No AGENTS.md section may go unclassified."""
    headings = re.findall(r"^## (.+)$", read(repo, "AGENTS.md"), re.MULTILINE)
    known = set(MIRRORED_SECTIONS) | set(AGENTS_ONLY_SECTIONS)
    for heading in headings:
        if heading.strip() not in known:
            failures.add(
                "parity completeness",
                f"AGENTS.md section {heading.strip()!r} is not classified. "
                "Add it to MIRRORED_SECTIONS with a pattern, or to "
                "AGENTS_ONLY_SECTIONS with a reason.",
            )
    for heading in sorted(known):
        if heading not in [h.strip() for h in headings]:
            failures.add(
                "parity completeness",
                f"{heading!r} is classified but is no longer a section of "
                "AGENTS.md. Remove the stale entry.",
            )


def check_references(repo: str, failures: Failures) -> None:
    """Every relative path a current document names must resolve."""
    for rel in scanned_files(repo):
        if rel.startswith(RECORD_DIRS) or rel in REFERENCE_ALLOWLIST:
            continue
        with open(os.path.join(repo, rel), encoding="utf-8", errors="replace") as fh:
            for lineno, line in enumerate(fh, 1):
                targets = []
                for match in MD_LINK.finditer(line):
                    target = match.group(1)
                    if target.startswith(("http://", "https://", "#", "mailto:")):
                        continue
                    targets.append(target.split("#")[0])
                for match in CODE_PATH.finditer(line):
                    target = match.group(1)
                    if "/" not in target or target.startswith(("http", "<", "~")):
                        continue
                    targets.append(target)
                for target in targets:
                    if not target or "*" in target or "$" in target or "<" in target:
                        continue
                    if os.path.exists(os.path.join(repo, target)):
                        continue
                    sibling = os.path.normpath(
                        os.path.join(os.path.dirname(os.path.join(repo, rel)), target)
                    )
                    if os.path.exists(sibling):
                        continue
                    failures.add(
                        "references",
                        f"{rel}:{lineno} names {target!r}, which does not exist",
                    )


def adr_numbers(repo: str) -> list[str]:
    adr_dir = os.path.join(repo, "docs/architecture/adr")
    if not os.path.isdir(adr_dir):
        return []
    return sorted(
        name[:4] for name in os.listdir(adr_dir) if re.match(r"^\d{4}-.*\.md$", name)
    )


def check_adr_range(repo: str, failures: Failures) -> None:
    """Stated process-ADR ranges must match the ADR files that exist."""
    numbers = adr_numbers(repo)
    if not numbers:
        return
    first, last = numbers[0], numbers[-1]
    nxt = f"{int(last) + 1:04d}"

    for rel in ("README.md", "QUICKSTART.md", "QUICKSTART.ja.md"):
        text = read_optional(repo, rel)
        if text is None:
            continue
        for stated_first, stated_last in re.findall(
            r"(\d{4})\s*(?:-|–|〜|through|から)\s*\*?\.?m?d?\*?`?\s*(\d{4})", text
        ):
            if (stated_first, stated_last) != (first, last):
                failures.add(
                    "ADR range",
                    f"{rel} states ADRs {stated_first}-{stated_last}; the "
                    f"repository has {first}-{last}",
                )
        for stated_next in re.findall(r"(\d{4})\s*(?:and up|以降)", text):
            if stated_next != nxt:
                failures.add(
                    "ADR range",
                    f"{rel} tells adopting projects to start at "
                    f"{stated_next}; the template occupies through {last}, so "
                    f"they must start at {nxt}",
                )


def check_version_claims(repo: str, failures: Failures) -> None:
    """No document may claim a released version that has no tag."""
    try:
        tags = subprocess.run(
            ["git", "-C", repo, "tag", "-l"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.split()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return  # no git available; nothing to contradict

    changelog = read_optional(repo, "CHANGELOG.md")
    if changelog is None:
        return
    for version, heading_tail in re.findall(
        r"^## (v[\d.]+)\s*—\s*(.*)$", changelog, re.MULTILINE
    ):
        if version in tags:
            continue
        if "unreleased" not in heading_tail.lower():
            failures.add(
                "version claims",
                f"CHANGELOG.md heading {version!r} has no matching git tag. "
                "Mark the section unreleased, or tag it.",
            )

    released = [v for v, _ in re.findall(r"^## (v[\d.]+)\s*—\s*(.*)$", changelog,
                                         re.MULTILINE)
                if v in tags]
    if released:
        newest = released[0]
        for rel in ("README.md", "README.ja.md"):
            text = read_optional(repo, rel)
            if text is None:
                continue
            banners = [b.rstrip(".") for b in re.findall(
                r"(?:Contract edition|契約バージョン):\s*(v[\d.]+)", text)]
            for banner in banners:
                if banner != newest:
                    failures.add(
                        "version claims",
                        f"{rel} banners {banner}; the newest tagged changelog "
                        f"entry is {newest}",
                    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="repository root")
    args = parser.parse_args()
    repo = os.path.abspath(args.repo)

    failures = Failures()
    check_mirror_parity(repo, failures)
    check_parity_completeness(repo, failures)
    check_references(repo, failures)
    check_adr_range(repo, failures)
    check_version_claims(repo, failures)
    return failures.report()


if __name__ == "__main__":
    sys.exit(main())
