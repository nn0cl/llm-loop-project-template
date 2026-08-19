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
  6. ID range collisions A live numbered document (LISS/WP/backlog item/ADR)
                        does not reuse a number that belonged to a
                        different, since-deleted document.
  7. Issue status sync  A LISS issue's own Status field agrees with its row
                        in the one work plan whose Issue Graph names it.
  8. Superseding phrases Every registered ADR-supersession anchor phrase is
                        still present in its target file.
  9. Open findings gate A closed work plan's own findings table lists no
                        review-finding issue whose Status is neither
                        `closed` nor `wont_do`, when loop-settings.toml
                        requires it.

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

Separately, the reference checker has been through three rounds of
self-referential false positives: its own regex literals and, once, a comment
illustrating one of them, parsed as targets and were reported as dangling
references to files that do not exist. `MD_LINK` and `CODE_PATH` now share one
filter, `_looks_like_a_path`, for exactly this reason — see its call sites for
the specific strings that triggered each round.

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
  * **Proximity is not the same sentence.** `EXTRA_MIRRORED_RULES` entries that
    use a `.{0,N}` proximity window between two terms (for example, "Reviewer"
    near "whole work plan") can be satisfied by two unrelated mentions that
    happen to sit within the window rather than a genuine connection between
    them. Review found a working construction of this on the first entry that
    used the pattern. Tightening the window only narrows the gap, the same way
    narrowing the ADR-range connective list did before that check was replaced
    outright — proximity matching is meaning-inference with extra steps, and
    belongs on this list rather than being chased through another round.

Each of these is a reading, or a registration gap, not a comparison the script
makes. The first two, and the proximity limit, belong to the Reviewer persona.
The ADR-range registration gap is why this list exists at all: read it before
trusting a green run on a document that states an ADR range this script does
not already know about.

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
import glob
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
    "Session Topology Across AI Coding Tools":
        r"0017-portable-three-layer-loop-and-file-based-intervention-fallback",
    "Loop Settings, Spikes, Backlog, and Findings":
        r"Loop Settings, Spikes, Backlog|loop-settings\.toml",
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
    # ADR 0014: self-review replaces per-phase separate-context review inside
    # a work plan; the Reviewer operates once, at the work plan's close.
    "Self-review (ADR 0014)": r"[Ss]elf-review",
    # Not just "whole work plan" alone: that phrase can appear with no
    # connection to review at all. Require "Reviewer" within the same
    # neighborhood as "whole ... work plan", or the compound phrase
    # "work-plan-level Reviewer" directly.
    "Work-plan-level Reviewer (ADR 0014)": r"work.plan.level Reviewer|"
        r"Reviewer.{0,80}whole (?:completed )?work plan|"
        r"whole (?:completed )?work plan.{0,80}Reviewer",
    "Work-plan close (ADR 0014)": r"[Ww]ork.[Pp]lan [Cc]lose",
    # ADR 0015. "Self-review (ADR 0014)" above is satisfied by ADR 0014's own
    # pre-existing content in every file, so it cannot detect these two
    # sentences being deleted — that gap is exactly what review found.
    # Anchor on text unique to ADR 0015's additions instead.
    "Self-review short-form default (ADR 0015)": r"self-review\.md.{0,20}short form",
    "Finding-response delta guidance (ADR 0015)": r"review finding on a\b",
    # Loop engineering ledger and audit extensions.
    "Loop settings file": r"loop-settings\.toml",
    "Init loop settings script": r"init-loop-settings\.sh",
    "Findings must be applied": r"Findings must be applied|findings-reuse\.md",
    "Post-hoc audit": r"post-hoc-audit\.md",
    "Spike ledger": r"docs/spike/",
    "Backlog ledger": r"docs/backlog/",
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

# Target-owned files created by bootstrap scripts (e.g. init-loop-settings.sh).
# Named throughout the contract so agents know the path; they may be absent
# until init runs. When present they resolve normally; when absent, naming
# them is not a dangling reference.
OPTIONAL_INIT_CREATED_FILES = {
    "docs/collaboration/loop-settings.toml",
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
    "docs/spike/",
    "docs/backlog/",
)

SCANNED_SUFFIXES = (".md", ".mdc", ".sh", ".yml", ".py")

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
CODE_PATH = re.compile(r"`([^`\s]+\.(?:md|mdc|sh|py|yml|yaml|toml|json))`")

# What a path or filename is actually made of — word characters, dot, slash,
# hyphen, tilde — with at least one alphanumeric character required, so a
# target of dots or slashes alone (an ellipsis, a bare separator) is not
# mistaken for one either. Shared by both matchers below rather than
# reimplemented per matcher, so neither can silently lose the property the
# other has.
def _looks_like_a_path(target: str) -> bool:
    return bool(re.fullmatch(r"[\w./~-]+", target)) and bool(
        re.search(r"[A-Za-z0-9]", target)
    )


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
                    # produced as a false positive against its own source. An
                    # earlier, narrower version of this filter required a
                    # slash or a recognized extension, which also rejected
                    # `LICENSE` — a real, extensionless, currently correct
                    # reference in this repository's own README — and left
                    # it silently unchecked. See `_looks_like_a_path`.
                    if not _looks_like_a_path(target):
                        continue
                    targets.append(target)
                for match in CODE_PATH.finditer(line):
                    target = match.group(1)
                    if target.startswith(("http", "<", "~")):
                        continue
                    # CODE_PATH's own regex already requires a recognized
                    # extension, which is why every current match happens to
                    # be a real path — but that has never been an explicit
                    # property of this branch, only an accident of what this
                    # script's source currently contains. Every self-inflicted
                    # false positive so far (regex literals matching as their
                    # own targets) was in a `\d{4}`-shaped backslash-and-brace
                    # fragment that happened to end in `.md`; a real path
                    # never contains those characters. Apply the same filter
                    # MD_LINK uses, so a future regex literal ending in a
                    # recognized extension does not reopen this path the way
                    # it repeatedly has for MD_LINK.
                    if not _looks_like_a_path(target):
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
                    if target in OPTIONAL_INIT_CREATED_FILES and not os.path.exists(
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


# Numbered-document prefixes tracked for reuse detection: directory -> a
# pattern whose group(1) is the file's full relative path and group(2) is
# its four-digit number. `docs/architecture/adr` reuses the same numbering
# space `adr_numbers()` already reads; the other three are the numbered
# planning-document families named in DA-2026-08-18-06.
NUMBERED_FILE_PATTERNS: dict[str, re.Pattern[str]] = {
    "docs/issues": re.compile(r"^(docs/issues/LISS-(\d{4})-[^/]+\.md)$"),
    "docs/work-plans": re.compile(r"^(docs/work-plans/WP-(\d{4})-[^/]+\.md)$"),
    "docs/backlog": re.compile(r"^(docs/backlog/item-(\d{4})-[^/]+\.md)$"),
    "docs/architecture/adr":
        re.compile(r"^(docs/architecture/adr/(\d{4})-[^/]+\.md)$"),
}

# This template's own pre-v1.0.0 history contains genuine, deliberate,
# already-fully-documented number reuse that predates this check: the ADR set
# was renumbered once during "process: consolidate the operating contract as
# the first edition (v1.0.0)" (commit cf9da58), and the local-issue/work-plan
# sequence was reset to a fresh start once during "chore: reset the
# repository's record artifacts to the initial state" (commit 9fcb2d2, itself
# an ancestor of cf9da58) — both single, Director-authorized, fully-recorded
# events, not organic drift. `git log --follow` correctly does not treat
# either as a rename, because it is not one: an unrelated document now
# occupies the freed number. Each currently-live path affected by one of
# those two historical events is listed here explicitly, once, so this check
# can tell a confirmed, already-explained past event apart from an
# unexplained new one. A path not on this list still fails the check exactly
# as designed; adding to this list is a deliberate registration, not a
# general-purpose escape hatch, and every entry must cite the commit that
# explains it in the same change that adds it.
KNOWN_HISTORICAL_ID_REUSE = {
    # cf9da58 "process: consolidate the operating contract as the first
    # edition (v1.0.0)" renumbered the ADR set in one commit.
    "docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md",
    "docs/architecture/adr/0002-design-first-ai-request-routing.md",
    "docs/architecture/adr/0003-input-output-reasoning-contracts.md",
    "docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md",
    "docs/architecture/adr/0013-preflight-validation-before-independent-review.md",
    # 9fcb2d2 "chore: reset the repository's record artifacts to the initial
    # state" removed this template's own bootstrap-era local issues and work
    # plans; the numbering sequence started over from LISS-0001/WP-0001 for
    # the template's real, post-reset local-issue history.
    "docs/issues/LISS-0001-review-issues-minor-fix-path.md",
    "docs/issues/LISS-0002-preflight-validation.md",
    "docs/issues/LISS-0003-code-path-filter-and-disclosure-history.md",
    "docs/work-plans/WP-0001-review-issues-minor-fix-path.md",
    "docs/work-plans/WP-0002-two-group-send-message-loop.md",
}


def _git_output(repo: str, args: list[str]) -> str | None:
    """Run a read-only git command against `repo`, following the same
    call-and-degrade pattern check_version_claims uses below: None means git
    is unavailable or the command failed, not "no results"."""
    try:
        result = subprocess.run(
            ["git", "-C", repo] + args,
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return result.stdout


def _historical_numbered_files(repo: str) -> dict[str, dict[str, set[str]]] | None:
    """Every path ever added under a tracked numbered-document prefix, on any
    branch, grouped by prefix and then by number. Returns None when git is
    unavailable (nothing to compare)."""
    output = _git_output(
        repo,
        ["log", "--all", "--diff-filter=A", "--name-only", "--pretty=format:"],
    )
    if output is None:
        return None
    history: dict[str, dict[str, set[str]]] = {
        prefix: {} for prefix in NUMBERED_FILE_PATTERNS
    }
    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        for prefix, pattern in NUMBERED_FILE_PATTERNS.items():
            match = pattern.match(line)
            if match:
                history[prefix].setdefault(match.group(2), set()).add(match.group(1))
    return history


def check_id_range_collisions(repo: str, failures: Failures) -> None:
    """A currently-live numbered document must not reuse a number that
    belonged to a different, since-deleted document.

    `git log --all --diff-filter=A --name-only` gives every path ever added,
    on any branch; comparing that against the live file set finds a number
    reused by a different filename. That alone is not enough to call it a
    collision: a file that was renamed keeps its old name in its own
    `git log --follow` history, and that is the same document's lineage, not
    two different documents sharing a number. Only a historical name the live
    file's own `--follow` history does not reach is a real collision.
    """
    history = _historical_numbered_files(repo)
    if history is None:
        return  # no git available; nothing to compare

    for prefix, pattern in NUMBERED_FILE_PATTERNS.items():
        dir_path = os.path.join(repo, prefix)
        if not os.path.isdir(dir_path):
            continue
        for name in sorted(os.listdir(dir_path)):
            rel = f"{prefix}/{name}"
            match = pattern.match(rel)
            if not match:
                continue
            number = match.group(2)
            historical_names = history.get(prefix, {}).get(number, set())
            other_names = historical_names - {rel}
            if not other_names:
                continue

            follow_output = _git_output(
                repo,
                ["log", "--follow", "--name-only", "--pretty=format:", "--", rel],
            )
            followed = {
                line.strip()
                for line in (follow_output or "").splitlines()
                if line.strip()
            }
            reused = sorted(other_names - followed)
            if reused and rel not in KNOWN_HISTORICAL_ID_REUSE:
                failures.add(
                    "id range collisions",
                    f"{rel} reuses number {number}, previously assigned to "
                    f"{', '.join(reused)} — a different, deleted file not "
                    "reached by `git log --follow` from the live path, so "
                    "not the same document's rename lineage",
                )


def check_issue_status_sync(repo: str, failures: Failures) -> None:
    """A LISS issue's own `Status:` field must agree with its row's Status
    column in the one work plan whose Issue Graph table names it.

    An issue that appears in zero work plans, or in more than one, is not
    this check's concern: zero means nothing to cross-reference yet, and more
    than one is ambiguous about which work plan is authoritative — guessing
    would risk a false positive of exactly the kind this script's docstring
    already disclaims. Only the unambiguous case (exactly one owning work
    plan) is checked, and only a genuine value disagreement is reported.
    """
    liss_status: dict[str, tuple[str, str]] = {}
    for path in sorted(glob.glob(os.path.join(repo, "docs/issues/LISS-*.md"))):
        name = os.path.basename(path)
        liss_match = re.match(r"^(LISS-\d{4})-", name)
        if not liss_match:
            continue
        text = read(repo, os.path.relpath(path, repo))
        status_match = re.search(r"^- Status: (.+)$", text, re.MULTILINE)
        if status_match is None:
            continue
        liss_status[liss_match.group(1)] = (status_match.group(1).strip(), name)

    wp_occurrences: dict[str, list[tuple[str, str]]] = {}
    for path in sorted(glob.glob(os.path.join(repo, "docs/work-plans/WP-*.md"))):
        wp_rel = os.path.relpath(path, repo)
        text = read(repo, wp_rel)
        section = re.search(
            r"^## Issue Graph\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL
        )
        if section is None:
            continue
        for row in re.finditer(
            r"^\| (LISS-\d{4}) \| ([^|]+) \|", section.group(1), re.MULTILINE
        ):
            liss_id, status = row.group(1), row.group(2).strip()
            wp_occurrences.setdefault(liss_id, []).append((wp_rel, status))

    for liss_id, (own_status, liss_name) in sorted(liss_status.items()):
        occurrences = wp_occurrences.get(liss_id, [])
        if len(occurrences) != 1:
            continue
        wp_rel, wp_status = occurrences[0]
        if wp_status != own_status:
            failures.add(
                "issue status sync",
                f"docs/issues/{liss_name} states Status: {own_status}, but "
                f"{wp_rel}'s Issue Graph lists {liss_id} as {wp_status!r}",
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


# Exact-anchored superseding-phrase requirements, modeled directly on
# ENTRY_DOCUMENT_ADR_STATEMENTS above: when an ADR supersedes another
# document's specific clause and that document is updated with a qualifying
# phrase to reflect it, the phrase is registered here, anchored to the
# CURRENT, VERIFIED wording. If a pattern stops matching, the check fails
# closed and says so, rather than silently passing a mirror that quietly
# reverted to the pre-supersession rule.
SUPERSEDING_PHRASE_REQUIREMENTS: dict[str, list[tuple[str, str]]] = {
    "docs/collaboration/design-agreement.md": [
        (
            r"Rule\s+3,\s+this\s+does\s+not\s+block\s+unrelated,\s+"
            r"concurrently\s+in-flight\s+work\s+plans\s+in\s+either\s+group",
            "ADR 0016",
        ),
    ],
    "docs/collaboration/ai-human-scheme.md": [
        (
            r"this\s+checkpoint,\s+for\s+one\s+work\s+plan,\s+does\s+not\s+"
            r"block\s+the\s+Design\s+&\s+Review\s+group's\s+or\s+the\s+"
            r"Implementation\s+group's\s+other\s+concurrently\s+in-flight\s+"
            r"work",
            "ADR 0016",
        ),
    ],
    "docs/at-tdd/process.md": [
        (
            r"Rule\s+3,\s+this\s+does\s+not\s+block\s+unrelated,\s+"
            r"concurrently\s+in-flight\s+work\s+plans\s+in\s+either\s+group",
            "ADR 0016",
        ),
    ],
}


def check_superseding_phrases(repo: str, failures: Failures) -> None:
    """Every registered superseding-phrase anchor must still be present in
    its target file. See SUPERSEDING_PHRASE_REQUIREMENTS above for what
    "registered" means and why this is presence-of-a-registered-string, not
    meaning-inference."""
    for target, requirements in SUPERSEDING_PHRASE_REQUIREMENTS.items():
        text = read_optional(repo, target)
        if text is None:
            continue
        for pattern, originating_adr in requirements:
            if re.search(pattern, text) is None:
                failures.add(
                    "superseding phrases",
                    f"{target}: expected qualifying phrase from "
                    f"{originating_adr} not found (pattern: {pattern!r}). If "
                    "the sentence was reworded or moved, update "
                    "SUPERSEDING_PHRASE_REQUIREMENTS in "
                    "scripts/check-contract-consistency.py to match; if it "
                    "was removed, the supersession is no longer stated "
                    "anywhere in this file.",
                )


def _block_work_plan_done_on_open_findings(repo: str) -> bool:
    """Read `[findings].block_work_plan_done_on_open_findings` from
    `docs/collaboration/loop-settings.toml`.

    The file is a flat `key = value` list under `[section]` headers (see the
    file itself), so a section-then-key regex is enough — no TOML library
    needed. Defaults to `True` when the file or the key is absent, matching
    this setting's own documented default (`docs/collaboration/loop-settings.md`
    and the toml file's own comment above the key both state `true` as the
    contract default)."""
    text = read_optional(repo, "docs/collaboration/loop-settings.toml")
    if text is None:
        return True
    section = re.search(r"^\[findings\]\n(.*?)(?=^\[|\Z)", text, re.MULTILINE | re.DOTALL)
    if section is None:
        return True
    match = re.search(
        r"^block_work_plan_done_on_open_findings\s*=\s*(true|false)\s*$",
        section.group(1),
        re.MULTILINE,
    )
    if match is None:
        return True
    return match.group(1) == "true"


def check_open_findings_gate(repo: str, failures: Failures) -> None:
    """A closed work plan's own findings table must list no `Type:
    review-finding` issue whose Status is neither `closed` nor `wont_do`,
    when `[findings].block_work_plan_done_on_open_findings` is true.

    "Closed" means the work plan's own "Work-Plan Close" section states a
    real, date-shaped `Date:` value, not the placeholder text every
    still-open work plan carries (`_pending Director action_`) — the same
    signal a human reader already uses, per DA-2026-08-19-03's Settled
    Ambiguities. A work plan with no "Work-Plan Close" section, or an
    unclosed one, is not this check's concern.

    Findings are read only from the work plan's own structured
    `| Issue | Status | Resolution |` table under "Work-Plan Review" — never
    inferred from a finding's own free-text content — the same
    anchor-on-existing-structure technique check_issue_status_sync already
    uses for the Issue Graph table.
    """
    if not _block_work_plan_done_on_open_findings(repo):
        return  # setting disabled; the gate does nothing

    for path in sorted(glob.glob(os.path.join(repo, "docs/work-plans/WP-*.md"))):
        wp_rel = os.path.relpath(path, repo)
        text = read(repo, wp_rel)

        close_section = re.search(
            r"^## Work-Plan Close\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL
        )
        if close_section is None:
            continue  # no Work-Plan Close section at all (older shape)
        date_match = re.search(r"^- Date: (.+)$", close_section.group(1), re.MULTILINE)
        if date_match is None:
            continue
        if not re.search(r"\d{4}-\d{2}-\d{2}", date_match.group(1)):
            continue  # placeholder text, e.g. "_pending Director action_"

        review_section = re.search(
            r"^## Work-Plan Review\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL
        )
        if review_section is None:
            continue

        for row in re.finditer(
            r"^\| (LISS-\d{4}) \|", review_section.group(1), re.MULTILINE
        ):
            liss_id = row.group(1)
            issue_paths = sorted(
                glob.glob(os.path.join(repo, f"docs/issues/{liss_id}-*.md"))
            )
            if not issue_paths:
                continue  # findings-table row names an issue that no longer exists
            issue_rel = os.path.relpath(issue_paths[0], repo)
            issue_text = read(repo, issue_rel)
            status_match = re.search(r"^- Status: (.+)$", issue_text, re.MULTILINE)
            if status_match is None:
                continue
            status = status_match.group(1).strip()
            if status not in ("closed", "wont_do"):
                failures.add(
                    "open findings gate",
                    f"{wp_rel} lists {liss_id} in its Work-Plan Review "
                    f"findings table, but {issue_rel} states Status: "
                    f"{status!r} — neither 'closed' nor 'wont_do'",
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
    check_id_range_collisions(repo, failures)
    check_issue_status_sync(repo, failures)
    check_superseding_phrases(repo, failures)
    check_open_findings_gate(repo, failures)
    return failures.report()


if __name__ == "__main__":
    sys.exit(main())
