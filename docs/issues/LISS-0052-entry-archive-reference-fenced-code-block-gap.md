# LISS-0052: `check_no_archive_reference_from_entry` misses a reference split inside a fenced code block

## Metadata

- Local issue ID: LISS-0052
- GitHub issue: none
- Status: proposed
- Phase: docs-only
- Type: review-finding
- Priority: low
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: unassigned — tracked, not immediately actionable enough to
  warrant a further correction cycle right now (see Disposition below).
- Related branch: none yet

## Summary

- `docs/collaboration/reviews/2026-08-19-liss-0050-attempt2-liss-0051-review.md`
  found that LISS-0050's corrected (Attempt 2) cross-line scan requires an
  inline single-backtick pair immediately bounding the `docs/archive/...`
  reference. A reference split across a hard line-wrap **inside a fenced
  code block** (```` ``` ````, on its own lines, not immediately adjacent
  to the path text) is invisible to both the per-line check and the
  cross-line check — neither the original per-line-only scan (before
  LISS-0050) nor either of LISS-0050's two attempts ever caught this case.
- Not a regression: the Reviewer confirmed no prior version of the check
  claimed fenced-code-block coverage; this is a real, previously
  undisclosed scope limit, now recorded rather than left implicit.

## Disposition (why this is tracked, not fixed immediately)

Unlike LISS-0044/LISS-0049/LISS-0050/LISS-0051, which were each resolved
within the same session they were found, this finding is recorded and
left open, matching the disposition WP-0014's Reviewer originally gave
LISS-0044 (approved-with-tracked-finding, resolved only when a later
concrete need arose):

- Practical exposure is narrow — an Entry document would need a fenced
  code example that itself contains a hard-wrapped `docs/archive/`
  path, a combination not present anywhere in this repository's actual
  Entry documents today.
- The correction cycle for this check has already gone through two
  rounds (LISS-0050 Attempt 1 rejected, Attempt 2 approved); a third
  immediate round risks the same kind of untested, rushed fix Attempt 1
  turned out to be. A calmer follow-up, with its own dedicated design
  intake, is the safer path for a narrow, currently-inert gap.
- No currently open work depends on this being fixed.

## Acceptance Notes (for whoever picks this up later)

- Extend `check_no_archive_reference_from_entry` (or add a third pass) to
  also scan the content of fenced code blocks (text between matching
  ```` ``` ```` delimiters) for a `docs/archive/...` reference split
  across a line wrap within the fence — using the same file-shaped-path
  regex, without requiring inline single-backtick bounding for that case
  (fence delimiters, not inline backticks, are the containing
  convention there).
- Verify with the exact case the Reviewer constructed: a `docs/archive/`
  path split across two lines inside a ` ``` ` / ` ``` ` fence in an
  Entry document.
- Also revisit the existing "3+ line split" Deferred Question already
  recorded in LISS-0050 while this area is being touched again, rather
  than opening a third overlapping issue for it.

## Review Finding Record

- Originating review record:
  `docs/collaboration/reviews/2026-08-19-liss-0050-attempt2-liss-0051-review.md`
  (LISS-0050 section, "New gap found: a reference split inside a fenced
  code block is invisible to both checks"; required as a condition of
  that section's own Approval of LISS-0050 Attempt 2)
- Affected artifact: `scripts/check-contract-consistency.py`'s
  `check_no_archive_reference_from_entry` function.
- Failure scenario: an Entry document contains a fenced code example
  whose content references a specific `docs/archive/` file, and the
  reference happens to be split across a hard line-wrap inside the
  fence; the check silently misses it.
- Reviewer grounds: independently constructed the exact fenced-code-block
  case, confirmed neither the per-line nor the cross-line pass matches
  it, pasted actual command output.
- Dispute raised by: none — a real, reproduced finding, not disputed.
- Arbiter decision record: none — not a deadlock; recorded as a tracked,
  deferred finding per the Disposition above.
- Changed files: none yet.
- Deterministic verification output: none yet — not yet actioned.
- Separate Reviewer closure record: none yet.

## Dependencies

- Parent: none
- Depends on: none — actionable whenever picked up; not blocked on future
  content.
- Blocks: none
- Related: `docs/issues/LISS-0050-entry-archive-reference-line-wrap-gap.md`,
  `docs/collaboration/reviews/2026-08-19-liss-0050-attempt2-liss-0051-review.md`

## Decisions Not Settled by the Design Agreement

- Whether to extend the existing backtick-span regex approach or use a
  dedicated fence-aware scan is left to whoever designs the fix.

## Context

- Included: the originating review's LISS-0050 "New gap found" subsection
  in full.
- Omitted: the already-tracked "3+ line split" Deferred Question in
  LISS-0050 — related but distinct; not duplicated here.
- Assumptions: none beyond what the review record states directly.

## AI Planning Records

Not required — planning size `S`.

## References

- `docs/collaboration/reviews/2026-08-19-liss-0050-attempt2-liss-0051-review.md`
- `docs/issues/LISS-0050-entry-archive-reference-line-wrap-gap.md`
- `scripts/check-contract-consistency.py`

## Work Notes

- 2026-08-19 — Design & Review group (Planner): opened this issue directly
  from the LISS-0050 (Attempt 2) review's own required condition of
  Approval, per `docs/collaboration/findings-reuse.md`'s "must change the
  system or be explicitly declined" rule. `Status: proposed` — real,
  narrow, and deliberately not actioned in this same correction cycle
  (see Disposition above); not blocking WP-0016's own close.

## Verification

- Not yet run — resolution has not started.
