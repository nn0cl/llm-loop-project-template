# Work Plan: Exclude Work-Plan History From Template Propagation

## Goal

- Confirm (already done in `DA-2026-08-18-04`'s Spike Result — no code
  change needed) that new `docs/collaboration/*.md` and
  `docs/architecture/adr/*.md` files already propagate automatically, and
  fix the adjacent gap the same empirical test surfaced: `docs/work-plans/
  WP-*.md` is copied into adopter repositories as if it were reusable
  template content, unlike the equivalent `docs/issues/LISS-*.md` and
  `docs/backlog/item-*.md` exclusions.

## Scope

- In: `scripts/lib/collaboration-template-paths.sh` exclusion list;
  `.github/workflows/ci.yml` smoke-test assertion; re-run of the empirical
  copy+update test; self-review; Preflight; separate-context Reviewer pass.
- Out: Tier 1/Tier 2 classification logic; any document content; the
  separate CI hardcoded-ADR-number-list gap (flagged elsewhere).

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0031 | ready | S | S | - | - | - | process/template-propagation-work-plan-exclusion |

## Plan-Owned Bug Records

None.

## AI Planning Records

None required — planning size `S`, first attempt.

## Recommended Order

1. LISS-0031 (single issue).

## Current Next Issue

- Issue: LISS-0031
- Reason it is unblocked: no dependencies; `DA-2026-08-18-04` covers it
  fully, including the exact exclusion pattern and CI assertion location.
- Reopening request needed: no.

## Minor Fix Path

Not formally invoked (this is a fresh work plan, not a correction against an
already-approved one), but the single issue is planning size `S`, one
mechanical exclusion-list addition plus a matching CI assertion, one attempt
expected, and touches no specification/ADR/port/data-model/architecture
boundary.

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

- Over-broad exclusion pattern could accidentally exclude
  `docs/work-plans/.gitkeep` or a future non-`WP-NNNN`-numbered file in
  that directory; mitigated by the exact-pattern acceptance criterion
  (`docs/work-plans/WP-*.md` only) and Task 3's explicit re-check that
  `.gitkeep` still copies.

## Verification Plan

- Empirical copy+update test re-run against a scratch adopter, before and
  after the fix.
- `.github/workflows/ci.yml`'s existing smoke-test command sequence, run
  locally.
- Separate-context Reviewer approval.
