# Work Plan: Contract-Sync Diff Records and Per-Agent-Tool Rule Registry

## Goal

- Close item-0012 facet 4 by adding a structured Sync Diff Record template
  and a canonical Per-Agent-Tool Rule Applicability Registry, extending
  ADR 0008's already-existing Tier 1/Tier 2 sync mechanism rather than
  rebuilding it, per
  `docs/backlog/item-0012-document-and-log-lifecycle-management.md` and
  `docs/collaboration/agreements/2026-08-19-contract-sync-diff-records.md`
  (`DA-2026-08-19-07`).

## Scope

- In: `docs/templates/sync-diff-record.md` (new), a new "Per-Agent-Tool
  Rule Applicability Registry" section plus a shortened cross-referencing
  edit to the existing Cursor bullet in
  `docs/collaboration/prompt-instruction-change-control.md`, one new
  cross-referencing paragraph plus a Step 6 addition in
  `docs/templates/contract-file-sync-prompt.md`, the required AI work
  trace (all three touched files are ADR-0006 contract files), self-review,
  Preflight, work-plan-level Reviewer pass.
- Out: any change to `docs/architecture/adr/0008-template-update-propagation.md`
  itself, `scripts/update-ai-collaboration-files.sh`,
  `scripts/copy-ai-collaboration-files.sh`, `CLAUDE.md`, or any of its
  four mirrors. No new ADR (see Settled Ambiguities in the covering
  agreement). Facets 5 (drift-prevention entry documents and CI checks)
  and 6 (review-summary packets) — later, separate work plans.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0046 | ready | M | M | AIP-0046-001 | - | - | process/contract-sync-diff-records |

## Plan-Owned Bug Records

None.

## AI Planning Records

See LISS-0046's own AIP-0046-001 (required, planning size `M`).

## Recommended Order

1. LISS-0046 (single issue).

## Current Next Issue

- Issue: LISS-0046
- Reason it is unblocked: no dependencies; `DA-2026-08-19-07` covers it
  fully, including exact content for all three files.
- Reopening request needed: no.

## Minor Fix Path

Does not apply — this adds new contract content (a new template file, a
new registry section), not a correction to an existing defect. Full
design-agreement + work-plan + Reviewer-pass cycle applies.

## Preflight Validation

- Result: _pending — recorded after the Implementation group completes
  LISS-0046_
- Checks and command output: _pending_
- Scope result: _pending_
- Next action: _pending_

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: _pending_
- Result read: _pending — Director close is a separate, later action._
- Next direction: _pending_
- New design agreement (if any): _pending — facets 5 and 6 each get their
  own design agreement when reached._

## Risks

- Low-medium (planning size `M`). Main risk: scope creep into rebuilding
  ADR 0008's already-working Tier 1/Tier 2 mechanism instead of only
  extending it — explicitly fenced off in Scope and checked directly in
  Preflight's scope-result step. Secondary risk: the new registry table
  in `prompt-instruction-change-control.md` could drift from the actual
  current mirror-sync behavior if not kept in sync with future changes —
  named as a standing maintenance expectation in the new section's own
  text, not a one-time artifact.
