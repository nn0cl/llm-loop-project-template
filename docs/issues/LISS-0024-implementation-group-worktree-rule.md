# LISS-0024: Add per-work-plan worktree/branch rule for the Implementation group

## Metadata

- Local issue ID: LISS-0024
- GitHub issue: none
- Status: proposed
- Phase: process-only
- Type: architecture
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/implementation-group-worktree-rule

## Summary

- Contract file: `docs/collaboration/branch-commit-pr-discipline.md`
  (governed by ADR 0006).
- Add a rule: the Implementation group works each work plan in a dedicated
  `git worktree` plus its existing feature-unit branch convention, so
  concurrent work by the Design & Review group (which works against `main`
  for docs/specs/ADRs/review records) does not collide with in-progress
  Implementation-group edits.
- State the worktree naming convention (consistent with existing branch
  naming, e.g. a worktree directory named after the feature branch) and the
  cleanup rule (remove the worktree after the branch merges or the work plan
  closes, whichever governs merge timing today).
- Do not change existing branch-naming or PR rules — this issue only adds
  the worktree-per-work-plan mechanic for the Implementation group.

## Acceptance Notes

- The document states when a worktree is created (work-plan handoff
  received) and when it is removed (post-merge or work-plan close).
- No existing branch/PR rule is weakened or contradicted.

## Dependencies

- Parent: WP-0002
- Depends on: LISS-0019
- Blocks: none
- Related: LISS-0022

## Decisions Not Settled by the Design Agreement

- None known.

## Context

- Included: `docs/collaboration/branch-commit-pr-discipline.md`, ADR 0016
- Omitted: n/a
- Assumptions: the project already uses standard `git worktree` tooling; no
  new dependency is introduced.

## References

- `docs/collaboration/branch-commit-pr-discipline.md`

## Work Notes

- 

## Verification

- `scripts/check-contract-consistency.py`
- Read-through confirming existing branch/PR rules are unchanged in
  substance.
