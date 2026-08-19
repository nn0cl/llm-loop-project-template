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
| LISS-0039 | ready | M | M | AIP-0039-001 | - | - | process/ci-open-finding-gate |

## Plan-Owned Bug Records

None.

## AI Planning Records

See LISS-0039's own AI Planning Records section.

## Recommended Order

1. LISS-0039.

## Current Next Issue

- Issue: LISS-0039
- Reason it is unblocked: no dependencies; `DA-2026-08-19-03` covers it
  fully, including the exact anchor structure (each work plan's own
  findings table).
- Reopening request needed: no.

## Minor Fix Path

Not applicable — new check function, planning size `M`.

## Preflight Validation

- Result: _pending Implementation-group execution_
- Checks and command output: _to be recorded by the Implementer_
- Scope result: _to be recorded_
- Next action: _to be recorded_

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: _pending Director action_
- Result read:
- Next direction:
- New design agreement (if any):

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
