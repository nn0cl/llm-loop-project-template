# Design Agreement: WP-0019's missing AI work trace

Store the completed record at
`docs/collaboration/agreements/2026-08-20-wp-0019-missing-trace.md`.

See `docs/collaboration/design-agreement.md` for the rules this record
implements.

## Identity

- Agreement ID: DA-2026-08-20-05
- Date: 2026-08-20
- Director: per ADR 0016 Rule 2, backlog-item-level agreement — see
  "Agreement" below.
- Planner / Specifier personas (model or tool used): Design & Review
  group, standing session (Claude Code, Planner/Specifier persona).
- Supersedes agreement (if any): none.

## Direction

`docs/backlog/item-0019-wp-0019-missing-trace.md`
(`Status: promoted`, "Promoted, in the Backlog-layer thread, immediately
at capture"): add the missing AI work trace for WP-0019's two
agent-operating-contract-file edits
(`docs/collaboration/design-review-perspectives.md`,
`docs/collaboration/restoration-ledger.md`), which PR #21's CI
("Check agent operating contract change traceability") correctly flags as
missing. Per ADR 0016 Rule 2, this item was never a check-in item; Design
& Review proceeds fully autonomously. This is the second, independent gap
blocking PR #21's merge, after item-0018's fix.

## Scope

- In scope: one new trace file documenting the two already-completed
  contract-file edits, per `docs/templates/ai-work-trace.md`.
- Explicitly out of scope: any edit to the two contract files themselves,
  or to any of WP-0019's own 23 archived files; any change to
  `docs/collaboration/prompt-instruction-change-control.md` itself
  (including the open question of whether `restoration-ledger.md` should
  be reclassified as a non-contract record — named, not resolved, per
  LISS-0061's own text).

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Write the trace, citing real commits/issues/review records for WP-0019's two contract-file edits | Implementer | Fast Path | Trace accurately states which contract files changed, why, and what behavior changes (none) | Direct factual check against the cited commits/files |
| 2 | Confirm the CI check's own condition is now satisfied locally | Implementer | Fast Path | `git diff --name-only <base> <head>` includes the new trace path | Reproduction of the CI step's own invocation |
| 3 | Preflight Validation over the whole work plan | Implementer | Preflight | Both checks above recorded with real output | WP-0022's own Preflight Validation section |
| 4 | Work-plan-level Reviewer pass | Reviewer | Review | Approval record addressing evidence-sufficiency explicitly | `docs/collaboration/reviews/2026-08-20-wp-0022-....md` |

Sequencing and dependencies: strictly 1 -> 2 -> 3 -> 4.

## Specifications

No `docs/specs/` file covers this work plan — a retroactive evidentiary
addition, not application or process behavior with its own acceptance
spec.

## Boundaries

- No edit to `docs/collaboration/design-review-perspectives.md`,
  `docs/collaboration/restoration-ledger.md`, or any file WP-0019 itself
  moved/archived.
- No edit to `docs/collaboration/prompt-instruction-change-control.md`.
- No file changed other than the one new trace file and this work plan's
  own tracking files.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Should `docs/collaboration/restoration-ledger.md` really count as an "agent operating contract file," given it is a data ledger rather than an instruction/policy document? | Under `prompt-instruction-change-control.md`'s own rule as currently, literally written ("`docs/collaboration/*.md` (except the record directories below)", and `restoration-ledger.md` is not one of the three excepted subdirectories), it is a covered contract file — this work plan treats it as one rather than reinterpreting the rule. Whether the rule's own text should change is a separate, later Architecture Path question, not resolved by this narrow fix | Design & Review group (Planner), recorded in LISS-0061's own text |
| Does the ADR 0016 path edit (WP-0002's Status-section pointer) also need a trace? | No — `docs/architecture/adr/0016-...md` is not on `prompt-instruction-change-control.md`'s covered-file list at all (that list does not include `docs/architecture/adr/*.md`); only the two `docs/collaboration/*.md`-pattern edits are in scope for this gap | Design & Review group (Planner), verified by direct reading of the contract-file list |

## Deferred Questions

None — this is a fully bounded, single-issue work plan with no open
question left for later.

## Verification

- `python3 scripts/check-contract-consistency.py` — no regression.
- `git diff --name-only <base> <head>` reproduction confirming the CI
  check's own `trace_added` condition is satisfied.
- Direct factual accuracy check of the new trace's content against the
  real commits/issues/review records it cites.

## Falsification Criteria

This design was wrong if, after execution:

- The new trace does not actually satisfy the CI check's own condition
  (i.e., `git diff --name-only` between the actual PR base/head still
  does not show a `docs/collaboration/traces/*.md` path).
- The trace's content misstates which files changed, why, or cites a
  commit/issue that does not actually correspond to the real edit.
- Any file other than the new trace and this work plan's own tracking
  files is changed.

## Agreement

- [x] **Director**: this plan and these specifications describe what I
      want built, and the stated boundaries are the right ones. — Per
      ADR 0016 Rule 2's backlog-item-level agreement:
      `docs/backlog/item-0019-wp-0019-missing-trace.md`'s own Promotion
      notes state "Promoted, in the Backlog-layer thread, immediately at
      capture... Design & Review proceeds autonomously from here," with
      the root cause already identified precisely and reproducible via
      PR #21's own CI failure.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Nothing in them requires guessing at a
      rule that was never stated. — Design & Review group (Planner),
      2026-08-20. The exact trace content requirements, the exact
      verification method, and the one genuinely open question this
      scope raised (the `restoration-ledger.md` classification) are all
      settled above, not left for the Implementer to guess.

If the AI cannot make its statement, the design phase is not finished,
regardless of the Director's readiness to proceed.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
