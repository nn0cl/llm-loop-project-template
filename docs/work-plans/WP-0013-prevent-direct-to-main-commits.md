# Work Plan: Prevent Direct-to-Main Commits

## Goal

- Add an explicit, checkable pre-commit branch-confirmation rule so no
  session (Backlog, Design & Review, or Implementation) commits directly to
  `main`/trunk, stated for every record kind this repository's process
  produces — not only "issue work" — per
  `docs/backlog/item-0013-prevent-direct-to-main-commits.md` and
  `docs/collaboration/agreements/2026-08-19-prevent-direct-to-main-commits.md`
  (`DA-2026-08-19-05`).

## Scope

- In: one new "Pre-Commit Branch Confirmation" rule in
  `docs/collaboration/branch-commit-pr-discipline.md`; one cross-referencing
  broadening edit in `docs/collaboration/local-issue-planning.md`'s
  "Dependency Rules" section; the required AI work trace (both files are
  ADR-0006 contract files); self-review; Preflight; work-plan-level
  Reviewer pass.
- Out: any new deterministic tooling (git hook, CI check) — item-0013's own
  "Known constraints" states the core ask is the written rule; a follow-up
  automated guard is a Deferred Question, not built here. Any edit to
  `CLAUDE.md` or its four mirrors (neither touched file is part of that
  literal-mirror set — confirmed by grep before this plan was written).
  item-0012 (document/log lifecycle management) — separate work plan(s),
  sequenced after this one per the Director's own instruction.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0042 | done | S | S | - | - | - | process/prevent-direct-to-main-commits |

## Plan-Owned Bug Records

None.

## AI Planning Records

None required — planning size `S`, first attempt.

## Recommended Order

1. LISS-0042 (single issue).

## Current Next Issue

- Issue: LISS-0042
- Reason it is unblocked: no dependencies; `DA-2026-08-19-05` covers it
  fully, including exact placement.
- Reopening request needed: no.

## Minor Fix Path

Applies in substance: planning size `S`, single narrow addition plus one
cross-referencing broadening edit, preserves everything else, one attempt
expected, no specification/ADR/port/data-model/architecture-boundary
change. Both touched files ARE ADR-0006 contract files
(`docs/collaboration/*.md`), so — per `CLAUDE.md`'s own "Contract-file
changes are never self-reviewed, regardless of work-plan scope" — a trace
under `docs/collaboration/traces/` and separate-context Reviewer approval
are required regardless of the `S` size; this is not exempted by Minor Fix
Path applying in substance to everything else.

## Preflight Validation

- Result: `pass`
- Checks and command output:

  ```console
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed
  ```

  Exit code: 0. Run by the Design & Review group (not the Implementer's own
  context) after fast-forward-merging the Implementation group's branch
  `process/prevent-direct-to-main-commits` (commit `37581e1`) into the
  shared branch.
- Scope result: `git diff 632a8e4..HEAD --stat` (632a8e4 is the promotion
  commit both item-0012 and item-0013 share) shows exactly 6 files: this
  work plan, the design agreement, LISS-0042, the two edited contract
  files (`docs/collaboration/branch-commit-pr-discipline.md`,
  `docs/collaboration/local-issue-planning.md`), and the new trace file
  under `docs/collaboration/traces/`. No edit to `CLAUDE.md` or any
  mirror. No open `Type: review-finding` issue affects this area (checked
  all `docs/issues/LISS-*.md` `Status` fields; none `proposed` or
  `in_progress`). No open spike case blocks this issue.
- Next action: submit to the Design & Review group's work-plan-level
  Reviewer pass, in a context separate from both the Planner/Specifier
  context that wrote the design agreement and the Implementer context that
  made the edits.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-19-wp-0013-prevent-direct-to-main-commits-review.md`
— **Approved**, separate-context Reviewer session, all three constraints
(context separation, deterministic precondition, falsification burden)
satisfied; nine failure scenarios searched, none reproduced as a blocking
problem. One non-blocking observation recorded (a minor, non-contradictory
substance overlap between the two edited files' wording) — does not affect
this work plan's Done.

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
| none | N/A | Reviewer issued Approved with a non-blocking observation only; no `Type: review-finding` issue opened. |

## Work-Plan Close

- Date: 2026-08-19
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-19-wp-0013-prevent-direct-to-main-commits-review.md`,
  Approved — nine failure scenarios searched, one non-blocking wording
  observation) via the Backlog thread, which independently confirmed the
  fix, the review record, and a clean `scripts/check-contract-consistency.py`
  run from a detached checkout before presenting this close.
- Next direction: closed with "はい". Merged content sits on
  `process/backlog-item-0012-and-0013` (currently ahead of `main`, together
  with WP-0014's still-in-progress work — not itself an approval of that).
  Push/PR/merge-to-main remain separate explicit actions, deferred until
  WP-0014 or a suitable batch point.
- New design agreement (if any): none opened by this close.

## Risks

- Low. Documentation-only, single incident, clear root cause, narrow scope.
  The only real risk is over-broadening the new rule into something that
  reads as requiring separate-context review for Backlog-layer records
  themselves — explicitly out of scope per item-0013's own "Boundaries or
  non-goals" (this fix is about branch discipline, not approval
  requirements) and restated in the design agreement's Falsification
  Criteria.
