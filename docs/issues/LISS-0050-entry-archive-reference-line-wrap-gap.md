# LISS-0050: `check_no_archive_reference_from_entry` misses a reference split across a hard line-wrap

## Metadata

- Local issue ID: LISS-0050
- GitHub issue: none
- Status: in_progress
- Phase: docs-only
- Type: review-finding
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: Design & Review group (Planner) — fix made directly,
  confirmed by a separate-context Reviewer.
- Related branch: process/item-0012-remaining-facets (same shared branch;
  no dedicated feature branch — a fix answering a WP-0016 Reviewer finding
  before that work plan's own Director close)

## Summary

- `docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`
  (Falsification Search #6) found that `check_no_archive_reference_from_entry`
  scans line-by-line only, with no cross-line joining. A genuine,
  file-shaped `docs/archive/...` reference split across a hard line-wrap
  — this repository's own dominant prose convention, observed in every
  document read for that review — is completely invisible to the check: a
  false negative in exactly the scenario ADR 0020 Rule 1 and this check
  exist to catch.
- Latent today: no Entry document currently contains such a reference, so
  this was a no-op at the time of the finding — same disposition as
  LISS-0044 and LISS-0049.

## Acceptance Notes

- `check_no_archive_reference_from_entry` also scans each adjacent raw
  line pair, concatenated with no inserted separator, in addition to the
  existing per-line scan — catching a reference split across exactly one
  line-wrap.
- A pair where either individual line already matched on its own is
  skipped in the cross-line pass, so a same-line reference is not
  double-reported.
- A cross-line match is reported with a line range (`N-N+1`) rather than
  a single line number, since the reference genuinely spans two source
  lines.
- Verified with real command output, both directions:
  - Negative (the exact case the finding constructed): a two-line split
    (`` "  point at `docs/archive/" `` / `` "issues/LISS-0005-foo.md` for
    the historical record." ``) appended to `agent-quickstart.md` is now
    correctly flagged, citing the reconstructed path and the line range.
  - Positive (same-line detection still works, not broken by the fix): a
    same-line reference (`docs/archive/some-test-path.md`) is still
    flagged with a precise single line number, and only once (not
    duplicated by the cross-line pass).
- Separate-context Reviewer confirmation obtained (this fix was made
  directly by the Design & Review group, so it cannot also confirm
  itself).

## Review Finding Record

- Originating review record:
  `docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`
  (Falsification Search #6; required as a condition of that review's own
  Approval)
- Affected artifact: `scripts/check-contract-consistency.py`'s
  `check_no_archive_reference_from_entry` function.
- Failure scenario: a future Entry-document edit references a specific
  `docs/archive/` file, but the reference happens to be split across a
  hard line-wrap during normal prose editing; the check silently misses
  it, and the forbidden reference lands undetected.
- Reviewer grounds: independently constructed a realistic two-line split
  matching this repository's own prose-wrapping convention, confirmed
  neither line matches the compiled regex on its own.
- Dispute raised by: none — a real, reproduced finding, not disputed.
- Arbiter decision record: none — not a deadlock; resolved directly.
- Changed files: `scripts/check-contract-consistency.py`.
- Deterministic verification output: see Acceptance Notes above and this
  issue's own Verification section.
- Separate Reviewer closure record: pending — dispatched as a fresh agent.

## Dependencies

- Parent: none
- Depends on: none — actionable immediately.
- Blocks: none
- Related: `docs/work-plans/WP-0016-drift-prevention-entry-docs-and-ci-checks.md`,
  `docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`,
  `docs/issues/LISS-0049-retired-terminology-substring-false-positive.md`
  (fixed in the same correction cycle)

## Decisions Not Settled by the Design Agreement

- None — the fix extends an existing check's scan logic within WP-0016's
  own already-accepted scope; no new architecture boundary crossed.

## Context

- Included: the WP-0016 review record's Falsification Search #6 in full,
  `check_no_archive_reference_from_entry`'s actual pre-fix and post-fix
  code.
- Omitted: LISS-0049 (fixed alongside this issue, but recorded as its own
  separate finding since it concerns a different function).
- Assumptions: the fix handles exactly a one-line-wrap split (two
  adjacent lines); a reference split across three or more lines is not
  handled and is not claimed to be — recorded as a Deferred Question
  below rather than silently assumed covered.

## AI Planning Records

Not required — planning size `S`.

## References

- `docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`
- `scripts/check-contract-consistency.py`

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should the check also handle a reference split across three or more lines? | Not built now — no realistic case observed in this repository's actual prose (paths are short enough that a two-line split already covers the practical wrapping width); revisit only if a real three-line split is ever found. |

## Work Notes

- 2026-08-19 — Design & Review group (Planner): opened this issue directly
  from the WP-0016 Reviewer's own required condition of Approval, and
  resolved it in the same session — cross-line-pair scanning added,
  verified against both the exact constructed negative case (now caught)
  and the pre-existing same-line positive case (still caught, not
  duplicated) with real command output. `Status: in_progress`, pending
  separate-context Reviewer confirmation under Minor Fix Path.

## Verification

- Command run: `python3 scripts/check-contract-consistency.py`
- Negative case (the exact finding, now caught):
  ```
  $ printf '  point at `docs/archive/\nissues/LISS-0005-foo.md` for the historical record.\n' >> docs/architecture/agent-quickstart.md
  $ python3 scripts/check-contract-consistency.py
  entry archive reference:
    docs/architecture/agent-quickstart.md:228-229 references a specific docs/archive/ file ('docs/archive/issues/LISS-0005-foo.md'), split across a line wrap -- ...
  contract consistency: 1 failure(s)
  ```
  (test line removed immediately after, file restored to its exact
  pre-test content, confirmed via `diff`)
- Positive case (same-line detection unaffected):
  ```
  $ printf '\ntest: docs/archive/some-test-path.md\n' >> docs/architecture/agent-quickstart.md
  $ python3 scripts/check-contract-consistency.py
  entry archive reference:
    docs/architecture/agent-quickstart.md:229 references a specific docs/archive/ file ('docs/archive/some-test-path.md') -- ...
  ```
  (one failure, precise single line number, not duplicated by the
  cross-line pass; test line removed, file restored, confirmed via `diff`)
- Final clean re-run after removing all synthetic artifacts:
  `contract consistency: all checks passed`, exit 0.
- Separate-context Reviewer confirmation: pending — dispatched as a fresh
  agent, per Minor Fix Path.
