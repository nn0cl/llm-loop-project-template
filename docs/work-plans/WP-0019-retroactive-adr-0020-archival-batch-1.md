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

To be recorded here by the Implementation group once both issues are
self-reviewed and complete, before requesting the work-plan-level Reviewer
pass. Required checks, at minimum:

1. `python3 scripts/check-contract-consistency.py` — full output, run after
   both issues land, showing zero new failures attributable to this work
   plan's changes.
2. `grep -rn "docs/work-plans/WP-0002-two-group-send-message-loop.md"
   docs/architecture/ docs/collaboration/*.md docs/templates/` — confirms
   the ADR 0016 reference update landed and no other current Canonical
   document was missed.
3. `grep -rn "docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md"
   docs/collaboration/design-review-perspectives.md` — confirms both
   citations now point at the archive path.
4. `git log --follow -- <each of the 23 destination paths>` (or a
   representative sample naming which were spot-checked and which were
   checked exhaustively) — confirms `git mv` history preservation, not
   delete+recreate.
5. `docs/collaboration/restoration-ledger.md` contains exactly 23 new rows,
   each with a real `source_commit` hash.
6. Re-confirmation that `docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md`
   and `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
   are unchanged and un-moved (`git status`/`git diff` show no touch to
   either path).

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
- **Disposition**: <filled in at Preflight>
- **Remaining blockers**: none expected; state any found.
- **Verification result**: <pointer to this file's own Preflight
  Validation section, populated above>.
- **Next approval required**: boundary-conformance (did the move stay
  inside ADR 0020's own rules, correctly excluding the two blocked design
  agreements and item-0004) and evidence-sufficiency (is every move backed
  by a real ledger row and preserved git history) — the two approval types
  most directly at stake for a pure archival move; specification-conformance
  and phase-correctness are secondary since no specification or AT-TDD
  phase content is touched.

## Work-Plan Review

Reviewer's approval record: <link, filled in after the Reviewer pass>

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves — not performed by
the Design & Review group itself. This section is filled in by the Director
at close.

- Date:
- Result read:
- Next direction:
- New design agreement (if any):

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
