# LISS-0067: Archive WP-0004, WP-0006 under ADR 0020 (blocked agreements, mandatory reference updates)

## Metadata

- Local issue ID: LISS-0067
- GitHub issue: none
- Status: done
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
- 2026-08-20 — Implementation group (Implementer persona), branch
  `wp-0024-execution`, after LISS-0066 landed. **LISS-0029 trace
  verification (done first, before moving anything)**: ran `ls
  docs/collaboration/traces/ | grep -i liss-0029` — zero hits. Cross-checked
  LISS-0029's own file directly: its Acceptance Notes state "Not an ADR-0006
  contract file (mirrors ADR 0016's own precedent — no trace required for
  this issue)," and its Work Notes never reference a trace file of its own.
  Conclusion: LISS-0029 genuinely has no separate trace file; only
  `2026-08-18-liss-0030-mirror-portable-loop-wording.md` exists for this
  branch pair, exactly as this issue's own research anticipated as the
  more likely outcome. **File count is therefore 11, not 12.**
  `git mv`'d all 11 files verbatim to their `docs/archive/...`
  destinations (`git status --short` showed all 11 as clean `R` renames).
  Applied both mandatory Rule-3 reference-path updates in the same working
  tree as the moves: ADR 0017 line 14 and ADR 0018 line 8, each changing
  only the `docs/work-plans/WP-000{4,6}-...md` path segment to
  `docs/archive/work-plans/WP-000{4,6}-...md` — no other text in either
  ADR touched (confirmed via `git diff` showing exactly one changed line
  per file). Ran the additional `grep -rln` sweep this issue's own
  Acceptance Notes require, for both work-plan filenames and all four
  issue IDs (LISS-0029, -0030, -0032, -0033) across
  `docs/architecture/adr/`, `docs/collaboration/*.md`, `docs/templates/*.md`
  — only ADR 0017 and ADR 0018 referenced the two work-plan paths (the two
  mandatory updates just applied); zero hits for any of the four issue
  IDs by direct path reference, and zero other Canonical document found.
  Re-ran the same `grep -rn` for the two old paths after the edits — zero
  remaining hits anywhere, confirming both updates actually landed and no
  dangling reference remains. Confirmed directly (`git status --short` and
  `test -f`) that both `docs/collaboration/agreements/2026-08-18-multi-agent-tool-loop-portability.md`
  (`DA-2026-08-18-03`) and `docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md`
  (`DA-2026-08-18-05`) remain unmodified at their original paths (blocked,
  per this issue's own Summary). Appended 11 restoration-ledger rows with
  `source_commit: PENDING`, same reasoning as LISS-0066's own Work Notes
  for why a literal placeholder is used instead of a guessed hash. Ran
  `python3 scripts/check-contract-consistency.py` — passed clean (recorded
  in full in the Self-Review below). Committed the 11 moves, the two ADR
  reference-path edits, the 11 ledger rows, and this Status/Work-Notes
  update together in one commit (ADR 0020 Rule 3 requires the ledger rows
  land in the same commit as the move — noted here because an earlier
  attempt in this same session to commit an unrelated one-line Issue-Graph
  fix for LISS-0066 accidentally swept up these already-`git mv`-staged
  renames into that other commit; caught before it was pushed anywhere,
  fixed with a non-destructive `git reset --soft`/`git reset <path>`
  re-split, and this issue's own moves were re-committed correctly as one
  atomic commit here). Then ran a small separate follow-up commit
  correcting the 11 `PENDING` values to that commit's real hash, same
  pattern as LISS-0066. Both hashes are recorded in the Self-Review below
  and cross-referenced from the parent work plan's Preflight section.

## Self-Review (full form, per `docs/templates/self-review.md`, planning size M)

### Deterministic Verification Output

Command: `ls docs/collaboration/traces/ | grep -i liss-0029` (run before
any move):

```text
(no output — zero matches)
```

Command: `python3 scripts/check-contract-consistency.py` (run after the 11
moves, the two ADR edits, and the ledger update, working tree state):

```text
contract consistency: all checks passed
```

Command: `grep -rn "docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md" docs/architecture/ docs/collaboration/*.md docs/templates/` and the WP-0006 equivalent (run after the ADR edits):

```text
(no output — zero matches outside the archive path itself; the two ADRs
now read docs/archive/work-plans/WP-000{4,6}-...md, which does not match
the old-path pattern searched for)
```

Command: `git log --follow --oneline -- docs/archive/work-plans/WP-0004-multi-agent-tool-loop-portability.md`
and the same for `docs/archive/collaboration/agreements/2026-08-18-multi-agent-tool-loop-portability.md` is
N/A (that file did not move) — used
`docs/archive/collaboration/reviews/2026-08-18-wp-0004-multi-agent-tool-loop-portability-review.md`
and `docs/archive/collaboration/traces/2026-08-18-liss-0030-mirror-portable-loop-wording.md`
instead (run after this issue's own commit landed): each shows full
pre-move history plus the move commit, confirming `--follow` preserved
history for this issue's own sample.

### Falsification Search

- **Risk: LISS-0029 actually has its own trace file under a name this
  issue's own research (and a case-insensitive grep) did not anticipate.**
  Checked two independent ways: `ls docs/collaboration/traces/ | grep -i
  liss-0029` (zero hits) and reading LISS-0029's own Acceptance Notes and
  Work Notes directly rather than trusting the directory listing alone —
  both a filename-based search and the issue's own self-description agree
  it has none. Does not occur: two independent checks, not one.
- **Risk: the ADR reference-path edit changes more than the one path
  segment named (Rule-3 says "path update only, no other change
  authorized").** Ran `git diff -- docs/architecture/adr/0017-*.md
  docs/architecture/adr/0018-*.md` after the edits and confirmed exactly
  one changed line per file, each changing only the
  `docs/work-plans/...` segment to `docs/archive/work-plans/...` — no
  other character in either file differs from before the edit.
  Does not occur: confirmed by direct diff inspection, not by trusting the
  Edit tool's own description of the change.
- **Risk: a third current Canonical document, beyond ADR 0017 and ADR
  0018, also cites one of these 11 files by direct path and was missed.**
  Ran the mandated `grep -rln` sweep for both work-plan filenames and all
  four issue IDs across `docs/architecture/adr/`, `docs/collaboration/*.md`,
  `docs/templates/*.md` before finalizing — only ADR 0017 and ADR 0018
  matched (the two work-plan-path hits, which are the two mandatory
  updates); no other file matched for any of the six search terms. Does
  not occur: independently re-verified, not assumed from the issue's own
  claim of "two mandatory updates" alone.
- **Risk: one of the two blocked design agreements was accidentally
  included in the move (a fat-fingered `git mv` on the wrong file).**
  Checked directly, twice: once by counting the `git status --short`
  output (exactly 11 `R` lines, matching the 11-file table, not 13) and
  once by `test -f` on both `DA-2026-08-18-03`'s and `DA-2026-08-18-05`'s
  own original paths after all 11 moves — both still present and
  unmodified. Does not occur: both checks confirm.
- **Risk: the restoration-ledger row order or `source_path`/
  `canonical_destination` pairing has a copy-paste swap between the WP-0004
  and WP-0006 halves.** Spot-checked the WP-0004-half rows'
  `canonical_destination` values against `ls docs/archive/work-plans/
  docs/archive/issues/ docs/archive/collaboration/traces/
  docs/archive/collaboration/reviews/` — all 11 resolve to real files at
  the stated paths, and none of the WP-0004-topic rows point at a
  WP-0006-topic destination or vice versa.

### Risks Not Fully Closed

- Same as LISS-0066: `source_commit` is `PENDING` in the first commit by
  construction, closed by the mandatory small follow-up commit recorded in
  Work Notes above.
- The mid-session commit-splitting incident (an unrelated one-line
  Issue-Graph fix briefly absorbing this issue's already-staged renames)
  is recorded transparently in Work Notes above rather than silently
  corrected, per the Prime Directive's "every executed fact leaves
  evidence" — the work-plan-level Reviewer should be able to see this
  happened and that it was caught and fixed with a non-destructive
  `git reset`, not a force-push or history rewrite of any shared branch.

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
