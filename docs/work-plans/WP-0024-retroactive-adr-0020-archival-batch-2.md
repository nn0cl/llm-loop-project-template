# Work Plan: Retroactive ADR 0020 archival — batch 2 (WP-0003 through WP-0009)

## Goal

- Apply ADR 0020's archival mechanism to batch 2, authorized by the
  Backlog thread in `docs/issues/LISS-0065-...md`'s own Work Notes:
  WP-0003, WP-0005, WP-0007, WP-0008, WP-0009 (fully eligible, including
  their own design agreements) and WP-0004, WP-0006 (eligible except
  their design agreements, which are normatively cited by ADR 0017 and
  ADR 0018 respectively). Also fold in two small housekeeping fixes the
  Backlog thread authorized in the same decision.

## Scope

- In:
  - LISS-0066: archive WP-0003, WP-0005, WP-0007, WP-0008, WP-0009 and
    all their owned issues/traces/reviews/agreements (21 files).
  - LISS-0067: archive WP-0004, WP-0006 and their owned
    issues/traces/reviews (11-12 files, exact count depends on the
    LISS-0029 trace verification named in that issue), excluding their
    two blocked design agreements, plus the two mandatory ADR
    reference-path updates (ADR 0017, ADR 0018).
  - LISS-0068: fix the five stale backlog `Links` fields (items
    0005-0009) and WP-0021's own empty Work-Plan Close `Date:` field.
  - Restoration-ledger rows for every moved file.
- Out:
  - `DA-2026-08-18-03` (WP-0004) and `DA-2026-08-18-05` (WP-0006) — both
    blocked, stay in place.
  - Any ADR (zero eligible, unchanged finding).
  - WP-0010 through WP-0023 and their own owned records — a later,
    separate batch. WP-0019 through WP-0023 specifically recommended for
    an even longer hold, per `LISS-0065`'s own proposal, agreed by the
    Backlog thread without redirection.
  - Any other backlog item's own `Links` field beyond the five named in
    LISS-0068 — not part of this batch's authorized housekeeping scope.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0066 | done | M | M | N/A | LISS-0065 | - | process/item-0016-batch-2-proposal |
| LISS-0067 | done | M | M | N/A | LISS-0065 | - | process/item-0016-batch-2-proposal |
| LISS-0068 | done | S | S | N/A | LISS-0065 | - | process/item-0016-batch-2-proposal |

## Recommended Order

1. LISS-0066 (the simpler five-work-plan archival set) — lands first as
   an independently reviewable commit.
2. LISS-0067 (the two-work-plan set with blocked agreements and mandatory
   reference updates) — sequenced second so its own Preflight also
   exercises the drift-prevention checks against LISS-0066's already-
   landed archive content.
3. LISS-0068 (the two housekeeping fixes) — sequenced last since its own
   backlog-`Links`-field updates may need to point at either a live or an
   already-archived work-plan path, depending on whether LISS-0066/0067
   landed first (they do, per this order).

## Current Next Issue

- Issue: LISS-0066
- Reason it is unblocked: its only dependency, LISS-0065, reflects the
  Backlog-thread's own recorded decision authorizing this exact scope.
- Reopening request needed: no.

## Minor Fix Path

Not applicable to LISS-0066/LISS-0067 (new archival moves). LISS-0068 is
Minor-Fix-Path-shaped in size/risk (planning size S, narrow, one attempt
expected) but is executed as an ordinary issue within this work plan
rather than the formal Minor Fix Path, since it is not a correction to
previously accepted work — it is new, authorized housekeeping.

## Preflight Validation

Recorded by the Implementation group (Implementer persona), branch
`wp-0024-execution`, after all three issues landed
(commits `2d715ed`, `ab6ac19`, `5a351c9`, `b462714`, `873321d`, `16a9862`).
Result: **pass**. All six required checks run for real below.

1. `python3 scripts/check-contract-consistency.py` — run after all three
   issues landed:

   ```text
   contract consistency: all checks passed
   ```

2. `grep -rn "docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md" docs/architecture/ docs/collaboration/*.md docs/templates/`:

   ```text
   docs/collaboration/restoration-ledger.md:90:| 2026-08-20 | `docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md` | b4627146ae85753c72fb76124cd7bd565cbd9d44 | N/A | `docs/archive/work-plans/WP-0004-multi-agent-tool-loop-portability.md` | archived | ... |
   ```

   and the WP-0006 equivalent:

   ```text
   docs/collaboration/restoration-ledger.md:95:| 2026-08-20 | `docs/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md` | b4627146ae85753c72fb76124cd7bd565cbd9d44 | N/A | `docs/archive/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md` | archived | ... |
   ```

   The only hits in both cases are the restoration ledger's own
   `source_path` column (expected — that column intentionally records the
   pre-move path as history). No hit in `docs/architecture/adr/0017-*.md`,
   `docs/architecture/adr/0018-*.md`, or any other file — both ADR
   reference updates landed and no other current Canonical document
   references either old path.

3. `git log --follow` on a representative sample spanning all three
   archival categories (work plan, issue, design agreement, review record,
   trace), across both LISS-0066 and LISS-0067's own destination sets:

   - `docs/archive/work-plans/WP-0003-coordinator-message-correction.md`,
     `docs/archive/collaboration/agreements/2026-08-19-contract-reviewer-v230.md`,
     `docs/archive/collaboration/traces/2026-08-18-liss-0028-coordinator-message-correction.md`
     (LISS-0066 sample) — each `git log --follow --oneline` shows the full
     pre-move commit history plus the LISS-0066 move commit (`2d715ed`).
   - `docs/archive/work-plans/WP-0008-coordinator-role-inoculation-rule.md`,
     `docs/archive/issues/LISS-0032-quality-gate-hooks-and-coverage-policy.md`,
     `docs/archive/collaboration/agreements/2026-08-18-coordinator-role-inoculation-rule.md`,
     `docs/archive/collaboration/reviews/2026-08-18-wp-0004-multi-agent-tool-loop-portability-review.md`,
     `docs/archive/collaboration/traces/2026-08-18-liss-0030-mirror-portable-loop-wording.md`
     (LISS-0067 sample, plus one from LISS-0066) — each shows preserved
     pre-move history plus the correct move commit (`2d715ed` or
     `b462714`).

   All 8 sampled paths preserved history with no gap; not run exhaustively
   across all 32 moved files, but the sample spans every document type
   this batch moved.

4. `docs/collaboration/restoration-ledger.md` row count:

   ```text
   $ grep -c "^| 2026-08" docs/collaboration/restoration-ledger.md
   55
   ```

   Pre-existing (batch 1) rows: 23 (5 for WP-0001's set, 18 for WP-0002's
   set). This work plan added 32: 21 from LISS-0066, and 11 (not 12) from
   LISS-0067 — the LISS-0029 trace verification found no separate trace
   file for LISS-0029 (`ls docs/collaboration/traces/ | grep -i liss-0029`
   returned zero hits, and LISS-0029's own Acceptance Notes state
   explicitly "no trace required for this issue"; only
   `2026-08-18-liss-0030-mirror-portable-loop-wording.md` exists for that
   branch pair). 23 + 21 + 11 = 55, matching the actual count exactly.

5. Re-confirmation `DA-2026-08-18-03` and `DA-2026-08-18-05` are unchanged
   and un-moved:

   ```text
   $ test -f docs/collaboration/agreements/2026-08-18-multi-agent-tool-loop-portability.md && echo present
   present
   $ test -f docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md && echo present
   present
   $ git log --oneline -- docs/collaboration/agreements/2026-08-18-multi-agent-tool-loop-portability.md docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md
   57af72e process: design phase for WP-0006 (quality-gate hooks + perspectives doc)
   d9c6e6b process: design phase for WP-0004 (multi-agent tool loop portability)
   ```

   Both files remain at their original paths with no commit touching them
   since their original creation — confirmed unchanged and un-moved.

6. `git diff` / `git show --stat` on LISS-0068's own landing commit
   (`16a9862`):

   ```text
   docs/backlog/item-0005-template-propagation-script-for-two-group-loop.md      | 2 +-
   docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md      | 2 +-
   docs/backlog/item-0007-multi-agent-tool-loop-portability.md                   | 2 +-
   docs/backlog/item-0008-coordinator-message-hallucination-correction.md        | 5 +-
   docs/backlog/item-0009-document-consistency-drift-on-completion.md            | 2 +-
   docs/issues/LISS-0068-batch-2-housekeeping-fixes.md                           | 56 +++++++++
   docs/work-plans/WP-0021-archive-copy-exclusion-gap.md                         | 4 +-
   docs/work-plans/WP-0024-retroactive-adr-0020-archival-batch-2.md              | 2 +-
   8 files changed, 64 insertions(+), 11 deletions(-)
   ```

   The five backlog items plus `WP-0021-...md` (six content-scope files,
   exactly as this issue's own Acceptance Notes name) are the only
   *housekeeping-content* changes. The other two files are LISS-0068's own
   `Status`/Work-Notes update and this work plan's own Issue Graph status
   sync — the same bookkeeping-only pattern every issue in this work plan
   required at its own close (LISS-0066 and LISS-0067 both also touched
   their own issue file and this work plan's Issue Graph in their landing
   commits), not an expansion of LISS-0068's own authorized content scope.
   No backlog item's `Links` field beyond the five named, and no field in
   WP-0021's Work-Plan-Close section beyond `Date`, was touched.

**Result: pass.** Permits submission to the independent Reviewer; this is
not itself an approval and does not set `wont_do` or `closed` on anything.

## Review Summary Packet

Filled in by the Implementation group once Preflight passes.

- **Scope**: archived 7 work plans (WP-0003 through WP-0009, excluding
  WP-0004/WP-0006 as candidates for their own design agreements) and
  their combined owned issue/trace/review/agreement files under ADR 0020;
  updated 2 ADR reference paths; fixed 5 stale backlog `Links` fields and
  1 empty work-plan close date. No application code, specification, or
  ADR *content* (beyond the two path pointers) changed.
- **Current canonical documents**: none newly established; ADR 0017 and
  ADR 0018 are amended in-place (path updates only), not superseded.
- **Changed files**: 32 `git mv` moves (21 from LISS-0066, 11 from
  LISS-0067 — the LISS-0029 trace verification found no separate trace
  file, so the actual count is 11, not 12), `docs/collaboration/restoration-ledger.md`
  (32 new rows, plus two follow-up commits correcting `PENDING`
  placeholders to real move-commit hashes), ADR 0017 and ADR 0018 (one
  path edit each), 6 content files for LISS-0068 (5 backlog items +
  `WP-0021-...md`).
- **Findings**: none opened or resolved by this work plan.
- **Disposition**: Preflight passed (see Preflight Validation above, all
  six checks run for real with pasted output). Ready for the
  work-plan-level Reviewer's separate-context pass. Not itself an
  approval — the Reviewer's own `Specification conformance`, `Phase
  correctness`, `Boundary conformance`, and `Evidence sufficiency`
  judgments are still outstanding.
- **Remaining blockers**: none found. One process note for the Reviewer's
  own attention, not a blocker: during LISS-0067's execution, an
  unrelated one-line WP-0024 Issue-Graph fix for LISS-0066 was briefly
  committed with LISS-0067's already-`git mv`-staged renames accidentally
  swept in (`git add <single-file-path>` still picks up everything already
  in the index). Caught immediately, before any push, and corrected with a
  non-destructive `git reset --soft` followed by `git reset <path>` to
  re-split the two changes into their correct separate commits — no force
  push, no history rewrite of shared state, no data loss. Recorded
  transparently in LISS-0067's own Work Notes and Self-Review rather than
  silently smoothed over, per the Prime Directive's evidence requirement.
- **Verification result**: pass — see this file's own Preflight
  Validation section above, all six required checks run with real,
  pasted command output. Commit hashes: `2d715ed` (LISS-0066 moves +
  ledger, `source_commit: PENDING`), `ab6ac19` (LISS-0066 ledger hash
  correction), `5a351c9` (WP-0024 Issue Graph sync for LISS-0066),
  `b462714` (LISS-0067 moves + ADR reference updates + ledger, `source_commit: PENDING`
  + WP-0024 Issue Graph sync for LISS-0067 in the same commit),
  `873321d` (LISS-0067 ledger hash correction), `16a9862` (LISS-0068
  fixes + WP-0024 Issue Graph sync for LISS-0068).
- **Next approval required**: boundary-conformance (did the move
  correctly exclude the two blocked design agreements and stay within the
  authorized scope) and evidence-sufficiency (is every move backed by a
  real ledger row and preserved git history).

## Work-Plan Review

Reviewer's approval record: <link, filled in after the Reviewer pass>

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves — not performed
by the Design & Review group itself.

- Date:
- Result read:
- Next direction:
- New design agreement (if any):

## Risks

- A reference-update miss (an inbound path this work plan's own sweep did
  not catch) could leave a current Canonical document pointing at a dead
  path. Mitigated by Preflight's explicit `grep` re-checks and by
  `check-contract-consistency.py`'s own dangling-reference check, which
  is exercised against a second real batch of archive content for the
  first time.
- The LISS-0029 trace-file ambiguity (LISS-0067's own flagged
  verification step) could result in either 11 or 12 files moved for that
  issue — not a defect either way, as long as the Implementer records
  which was actually found rather than guessing.
- LISS-0068's own backlog-`Links`-field fixes must point at whichever
  path (live or archived) is actually correct at the moment that issue
  executes, given it is sequenced after the archival issues in this same
  work plan — mitigated by the Recommended Order placing it last and by
  its own Acceptance Notes naming this explicitly.

## Verification Plan

- `python3 scripts/check-contract-consistency.py` after all three issues
  land.
- Targeted `grep` sweep confirming both mandatory reference updates
  landed and no other current Canonical document was missed.
- `git log --follow` confirmation of preserved history.
- Restoration-ledger row count and content check.
- Confirmation that `DA-2026-08-18-03` and `DA-2026-08-18-05` remain
  untouched.
- Independent work-plan-level Reviewer approval, in a separate context.
