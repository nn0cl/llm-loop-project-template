# LISS-0021: Update the collaboration loop for backlog-gated, non-blocking, two-group execution

## Metadata

- Local issue ID: LISS-0021
- GitHub issue: none
- Status: done
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

- 2026-08-18 (Implementer, Implementation group, first standing session):
  rewrote "The Loop" diagram and surrounding prose in
  `docs/collaboration/ai-human-scheme.md` to show the backlog-item gate as
  entry point, the Design & Review / Implementation group boundary with
  `SendMessage` handoff labels, and cross-referenced
  `docs/collaboration/cross-session-messaging.md` (LISS-0022, not yet
  created at this point in the sequence — expected forward reference).
  Added "Non-blocking concurrency across work plans" and "Intervention
  channel" subsections stating ADR 0016 Rules 3 and 4 precisely. Updated
  "Human agreement (Director)" to state the backlog-item gate replaces the
  live per-work-plan dialogue turn, and that the close does not block other
  concurrent work plans. Added a paragraph to "Decision Gates" distinguishing
  a reopening request (loop-initiated) from Director intervention
  (Director-initiated) and stating reopening does not block unrelated
  concurrent work. Did not touch the Reviewer's three constraints, the
  Implementer's self-review requirements, or the Three Invariants sections —
  confirmed by reading each after the edit.
- Trace: `docs/collaboration/traces/2026-08-18-liss-0021-ai-human-scheme-loop-update.md`.
- 2026-08-18, Preflight-driven follow-up (Implementer, same session): the
  work-plan-level Preflight grep sweep (per WP-0002's Verification Plan)
  found the "Roles > Director > Responsibilities" list (lines 26-33
  pre-fix) still stated "build the detailed plan with the Planner through
  dialogue" and "reach the design agreement... on the record" with no
  qualification, which could be misread as still requiring a live
  per-work-plan dialogue turn in every case. Added a cross-reference to ADR
  0016 Rule 2 and to `design-agreement.md`'s "Backlog-item-level agreement"
  directly in that list, without removing the live-dialogue path itself
  (still valid when the Director chooses to run it). Re-ran
  `scripts/check-contract-consistency.py`: `contract consistency: all
  checks passed`.

### Self-Review (Implementer, design note -> drafted change)

Per `docs/templates/self-review.md`, short form (per this session's explicit
instruction, notwithstanding this issue's `M` planning size).

```text
Phase / finding: Architecture Path design note -> drafted change to
  docs/collaboration/ai-human-scheme.md (Loop diagram, Human agreement,
  Decision Gates)

Command run: python3 scripts/check-contract-consistency.py
Result:
  references:
    docs/architecture/adr/0016-...md:192 names 'docs/collaboration/cross-session-messaging.md', which does not exist
    docs/architecture/adr/0016-...md:284 names 'docs/collaboration/cross-session-messaging.md', which does not exist
    docs/collaboration/ai-human-scheme.md:91 names 'docs/collaboration/cross-session-messaging.md', which does not exist
    docs/collaboration/ai-human-scheme.md:186 names 'docs/collaboration/cross-session-messaging.md', which does not exist
  contract consistency: 4 failure(s)
(All 4 are the same kind of failure — a reference to LISS-0022's own
  not-yet-created target file. 2 pre-existing from ADR 0016, 2 new from this
  file's own new cross-references. No other failure category. Expected to
  drop to the original 2 once LISS-0022 creates the file next.)

Risks considered:
  1. The diagram omits one of the four required elements: backlog gate as
     entry point, autonomous Design & Review production after approval,
     handoff to Implementation group, non-blocking Reviewer/close across
     concurrent work plans.
  2. The intervention-channel prose states an effect other than "gates the
     specific item, not the whole group; resolves only on Director
     instruction; does not silently expire" (Acceptance Notes' exact
     requirement).
  3. Wording implies the design-agreement or work-plan-close gates are
     removed, rather than only their cadence/blocking behavior changing.
  4. The Reviewer's three constraints, the Implementer's self-review
     requirements, or the Three Invariants sections were altered.
  5. The consistency checker regresses with a failure category other than
     the expected not-yet-created cross-session-messaging.md reference.

Why each does not occur:
  1. Read-through of the redrawn diagram: "Backlog item approved" is the
     first line; "Planner builds the plan... no further live Director turn
     required per work plan" appears directly under the Design & Review
     group divider; a "handoff: design agreement recorded -> SendMessage"
     line separates the two groups; the "Non-blocking concurrency across
     work plans" subsection states work plans can be in flight
     concurrently without one blocking another. All four present.
  2. The "Intervention channel" subsection's four bullets restate, near
     verbatim, ADR 0016 Rule 4's own four effects (continues development-
     loop/review work on that item; each subsequent step requires explicit
     approval; persists until a resolving instruction; other concurrent
     work in either group unaffected) — matching the Acceptance Notes'
     exact wording requirement.
  3. "Human agreement (Director)" explicitly states "There is no per-phase
     and no per-issue human gate... The Director's intervention channel...
     is not a third standing gate" and "this checkpoint... does not block
     the Design & Review group's or the Implementation group's other
     concurrently in-flight work — only the start of that work plan's own
     next direction waits on it" — the two gates are described as changed
     in cadence/blocking behavior only, never as removed.
  4. Read the "Three constraints on the Reviewer's approval" section
     (unchanged: context separation, deterministic precondition,
     falsification burden, byte-for-byte), the "Self-review (Implementer,
     inside a work plan)" section (unchanged), and "The Three Invariants"
     section (unchanged) after the edit; none were in either Edit call's
     old_string/new_string diff.
  5. Ran the checker after the edit (output above): the only failure
     category present is the reference check, and every listed failure
     names `docs/collaboration/cross-session-messaging.md`, the expected
     not-yet-created file. No new failure category (e.g. ADR range,
     mirror-parity) appeared.
```
