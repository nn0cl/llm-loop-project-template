# Work Plan: Retroactive ADR 0020 archival — batch 1 (WP-0001, WP-0002)

## Goal

- Apply `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`'s
  four-layer model, status vocabulary, and archival mechanism to this
  repository's own existing history, for exactly the first batch the
  Backlog thread authorized: `docs/work-plans/WP-0001-review-issues-minor-fix-path.md`
  and `docs/work-plans/WP-0002-two-group-send-message-loop.md`, and each
  work plan's own owned Evidence-layer records (issues, traces, review
  records). Confirm the drift-prevention checks (`scripts/check-contract-consistency.py`)
  correctly validate the result once real `docs/archive/` content exists —
  the first time either has happened since ADR 0020 landed.

## Scope

- In:
  - Moving WP-0001, LISS-0001, and WP-0001's one trace and two review
    records (5 files) to `docs/archive/...`, per LISS-0056.
  - Moving WP-0002, its nine issues (LISS-0019 through LISS-0027), its six
    traces, and its two review records (18 files) to `docs/archive/...`,
    per LISS-0057.
  - One restoration-ledger row per moved file (23 total), in the same
    commit as each move.
  - The two mandatory Rule-3 reference updates LISS-0057 names (ADR 0016's
    Status section; `design-review-perspectives.md`'s two citations).
  - Re-verifying, directly against the actual files (not against
    `docs/spike/case-0002-.../case.md`'s now-dated spot-check alone), that
    both work plans are still genuinely Rule-2-eligible at execution time.
- Out:
  - `docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md`
    (`DA-2026-08-02-04`) and `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
    (`DA-2026-08-18-01`) — both blocked from archival by a current,
    Accepted ADR's own normative citation (ADR 0012 and ADR 0016
    respectively); see LISS-0056 and LISS-0057's own "Explicit exclusion"
    sections.
  - `docs/backlog/item-0004-two-group-send-message-loop.md` — Rule-2
    eligible in principle, but deliberately deferred to a later, separate
    batch given its markedly larger reference graph; see LISS-0057's own
    "Explicit exclusion" section.
  - Any ADR (zero are Rule-2-eligible in this repository today).
  - WP-0003 through WP-0018 and their own owned records — a later, separate
    batch, each re-verified fresh at that time, per
    `docs/issues/LISS-0055-...md`'s own "Proposed batching plan."
  - Any change to ADR 0020's own rules.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0056 | done | S | S | N/A | LISS-0055 | - | process/promote-item-0016 |
| LISS-0057 | done | M | M | N/A | LISS-0055 | - | process/promote-item-0016 |

## Recommended Order

1. LISS-0056 (WP-0001 batch) — smaller, no mandatory Canonical-document
   reference updates; lands first as an independently reviewable commit.
2. LISS-0057 (WP-0002 batch) — larger, includes the two mandatory Rule-3
   reference updates; sequenced second so its own Preflight run also
   exercises the drift-prevention checks against LISS-0056's already-landed
   archive content, not only its own.

## Current Next Issue

- Issue: none
- Reason it is unblocked: both LISS-0056 and LISS-0057 are `Status: done`;
  Preflight Validation (below) is the only remaining step before
  submitting this work plan to the work-plan-level Reviewer.
- Reopening request needed: no.

## Minor Fix Path

Not applicable to the initial execution of this work plan — both issues are
new archival moves under an already-Accepted ADR (0020), not corrections to
previously accepted work.

## Preflight Validation

Run by the Implementation group after both LISS-0056 and LISS-0057 landed
and were self-reviewed. **Result: pass.** All six required checks below
were run for real against the actual committed tree (not against either
issue's own self-review record alone); full output pasted, not
summarized.

1. `python3 scripts/check-contract-consistency.py` — full output:

   ```text
   contract consistency: all checks passed
   ```

2. `grep -rn "docs/work-plans/WP-0002-two-group-send-message-loop.md"
   docs/architecture/ docs/collaboration/*.md docs/templates/` — full
   output:

   ```text
   docs/collaboration/restoration-ledger.md:51:| 2026-08-20 | `docs/work-plans/WP-0002-two-group-send-message-loop.md` | 81ddf2a8afcdda027f713fcb35242eb0d793c168 | N/A | `docs/archive/work-plans/WP-0002-two-group-send-message-loop.md` | archived | Director-closed (2026-08-18); all nine owned issues at terminal `Status: done` (corrected by commit `73ab2ce`/PR #20, verified independently in `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`'s post-close Addendum); no open `Type: review-finding` issue names it. |
   ```

   The single hit is the restoration ledger's own `source_path` column —
   an Evidence-layer historical record of the pre-move path, not a
   Canonical document pointing at a dead path. Zero hits in
   `docs/architecture/` or `docs/templates/`, and zero in any other
   `docs/collaboration/*.md` file. Confirms the ADR 0016 reference update
   landed and no other current Canonical document was missed.

3. `grep -rn "docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md"
   docs/collaboration/design-review-perspectives.md` — as literally
   written, this returns **zero hits** (exit code 1) once the fix is
   correctly applied: the correct archive path is
   `docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`,
   and inserting `archive/` immediately after `docs/` means the pre-move
   path string is no longer a substring of the post-move one — so this
   exact command cannot show a passing result after a correct fix. This
   is an imprecision in this check's own wording (also present in
   LISS-0057's own Verification section, flagged there in Work Notes),
   not a real defect. The equivalent corrected search (matching the
   filename without the stale `docs/collaboration/` prefix) confirms both
   citations:

   ```text
   $ grep -rn "2026-08-18-wp-0002-two-group-send-message-loop-review.md" docs/collaboration/design-review-perspectives.md
   docs/collaboration/design-review-perspectives.md:66:`docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`
   docs/collaboration/design-review-perspectives.md:169:`docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`,
   ```

4. `git log --follow --oneline -- <path>` run exhaustively (not sampled)
   against all 23 destination paths; every one returned 2 or more
   commits, confirming a preserved rename in every case, not
   delete+recreate:

   ```text
    2 : docs/archive/work-plans/WP-0001-review-issues-minor-fix-path.md
    2 : docs/archive/issues/LISS-0001-review-issues-minor-fix-path.md
    2 : docs/archive/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md
    2 : docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md
    2 : docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path-arbiter.md
    7 : docs/archive/work-plans/WP-0002-two-group-send-message-loop.md
    4 : docs/archive/issues/LISS-0019-adr-0016-two-group-topology.md
    4 : docs/archive/issues/LISS-0020-personas-group-mapping.md
    4 : docs/archive/issues/LISS-0021-ai-human-scheme-loop-update.md
    4 : docs/archive/issues/LISS-0022-cross-session-messaging-protocol.md
    4 : docs/archive/issues/LISS-0023-session-start-standing-pair.md
    4 : docs/archive/issues/LISS-0024-implementation-group-worktree-rule.md
    4 : docs/archive/issues/LISS-0025-design-agreement-backlog-gate-reconciliation.md
    4 : docs/archive/issues/LISS-0026-backlog-readme-bulk-gate.md
    5 : docs/archive/issues/LISS-0027-at-tdd-process-adr-0016-qualification.md
    2 : docs/archive/collaboration/traces/2026-08-18-liss-0020-personas-group-mapping.md
    2 : docs/archive/collaboration/traces/2026-08-18-liss-0021-ai-human-scheme-loop-update.md
    2 : docs/archive/collaboration/traces/2026-08-18-liss-0022-cross-session-messaging-protocol.md
    3 : docs/archive/collaboration/traces/2026-08-18-liss-0023-session-start-standing-pair.md
    4 : docs/archive/collaboration/traces/2026-08-18-liss-0024-implementation-group-worktree-rule.md
    2 : docs/archive/collaboration/traces/2026-08-18-liss-0025-design-agreement-backlog-gate-reconciliation.md
    3 : docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md
    2 : docs/archive/collaboration/reviews/2026-08-18-liss-0027-at-tdd-process-adr-0016-qualification-review.md
   ```

5. `docs/collaboration/restoration-ledger.md` row count and hash check:

   ```text
   $ grep -c "| archived |" docs/collaboration/restoration-ledger.md
   23

   $ grep -oE '\| [0-9a-f]{40} \|' docs/collaboration/restoration-ledger.md | sort -u
   | 81ddf2a8afcdda027f713fcb35242eb0d793c168 |
   | dfe5030a7ead7e8e1bcf472e47ce6af4022f287c |
   ```

   Exactly 23 new rows (5 from LISS-0056 + 18 from LISS-0057), each with a
   real, 40-character `source_commit` hash, exactly one of two values
   (matching the two moves' own final commit hashes) — no `PENDING`
   placeholder remains anywhere in the file.

6. Re-confirmation that
   `docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md`
   and `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
   are unchanged and un-moved:

   ```text
   $ git status --short -- docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md
   (no output)

   $ git diff --stat docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md
   (no output)

   $ ls -la docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md
   -rw-r--r--@ 1 nn0cl  staff   5511 ... 2026-08-02-review-issue-and-minor-fix-path.md
   -rw-r--r--@ 1 nn0cl  staff  17899 ... 2026-08-18-two-group-send-message-loop.md
   ```

   Both files present, unmodified, at their original paths.

**Deviations found during Preflight** (both already recorded in
LISS-0057's own Work Notes, restated here for the work-plan-level
record): the hash self-reference correction mechanic (a commit cannot
literally contain its own final hash via a single amend — resolved with a
small follow-up correction commit for each of LISS-0056 and LISS-0057
instead), and the item-3/item-2-in-LISS-0057 grep command's wording
(the literal command necessarily shows zero hits once the fix is correct,
not "both hits point at the archive path" — an equivalent corrected
search confirms the underlying fact is true). Neither is a defect in the
archival work itself.

## Review Summary Packet

Filled in by the Implementation group once Preflight passes, before
submitting to the work-plan-level Reviewer, per
`docs/collaboration/design-agreement.md`'s "Review Summary Packet" section.

- **Scope**: archived WP-0001 and WP-0002 and their 23 combined owned
  issue/trace/review-record files under ADR 0020; updated 2 live inbound
  references in current Canonical documents; added 23 restoration-ledger
  rows. No application code, specification, or ADR content changed.
- **Current canonical documents**: none newly established — this work plan
  applies an already-Accepted ADR (0020); `docs/architecture/adr/0016-...md`
  and `docs/collaboration/design-review-perspectives.md` are amended
  in-place (path updates only), not superseded.
- **Changed files**: the 23 `git mv` moves (per LISS-0056/LISS-0057's own
  tables), `docs/collaboration/restoration-ledger.md` (23 new rows), ADR
  0016 (one path edit), `design-review-perspectives.md` (two path edits).
- **Findings**: none opened or resolved by this work plan.
- **Disposition**: Preflight Validation passed (all 6 required checks,
  full output above); both LISS-0056 and LISS-0057 are `Status: done`
  with self-review records recorded in their own Work Notes (short form
  for LISS-0056, full form for LISS-0057). Ready for the work-plan-level
  Reviewer pass in a separate context.
- **Remaining blockers**: none found. Two non-blocking deviations from
  the plan's own literal text were found and recorded (not silently
  resolved): (1) the ledger's `source_commit` self-reference cannot be
  produced by a single `git commit --amend`, since amending changes the
  commit's own hash again — resolved with a small follow-up correction
  commit for each issue instead (LISS-0056: `d02eb3c`; LISS-0057:
  `42f4ea6`); (2) LISS-0057's own Verification section's second `grep`
  command (and this file's own Preflight item 3, mirroring it) shows zero
  hits once the fix is correctly applied, not "both hits point at the
  archive path" as originally worded — confirmed via an equivalent
  corrected search that the underlying fact (both citations updated) is
  true. Neither affects the archival work's correctness.
- **Verification result**: see this file's own Preflight Validation
  section above — all 6 required checks passed with full output pasted.
- **Next approval required**: boundary-conformance (did the move stay
  inside ADR 0020's own rules, correctly excluding the two blocked design
  agreements and item-0004) and evidence-sufficiency (is every move backed
  by a real ledger row and preserved git history) — the two approval types
  most directly at stake for a pure archival move; specification-conformance
  and phase-correctness are secondary since no specification or AT-TDD
  phase content is touched.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-20-wp-0019-retroactive-adr-0020-archival-batch-1-review.md`
— **Approved** (2026-08-20, Reviewer persona, Design & Review group
standing session, separate context from the Implementation-group subagent
session that executed LISS-0056/LISS-0057 in its own worktree/branch).

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

No `Type: review-finding` issues were opened — the review found no defect
requiring correction. Both deviations the Implementation group flagged
during execution (the ledger's hash self-reference resolution mechanic;
the Verification-section grep command that cannot literally pass post-fix
by construction) were independently confirmed as genuine plan-text
imprecisions, not defects in the archival work itself; the review record's
own "Reasons" section carries a non-blocking suggestion for a future ADR
0020 documentation clarification.

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves.

- Date: 2026-08-20
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-20-wp-0019-retroactive-adr-0020-archival-batch-1-review.md`,
  Approved — the Reviewer independently re-ran `scripts/check-contract-consistency.py`
  against a fresh `git archive` of the branch, confirmed all 23 moves show
  `R100` similarity, and independently confirmed the two Implementer-flagged
  deviations were genuine plan-wording gaps, not defects) via the Backlog
  thread, which independently confirmed a clean
  `scripts/check-contract-consistency.py` run from a detached checkout,
  `docs/archive/` containing real moved content, and 25 rows (23 entries
  plus header/separator) in `docs/collaboration/restoration-ledger.md`.
- Next direction: closed with "はい". This is item-0016's first archival
  batch only (WP-0001, WP-0002) — report back with what was learned before
  proposing the next batch, per the original mandate. Merged content sits
  on `process/promote-item-0016`. Push/PR/merge-to-main are separate
  explicit actions, pending.
- New design agreement (if any): none opened by this close.

## Risks

- A move missed by this work plan's own reference sweep could leave a
  current Canonical document pointing at a path that no longer exists.
  Mitigated by the Preflight's explicit `grep` re-checks (items 2-3 above)
  and by `check-contract-consistency.py`'s own dangling-reference and
  Entry-archive-reference checks, which are exercised against real archive
  content for the first time by this work plan.
- `LISS-0052` (open, low-priority: a fenced-code-block gap in
  `check_no_archive_reference_from_entry`) remains open; low risk here
  since neither reference update this work plan makes sits inside a fenced
  code block, and no Entry document (`agent-quickstart.md`, `CLAUDE.md`,
  `README*.md`) cites any of the 23 moved paths — confirmed by the same
  `grep` sweep. Re-check before a larger, later batch, per LISS-0052's and
  case-0002's own notes.
- Item-0004's deliberate exclusion from this batch (see Scope, Out) leaves
  it as a nearer-term follow-up than WP-0003-through-WP-0018, since it is
  already Rule-2-eligible; not resolved here to keep this batch's own
  review surface bounded.

## Verification Plan

- `python3 scripts/check-contract-consistency.py` after both issues land.
- Targeted `grep` sweep confirming the two mandatory reference updates
  landed and no other current Canonical document was missed.
- `git log --follow` confirmation of preserved history for each moved file.
- Restoration-ledger row count and content check (23 new rows).
- Confirmation that `DA-2026-08-02-04` and `DA-2026-08-18-01` are untouched.
- Independent work-plan-level Reviewer approval, in a separate context.
