# Work Plan: Document and Log Lifecycle Model

## Goal

- Produce ADR 0020, an empty restoration ledger, and a small disambiguating
  cross-reference edit, closing facets 1-3 of
  `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
  (four-layer document model, status vocabulary and consolidation
  conditions, trace lifecycle), per
  `docs/spike/case-0001-document-log-lifecycle-management/case.md`
  (Status: closed, Selection: Option B) and
  `docs/collaboration/agreements/2026-08-19-document-log-lifecycle-model.md`
  (`DA-2026-08-19-06`).

## Scope

- In: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
  (new), `docs/collaboration/restoration-ledger.md` (new, empty),
  `docs/collaboration/local-issue-planning.md` (one short cross-reference
  paragraph added to its "Status Values" section), the required AI work
  trace (`local-issue-planning.md` is an ADR-0006 contract file),
  self-review, Preflight, work-plan-level Reviewer pass.
- Out: any move, archive, deletion, or content edit of an existing
  `docs/issues/`, `docs/work-plans/`, `docs/collaboration/traces/`,
  `docs/collaboration/reviews/`, `docs/collaboration/agreements/`, or
  other `docs/architecture/adr/` file — retroactive application is a
  separate, later work plan, per the Director's own sequencing decision
  at item-0012's promotion. Facets 4 (contract-sync diff record), 5
  (drift-prevention entry documents and CI checks), and 6
  (review-summary packets) — sequenced as later, separate work plans per
  the spike's own decomposition table. Any edit to `CLAUDE.md` or its four
  mirrors (ADR 0020 is self-contained, following the ADR 0018 precedent
  of no companion policy doc or required-reading-list entry; confirmed by
  grep that no mirror file references ADR numbers directly).

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0043 | ready | L | L | AIP-0043-001 | case-0001 (closed) | later item-0012 facet-4/5/6 work plans | process/document-log-lifecycle-model |

## Plan-Owned Bug Records

None.

## AI Planning Records

See LISS-0043's own AIP-0043-001 (required, planning size `L`).

## Recommended Order

1. LISS-0043 (single issue).

## Current Next Issue

- Issue: LISS-0043
- Reason it is unblocked: its one dependency (spike case-0001) is closed;
  `DA-2026-08-19-06` covers it fully, including the exact ADR text,
  ledger content, and cross-reference paragraph.
- Reopening request needed: no.

## Minor Fix Path

Does not apply — this is Architecture Path work (a new ADR), not a minor
fix or review-finding correction. Full design-agreement + work-plan +
Reviewer-pass cycle applies, matching ADR 0016/0018/0019's own precedent
for how this repository lands a new ADR.

## Preflight Validation

- Result: _pending — recorded after the Implementation group completes
  LISS-0043_
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
- New design agreement (if any): _pending — the later facet-4/5/6 work
  plans each get their own design agreement when reached, per the spike's
  decomposition table; not opened by this work plan's own close._

## Risks

- Medium (planning size `L`, new ADR). Main risk: Rule 2's illustrative,
  non-exhaustive per-type consolidation triggers may need refinement once
  the later retroactive-application work plan actually applies them —
  named explicitly in ADR 0020's own Consequences section, not hidden.
  Secondary risk: scope creep into touching `CLAUDE.md`/mirrors or an
  existing repository document — explicitly fenced off in this work
  plan's own Scope and in ADR 0020's Rule 7, and checked directly in
  Preflight's scope-result step.
