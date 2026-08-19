# LISS-0049: `check_retired_terminology`'s substring match has no word-boundary safeguard

## Metadata

- Local issue ID: LISS-0049
- GitHub issue: none
- Status: closed
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
  (Falsification Search #3) found that `check_retired_terminology`'s
  matching (`if term in line:`, a plain Python substring test) has no
  word-boundary safeguard. Retiring a short or common term — the Reviewer
  tested `AI` — produces a large, indiscriminate false-positive blast
  radius: 389 failures on the Reviewer's own construction, by matching
  inside unrelated identifiers that merely happen to contain the same
  letters (`AIDE`, `AIP-0043`, and similar), not genuine uses of the
  retired term as its own word.
- Latent today: `docs/collaboration/terminology-migration.md`'s table is
  empty, so this was a no-op at the time of the finding — the same
  disposition this repository gave the structurally identical
  `RECORD_DIRS`/`docs/archive/` gap (`LISS-0044`, from WP-0014's Reviewer,
  resolved two work plans later by WP-0016 itself).

## Acceptance Notes

- `check_retired_terminology` matches each retired term with a
  word-boundary-anchored regex (`\bterm\b`, `re.escape`d), not a bare
  substring test.
- A word-boundary match still correctly flags a genuine standalone use of
  the retired term (e.g. `AI-assisted`, where `AI` is its own
  hyphen-separated token) — it only excludes a match fused into a longer
  identifier with no boundary between the retired term and its neighbors
  (`AIDE`, `AIP-0043`, `MAINTAIN`, `CONTAINS`).
- `docs/collaboration/terminology-migration.md`'s own guidance gains a
  short caution recommending a specific multi-word phrase over a
  short/common single word as the retired term, since even a
  correctly-word-boundary-matched common word will still legitimately
  flag every standalone use of it — the fix narrows false positives, it
  does not make an inherently broad term retirement painless.
- Verified with real command output, both directions:
  - Positive (still catches a genuine standalone use): retiring `AI`,
    then a scratch line containing `AI-assisted`/`AIDE`/`AIP-0043-001`/
    `AI is retired` correctly flags exactly the standalone tokens.
  - Negative, isolated (false positives eliminated): a scratch line
    containing only `AIDE integration reference. See AIP-0043-001 for
    details. MAINTAIN and CONTAINS text.` (no genuine standalone `AI`
    token) produces **zero** failures after the fix, where the original
    substring match would have flagged all four.
- Separate-context Reviewer confirmation obtained (this fix was made
  directly by the Design & Review group, so it cannot also confirm
  itself).

## Review Finding Record

- Originating review record:
  `docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`
  (Falsification Search #3; required as a condition of that review's own
  Approval)
- Affected artifact: `scripts/check-contract-consistency.py`'s
  `check_retired_terminology` function.
- Failure scenario: a future session retires a short or common term in
  `docs/collaboration/terminology-migration.md`; the next CI run produces
  a large, indiscriminate false-positive failure list from unrelated
  identifiers that merely contain the same letters, rather than genuine
  uses of the retired term.
- Reviewer grounds: independently constructed synthetic case, 389
  reproduced failures on the pre-fix code, pasted actual command output.
- Dispute raised by: none — a real, reproduced finding, not disputed.
- Arbiter decision record: none — not a deadlock; resolved directly.
- Changed files: `scripts/check-contract-consistency.py`,
  `docs/collaboration/terminology-migration.md`.
- Deterministic verification output: see Acceptance Notes above and this
  issue's own Verification section.
- Separate Reviewer closure record:
  `docs/collaboration/reviews/2026-08-19-liss-0049-liss-0050-word-boundary-and-line-wrap-fix-review.md`
  — Approved, with one required follow-up condition (a retired term
  starting/ending in punctuation can silently fail to match, or match
  only the fused case) opened as `docs/issues/LISS-0051-retired-terminology-punctuation-edged-term-gap.md`.

## Dependencies

- Parent: none
- Depends on: none — actionable immediately (does not require future
  content, unlike LISS-0044).
- Blocks: none
- Related: `docs/work-plans/WP-0016-drift-prevention-entry-docs-and-ci-checks.md`,
  `docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`,
  `docs/issues/LISS-0050-entry-archive-reference-line-wrap-gap.md` (fixed
  in the same correction cycle)

## Decisions Not Settled by the Design Agreement

- None — the fix is a narrowing of an existing check's matching logic,
  within WP-0016's own already-accepted scope; no new architecture
  boundary crossed.

## Context

- Included: the WP-0016 review record's Falsification Search #3 in full,
  `check_retired_terminology`'s actual pre-fix and post-fix code.
- Omitted: LISS-0050 (fixed alongside this issue, but recorded as its own
  separate finding since it concerns a different function).
- Assumptions: none beyond what the review record states directly.

## AI Planning Records

Not required — planning size `S`.

## References

- `docs/collaboration/reviews/2026-08-19-wp-0016-drift-prevention-entry-docs-and-ci-checks-review.md`
- `scripts/check-contract-consistency.py`
- `docs/collaboration/terminology-migration.md`

## Work Notes

- 2026-08-19 — Design & Review group (Planner): opened this issue directly
  from the WP-0016 Reviewer's own required condition of Approval, and
  resolved it in the same session — word-boundary regex applied,
  guidance note added, verified against both a positive (still catches
  genuine use) and an isolated negative (false positives eliminated) case
  with real command output. `Status: in_progress`, pending separate-context
  Reviewer confirmation under Minor Fix Path.
- 2026-08-19 — Design & Review group (Planner): separate-context Reviewer
  confirmed the fix with independently constructed evidence (see
  References). `Status: closed`. Opened LISS-0051 for the Reviewer's own
  required follow-up condition.

## Verification

- Command run: `python3 scripts/check-contract-consistency.py`
- Isolated negative case (false positives eliminated):
  ```
  $ printf 'AIDE integration reference. See AIP-0043-001 for details. MAINTAIN and CONTAINS text.\n' > scratch-reviewer-negative-test.md
  $ python3 scripts/check-contract-consistency.py 2>&1 | grep "scratch-reviewer-negative-test"
  (no output -- zero matches)
  ```
- Positive case (genuine use still caught): a line containing
  `AI-assisted`, `AIDE`, `AIP-0043-001`, and a standalone `AI is retired`
  produced exactly one failure line for the file (the check reports once
  per file/line/term via `.search()`, matching the pre-existing
  granularity), confirming the standalone token is still detected.
- Final clean re-run after removing all synthetic artifacts:
  `contract consistency: all checks passed`, exit 0.
- Separate-context Reviewer confirmation: Approved (see References) —
  the Reviewer independently retired a different term ("log," not "AI")
  and ran the real checker against 132 real files containing "backlog"
  outside `docs/backlog/`, confirming zero false positives and 29 correct
  standalone-use flags, a stronger adversarial test than this issue's own
  evidence. Also independently found and required tracking of a narrower
  follow-up gap (punctuation-edged terms), opened as LISS-0051.
