# Work Plan: Prevent Direct-to-Main Commits

## Goal

- Add an explicit, checkable pre-commit branch-confirmation rule so no
  session (Backlog, Design & Review, or Implementation) commits directly to
  `main`/trunk, stated for every record kind this repository's process
  produces — not only "issue work" — per
  `docs/backlog/item-0013-prevent-direct-to-main-commits.md` and
  `docs/collaboration/agreements/2026-08-19-prevent-direct-to-main-commits.md`
  (`DA-2026-08-19-01`).

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
- Reason it is unblocked: no dependencies; `DA-2026-08-19-01` covers it
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

- Result: _pending — recorded after Implementation group completes LISS-0042_
- Checks and command output: _pending_
- Scope result: _pending_
- Next action: _pending_

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: _pending_
- Result read: _pending — Director close is a separate, later action; this
  work plan stops at Reviewer approval and reports readiness._
- Next direction: _pending_
- New design agreement (if any): _pending_

## Risks

- Low. Documentation-only, single incident, clear root cause, narrow scope.
  The only real risk is over-broadening the new rule into something that
  reads as requiring separate-context review for Backlog-layer records
  themselves — explicitly out of scope per item-0013's own "Boundaries or
  non-goals" (this fix is about branch discipline, not approval
  requirements) and restated in the design agreement's Falsification
  Criteria.
