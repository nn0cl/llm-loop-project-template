# Design Agreement: Process ADR for Loop Ledgers

## Identity

- Agreement ID: DA-2026-08-19-02
- Date: 2026-08-19
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0002-adr-loop-ledgers.md` (`Status: promoted`):
promote the existing docs-first loop-ledger rules (spike cases, backlog
promotion, loop-settings, post-hoc audit, findings-must-apply — all landed
in v2.3.0, per item-0001's now-Approved review) into a single accepted
process ADR, so adopters can cite one decision record instead of five
separate collaboration documents with no unifying ADR.

## Spike Result

- Confirmed next-free ADR number: `0019` (`ls docs/architecture/adr/`
  currently runs `0001`-`0018`, contiguous, per WP-0004/WP-0006/WP-0007's
  already-merged and reconciled work).
- Read ADR 0012 (`review-issues-minor-fix-and-model-routing`) and ADR 0015
  (`review-cost-discipline`) in full: neither states the spike/backlog/
  loop-settings/post-hoc-audit/findings-must-apply rules this item asks to
  formalize — ADR 0012 governs the review-finding *lifecycle*
  (`proposed -> ... -> closed`), which `findings-reuse.md` cites and this
  new ADR should cite in turn, not restate or supersede. No numbering or
  supersession conflict found against ADR 0012-0015 or ADR 0016-0018 (the
  three most recently landed ADRs, all process/topology decisions with no
  overlapping subject matter).
- The five source documents
  (`docs/spike/README.md`, `docs/backlog/README.md`,
  `docs/collaboration/loop-settings.md`,
  `docs/collaboration/post-hoc-audit.md`,
  `docs/collaboration/findings-reuse.md`) are each already-accepted,
  in-force collaboration docs (not proposals) — this ADR's job is to state,
  once, that these five ledgers are an accepted architectural decision and
  point at each as the source of truth for its own operational detail, the
  same pattern ADR 0016 uses for `cross-session-messaging.md` (an ADR
  states the decision; the collaboration doc carries the operational
  detail).

## Scope

- In scope:
  - A new ADR (`0019`) stating: the five ledgers (spike, backlog,
    loop-settings, post-hoc-audit, findings-must-apply) are an accepted,
    unified process decision; each ledger's full detail lives in its own
    named collaboration document, not restated in the ADR; no existing
    ADR 0012-0015 or ADR 0016-0018 rule is superseded or reworded.
  - This ADR is not an ADR-0006 contract file (ADRs are excluded from that
    list) — no trace required.
- Explicitly out of scope:
  - Rewriting any of the five source documents' own content.
  - Any change to ADR 0012-0015 or ADR 0016-0018.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Write ADR 0019 | Implementer | Architecture Path | States the five-ledger decision as accepted; cites each source document by path rather than restating its content; states explicitly it supersedes nothing in ADR 0012-0015/0016-0018 | read-through against this Direction |
| 2 | Self-review | Implementer | Architecture Path | Short-form self-review (single new document, no cross-file edits) | self-review record in LISS-0038 Work Notes |
| 3 | Preflight | Implementer / deterministic tool | Architecture Path | `pass` recorded | Preflight section in WP-0010 |
| 4 | Work-plan-level Reviewer pass | Reviewer (Design & Review group, separate context) | Architecture Path | Confirms no supersession/numbering conflict and no restated content drifting from its source | review record under `docs/collaboration/reviews/` |

Sequencing: Task 1 blocks 2. Task 2 blocks 3. Task 3 blocks 4.

## Specifications

- None. Process/governance ADR; no application specification.

## Boundaries

- No supersession of ADR 0012-0015 or ADR 0016-0018.
- No change to the five source collaboration documents' own content.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` until the
  Director's own work-plan-close action.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does this ADR restate each ledger's operational detail, or point at it? | Points at it — mirrors ADR 0016's own pattern of stating the decision and pointing at `cross-session-messaging.md` for detail, avoiding a second, driftable copy of content the source document already owns. | Design & Review group (Planner) |
| ADR number | `0019`, confirmed as next-free at spike time; Implementer re-confirms at execution time per the same defensive pattern used for ADR 0017/0018. | Design & Review group (Planner) |

## Deferred Questions

None.

## Verification

- `ls docs/architecture/adr/` re-confirmed at execution time.
- Read-through against ADR 0012-0015/0016-0018 for no supersession
  conflict.
- Work-plan-level Reviewer approval.

## Falsification Criteria

- The new ADR restates a source document's operational content instead of
  pointing at it, creating a second copy that can drift.
- The new ADR silently supersedes or contradicts ADR 0012-0015 or
  0016-0018.
- The ADR number collides with a concurrently in-flight work plan's own
  claim, unflagged.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0002-adr-loop-ledgers.md`, `Status: promoted`,
      Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
