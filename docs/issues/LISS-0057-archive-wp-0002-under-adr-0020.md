# LISS-0057: Archive WP-0002 and its owned records under ADR 0020

## Metadata

- Local issue ID: LISS-0057
- GitHub issue: none
- Status: done
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: docs-only
- Type: process
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A — first attempt. Larger than LISS-0056
  (18 files vs. 5, plus two mandatory Rule-3 reference updates in current
  Canonical documents), still within Minor-Fix-adjacent mechanical scope.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0019-retroactive-adr-0020-archival-batch-1.md`)
- Related branch: process/promote-item-0016 (this issue's own execution
  branch is created off it, per the work plan)

## Summary

Apply `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
Rules 2-3 to `docs/work-plans/WP-0002-two-group-send-message-loop.md` and
its owned Evidence-layer records (9 issues, 6 traces, 2 review records):
move each file verbatim to `docs/archive/...`, record one restoration-ledger
row per move in the same commit, and update the two live inbound references
this issue's own research found in current Canonical documents (Rule 3).
Leave `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
(`DA-2026-08-18-01`) untouched (see "Explicit exclusion" below).

## Acceptance Notes

### Files to move (18 total), verbatim, via `git mv`

| # | Source | Destination |
| --- | --- | --- |
| 1 | `docs/work-plans/WP-0002-two-group-send-message-loop.md` | `docs/archive/work-plans/WP-0002-two-group-send-message-loop.md` |
| 2 | `docs/issues/LISS-0019-adr-0016-two-group-topology.md` | `docs/archive/issues/LISS-0019-adr-0016-two-group-topology.md` |
| 3 | `docs/issues/LISS-0020-personas-group-mapping.md` | `docs/archive/issues/LISS-0020-personas-group-mapping.md` |
| 4 | `docs/issues/LISS-0021-ai-human-scheme-loop-update.md` | `docs/archive/issues/LISS-0021-ai-human-scheme-loop-update.md` |
| 5 | `docs/issues/LISS-0022-cross-session-messaging-protocol.md` | `docs/archive/issues/LISS-0022-cross-session-messaging-protocol.md` |
| 6 | `docs/issues/LISS-0023-session-start-standing-pair.md` | `docs/archive/issues/LISS-0023-session-start-standing-pair.md` |
| 7 | `docs/issues/LISS-0024-implementation-group-worktree-rule.md` | `docs/archive/issues/LISS-0024-implementation-group-worktree-rule.md` |
| 8 | `docs/issues/LISS-0025-design-agreement-backlog-gate-reconciliation.md` | `docs/archive/issues/LISS-0025-design-agreement-backlog-gate-reconciliation.md` |
| 9 | `docs/issues/LISS-0026-backlog-readme-bulk-gate.md` | `docs/archive/issues/LISS-0026-backlog-readme-bulk-gate.md` |
| 10 | `docs/issues/LISS-0027-at-tdd-process-adr-0016-qualification.md` | `docs/archive/issues/LISS-0027-at-tdd-process-adr-0016-qualification.md` |
| 11 | `docs/collaboration/traces/2026-08-18-liss-0020-personas-group-mapping.md` | `docs/archive/collaboration/traces/2026-08-18-liss-0020-personas-group-mapping.md` |
| 12 | `docs/collaboration/traces/2026-08-18-liss-0021-ai-human-scheme-loop-update.md` | `docs/archive/collaboration/traces/2026-08-18-liss-0021-ai-human-scheme-loop-update.md` |
| 13 | `docs/collaboration/traces/2026-08-18-liss-0022-cross-session-messaging-protocol.md` | `docs/archive/collaboration/traces/2026-08-18-liss-0022-cross-session-messaging-protocol.md` |
| 14 | `docs/collaboration/traces/2026-08-18-liss-0023-session-start-standing-pair.md` | `docs/archive/collaboration/traces/2026-08-18-liss-0023-session-start-standing-pair.md` |
| 15 | `docs/collaboration/traces/2026-08-18-liss-0024-implementation-group-worktree-rule.md` | `docs/archive/collaboration/traces/2026-08-18-liss-0024-implementation-group-worktree-rule.md` |
| 16 | `docs/collaboration/traces/2026-08-18-liss-0025-design-agreement-backlog-gate-reconciliation.md` | `docs/archive/collaboration/traces/2026-08-18-liss-0025-design-agreement-backlog-gate-reconciliation.md` |
| 17 | `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md` | `docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md` |
| 18 | `docs/collaboration/reviews/2026-08-18-liss-0027-at-tdd-process-adr-0016-qualification-review.md` | `docs/archive/collaboration/reviews/2026-08-18-liss-0027-at-tdd-process-adr-0016-qualification-review.md` |

Note: LISS-0019, LISS-0026, and LISS-0027 have no individual trace file
(confirmed directly against WP-0002's own Preflight Validation section,
item 3 — six traces cover LISS-0020 through LISS-0025 only). Do not
fabricate traces for the missing three; this is expected, not a gap to
fix as part of this archival issue.

Add one restoration-ledger row per moved file (18 rows total) to
`docs/collaboration/restoration-ledger.md`, `classification: archived`,
`source_tag: N/A`, real `source_commit` hash of this move commit. Suggested
`reason` text per type (adjust per file, keep to one sentence each naming
the Rule 2 trigger):

- WP-0002: "Director-closed (2026-08-18); all nine owned issues at
  terminal `Status: done` (corrected by commit `73ab2ce`/PR #20, verified
  independently in `docs/spike/case-0002-.../case.md`'s post-close
  Addendum); no open `Type: review-finding` issue names it."
- Each of the 9 issues: "Terminal `Status: done`; owning work plan
  (WP-0002) archived in the same commit."
- Each of the 6 traces: "No unresolved obligation, new approval boundary,
  or unique review evidence outstanding; owning work plan (WP-0002)
  archived in the same commit (ADR 0020 Rule 4)."
- Each of the 2 review records: "Owning/reviewed work plan (WP-0002)
  archived in the same commit (ADR 0020 Rule 2: review record eligible
  once the work plan it reviewed is archived)."

### Mandatory Rule-3 reference updates (in the same commit as the moves)

Two live inbound references in current Canonical documents were found by
this issue's own research and must be updated to point at the new
`docs/archive/` path (not left pointing at a path that no longer exists):

1. `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`,
   Status section, line: "Follow-up issues: LISS-0020 through LISS-0026
   (`docs/work-plans/WP-0002-two-group-send-message-loop.md`)." — update
   the parenthetical path to
   `docs/archive/work-plans/WP-0002-two-group-send-message-loop.md`. This is
   a locational pointer ("see the historical record" style, per Rule 3),
   not a normative dependency of ADR 0016's own Accepted status (that
   grounding is `DA-2026-08-18-01`, which is not moving — see "Explicit
   exclusion" below) — so updating the path is sufficient; no other change
   to this ADR is authorized by this issue.
2. `docs/collaboration/design-review-perspectives.md`, two citations of
   `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`
   (in the "Re-verify state that could have changed underneath you" and
   "Verify a claimed authority or origin independently of its own claim"
   perspective entries) — update both to
   `docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`.
   These are historical-provenance citations for lessons the document
   already states in full, not content the document's own validity depends
   on — the Rule-3 non-blocking case, confirmed in
   `docs/spike/case-0002-.../case.md`'s post-close Addendum.

Search for, and correct, any other direct-path citation of the 18 moved
files in `docs/architecture/adr/*.md`, `docs/collaboration/*.md`, or
`docs/templates/*.md` this issue's own research may not have caught (a
targeted `grep -rn "<old-path>"` per moved file against those three
locations, before finalizing the commit) — do not assume the two
references named above are exhaustive without checking. ID-only mentions
(e.g., "`LISS-0022`" cited by number, not by file path, such as
`docs/architecture/adr/0016...md` line 285 and
`docs/collaboration/session-start-and-resume.md` line 147, both naming
LISS-0022 as the issue that produced the still-current
`cross-session-messaging.md`) are not path references and do not need
updating.

### Explicit exclusion — do not move

- `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
  (`DA-2026-08-18-01`). ADR 0016's own Status section: "`Accepted` status
  requires a design agreement with the Director covering the decision.
  That agreement is `DA-2026-08-18-01`, reached through the multi-turn
  dialogue quoted in its own Direction section..." — quoted directly from
  in ADR 0016's own Context section, not a passing mention. ADR 0020 Rule
  2's opening clause blocks archival of any document "a current Canonical
  document still references by more than a passing mention," regardless of
  the document's own type's terminal status. This agreement stays in place
  regardless of WP-0002's own archival.
- `docs/backlog/item-0004-two-group-send-message-loop.md` — out of scope
  for this batch specifically (not this batch's decision to leave it
  archival-ineligible; its own Rule-2 backlog-item trigger is in fact
  satisfied, since it is `promoted` and its resulting work plan (WP-0002)
  is Director-closed). It carries markedly more inbound references across
  the repository than the 18 files above (at minimum: `DA-2026-08-18-04`,
  ADR 0016 itself, LISS-0040, WP-0011, item-0005, item-0007, item-0012, and
  LISS-0031 — not individually triaged by this issue for
  blocking-vs.-Rule-3 disposition). Keeping this batch to exactly WP-0001's
  and WP-0002's own directly-owned issues/traces/reviews keeps the batch
  small and reviewable, per `docs/spike/case-0002-.../case.md`'s own
  Option-B rationale; item-0004's own archival is deferred to a later,
  separate batch that can give its full reference graph the same
  individual scrutiny this issue gave WP-0002's.
- `docs/collaboration/agreements/2026-08-18-coordinator-message-correction.md`
  — a separate, later design agreement that cites `DA-2026-08-18-01`; not
  itself in WP-0002's own issue/trace/review set and not archived by this
  issue.

## Dependencies

- Parent: `docs/work-plans/WP-0019-retroactive-adr-0020-archival-batch-1.md`
- Depends on: `docs/issues/LISS-0055-retroactive-adr-0020-batching-aggressiveness-decision.md`
  (`Status: done`), `docs/issues/LISS-0056-archive-wp-0001-under-adr-0020.md`
  (sequencing convenience only — not a hard dependency; the two issues
  touch disjoint file sets and could run in either order, but running
  LISS-0056 first keeps the batch's own commits small and independently
  reviewable, per the work plan's Recommended Order)
- Blocks: none
- Related: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `docs/collaboration/restoration-ledger.md`,
  `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`

## Decisions Not Settled by the Design Agreement

- None — this issue's scope is fully settled by
  `docs/collaboration/agreements/2026-08-20-retroactive-adr-0020-batch-1.md`
  (`DA-2026-08-20-02`).

## Context

- Included: ADR 0020 full text, WP-0002's own file (including its own
  Preflight Validation trace-list), all 9 issue files, all 6 trace files,
  both review record files, ADR 0016's full text, `design-review-perspectives.md`'s
  full text, a repository-wide `grep` sweep of `docs/architecture/adr/`,
  `docs/collaboration/*.md`, and `docs/templates/*.md` for inbound
  references to each of the 18 moved files' paths and to
  `docs/backlog/item-0004-...md`.
- Omitted: WP-0001 and its own records (LISS-0056's scope, not this
  issue's); WP-0003 through WP-0018; full individual disposition triage of
  every document that cites `item-0004` (explicitly deferred, see
  "Explicit exclusion" above, not silently skipped).
- Assumptions: none beyond what case-0002's Addendum and this issue's own
  Acceptance Notes state explicitly.

## References

- `docs/architecture/adr/0020-document-and-log-lifecycle-model.md` (Rules
  2, 3, 4, 5)
- `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`
  (Selection section and post-close Addendum)
- `docs/issues/LISS-0055-retroactive-adr-0020-batching-aggressiveness-decision.md`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0019, scoped per the design agreement. Not yet dispatched.
- 2026-08-20 — Implementation group (Implementer persona). Re-verified
  Rule-2 eligibility directly against the actual files before moving
  anything: `docs/work-plans/WP-0002-two-group-send-message-loop.md`'s
  own Issue Graph lists all nine issues (LISS-0019 through LISS-0027) as
  `done`, and its own Work-Plan Close section states "Date: 2026-08-18"
  with both Reviewer approvals read; a repository-wide `grep` for `Type:
  review-finding` issues naming WP-0002 found none open. Moved all 18
  files listed in this issue's Acceptance Notes table via `git mv` in the
  same commit as the two mandatory Rule-3 reference updates (ADR 0016's
  Status section path; both `design-review-perspectives.md` citations).
  Ran the additional `grep` sweep the Acceptance Notes require (a
  separate-context agent, since the sweep spans many files) across
  `docs/architecture/adr/*.md`, `docs/collaboration/*.md`, and
  `docs/templates/*.md` for all 18 old paths: no dangling reference found
  beyond the two already fixed.
- 2026-08-20 — Implementation group (Implementer persona). Same hash
  self-reference issue as LISS-0056 (see that issue's own Work Notes):
  the ledger rows were committed with `source_commit: PENDING`, the move
  commit's real hash (`81ddf2a8afcdda027f713fcb35242eb0d793c168`)
  captured via `git rev-parse HEAD`, then corrected in a small follow-up
  commit (`42f4ea6...`) rather than an amend (an amend would change the
  commit's own hash again, since the hash is a function of its content
  and the content now includes a hash value).
- 2026-08-20 — Implementation group (Implementer persona). Verification
  wording issue found: this issue's own Verification section's second
  `grep` command (`grep -rn "docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md"
  docs/collaboration/design-review-perspectives.md`) returns **zero**
  hits once the fix is correctly applied — not "both hits now point at
  the docs/archive/ path" as the Verification section's prose predicts.
  Reason: the correct archive path is
  `docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`,
  and inserting `archive/` after `docs/` breaks the original string as a
  substring of the new one (`docs/collaboration/reviews/...` is no longer
  contained inside `docs/archive/collaboration/reviews/...`), so a grep
  for the pre-move path necessarily finds nothing once the fix is
  correct. Confirmed this is a wording issue, not a real defect, by
  running the equivalent corrected search (matching the filename without
  the stale `docs/collaboration/` prefix) — see Deterministic
  Verification Output below; both citations do read the new
  `docs/archive/` path. Flagging this as a plan/issue-text imprecision to
  report back, not resolving it by silently rewriting this issue's own
  Verification section.
- 2026-08-20 — Implementation group (Implementer persona). Full-form
  self-review (planning size `M`, per `docs/templates/self-review.md`,
  using `docs/templates/review-record.md`'s Deterministic Verification
  Output and Falsification Search sections, filled out as the
  Implementer):

  ### Deterministic Verification Output

  ```text
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed

  $ grep -rn "docs/work-plans/WP-0002-two-group-send-message-loop.md" docs/architecture/ docs/collaboration/*.md docs/templates/
  docs/collaboration/restoration-ledger.md:51:| 2026-08-20 | `docs/work-plans/WP-0002-two-group-send-message-loop.md` | 81ddf2a8afcdda027f713fcb35242eb0d793c168 | N/A | `docs/archive/work-plans/WP-0002-two-group-send-message-loop.md` | archived | Director-closed (2026-08-18); all nine owned issues at terminal `Status: done` (corrected by commit `73ab2ce`/PR #20, verified independently in `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`'s post-close Addendum); no open `Type: review-finding` issue names it. |
  (the one hit is the ledger's own source_path column, an Evidence-layer
  record of the old path for recovery purposes, not a Canonical document
  pointing at a dead path; zero hits in docs/architecture/ or
  docs/templates/, and zero in any other docs/collaboration/*.md file —
  confirms the ADR 0016 reference update landed and no other current
  Canonical document was missed)

  $ grep -rn "docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md" docs/collaboration/design-review-perspectives.md
  (no output — see Work Notes above: this is expected once the fix is
  correct, since "docs/archive/collaboration/..." does not contain
  "docs/collaboration/..." as a substring; this literal command cannot
  show a passing result post-fix)

  $ grep -rn "2026-08-18-wp-0002-two-group-send-message-loop-review.md" docs/collaboration/design-review-perspectives.md
  docs/collaboration/design-review-perspectives.md:66:`docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`
  docs/collaboration/design-review-perspectives.md:169:`docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`,
  (corrected search, filename only — confirms both citations now read
  the docs/archive/ path)

  $ git log --follow --oneline -- docs/archive/work-plans/WP-0002-two-group-send-message-loop.md
  81ddf2a process: archive WP-0002 and its owned records under ADR 0020 (LISS-0057)
  73ab2ce process: sync WP-0002's nine issue statuses to done
  7f82227 process: record work-plan close for WP-0002; capture coordinator-message correction
  9dac0eb docs: record separate-context Reviewer confirmation for LISS-0027
  88cb258 docs: record work-plan-level Reviewer approval for WP-0002 (LISS-0020-0026)
  dad873b docs: record WP-0002 issue-graph progress and Preflight Validation pass (LISS-0020-0026)
  48a128d process: design phase for standing two/three-layer send_message loop
  (7 commits — pre-move history fully preserved, not delete+recreate)

  All 23 combined moved files (5 from LISS-0056 + 18 from this issue)
  were checked exhaustively for `git log --follow` history preservation,
  not only WP-0002's own file — every one returned 2 or more commits,
  confirming a rename in every case (full per-file counts recorded in
  this session's own command output, summarized: WP-0001 set 2 commits
  each; WP-0002 7 commits; LISS-0019/20/21/22/23/24/25/26 4 commits each;
  LISS-0027 5 commits; traces 2-4 commits each; both review records 2-3
  commits each).

  $ grep -c "| archived |" docs/collaboration/restoration-ledger.md
  23
  (5 from LISS-0056 + 18 from this issue = 23, matches both issues'
  own expected totals)
  ```

  ### Falsification Search

  | # | Failure scenario searched for | Grounds it does not occur | Result |
  |---|---|---|---|
  | 1 | A current Canonical document other than the two named (ADR 0016, `design-review-perspectives.md`) still points at one of the 18 old paths | Dedicated `grep` sweep (separate-context agent) across `docs/architecture/adr/*.md`, `docs/collaboration/*.md` (top-level), and `docs/templates/*.md` for all 18 old paths found zero dangling hits beyond the two already fixed; sanity-checked against the two known-good fixes to confirm the search methodology itself was sound | not reproduced |
  | 2 | A moved file's content was altered rather than moved verbatim (`git mv` silently combined with an edit) | `git status`/`git diff --stat` for the move commit (`81ddf2a`) shows all 18 entries as `rename ... (100%)` — a 100% similarity rename means git detected zero content difference between old and new blob; a content edit would show as a lower similarity percentage or a separate modify line | not reproduced |
  | 3 | A restoration-ledger row's `source_commit` does not match the actual move commit | Initially true by construction (`PENDING` placeholder, then a stale hash would have resulted from an amend — see Work Notes above on why amend does not converge); resolved via a follow-up correction commit (`42f4ea6`) that set all 18 `source_commit` values to `81ddf2a8afcdda027f713fcb35242eb0d793c168`, verified via `git show --stat 81ddf2a` showing exactly the 18 renames plus the ADR 0016 and `design-review-perspectives.md` edits in that same commit | not reproduced (after the correction commit) |
  | 4 | `check-contract-consistency.py` passing locally does not mean the work plan's own Issue Graph and this issue's `Status` field stayed in sync | Checker's own "Issue status sync" rule (#7) explicitly compares LISS `Status` fields against their work plan's Issue Graph row; ran the checker after setting this issue's `Status: done` and syncing WP-0019's Issue Graph row to `done` — passed with zero failures, confirming sync, not merely absence of a check | not reproduced |

  ### Scenarios Not Searched

  - Whether a document outside the three Canonical-document locations
    named in this issue's own Acceptance Notes (i.e., outside
    `docs/architecture/adr/*.md`, `docs/collaboration/*.md`,
    `docs/templates/*.md`) cites one of the 18 old paths — out of this
    issue's own defined check scope (Evidence-layer documents such as
    other issues/traces/reviews are expected to still use ID-only or
    historical references, per ADR 0020 Rule 1's own layer definitions,
    and are not required to be updated).
  - Whether `docs/backlog/item-0004-two-group-send-message-loop.md`'s own
    larger reference graph is internally consistent — explicitly out of
    scope per this issue's own "Explicit exclusion" section and the work
    plan's Scope/Out list.

## Verification

- After the moves and reference updates:
  `python3 scripts/check-contract-consistency.py` shows no new failures
  attributable to this change (dangling references, mirror parity, or
  Entry-archive-reference checks) — paste the full output.
- `grep -rn "docs/work-plans/WP-0002-two-group-send-message-loop.md"
  docs/architecture/ docs/collaboration/*.md docs/templates/` returns no
  hits outside `docs/archive/` and the restoration ledger (confirms the
  ADR 0016 reference update landed).
- `grep -rn "docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md"
  docs/collaboration/design-review-perspectives.md` shows both hits now
  point at the `docs/archive/` path.
- `git log --follow -- docs/archive/work-plans/WP-0002-two-group-send-message-loop.md`
  shows the file's pre-move history is preserved.
- `docs/collaboration/restoration-ledger.md` contains exactly 18 new rows
  after this issue's commit (23 total combined with LISS-0056's 5), one per
  moved file, each with a real `source_commit` hash matching the move
  commit.
