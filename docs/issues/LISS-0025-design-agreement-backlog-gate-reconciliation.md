# LISS-0025: Reconcile the design-agreement gate with backlog-level authorization

## Metadata

- Local issue ID: LISS-0025
- GitHub issue: none
- Status: review
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

- 2026-08-18 (Implementer, Implementation group, first standing session):
  revised "What the design phase produces" points 1-2 in
  `docs/collaboration/design-agreement.md` to allow the Director's
  direction/plan-building to happen once at backlog-item approval. Added
  "Backlog-item-level agreement" under "Reaching agreement" stating backlog
  approval can satisfy the Director's agreement statement (scoped to what
  the item states; out-of-scope work needs a reopening request; the AI's
  own executability statement is still made fresh against the actual plan).
  Added "Intervention-gated provisional records" stating design-agreement
  content touched during a Director-gated item is provisional until a
  resolving instruction. Did not touch the two-gate structure, the "What
  the record must contain" field list, or "Reopening the agreement"'s
  trigger list.
- Trace: `docs/collaboration/traces/2026-08-18-liss-0025-design-agreement-backlog-gate-reconciliation.md`.
- 2026-08-18, Preflight-driven follow-up (Implementer, same session): the
  work-plan-level Preflight grep sweep for the superseded ADR 0014 clause 5
  phrasing ("the next work plan does not start without [close]") found
  "Closing a work plan"'s closing paragraph ("The next work plan does not
  start without this") unqualified — read in isolation, without ADR 0016's
  own "Supersession, precisely" table nearby, it could be misread as the
  pre-ADR-0016 global blocking model rather than scoped to this specific
  work plan's own successor. Reworded to state explicitly that this is
  about the one work plan being closed and its own direct successor, cited
  ADR 0016 Rule 3 by name, and stated unrelated concurrent work plans are
  unaffected. Re-ran `scripts/check-contract-consistency.py`: `contract
  consistency: all checks passed`.

### Self-Review (Implementer, design note -> drafted change)

Per `docs/templates/self-review.md`, short form (per this session's explicit
instruction, notwithstanding this issue's `M` planning size).

```text
Phase / finding: Architecture Path design note -> drafted change to
  docs/collaboration/design-agreement.md (backlog-item-level agreement,
  intervention-gated provisional records)

Command run: python3 scripts/check-contract-consistency.py
Result: contract consistency: all checks passed

grep -n "Silence is not agreement" docs/collaboration/design-agreement.md
Result:
  46:If the AI cannot make the second statement, the design phase is not finished,
  47-regardless of the Director's readiness to proceed. Silence is not agreement,
  67:This does **not** weaken "Silence is not agreement" above. Backlog-item

Risks considered:
  1. The new rule states or implies backlog-item approval is a blanket
     delegation rather than scoped to the item's stated content.
  2. "Silence is not agreement" is weakened, removed, or contradicted.
  3. The "Reopening the agreement" trigger list is altered.
  4. The two-gate structure (design agreement, work-plan close) or the
     record template's required fields section changes.
  5. The intervention-gated provisional rule states an effect stronger than
     ADR 0016 Rule 4 actually specifies (e.g., "blocked" rather than
     "provisional, pending resolving instruction").

Why each does not occur:
  1. The "Backlog-item-level agreement" subsection states explicitly: "it
     is scoped strictly to what the backlog item states. A work plan that
     goes beyond the approved backlog item's stated scope is not covered by
     backlog-item-level agreement; it requires its own reopening request."
  2. Original sentence "Silence is not agreement, and neither is proceeding
     without objection" (line 47) is unedited at its original location; the
     new subsection additionally states this in its own words: "Backlog-item
     approval is itself an explicit, on-the-record act by the Director —
     not silence, and not proceeding without objection."
  3. Read "Reopening the agreement" (now starting at line 125) after the
     edit: the six original bullets (decision the agreement does not
     settle; boundary crossed; deferred question's condition reached;
     verification contradicts an assumption; Arbiter finds neither side
     grounded; falsification criterion met) are present, unedited, in the
     original order.
  4. Read "What the record must contain" and "Closing a work plan" after
     the edit: both sections are present unedited; the edit only touched
     "What the design phase produces" (points 1-2, adding an ADR 0016
     cross-reference, not removing any of the four original numbered
     items) and added two new subsections under "Reaching agreement," not
     replacing it.
  5. The new subsection's own wording ("Any design-agreement content
     touched while that gate is active is provisional... until the
     Director's resolving instruction confirms it") matches ADR 0016 Rule
     4's stated effect exactly: "the group continues its development-loop
     and review work on that item... each subsequent step requires the
     Director's explicit approval... until the Director gives a resolving
     instruction" — a gated/provisional mode, not a halt, matching the
     Direction section's explicit refinement in `DA-2026-08-18-01`.
```
