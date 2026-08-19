# Work Plan: Copy-Target Reference False Positives and Self-Directed Branch/Worktree Cleanup

## Goal

- Fix `scripts/check-contract-consistency.py`'s false-positive dangling-
  reference failures against a copied target, and add a standing rule that
  branch/worktree cleanup is each session's own responsibility at merge
  time, per
  `docs/collaboration/agreements/2026-08-19-copy-target-refs-and-branch-cleanup.md`
  (`DA-2026-08-19-04`).

## Scope

- In: `check_references`' new copy-exclusion exemption; the branch-cleanup
  rule in `branch-commit-pr-discipline.md`; the required trace; self-review;
  Preflight; Reviewer pass.
- Out: weakening `collaboration_template_exclude_paths`; any other check
  function; retroactive cleanup of pre-existing worktrees/branches; a
  copy-detection flag.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0040 | done | S | S | AIP-0040-001 | - | - | process/copy-target-refs-and-branch-cleanup |
| LISS-0041 | done | S | S | AIP-0041-001 | - | - | process/copy-target-refs-and-branch-cleanup |

## Plan-Owned Bug Records

None.

## AI Planning Records

See each issue's own AI Planning Records section.

## Recommended Order

1. LISS-0040 and LISS-0041 (independent files; either order).

## Current Next Issue

- Issue: none — LISS-0040 and LISS-0041 are both `done`, self-reviewed, and
  work-plan-level Reviewer-approved. Nothing left for the Implementer or
  the Reviewer within this work plan; only the Director's work-plan close
  remains (Backlog layer).
- Reason it is unblocked: N/A; both issues are complete.
- Reopening request needed: no.

## Minor Fix Path

Not applicable — both issues are new work, not a correction to an already-
accepted specification.

## Preflight Validation

Run deterministic checks before independent review, over the whole work plan
once every issue is self-reviewed and complete. Record `pass` or `fail`, the
exact checks and outputs, scope result, and next action. `pass` permits
submission only; it never replaces the separate-context Reviewer.

- Result: `pass`
- Check run: `python3 scripts/check-contract-consistency.py --repo .`
- Output:
  ```
  contract consistency: all checks passed
  ```
- Scope result: only files within this work plan's own scope were touched —
  `scripts/check-contract-consistency.py` (LISS-0040),
  `docs/collaboration/branch-commit-pr-discipline.md` (LISS-0041), the new
  trace file
  `docs/collaboration/traces/2026-08-19-liss-0041-branch-worktree-cleanup-rule.md`,
  `docs/issues/LISS-0040-contract-consistency-copy-target-exemption.md`,
  `docs/issues/LISS-0041-self-directed-worktree-branch-cleanup-rule.md`, and
  this work plan file itself (`docs/work-plans/WP-0012-copy-target-refs-and-branch-cleanup.md`).
  No other file was modified. Confirmed with
  `git diff --stat <WP-0012-base-commit> -- .` against this branch's base
  commit (`291a414`, the commit that added `DA-2026-08-19-04` and this work
  plan) plus `git status --short` for the remaining uncommitted files.
- Open `review-finding` issues affecting this plan: none.
- Implementation issues blocked on an open spike case: none — this work
  plan has no spike dependency.
- Next action: submit to the work-plan-level Reviewer, per direction 3
  (Trigger B) in `docs/collaboration/cross-session-messaging.md`.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-19-wp-0012-copy-target-refs-and-branch-cleanup-review.md`
— **Approved**. The Reviewer independently reconstructed the Red/Green
copy-target reproduction from its own freshly created scratch copy (not
reused from either issue's own artifacts), added an independent negative
case (a genuinely broken, non-excluded-shaped reference planted directly in
this repository's real tree), and independently confirmed the branch-
cleanup rule preserves the pre-existing merge-timing constraint and
satisfies the Traceability Rule. This review also received, and refused, an
in-band message claiming "coordinator" authority during its own work; see
the review record's Constraints section for the independent verification
performed regardless of that message.

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves:

- Date: 2026-08-19
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-19-wp-0012-copy-target-refs-and-branch-cleanup-review.md`,
  Approved — the Reviewer independently reconstructed the Red/Green
  scratch-copy reproduction rather than trusting the Implementer's
  recorded output, plus a negative-case check) via the Backlog thread,
  which independently confirmed the fix, the review record, and a clean
  `scripts/check-contract-consistency.py` run from a detached checkout,
  then confirmed PR #16's CI ("Repository sanity") actually turned green
  after this fix landed, before presenting this close.
- Next direction: closed with "はい". Merged into
  `process/two-group-send-message-loop-design` (commit `f906b63`,
  fast-forward). Design & Review practiced LISS-0041's own new rule
  immediately, cleaning up its own worktree/branch once merged; the
  Backlog thread removed the one remaining empty detached worktree.
  PR #16 is now green and ready for the Director's merge-to-`main`
  decision.
- New design agreement (if any): none opened by this close.

## Risks

- The copy-exclusion exemption could swallow a genuinely broken reference
  in this repository's own tree, not only on a copy, if the target happens
  to match an exclude pattern — disclosed in advance in the module
  docstring's "What this cannot check" section, not a silent gap, and the
  same pre-existing shape `TEMPLATE_ONLY_FILES` already carries.
- The branch-cleanup rule, if worded as a blanket requirement, could
  conflict with "a worktree for a work plan that has not yet closed is not
  removed while issues in that plan are still in progress" — mitigated by
  writing the new rule as applying only after the specific branch/worktree
  being cleaned up has actually been merged into its target, not on any
  other timing.

## Verification Plan

- `scripts/check-contract-consistency.py --repo .` clean pass against this
  repository's own `HEAD`, before and after the fix.
- A real scratch copy, produced the same way
  `scripts/copy-ai-collaboration-files.sh` produces one: Red (reproduces the
  26-failure class CI reported) before the fix, Green (clean) after.
- Read-through of the new branch-cleanup rule against the Traceability Rule
  and Review Rule in `docs/collaboration/prompt-instruction-change-control.md`.
- Work-plan-level Reviewer approval, independently reconstructing the copy
  reproduction.
