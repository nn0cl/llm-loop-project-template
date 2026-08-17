# LISS-0023: Add the standing two-group pair as a session type

## Metadata

- Local issue ID: LISS-0023
- GitHub issue: none
- Status: proposed
- Phase: process-only
- Type: architecture
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/session-start-standing-pair

## Summary

- Contract file: `docs/collaboration/session-start-and-resume.md` (governed
  by ADR 0006).
- Add a fourth session type, "Standing Two-Group Pair", describing:
  - the Director starts the Design & Review group session and the
    Implementation group session once each (not per work plan);
  - each session's first message states its group and persona set, per the
    existing Session Entry Checklist;
  - both sessions read `docs/collaboration/loop-settings.toml` and the
    normal recovery-order documents at their own start, same as any other
    session;
  - ongoing operation follows the handoff protocol in
    `docs/collaboration/cross-session-messaging.md` (LISS-0022) rather than
    the Director restating a task message per work plan;
  - when either session ends (process restart, crash, manual stop), the
    Director or the other group re-establishes it using the same repository
    artifacts (backlog, agreements, work plans) as any resumed session —
    the standing pair does not introduce a new continuity mechanism, it
    reuses the existing artifact-only continuity rule.

## Acceptance Notes

- The new session type is listed alongside the existing three, with its own
  short heading.
- It cross-references LISS-0022's protocol document instead of duplicating
  its content.
- It restates that artifact-only continuity (no chat memory) still applies
  to a standing session after a restart.

## Dependencies

- Parent: WP-0002
- Depends on: LISS-0019
- Blocks: none
- Related: LISS-0022

## Decisions Not Settled by the Design Agreement

- None known.

## Context

- Included: `docs/collaboration/session-start-and-resume.md`, ADR 0016
- Omitted: n/a
- Assumptions: none

## References

- `docs/collaboration/session-start-and-resume.md`

## Work Notes

- 

## Verification

- `scripts/check-contract-consistency.py`
- Read-through confirming no contradiction with the "artifact-only
  continuity" rule.
