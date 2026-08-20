# Restoration Ledger

The single, append-only record of every document archived or consolidated
under `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
(Rules 3 and 5). Every row is added in the same commit as the archive move
or trace consolidation it records. Never reorder or rewrite an existing
row — a correction is a new row, not an edit to an old one.

This ledger starts empty. It is populated only by ordinary ongoing
archival from this point forward, and by the later, separate
retroactive-application work plan referenced in
`docs/backlog/item-0012-document-and-log-lifecycle-management.md`'s
Promotion notes — not backfilled speculatively by ADR 0020's own work plan
(WP-0014).

## How to read a row

- `date` — the date the row was recorded.
- `source_path` — the document's path before the move.
- `source_commit` — the full commit hash that performed the move.
- `source_tag` — optional; an annotated git tag, only when one was also
  created for this move (not required by default under ADR 0020).
- `canonical_destination` — the `docs/archive/...` path the document now
  lives at, or the representative trace's path for a trace consolidation
  (`classification: consolidated-into-representative`).
- `classification` — one of `archived`, `consolidated-into-representative`,
  `superseded`.
- `reason` — one sentence naming the ADR 0020 Rule 2 trigger that applied.

## Recovery

For any row, the current copy is at `canonical_destination`. As a second,
independent recovery path, the original pre-move state is also always
available from git history:

```console
git show <source_commit>^:<source_path>
```

(the parent of `source_commit`, since `source_commit` is the move itself).

## Ledger

| date | source_path | source_commit | source_tag | canonical_destination | classification | reason |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-08-20 | `docs/work-plans/WP-0001-review-issues-minor-fix-path.md` | a771e48fc772b1600f8fa930e58ad56c12185d52 | N/A | `docs/archive/work-plans/WP-0001-review-issues-minor-fix-path.md` | archived | Work plan carries no formal Director-close commit (predates that convention) but its own file records its sole issue, LISS-0001, at terminal `Status: done` with "Current Next Issue: none"; no open `Type: review-finding` issue names it — judgment call recorded in `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`'s Selection section, per ADR 0020 Rule 2's "record its own judgment call for cases not listed here" allowance. |
| 2026-08-20 | `docs/issues/LISS-0001-review-issues-minor-fix-path.md` | a771e48fc772b1600f8fa930e58ad56c12185d52 | N/A | `docs/archive/issues/LISS-0001-review-issues-minor-fix-path.md` | archived | Terminal `Status: done`; owning work plan (WP-0001) archived in the same commit. |
| 2026-08-20 | `docs/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md` | a771e48fc772b1600f8fa930e58ad56c12185d52 | N/A | `docs/archive/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md` | archived | Owning work plan (WP-0001) archived in the same commit; work plan review record (Rule 2: eligible once the work plan it reviewed is archived). |
| 2026-08-20 | `docs/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md` | a771e48fc772b1600f8fa930e58ad56c12185d52 | N/A | `docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md` | archived | Owning work plan (WP-0001) archived in the same commit; work plan review record (Rule 2: eligible once the work plan it reviewed is archived). |
| 2026-08-20 | `docs/collaboration/reviews/2026-08-02-review-issues-minor-fix-path-arbiter.md` | a771e48fc772b1600f8fa930e58ad56c12185d52 | N/A | `docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path-arbiter.md` | archived | Owning work plan (WP-0001) archived in the same commit; work plan review record (Rule 2: eligible once the work plan it reviewed is archived). |
