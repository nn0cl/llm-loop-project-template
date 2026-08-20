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
| LISS-0067 | ready | M | M | N/A | LISS-0065 | - | process/item-0016-batch-2-proposal |
| LISS-0068 | ready | S | S | N/A | LISS-0065 | - | process/item-0016-batch-2-proposal |

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

To be recorded here by the Implementation group once all three issues are
self-reviewed and complete, before requesting the work-plan-level
Reviewer pass. Required checks, at minimum:

1. `python3 scripts/check-contract-consistency.py` — full output, run
   after all three issues land, showing zero new failures.
2. `grep -rn "docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md"
   docs/architecture/ docs/collaboration/*.md docs/templates/` and the
   WP-0006 equivalent — confirms both ADR reference updates landed and no
   other current Canonical document was missed.
3. `git log --follow` on a representative sample of destination paths
   (or exhaustively, stating which), confirming preserved history.
4. `docs/collaboration/restoration-ledger.md` contains the expected
   number of new rows (21 from LISS-0066, plus 11 or 12 from LISS-0067,
   depending on the LISS-0029 trace finding).
5. Re-confirmation that `DA-2026-08-18-03` and `DA-2026-08-18-05` are
   unchanged and un-moved.
6. `git diff` confirms LISS-0068's own scope is confined to exactly the
   six files it names.

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
- **Changed files**: the ~32-34 `git mv` moves (per LISS-0066/LISS-0067's
  own tables), `docs/collaboration/restoration-ledger.md` (new rows), ADR
  0017 and ADR 0018 (one path edit each), 6 files for LISS-0068.
- **Findings**: none opened or resolved by this work plan.
- **Disposition**: <filled in at Preflight>
- **Remaining blockers**: none expected; state any found.
- **Verification result**: <pointer to this file's own Preflight
  Validation section, populated above>.
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
