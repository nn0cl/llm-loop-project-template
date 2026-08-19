# Work Plan: <short title>

## Goal

- 

## Scope

- In:
- Out:

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0000 | proposed | TBD | TBD | AIP-0000-001 | - | - | feature/<name> |

## Plan-Owned Bug Records

<!-- Use only when a bug belongs to this approved plan and has no local issue.
Keep the mutable record here as the single source of truth. -->

### BUG-PLAN-001

- Summary:
- Status:
- Initial planning size:
- Current planning size:
- Reclassification reason:
- Acceptance evidence:
- Phase:
- Deterministic verification:
- Related scope:
- AI planning record: AIP-BUG-PLAN-001-001

## AI Planning Records

<!-- Required for plan-owned bugs of size M or larger and when a second
attempt starts. Link to a local issue record instead of duplicating it. -->

### AIP-BUG-PLAN-001-001

- Status: proposed | accepted | superseded
- Created by:
  - Agent/environment:
  - Model as displayed:
  - Reasoning setting as displayed:
  - N/A reason:
- Created at:
- Planning size:
- Intended execution route:
- Intended scope:
- Estimated token range:
- Estimated token midpoint:
- Token metric:
- Estimation basis:
- Assumptions:
- Confidence:
- Revises:
- Revision reason:
- Superseded by:

## Recommended Order

1. 

## Current Next Issue

- Issue:
- Reason it is unblocked:
- Reopening request needed:

## Minor Fix Path

Use only when the issue is planning size `S`, preserves accepted behavior, and
is expected to finish in one attempt. It must not change a specification, ADR,
port, data model, dependency, or architecture boundary. Record a compact
design note, deterministic verification, and separate Reviewer confirmation.
Escalate to Feature Path or Architecture Path if any condition stops being
true, including when a second attempt is needed.

## Preflight Validation

Run deterministic checks before independent review, over the whole work plan
once every issue is self-reviewed and complete. Record `pass` or `fail`, the
exact checks and outputs, scope result, and next action. `pass` permits
submission only; it never replaces the separate-context Reviewer.

## Review Summary Packet

Filled in once Preflight Validation passes, before submitting to the
work-plan-level Reviewer — the Reviewer's own canonical review input, per
`docs/backlog/item-0012-document-and-log-lifecycle-management.md` facet 6
and `docs/collaboration/design-agreement.md`'s own "Review Summary
Packet" section. Detailed traces, self-reviews, and issue Work Notes are
linked as evidence for a deeper falsification search, not required
reading to start the review.

- **Scope**: what this work plan actually changed, in one or two
  sentences.
- **Current canonical documents**: which ADRs, contract files, or specs
  this work plan's content is now the current source for (or which
  existing ones it extends/amends).
- **Changed files**: the exact file list (new/edited/moved), matching
  the actual diff — not a paraphrase.
- **Findings**: any `Type: review-finding` issue this work plan resolved
  or opened, each with its own current status.
- **Disposition**: what happened — resolved cleanly, resolved with
  tracked follow-ups, blocked, etc.
- **Remaining blockers**: anything still open that could affect the
  Reviewer's decision.
- **Verification result**: the actual Preflight command output (or a
  pointer to its exact location in this same file), not a restated
  summary.
- **Next approval required**: which of the four approval types
  (specification-conformance, phase-correctness, boundary-conformance,
  evidence-sufficiency — per `CLAUDE.md`'s "Approval Model") this work
  plan actually needs, given what changed.

## Work-Plan Review

Reviewer's approval record: <link>

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves:

- Date:
- Result read: <what the Director found on reading the approved work>
- Next direction: <the next work plan's direction, or "engagement ends">
- New design agreement (if any): <link>

## Risks

- 

## Verification Plan

- 
