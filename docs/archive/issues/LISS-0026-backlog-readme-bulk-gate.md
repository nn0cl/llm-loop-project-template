# LISS-0026: State backlog-item approval as the bulk design-phase gate

## Metadata

- Local issue ID: LISS-0026
- GitHub issue: none
- Status: done
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

- 2026-08-18 (Implementer, Implementation group, first standing session):
  added Rules 6 ("Bulk design-phase gate") and 7 ("Compliance boundary") to
  `docs/backlog/README.md`, cross-referencing ADR 0016 Rules 2 and 5 and
  `docs/collaboration/design-agreement.md`'s new "Backlog-item-level
  agreement" and "Reopening the agreement" sections rather than duplicating
  their content.
- **No AI work trace under `docs/collaboration/traces/` for this issue.**
  `docs/backlog/README.md` is explicitly not a contract file under
  `docs/collaboration/prompt-instruction-change-control.md`'s Agent
  Operating Contract Files list (it lives under `docs/backlog/`, not
  `docs/collaboration/*.md` or any other listed path), so ADR 0006's
  Traceability Rule does not apply. Normal self-review (below) plus the
  later work-plan-level Reviewer pass applies to this issue, same as any
  non-contract-file change. This is stated here explicitly, per this
  session's operating instructions, so a later reader does not wonder why
  LISS-0026 has no trace while LISS-0020 through LISS-0025 each have one.

### Self-Review (Implementer, design note -> drafted change)

Per `docs/templates/self-review.md`, short form.

```text
Phase / finding: Architecture Path design note -> drafted change to
  docs/backlog/README.md (Rules 6-7)

Command run: python3 scripts/check-contract-consistency.py
Result: contract consistency: all checks passed

Risks considered:
  1. The bulk-gate rule or the compliance boundary is duplicated in prose
     rather than cross-referenced, contradicting the Acceptance Notes'
     "cross-references rather than duplicated prose" requirement.
  2. A cross-referenced path does not actually exist or does not contain
     the claimed section (e.g. "Backlog-item-level agreement" in
     design-agreement.md, added by LISS-0025 earlier in this same pass).
  3. The compliance-boundary rule is stated as a one-time check rather than
     a standing constraint, understating ADR 0016 Rule 5.

Why each does not occur:
  1. Rule 6 states the gate in one sentence and points to "ADR 0016 Rule 2
     and docs/collaboration/design-agreement.md's 'Backlog-item-level
     agreement'" rather than restating that subsection's content; Rule 7
     states the boundary in one sentence and points to "docs/collaboration/
     design-agreement.md's 'Reopening the agreement'" and "ADR 0016 Rule 5"
     rather than restating them.
  2. `docs/collaboration/design-agreement.md`'s "Backlog-item-level
     agreement" subsection was added by this same session's LISS-0025 work,
     landed immediately before this issue in the Recommended Order
     sequence, and confirmed present by this session's own read-through
     during LISS-0025's self-review; ADR 0016 Rules 2 and 5 were confirmed
     present by direct reading of the ADR file at the start of this
     work-plan pass.
  3. Rule 7's text reads "a standing constraint, not satisfied implicitly
     or checked once and forgotten," matching ADR 0016 Rule 5's own
     wording ("a standing constraint that applies continuously... not a
     checkbox verified once per item") in substance.
```
