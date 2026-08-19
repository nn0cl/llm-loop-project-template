# Work Plan: Catch Document-Consistency Drift Deterministically

## Goal

- Extend `scripts/check-contract-consistency.py` with two new deterministic
  checks (ID-range collision detection, superseding-phrase propagation via
  an anchored-registration mechanism), add an issue-status/work-plan
  cross-reference check, and make `.github/workflows/ci.yml`'s ADR-existence
  step dynamic instead of hardcoded — per
  `docs/backlog/item-0009-document-consistency-drift-on-completion.md` and
  `docs/collaboration/agreements/2026-08-18-document-consistency-drift-checks.md`
  (`DA-2026-08-18-06`).

## Scope

- In: the four Plan tasks above, plus self-review, Preflight, and
  separate-context Reviewer pass.
- Out: pattern 5 (template-copy exclusion gaps — tracked by
  `task_cdbaa1ce`); any meaning-inference heuristic; item-0006's own scope.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0035 | done | M | M | AIP-0035-001 | - | - | process/document-consistency-drift-checks |

## Plan-Owned Bug Records

None.

## AI Planning Records

See LISS-0035's own AI Planning Records section.

## Recommended Order

1. LISS-0035 (single issue; four tasks against one script plus one CI
   file, tightly coupled enough to keep as one reviewable unit).

## Current Next Issue

- Issue: LISS-0035
- Reason it is unblocked: no dependencies; `DA-2026-08-18-06` covers it
  fully, including the exact registration-mechanism shape.
- Reopening request needed: no.

## Minor Fix Path

Not applicable (planning size `M`, new check functions, not a small
correction against an already-approved result).

## Preflight Validation

- Result: `pass`
- Checks and command output:
  - CI's "Check architecture decision records" step logic, reproduced
    locally against the real `docs/architecture/adr/` directory:
    ```text
    PASS: contiguous ADR sequence 0001-0016, 16 files
    ```
  - `python3 scripts/check-contract-consistency.py` (full run, all eight
    checks, against `HEAD`):
    ```text
    contract consistency: all checks passed
    ```
    Exit code: 0.
  - Each of the three new check functions (`check_id_range_collisions`,
    `check_issue_status_sync`, `check_superseding_phrases`) additionally
    verified in isolation: clean pass on `HEAD`, and a demonstrated failure
    against a constructed synthetic case per check. Full pasted output for
    all of the above is in LISS-0035's Work Notes (self-review, full form).
- Scope result: all four in-scope tasks (CI dynamic ADR check; three new
  script-level checks; docstring update) complete and verified per
  DA-2026-08-18-06's Plan and Verification sections. No open
  `review-finding` issues affect this work plan. No implementation issue is
  blocked on an open spike case.
- Next action: submit to the Design & Review group's separate-context
  Reviewer pass (per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`
  and this work plan's own Plan, Task 8). Preflight is not itself an
  approval and does not set `wont_do` or `closed`.

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: 2026-08-18
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-18-wp-0007-document-consistency-drift-checks-review.md`,
  Approved — the Reviewer built its own synthetic failure case against
  `check_issue_status_sync` rather than only re-reading the reported one,
  and disclosed narrower verification depth for the other two new checks
  rather than glossing over it) via the Backlog thread, which independently
  confirmed the new checker code, the review record, and a clean
  `scripts/check-contract-consistency.py` run from a detached checkout
  before presenting this close.
- Next direction: closed with "はい。Close". Merged into
  `process/two-group-send-message-loop-design` (commit `456680d`, together
  with WP-0004/0005/0008). Push and PR remain separate explicit actions.
- New design agreement (if any): none opened by this close.

## Risks

- The superseding-phrase registration mechanism, if under-populated,
  provides false confidence (a document not yet registered is invisible to
  it, exactly like the ADR-range mechanism's own documented gap); mitigated
  by registering three real, already-known instances rather than shipping
  the mechanism empty, and by the module docstring's existing practice of
  disclosing this exact class of gap explicitly rather than implying full
  coverage.
- A new check could itself become a source of false positives against this
  repository's own history (the script's docstring documents three prior
  rounds of exactly this happening); mitigated by requiring each new
  check's synthetic-failure case to be independently reproduced by the
  Reviewer, not just asserted by the Implementer.

## Verification Plan

- Each new check: clean pass on `HEAD`, demonstrated failure on a
  constructed synthetic case.
- Full `scripts/check-contract-consistency.py` run.
- CI ADR-existence step's dynamic logic reproduced locally.
- Separate-context Reviewer approval, independently re-running at least one
  synthetic-failure case per new check.
