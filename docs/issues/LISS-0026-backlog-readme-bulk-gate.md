# LISS-0026: State backlog-item approval as the bulk design-phase gate

## Metadata

- Local issue ID: LISS-0026
- GitHub issue: none
- Status: proposed
- Phase: process-only
- Type: architecture
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/backlog-readme-bulk-gate

## Summary

- Not a contract file (`docs/backlog/README.md` is outside
  `docs/collaboration/*.md`); normal self-review plus the work-plan-level
  Reviewer pass applies, ADR 0006 does not.
- Add a note stating: once the Director approves a backlog item for
  promotion, that approval is the design-phase human gate for the work it
  authorizes (per ADR 0016 and the updated
  `docs/collaboration/design-agreement.md`), and the Design & Review group
  may proceed autonomously from there.
- State the compliance boundary explicitly: autonomous progress after
  backlog approval remains bounded by the project's operational rules and
  applicable law, and this is not satisfied implicitly — a backlog item
  that would require exceeding either is a reopening request, not a
  judgment call.
- Cross-reference ADR 0016 and `docs/collaboration/design-agreement.md`
  instead of duplicating their content.

## Acceptance Notes

- `docs/backlog/README.md` states the bulk-gate rule and the compliance
  boundary, each in one place, with cross-references rather than duplicated
  prose.

## Dependencies

- Parent: WP-0002
- Depends on: LISS-0019
- Blocks: none
- Related: LISS-0025

## Decisions Not Settled by the Design Agreement

- None known.

## Context

- Included: `docs/backlog/README.md`, ADR 0016 (from LISS-0019)
- Omitted: n/a
- Assumptions: none

## References

- `docs/backlog/README.md`

## Work Notes

- 

## Verification

- Read-through: cross-references resolve to the correct updated documents
  (post LISS-0019 and LISS-0025).
