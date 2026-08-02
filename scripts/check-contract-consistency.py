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

What this cannot check, and who does
------------------------------------

Independent review found three holes in an earlier version of this script, each
a case where it passed a tree containing a defect it claimed to cover. Those are
fixed, and the checks that used to depend on a fixed set of separator words or a
literal banner prefix no longer do. Two limits remain, and they are structural
rather than bugs:

  * **Meaning.** Parity asks whether a rule is present, never whether it still
    says the same thing. A mirror that keeps the phrase `context separation`
    while inverting the rule underneath it passes here.
  * **Whether a reference points at the *intended* document.** The reference
    check resolves names; it cannot know that a sentence meant
    `docs/templates/review-record.md` and said
    `docs/templates/design-agreement.md`, when both exist.
  * **The adopter's starting ADR number.** The range check no longer reads
    phrasings, but the sentence telling an adopting project where to start
    their own numbering is still matched by phrase, so an unusual wording can
    evade it.
  * **Anything about a document this repository does not have.** In an adopting
    project the entry documents are the project's own, and checks over them are
    skipped there.

Each of these is a reading, not a comparison. They belong to the Reviewer
persona. Two rounds of independent review found holes in earlier versions of
this script — every one of them a place where it claimed a check it did not
have, rather than a place where a check was merely weak.

Treat a green run as "no mechanical drift found", never as "the contract is
consistent". The second claim is a judgment and nothing here makes it.

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
    "Project Boundaries": r"## Project Boundaries",
    "Current Non-Decisions": r"Non-Decisions",
}

# Sections deliberately not mirrored, each with the reason a reader can check.
# Empty on purpose: an earlier version exempted the two target-fill sections
# above on the ground that "each tool file carries its own", which review found
# to be false for three of four mirrors. The sections were added to the mirrors
# instead of the justification being reworded.
AGENTS_ONLY_SECTIONS: dict[str, str] = {}

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

# Document names that are examples of files a target project creates, not
# references to files this repository has. Each is named in an "e.g." list.
# Kept as an explicit list rather than a rule about "e.g." lines, so that a
# genuine dangling reference on such a line is still caught.
EXAMPLE_DOCUMENT_NAMES = {
    "backend-architecture.md",
    "frontend-architecture.md",
    "persistence.md",
    "rust-clean-architecture.md",
}

# Files this template has but does not distribute: an adopting project owns its
# own README and receives no CHANGELOG from us. Checks over them are skipped
# where they are absent, and naming one is never a dangling reference.
# Their existence inside this repository is asserted by CI's required_files
# list, not here: a checker that both defines what may be missing and decides
# whether something is missing has no independent signal.
TEMPLATE_ONLY_FILES = {
    "README.md",
    "README.ja.md",
    "QUICKSTART.md",
    "QUICKSTART.ja.md",
    "CHANGELOG.md",
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

    See TEMPLATE_ONLY_FILES: a target project owns its own entry documents, so
    checks over them are skipped there rather than failing.
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
    """Every relative path or filename a current document names must resolve."""
    basemap: dict[str, list[str]] = {}
    for dirpath, dirnames, filenames in os.walk(repo):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for name in filenames:
            rel_path = os.path.relpath(os.path.join(dirpath, name), repo)
            basemap.setdefault(name, []).append(rel_path)

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
                    if target.startswith(("http", "<", "~")):
                        continue
                    targets.append(target)
                for target in targets:
                    if not target or "*" in target or "$" in target or "<" in target:
                        continue
                    # Claude Code's import syntax names a file with a leading @.
                    target = target.lstrip("@")
                    if target in EXAMPLE_DOCUMENT_NAMES:
                        continue
                    # Exempt an entry document only where it genuinely does
                    # not exist — that is, in an adopting project. Inside this
                    # repository the file is present, so a reference to it
                    # resolves normally and its deletion is caught.
                    if target in TEMPLATE_ONLY_FILES and not os.path.exists(
                        os.path.join(repo, target)
                    ):
                        continue
                    if os.path.exists(os.path.join(repo, target)):
                        continue
                    sibling = os.path.normpath(
                        os.path.join(os.path.dirname(os.path.join(repo, rel)), target)
                    )
                    if os.path.exists(sibling):
                        continue
                    # A bare filename resolves against the repository root and
                    # the referencing file's own directory, both tried above,
                    # and then against a unique file of that name. An earlier
                    # version accepted any file anywhere with that name; a name
                    # two files answer to now fails, because the document
                    # should say which one it means.
                    if "/" not in target:
                        matches = basemap.get(target, [])
                        if len(matches) == 1:
                            continue
                        if len(matches) > 1:
                            failures.add(
                                "references",
                                f"{rel}:{lineno} names {target!r}, which "
                                f"{len(matches)} files answer to "
                                f"({', '.join(sorted(matches)[:3])}). Write the "
                                "path.",
                            )
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
    """Every ADR number an entry document names must be one that exists.

    This does not parse phrasings. Any four-digit ADR-shaped token on a line
    that mentions ADRs must name an ADR the repository has, or the number an
    adopting project starts at. Rewording the sentence does not evade it.
    """
    numbers = adr_numbers(repo)
    if not numbers:
        return
    last = numbers[-1]
    nxt = f"{int(last) + 1:04d}"
    valid = set(numbers) | {nxt}

    for rel in ("README.md", "QUICKSTART.md", "QUICKSTART.ja.md"):
        text = read_optional(repo, rel)
        if text is None:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if not re.search(r"\bADR|adr/", line, re.IGNORECASE):
                continue
            for token in re.findall(r"\b(0\d{3})\b", line):
                if token in valid:
                    continue
                failures.add(
                    "ADR range",
                    f"{rel}:{lineno} names ADR {token}, which the repository "
                    f"does not have. It has {numbers[0]}-{last}, and an "
                    f"adopting project starts at {nxt}.",
                )

            # Two ADR numbers joined by nothing but a dash or a bare range
            # word state a range, and its ends must be the set's ends. The
            # separator must carry no other words: "0006 and ADR 0013" cites
            # two ADRs and is left alone, while "0001 to 0011" and "0001-0013"
            # are ranges. This layer catches an understated range on a line
            # even when another line names the true last ADR.
            for a, between, b in re.findall(
                r"\b(0\d{3})\b([^0-9]{0,12}?)\b(0\d{3})\b", line
            ):
                if not re.fullmatch(
                    r"[\s\-–—〜~]*(?:to|through|まで)?[\s\-–—〜~]*",
                    between,
                    re.IGNORECASE,
                ):
                    continue
                if (a, b) != (numbers[0], last):
                    failures.add(
                        "ADR range",
                        f"{rel}:{lineno} states the range {a}-{b}; the "
                        f"repository has {numbers[0]}-{last}",
                    )

        # A document that describes the ADR set must name both of its ends.
        # This replaces an earlier rule that paired two numbers on one line and
        # called them a range: that produced a false failure when a sentence
        # cited two unrelated ADRs, and missed an understated range split
        # across two lines. Naming both ends is a property of the document, so
        # neither rewording nor line breaks evade it.
        if re.search(r"\bADR|adr/", text, re.IGNORECASE):
            doc_tokens = set(re.findall(r"\b(0\d{3})\b", text))
            for end in (numbers[0], last):
                if end not in doc_tokens:
                    failures.add(
                        "ADR range",
                        f"{rel} describes the ADR set without naming {end}. "
                        f"The set runs {numbers[0]}-{last}; a document that "
                        "states a range must state the current one.",
                    )

        # The number an adopter is told to start at must be last + 1. Unlike
        # the token check above, this one reads a phrasing, so it is evadable
        # by rewording. See "What this cannot check" in the module docstring.
        for stated in re.findall(
            r"(0\d{3})\s*(?:and up|onwards?|以降|から採番)", text
        ):
            if stated != nxt:
                failures.add(
                    "ADR range",
                    f"{rel} tells adopting projects to start at {stated}; the "
                    f"template occupies through {last}, so they must start at "
                    f"{nxt}",
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

    released = {v for v, _ in re.findall(r"^## (v[\d.]+)\s*—\s*(.*)$", changelog,
                                         re.MULTILINE)} & set(tags)

    # Any version a README names must be a version that exists as a tag. This
    # does not depend on the banner's wording: an untagged version cited
    # anywhere in a README is a claim nothing backs.
    for rel in ("README.md", "README.ja.md"):
        text = read_optional(repo, rel)
        if text is None:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            # No escape hatch. An earlier version skipped any line mentioning
            # "unreleased" or "CHANGELOG", which let a false release claim ride
            # on either word. A README that wants to discuss an unreleased
            # version links to the changelog instead of naming the version.
            for version in re.findall(r"\b(v\d+\.\d+\.\d+)\b", line):
                if version in tags:
                    continue
                failures.add(
                    "version claims",
                    f"{rel}:{lineno} names {version}, which has no git tag. "
                    "Tag it, or say on that line that it is unreleased.",
                )
        if released:
            newest = max(released, key=lambda v: [int(n) for n in v[1:].split(".")])
            for version in re.findall(r"\b(v\d+\.\d+\.\d+)\b", text):
                if version in tags and version != newest:
                    failures.add(
                        "version claims",
                        f"{rel} names {version}; the newest released changelog "
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
