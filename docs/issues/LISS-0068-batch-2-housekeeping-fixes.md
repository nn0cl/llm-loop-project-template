# LISS-0068: Fix stale backlog Links fields (items 0005-0009) and WP-0021's empty close date

## Metadata

- Local issue ID: LISS-0068
- GitHub issue: none
- Status: done
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: Fast Path
- Type: process
- Priority: low
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0024-retroactive-adr-0020-archival-batch-2.md`)
- Related branch: process/item-0016-batch-2-proposal (this issue's own
  execution branch is created off it, per the work plan)

## Summary

Two small, unrelated-to-archival housekeeping fixes the Backlog thread
folded into this same work plan (per its decision recorded in
`docs/issues/LISS-0065-...md`'s Work Notes):

1. Five backlog items' own `Links: Work plan (when promoted)` field still
   reads "none yet," even though each is genuinely done via a real,
   already-Director-closed work plan — confirmed by direct cross-reference
   in `LISS-0065`'s own "Separately resolved" table.
2. `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`'s own
   "Work-Plan Close" section has an empty `Date:` field despite being
   functionally Director-closed (folded into WP-0019's combined close
   narrative without its own section being updated) — the actual date,
   `2026-08-20`, is already known from PR #21's own merge record.

## Acceptance Notes

### 1. Backlog `Links` field corrections

For each of the five files below, change the `Work plan (when promoted):
none yet` line (or the equivalent existing wording) to point at the real
resolving work plan, using this exact wording pattern: "Work plan (when
promoted): `docs/work-plans/WP-NNNN-*.md` — confirmed via direct
cross-reference; this item's own `Links` field was never updated when the
work landed (see `docs/issues/LISS-0065-...md`'s own cross-reference
table)."

| File | Points to |
| --- | --- |
| `docs/backlog/item-0005-template-propagation-script-for-two-group-loop.md` | `docs/work-plans/WP-0005-template-propagation-work-plan-exclusion.md` |
| `docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md` | `docs/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md` |
| `docs/backlog/item-0007-multi-agent-tool-loop-portability.md` | `docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md` |
| `docs/backlog/item-0008-coordinator-message-hallucination-correction.md` | `docs/work-plans/WP-0003-coordinator-message-correction.md` |
| `docs/backlog/item-0009-document-consistency-drift-on-completion.md` | `docs/work-plans/WP-0007-document-consistency-drift-checks.md` |

**Important sequencing note**: if this issue is executed on a branch
where LISS-0066/LISS-0067 have already archived the corresponding work
plans, point instead at the `docs/archive/work-plans/...` path each work
plan actually resides at by that point (check directly which is true at
execution time — do not guess). Either a live or an archived path is
correct as long as it is the path that actually resolves; do not leave a
dangling reference either way.

### 2. WP-0021's own close date

In `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`'s own
"Work-Plan Close" section, change:

```diff
-- Date:
+- Date: 2026-08-20 (filled in retroactively — folded into WP-0019's own
+  combined close narrative at the time; PR #21's merge record confirms
+  this date)
```

Do not alter any other field in that section (`Result read`, `Next
direction`, `New design agreement` — leave exactly as they are, even if
empty; this issue's own scope is the one missing date only).

## Dependencies

- Parent: `docs/work-plans/WP-0024-retroactive-adr-0020-archival-batch-2.md`
- Depends on: `docs/issues/LISS-0065-retroactive-adr-0020-batch-2-proposal.md`
  (the Backlog-thread decision folding this in)
- Blocks: none
- Related: `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`

## Decisions Not Settled by the Design Agreement

- None — fully settled by
  `docs/collaboration/agreements/2026-08-20-retroactive-adr-0020-batch-2.md`
  (`DA-2026-08-20-07`).

## Context

- Included: `docs/issues/LISS-0065-...md`'s own cross-reference table and
  "Real gap found" section (the source of both fixes this issue applies).
- Omitted: nothing else — this is a small, fully bounded correction.
- Assumptions: none.

## References

- `docs/issues/LISS-0065-retroactive-adr-0020-batch-2-proposal.md`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0024, scoped per the design agreement. Not yet dispatched.
- 2026-08-20 — Implementation group (Implementer persona), branch
  `wp-0024-execution`, after LISS-0066 and LISS-0067 both landed. Per this
  issue's own sequencing note, checked directly which path each of the
  five target work plans now lives at, rather than assuming: all five
  (WP-0003, WP-0004, WP-0005, WP-0006, WP-0007) are already archived by
  LISS-0066/LISS-0067 by this point (`ls
  docs/archive/work-plans/WP-000{3,4,5,6,7}-*.md` confirmed all five
  present at their `docs/archive/...` paths). Pointed all five backlog
  items' `Links` fields at the `docs/archive/work-plans/...` path
  accordingly, using the exact wording pattern this issue's own Acceptance
  Notes specify. For item-0008, whose existing wording was a multi-line
  speculative note ("likely a Minor Fix Path addendum... or a new small
  work plan otherwise") rather than the plain "none yet" the other four
  had, replaced the whole speculative passage with the same standard
  wording pattern — the speculation is now resolved, so the standard
  pattern is the correct final text, not a shortened version of the old
  speculation. Applied the WP-0021 close-date fix exactly per the diff
  this issue's own Acceptance Notes specify, touching no other field in
  that section. `git diff --stat` confirms the five backlog items and
  WP-0021 (six files) are the only content-scope changes; this issue's own
  Status/Work-Notes update and WP-0024's Issue Graph status sync
  (bookkeeping, not content scope) are the only other files touched, same
  pattern as LISS-0066/LISS-0067's own closes.

## Self-Review (short form, per `docs/templates/self-review.md`, planning size S)

Phase / finding: Fast Path, docs-only housekeeping fix.

Command run: `python3 scripts/check-contract-consistency.py`

Result:

```text
contract consistency: all checks passed
```

Risks considered:
- One of the five backlog items' new `Links` path does not actually
  resolve to a real file (typo, or archived to a different path than
  assumed).
- The `git diff` footprint exceeds the six files this issue's own
  Verification section names.

Why each does not occur:
- Re-ran `grep -n "Work plan (when promoted)"` across all five backlog
  files after the edits and cross-checked each resulting path against the
  actual `docs/archive/work-plans/` directory listing (see Work Notes
  above) — all five resolve to real, already-archived files.
- `git diff --stat` shows the five backlog items plus
  `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md` as the only
  content-bearing changes (six files); the two additional touched files
  (this issue's own Status/Work-Notes and WP-0024's Issue Graph sync) are
  the same bookkeeping-only pattern LISS-0066 and LISS-0067 both also
  required, not an expansion of this issue's own housekeeping scope.

## Verification

- `python3 scripts/check-contract-consistency.py` — no regression.
- `git diff` confined to exactly six files (the five backlog items plus
  `WP-0021-...md`).
- Direct confirmation each updated `Links`/path reference actually
  resolves (points at a real, existing file, live or archived).
