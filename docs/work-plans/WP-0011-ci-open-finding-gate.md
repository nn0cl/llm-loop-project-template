# Work Plan: Deterministic Gate for Open Review-Finding Issues

## Goal

- Add `check_open_findings_gate` to `scripts/check-contract-consistency.py`,
  failing when a closed work plan still lists a `Type: review-finding`
  issue that is neither `closed` nor `wont_do`, honoring
  `[findings].block_work_plan_done_on_open_findings`, per
  `docs/collaboration/agreements/2026-08-19-ci-open-finding-gate.md`
  (`DA-2026-08-19-03`).

## Scope

- In: the new check function, its wiring, self-review, Preflight, Reviewer
  pass.
- Out: `findings-reuse.md` lifecycle changes; retroactively closing
  `LISS-0003`; replacing the separate-context Reviewer.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0039 | done | M | M | AIP-0039-001 | - | - | process/ci-open-finding-gate |

## Plan-Owned Bug Records

None.

## AI Planning Records

See LISS-0039's own AI Planning Records section.

## Recommended Order

1. LISS-0039.

## Current Next Issue

- Issue: none — LISS-0039 is executed and self-reviewed (`Status: review`).
  Preflight Validation below recorded `pass`.
- Reason: nothing left for the Implementer within this work plan's scope;
  the whole work plan is ready for the Design & Review group's
  separate-context Reviewer pass (Task 5).
- Reopening request needed: no.

## Minor Fix Path

Not applicable — new check function, planning size `M`.

## Preflight Validation

- Result: **pass**
- Checks and command output:

  ```text
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed
  ```

  Exit code 0. Also see LISS-0039's own Deterministic Verification Output
  for the synthetic failure and synthetic pass-with-flag-false cases run
  against isolated scratch fixtures (not against this repository), which
  together demonstrate the new `check_open_findings_gate` function actually
  fires when it should and actually reads
  `[findings].block_work_plan_done_on_open_findings` rather than always
  passing or always failing.
- Scope result: LISS-0039's Status is `review`; full-form self-review is
  recorded in its own Work Notes (planning size `M`); no open
  `Type: review-finding` issue affects this area (`LISS-0003` is explicitly
  out of this item's own scope, per `DA-2026-08-19-03`'s Settled
  Ambiguities); no issue in this plan is blocked on an open spike case. Only
  `scripts/check-contract-consistency.py` was touched, matching this work
  plan's Scope; no other file was edited. `scripts/check-contract-consistency.py`
  is not an ADR-0006 contract file, so no AI work trace is required, per
  `DA-2026-08-19-03`'s own Scope statement.
- Next action: submit to the Design & Review group's separate-context
  Reviewer pass (Task 5). This Preflight result is not itself an approval
  and does not set any issue to `done`/`closed`.

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: 2026-08-19
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-19-wp-0011-ci-open-finding-gate-review.md`,
  Approved — the Reviewer built its own independent test, injecting the
  real historical `LISS-0003` scenario into a copy of the already-closed
  WP-0003's findings table and confirming both the trigger and the
  `block_work_plan_done_on_open_findings = false` stand-down path) via the
  Backlog thread, which independently confirmed the new checker code, the
  review record, and a clean `scripts/check-contract-consistency.py` run
  from a detached checkout before presenting this close.
- Next direction: closed with "はい". Merged into
  `process/two-group-send-message-loop-design` (commit `a35c25e`, together
  with WP-0010). Push and PR remain separate explicit actions. This closes
  the entire pre-existing backlog (item-0001 through item-0003) plus the
  two-group send_message loop batch (item-0004 through item-0010) — every
  promoted backlog item as of 2026-08-19 is now Director-closed.
- New design agreement (if any): none opened by this close.

## Risks

- False positives against this repository's own real work-plan history if
  the findings-table parsing is too loose; mitigated by anchoring on the
  exact existing table shape (`| Issue | Status | Resolution |`) every
  current work plan already uses, and requiring a clean pass on `HEAD` as
  part of Preflight.
- False negatives (the check silently ignores `LISS-0003`'s real
  `resolved` state) are expected and disclosed in advance, per
  `DA-2026-08-19-03`'s own Settled Ambiguities — not a defect to fix
  silently within this item's scope.

## Verification Plan

- Clean pass on `HEAD`.
- Synthetic failure case (open finding, flag `true`).
- Synthetic pass case (same finding, flag `false`).
- Reviewer approval, independently reconstructing at least one case.
