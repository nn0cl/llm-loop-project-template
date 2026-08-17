# LISS-0020: Map personas to the two standing session groups

## Metadata

- Local issue ID: LISS-0020
- GitHub issue: none
- Status: proposed
- Phase: process-only
- Type: architecture
- Priority: high
- Initial planning size: S
- Current planning size: S
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/personas-group-mapping

## Summary

- Contract file: `docs/collaboration/personas.md` (governed by ADR 0006).
- Add a "Session Groups" section stating: Planner, Specifier, Reviewer, and
  Arbiter operate inside the **Design & Review group**; Implementer operates
  inside the **Implementation group**. The two groups are standing sessions
  connected via the `SendMessage` / `ListAgents` tools, per ADR 0016.
- Update the "Where each persona operates" diagram to show the group
  boundary and the cross-session handoff points (backlog-item approval ->
  Design & Review group; design agreement recorded -> handoff to
  Implementation group; Preflight pass -> handoff back to Design & Review
  group for the Reviewer pass; Reviewer approval -> Director close).
- Do not change any persona's responsibilities, inputs, outputs, done-when,
  or must-not fields — this issue is a topology mapping, not a persona
  redefinition.

## Acceptance Notes

- `grep` confirms every core persona name appears with its group assignment.
- The ASCII diagram in "Where each persona operates" reflects the group
  boundary without contradicting ADR 0016 or ADR 0014.
- No persona's five required fields (responsibilities, inputs, outputs,
  done-when, must-not) changed in substance.

## Dependencies

- Parent: WP-0002
- Depends on: LISS-0019
- Blocks: none
- Related: LISS-0021, LISS-0022

## Decisions Not Settled by the Design Agreement

- None known.

## Context

- Included: `docs/collaboration/personas.md`, ADR 0016 (from LISS-0019)
- Omitted: n/a
- Assumptions: none

## References

- `docs/collaboration/personas.md`

## Work Notes

- 

## Verification

- `scripts/check-contract-consistency.py`
- Read-through confirming the five required fields per persona are
  unchanged.
