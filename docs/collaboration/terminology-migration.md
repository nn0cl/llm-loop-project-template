# Terminology Migration Table

The old-to-new terminology this repository has actually retired, per
`docs/architecture/adr/0020-document-and-log-lifecycle-model.md`'s Entry
document requirements (item-0012 facet 5). Every session should be able to
tell, from this one table, whether a term it is about to write or read is
current or retired.

This table starts empty. A row is added only when a term is actually
retired by a real decision (an Accepted ADR, a design agreement, or an
equivalent recorded decision) — not backfilled speculatively for terms
that were never actually used, and not populated ahead of the later
retroactive-application work plan's own review of this repository's
existing history.

`scripts/check-contract-consistency.py`'s `check_retired_terminology`
check fails a build if a retired term below still appears in a current
document (anything outside `docs/collaboration/traces/`, `reviews/`,
`agreements/`, `docs/issues/`, `docs/work-plans/`, `docs/spike/`,
`docs/backlog/`, or `docs/archive/` — the same record/archive directories
ADR 0020 and this script already treat as historical). An empty table
(no rows) makes the check a no-op, not a failure. Matching is
word-boundary-anchored (a retired term fused into a longer identifier,
like `AIP-0043`, does not match `AI`), but a short or very common word
retired on its own will still legitimately flag every standalone use of
it across the repository — prefer a specific multi-word phrase as the
retired term when one exists, rather than a single short/common word, to
keep a real retirement's failure list reviewable.

## Table

| Retired term | Replacement | Retired by | Date |
| --- | --- | --- | --- |
| _(no entries yet)_ | | | |
