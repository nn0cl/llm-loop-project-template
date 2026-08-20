# LISS-0064: WP-0023's own Issue Graph row was never synced to LISS-0063's terminal status

## Metadata

- Local issue ID: LISS-0064
- GitHub issue: none
- Status: closed
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: docs-only
- Type: review-finding
- Priority: high (blocks Reviewer approval of WP-0023)
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt.
- Owner/agent: Implementation group (same session that executed LISS-0063,
  `wp-0023-execution` branch, per the Minor Fix Path)
- Related branch: wp-0023-execution

## Summary

Independently re-running `python3 scripts/check-contract-consistency.py`
against a fresh `git archive` extraction of `wp-0023-execution`'s actual
final committed state (both commits `6125931` and `dd5e9f9`) — not
against the Implementer's own pasted Preflight output — produces a real
failure:

```
issue status sync:
  docs/issues/LISS-0063-check-and-spawn-wake-protocol.md states Status: done, but docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md's Issue Graph lists LISS-0063 as 'ready'

contract consistency: 1 failure(s)
```

This is the same defect class as `LISS-0060` (found during WP-0021's
review) and the class the Implementer self-caught during WP-0022's own
Preflight — recurring a third time, and this time not caught before
being reported as Preflight-passed. WP-0023's own Preflight Validation
section's check #1 was run *before* the second commit added the
Preflight content itself to `WP-0023-...md`, and the Issue Graph row was
never revisited afterward — the same root cause as `LISS-0060`.

## Acceptance Notes

Change `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`'s
Issue Graph row for `LISS-0063` from `ready` to `done`:

```diff
-| LISS-0063 | ready | M | M | N/A | LISS-0062 | - | process/promote-item-0020 |
+| LISS-0063 | done | M | M | N/A | LISS-0062 | - | process/promote-item-0020 |
```

No other change is authorized by this finding.

## Review Finding Record

- Originating review record:
  `docs/collaboration/reviews/2026-08-20-wp-0023-self-sustaining-wakeup-protocol-review.md`
  (recorded once this finding is resolved and the full review completes)
- Affected artifact:
  `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`'s Issue
  Graph table
- Failure scenario: `check_issue_status_sync` fails against the work
  plan's actual final committed state, contradicting the Preflight
  Validation section's own claim of `all checks passed` for that exact
  check
- Reviewer grounds: independently re-ran
  `python3 scripts/check-contract-consistency.py` against a fresh
  `git archive wp-0023-execution` extraction and reproduced the failure
  directly; confirmed by direct `git show
  wp-0023-execution:docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`
  that the Issue Graph row still reads `ready`
- Dispute raised by: none — a straightforward, deterministically
  reproducible sync gap, not a judgment call
- Arbiter decision record: none needed — no deadlock
- Changed files: `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`
  (one table cell)
- Deterministic verification output: recorded in this issue's own
  Verification section once the fix lands
- Separate Reviewer closure record:
  `docs/collaboration/reviews/2026-08-20-wp-0023-self-sustaining-wakeup-protocol-review.md`
  (Falsification Search row 5) — confirmed independently, against a fresh
  `git archive` extraction of the corrected commit (`4c4d861`), not
  against the Implementer's own pasted output. Same precedent as
  `LISS-0060`.

## Dependencies

- Parent: `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`
- Depends on: none
- Blocks: WP-0023's own work-plan-level Reviewer approval
- Related: `docs/issues/LISS-0063-check-and-spawn-wake-protocol.md`,
  `docs/issues/LISS-0060-wp-0021-issue-graph-status-sync.md` (same defect
  class, third occurrence this session)

## Decisions Not Settled by the Design Agreement

- None — mechanical correction to the work plan's own tracking table.

## Context

- Included: `docs/work-plans/WP-0023-...md`'s full Issue Graph section,
  `docs/issues/LISS-0063-...md`'s own `Status` field, the actual
  `check-contract-consistency.py` output from a fresh, independent
  reproduction.
- Omitted: nothing else — self-contained.
- Assumptions: none.

## References

- `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`
- `docs/issues/LISS-0063-check-and-spawn-wake-protocol.md`
- `docs/issues/LISS-0060-wp-0021-issue-graph-status-sync.md` (precedent)

## Work Notes

- 2026-08-20 — Reviewer persona (Design & Review group), independent
  verification pass on WP-0023. Found this defect by re-running the
  deterministic check against a fresh `git archive` extraction rather
  than trusting the Implementer's own Preflight output — the same method
  that caught `LISS-0060`. This is the third occurrence of this exact
  defect class this session (WP-0021: caught as `LISS-0060`; WP-0022:
  self-caught by the Implementer during its own Preflight; WP-0023:
  recurred, uncaught before this review). Worth a note for future
  dispatch instructions to explicitly call out syncing the work plan's
  own Issue Graph row as part of any issue-closing step — not resolved by
  this issue itself, which stays scoped to the one-cell fix, but flagged
  here for the record. Routed as a `Type: review-finding`, Minor Fix Path
  eligible. Not fixed silently by the Reviewer itself — sent back to the
  Implementation-group session that produced WP-0023 for correction, per
  this repository's own separation-of-duties discipline.
- 2026-08-20 — Implementation group (Implementer persona), Minor Fix Path.
  Merged the Reviewer's finding commit (`269384e`) into `wp-0023-execution`.
  Applied the exact one-cell fix from this issue's own Acceptance Notes:
  `docs/work-plans/WP-0023-self-sustaining-wakeup-protocol.md`'s Issue
  Graph row for `LISS-0063` changed from `ready` to `done`, no other cell
  touched. Re-ran `python3 scripts/check-contract-consistency.py` and
  confirmed `all checks passed` (see Verification below). `Status` updated
  to `resolved`.

## Verification

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

Confirms `check_issue_status_sync` no longer fails: WP-0023's Issue Graph
row for LISS-0063 now reads `done`, matching
`docs/issues/LISS-0063-check-and-spawn-wake-protocol.md`'s own `Status`
field.
