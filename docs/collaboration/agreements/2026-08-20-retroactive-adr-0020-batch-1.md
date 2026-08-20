# Design Agreement: Retroactive ADR 0020 archival — batch 1 (WP-0001, WP-0002)

Store the completed record at
`docs/collaboration/agreements/2026-08-20-retroactive-adr-0020-batch-1.md`.

See `docs/collaboration/design-agreement.md` for the rules this record
implements.

## Identity

- Agreement ID: DA-2026-08-20-02
- Date: 2026-08-20
- Director: per ADR 0016 Rule 2, backlog-item-level agreement — see
  "Agreement" below.
- Planner / Specifier personas (model or tool used): Design & Review group,
  standing session (Claude Code, Planner/Specifier persona).
- Supersedes agreement (if any): none.

## Direction

Stated across two layers, per ADR 0016 Rule 2's backlog-item-level
agreement:

- `docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`
  (`Status: promoted`): apply ADR 0020's rules to this repository's own
  existing history, batched, with an explicit Backlog-thread check-in
  before any large first sweep (its own stated exception to ADR 0016 Rule
  2's usual full autonomy).
- The Backlog-thread's own response to `docs/issues/LISS-0055-...md`
  (recorded in that issue's own Work Notes, 2026-08-20): authorizes the
  proposed first batch — WP-0001 and WP-0002 together, oldest-first — with
  later work-plan-scoped batches to follow as separate, later executions,
  each re-verified fresh. "Do not go further than this batch" — report
  back once done and reviewed, before proposing the next batch.

## Scope

- In scope: exactly the two work plans and their owned records named in
  `docs/work-plans/WP-0019-retroactive-adr-0020-archival-batch-1.md`'s own
  Scope section (23 files total across LISS-0056 and LISS-0057), the 23
  restoration-ledger rows, and the two mandatory Rule-3 reference updates
  that work plan names.
- Explicitly out of scope: `DA-2026-08-02-04`, `DA-2026-08-18-01`,
  `docs/backlog/item-0004-...md`, any ADR, WP-0003 through WP-0018 and
  their records, and any change to ADR 0020's own rules — see WP-0019's own
  Scope section for the full list and grounds.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Archive WP-0001 and its 4 owned records (5 files) | Implementer | docs-only | LISS-0056's Acceptance Notes fully satisfied; ledger has 5 new rows | `git mv` + `git log --follow`; ledger row count |
| 2 | Archive WP-0002 and its 17 owned records (18 files); update the 2 mandatory Canonical-document references | Implementer | docs-only | LISS-0057's Acceptance Notes fully satisfied; ledger has 18 more rows (23 total) | `git mv` + `git log --follow`; ledger row count; targeted `grep` for both reference updates |
| 3 | Preflight Validation over the whole work plan | Implementer | Preflight | `python3 scripts/check-contract-consistency.py` shows zero new failures | Full command output pasted in WP-0019's own Preflight Validation section |
| 4 | Work-plan-level Reviewer pass | Reviewer | Review | Approval record addressing boundary-conformance and evidence-sufficiency explicitly (per WP-0019's own Review Summary Packet) | `docs/collaboration/reviews/2026-08-20-wp-0019-....md` |

Sequencing and dependencies:

- Task 1 before Task 2 (independent file sets, but sequencing keeps each
  commit small and independently reviewable, per WP-0019's Recommended
  Order).
- Task 3 only after both Task 1 and Task 2 land.
- Task 4 only after Task 3 records a `pass`.

## Specifications

No `docs/specs/` file covers this work plan — pure archival/document-move
process work under an already-Accepted ADR, not application behavior.

## Boundaries

- No content rewriting of any moved file (Rule 3: verbatim move only).
- No redirect stub at any old path (Rule 3).
- No touch to `DA-2026-08-02-04`, `DA-2026-08-18-01`, any ADR file, or
  `docs/backlog/item-0004-...md`.
- No touch to WP-0003 through WP-0018 or their own owned records.
- No change to ADR 0020's own Decision text.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Is WP-0002 genuinely Rule-2-eligible, or does its issue-status gap still need a judgment call? | Genuinely eligible — the nine issues' `Status` fields were corrected to `done` (commit `73ab2ce`, PR #20), independently re-verified against the actual files after merging `main` into `process/promote-item-0016` | Design & Review group (Planner), recorded in `docs/spike/case-0002-.../case.md`'s post-close Addendum and `docs/issues/LISS-0055-...md`'s Work Notes |
| Are `DA-2026-08-02-04` and `DA-2026-08-18-01` archival-eligible once their own work plans archive? | No — each is cited normatively, by ID, as the Accepted-status grounding of a current, unsuperseded ADR (0012 and 0016 respectively); ADR 0020 Rule 2's general opening clause blocks archival regardless of the design agreement's own terminal state | Design & Review group (Planner), same Addendum |
| Is `docs/backlog/item-0004-...md`'s archival in scope for this batch? | No — deliberately deferred; it is Rule-2-eligible but has a markedly larger reference graph than this batch's other 23 files, and absorbing its full individual-reference triage here would grow this batch past a reviewable single unit | Design & Review group (Planner), recorded in LISS-0057's "Explicit exclusion" section |
| Which inbound references in current Canonical documents require updating under Rule 3? | Exactly two: ADR 0016's Status-section path to WP-0002's file, and `design-review-perspectives.md`'s two citations of WP-0002's own review record; all other WP-0002-related mentions found in canonical documents are ID-only, not path references, and need no change | Design & Review group (Planner), repository-wide `grep` sweep recorded in LISS-0057 |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should `docs/backlog/item-0004-...md` be archived, and what disposition applies to each of its own inbound references (`DA-2026-08-18-04`, ADR 0016, LISS-0040, WP-0011, item-0005, item-0007, item-0012, LISS-0031)? | A later, separate batch that gives item-0004's own reference graph the same individual scrutiny this batch gave WP-0002's — not this work plan. |
| What is the next archival batch after WP-0001/WP-0002 (a WP-0003-through-some-cutoff range, or a different scope)? | The Design & Review group proposes it after this batch is reviewed and reported back, per item-0016's own "do not go further than this batch" instruction — not decided here. |

## Verification

- `python3 scripts/check-contract-consistency.py` — zero new failures.
- `git log --follow` on each of the 23 destination paths, confirming
  preserved pre-move history.
- Restoration-ledger row count (23 new rows) and per-row schema check.
- Targeted `grep` confirming both mandatory Rule-3 reference updates
  landed, and that `DA-2026-08-02-04`/`DA-2026-08-18-01` remain untouched.

## Falsification Criteria

This design was wrong if, after execution:

- Any of the 23 files was rewritten rather than moved verbatim (content
  diff beyond the file's own path-relative self-references, if any).
- `check-contract-consistency.py` reports a new dangling reference, mirror
  parity failure, or Entry-archive-reference failure attributable to this
  move.
- A current Canonical document is found, after the move, still pointing at
  an old (now-nonexistent) path for any of the 23 files.
- `DA-2026-08-02-04` or `DA-2026-08-18-01` was moved, edited, or deleted.
- The restoration ledger is missing a row for any moved file, or a row's
  `source_commit` does not match the actual move commit.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. — Per ADR 0016
      Rule 2's backlog-item-level agreement: stated at
      `docs/backlog/item-0016-...md` approval and confirmed by the
      Backlog-thread's own response to `docs/issues/LISS-0055-...md`
      authorizing exactly this batch (WP-0001 + WP-0002, oldest-first,
      "do not go further than this batch").
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Nothing in them requires guessing at a rule
      that was never stated. — Design & Review group (Planner), 2026-08-20.
      Every file to move, its destination, its ledger reason, and every
      required reference update is named explicitly in
      `docs/work-plans/WP-0019-...md`, `docs/issues/LISS-0056-...md`, and
      `docs/issues/LISS-0057-...md`; the two genuinely ambiguous questions
      this scope raised (design-agreement archival eligibility; item-0004's
      inclusion) are resolved above under Settled Ambiguities, not left for
      the Implementer to guess.

If the AI cannot make its statement, the design phase is not finished,
regardless of the Director's readiness to proceed.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
