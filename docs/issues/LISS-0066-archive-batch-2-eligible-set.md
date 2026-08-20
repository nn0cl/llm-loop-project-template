# LISS-0066: Archive WP-0003, WP-0005, WP-0007, WP-0008, WP-0009 under ADR 0020

## Metadata

- Local issue ID: LISS-0066
- GitHub issue: none
- Status: ready
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: docs-only
- Type: process
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A — first attempt. Covers 5 work plans, none
  with a blocked design agreement or a mandatory reference update — the
  "simple" half of batch 2 (LISS-0067 covers the two work plans that do
  have a blocked agreement and a required reference update).
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0024-retroactive-adr-0020-archival-batch-2.md`)
- Related branch: process/item-0016-batch-2-proposal (this issue's own
  execution branch is created off it, per the work plan)

## Summary

Apply ADR 0020 Rules 2-3 to five of batch 2's seven authorized work plans
(`docs/issues/LISS-0065-...md`, Backlog-thread decision recorded in its
own Work Notes): WP-0003, WP-0005, WP-0007, WP-0008, WP-0009, and — unlike
WP-0001/WP-0002 in batch 1 — **each of these five work plans' own design
agreement is archival-eligible too**, since none is normatively cited by
any current ADR (independently confirmed by `grep` sweep across
`docs/architecture/adr/*.md`, `docs/collaboration/*.md`, and
`docs/templates/*.md` — zero hits for any of the five agreement IDs).

## Acceptance Notes

### Files to move, verbatim, via `git mv`

| # | Source | Destination |
| --- | --- | --- |
| 1 | `docs/work-plans/WP-0003-coordinator-message-correction.md` | `docs/archive/work-plans/WP-0003-coordinator-message-correction.md` |
| 2 | `docs/issues/LISS-0028-coordinator-message-hallucination-correction.md` | `docs/archive/issues/LISS-0028-coordinator-message-hallucination-correction.md` |
| 3 | `docs/collaboration/traces/2026-08-18-liss-0028-coordinator-message-correction.md` | `docs/archive/collaboration/traces/2026-08-18-liss-0028-coordinator-message-correction.md` |
| 4 | `docs/collaboration/reviews/2026-08-18-wp-0003-coordinator-message-correction-review.md` | `docs/archive/collaboration/reviews/2026-08-18-wp-0003-coordinator-message-correction-review.md` |
| 5 | `docs/collaboration/agreements/2026-08-18-coordinator-message-correction.md` (`DA-2026-08-18-02`) | `docs/archive/collaboration/agreements/2026-08-18-coordinator-message-correction.md` |
| 6 | `docs/work-plans/WP-0005-template-propagation-work-plan-exclusion.md` | `docs/archive/work-plans/WP-0005-template-propagation-work-plan-exclusion.md` |
| 7 | `docs/issues/LISS-0031-template-propagation-work-plan-exclusion.md` | `docs/archive/issues/LISS-0031-template-propagation-work-plan-exclusion.md` |
| 8 | `docs/collaboration/reviews/2026-08-18-wp-0005-template-propagation-work-plan-exclusion-review.md` | `docs/archive/collaboration/reviews/2026-08-18-wp-0005-template-propagation-work-plan-exclusion-review.md` |
| 9 | `docs/collaboration/agreements/2026-08-18-template-propagation-work-plan-exclusion.md` (`DA-2026-08-18-04`) | `docs/archive/collaboration/agreements/2026-08-18-template-propagation-work-plan-exclusion.md` |
| 10 | `docs/work-plans/WP-0007-document-consistency-drift-checks.md` | `docs/archive/work-plans/WP-0007-document-consistency-drift-checks.md` |
| 11 | `docs/issues/LISS-0035-document-consistency-drift-checks.md` | `docs/archive/issues/LISS-0035-document-consistency-drift-checks.md` |
| 12 | `docs/collaboration/reviews/2026-08-18-wp-0007-document-consistency-drift-checks-review.md` | `docs/archive/collaboration/reviews/2026-08-18-wp-0007-document-consistency-drift-checks-review.md` |
| 13 | `docs/collaboration/agreements/2026-08-18-document-consistency-drift-checks.md` (`DA-2026-08-18-06`) | `docs/archive/collaboration/agreements/2026-08-18-document-consistency-drift-checks.md` |
| 14 | `docs/work-plans/WP-0008-coordinator-role-inoculation-rule.md` | `docs/archive/work-plans/WP-0008-coordinator-role-inoculation-rule.md` |
| 15 | `docs/issues/LISS-0036-coordinator-role-inoculation-rule.md` | `docs/archive/issues/LISS-0036-coordinator-role-inoculation-rule.md` |
| 16 | `docs/collaboration/reviews/2026-08-18-wp-0008-coordinator-role-inoculation-rule-review.md` | `docs/archive/collaboration/reviews/2026-08-18-wp-0008-coordinator-role-inoculation-rule-review.md` |
| 17 | `docs/collaboration/agreements/2026-08-18-coordinator-role-inoculation-rule.md` (`DA-2026-08-18-07`) | `docs/archive/collaboration/agreements/2026-08-18-coordinator-role-inoculation-rule.md` |
| 18 | `docs/work-plans/WP-0009-contract-reviewer-v230.md` | `docs/archive/work-plans/WP-0009-contract-reviewer-v230.md` |
| 19 | `docs/issues/LISS-0037-contract-reviewer-v230.md` | `docs/archive/issues/LISS-0037-contract-reviewer-v230.md` |
| 20 | `docs/collaboration/reviews/2026-08-19-contract-reviewer-v230-review.md` | `docs/archive/collaboration/reviews/2026-08-19-contract-reviewer-v230-review.md` |
| 21 | `docs/collaboration/agreements/2026-08-19-contract-reviewer-v230.md` (`DA-2026-08-19-01`) | `docs/archive/collaboration/agreements/2026-08-19-contract-reviewer-v230.md` |

Note: WP-0005, WP-0007, WP-0008, WP-0009 have no individual trace file —
confirmed directly by `ls docs/collaboration/traces/` and a topic-keyword
search; not a gap to fabricate a trace for, matching this repository's
own precedent (WP-0002's LISS-0019/0026/0027 had none either).

Add one restoration-ledger row per moved file (21 rows total) to
`docs/collaboration/restoration-ledger.md`, `classification: archived`,
`source_tag: N/A`, real `source_commit` hash of the actual move commit
(fill in via the same PENDING-placeholder-then-follow-up-correction-commit
pattern this repository's batch-1 execution used, per
`docs/issues/LISS-0056-...md`'s own precedent — a single commit cannot
contain its own final hash). Suggested `reason` text per type (adjust per
file, one sentence each, naming the ADR 0020 Rule 2 trigger):

- Each work plan: "Director-closed (`<its own real date>`); all owned
  issues at terminal `Status: done`; no open `Type: review-finding` issue
  names it (confirmed directly, `docs/issues/LISS-0065-...md`)."
- Each issue: "Terminal `Status: done`; owning work plan archived in the
  same commit."
- Each review record: "Owning/reviewed work plan archived in the same
  commit (ADR 0020 Rule 2: review record eligible once the work plan it
  reviewed is archived)."
- Each trace (WP-0003 only): "No unresolved obligation, new approval
  boundary, or unique review evidence outstanding; owning work plan
  archived in the same commit (ADR 0020 Rule 4)."
- Each design agreement: "Owning work plan archived in the same commit;
  confirmed not normatively cited by any current ADR or
  `docs/collaboration/*.md`/`docs/templates/*.md` document (`grep` sweep,
  recorded in `docs/issues/LISS-0065-...md`)."

### No reference updates required for this issue's own five work plans

Confirmed by `grep` sweep (recorded in `docs/issues/LISS-0065-...md`):
no current Canonical document (`docs/architecture/adr/*.md`,
`docs/collaboration/*.md`, `docs/templates/*.md`) cites any of these five
work plans' own file paths, issue IDs' paths, review-record paths, or
design-agreement IDs by direct path reference. Still run the same
additional `grep` sweep this issue's own Verification section requires
before finalizing, in case something was missed — do not assume the
proposal's own sweep is exhaustive without re-checking.

## Dependencies

- Parent: `docs/work-plans/WP-0024-retroactive-adr-0020-archival-batch-2.md`
- Depends on: `docs/issues/LISS-0065-retroactive-adr-0020-batch-2-proposal.md`
  (`Status` reflecting the Backlog-thread's recorded decision)
- Blocks: none
- Related: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `docs/collaboration/restoration-ledger.md`

## Decisions Not Settled by the Design Agreement

- None — fully settled by
  `docs/collaboration/agreements/2026-08-20-retroactive-adr-0020-batch-2.md`
  (`DA-2026-08-20-07`).

## Context

- Included: `docs/issues/LISS-0065-...md`'s full text (the authoritative
  eligibility research this issue executes), each of the five work
  plans' and their owned issues'/traces'/reviews'/agreements' own files.
- Omitted: WP-0004, WP-0006 (LISS-0067's own scope); the two housekeeping
  fixes (LISS-0068's own scope); WP-0010 onward (out of this batch).
- Assumptions: none beyond what `LISS-0065` already recorded.

## References

- `docs/issues/LISS-0065-retroactive-adr-0020-batch-2-proposal.md`
- `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0024, scoped per the design agreement. Not yet dispatched.

## Verification

- After the moves: `python3 scripts/check-contract-consistency.py` shows
  no new failures.
- `git log --follow` on each of the 21 destination paths, confirming
  preserved history.
- `docs/collaboration/restoration-ledger.md` contains exactly 21 new rows
  from this issue, each with a real `source_commit` hash.
- Targeted `grep` re-sweep for any inbound reference this issue's own
  research may not have caught.
