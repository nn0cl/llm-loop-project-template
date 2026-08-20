# LISS-0067: Archive WP-0004, WP-0006 under ADR 0020 (blocked agreements, mandatory reference updates)

## Metadata

- Local issue ID: LISS-0067
- GitHub issue: none
- Status: ready
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: docs-only
- Type: process
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A — first attempt. Split from LISS-0066
  because both work plans here have a normatively-blocked design
  agreement plus a mandatory ADR reference-path update — the more
  complex half of batch 2.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0024-retroactive-adr-0020-archival-batch-2.md`)
- Related branch: process/item-0016-batch-2-proposal (this issue's own
  execution branch is created off it, per the work plan)

## Summary

Apply ADR 0020 Rules 2-3 to WP-0004 and WP-0006. Both work plans'
own file, owned issues, trace(s), and review record are archival-eligible.
**Both work plans' own design agreements are blocked** — same ADR
0020 Rule 2 general-opening-clause pattern as batch 1's `DA-2026-08-02-04`/
`DA-2026-08-18-01`:

- `DA-2026-08-18-03` (WP-0004's agreement): ADR 0017's own Status section
  states "Accepted status requires a design agreement... That agreement
  is `DA-2026-08-18-03`" — a normative Accepted-status grounding
  citation, not a passing mention.
- `DA-2026-08-18-05` (WP-0006's agreement): ADR 0018's own Status section
  states "Covered by `DA-2026-08-18-05`" — same normative pattern.

Both ADRs also cite the **work plan's own file path** directly (a
locational "Follow-up issues... (path)" pointer, the same
Rule-3-reference-update, non-blocking case ADR 0016's own citation of
WP-0002's path was in batch 1) — these two references must be updated to
the new `docs/archive/` path in the same commit as each move.

## Acceptance Notes

### Files to move, verbatim, via `git mv`

| # | Source | Destination |
| --- | --- | --- |
| 1 | `docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md` | `docs/archive/work-plans/WP-0004-multi-agent-tool-loop-portability.md` |
| 2 | `docs/issues/LISS-0029-adr-0017-portable-three-layer-loop.md` | `docs/archive/issues/LISS-0029-adr-0017-portable-three-layer-loop.md` |
| 3 | `docs/issues/LISS-0030-mirror-portable-loop-wording.md` | `docs/archive/issues/LISS-0030-mirror-portable-loop-wording.md` |
| 4 | `docs/collaboration/traces/2026-08-18-liss-0030-mirror-portable-loop-wording.md` | `docs/archive/collaboration/traces/2026-08-18-liss-0030-mirror-portable-loop-wording.md` |
| 5 | `docs/collaboration/reviews/2026-08-18-wp-0004-multi-agent-tool-loop-portability-review.md` | `docs/archive/collaboration/reviews/2026-08-18-wp-0004-multi-agent-tool-loop-portability-review.md` |
| 6 | `docs/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md` | `docs/archive/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md` |
| 7 | `docs/issues/LISS-0032-quality-gate-hooks-and-coverage-policy.md` | `docs/archive/issues/LISS-0032-quality-gate-hooks-and-coverage-policy.md` |
| 8 | `docs/issues/LISS-0033-design-review-perspectives-doc.md` | `docs/archive/issues/LISS-0033-design-review-perspectives-doc.md` |
| 9 | `docs/collaboration/traces/2026-08-18-liss-0032-definition-of-done-hook-coverage.md` | `docs/archive/collaboration/traces/2026-08-18-liss-0032-definition-of-done-hook-coverage.md` |
| 10 | `docs/collaboration/traces/2026-08-18-liss-0033-perspectives-doc-and-required-reading.md` | `docs/archive/collaboration/traces/2026-08-18-liss-0033-perspectives-doc-and-required-reading.md` |
| 11 | `docs/collaboration/reviews/2026-08-18-wp-0006-quality-gate-hooks-and-perspectives-doc-review.md` | `docs/archive/collaboration/reviews/2026-08-18-wp-0006-quality-gate-hooks-and-perspectives-doc-review.md` |

**Before moving item 2 (LISS-0029)**: verify directly whether it has its
own individual trace file under a name this issue's own research did not
find (`ls docs/collaboration/traces/ | grep -i liss-0029`, and check
LISS-0029's own Work Notes for any trace reference). WP-0004's own
"Branch note" states LISS-0029 and LISS-0030 landed together on one
branch as a sequential unit, and only one trace file
(`2026-08-18-liss-0030-...md`) was found by this issue's own research —
if LISS-0029 genuinely has none, move only the one found; if it turns out
to have its own separate trace, add it to the move table and the ledger,
recording which was found in this issue's own Work Notes rather than
assuming.

**Do not move**: `docs/collaboration/agreements/2026-08-18-multi-agent-tool-loop-portability.md`
(`DA-2026-08-18-03`) or `docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md`
(`DA-2026-08-18-05`) — both blocked, per this issue's own Summary above.

### Mandatory Rule-3 reference updates (in the same commit as each move)

1. `docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`,
   line ~14: "Follow-up issues: LISS-0029 (this document) and LISS-0030
   (mirror-wording propagation),
   `docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md`." —
   update the path to
   `docs/archive/work-plans/WP-0004-multi-agent-tool-loop-portability.md`.
   Locational pointer, not the ADR's own normative grounding (that is
   `DA-2026-08-18-03`, which is not moving) — path update only, no other
   change authorized to this ADR.
2. `docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md`,
   line ~8: "Follow-up issues: LISS-0032, LISS-0033
   (`docs/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md`)." —
   update the path to
   `docs/archive/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md`.
   Same non-blocking, locational-pointer case; no other change authorized.

Search for, and correct, any other direct-path citation of these 11
files this issue's own research may not have caught (a targeted `grep
-rn "<old-path>"` per moved file against `docs/architecture/adr/*.md`,
`docs/collaboration/*.md`, and `docs/templates/*.md`, before finalizing
the commit).

Add one restoration-ledger row per moved file (11 or 12, depending on the
LISS-0029 trace verification above) using the same suggested-reason
pattern LISS-0066 uses, and the same PENDING-placeholder-then-
follow-up-correction-commit mechanic for `source_commit`.

## Dependencies

- Parent: `docs/work-plans/WP-0024-retroactive-adr-0020-archival-batch-2.md`
- Depends on: `docs/issues/LISS-0065-retroactive-adr-0020-batch-2-proposal.md`
- Blocks: none
- Related: `docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`,
  `docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md`

## Decisions Not Settled by the Design Agreement

- None — fully settled by
  `docs/collaboration/agreements/2026-08-20-retroactive-adr-0020-batch-2.md`
  (`DA-2026-08-20-07`).

## Context

- Included: `docs/issues/LISS-0065-...md`'s full text, ADR 0017 and ADR
  0018's full text, WP-0004 and WP-0006's own files and their owned
  issues/traces/reviews.
- Omitted: WP-0003, WP-0005, WP-0007, WP-0008, WP-0009 (LISS-0066's own
  scope); the two housekeeping fixes (LISS-0068's own scope).
- Assumptions: none beyond what `LISS-0065` already recorded; the
  LISS-0029 trace question is named explicitly as something to verify,
  not assumed.

## References

- `docs/issues/LISS-0065-retroactive-adr-0020-batch-2-proposal.md`
- `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0024, scoped per the design agreement. Not yet dispatched.

## Verification

- After the moves and reference updates: `python3 scripts/check-contract-consistency.py`
  shows no new failures.
- `grep -rn "docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md"
  docs/architecture/ docs/collaboration/*.md docs/templates/` and the
  equivalent for WP-0006 return no hits outside `docs/archive/` and the
  restoration ledger.
- `git log --follow` on each destination path, confirming preserved
  history.
- Restoration-ledger row count matches the actual number of files moved
  (11 or 12).
- Confirmation `DA-2026-08-18-03` and `DA-2026-08-18-05` remain untouched
  at their original paths.
