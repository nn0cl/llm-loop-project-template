# LISS-0021: Update the collaboration loop for backlog-gated, non-blocking, two-group execution

## Metadata

- Local issue ID: LISS-0021
- GitHub issue: none
- Status: proposed
- Phase: process-only
- Type: architecture
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/ai-human-scheme-loop-update

## Summary

- Contract file: `docs/collaboration/ai-human-scheme.md` (governed by ADR
  0006).
- Revise "The Loop" diagram and surrounding prose to show:
  - the Director's approval moving to the backlog-item level (not a
    per-work-plan blocking dialogue);
  - the Design & Review group producing the plan, specs, and design
    agreement autonomously after backlog approval;
  - the handoff to the Implementation group (self-reviewed
    Red/Green/Refactor per issue, Preflight, then handoff back);
  - the work-plan-level Reviewer pass and Director close, explicitly marked
    as non-blocking across concurrent work plans (multiple work plans may be
    mid-loop or awaiting close at once);
  - the intervention channel: a Director chat message into either group's
    session gates that specific in-flight item to per-step human approval
    until a resolving instruction, without affecting other concurrent work.
- Update "Human agreement (Director)" and "Decision Gates" sections to state
  the backlog-item gate and the non-blocking multi-work-plan behavior
  explicitly, and to cross-reference ADR 0016.
- Do not change the Reviewer's three constraints, the Implementer's
  self-review requirements, or the three invariants — those are unchanged by
  ADR 0016.

## Acceptance Notes

- The Loop diagram shows the backlog gate as the entry point and shows two
  or more work plans able to be in flight without one blocking another.
- Prose states the intervention channel's effect precisely: gates the
  specific item, not the whole group; resolves only on Director instruction;
  does not silently expire.
- No wording implies the design-agreement or work-plan-close gates are
  removed — only their blocking/serialization behavior changes.

## Dependencies

- Parent: WP-0002
- Depends on: LISS-0019
- Blocks: none
- Related: LISS-0020, LISS-0025

## Decisions Not Settled by the Design Agreement

- None known.

## Context

- Included: `docs/collaboration/ai-human-scheme.md`, ADR 0016 (from
  LISS-0019), the Director's intervention-semantics clarification recorded
  in the design agreement's Settled Ambiguities.
- Omitted: n/a
- Assumptions: none

## AI Planning Records

### AIP-0021-001

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
- Intended scope: rewrite one diagram and its surrounding prose in one
  contract file; no code changes
- Estimated token range: 2,500–6,000
- Estimated token midpoint: 4,000
- Token metric: output tokens for the revised sections
- Estimation basis: the section is self-contained (~120 lines) in the
  current file
- Assumptions: none
- Confidence: medium — the diagram needs to represent concurrency (multiple
  in-flight work plans), which the current ASCII format was not designed for
- Revises: none
- Revision reason: n/a
- Superseded by: none

## References

- `docs/collaboration/ai-human-scheme.md`
- `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`

## Work Notes

- 

## Verification

- `scripts/check-contract-consistency.py`
- Read-through against ADR 0016's Decision section.
