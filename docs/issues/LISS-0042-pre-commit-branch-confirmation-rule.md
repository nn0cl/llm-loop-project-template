# LISS-0042: Pre-commit branch confirmation rule

## Metadata

- Local issue ID: LISS-0042
- GitHub issue: none
- Status: done
- Phase: docs-only
- Type: process
- Priority: high
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: Design & Review group (Planner/Specifier) for design;
  Implementation group for the edit.
- Related branch: process/prevent-direct-to-main-commits

## Summary

- Add an explicit, checkable rule to
  `docs/collaboration/branch-commit-pr-discipline.md` requiring any session
  to confirm its current branch is not `main`/trunk before running any
  `git commit` — stated for every kind of record this repository's process
  produces, including Backlog-layer records such as
  `docs/backlog/item-NNNN-*.md`, not only "issue work" in the AT-TDD sense.
  Broaden `docs/collaboration/local-issue-planning.md`'s existing
  issue-work-only wording to cross-reference the new general rule so it no
  longer reads as excluding non-issue records.
- Root cause and incident: `docs/backlog/item-0013-prevent-direct-to-main-commits.md`
  — the Backlog thread committed `docs/backlog/item-0012-*.md` directly to
  `main` after a post-merge branch switch left the working tree on `main`;
  caught, reverted (`git revert`, commit `b6c8961`).

## Acceptance Notes

- `docs/collaboration/branch-commit-pr-discipline.md` states a
  "Pre-Commit Branch Confirmation" rule: before any commit, confirm the
  current branch is not `main`/trunk; if it is, create or switch to a
  dedicated branch first; states this applies to every record kind
  including Backlog-layer records, not only issue work; names the
  read-vs-commit distinction (checking out `main` to read post-merge state
  is fine; committing while still on it is the failure this rule targets).
- `docs/collaboration/local-issue-planning.md`'s "Dependency Rules" section
  no longer reads as scoping the direct-to-main prohibition to issue work
  only; it cross-references the new general rule in
  `branch-commit-pr-discipline.md` instead of restating or narrowing it.
- No change to CI, hooks, or any new deterministic tooling — item-0013's own
  "Known constraints" states the core ask is the written rule, not
  necessarily new tooling; a follow-up automated guard (e.g., a pre-commit
  hook) is recorded as a Deferred Question, not built here.
- `scripts/check-contract-consistency.py` passes unchanged (neither file is
  part of the `AGENTS.md`/`CLAUDE.md`/mirror text-identity set — confirmed
  by grep: no mirror file inlines either document's text, only links to
  it).
- AI work trace recorded under `docs/collaboration/traces/`, per ADR 0006 —
  both touched files are agent operating contract files
  (`docs/collaboration/*.md`), so a trace and separate-context Reviewer
  approval are required regardless of planning size.

## Review Finding Record

N/A — not a review-finding issue.

## Dependencies

- Parent: none
- Depends on: none
- Blocks: none
- Related: `docs/backlog/item-0013-prevent-direct-to-main-commits.md`,
  revert commit `b6c8961`

## Decisions Not Settled by the Design Agreement

- None — item-0013's promotion note settles scope and urgency; the only
  Design & Review judgment call is exactly where in
  `branch-commit-pr-discipline.md` the new rule lives and how
  `local-issue-planning.md` should reference it, both delegated explicitly
  by the item's "your call" wording.

## Context

- Included: `docs/backlog/item-0013-prevent-direct-to-main-commits.md`,
  `docs/collaboration/branch-commit-pr-discipline.md`,
  `docs/collaboration/local-issue-planning.md`,
  `docs/collaboration/prompt-instruction-change-control.md`, revert commit
  `b6c8961`.
- Omitted: item-0012 (document/log lifecycle management) — separate,
  unrelated backlog item, sequenced after this one per the Director's own
  instruction; not read for this issue's design beyond noting its
  existence.
- Assumptions: none beyond what the incident record and item-0013 state
  directly.

## AI Planning Records

Not required — planning size `S`, first attempt.

## References

- `docs/backlog/item-0013-prevent-direct-to-main-commits.md`
- `docs/collaboration/branch-commit-pr-discipline.md`
- `docs/collaboration/local-issue-planning.md`
- `docs/collaboration/prompt-instruction-change-control.md`
- Revert commit `b6c8961`

## Work Notes

- 2026-08-19 — Design & Review group (Planner/Specifier): local issue,
  work plan (`WP-0013`), and design agreement
  (`docs/collaboration/agreements/2026-08-19-prevent-direct-to-main-commits.md`,
  `DA-2026-08-19-01`) drafted on the shared branch
  `process/backlog-item-0012-and-0013`. Dispatched to the Implementation
  group on branch `process/prevent-direct-to-main-commits`.

## Verification

- `scripts/check-contract-consistency.py` — recorded in WP-0013's Preflight
  Validation section.
- Read-through diff confirming both edits are narrow, accurate, and do not
  duplicate or contradict existing wording.
- Work-plan-level Reviewer approval, separate context, per ADR 0006 (this
  is a contract-file change regardless of the `S` planning size).
