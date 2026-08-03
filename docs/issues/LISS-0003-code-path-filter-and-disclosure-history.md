# LISS-0003: CODE_PATH lacks its own filter; disclosure omits the self-reference history

## Metadata

- Local issue ID: LISS-0003
- GitHub issue: N/A
- Status: resolved
- Phase: Minor Fix Path
- Type: review-finding
- Priority: low
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A
- Owner/agent: Implementer, Claude Opus 5 via Claude Code
- Related branch: process/review-issues-minor-fix-path

## Summary

- Two non-blocking observations from the Reviewer's approval of the contract
  consistency checker (round 6, `docs/collaboration/reviews/2026-08-02-contract-consistency-review-6.md`):
  `CODE_PATH`'s reference matching has no filter of its own and survives only
  because an unrelated `*` exclusion happens to cover every current case; and
  the module's "What this cannot check" disclosure doesn't mention that the
  reference checker went through three rounds of self-referential false
  positives before reaching this state.

## Acceptance Notes

- `CODE_PATH` carries an explicit filter of its own, with a comment naming the
  Reviewer's finding, so a future change to the unrelated `*` filter cannot
  silently reopen this path.
- The disclosure names the self-reference history in one line, without
  overstating what changed this round.
- No existing check's behavior changes for any real input: verified by the
  full negative-test suite and a clean-tree run before and after.

## Review Finding Record

- Originating review record:
  `docs/collaboration/reviews/2026-08-02-contract-consistency-review-6.md`
  ("Two small, non-blocking observations for whoever next touches this
  file").
- Affected artifact: `scripts/check-contract-consistency.py`.
- Failure scenario: none currently live — both are latent-risk /
  documentation-debt findings, not defects with a live instance. The Reviewer
  named them "worth doing whenever this file is next opened," explicitly not
  a condition of approval.
- Reviewer grounds: `CODE_PATH`'s soundness today is incidental (an unrelated
  filter happens to cover it), not structural — the same shape as `LICENSE`
  being an incidental casualty of round 5's `MD_LINK` fix. The disclosure is
  structurally accurate but omits operational history a future reader would
  want, given the code comments already document it.
- Dispute raised by: none.
- Arbiter decision record: not applicable — no dispute.
- Changed files: `scripts/check-contract-consistency.py`.
- Deterministic verification output: recorded in
  `docs/collaboration/reviews/2026-08-02-liss-0003-preflight.md`.
- Separate Reviewer closure record:
  `docs/collaboration/reviews/2026-08-02-liss-0003-review.md`.

## Dependencies

- Parent: none.
- Depends on: pull request #8 (merged into `main`, tagged `v1.1.0`).
- Blocks: none.
- Related: none.

## Decisions Not Settled by the Design Agreement

- None. Minor Fix Path: no specification, ADR, port, data model, dependency,
  or architecture boundary changes.

## Context

- Included: `scripts/check-contract-consistency.py`, the round-6 review
  record.
- Omitted: the rest of the contract set — unaffected by this change.
- Assumptions: the `*` filter `CODE_PATH` currently depends on is the
  post-collection guard `if not target or "*" in target or "$" in target or
  "<" in target: continue`, applied uniformly to targets gathered from both
  `MD_LINK` and `CODE_PATH`. Confirmed by reading the current source before
  writing the fix.

## AI Planning Records

N/A — planning size S, single attempt.

## References

- `docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md`
  for the Minor Fix Path this issue uses.
- `docs/architecture/adr/0013-preflight-validation-before-independent-review.md`
  for the Preflight Validation this change is submitted under.

## Work Notes

- Both findings fixed in one commit: narrow edits to the same file with no
  interaction between them.

## Verification

- See the covering trace, the Preflight record, and the Reviewer's
  approval at `docs/collaboration/reviews/2026-08-02-liss-0003-review.md`.
