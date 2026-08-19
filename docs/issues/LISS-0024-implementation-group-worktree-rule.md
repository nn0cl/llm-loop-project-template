# LISS-0024: Add per-work-plan worktree/branch rule for the Implementation group

## Metadata

- Local issue ID: LISS-0024
- GitHub issue: none
- Status: review
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

- 2026-08-18 (Implementer, Implementation group, first standing session):
  added "Implementation-group worktree, per work plan" under "Parallel
  Agent Work (Worktrees)" in
  `docs/collaboration/branch-commit-pr-discipline.md`, stating why (Design &
  Review group works against `main` concurrently), when created (at the
  design-agreement handoff, before Phase 0 starts), the naming convention
  (worktree directory named after the work plan's feature branch), and when
  removed (after merge or work-plan close, whichever governs first). This
  session's own operating environment — a dedicated git worktree at
  `.claude/worktrees/agent-a2450968f458bbc6f`, checked during bootstrap — is
  itself a live instance of the rule now documented.
- Trace: `docs/collaboration/traces/2026-08-18-liss-0024-implementation-group-worktree-rule.md`.

### Self-Review (Implementer, design note -> drafted change)

Per `docs/templates/self-review.md`, short form.

```text
Phase / finding: Architecture Path design note -> drafted change to
  docs/collaboration/branch-commit-pr-discipline.md (new worktree
  subsection)

Command run: python3 scripts/check-contract-consistency.py
Result: contract consistency: all checks passed

Risks considered:
  1. The new subsection weakens or contradicts an existing branch-naming,
     CI-gate, or PR rule.
  2. "When created" and "when removed" are left implicit rather than
     stated as explicit timing rules (the issue's Acceptance Notes require
     both).
  3. The naming convention contradicts the existing branch-naming
     convention rather than being consistent with it.

Why each does not occur:
  1. Read the full file after the edit: "Branches", "Continuous Integration
     Gate", the original three "Parallel Agent Work" bullets, "Stacked
     Branches for Phase Splitting", "Commits", "Pull Requests", and
     "Feature-Unit Branch Creation" are all present unchanged; the new
     subsection ends with an explicit disclaimer, "This does not change
     branch-naming, the CI gate, the feature-unit branch creation steps, or
     any other rule in this document."
  2. The subsection has explicit "**When created**" and "**When removed**"
     bullets, each stating a concrete trigger (design-agreement handoff /
     before Phase 0; branch merge or work-plan close, whichever first) —
     not left to inference.
  3. The naming convention bullet reads "the worktree directory is named
     after the work plan's feature branch... consistent with the
     branch-naming convention above," explicitly building on rather than
     replacing the existing `feature/<name>` / `process/<topic>` etc.
     convention stated in "Branches."
```
