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
| LISS-0035 | ready | M | M | AIP-0035-001 | - | - | process/document-consistency-drift-checks |

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
