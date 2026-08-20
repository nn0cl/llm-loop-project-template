# LISS-0060: WP-0021's own Issue Graph row was never synced to LISS-0059's terminal status

## Metadata

- Local issue ID: LISS-0060
- GitHub issue: none
- Status: closed
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: docs-only
- Type: review-finding
- Priority: high (blocks Reviewer approval of WP-0021, which itself blocks
  PR #21)
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt.
- Owner/agent: Implementation group (same session that executed LISS-0059,
  `wp-0021-execution` branch, per the Minor Fix Path)
- Related branch: wp-0021-execution

## Summary

Independently re-running `python3 scripts/check-contract-consistency.py`
against a fresh `git archive` extraction of `wp-0021-execution`'s actual
final committed state (both commits `3164778` and `3052b6a`) — not against
the Implementer's own pasted Preflight output — produces a real failure
`check_issue_status_sync` catches:

```
docs/issues/LISS-0059-archive-copy-exclusion-gap.md states Status: done,
but docs/work-plans/WP-0021-archive-copy-exclusion-gap.md's Issue Graph
lists LISS-0059 as 'ready'

contract consistency: 1 failure(s)
```

`docs/issues/LISS-0059-archive-copy-exclusion-gap.md`'s own `Status` field
was correctly updated to `done` (confirmed directly), but
`docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`'s own Issue Graph
table row for `LISS-0059` was never updated to match — it still reads
`ready` in the final committed state (`docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`,
Issue Graph, line ~37). This means the Preflight Validation section's own
check #2 (`python3 scripts/check-contract-consistency.py`, claimed
`contract consistency: all checks passed`) was not actually re-run against
the work plan's own final, fully-committed state — either it was run
before the work plan file's own Issue Graph section was written in its
final form, or the Issue Graph edit was simply missed. Neither commit
(`3164778`, the fix; `3052b6a`, the Preflight record) touches this row.

## Acceptance Notes

Change `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`'s Issue
Graph row for `LISS-0059` from `ready` to `done`:

```diff
-| LISS-0059 | ready | S | S | N/A | - | - | process/promote-item-0018 |
+| LISS-0059 | done | S | S | N/A | - | - | process/promote-item-0018 |
```

No other change is authorized by this finding — this is a single-cell
table sync correction, not a reopening of any other part of the work
plan's own content.

## Review Finding Record

- Originating review record:
  `docs/collaboration/reviews/2026-08-20-wp-0021-archive-copy-exclusion-gap-review.md`
  (recorded once this finding is resolved and the full review completes)
- Affected artifact:
  `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`'s Issue Graph
  table
- Failure scenario: `check_issue_status_sync` fails against the work
  plan's actual final committed state, contradicting the Preflight
  Validation section's own claim of `all checks passed` for that exact
  check
- Reviewer grounds: independently re-ran
  `python3 scripts/check-contract-consistency.py` against a fresh
  `git archive wp-0021-execution` extraction (not against the
  Implementer's own pasted output) and reproduced the failure directly;
  confirmed by direct `git show wp-0021-execution:docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`
  that the Issue Graph row still reads `ready`
- Dispute raised by: none — a straightforward, deterministically
  reproducible sync gap, not a judgment call
- Arbiter decision record: none needed — no deadlock
- Changed files: `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`
  (one table cell)
- Deterministic verification output: recorded in this issue's own
  Verification section once the fix lands
- Separate Reviewer closure record:
  `docs/collaboration/reviews/2026-08-20-wp-0021-archive-copy-exclusion-gap-review.md`
  (Falsification Search row 6) — confirmed independently, against a fresh
  `git archive` extraction of the corrected commit (`9574fbc`), not against
  the Implementer's own pasted output.

## Dependencies

- Parent: `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`
- Depends on: none
- Blocks: WP-0021's own work-plan-level Reviewer approval
- Related: `docs/issues/LISS-0059-archive-copy-exclusion-gap.md`

## Decisions Not Settled by the Design Agreement

- None — this is a mechanical correction to the work plan's own tracking
  table, not a design question.

## Context

- Included: `docs/work-plans/WP-0021-...md`'s full Issue Graph section,
  `docs/issues/LISS-0059-...md`'s own `Status` field, the actual
  `check-contract-consistency.py` output from a fresh, independent
  reproduction.
- Omitted: nothing else — this finding is fully self-contained.
- Assumptions: none.

## References

- `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`
- `docs/issues/LISS-0059-archive-copy-exclusion-gap.md`
- `docs/collaboration/findings-reuse.md` (findings must be applied, not
  merely noted)

## Work Notes

- 2026-08-20 — Reviewer persona (Design & Review group), independent
  verification pass on WP-0021. Found this defect by re-running the
  deterministic check against a fresh `git archive` extraction rather than
  trusting the Implementer's own Preflight output — per
  `docs/collaboration/design-review-perspectives.md`'s "Re-verify state
  that could have changed underneath you" perspective. Routed as a
  `Type: review-finding`, Minor Fix Path eligible (planning size S,
  preserves accepted scope, no specification/ADR/port/data
  model/architecture boundary touched, expected to finish in one attempt).
  Not fixed silently by the Reviewer itself — sent back to the
  Implementation-group session that produced WP-0021 for correction, per
  this repository's own separation-of-duties discipline.

- 2026-08-20 — Implementer persona, `wp-0021-execution`. Merged this
  issue's own commit (`bbe05c8`, from `process/promote-item-0018`) into
  `wp-0021-execution` (clean merge, no conflicts — sibling commits off the
  same `54f73c7` base touching disjoint files). Applied the exact one-line
  diff from this issue's own Acceptance Notes:
  `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`'s Issue Graph
  row for `LISS-0059` changed from `ready` to `done`. Re-ran
  `python3 scripts/check-contract-consistency.py` against the real
  repository (no `--repo` flag) and confirmed `contract consistency: all
  checks passed` for real this time. No other line of the work plan file,
  and no other file, touched by this correction.

## Verification

Before fix (Reviewer's own independent reproduction, against a fresh
`git archive` extraction of `wp-0021-execution`'s committed state, quoted
from this finding's own Summary section above):

```
docs/issues/LISS-0059-archive-copy-exclusion-gap.md states Status: done,
but docs/work-plans/WP-0021-archive-copy-exclusion-gap.md's Issue Graph
lists LISS-0059 as 'ready'

contract consistency: 1 failure(s)
```

After fix (`python3 scripts/check-contract-consistency.py`, real
repository, no `--repo` flag, run by the Implementer on
`wp-0021-execution` after applying the one-line Issue Graph correction):

```
contract consistency: all checks passed
```

`docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`'s Issue Graph row
for `LISS-0059` now reads `done`, matching
`docs/issues/LISS-0059-archive-copy-exclusion-gap.md`'s own `Status`
field. No other line in the diff.
