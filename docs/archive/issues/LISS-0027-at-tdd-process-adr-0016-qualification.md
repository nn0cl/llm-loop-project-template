# LISS-0027: Qualify docs/at-tdd/process.md's close-checkpoint phrasing per ADR 0016

## Metadata

- Local issue ID: LISS-0027
- GitHub issue: none
- Status: done
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

- 2026-08-18 (Implementer, Implementation group, first standing session):
  qualified `docs/at-tdd/process.md`'s "Work-Plan Review and Close" step 4,
  mirroring `design-agreement.md`'s already-reviewed "Closing a work plan"
  wording nearly verbatim (same opening clause, same ADR 0016 Rule 3
  citation and "unrelated, concurrently in-flight" qualifier) — no new
  wording invented, per this issue's own instruction.
- Trace: `docs/collaboration/traces/2026-08-18-liss-0027-at-tdd-process-adr-0016-qualification.md`.
- 2026-08-18 (Reviewer, Design & Review group, separate context): confirmed.
  Record: `docs/collaboration/reviews/2026-08-18-liss-0027-at-tdd-process-adr-0016-qualification-review.md`
  (Approved). Re-ran `scripts/check-contract-consistency.py` and a targeted
  grep independently rather than trusting the Implementer's recorded output;
  both confirmed. This closes Falsification Search scenario #11 from the
  original WP-0002 Reviewer pass. Work-plan close remains the Director's own
  pending action; this issue's Status stays `review`, not `closed`, pending
  that.

### Self-Review (Implementer, design note -> drafted change)

Per `docs/templates/self-review.md`, short form.

```text
Phase / finding: Minor Fix Path design note -> drafted change to
  docs/at-tdd/process.md (Work-Plan Review and Close, step 4)

Command run: python3 scripts/check-contract-consistency.py
Result: contract consistency: all checks passed

Command run: grep -n "does not start without" docs/at-tdd/process.md
Result:
  198:   specific work plan's own successor does not start without this. Per

Risks considered:
  1. The bare, unqualified "The next work plan does not start without
     this." phrase still appears anywhere in the file.
  2. The fix invents new wording instead of mirroring the already-reviewed
     pattern from ai-human-scheme.md / design-agreement.md.
  3. Content in docs/at-tdd/process.md other than step 4 changed.
  4. The consistency checker regresses.

Why each does not occur:
  1. The grep above shows only the qualified sentence; no bare occurrence
     of the old phrase remains anywhere in the file (single match, already
     qualified).
  2. Diffed the new text against design-agreement.md's "Closing a work
     plan" paragraph: "This specific work plan's own successor does not
     start without this... Per [ADR 0016] Rule 3, this does not block
     unrelated, concurrently in-flight work plans in either group — only
     the one work plan being closed, and what directly follows from
     closing it, wait on this action" is carried over near-verbatim, with
     only the ADR path written out in full rather than as a prior
     cross-reference, since this is the sentence's first ADR-0016 mention
     in this file.
  3. The edit's old_string/new_string in the Edit tool call touched only
     the two sentences following "The next work plan does not start
     without this" in step 4; no other line in the file was part of either
     string.
  4. Ran the checker after the edit (output above): zero failures.
```
