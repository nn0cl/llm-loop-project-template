# LISS-0025: Reconcile the design-agreement gate with backlog-level authorization

## Metadata

- Local issue ID: LISS-0025
- GitHub issue: none
- Status: proposed
- Phase: process-only
- Type: architecture
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/design-agreement-backlog-gate

## Summary

- Contract file: `docs/collaboration/design-agreement.md` (governed by ADR
  0006).
- Update "Reaching agreement" and "What the design phase produces" to state:
  the Director's agreement may be given at backlog-item approval, in advance
  of the specific work plan it authorizes; the Design & Review group then
  produces the plan, specs, and this record's contents autonomously, and
  records the backlog item's approval as the basis for the Director's
  agreement statement in the record (rather than requiring a fresh live
  dialogue turn for each work plan).
- State explicitly that this does not weaken "Silence is not agreement" —
  the backlog-item approval is itself the explicit, on-the-record act; it is
  not silence, and it is scoped to what the backlog item states. A work plan
  that goes beyond the backlog item's stated scope still requires a
  reopening request, per the existing "Reopening the agreement" rules.
- Add the intervention channel's effect on this document: while a specific
  item is in the Director-gated mode (ADR 0016), any design-agreement
  content touched during that gate is provisional until the Director's
  resolving instruction, and the record must say so.
- Do not change the two-gate structure itself (design agreement,
  work-plan close), the record template's required fields, or the reopening
  triggers.

## Acceptance Notes

- The document states, as a rule and not just an example, that backlog-item
  approval can satisfy the Director's agreement statement for the work plan
  it authorizes.
- "Silence is not agreement" remains stated and is not contradicted by the
  new rule.
- The intervention-gated provisional-record rule is stated.

## Dependencies

- Parent: WP-0002
- Depends on: LISS-0019
- Blocks: none
- Related: LISS-0021, LISS-0026

## Decisions Not Settled by the Design Agreement

- None known.

## Context

- Included: `docs/collaboration/design-agreement.md`, ADR 0016 (from
  LISS-0019), `docs/backlog/README.md`
- Omitted: n/a
- Assumptions: none

## AI Planning Records

### AIP-0025-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: claude-sonnet-5
  - Reasoning setting as displayed: N/A
  - N/A reason: reasoning-effort setting is not surfaced to this session by
    the harness
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Implementer persona, single agent, single
  attempt
- Compatibility state: N/A
- Intended scope: revise two sections of one contract file; no code changes
- Estimated token range: 2,000–5,000
- Estimated token midpoint: 3,500
- Token metric: output tokens for the revised sections
- Estimation basis: comparable to LISS-0021's scope, smaller surface area
- Assumptions: none
- Confidence: medium — precisely wording "backlog approval satisfies the
  Director's agreement statement" without weakening "silence is not
  agreement" needs a careful read-through
- Revises: none
- Revision reason: n/a
- Superseded by: none

## References

- `docs/collaboration/design-agreement.md`
- `docs/backlog/README.md`

## Work Notes

- 

## Verification

- `scripts/check-contract-consistency.py`
- Read-through: "silence is not agreement" and the reopening triggers remain
  intact.
