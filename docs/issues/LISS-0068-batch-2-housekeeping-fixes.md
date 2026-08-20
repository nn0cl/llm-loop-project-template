# LISS-0068: Fix stale backlog Links fields (items 0005-0009) and WP-0021's empty close date

## Metadata

- Local issue ID: LISS-0068
- GitHub issue: none
- Status: ready
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

## Verification

- `python3 scripts/check-contract-consistency.py` — no regression.
- `git diff` confined to exactly six files (the five backlog items plus
  `WP-0021-...md`).
- Direct confirmation each updated `Links`/path reference actually
  resolves (points at a real, existing file, live or archived).
