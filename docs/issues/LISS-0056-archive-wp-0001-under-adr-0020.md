# LISS-0056: Archive WP-0001 and its owned records under ADR 0020

## Metadata

- Local issue ID: LISS-0056
- GitHub issue: none
- Status: done
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: docs-only
- Type: process
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0019-retroactive-adr-0020-archival-batch-1.md`)
- Related branch: process/promote-item-0016 (this issue's own execution
  branch is created off it, per the work plan)

## Summary

Apply `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
Rules 2-3 to `docs/work-plans/WP-0001-review-issues-minor-fix-path.md` and
its owned Evidence-layer records: move each file verbatim to
`docs/archive/...`, record one restoration-ledger row per move in the same
commit, and leave `docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md`
(`DA-2026-08-02-04`) and `docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md`
untouched (see "Explicit exclusion" below).

## Acceptance Notes

Move exactly these five files, verbatim (no content rewriting), each to
`docs/archive/<original-directory-under-docs>/<original-filename>`:

| # | Source | Destination |
| --- | --- | --- |
| 1 | `docs/work-plans/WP-0001-review-issues-minor-fix-path.md` | `docs/archive/work-plans/WP-0001-review-issues-minor-fix-path.md` |
| 2 | `docs/issues/LISS-0001-review-issues-minor-fix-path.md` | `docs/archive/issues/LISS-0001-review-issues-minor-fix-path.md` |
| 3 | `docs/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md` | `docs/archive/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md` |
| 4 | `docs/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md` | `docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md` |
| 5 | `docs/collaboration/reviews/2026-08-02-review-issues-minor-fix-path-arbiter.md` | `docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path-arbiter.md` |

Use `git mv` for each so history follows the file. Add one row per move to
`docs/collaboration/restoration-ledger.md` (Rule 5's seven columns:
`date, source_path, source_commit, source_tag, canonical_destination,
classification, reason`), `classification: archived`, `source_tag: N/A`,
`source_commit` filled in with the actual commit hash of this same move
commit (the ledger rows and the `git mv` commit land together, per Rule 5).
Suggested `reason` text (adjust to the actual file, keep it one sentence
naming the Rule 2 trigger):

- WP-0001: "Work plan carries no formal Director-close commit (predates
  that convention) but its own file records its sole issue, LISS-0001, at
  terminal `Status: done` with 'Current Next Issue: none'; no open
  `Type: review-finding` issue names it — judgment call recorded in
  `docs/spike/case-0002-.../case.md`'s Selection section, per ADR 0020 Rule
  2's 'record its own judgment call for cases not listed here' allowance."
- LISS-0001: "Terminal `Status: done`; owning work plan (WP-0001) archived
  in the same commit."
- Trace and both review records: "Owning work plan (WP-0001) archived in
  the same commit; work plan review record (`Rule 2`: eligible once the
  work plan it reviewed is archived)."

**Explicit exclusion — do not move:**

- `docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md`
  (`DA-2026-08-02-04`). `docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md`'s
  own Status section states "Accepted. Covered by `DA-2026-08-02-04`." — a
  current, Accepted, not-fully-superseded ADR citing this specific
  agreement ID as its own Accepted-status grounding, not in passing. ADR
  0020 Rule 2's opening clause: "A document with... content a current
  Canonical document still references by more than a passing mention is
  never eligible, regardless of its own type's terminal status." This
  agreement stays in place regardless of WP-0001's own archival.
- `docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md`
  itself and `docs/specs/review-issue-and-minor-fix-path.feature.md` — an
  ADR (zero ADRs are Rule-2-eligible in this repository today, per
  case-0002's own research) and a current spec file (Canonical layer, not
  Evidence), neither in scope for this or any near-term batch.

**Optional, non-blocking courtesy check**: `docs/collaboration/reviews/2026-08-02-mirror-parity-and-v101-review.md`
cites `docs/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md`
(item 4 above). That citing document is itself an Evidence-layer review
record, not a current Canonical document, so ADR 0020 Rule 3's mandatory
reference-update requirement does not apply — but update the citation to
the new archive path anyway if it reads as a direct "see that file" pointer
rather than a passing historical mention, for reader convenience. Record
whichever choice is made in this issue's own Work Notes; do not silently
skip recording the check even if no edit is made.

## Dependencies

- Parent: `docs/work-plans/WP-0019-retroactive-adr-0020-archival-batch-1.md`
- Depends on: `docs/issues/LISS-0055-retroactive-adr-0020-batching-aggressiveness-decision.md`
  (`Status: done` — Backlog-thread authorization recorded there)
- Blocks: none
- Related: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `docs/collaboration/restoration-ledger.md`,
  `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`

## Decisions Not Settled by the Design Agreement

- None — this issue's scope is fully settled by
  `docs/collaboration/agreements/2026-08-20-retroactive-adr-0020-batch-1.md`
  (`DA-2026-08-20-02`).

## Context

- Included: ADR 0020 full text, WP-0001's own file, LISS-0001's own file,
  the trace and both review records listed above, ADR 0012's Status
  section, DA-2026-08-02-04's own file, direct `grep` sweep of
  `docs/architecture/adr/`, `docs/collaboration/*.md`, and
  `docs/templates/*.md` for inbound references to each moved file's path.
- Omitted: WP-0002 and its own records (LISS-0057's scope, not this
  issue's); WP-0003 through WP-0018 (out of this batch entirely).
- Assumptions: none beyond what case-0002's Addendum and this issue's own
  Acceptance Notes state explicitly.

## References

- `docs/architecture/adr/0020-document-and-log-lifecycle-model.md` (Rules
  2, 3, 5)
- `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`
  (Selection section and post-close Addendum)
- `docs/issues/LISS-0055-retroactive-adr-0020-batching-aggressiveness-decision.md`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0019, scoped per the design agreement. Not yet dispatched.
- 2026-08-20 — Implementation group (Implementer persona). Re-verified
  Rule-2 eligibility directly against the actual files before moving
  anything: `docs/work-plans/WP-0001-review-issues-minor-fix-path.md`'s
  own Issue Graph shows `LISS-0001 | done` and its own "Current Next
  Issue" section states "Issue: none"; `docs/issues/LISS-0001-...md`'s own
  `Status: done`; a repository-wide `grep` for `Type: review-finding`
  issues naming WP-0001 or LISS-0001 found none open. Moved all 5 files
  listed in this issue's Acceptance Notes table via `git mv` (destination
  directories under `docs/archive/` did not exist yet and were created
  first with `mkdir -p`; `git mv` then registered each as a rename, not a
  delete+add, confirmed via `git status`). Added 5 rows to
  `docs/collaboration/restoration-ledger.md` using the suggested reason
  text verbatim (only cosmetic quoting adjustments for Markdown-table
  safety). Courtesy check (Acceptance Notes' "Optional, non-blocking
  courtesy check"): searched
  `docs/collaboration/reviews/2026-08-02-mirror-parity-and-v101-review.md`
  for a citation of the review record
  (`docs/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md`,
  item 4). No such citation exists in that file — `grep -n
  "review-issues-minor-fix-path"` against it returns exactly one hit
  (line 76), and that hit names the *trace* file (item 3), not the review
  record, and appears only inside a pasted `grep` command's own output
  from a historical stale-ADR-range sweep (illustrating a prior search
  result, annotated "record dir, historical, excluded by design"), not a
  live "see that file" navigational pointer. Decision: no edit made to
  `2026-08-02-mirror-parity-and-v101-review.md` — its one mention is a
  passing historical mention (pasted evidence of a past search), not the
  kind of direct pointer the courtesy check asks to redirect, and it does
  not even cite the file the courtesy check named.
- 2026-08-20 — Implementation group (Implementer persona). Hash
  self-reference note: the plan's suggested "commit, then amend to insert
  this commit's own hash" mechanic does not actually converge — amending
  changes the commit's content (the ledger cell now holding a hash),
  which changes the commit's own hash again, so the first amend
  (`a771e48...`) left the ledger referencing a hash that was immediately
  stale and now dangling/unreachable. Corrected via the plan's own
  documented alternative ("a small follow-up correction commit"): a
  second commit (`d02eb3c...`) edited only the ledger's `source_commit`
  cells to the real, final, reachable hash of the move commit
  (`dfe5030a7ead7e8e1bcf472e47ce6af4022f287c`), which is not touched
  again after that. Flagging this as a deviation from the literal
  amend-only mechanic described in the dispatch instructions, though it
  matches the fallback the same instructions also offered.
- 2026-08-20 — Implementation group (Implementer persona). Self-review
  (short form, per `docs/templates/self-review.md`):
  - Phase / finding: Fast Path — docs-only archival move (no Red/Green/
    Refactor cycle; ADR 0020 Rules 2-3 mechanics).
  - Command run: `python3 scripts/check-contract-consistency.py`
  - Result: initial run failed with one finding —
    `docs/issues/LISS-0056-archive-wp-0001-under-adr-0020.md states
    Status: done, but docs/work-plans/WP-0019-retroactive-adr-0020-archival-batch-1.md's
    Issue Graph lists LISS-0056 as 'ready'` — fixed by updating WP-0019's
    Issue Graph row for LISS-0056 to `done`; re-run:
    `contract consistency: all checks passed`.
  - Risks considered: (1) a moved file's git history broken by
    delete+recreate instead of `git mv`; (2) a restoration-ledger row's
    `source_commit` not matching the actual, final, reachable move
    commit; (3) the work plan's own Issue Graph status drifting from the
    issue's own `Status` field.
  - Why each does not occur: (1) `git log --follow --oneline -- docs/archive/work-plans/WP-0001-review-issues-minor-fix-path.md`
    shows two commits (`dfe5030` then, following back, the pre-move
    `39cf12f`), confirming rename history was preserved, not
    delete+recreate. (2) all five ledger rows were corrected in commit
    `d02eb3c` to `dfe5030a7ead7e8e1bcf472e47ce6af4022f287c`, the actual
    commit containing the `git mv`s and the ledger rows, verified via
    `git show --stat dfe5030` showing all five renames. (3) resolved and
    re-verified — `check-contract-consistency.py` now passes with zero
    failures after syncing WP-0019's Issue Graph.

## Verification

- After the move: `python3 scripts/check-contract-consistency.py` shows no
  new failures attributable to this move (dangling references, mirror
  parity, or Entry-archive-reference checks).
- `git log --follow -- docs/archive/work-plans/WP-0001-review-issues-minor-fix-path.md`
  shows the file's pre-move history is preserved (confirms `git mv`, not
  delete+recreate).
- `docs/collaboration/restoration-ledger.md` contains exactly five new rows
  after this issue's commit, one per moved file, each with a real
  `source_commit` hash matching the move commit.
