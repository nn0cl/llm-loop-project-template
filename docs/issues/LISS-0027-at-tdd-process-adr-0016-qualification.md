# LISS-0027: Qualify docs/at-tdd/process.md's close-checkpoint phrasing per ADR 0016

## Metadata

- Local issue ID: LISS-0027
- GitHub issue: none
- Status: proposed
- Phase: process-only
- Type: architecture
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Implementer)
- Related branch: process/at-tdd-process-adr-0016-qualification

## Summary

- Contract file: `docs/at-tdd/process.md` (governed by ADR 0006).
- Minor Fix Path (per WP-0002 and
  `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`'s
  Reopening Log, 2026-08-18): the Reviewer pass for WP-0002 found this file
  carries the same unqualified pre-ADR-0016 phrasing already fixed in
  `docs/collaboration/design-agreement.md` and
  `docs/collaboration/ai-human-scheme.md` — "the next work plan does not
  start without this" (line 198, in "Work-Plan Review and Close"). It was
  out of WP-0002's original Scope, so it was correctly left unedited and
  reported as a finding rather than silently fixed. The Director then
  extended scope to include this fix.
- Fix: add the same ADR 0016 Rule 3 qualification already used in the other
  two files — this checkpoint does not block *unrelated, concurrently
  in-flight* work plans in either group; only the one work plan being
  closed, and what directly follows from closing it, wait on this action.
  Mirror the exact cross-reference pattern used in
  `docs/collaboration/ai-human-scheme.md` (`### Non-blocking concurrency
  across work plans` section) and `docs/collaboration/design-agreement.md`
  (`Closing a work plan` section) rather than inventing new wording.
- Does not change any specification, ADR, port, data model, dependency, or
  architecture boundary — only qualifies existing phrasing to match an
  already-accepted rule (ADR 0016 Rule 3), consistent with the Minor Fix
  Path's own conditions.

## Acceptance Notes

- `docs/at-tdd/process.md`'s "Work-Plan Review and Close" section states
  the ADR 0016 Rule 3 qualification, cross-referencing ADR 0016 rather than
  duplicating its prose at length.
- No other content in `docs/at-tdd/process.md` changes.
- An AI work trace exists under `docs/collaboration/traces/` for this
  change (required regardless of Minor Fix Path or work-plan scope, per
  `docs/collaboration/prompt-instruction-change-control.md`).
- A separate-context Reviewer confirms the fix — self-review does not
  satisfy ADR 0006 for a contract-file change, Minor Fix Path or not.

## Dependencies

- Parent: WP-0002 (Minor Fix Path addendum, per the design agreement's
  Reopening Log, 2026-08-18)
- Depends on: none (ADR 0016 already accepted; this only propagates its
  already-reviewed wording pattern to one more file)
- Blocks: WP-0002's Work-Plan Close
- Related: LISS-0021 (`ai-human-scheme.md`), LISS-0025 (`design-agreement.md`)
  — source of the pattern being mirrored here

## Decisions Not Settled by the Design Agreement

- None known.

## Context

- Included: `docs/at-tdd/process.md` (lines 185-199), the corresponding
  already-fixed sections in `docs/collaboration/ai-human-scheme.md` and
  `docs/collaboration/design-agreement.md`, ADR 0016.
- Omitted: n/a
- Assumptions: none

## References

- `docs/at-tdd/process.md`
- `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`

## Work Notes

- 

## Verification

- `scripts/check-contract-consistency.py`
- Targeted `grep` sweep for the unqualified phrase, confirming none remain.
- Read-through against the pattern already used in `ai-human-scheme.md` /
  `design-agreement.md`.
