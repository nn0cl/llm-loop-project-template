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

**Current (corrected, attempt 2) design** — the first attempt (a
no-separator concatenation of every adjacent line pair) was reviewed and
Rejected; see "Attempt 1 (rejected)" and Work Notes below for the full
history, preserved per Invariant 2.

- `check_no_archive_reference_from_entry` also scans each adjacent raw
  line pair, joined with the real newline preserved, for a match of
  `ENTRY_ARCHIVE_BACKTICKED_SPAN` (a `docs/archive/...` file reference
  still bounded by an opening and a closing backtick) — catching a
  reference split across exactly one line-wrap.
- Requiring the backtick delimiters — this repository's own established
  convention for every specific-file reference — is what avoids flagging
  a bare, legitimate abstract mention of the directory followed by
  unrelated next-line prose (the false positive Attempt 1 produced).
- A match fully contained within one line (no embedded newline in its own
  span) is skipped in the cross-line pass — it was already reported by
  the per-line scan; a match that does contain the newline is a genuine
  cross-line split and is always reported, independent of whether either
  line also carries its own separate, unrelated standalone match (fixing
  Attempt 1's under-suppression bug).
- A cross-line match is reported with a line range (`N-N+1`) rather than
  a single line number, since the reference genuinely spans two source
  lines.
- Verified with real command output, all three of the Reviewer's own
  adversarial cases from the Attempt-1 rejection, reconstructed against
  the corrected code:
  - Positive (backtick-delimited split, Reviewer's own wording): caught,
    reports the reconstructed path and line range.
  - False-positive probe (bare mention + unrelated next-line prose, no
    backticks): correctly **not** flagged — `contract consistency: all
    checks passed`.
  - Under-suppression probe (one same-line match plus one separate
    cross-line match on the same line pair): **both** now correctly
    reported as two distinct failures.
- Separate-context Reviewer confirmation obtained (this fix was made
  directly by the Design & Review group, so it cannot also confirm
  itself).

### Attempt 1 (rejected) — preserved for the record

The original fix concatenated every adjacent raw line pair with no
separator and re-scanned with the plain `ENTRY_ARCHIVE_REFERENCE` regex,
skipping a pair if either individual line already had its own match. The
Reviewer (`docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`)
independently found this both introduced a new false positive (a bare,
docstring-permitted abstract mention of `docs/archive/` followed by
unrelated next-line prose starting with a dotted token was wrongly
flagged) and had a silent under-suppression bug (a line carrying both its
own standalone match and a separate cross-line-continuing match had the
second, genuine violation silently dropped by the pair-skip condition).
**Rejected.** See that review record's own "LISS-0050" section for the
full falsification detail.

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
- Separate Reviewer closure record: Attempt 1 —
  `docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`
  (Rejected, two reproduced defects). Attempt 2 (this corrected fix):
  pending — dispatched as a fresh agent.

## Dependencies

- Parent: none
- Depends on: none — actionable immediately.
- Blocks: none
- Related: `docs/work-plans/WP-0016-drift-prevention-entry-docs-and-ci-checks.md`,
  `docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`,
  `docs/issues/LISS-0049-retired-terminology-substring-false-positive.md`
  (fixed in the same correction cycle),
  `docs/issues/LISS-0051-retired-terminology-punctuation-edged-term-gap.md`

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
  resolved it in the same session (Attempt 1) — cross-line-pair scanning
  added, verified against both the exact constructed negative case (now
  caught) and the pre-existing same-line positive case (still caught, not
  duplicated) with real command output. `Status: in_progress`, pending
  separate-context Reviewer confirmation under Minor Fix Path.
- 2026-08-19 — Design & Review group (Planner): Attempt 1 was **Rejected**
  by a separate-context Reviewer, which independently found and
  reproduced two real defects (a new false positive on a bare abstract
  mention followed by unrelated prose; a silent under-suppression bug
  when a line carries both a standalone and a separate cross-line match).
  Applied a corrected design (Attempt 2, this issue's current Acceptance
  Notes): backtick-delimited cross-line matching, using this repository's
  own convention that every specific-file reference is backtick-bounded,
  instead of naive no-separator concatenation. Verified against all three
  of the Reviewer's own adversarial cases, reconstructed identically —
  positive case still caught, false-positive probe now correctly clean,
  under-suppression probe now correctly reports both violations.
  `Status: in_progress`, pending a fresh separate-context Reviewer
  confirmation of Attempt 2.

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

### Attempt 2 (corrected) verification — the Reviewer's own three adversarial cases, reconstructed

```
$ printf 'See the retired snapshot under `docs/archive/adr/\n0007-old-decision.md` for the superseded rationale.\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
entry archive reference:
  docs/architecture/agent-quickstart.md:228-229 references a specific docs/archive/ file ('docs/archive/adr/0007-old-decision.md'), split across a line wrap -- ...
(restored; diff confirmed identical)

$ printf 'This document explains the archive mechanism in the abstract; see docs/archive/\nconfig.py contains unrelated local script settings, not an archive pointer.\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
(no false positive; restored; diff confirmed identical)

$ printf 'First see `docs/archive/known.md` for background, and also `docs/archive/\nnewer.md` for the follow-up update.\n' >> docs/architecture/agent-quickstart.md
$ python3 scripts/check-contract-consistency.py
references:
  docs/architecture/agent-quickstart.md:228 names 'docs/archive/known.md', which does not exist
entry archive reference:
  docs/architecture/agent-quickstart.md:228 references a specific docs/archive/ file ('docs/archive/known.md') -- ...
  docs/architecture/agent-quickstart.md:228-229 references a specific docs/archive/ file ('docs/archive/newer.md'), split across a line wrap -- ...
contract consistency: 3 failure(s)
(both violations now reported; restored; diff confirmed identical)

$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
$ git status --short
(clean)
```

- Separate-context Reviewer confirmation: pending — dispatched as a fresh
  agent, per Minor Fix Path.
