# Work Plan: Process ADR for Loop Ledgers

## Goal

- Write ADR 0019, formalizing the existing docs-first loop-ledger rules
  (spike, backlog, loop-settings, post-hoc-audit, findings-must-apply) as
  a single accepted process decision, per
  `docs/collaboration/agreements/2026-08-19-adr-loop-ledgers.md`
  (`DA-2026-08-19-02`).

## Scope

- In: ADR 0019, self-review, Preflight, Reviewer pass.
- Out: rewriting the five source documents; changes to ADR 0012-0015/0016-0018.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0038 | done | S | S | - | - | - | process/adr-0019-loop-ledgers |

## Plan-Owned Bug Records

None.

## AI Planning Records

None required — planning size `S`.

## Recommended Order

1. LISS-0038.

## Current Next Issue

- Issue: LISS-0038
- Reason it is unblocked: no dependencies; `DA-2026-08-19-02` covers it
  fully.
- Reopening request needed: no.

## Minor Fix Path

Not applicable — new ADR, not a correction.

## Preflight Validation

- Result: `pass`
- Checks and command output:

  ```
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed
  ```

  First run (before the entry-document sync below) failed with two findings,
  both resolved in the same commit: (1) an illustrative
  `docs/backlog/item-NNNN-short-slug.md` string in ADR 0019's prose resolved
  as a dangling file reference — fixed by switching to this repository's own
  established `item-NNNN-*.md` wildcard convention (already used in ADR
  0016, `ai-human-scheme.md`, `design-agreement.md`); (2) the expected
  ADR-range drift in `README.md`, `QUICKSTART.md`, `QUICKSTART.ja.md` caused
  by adding a 19th ADR file — fixed by syncing those files' registered
  range statements (0018 -> 0019 / next-adopter 0019 -> 0020), the same
  mechanical step commit `b1a49c1` (ADR 0018) made for the same reason.
  `.github/workflows/ci.yml`'s ADR-existence check is dynamic/contiguous-
  sequence based (LISS-0035) and needed no edit.
- Scope result: LISS-0038 self-reviewed and complete (Status: `review`); it
  is the work plan's only issue. `ls docs/architecture/adr/` reconfirmed
  `0019` was free before creation and the sequence is contiguous 0001-0019
  after. No open `Type: review-finding` issues and no spike-blocked
  implementation issues affect this plan.
- Next action: submit to the work-plan-level Reviewer, separate context
  (Design & Review group), per the design agreement's Plan task 4.

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: 2026-08-19
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-19-wp-0010-adr-loop-ledgers-review.md`,
  Approved — independently spot-checked two of ADR 0019's five ledger
  summaries against their source files rather than trusting the ADR's own
  prose) via the Backlog thread, which independently confirmed ADR 0019,
  the review record, and a clean `scripts/check-contract-consistency.py`
  run from a detached checkout before presenting this close.
- Next direction: closed with "はい". Merged into
  `process/two-group-send-message-loop-design` (commit `a35c25e`, together
  with WP-0011). Push and PR remain separate explicit actions.
- New design agreement (if any): none opened by this close.

## Risks

- Minimal — single new document, no code, no cross-file edits beyond
  itself.

## Verification Plan

- `ls docs/architecture/adr/` re-confirmed.
- Read-through against ADR 0012-0015/0016-0018 for supersession conflicts.
- Reviewer approval.
