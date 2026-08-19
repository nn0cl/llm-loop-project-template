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
| LISS-0040 | review | S | S | AIP-0040-001 | - | - | process/copy-target-refs-and-branch-cleanup |
| LISS-0041 | in_progress | S | S | AIP-0041-001 | - | - | process/copy-target-refs-and-branch-cleanup |

## Plan-Owned Bug Records

None.

## AI Planning Records

See each issue's own AI Planning Records section.

## Recommended Order

1. LISS-0040 and LISS-0041 (independent files; either order).

## Current Next Issue

- Issue: LISS-0040 and LISS-0041, both unblocked.
- Reason it is unblocked: no dependency; both issues touch different files
  and can proceed in either order or concurrently within the same
  Implementation-group worktree.
- Reopening request needed: no.

## Minor Fix Path

Not applicable — both issues are new work, not a correction to an already-
accepted specification.

## Preflight Validation

Run deterministic checks before independent review, over the whole work plan
once every issue is self-reviewed and complete. Record `pass` or `fail`, the
exact checks and outputs, scope result, and next action. `pass` permits
submission only; it never replaces the separate-context Reviewer.

_pending — recorded once both issues are self-reviewed._

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves:

- Date: _pending Director action_
- Result read:
- Next direction:
- New design agreement (if any):

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
