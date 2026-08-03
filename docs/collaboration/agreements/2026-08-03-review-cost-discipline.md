# Design Agreement: Review Cost Discipline

## Identity

- Agreement ID: DA-2026-08-03-02
- Date: 2026-08-03
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5, Claude
  Code, chat dialogue.
- Supersedes agreement (if any): none.

## Direction

Fix the cost problem diagnosed in dialogue: self-authored process records
(design agreements, traces, Preflight records) were written at full weight
regardless of change size, and multi-round independent review resumed the
same Reviewer agent across rounds rather than a fresh, scoped invocation each
time — both confirmed with concrete numbers and file evidence from this
repository's own session history (see ADR 0015's Context section).

## Scope

- In scope: `docs/templates/self-review.md` (new, short + full forms);
  `docs/architecture/adr/0015-review-cost-discipline.md`; propagation into
  the nine contract files, `llm-cost-reduction.md`, `README.md`, the ADR
  count bump (14→15), and CI's file list.
- Explicitly out of scope: no change to the three approval constraints
  themselves; no change to ADR 0006's substantive separate-context Reviewer
  requirement.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Write `docs/templates/self-review.md` (short + full forms) | Implementer | Refactor | Template exists, short form bounded, full form points to `review-record.md`'s shape | Manual read |
| 2 | Write ADR 0015 | Implementer | Refactor | ADR states the diagnosis and the decision | Manual read |
| 3 | Propagate into all nine contract files | Implementer | Refactor | All nine gain the self-review pointer and finding-response guidance | `grep` across all nine |
| 4 | Update `llm-cost-reduction.md` Warning Signs | Implementer | Refactor | New patterns named | Manual read |
| 5 | Bump ADR count 14→15 everywhere stated | Implementer | Refactor | No stale "fourteen ADRs" text remains | `grep` sweep across entry documents |
| 6 | Add `self-review.md` to CI `required_files` | Implementer | Refactor | CI's file list includes it | Manual read of `ci.yml` |

Sequencing and dependencies: none beyond the obvious — the template and ADR
(1, 2) precede propagation (3-6).

## Specifications

No application specification applies — process/governance change, consistent
with how prior process-ADR changes in this repository have been handled.

## Boundaries

- Must not change what the three approval constraints require.
- Must not change ADR 0006's contract-file review requirement.
- Any exception to a contract requirement — including skipping the
  separate-context Reviewer this agreement's own execution needed — requires
  authority named somewhere in the contract. **At the time this agreement was
  first executed, no such authority was named, and the exception recorded
  below was taken anyway. That was a boundary violation, found by a
  retroactive fresh-context review
  (`docs/collaboration/reviews/2026-08-03-review-cost-discipline-review.md`,
  Finding 1) and corrected under a follow-up agreement,
  `docs/collaboration/agreements/2026-08-03-review-cost-discipline-correction.md`
  (DA-2026-08-03-03).** This section is edited in place, after the fact, to
  state that plainly rather than leave the original omission standing.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Can the Director instruct that independent review be skipped for this one change? | **No, and the original answer recorded here ("yes, this instance only") was wrong.** No provision in the contract grants the Director that authority over ADR 0006's separate-context requirement; the design agreement is not itself a source of that authority. See the corrected Boundaries section above. | Reviewer's rejection record, Finding 1; corrected under DA-2026-08-03-03 |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Whether a bounded, contract-defined Director-override provision should ever exist for ADR 0006 | Settled under DA-2026-08-03-03: no such provision is adopted; the contract states explicitly that none exists. This row is kept, not deleted, so the original deferral and its resolution both remain visible. |

## Verification

- `python3 scripts/check-contract-consistency.py --repo .`.
- `required_files` existence check.
- ADR loop range `0001`-`0015`.
- `bash -n`; conflict-marker sweep.
- Copy-script smoke test confirming `self-review.md` distributes.

## Falsification Criteria

This design would be wrong if: the propagation left any of the nine contract
files stating a different self-review default than the others; the ADR count
bump missed an entry-document location; or — the criterion this record failed
to state the first time, and the gap a retroactive review had to name instead
of this agreement naming it itself — if the change shipped without the
separate-context Reviewer approval ADR 0006 requires unconditionally.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation.

Both statements held for the plan's content. They did not extend to
authorizing the Reviewer-approval skip recorded in the original Boundaries
text — no field in this template grants that authority, a gap this rewrite
states directly rather than papering over.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
| 2026-08-03 | Whether this agreement's own execution had authority to skip ADR 0006's separate-context Reviewer requirement | No such authority existed. Corrected under DA-2026-08-03-03, which also brought this record's missing fields (Plan, Specifications, Boundaries, Settled Ambiguities, Deferred Questions, Verification, Falsification Criteria) up to `design-agreement.md`'s template. |
