# Design Agreement: Retroactive ADR 0020 archival — batch 2 (WP-0003 through WP-0009)

Store the completed record at
`docs/collaboration/agreements/2026-08-20-retroactive-adr-0020-batch-2.md`.

See `docs/collaboration/design-agreement.md` for the rules this record
implements.

## Identity

- Agreement ID: DA-2026-08-20-07
- Date: 2026-08-20
- Director: per ADR 0016 Rule 2, backlog-item-level agreement — see
  "Agreement" below.
- Planner / Specifier personas (model or tool used): Design & Review
  group, standing session (Claude Code, Planner/Specifier persona).
- Supersedes agreement (if any): none.

## Direction

`docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`'s
own Promotion notes (updated 2026-08-20, commit `63a08eb`) authorized
Design & Review to propose a concrete batch-2 plan; that proposal
(`docs/issues/LISS-0065-...md`) was answered by the Backlog thread's own
recorded decision (commit `c08095d`, in that issue's Work Notes):
authorizing WP-0003 through WP-0009 as batch 2 (excluding the two
normatively-blocked design agreements), and folding in two small
housekeeping fixes into this same work plan.

## Scope

- In scope: exactly the file sets `docs/work-plans/WP-0024-...md`'s own
  Scope section names (LISS-0066, LISS-0067, LISS-0068).
- Explicitly out of scope: `DA-2026-08-18-03`, `DA-2026-08-18-05`, any
  ADR's own substantive content, WP-0010 through WP-0023 and their own
  records, any backlog item's `Links` field beyond the five named.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Archive WP-0003, WP-0005, WP-0007, WP-0008, WP-0009 and their 21 combined owned files | Implementer | docs-only | LISS-0066's Acceptance Notes fully satisfied | `git mv` + `git log --follow`; ledger row count |
| 2 | Archive WP-0004, WP-0006 and their 11-12 owned files; update ADR 0017/0018's reference paths | Implementer | docs-only | LISS-0067's Acceptance Notes fully satisfied | Same, plus targeted `grep` for both reference updates |
| 3 | Fix the 5 stale backlog `Links` fields and WP-0021's empty close date | Implementer | Fast Path | LISS-0068's Acceptance Notes fully satisfied | `git diff` confined to 6 files |
| 4 | Preflight Validation over the whole work plan | Implementer | Preflight | All checks in WP-0024's own Preflight Validation section recorded with real output | WP-0024's own section |
| 5 | Work-plan-level Reviewer pass | Reviewer | Review | Approval record addressing boundary-conformance and evidence-sufficiency explicitly | `docs/collaboration/reviews/2026-08-20-wp-0024-....md` |

Sequencing and dependencies: 1, then 2 (drift-prevention checks exercise
against cumulative archive content), then 3 (backlog-`Links` fixes must
know whether the archival already landed); 4 only after 1-3; 5 only after
4 records a `pass`.

## Specifications

No `docs/specs/` file covers this work plan — pure archival/process work.

## Boundaries

- No content rewriting of any moved file beyond the two authorized
  ADR reference-path edits.
- No redirect stub at any old path.
- No touch to `DA-2026-08-18-03`, `DA-2026-08-18-05`, any ADR's own
  substantive content, or WP-0010 through WP-0023.
- No backlog item's `Links` field touched beyond the five named in
  LISS-0068.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Are WP-0003, WP-0005, WP-0007, WP-0008, WP-0009's own design agreements archival-eligible? | Yes — independently confirmed via `grep` sweep across `docs/architecture/adr/*.md`, `docs/collaboration/*.md`, `docs/templates/*.md`: none of the five is normatively cited anywhere | Design & Review group (Planner), recorded in `LISS-0065`'s own table |
| Are WP-0004 and WP-0006's own design agreements archival-eligible? | No — each is normatively cited as its own ADR's (0017, 0018 respectively) Accepted-status grounding, same pattern as batch 1's `DA-2026-08-02-04`/`DA-2026-08-18-01` | Design & Review group (Planner), same table |
| Does LISS-0029 have its own individual trace file? | Not confirmed by this proposal's own research (only one trace found, under LISS-0030's name, for the sequential two-issue unit) — explicitly named as a verification step for the Implementer, not assumed either way | Design & Review group (Planner), recorded in `LISS-0067`'s own Acceptance Notes |
| Should WP-0019 through WP-0023 be included in this or a near-term future batch? | No — held out longer than WP-0010-0018, per the Design & Review group's own recommendation in `LISS-0065`, agreed by the Backlog thread without redirection | Backlog thread, recorded in `LISS-0065`'s own Work Notes (commit `c08095d`) |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| What is batch 3 (a further slice of WP-0010 through WP-0018)? | A later, separate proposal, after this batch lands and is reviewed — not decided here. |
| When (if ever) does WP-0019 through WP-0023 become eligible for its own archival consideration? | A future batch's own fresh re-verification, once its design agreements have had time to potentially accrue their own normative citations or not — not decided here. |

## Verification

- `python3 scripts/check-contract-consistency.py` — zero new failures.
- `git log --follow` on each destination path.
- Restoration-ledger row count and per-row schema check.
- Targeted `grep` confirming both mandatory reference updates landed, and
  that `DA-2026-08-18-03`/`DA-2026-08-18-05` remain untouched.
- `git diff` confirming LISS-0068's own six-file scope.

## Falsification Criteria

This design was wrong if, after execution:

- Any moved file was rewritten rather than moved verbatim.
- `check-contract-consistency.py` reports a new dangling reference,
  mirror parity, or Entry-archive-reference failure attributable to this
  move.
- A current Canonical document is found, after the move, still pointing
  at an old (now-nonexistent) path.
- `DA-2026-08-18-03` or `DA-2026-08-18-05` was moved, edited, or deleted.
- The restoration ledger is missing a row for any moved file, or a row's
  `source_commit` does not match the actual move commit.
- Any backlog item's `Links` field other than the five named was touched.

## Agreement

- [x] **Director**: this plan and these specifications describe what I
      want built, and the stated boundaries are the right ones. — Per
      ADR 0016 Rule 2's backlog-item-level agreement: stated at
      `docs/backlog/item-0016-...md`'s own batch-2-proposal authorization
      (commit `63a08eb`) and confirmed by the Backlog thread's own
      response to `docs/issues/LISS-0065-...md` (commit `c08095d`)
      authorizing exactly this scope, including the two folded-in
      housekeeping fixes.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Nothing in them requires guessing at a
      rule that was never stated. — Design & Review group (Planner),
      2026-08-20. Every file to move, its destination, its ledger
      reason, every required reference update, and both housekeeping
      fixes are named explicitly in `docs/work-plans/WP-0024-...md`,
      `docs/issues/LISS-0066-...md`, `LISS-0067-...md`, and
      `LISS-0068-...md`; the one genuine open verification step
      (LISS-0029's own trace) is named as a step to perform, not guessed.

If the AI cannot make its statement, the design phase is not finished,
regardless of the Director's readiness to proceed.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
