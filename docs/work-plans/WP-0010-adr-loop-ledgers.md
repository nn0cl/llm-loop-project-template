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
| LISS-0038 | ready | S | S | - | - | - | process/adr-0019-loop-ledgers |

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

- Minimal — single new document, no code, no cross-file edits beyond
  itself.

## Verification Plan

- `ls docs/architecture/adr/` re-confirmed.
- Read-through against ADR 0012-0015/0016-0018 for supersession conflicts.
- Reviewer approval.
