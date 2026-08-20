# Work Plan: `check-contract-consistency.py` excludes `.claude/`

## Goal

- Fix `scripts/check-contract-consistency.py`'s two `os.walk` sites so
  they exclude the harness-local, untracked `.claude/` directory the same
  way they already exclude `.git/`, eliminating false-positive ambiguous-
  reference noise when the checker runs from a location with active
  sibling agent worktrees under `.claude/worktrees/`.

## Scope

- In:
  - `scripts/check-contract-consistency.py`'s `scanned_files()` and
    `check_references()` `os.walk` prune lines (both currently exclude
    only `.git`).
  - A controlled fixture-based reproduction of the false positive, before
    and after the fix.
- Out:
  - Any other check function's own logic.
  - `SCANNED_SUFFIXES`, `RECORD_DIRS`, or any other existing
    exclusion/inclusion constant.
  - Any change to what counts as a genuine, in-scope reference failure.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0058 | ready | S | S | N/A | - | - | process/promote-item-0017 |

## Recommended Order

1. LISS-0058 (the only issue) — reproduce the false positive in a fixture,
   apply the fix, re-verify.

## Current Next Issue

- Issue: LISS-0058
- Reason it is unblocked: no dependency; scope is fully settled by the
  design agreement, and the backlog item itself states the fix is
  "reproducible, narrow, root cause identified with the exact line."
- Reopening request needed: no.

## Minor Fix Path

Not used formally (this is a new issue against a confirmed bug, not a
correction to previously accepted work), but the change itself is
Minor-Fix-Path-shaped in size and risk: planning size `S`, a single
narrowly-scoped file, one attempt expected, no specification, ADR, port,
data model, or architecture boundary changed.

## Preflight Validation

To be recorded here by the Implementation group once LISS-0058 is
self-reviewed and complete, before requesting the work-plan-level Reviewer
pass. Required checks, at minimum:

1. The fixture-based before/after reproduction LISS-0058's own Acceptance
   Notes describe — full pasted output, both runs.
2. `python3 scripts/check-contract-consistency.py` (default `--repo .`,
   against the real repository) — full output, confirming no regression.
3. `git diff scripts/check-contract-consistency.py` — confirms the change
   is confined to the two named prune lines (plus, if needed, a shared
   constant if the Implementer chooses to factor the exclusion list out
   rather than duplicate the tuple — either is acceptable, state which was
   chosen).

## Review Summary Packet

Filled in by the Implementation group once Preflight passes.

- **Scope**: fixed two `os.walk` exclusion sites in
  `scripts/check-contract-consistency.py` to also prune `.claude`,
  eliminating false-positive ambiguous-reference noise from nested sibling
  worktrees under `.claude/worktrees/`.
- **Current canonical documents**: none — `scripts/check-contract-consistency.py`
  is tooling, not an ADR-0006 contract file (confirmed by the backlog
  item's own "Known constraints" note), though this work plan treats the
  change with the same review rigor as this script's own six-round
  2026-08-02 review history, per that same note.
- **Changed files**: `scripts/check-contract-consistency.py` only.
- **Findings**: none opened or resolved by this work plan.
- **Disposition**: <filled in at Preflight>
- **Remaining blockers**: none expected; state any found.
- **Verification result**: <pointer to this file's own Preflight
  Validation section, populated above>.
- **Next approval required**: evidence-sufficiency (is the false positive
  genuinely reproduced and genuinely fixed, with real pasted output) —
  the one approval type most directly at stake for a bug-fix this narrow;
  specification-conformance, phase-correctness, and boundary-conformance
  are secondary since no specification, phase, or architecture boundary is
  touched.

## Work-Plan Review

Reviewer's approval record: <link, filled in after the Reviewer pass>

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves — not performed by
the Design & Review group itself.

- Date:
- Result read:
- Next direction:
- New design agreement (if any):

## Risks

- A fixture reproduction that does not faithfully mirror the real bug
  (e.g., too small to trigger the ambiguous-basename check, or missing the
  nested full-checkout structure) could produce a false "no noise before
  the fix either" result. Mitigated by requiring the fixture to copy this
  repository's own real tracked content into both the top-level and the
  nested `.claude/worktrees/fake-sibling/` path, not synthetic minimal
  files.
- Excluding the whole `.claude` top-level directory (rather than only
  `.claude/worktrees`) is a broader exclusion than the backlog item's own
  literal title names. Mitigated by direct `git ls-tree` confirmation nothing
  under `.claude/` is tracked, and the item's own text explicitly leaves
  "how broad to make the exclusion" as "Design & Review's call."

## Verification Plan

- Fixture-based before/after reproduction (pasted output).
- `python3 scripts/check-contract-consistency.py` against the real
  repository, before and after (no regression).
- `git diff` confirming a narrowly-scoped change.
- Independent work-plan-level Reviewer approval, in a separate context.
