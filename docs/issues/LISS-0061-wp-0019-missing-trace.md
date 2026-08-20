# LISS-0061: Add the missing AI work trace for WP-0019's contract-file edits

## Metadata

- Local issue ID: LISS-0061
- GitHub issue: none
- Status: done
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: Fast Path
- Type: process
- Priority: high
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0022-wp-0019-missing-trace.md`)
- Related branch: process/promote-item-0016 (this issue's own execution
  branch is created off it, per the work plan)

## Summary

PR #21's CI ("Check agent operating contract change traceability") fails:
the PR's total diff (`git diff --name-only <base> <head>`) modifies two
agent operating contract files under
`docs/collaboration/prompt-instruction-change-control.md`'s own
"Agent Operating Contract Files" list —
`docs/collaboration/design-review-perspectives.md` (two reference-path
updates, from WP-0019's LISS-0057) and `docs/collaboration/restoration-ledger.md`
(23 new rows, from WP-0019's LISS-0056/LISS-0057) — but adds no new file
under `docs/collaboration/traces/` to the diff.

Confirmed directly by reading the CI step's own logic
(`.github/workflows/ci.yml`, "Check agent operating contract change
traceability" step): it sets `contract_changed=true` for any diffed path
matching `docs/collaboration/*.md` other than the three excepted record
subdirectories (`traces/`, `reviews/`, `agreements/`), and `trace_added=true`
only for a diffed path matching `docs/collaboration/traces/*.md`. WP-0019's
own archival work moved six pre-existing traces from
`docs/collaboration/traces/` to `docs/archive/collaboration/traces/` — a
rename whose *new* path is under `docs/archive/`, which does not match
`docs/collaboration/traces/*.md`, so it does not satisfy `trace_added`.
Neither `docs/issues/LISS-0056-...md` nor `docs/issues/LISS-0057-...md`
records a new trace for the two contract-file edits themselves (both
issues' own Work Notes were re-read directly to confirm this — neither
mentions creating one).

Note that `docs/collaboration/restoration-ledger.md` is, by its own
nature, an append-only data ledger rather than an instruction/policy
document — but `prompt-instruction-change-control.md`'s own contract-file
list is written as "`docs/collaboration/*.md` (except the record
directories below)," and the three excepted subdirectories
(`traces/`, `reviews/`, `agreements/`) do not include top-level
`restoration-ledger.md`. Under the rule as currently, literally written,
it is a covered contract file, so this issue treats it as one rather than
arguing for a different reading — changing that classification, if
warranted, is its own separate Architecture Path decision (a change to
`prompt-instruction-change-control.md` itself, which is out of this
issue's scope), not something to resolve by reinterpretation here.

## Acceptance Notes

Add one new file under `docs/collaboration/traces/`, named
`docs/collaboration/traces/2026-08-20-wp-0019-contract-file-edits.md`,
using `docs/templates/ai-work-trace.md`. Per
`prompt-instruction-change-control.md`'s Traceability Rule, it must state:

- which contract file(s) changed: `docs/collaboration/design-review-perspectives.md`
  and `docs/collaboration/restoration-ledger.md`.
- why the change was needed: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
  Rule 3 requires every archive move to (a) update any live inbound
  reference in a current Canonical document to the new `docs/archive/`
  path, in the same commit as the move, and (b) record one restoration-
  ledger row per moved file, in the same commit as the move. WP-0019
  (`docs/work-plans/WP-0019-retroactive-adr-0020-archival-batch-1.md`,
  `docs/issues/LISS-0056-...md`, `docs/issues/LISS-0057-...md`) performed
  both for its 23-file archival batch: `design-review-perspectives.md`'s
  two citations of WP-0002's own review record were updated from
  `docs/collaboration/reviews/2026-08-18-wp-0002-...md` to
  `docs/archive/collaboration/reviews/2026-08-18-wp-0002-...md`; ADR
  0016's own Status-section path to WP-0002's file was updated the same
  way (that edit is to `docs/architecture/adr/0016-...md`, which is
  covered by a *different* contract-file pattern —
  `docs/collaboration/*.md` does not match an `.md` file under
  `docs/architecture/`, and `docs/architecture/adr/*.md` is not itself on
  `prompt-instruction-change-control.md`'s covered-file list at all — so
  that specific edit is not part of this gap; only the two
  `docs/collaboration/*.md`-pattern files are).
- what agent behavior is expected to change as a result: none — this is a
  retroactive trace documenting an already-completed, already-reviewed
  archival move (WP-0019's own work-plan-level Reviewer approval,
  `docs/collaboration/reviews/2026-08-20-wp-0019-retroactive-adr-0020-archival-batch-1-review.md`,
  already covers the substance of these two edits). No new rule or agent
  behavior is introduced by this trace; it exists only to satisfy the
  Traceability Rule's own evidentiary requirement for the edits WP-0019
  already made.

Fill the trace's own sections accurately against the real, already-
committed facts (do not invent context that was not actually used):

- **Request/Covering design agreement**: cite
  `docs/collaboration/agreements/2026-08-20-retroactive-adr-0020-batch-1.md`
  (`DA-2026-08-20-02`) — the agreement that authorized WP-0019, whose own
  work is what these two contract-file edits belong to.
- **Canonical issue or work plan**: `docs/work-plans/WP-0019-retroactive-adr-0020-archival-batch-1.md`,
  `docs/issues/LISS-0057-archive-wp-0002-under-adr-0020.md` (the issue
  whose Acceptance Notes actually required both edits).
- **AI Execution Records**: one attempt, describing the actual work
  already done (the 23-file archival move plus the two reference-path
  edits, executed by the Implementation-group subagent session that
  produced WP-0019, per that work plan's own commit history — commit
  `81ddf2a`, "process: archive WP-0002 and its owned records under ADR
  0020 (LISS-0057)").
- **Preflight Validation**: point at
  `docs/work-plans/WP-0019-...md`'s own "Preflight Validation" section,
  which already covers these two edits' correctness (its checks #2 and #3
  are specifically about these two files).
- **Decisions Carried**: cite the Reviewer's approval record
  (`docs/collaboration/reviews/2026-08-20-wp-0019-retroactive-adr-0020-archival-batch-1-review.md`),
  which already independently verified these exact two edits (see that
  record's own Deterministic Verification Output, the `git diff` against
  `docs/architecture/adr/0016-...md` and `docs/collaboration/design-review-perspectives.md`).
- **Verification**: `git diff <base>...<head> -- docs/collaboration/design-review-perspectives.md docs/collaboration/restoration-ledger.md`
  reproduces the exact two-file diff this trace documents.
- **Changed Files**: this trace is written *for* the two contract-file
  edits, but this issue's own commit changes only this new trace file
  itself (the two contract files were already changed by WP-0019 and are
  not re-edited here).

Do not edit `docs/collaboration/design-review-perspectives.md`,
`docs/collaboration/restoration-ledger.md`, or any of WP-0019's own
23 archived/moved files — this issue adds evidence for an
already-completed, already-reviewed change; it does not redo or alter
that change.

## Dependencies

- Parent: `docs/work-plans/WP-0022-wp-0019-missing-trace.md`
- Depends on: `docs/work-plans/WP-0019-retroactive-adr-0020-archival-batch-1.md`
  (the work plan whose edits this trace documents; already Director-closed)
- Blocks: PR #21 (WP-0019's own merge to `main`, now combined with
  item-0018's fix on `process/promote-item-0016`) — CI's traceability
  check cannot pass without it.
- Related: `docs/backlog/item-0019-wp-0019-missing-trace.md`,
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/issues/LISS-0056-archive-wp-0001-under-adr-0020.md`,
  `docs/issues/LISS-0057-archive-wp-0002-under-adr-0020.md`

## Decisions Not Settled by the Design Agreement

- None — scope is fully settled by
  `docs/collaboration/agreements/2026-08-20-wp-0019-missing-trace.md`.

## Context

- Included: `docs/backlog/item-0019-...md`'s full text, PR #21's actual
  second CI failure log (independently fetched via `gh run view --log`),
  `.github/workflows/ci.yml`'s exact traceability-check step,
  `docs/collaboration/prompt-instruction-change-control.md`'s Agent
  Operating Contract Files list and Traceability Rule, WP-0019's own
  Preflight Validation and Reviewer approval records (already covering the
  substance of the two edits this trace documents).
- Omitted: nothing else — this is a narrow, evidence-only addition.
- Assumptions: none. The one ambiguity this issue's own text surfaces
  (whether `restoration-ledger.md` should really be classified as a
  contract file, given its data-ledger nature) is explicitly named as
  out of scope for this issue, not silently resolved.

## References

- `docs/backlog/item-0019-wp-0019-missing-trace.md`
- `docs/collaboration/prompt-instruction-change-control.md`
- `docs/templates/ai-work-trace.md`
- PR #21: https://github.com/nn0cl/llm-loop-project-template/pull/21
- Failing CI run: https://github.com/nn0cl/llm-loop-project-template/actions/runs/32342134917

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0022, scoped per the design agreement. Independently
  confirmed via `gh run view --log` that PR #21's second CI failure
  matches the backlog item's own description, and via direct reading of
  `.github/workflows/ci.yml`'s own step logic and
  `docs/issues/LISS-0056-...md`/`LISS-0057-...md`'s Work Notes that no
  trace was in fact ever created for these two edits. Not yet dispatched.
- 2026-08-20 — Implementation group (Implementer persona). Dispatched from
  WP-0022 on branch `wp-0022-execution` (created from local branch
  `process/promote-item-0016` at commit `1c6a28a`). Wrote
  `docs/collaboration/traces/2026-08-20-wp-0019-contract-file-edits.md`
  using `docs/templates/ai-work-trace.md`, documenting WP-0019's two
  already-completed contract-file edits: `docs/collaboration/design-review-perspectives.md`
  (2 line changes, both citations of WP-0002's review record, made in
  commit `81ddf2a`) and `docs/collaboration/restoration-ledger.md` (23 new
  rows total — 5 added in commit `dfe5030`/LISS-0056, 18 added in commit
  `81ddf2a`/LISS-0057). Every factual claim in the trace (line numbers,
  row counts, commit hashes) was independently reproduced by direct
  command output against the real committed tree (`git show 81ddf2a`,
  `git show dfe5030`, `grep -n`/`grep -c` against the current files), not
  copied unverified from this issue's or WP-0019's own prose. Confirmed
  the CI traceability check's own condition is now satisfied:
  `git diff --name-only main HEAD` includes
  `docs/collaboration/traces/2026-08-20-wp-0019-contract-file-edits.md`.
  Ran `python3 scripts/check-contract-consistency.py` — no regression (see
  this trace's own Verification section and
  `docs/work-plans/WP-0022-...md`'s own Preflight Validation section for
  full pasted output). No edit was made to
  `docs/collaboration/design-review-perspectives.md`,
  `docs/collaboration/restoration-ledger.md`, or any of WP-0019's own 23
  archived files. `Status` updated to `done`.

  **Self-review (short form, planning size `S`, per
  `docs/templates/self-review.md`):**

  - Deterministic precondition: `python3 scripts/check-contract-consistency.py`
    exits 0 ("contract consistency: all checks passed"); `git diff
    --name-only main HEAD` shows exactly the new trace file and this issue
    file, with the trace path present, satisfying the CI check's own
    `trace_added` condition; `git status --porcelain` before commit showed
    no unexpected file touched.
  - Falsification burden — failure scenarios searched for:
    1. The trace cites a commit or line number that does not actually
       match the real diff. Not reproduced: `git show 81ddf2a` and
       `git show dfe5030` were read directly, and the cited line numbers
       (66, 169) and row counts (5, 18, 23 total) were independently
       reproduced via `grep -n`/`grep -c` against the current working
       tree, not taken from either issue's own prose.
    2. `docs/collaboration/restoration-ledger.md`'s "23 new rows" claim
       actually came from a single commit rather than the two-commit
       split (5 from LISS-0056, 18 from LISS-0057) the trace states. Not
       reproduced: `git show dfe5030 -- docs/collaboration/design-review-perspectives.md`
       returns no output (that commit did not touch the file), confirming
       only `81ddf2a` edited `design-review-perspectives.md`, while both
       `dfe5030` and `81ddf2a` each added ledger rows (5 and 18
       respectively, verified by `grep -c '^+|'` on each commit's diff).
    3. This commit accidentally re-edits one of the two contract files or
       one of WP-0019's own archived files. Not reproduced: `git status
       --porcelain` before staging shows only the new trace file and the
       modified `LISS-0061-...md`; no other path appears.

## Verification

- `python3 scripts/check-contract-consistency.py` — no regression.
- `git diff --name-only <base> <head>` (matching the CI step's own
  invocation) includes the new trace file's path, confirming the CI
  check's own `trace_added` condition is now satisfied.
- The new trace file itself accurately cites the real commits, issues,
  and review records involved — not invented content.
