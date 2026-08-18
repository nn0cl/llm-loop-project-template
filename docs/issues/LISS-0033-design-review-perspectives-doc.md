# LISS-0033: Create the living design & review perspectives document

## Metadata

- Local issue ID: LISS-0033
- GitHub issue: none
- Status: ready
- Phase: phase-0-design (new contract document, no application code)
- Type: process-document
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/design-review-perspectives-doc

## Summary

- Create `docs/collaboration/design-review-perspectives.md` (a new
  ADR-0006 contract file), organized by named, generalizable *perspective*
  (not chronologically by finding), seeded with at least 3 real
  perspectives distilled from this repository's own actual
  `docs/collaboration/reviews/*.md` history — read a representative sample
  (at minimum the 2026-08-02 contract-consistency review series and the
  2026-08-18 WP-0002/WP-0003 reviews) and generalize genuine findings from
  them, not invented examples. Each entry states: the perspective, when to
  apply it, and the originating finding(s)/review(s) it was distilled from
  (linked). Explicitly states how this document differs from
  `docs/collaboration/findings-reuse.md` (generalized perspectives vs.
  per-finding issue tracking) without duplicating its lifecycle rules.
- Wire the new document into required reading:
  `docs/architecture/agent-quickstart.md`'s "Required Area Documents" and
  `CLAUDE.md`'s reading list, alongside
  `docs/collaboration/source-code-quality.md`, per item-0006's own
  "becomes required reading during design intake" requirement.

## Acceptance Notes

- At least 3 real, generalizable perspectives, each traced to a real
  finding/review record (link, not invented).
- Document structure supports refinement (merging new evidence into an
  existing perspective) rather than only chronological appending — state
  this explicitly as the document's own editing rule, near its top.
- No duplication of `findings-reuse.md`'s lifecycle
  (`proposed -> accepted -> in_progress -> resolved -> closed`) — this
  document is not a tracker.
- `docs/architecture/agent-quickstart.md` and `CLAUDE.md` both list the new
  document.
- `scripts/check-contract-consistency.py` passes (new file's references
  resolve; it is correctly picked up by the mirror/reference checks the
  script runs).
- AI work trace(s) exist for every contract file touched by this issue
  (the new document itself, and `CLAUDE.md`).
- Self-review recorded (full form).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md
- Depends on: LISS-0032 (cites ADR 0018 by number)
- Blocks: none
- Related: `docs/collaboration/findings-reuse.md`,
  `docs/collaboration/source-code-quality.md`

## Decisions Not Settled by the Design Agreement

- Exact wording/selection of which 3+ perspectives to seed is left to the
  Implementer's judgment, bounded by "real, traced to actual review
  records" — this is execution-level curation, not a planning ambiguity.

## Context

- Included: ADR 0018 (once LISS-0032 lands), `DA-2026-08-18-05`,
  `docs/collaboration/findings-reuse.md`,
  `docs/collaboration/source-code-quality.md`,
  `docs/architecture/agent-quickstart.md`, `CLAUDE.md`, a representative
  sample of `docs/collaboration/reviews/*.md`.
- Omitted: every review record in full detail — read for the generalizable
  lesson, not reproduced verbatim.
- Assumptions: LISS-0032's ADR exists and is stable before this issue
  starts (enforced by the dependency above).

## AI Planning Records

### AIP-0033-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Sonnet 5 via Claude Code, Design & Review
    group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: not surfaced in this environment
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Implementation-group agent, Architecture Path,
  one new document plus two required-reading-list edits
- Compatibility state: Verified — confirmed via directory listing that
  `docs/collaboration/reviews/` has a real, substantial history to distill
  from (2026-08-02 and 2026-08-18 series)
- Intended scope: `docs/collaboration/design-review-perspectives.md`
  (new), `docs/architecture/agent-quickstart.md`, `CLAUDE.md`
- Estimated token range: 6,000-14,000 tokens
- Estimated token midpoint: 9,000
- Token metric: approximate output tokens, dominated by reading review
  history and drafting the new document
- Estimation basis: comparable to a mid-sized new contract document plus
  two small wiring edits
- Assumptions: single execution attempt
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md`
  (`DA-2026-08-18-05`)
- `docs/collaboration/findings-reuse.md`

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0006-*.md`'s promotion. Dispatched to the
  Implementation group together with LISS-0032.

## Verification

- Pending Implementation-group execution.
