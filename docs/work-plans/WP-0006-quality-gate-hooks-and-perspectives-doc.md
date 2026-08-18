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
| LISS-0032 | ready | M | M | AIP-0032-001 | - | LISS-0033 | process/quality-gate-hooks-and-coverage-policy |
| LISS-0033 | ready | M | M | AIP-0033-001 | LISS-0032 | - | process/design-review-perspectives-doc |

## Plan-Owned Bug Records

None.

## AI Planning Records

See each issue's own AI Planning Records section.

## Recommended Order

1. LISS-0032 (ADR 0018, hooks/coverage policy) — LISS-0033's perspectives
   document and its wiring cite the ADR by number.
2. LISS-0033 (perspectives document).

## Current Next Issue

- Issue: LISS-0032
- Reason it is unblocked: no dependencies; `DA-2026-08-18-05` covers it
  fully, including the resolved numeric-floor and retroactivity questions.
- Reopening request needed: no.

## Minor Fix Path

Not applicable to initial execution (both issues are Architecture Path,
planning size `M`).

## Preflight Validation

- Result: _pending Implementation-group execution_
- Checks and command output: _to be recorded by the Implementer_
- Scope result: _to be recorded_
- Next action: _to be recorded_

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
