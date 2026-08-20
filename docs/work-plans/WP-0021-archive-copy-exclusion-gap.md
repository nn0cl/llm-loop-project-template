# Work Plan: `docs/archive/` copy-exclusion gap

## Goal

- Add `docs/archive/*` to `scripts/lib/collaboration-template-paths.sh`'s
  `collaboration_template_exclude_paths` array so
  `scripts/check-contract-consistency.py`'s copy-exclusion exemption logic
  (`_copy_exclusion_patterns()`/`_is_copy_excluded_reference()`, from
  item-0011/LISS-0040) recognizes a reference to a `docs/archive/` file as
  expected-absent on a copied/adopter target, unblocking PR #21 (WP-0019's
  merge) which is currently failing CI's "Check template copy smoke test"
  with 26 dangling-reference failures.

## Scope

- In:
  - One array entry added to `scripts/lib/collaboration-template-paths.sh`.
  - Before/after reproduction of the actual CI failure, using the same
    copy mechanism `.github/workflows/ci.yml`'s "Check template copy smoke
    test" step uses.
  - Correcting `docs/backlog/item-0018-...md`'s own premise that this
    closes `LISS-0044` (already closed; a different, already-resolved
    mechanism) — recorded, not acted on by reopening that issue.
- Out:
  - Any change to `collaboration_template_paths` (the copy-inclusion
    list) — `docs/archive` must not start being copied.
  - Any change to `scripts/check-contract-consistency.py`'s own Python
    logic — the fix is entirely data-driven from the shell array that
    script already parses.
  - Reopening or editing `docs/issues/LISS-0044-...md`.
  - Any other check function or exclusion mechanism.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0059 | ready | S | S | N/A | - | - | process/promote-item-0018 |

## Recommended Order

1. LISS-0059 (the only issue) — reproduce the real CI failure locally
   first, apply the one-line fix, re-verify.

## Current Next Issue

- Issue: LISS-0059
- Reason it is unblocked: no dependency; scope is fully settled by the
  design agreement; root cause already confirmed against the actual CI
  log and the actual current source of both scripts involved.
- Reopening request needed: no.

## Minor Fix Path

Not used formally (this is a new issue against a confirmed, CI-reproduced
bug, not a correction to previously accepted work), but the change itself
is Minor-Fix-Path-shaped in size and risk: planning size `S`, a single
one-line array addition, one attempt expected, no specification, ADR,
port, data model, or architecture boundary changed.

## Preflight Validation

To be recorded here by the Implementation group once LISS-0059 is
self-reviewed and complete, before requesting the work-plan-level Reviewer
pass. Required checks, at minimum:

1. The before/after copy-smoke-test reproduction LISS-0059's own
   Acceptance Notes describe — full pasted output, both runs, using the
   exact `scripts/copy-ai-collaboration-files.sh` invocation
   `.github/workflows/ci.yml`'s own "Check template copy smoke test" step
   uses.
2. `python3 scripts/check-contract-consistency.py` (real repository, no
   `--repo` flag) — full output, confirming no regression.
3. `git diff scripts/lib/collaboration-template-paths.sh` — confirms
   exactly one line added, nothing else touched.
4. Confirmation `docs/archive` does not appear anywhere under the copied
   target directory after the fix (it must remain un-copied).

## Review Summary Packet

Filled in by the Implementation group once Preflight passes.

- **Scope**: added one array entry
  (`scripts/lib/collaboration-template-paths.sh`'s
  `collaboration_template_exclude_paths`) so the checker's existing
  copy-exclusion exemption logic recognizes `docs/archive/*` references as
  expected-absent on a copied target; unblocks PR #21.
- **Current canonical documents**: none newly established;
  `scripts/lib/collaboration-template-paths.sh` is not an ADR-0006
  contract file, but is treated with the same reproduction rigor as any
  checker-affecting change in this repository's history.
- **Changed files**: `scripts/lib/collaboration-template-paths.sh` only.
- **Findings**: none opened; corrects (without editing)
  `docs/backlog/item-0018-...md`'s own premise about `LISS-0044`'s status.
- **Disposition**: <filled in at Preflight>
- **Remaining blockers**: none expected; state any found.
- **Verification result**: <pointer to this file's own Preflight
  Validation section, populated above>.
- **Next approval required**: evidence-sufficiency (is the CI failure
  genuinely reproduced locally and genuinely fixed, with real pasted
  output) — the one approval type most directly at stake for a one-line
  data fix; specification-conformance, phase-correctness, and
  boundary-conformance are secondary since no specification, phase, or
  architecture boundary is touched.

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

- A fixture/reproduction that does not use the exact same
  `copy-ai-collaboration-files.sh` invocation CI uses could produce a
  different result than the real CI failure. Mitigated by requiring
  LISS-0059's own reproduction to read `.github/workflows/ci.yml`'s own
  step before reproducing, and to use the identical flags.
- This work plan is explicitly blocking PR #21's own merge; a delay here
  has a direct downstream effect. Mitigated by the fix's own narrow,
  one-line scope and already-confirmed root cause (no open design
  question remains).

## Verification Plan

- Before/after copy-smoke-test reproduction (pasted output).
- `python3 scripts/check-contract-consistency.py` against the real
  repository, before and after (no regression).
- `git diff` confirming a one-line change.
- Confirmation `docs/archive` remains un-copied.
- Independent work-plan-level Reviewer approval, in a separate context.
