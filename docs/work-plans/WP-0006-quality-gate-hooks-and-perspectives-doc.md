# Work Plan: Mandatory Quality-Gate Hooks, Coverage Policy, and Perspectives Document

## Goal

- Add a mandatory pre-commit quality-gate hook requirement and a
  branch/route coverage anti-gaming policy to this template's contract, and
  create a living design/review-perspectives document, per
  `docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md`
  and `docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md`
  (`DA-2026-08-18-05`).

## Scope

- In: a new ADR (0018, pending numbering confirmation); updates to
  `tooling.md`, `testing-strategy.md`, `definition-of-done.md`,
  `scripts/lib/emit-tooling-setup-prompt.sh`; a new
  `docs/collaboration/design-review-perspectives.md` seeded from real
  review history; wiring it into required reading; traces for
  contract-file changes; self-review; Preflight; separate-context Reviewer
  pass.
- Out: installing any hook/coverage tool in this template repository
  itself; mandating a universal numeric coverage floor; rewriting
  `findings-reuse.md`'s lifecycle.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0032 | review | M | M | AIP-0032-001 | - | LISS-0033 | process/quality-gate-hooks-and-coverage-policy |
| LISS-0033 | review | M | M | AIP-0033-001 | LISS-0032 | - | process/quality-gate-hooks-and-coverage-policy (executed on LISS-0032's branch; see LISS-0033 Work Notes) |

## Plan-Owned Bug Records

None.

## AI Planning Records

See each issue's own AI Planning Records section.

## Recommended Order

1. LISS-0032 (ADR 0018, hooks/coverage policy) — LISS-0033's perspectives
   document and its wiring cite the ADR by number.
2. LISS-0033 (perspectives document).

## Current Next Issue

- Issue: none — both LISS-0032 and LISS-0033 are executed and self-reviewed
  (`Status: review`). Preflight Validation above recorded `pass`.
- Reason: nothing left for the Implementer within this work plan's scope;
  the whole work plan is ready for the Design & Review group's
  separate-context Reviewer pass (Task 10).
- Reopening request needed: no. One item is flagged for the Reviewer's and
  Design & Review group's attention without requiring a reopening — the
  ADR-0017/0018 numbering-gap reconciliation named in Preflight Validation's
  Scope result, above.

## Minor Fix Path

Not applicable to initial execution (both issues are Architecture Path,
planning size `M`).

## Preflight Validation

- Result: **pass**
- Checks and command output:

  ```text
  $ python3 scripts/check-contract-consistency.py --repo .
  contract consistency: all checks passed
  ```

  ```text
  $ bash scripts/init-loop-settings.sh --prompt-only | grep -n "ADR 0018"
  51:**Mandatory: wire an actual, commit-blocking pre-commit hook (ADR 0018).**
  78:**Mandatory: state the branch/route coverage approach (ADR 0018).** In the
  82:not a subset chosen to hit a number. Consistent with ADR 0018's no-
  120:**CI is additive, not a substitute (ADR 0018).** These CI jobs are required
  ```

  Trace file existence, one per contract file touched by this work plan:
  ```text
  $ ls docs/collaboration/traces/2026-08-18-liss-0032* docs/collaboration/traces/2026-08-18-liss-0033*
  docs/collaboration/traces/2026-08-18-liss-0032-definition-of-done-hook-coverage.md
  docs/collaboration/traces/2026-08-18-liss-0033-perspectives-doc-and-required-reading.md
  ```
  These two trace files together name every contract file touched by this
  work plan: `docs/collaboration/definition-of-done.md` (LISS-0032's own
  trace), and `docs/collaboration/design-review-perspectives.md` plus
  `CLAUDE.md` (LISS-0033's own trace).

- Scope result: both issues' Status is `review`; both have full-form
  self-review recorded in their own Work Notes (planning size `M`); no
  open `Type: review-finding` issues affect this area; no issue in this
  plan is blocked on an open spike case. One repository-wide finding this
  Preflight surfaces for the Reviewer's attention, not fixable within this
  work plan's own scope: adding ADR 0018 (see LISS-0032's Work Notes for
  the numbering rationale) left `docs/architecture/adr/` with a temporary
  gap at `0017` on this branch — that number belongs to a separate,
  unmerged WP-0004 branch (`process/adr-0017-portable-loop`). `README.md`,
  `QUICKSTART.md`, `QUICKSTART.ja.md`, and `.github/workflows/ci.yml` were
  all updated to state the range accurately for *this* branch
  (`0001-0016, 0018`, disclosed explicitly rather than implied as
  contiguous), and `check-contract-consistency.py` passes against this
  branch as it stands — but reconciling the gap once WP-0004's `0017`
  branch also lands is explicitly out of this Implementer's authority and
  is flagged here, per the design agreement's own "Falsification Criteria"
  ("Two work plans... claim the same ADR number without either being
  flagged as a reopening-worthy conflict" — this is not that case, since
  `0017` and `0018` do not collide, but the resulting gap still needs the
  Design & Review group's attention at merge time).
- Next action: submit to the Design & Review group's separate-context
  Reviewer pass (Task 10). This Preflight result is not itself an
  approval and does not set any issue to `done`/`closed`.

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: _pending Director action_
- Result read:
- Next direction:
- New design agreement (if any):

## Risks

- ADR numbering collision with the concurrently in-flight WP-0004 (both
  claim adjacent ADR numbers); mitigated by requiring the Implementer to
  confirm the true next-free number at execution time and treat a
  collision as a reopening-worthy finding, not a silent renumbering.
- The perspectives document could end up as an empty template or invented
  examples instead of real, distilled findings; mitigated by the explicit
  acceptance criterion requiring at least 3 entries traced to real
  `docs/collaboration/reviews/*.md` records, checked independently by the
  Reviewer.
- The hook-wiring requirement, stated at the contract level with no fixed
  stack, risks being too abstract to be actionable; mitigated by requiring
  the strengthened tooling-setup prompt to name concrete per-stack examples
  (native git hooks, husky/lefthook, pre-commit, etc.), consistent with how
  the existing prompt already gives per-ecosystem tool examples elsewhere.

## Verification Plan

- `scripts/check-contract-consistency.py`.
- `scripts/init-loop-settings.sh --prompt-only` output review.
- Trace file existence check for every contract file touched.
- Separate-context Reviewer approval, including independent verification
  that the perspectives document's seeded entries trace to real review
  records.
