# LISS-0035: Catch document-consistency drift deterministically

## Metadata

- Local issue ID: LISS-0035
- GitHub issue: none
- Status: review
- Phase: phase-0-design (tooling extension, no application code)
- Type: tooling-enhancement
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/document-consistency-drift-checks

## Summary

- Make `.github/workflows/ci.yml`'s "Check architecture decision records"
  step dynamic (glob `docs/architecture/adr/*.md` instead of a hardcoded
  `for n in 0001 ... 0016` list), eliminating the recurring manual-bump
  problem at its source.
- Add `check_id_range_collisions` to `scripts/check-contract-consistency.py`:
  compares currently-live numbered files (`LISS-*`, `WP-*`, `item-*`,
  ADR `NNNN-*`) against every number ever assigned per `git log --all
  --diff-filter=A --name-only`, flagging a live file whose number was
  previously used by a different, deleted file.
- Add `check_issue_status_sync`: cross-references each
  `docs/issues/LISS-*.md`'s `Status:` field against its row's status
  column in the work plan(s) whose Issue Graph table names that issue ID.
- Add a `SUPERSEDING_PHRASE_REQUIREMENTS` registration table and
  `check_superseding_phrases` function, modeled exactly on
  `ENTRY_DOCUMENT_ADR_STATEMENTS`/`check_adr_range`, registering ADR 0016's
  three known real supersession instances
  (`docs/collaboration/design-agreement.md`,
  `docs/collaboration/ai-human-scheme.md`, `docs/at-tdd/process.md`).
- Update the script's module docstring to list the new checks alongside
  the existing five.

## Acceptance Notes

- CI step reproduced locally passes against the current ADR set with no
  hardcoded numbers remaining.
- `check_id_range_collisions`: passes clean on current `HEAD`; a
  constructed synthetic collision (e.g. a temp copy with a duplicate
  historical number reintroduced) produces a clear failure message, with
  actual command output pasted in Work Notes.
- `check_issue_status_sync`: same pattern — clean pass on `HEAD`, clear
  failure on a constructed mismatch.
- `check_superseding_phrases`: clean pass on `HEAD` with the three
  registered instances (confirm their exact current anchor wording by
  reading each file first, do not guess it); a constructed removal of one
  registered anchor produces a clear failure, not a silent pass.
- Module docstring's numbered check list updated to match the actual set
  of checks after this change.
- Full `python3 scripts/check-contract-consistency.py` passes.
- Self-review recorded (full form — planning size `M`, four distinct
  additions).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0009-document-consistency-drift-on-completion.md
- Depends on: none
- Blocks: none
- Related: `task_76618661` (superseded by Task 1 of this issue — the
  Design & Review group dismisses it once this issue's CI fix is verified,
  per `DA-2026-08-18-06`'s Deferred Questions), `task_cdbaa1ce` (pattern 5,
  explicitly out of scope here)

## Decisions Not Settled by the Design Agreement

- None identified at design time.

## Context

- Included: `docs/backlog/item-0009-*.md`,
  `scripts/check-contract-consistency.py` (whole file — it is short enough
  to read in full and the new functions must match its existing style),
  `.github/workflows/ci.yml` (the one step only), `DA-2026-08-18-06`.
- Omitted: application-level specs (none apply); pattern 5's own fix
  (tracked elsewhere).
- Assumptions: `docs/architecture/adr/0016-*.md`'s three cited files
  (`design-agreement.md`, `ai-human-scheme.md`, `docs/at-tdd/process.md`)
  still contain the qualifying phrase WP-0002/LISS-0027 added — verify by
  reading each before writing the anchor pattern, per the acceptance notes
  above; if any has since changed, that is a reopening-worthy finding, not
  a silent adjustment.

## AI Planning Records

### AIP-0035-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Sonnet 5 via Claude Code, Design & Review
    group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: not surfaced in this environment
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Implementation-group agent, Architecture Path,
  one CI-file edit plus three new functions and a docstring update in one
  script
- Compatibility state: Verified — confirmed via full read of
  `scripts/check-contract-consistency.py` that the anchored-registration
  pattern (`ENTRY_DOCUMENT_ADR_STATEMENTS`/`check_adr_range`) is a real,
  reusable template for the superseding-phrase mechanism, not an assumption
- Intended scope: `.github/workflows/ci.yml` (one step),
  `scripts/check-contract-consistency.py` (three new functions, one
  registration table, docstring update)
- Estimated token range: 10,000-20,000 tokens
- Estimated token midpoint: 15,000
- Token metric: approximate output tokens, including synthetic-test
  construction and verification output
- Estimation basis: three new, moderately complex Python functions plus
  synthetic verification for each, larger than WP-0004/0005's single-file
  changes but smaller than a full new subsystem
- Assumptions: single execution attempt
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/collaboration/agreements/2026-08-18-document-consistency-drift-checks.md`
  (`DA-2026-08-18-06`)
- `scripts/check-contract-consistency.py` (existing `check_adr_range`/
  `ENTRY_DOCUMENT_ADR_STATEMENTS` as the direct structural precedent)

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0009-*.md`'s promotion, after a full read of
  `scripts/check-contract-consistency.py`'s actual structure (not assumed
  from the backlog item's own framing — found the real ADR-range gap is in
  a separate CI file, not the script itself). Dispatched to the
  Implementation group.
- 2026-08-18 (Implementation group, Implementer): all four tasks executed
  on branch `process/document-consistency-drift-checks`. Self-review below
  (full form, planning size `M`, per `docs/templates/self-review.md` and
  `docs/architecture/adr/0015-review-cost-discipline.md`).

### Self-Review (full form, planning size M)

**Phase**: Architecture Path, single-attempt execution of DA-2026-08-18-06's
Plan (Tasks 1-5; this record covers Task 6).

**Commands run** (see "Deterministic Verification Output" below for full
pasted output of each):

1. `bash` reproduction of the updated CI step's logic against the real
   `docs/architecture/adr/` directory.
2. `python3 scripts/check-contract-consistency.py` (full run) against `HEAD`.
3. Each of the three new check functions run in isolation against `HEAD`
   (via a small harness that imports the module and calls the function
   directly with the same `repo` value `--repo` would produce), and against
   constructed synthetic repositories/fixtures.

**Judgment calls made** (as DA-2026-08-18-06 anticipated and explicitly
delegated):

1. **Task 2 — rename vs. genuine collision.** Implemented exactly as
   specified: `git log --follow --name-only` on the live file's own path
   decides whether a historical name sharing its number is the same
   document's own rename lineage (not a collision) or a different,
   deleted document (a real collision). Verified this distinguishes the
   two cases correctly with a synthetic repo containing both a real
   collision (LISS-0001 "alpha" deleted, LISS-0001 "beta" — different
   content — added later) and a genuine rename (LISS-0002 "gamma",
   `git mv`'d to a new filename, same number) — see Deterministic
   Verification Output. **Escalation beyond the literal task text**: running
   the check as specified against this repository's actual `HEAD` produced
   10 real (by `--follow`'s own logic) but not-actually-drift findings, all
   traced to two specific, single, Director-authorized historical events
   already fully documented in their own commit messages: `cf9da58`
   ("process: consolidate the operating contract as the first edition
   (v1.0.0)") renumbered the ADR set in one commit, and `9fcb2d2` ("chore:
   reset the repository's record artifacts to the initial state") reset the
   local-issue/work-plan sequence to a fresh start — `9fcb2d2` is itself an
   ancestor of `cf9da58`. Neither is a `--follow`-visible rename because
   neither actually is one: an unrelated document occupies the freed number
   by design. Rather than (a) let the check fail on every run against this
   repository's own history forever, breaking the "passes clean on `HEAD`"
   acceptance criterion, or (b) weaken the check with a commit-hash history
   boundary (rejected: a hardcoded commit hash would make the check error
   on `git log ^<hash>` in any adopting project's fork, where that commit
   does not exist), I added `KNOWN_HISTORICAL_ID_REUSE`, an explicit,
   exact, per-file registry of the ten specific already-explained reuses,
   each commented with the commit that explains it — the same idiom this
   script already uses for `REFERENCE_ALLOWLIST` and
   `EXAMPLE_DOCUMENT_NAMES`: a literal list of specific paths, not a
   meaning-inference heuristic, and inert (never matches) in any repository
   that does not have these specific historical files. I judge this
   consistent with the Falsification Criteria's "no new meaning-inference
   heuristic" boundary because nothing here infers what any text means; it
   registers specific, already-fully-documented historical facts by exact
   path, the same as every other allowlist in this script.
2. **Task 3 — ambiguous work-plan membership.** Chose to skip silently
   (not report informational) when a LISS ID appears in zero or more than
   one work plan's Issue Graph table. Reasoning: zero occurrences means
   there is nothing to cross-reference yet (not a defect); more than one
   occurrence is genuinely ambiguous about which work plan is authoritative,
   and guessing risks exactly the false-positive class this script's own
   docstring already disclaims. Verified with a synthetic fixture containing
   all three cases side by side (a real single-work-plan mismatch, a
   matching single-work-plan case, and a two-work-plan ambiguous case with
   different statuses in each) — only the genuine mismatch was reported.
3. **Task 4 — anchor phrases.** Read each of the three target files
   directly (not assumed from memory) and found the ADR-0016-Rule-3
   qualifying phrase most directly tied to the "work-plan close does not
   block other concurrently in-flight work" statement in each — exact
   wording below under "Anchor phrases found and used." `design-agreement.md`
   and `at-tdd/process.md` carry the identical sentence; `ai-human-scheme.md`
   states the same qualification with different wording (its own sentence
   structure), so its registered pattern is different from the other two's,
   not a shared literal string.

**Anchor phrases found and used** (Task 4):

- `docs/collaboration/design-agreement.md`: "Rule 3, this does not block
  unrelated, concurrently in-flight work plans in either group" (the
  sentence wraps across a line break in the source; the registered pattern
  uses `\s+` in place of literal spaces so line-wrapping does not break the
  match).
- `docs/at-tdd/process.md`: the identical sentence, "Rule 3, this does not
  block unrelated, concurrently in-flight work plans in either group",
  same `\s+`-tolerant pattern.
- `docs/collaboration/ai-human-scheme.md`: "this checkpoint, for one work
  plan, does not block the Design & Review group's or the Implementation
  group's other concurrently in-flight work" — a differently-worded
  statement of the same ADR 0016 Rule 3 qualification.

**Risks considered and why each does not occur**:

- A new check crashes on a repository with no `.git` (git unavailable):
  `check_id_range_collisions` returns early when `_git_output` returns
  `None`; verified against a directory with no `.git` at all — no crash,
  reports clean.
- A new check crashes on a work plan file with no "## Issue Graph" heading:
  `check_issue_status_sync`'s section regex returns `None` for such a file
  and the loop `continue`s past it. Confirmed no work-plan file in this
  repository is missing that heading (`grep -L` found none), so the branch
  is currently untested against a real file, but the code path is a plain
  early-`continue`, not a computation that could raise.
- A registered superseding-phrase target file is absent (adopting-project
  case): `check_superseding_phrases` uses `read_optional`, matching
  `check_adr_range`'s own handling of `TEMPLATE_ONLY_FILES` — an established,
  already-exercised pattern in this script, not new risk.
- The `KNOWN_HISTORICAL_ID_REUSE` allowlist silently hides a *future*, real
  collision by coincidentally reusing one of the ten registered paths: not
  possible, because the registry is keyed on the *live file's own full
  path*, not a bare number — a new file introducing a genuine collision
  would need the exact same path string as one of these ten specific,
  already-existing, currently-live files to be suppressed, which would mean
  it is not a new file at all.
- `check_issue_status_sync` false-flags on a WP row for an ID that isn't
  actually in the "Issue Graph" table (e.g. a mention inside prose, or in
  the separate "Work-Plan Review" findings table that shares the
  `| Issue | Status | ... |` header shape): the section regex scopes
  extraction strictly to text between the `## Issue Graph` heading and the
  next `## ` heading, so the "Work-Plan Review" table (a different section)
  is never read by this check. Confirmed structurally by inspecting every
  current `docs/work-plans/WP-*.md` file's heading order.

## Verification

### Task 1 — CI ADR-existence step (bash reproduction against the real directory)

```text
$ bash scripts... (reproduced step, see .github/workflows/ci.yml diff)
PASS: contiguous ADR sequence 0001-0016, 16 files
```

### Task 2 — `check_id_range_collisions`

Clean pass on `HEAD`:

```text
$ python3 -c "...import module, run check_id_range_collisions(repo, Failures())..."
contract consistency: all checks passed
```

Synthetic repo (`git init` in a scratch temp dir): LISS-0001 "alpha" added,
deleted, then LISS-0001 "beta" (different content) added at the same
number — a real collision; LISS-0002 "gamma" added then `git mv`'d to a new
filename, same number — a genuine rename, not a collision:

```text
id range collisions:
  docs/issues/LISS-0001-beta-issue.md reuses number 0001, previously assigned to docs/issues/LISS-0001-alpha-issue.md — a different, deleted file not reached by `git log --follow` from the live path, so not the same document's rename lineage

contract consistency: 1 failure(s)
```

(LISS-0002's rename correctly produced no failure — confirmed by its
absence from the output above, and independently by
`git log --follow --name-only` on the renamed path reaching the old name.)

### Task 3 — `check_issue_status_sync`

Clean pass on `HEAD`:

```text
contract consistency: all checks passed
```

Synthetic fixture (temp dir, no git needed — this check does not use git):
LISS-0099 states `Status: done`, its one owning work plan's Issue Graph
lists it as `ready` (real mismatch); LISS-0100 states `Status: ready`,
matching its one owning work plan exactly (no report); LISS-0101 appears in
two work plans with different statuses (`resolved` and `in_progress`) —
ambiguous, skipped:

```text
issue status sync:
  docs/issues/LISS-0099-example-issue.md states Status: done, but docs/work-plans/WP-0099-example-plan.md's Issue Graph lists LISS-0099 as 'ready'

contract consistency: 1 failure(s)
```

### Task 4 — `check_superseding_phrases`

Clean pass on `HEAD` with all three registered instances:

```text
contract consistency: all checks passed
```

Synthetic failure (scratch copy of the three target files in a temp
directory, real working tree never touched): removed the registered
sentence from the scratch copy of `docs/collaboration/design-agreement.md`:

```text
superseding phrases:
  docs/collaboration/design-agreement.md: expected qualifying phrase from ADR 0016 not found (pattern: 'Rule\s+3,\s+this\s+does\s+not\s+block\s+unrelated,\s+concurrently\s+in-flight\s+work\s+plans\s+in\s+either\s+group'). If the sentence was reworded or moved, update SUPERSEDING_PHRASE_REQUIREMENTS in scripts/check-contract-consistency.py to match; if it was removed, the supersession is no longer stated anywhere in this file.

contract consistency: 1 failure(s)
```

`git status --short` and `git diff` on the real working tree, taken after
this synthetic test, confirmed no changes to
`docs/collaboration/design-agreement.md`, `docs/collaboration/ai-human-scheme.md`,
or `docs/at-tdd/process.md` — the removal was made only in a temp scratch
copy, never in the tracked working tree.

### Full script run

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

Recorded in full in `docs/work-plans/WP-0007-document-consistency-drift-checks.md`'s
Preflight Validation section.
