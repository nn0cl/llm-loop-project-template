# Work Plan: Drift-Prevention Entry Documents and CI Checks (Scoped)

## Goal

- Close item-0012 facet 5's two most tractable deterministic checks (no
  retired terminology; no Archive document referenced from an Entry
  document), the Entry-document content requirement, and
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`, per
  `docs/backlog/item-0012-document-and-log-lifecycle-management.md` and
  `docs/collaboration/agreements/2026-08-19-drift-prevention-entry-docs-and-ci-checks.md`
  (`DA-2026-08-19-08`). The two harder checks facet 5 also names
  (single-canonical-per-theme, canonical-document-source-link) are
  explicitly deferred — see the design agreement's Deferred Questions.

## Scope

- In: `docs/collaboration/terminology-migration.md` (new),
  `scripts/check-contract-consistency.py` (two new check functions, a
  `RECORD_DIRS` entry, docstring update, `main()` registration),
  `docs/architecture/agent-quickstart.md` (new section),
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` (closed),
  the synthetic-case verification (created and removed within this work
  plan, not left in the tree), the required AI work trace, self-review,
  Preflight, work-plan-level Reviewer pass.
- Out: the single-canonical-per-theme and canonical-source-link checks
  (deferred); any `docs/archive/` content actually persisting after this
  work plan closes; `CLAUDE.md` or its four mirrors; facet 6
  (review-summary packets); the retroactive-application work plan.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0048 | ready | M | M | AIP-0048-001 | - | - | process/drift-prevention-entry-docs-and-ci-checks |

## Plan-Owned Bug Records

None.

## AI Planning Records

See LISS-0048's own AIP-0048-001 (required, planning size `M`).

## Recommended Order

1. LISS-0048 (single issue).

## Current Next Issue

- Issue: LISS-0048
- Reason it is unblocked: no dependencies; `DA-2026-08-19-08` covers it
  fully, including exact code for both new checks.
- Reopening request needed: no.

## Minor Fix Path

Does not apply — this adds new deterministic checks and new contract
content, not a correction to an existing defect (except incidentally
closing LISS-0044, which is itself folded into this work plan's own full
design-agreement cycle rather than run as a separate Minor Fix Path
correction, since it shares one cohesive branch/verification unit with
the rest of this issue).

## Preflight Validation

- Result: `pass`
- Checks and command output:

  ```console
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed
  ```

  Exit code: 0. First real-tree run (Implementer's own Task 4) correctly
  `fail`ed: the design agreement's own File 2 and File 3 contradicted
  each other — `check_no_archive_reference_from_entry`'s original bare
  substring match flagged File 3's own legitimate abstract mention of
  `docs/archive/`. `DA-2026-08-19-08` was amended with a corrected,
  file-shaped-path regex (`ENTRY_ARCHIVE_REFERENCE`), sent back to the
  same Implementation-group session, and re-applied (commit `d9fe2a2`).
  This run is against the merged result, independently re-verified in
  this worktree (fetched the Implementer's actual branch directly,
  diffed it against the corrected agreement text — matched exactly —
  before merging).
- Scope result: `git diff 3ae03d6..HEAD --stat` (`3ae03d6` is this work
  plan's own design-intake commit) shows exactly 7 files: this design
  agreement (the correction), the new terminology-migration table, the
  script edit, the agent-quickstart.md addition, the new trace file,
  LISS-0044 (closed), and LISS-0048's own Work Notes. `find docs/archive`
  confirms no `docs/archive/` path exists anywhere in the tree — the
  synthetic verification case was fully removed. No `CLAUDE.md`/mirror
  file touched. No open `Type: review-finding` issue affects this area.
- Next action: submit to the Design & Review group's work-plan-level
  Reviewer pass, in a context separate from both the Planner/Specifier
  context that wrote the design agreement and the Implementer context
  that transcribed and corrected it.

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: _pending_
- Result read: _pending — Director close is a separate, later action._
- Next direction: _pending_
- New design agreement (if any): _pending — the deferred checks and
  facet 6 each get their own design agreement when reached._

## Risks

- Medium (planning size `M`, new deterministic-check code — the class of
  change this repository's own review history shows is easiest to get
  subtly wrong, per `docs/collaboration/design-review-perspectives.md`'s
  precedent from the original `check-contract-consistency.py` review
  series). Mitigated by: exact code specified in the design agreement
  (Implementer transcribes, does not design), mandatory synthetic-case
  verification per check (not just a clean real-tree run), and a
  work-plan-level Reviewer pass that independently re-derives whether the
  new checks' own regexes/logic could produce a false positive or false
  negative, not only whether they currently pass.
