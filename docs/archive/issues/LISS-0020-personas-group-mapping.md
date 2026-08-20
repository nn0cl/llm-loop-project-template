# LISS-0020: Map personas to the two standing session groups

## Metadata

- Local issue ID: LISS-0020
- GitHub issue: none
- Status: done
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

- 2026-08-18 (Implementer, Implementation group, first standing session):
  added a "Session Groups" section to `docs/collaboration/personas.md`
  stating Planner/Specifier/Reviewer/Arbiter operate in the Design & Review
  group and Implementer operates in the Implementation group, per ADR 0016
  Rule 1. Redrew the "Where each persona operates" diagram to show the group
  boundary (double-line dividers) and the four cross-session handoff points:
  backlog-item approval -> Design & Review group; design agreement recorded
  -> handoff to Implementation group; Preflight pass -> handoff back to
  Design & Review group; Reviewer approval -> Director close. Did not touch
  any persona's five required fields (responsibilities, inputs, outputs,
  done-when, must-not) — confirmed by reading the full "Core personas"
  section after the edit; only the diagram above it and the new section
  before it changed.
- Trace: `docs/collaboration/traces/2026-08-18-liss-0020-personas-group-mapping.md`.

### Self-Review (Implementer, design note -> drafted change)

Per `docs/templates/self-review.md`, short form.

```text
Phase / finding: Architecture Path design note -> drafted change to
  docs/collaboration/personas.md (Session Groups section + redrawn diagram)

Command run: python3 scripts/check-contract-consistency.py
Result:
  references:
    docs/architecture/adr/0016-...md:192 names 'docs/collaboration/cross-session-messaging.md', which does not exist
    docs/architecture/adr/0016-...md:284 names 'docs/collaboration/cross-session-messaging.md', which does not exist
  contract consistency: 2 failure(s)
(Same 2 pre-existing, expected failures as the baseline run before this
  issue's edit — both are LISS-0022's own target file, not yet created. No
  new failure introduced by this edit.)

grep -n "Planner\|Specifier\|Reviewer\|Arbiter\|Implementer" docs/collaboration/personas.md | grep -i "group"
Result:
  22:- **Design & Review group**: Planner, Specifier, Reviewer, Arbiter.
  23:- **Implementation group**: Implementer, working in a dedicated `git

Risks considered:
  1. A persona's five required fields (responsibilities, inputs, outputs,
     done-when, must-not) changed in substance.
  2. The diagram now contradicts ADR 0016 or ADR 0014 (e.g., implying a
     third group, or implying the design-agreement/work-plan-close gates
     moved).
  3. The consistency checker regresses beyond the 2 pre-existing, expected
     failures.
  4. A persona name is missing its group assignment.

Why each does not occur:
  1. Read the full "Core personas" section (lines 83-201 post-edit) after
     the change: Planner, Specifier, Implementer, Reviewer, Arbiter, and
     Deterministic Tool all show their original Responsibilities/Inputs/
     Outputs/Done when/Must not text, byte-for-byte unchanged from the
     pre-edit file — only the diagram section above "## Core personas" was
     replaced.
  2. The redrawn diagram keeps exactly the same node sequence as the
     original (Planner -> Specifier -> DESIGN AGREEMENT -> Implementer ->
     Preflight -> Reviewer -> Arbiter -> WORK PLAN CLOSE -> Deterministic
     Tool), only adding group-boundary dividers and handoff labels around
     the existing flow; it does not add, remove, or reorder a gate. Backlog
     is drawn as a pre-loop step producing the trigger for Planner, not as a
     third group, matching ADR 0016 Rule 1's explicit statement that Backlog
     "carries no persona of its own."
  3. Ran the checker before (2 failures) and after (2 failures, identical
     text) this edit — see Result above.
  4. The grep above matches all five persona names with an explicit group
     line for each.
```
