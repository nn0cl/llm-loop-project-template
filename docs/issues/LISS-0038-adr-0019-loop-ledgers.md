# LISS-0038: Write ADR 0019 (process ADR for loop ledgers)

## Metadata

- Local issue ID: LISS-0038
- GitHub issue: none
- Status: ready
- Phase: phase-0-design
- Type: architecture-decision
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/adr-0019-loop-ledgers

## Summary

- Write `docs/architecture/adr/0019-loop-ledgers.md` (or a fuller
  descriptive slug the Implementer chooses, matching this repo's existing
  ADR filename style) stating the five ledgers (spike, backlog,
  loop-settings, post-hoc-audit, findings-must-apply) are an accepted,
  unified process decision, pointing at each source document for its own
  operational detail rather than restating it, and stating explicitly it
  supersedes nothing in ADR 0012-0015 or ADR 0016-0018.

## Acceptance Notes

- Confirms `0019` is genuinely the next-free ADR number at execution time
  (`ls docs/architecture/adr/`) before creating the file.
- Points at, rather than restates, each of the five source documents'
  operational content.
- States explicitly no supersession of ADR 0012-0015/0016-0018.
- Not an ADR-0006 contract file — no trace required.
- Self-review recorded (short form).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0002-adr-loop-ledgers.md
- Depends on: none
- Blocks: none
- Related: `docs/spike/README.md`, `docs/backlog/README.md`,
  `docs/collaboration/loop-settings.md`,
  `docs/collaboration/post-hoc-audit.md`,
  `docs/collaboration/findings-reuse.md`

## Decisions Not Settled by the Design Agreement

- None identified.

## Context

- Included: `docs/backlog/item-0002-*.md`, `DA-2026-08-19-02`, the five
  source documents (read for what to point at, not restate), ADR
  0012-0015, ADR 0016-0018.
- Omitted: application code (none applies).
- Assumptions: none beyond the design agreement's own settled points.

## AI Planning Records

Not required — planning size `S`.

## References

- `docs/collaboration/agreements/2026-08-19-adr-loop-ledgers.md`
  (`DA-2026-08-19-02`)

## Work Notes

- 2026-08-19 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0002-*.md`'s promotion. Confirmed no numbering or
  supersession conflict against ADR 0012-0015/0016-0018. Dispatched to the
  Implementation group.

## Verification

- Pending Implementation-group execution.
