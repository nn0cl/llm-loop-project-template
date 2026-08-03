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

Four rounds of independent review found holes in earlier versions of this
script, every one of them a case where it claimed a check it did not actually
have. Three of those holes were in code trying to infer what a sentence meant
from a fixed list of connective words or a literal prefix — "to", "through",
"-", "Contract edition:". Each list was evaded by an ordinary phrasing not on
it ("up to", "up through", a comma, a false banner with different words). That
pattern repeated three times before the connective-parsing approach was
abandoned rather than patched again: ADR-range detection is now exact-anchored
(see ENTRY_DOCUMENT_ADR_STATEMENTS) instead of parsed, which is sound but tied
to today's wording — see below.

What remains is structural, not a bug waiting for the next round:

  * **Meaning.** Parity asks whether a rule is present, never whether it still
    says the same thing. A mirror that keeps the phrase `context separation`
    while inverting the rule underneath it passes here.
  * **Whether a reference points at the *intended* document.** The reference
    check resolves names; it cannot know that a sentence meant
    `docs/templates/review-record.md` and said
    `docs/templates/design-agreement.md`, when both exist.
  * **An ADR-range statement not yet registered in
    ENTRY_DOCUMENT_ADR_STATEMENTS.** The check no longer parses prose for a
    range at all; it requires each *known* range-stating sentence, anchored by
    its surrounding text, to show the current bounds. A new range statement
    added to an entry document is invisible to this check until it is
    registered — which is the same fail-open gap as an unclassified
    `AGENTS.md` section would be if `check_parity_completeness` did not exist,
    except no equivalent completeness check exists for this one. A reworded
    *registered* sentence fails closed instead: the anchor stops matching and
    the check says so, rather than silently passing a wrong number.
  * **The adopter's starting ADR number** is covered by the same registered,
    anchored patterns as the range statements above — it has no separate
    mechanism and no separate gap. A statement of it that is not registered
    is invisible in the same way an unregistered range statement is.
  * **Anything about a document this repository does not have.** In an adopting
    project the entry documents are the project's own, and checks over them are
    skipped there.

Each of these is a reading, or a registration gap, not a comparison the script
makes. The first two belong to the Reviewer persona. The third is why this
list exists at all: read it before trusting a green run on a document that
states an ADR range this script does not already know about.

Treat a green run as "no mechanical drift found in what this script knows to
compare", never as "the contract is consistent". The second claim is a
judgment and nothing here makes it.

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
                    target = target.split("#")[0]
                    # Square-bracket-then-paren syntax is not unique to
                    # markdown links: a regex character class followed by a
                    # capture group parses the same way, and so does an
                    # ellipsis illustrating that fact in a comment — both of
                    # which this exact paragraph has, at different times,
                    # produced as a false positive against its own source.
                    # Accept only what a path or filename is actually made
                    # of — word characters, dot, slash, hyphen, tilde — and
                    # require at least one alphanumeric character, so a
                    # target of dots or slashes alone (an ellipsis, a bare
                    # separator) is not mistaken for one either. An earlier,
                    # narrower version required a slash or a recognized
                    # extension, which also rejected `LICENSE` — a real,
                    # extensionless, currently correct reference in this
                    # repository's own README — and left it silently
                    # unchecked.
                    if not re.fullmatch(r"[\w./~-]+", target) or not re.search(
                        r"[A-Za-z0-9]", target
                    ):
                        continue
                    targets.append(target)
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


# Exact-anchored ADR-range statements, one entry per sentence that currently
# states the process-ADR range or the number an adopting project starts at.
#
# Three rounds of independent review demonstrated that detecting "this prose
# states a range" from connective words is unbounded: every whitelist of
# separators ("-", "to", "through", "まで") was evaded by an ordinary English
# phrasing not on it ("up to", "up through", ", ", " / "). That is the same
# meaning-inference problem as mirror-parity content drift and reference
# intent, both already disclosed as outside what this script can do. Rather
# than add a fourth heuristic and wait for the fifth phrasing that breaks it,
# this check does not parse prose for a range at all.
#
# Instead, each pattern below is anchored to CURRENT, VERIFIED wording in the
# named file, with one digit group standing in for the bound that must equal
# `last` (the newest ADR) or `next` (where an adopting project starts). If a
# pattern stops matching — because the sentence was reworded, moved, or
# removed — the check fails closed and says so, rather than silently passing.
# Update the pattern here in the same change that reword the sentence; that
# coupling is deliberate, the same way parity completeness forces a new
# AGENTS.md section to be classified before it is silently ignored.
ENTRY_DOCUMENT_ADR_STATEMENTS: dict[str, list[tuple[str, str]]] = {
    "README.md": [
        (r"ADRs included here \(0001-(\d{4})\)", "last"),
        (r"own decisions from (\d{4}) up", "next"),
    ],
    "QUICKSTART.md": [
        (r"`docs/architecture/adr/0001-\*\.md` through `(\d{4})-\*\.md`", "last"),
        (r"keep any ADR your\s+project numbered afterward \((\d{4}) and up\)", "next"),
        (r'records" asserts ADRs 0001[–-](\d{4})', "last"),
    ],
    "QUICKSTART.ja.md": [
        (r"`docs/architecture/adr/0001-\*\.md` から `(\d{4})-\*\.md` までは", "last"),
        (r"ADR（(\d{4}) 以降）", "next"),
        (r"ADR 0001〜(\d{4}) を検査", "last"),
    ],
}


def check_adr_range(repo: str, failures: Failures) -> None:
    """Every ADR number an entry document names must be one that exists, and
    every registered range statement must show the current bounds.

    The per-token pass below is sound and general: any four-digit ADR-shaped
    token on a line that mentions ADRs must name an ADR the repository has, or
    the number an adopting project starts at. It catches a reference to an ADR
    that does not exist (`ADR 0099`) however the sentence is worded.

    It does not, by itself, catch a wrong *bound* stated for the current
    range, because the upper bound of an understated range ("...through
    0011") is itself a real ADR number and so passes the token test. That is
    covered by ENTRY_DOCUMENT_ADR_STATEMENTS instead — see its docstring for
    why that problem is solved by exact anchoring rather than parsing.
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

        for pattern, which in ENTRY_DOCUMENT_ADR_STATEMENTS.get(rel, []):
            match = re.search(pattern, text)
            if match is None:
                failures.add(
                    "ADR range",
                    f"{rel}: expected range statement not found "
                    f"(pattern: {pattern!r}). If the sentence was reworded or "
                    "moved, update ENTRY_DOCUMENT_ADR_STATEMENTS in "
                    "scripts/check-contract-consistency.py to match; if it was "
                    "removed, the current range is no longer stated anywhere "
                    "in this file.",
                )
                continue
            found = match.group(1)
            expected = last if which == "last" else nxt
            if found != expected:
                failures.add(
                    "ADR range",
                    f"{rel} states {found} where {expected} is expected "
                    f"(pattern: {pattern!r})",
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
                    "Tag it, or link to CHANGELOG.md instead of naming a "
                    "version this repository cannot show.",
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
