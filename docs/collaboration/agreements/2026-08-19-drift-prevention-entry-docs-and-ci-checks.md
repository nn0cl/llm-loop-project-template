# Design Agreement: Drift-Prevention Entry Documents and CI Checks (Scoped)

## Identity

- Agreement ID: DA-2026-08-19-08
- Date: 2026-08-19
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
(`Status: promoted`) facet 5 ("Prevent spec drift from stale documents"),
whose Promotion notes are this agreement's Director authorization under
ADR 0016 Rule 2: build the two most tractable of facet 5's five proposed
deterministic checks (no retired terminology; no Archive document
referenced from an Entry document — `check_issue_status_sync` already
exists and is not rebuilt), the Entry-document content facet 5 asks for,
and close `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`
(the WP-0014 Reviewer's own tracked finding, a natural fit here since both
concern `docs/archive/` handling). The remaining two proposed checks
(single-canonical-per-theme, canonical-document-source-link) are
explicitly deferred — see Deferred Questions — rather than designed under
time pressure within this same work plan.

## Scope

- In scope:
  - `docs/collaboration/terminology-migration.md` (new), exact content in
    "Exact Content to Produce" -> "File 1".
  - `scripts/check-contract-consistency.py`: four precise edits — (a) two
    new numbered items in the module docstring's check list, (b) one new
    entry in `RECORD_DIRS`, (c) two new function definitions, (d) two new
    calls in `main()`. All specified exactly in "File 2" below.
  - `docs/architecture/agent-quickstart.md`: one new section, "File 3"
    below.
  - `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`: closed,
    once the `RECORD_DIRS` fix is verified against a synthetic case (see
    Plan Task 5).
  - The required AI work trace (`terminology-migration.md` is an
    ADR-0006 contract file).
- Explicitly out of scope:
  - The single-canonical-per-theme and canonical-document-source-link
    checks (Deferred Questions).
  - Any `docs/archive/` content persisting in the tree after this work
    plan closes — the synthetic verification case is created and removed
    within the same work plan, never committed.
  - Any edit to `CLAUDE.md` or its four mirrors.
  - item-0012 facet 6 (review-summary packets) and the later
    retroactive-application work plan.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Create `docs/collaboration/terminology-migration.md` | Implementer | Architecture Path (content fully specified) | Matches "Exact Content to Produce" verbatim | read-through diff |
| 2 | Edit `scripts/check-contract-consistency.py` (four precise edits) | Implementer | Architecture Path (code fully specified; Implementer transcribes) | Matches "Exact Content to Produce" -> "File 2" verbatim at each of the four insertion points; no other line in the file changes | read-through diff |
| 3 | Add the "Document Currency and Canonical Reading" section to `agent-quickstart.md` | Implementer | Architecture Path | Matches "File 3" verbatim; no other part of the file changes | read-through diff |
| 4 | Real-tree verification | Implementer | Architecture Path | `python3 scripts/check-contract-consistency.py` passes cleanly against the actual repo tree (both new checks are no-ops today — empty terminology table, no Entry document references `docs/archive/`) | command output |
| 5 | Synthetic-case verification, then removal | Implementer | Architecture Path | Create a throwaway `docs/archive/issues/LISS-9999-synthetic-test.md` containing one outbound link to a real, currently-existing document (e.g. `docs/architecture/adr/0001-*.md`, by its actual filename) — confirm the checker does NOT flag it (RECORD_DIRS exemption working); separately, temporarily add a line in a scratch/throwaway file (not a real Entry document) containing `docs/archive/issues/LISS-9999-synthetic-test.md` as an inbound reference — confirm the checker DOES resolve it successfully (file exists); also temporarily add one made-up term to the terminology table and one matching current-document usage — confirm `check_retired_terminology` correctly flags it; then remove every synthetic artifact (the mock archive file, the scratch inbound-reference file, the temporary table row) before the final commit, leaving the working tree exactly as Task 1-3 left it plus verification evidence pasted into the self-review | actual command output pasted into LISS-0048's self-review, for both the positive (no false flag) and negative (correctly flags) cases per check |
| 6 | Close `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` | Implementer | Architecture Path | `Status: closed`, with a Work Notes entry citing the Task 5 verification evidence; original entries left in place per Invariant 2 | read-through diff |
| 7 | AI work trace | Implementer | Architecture Path | States which contract file changed (`terminology-migration.md`), why, what agent behavior changes; names the script and agent-quickstart.md edits too, for completeness | trace file present |
| 8 | Self-review | Implementer | Architecture Path | Short-form self-review per `docs/templates/self-review.md` (size `M`, short form is the ADR-0015 default; no escalation criteria apply — one cohesive branch, single attempt expected), recorded in LISS-0048 Work Notes, including both Task 4 and Task 5's actual pasted output | self-review record |
| 9 | Preflight Validation | Implementer / deterministic tool | Architecture Path | `pass` recorded with Task 4's real-tree output and an explicit scope check confirming no synthetic artifact remains | Preflight section in WP-0016 |
| 10 | Work-plan-level Reviewer pass | Reviewer (Design & Review group, separate context) | Architecture Path | Review record confirms mechanical accuracy, independently re-derives whether the two new checks could false-positive/false-negative on a case this design agreement did not anticipate, and confirms no synthetic artifact was left in the tree | review record under `docs/collaboration/reviews/` |

Sequencing: Tasks 1, 2, and 3 may proceed in any order. All three block
Task 4. Task 4 blocks 5. Task 5 blocks 6. Task 6 blocks 7. Task 7 blocks
8. Task 8 blocks 9. Task 9 blocks 10.

## Exact Content to Produce

### File 1: `docs/collaboration/terminology-migration.md` (new)

```markdown
# Terminology Migration Table

The old-to-new terminology this repository has actually retired, per
`docs/architecture/adr/0020-document-and-log-lifecycle-model.md`'s Entry
document requirements (item-0012 facet 5). Every session should be able to
tell, from this one table, whether a term it is about to write or read is
current or retired.

This table starts empty. A row is added only when a term is actually
retired by a real decision (an Accepted ADR, a design agreement, or an
equivalent recorded decision) — not backfilled speculatively for terms
that were never actually used, and not populated ahead of the later
retroactive-application work plan's own review of this repository's
existing history.

`scripts/check-contract-consistency.py`'s `check_retired_terminology`
check fails a build if a retired term below still appears in a current
document (anything outside `docs/collaboration/traces/`, `reviews/`,
`agreements/`, `docs/issues/`, `docs/work-plans/`, `docs/spike/`,
`docs/backlog/`, or `docs/archive/` — the same record/archive directories
ADR 0020 and this script already treat as historical). An empty table
(no rows) makes the check a no-op, not a failure.

## Table

| Retired term | Replacement | Retired by | Date |
| --- | --- | --- | --- |
| _(no entries yet)_ | | | |
```

### File 2: `scripts/check-contract-consistency.py` (four precise edits)

**Edit 2a — module docstring.** Insert these two new numbered items
immediately after item 9's paragraph (the "Open findings gate" item,
ending "...when loop-settings.toml requires it.") and before the blank
line preceding "What this cannot check, and who does":

```
  10. Retired terminology A term retired in
                        docs/collaboration/terminology-migration.md does
                        not still appear in a current document.
  11. Entry archive refs No Entry-layer document (ADR 0020 Rule 1)
                        references a docs/archive/ path directly.
```

**Edit 2b — `RECORD_DIRS`.** Add one new entry, as the last line before
the closing parenthesis, to the existing tuple (currently ending
`"docs/backlog/",`):

```python
RECORD_DIRS = (
    "docs/collaboration/traces/",
    "docs/collaboration/reviews/",
    "docs/collaboration/agreements/",
    "docs/issues/",
    "docs/work-plans/",
    "docs/spike/",
    "docs/backlog/",
    "docs/archive/",
)
```

(Only the last line, `"docs/archive/",`, is new — the rest is shown for
exact placement; do not otherwise alter this tuple.)

**Edit 2c — two new function definitions.** Insert both, in this order,
immediately after `check_version_claims`'s closing (its last statement is
the `for version in re.findall(...)` loop's `failures.add(...)` call) and
immediately before `def main() -> int:`:

```python
# Entry-layer documents, per ADR 0020 Rule 1 -- the fixed, small set every
# session reads first. Kept as an explicit list here (not derived from
# RECORD_DIRS or any other constant) because "Entry" is a document *role*,
# not a directory pattern, and this repository's actual Entry set is small
# enough to name directly rather than infer.
ENTRY_DOCUMENTS = (
    "docs/architecture/agent-quickstart.md",
    "CLAUDE.md",
    "AGENTS.md",
    ".github/copilot-instructions.md",
    "README.md",
    "README.ja.md",
)
ENTRY_DOCUMENT_GLOBS = (
    ".grok/rules/*.md",
    ".cursor/rules/*.mdc",
)


def check_no_archive_reference_from_entry(repo: str, failures: Failures) -> None:
    """No Entry-layer document (ADR 0020 Rule 1) may reference a
    `docs/archive/` path directly.

    Entry documents are the fixed, small set every session reads first;
    they describe current process, not history. If an Entry document ever
    needs to mention archived material, it should point at the restoration
    ledger (`docs/collaboration/restoration-ledger.md`) or a current
    Canonical document instead of the archived file directly -- ADR 0020's
    own Rule 1 states Archive content is "off the normal reading path."
    """
    entry_paths = list(ENTRY_DOCUMENTS)
    for pattern in ENTRY_DOCUMENT_GLOBS:
        entry_paths.extend(
            os.path.relpath(p, repo)
            for p in sorted(glob.glob(os.path.join(repo, pattern)))
        )

    for rel in entry_paths:
        text = read_optional(repo, rel)
        if text is None:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if "docs/archive/" in line:
                failures.add(
                    "entry archive reference",
                    f"{rel}:{lineno} references a docs/archive/ path -- "
                    "Entry documents should point at the restoration ledger "
                    "or a current Canonical document instead, per ADR 0020 "
                    "Rule 1.",
                )


# The canonical old-to-new terminology table. Starts empty; a row is added
# only when a term is actually retired by a real decision, not backfilled
# speculatively. See docs/collaboration/terminology-migration.md itself.
TERMINOLOGY_MIGRATION_TABLE = "docs/collaboration/terminology-migration.md"


def check_retired_terminology(repo: str, failures: Failures) -> None:
    """No retired term from `docs/collaboration/terminology-migration.md`
    may appear in a current document.

    "Current" means: not under one of the RECORD_DIRS (dated statements
    about the past, already exempt from present-tense consistency) and not
    the migration table itself (which names retired terms on purpose). An
    empty table (no rows yet) makes this check a no-op, not a failure --
    there is nothing to enforce until a real retirement is recorded there
    first.
    """
    table_text = read_optional(repo, TERMINOLOGY_MIGRATION_TABLE)
    if table_text is None:
        return
    retired_terms = [
        row.group(1)
        for row in re.finditer(
            r"^\| `([^`]+)` \| `[^`]+` \|", table_text, re.MULTILINE
        )
    ]
    if not retired_terms:
        return

    for rel in scanned_files(repo):
        if rel.startswith(RECORD_DIRS) or rel == TERMINOLOGY_MIGRATION_TABLE:
            continue
        text = read(repo, rel)
        for lineno, line in enumerate(text.splitlines(), 1):
            for term in retired_terms:
                if term in line:
                    failures.add(
                        "retired terminology",
                        f"{rel}:{lineno} uses retired term {term!r} -- see "
                        f"{TERMINOLOGY_MIGRATION_TABLE} for its replacement.",
                    )
```

**Edit 2d — `main()` registration.** Add two new calls immediately after
`check_open_findings_gate(repo, failures)` and before
`return failures.report()`:

```python
    check_open_findings_gate(repo, failures)
    check_no_archive_reference_from_entry(repo, failures)
    check_retired_terminology(repo, failures)
    return failures.report()
```

(Only the two new lines are new; shown with their existing neighbors for
exact placement.)

### File 3: `docs/architecture/agent-quickstart.md` — new section

Insert this new section immediately after the existing "## Session Entry"
section (after its numbered list ends, item 6 "No 'coordinator' persona
exists...") and before "For session-entry checklists and resume
examples, see...":

```markdown
## Document Currency and Canonical Reading

Before treating any document as authoritative:

- **Current vs. historical.** `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
  defines the status vocabulary (`draft | active | canonical | superseded |
  archived`) and the Entry/Canonical/Evidence/Archive layers. A document's
  own type-specific status field (an ADR's Status section, a local issue's
  `Status:`, a work plan's Work-Plan-Close state) is the source of truth
  for whether it is current.
- **Canonical documents.** The current source for a rule is: an Accepted,
  not-fully-superseded ADR (`docs/architecture/adr/`); a
  `docs/collaboration/*.md` or `docs/templates/*.md` contract/policy file;
  or a current `docs/specs/` file. `CLAUDE.md`'s own "Reading Sequence and
  Operating Path" section lists the documents a session actually reads, in
  order — read that, not this bullet, for the literal reading sequence.
- **Terminology.** `docs/collaboration/terminology-migration.md` is the
  canonical old-to-new terminology table. Check it before using an
  unfamiliar or possibly-outdated term; `scripts/check-contract-consistency.py`'s
  `check_retired_terminology` enforces it deterministically once a term is
  actually retired there.
- **Never enter from an old ADR directly.** An ADR is a decision record,
  not a standing instruction manual — read its own Status section first
  (superseded clauses are named there, per ADR 0016's own convention) and
  prefer the current `docs/collaboration/*.md` contract file or a later
  Accepted ADR for what to actually do today. Once ADR 0020's archive
  mechanism has moved a document under `docs/archive/`, treat it the same
  way: consult `docs/collaboration/restoration-ledger.md` for why it moved
  and what replaced it, rather than reading the archived copy as current.
```

## Specifications

- None. Documentation/process-governance change plus deterministic
  tooling (two new CI check functions); no application specification.

## Boundaries

- `docs/collaboration/terminology-migration.md` is an ADR-0006 contract
  file — trace and separate-context Reviewer approval are mandatory.
  `scripts/check-contract-consistency.py` and
  `docs/architecture/agent-quickstart.md` are not independently
  ADR-0006 contract files, but are reviewed for correctness in the same
  pass regardless.
- No `docs/archive/` content persists after this work plan closes — the
  synthetic verification case (Plan Task 5) is created and removed within
  the same work plan.
- No edit to `CLAUDE.md` or its four mirrors.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` (in the
  Director-facing sense) until the Director's own work-plan-close action.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Should this work plan attempt all five of facet 5's proposed checks? | No — only the two that can be built and verified now without a prerequisite design decision (retired terminology, Entry-archive-reference). `check_issue_status_sync` already exists (item-0009/WP-0007), confirmed by direct reading, not rebuilt. The remaining two (single-canonical-per-theme, canonical-source-link) need a "theme" registry concept this repository does not have — see Deferred Questions. | Design & Review group (Planner) |
| Should LISS-0044 be folded into this work plan? | Yes — both concern `docs/archive/` handling in the same script; fixing them together avoids two separate branches touching the same `RECORD_DIRS` constant, and LISS-0044's own Acceptance Notes ask for exactly the kind of synthetic-case verification this work plan already needs to build for its own new checks. | Design & Review group (Planner) |
| How is the synthetic verification case kept from becoming real `docs/archive/` content this work plan wasn't authorized to create? | Created, exercised, and removed within Plan Task 5, before the final commit — verified by the Preflight scope check (no `docs/archive/` path present in the final tree) and independently re-confirmed by the Reviewer. | Design & Review group (Planner) |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should facet 5's remaining two checks (single-canonical-per-theme; every Canonical document carries a source/evidence link) be built now or later? | Deferred — both need a "theme" registry concept (which documents belong to the same theme, so "more than one current per theme" is checkable) this repository does not have today. Building one under time pressure inside this work plan risks the same kind of premature-mechanism mistake ADR 0020's own spike (case-0001) explicitly avoided for the four-layer model itself. Settle this when a future session designs the theme registry — plausibly alongside the retroactive-application work plan, which will need to catalog themes anyway as it consolidates historical documents. |

## Verification

- `python3 scripts/check-contract-consistency.py` — clean run against the
  real repo tree (Plan Task 4).
- Per-check synthetic-case verification, both positive (no false flag) and
  negative (correctly flags a constructed bad case) — Plan Task 5, actual
  output pasted into the self-review.
- Read-through diff confirming all changes match "Exact Content to
  Produce" verbatim, and that no synthetic artifact remains in the final
  tree.
- Work-plan-level Reviewer approval, separate context — including an
  independent attempt to find a false-positive/false-negative case this
  design agreement did not anticipate.

## Falsification Criteria

- Any `docs/archive/` path exists in the repository tree after this work
  plan's final commit.
- `check_retired_terminology` or `check_no_archive_reference_from_entry`
  is registered in `main()` but not demonstrated, with actual pasted
  output, against a constructed failing case.
- `CLAUDE.md` or a mirror file is edited.
- No AI work trace is recorded for this contract-file-touching work plan.
- LISS-0044 is left open, or closed without citing the actual verification
  evidence.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
