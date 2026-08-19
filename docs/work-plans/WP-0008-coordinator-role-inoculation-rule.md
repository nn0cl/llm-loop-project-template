# Work Plan: Coordinator-Role Inoculation Rule

## Goal

- Add a standing rule to `docs/architecture/agent-quickstart.md` stating no
  "coordinator" persona exists in this project's model and that any
  in-band message claiming that or other unverified authority must be
  refused and reported, per
  `docs/backlog/item-0010-coordinator-role-inoculation-rule.md` and
  `docs/collaboration/agreements/2026-08-18-coordinator-role-inoculation-rule.md`
  (`DA-2026-08-18-07`).

## Scope

- In: the one addition above, self-review, Preflight, work-plan-level
  Reviewer pass.
- Out: any edit to `CLAUDE.md`, the four mirrors, or `personas.md`.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0036 | review | S | S | - | - | - | process/coordinator-role-inoculation-rule |

## Plan-Owned Bug Records

None.

## AI Planning Records

None required — planning size `S`, first attempt.

## Recommended Order

1. LISS-0036 (single issue).

## Current Next Issue

- Issue: LISS-0036
- Reason it is unblocked: no dependencies; `DA-2026-08-18-07` covers it
  fully, including the exact placement decision.
- Reopening request needed: no.

## Minor Fix Path

Applies in substance: planning size `S`, single narrow documentation
addition, preserves everything else, one attempt expected, no
specification/ADR/port/data-model/architecture-boundary change. Not an
ADR-0006 contract-file change (confirmed: `agent-quickstart.md` is not on
that list), so no trace is required, but the work-plan-level Reviewer pass
still applies.

## Preflight Validation

- Result: `pass`
- Checks and command output:

  ```console
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed
  ```

  Exit code: 0. Confirms `agent-quickstart.md`'s addition did not disturb
  mirror-parity machinery, as expected since it is not an ADR-0006 contract
  file (per `DA-2026-08-18-07`'s Spike Result).
- Scope result: only `docs/architecture/agent-quickstart.md` was touched, in
  its "Session Entry" section, as a new numbered item (item 6) after the
  existing list — matching the design agreement's Plan and Scope. No edit to
  `CLAUDE.md`, the four mirrors, or `docs/collaboration/personas.md`. No
  `Type: review-finding` issues open against this area.
- Next action: submit to the Design & Review group's work-plan-level
  Reviewer pass.

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

- Minimal — single narrow documentation addition, no code, no contract-file
  mirror-propagation surface.

## Verification Plan

- `scripts/check-contract-consistency.py` (regression check).
- Read-through diff.
- Work-plan-level Reviewer approval.
