# Work Plan: Interactive copy script

## Goal

- Make `scripts/copy-ai-collaboration-files.sh` prompt for `--target`,
  `--project-name`, `--domain-summary`, and `--stack` when they are not
  supplied as flags and an interactive terminal is present, mirroring
  `scripts/update-ai-collaboration-files.sh`'s existing interactive-prompt
  precedent, per `docs/backlog/item-0015-interactive-copy-script.md` and
  `docs/collaboration/agreements/2026-08-20-interactive-copy-script.md`
  (`DA-2026-08-20-01`).

## Scope

- In: `scripts/copy-ai-collaboration-files.sh` (new `is_interactive_tty()`
  helper, new `--non-interactive` flag, prompting for the four named
  values, updated `usage()`); a new pty-based deterministic test file under
  `scripts/tests/`; one new CI step in `.github/workflows/ci.yml` exercising
  it; `docs/specs/interactive-copy-script.feature.md` (already written by
  the Design & Review group, ahead of this work plan, as part of design
  intake).
- Out: any change to `scripts/update-ai-collaboration-files.sh` itself;
  any change to `docs/collaboration/adoption-guide.md`; prompting for
  `--force` or `--dry-run` (both stay flag-only); re-validating a prompted
  `--target` path's existence beyond the script's single existing check —
  see the spec's own "Out of Scope" section for the full, authoritative
  list.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0054 | ready | M | M | AIP-0054-001 | - | - | process/interactive-copy-script |

## Plan-Owned Bug Records

None.

## AI Planning Records

See LISS-0054's own `AIP-0054-001` — this work plan has a single issue and
does not duplicate the record here.

## Recommended Order

1. LISS-0054 (single issue: Red, then Green, then Refactor, each
   self-reviewed before the next phase starts).

## Current Next Issue

- Issue: LISS-0054
- Reason it is unblocked: no dependencies; `DA-2026-08-20-01` covers it
  fully, including the exact prompt contract (the spec), the settled
  judgment calls, and the deterministic verification approach.
- Reopening request needed: no.

## Minor Fix Path

Does not apply — this is new behavior (Feature Path), not a review-finding
correction.

## Preflight Validation

Run by the Design & Review group, after the Implementation group's branch
is merged into the shared branch, before the separate-context Reviewer
pass. Recorded below once the Implementation group's work lands.

- Result: pending
- Checks and command output: pending
- Scope result: pending
- Next action: pending

## Review Summary Packet

Filled in once Preflight Validation passes, before submitting to the
work-plan-level Reviewer.

- **Scope**: pending — filled in after Preflight.
- **Current canonical documents**: `docs/specs/interactive-copy-script.feature.md`
  becomes the current behavior spec for `scripts/copy-ai-collaboration-files.sh`'s
  interactive mode; no ADR or contract file is added or amended by this
  work plan.
- **Changed files**: pending — filled in after Preflight, from the actual
  diff.
- **Findings**: none opened or resolved by this work plan.
- **Disposition**: pending.
- **Verification result**: pending — pointer to this section's own
  Preflight output once recorded.
- **Next approval required**: pending — expected to be `Specification
  conformance` (does the implementation match every scenario in the spec)
  and `Evidence sufficiency` (does the pty-based test suite actually
  exercise the TTY-gated branches, not just the flag-driven path already
  covered by the pre-existing smoke test).

## Work-Plan Review

Reviewer's approval record: pending

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves. Pending — this
work plan does not merge to `main`; per this session's own mandate, the
Backlog thread/Director performs the eventual `main` merge and close.

- Date: pending
- Result read: pending
- Next direction: pending
- New design agreement (if any): pending

## Risks

- pty-based test timing sensitivity: reading from a pseudo-terminal after
  writing input can race if the script has not yet reached its next
  `read -p` call. The Implementer should poll/retry reads with a bounded
  timeout rather than a single fixed `sleep`, and the test file's own
  comments should state the retry strategy so a later reader does not
  mistake a generous timeout for a hang.
- A prompt's exact wording is pinned down by the spec, but if the
  Implementer finds the spec ambiguous about phrasing (not behavior), it
  should choose wording consistent with `scripts/update-ai-collaboration-files.sh`'s
  own tone and note the choice in Work Notes, rather than treating a
  wording gap as a reopening trigger.

## Verification Plan

- `bash -n scripts/copy-ai-collaboration-files.sh` (syntax).
- The new pty-based Python test file, run directly (`python3
  scripts/tests/test_copy_ai_collaboration_files_interactive.py` or
  equivalent invocation the Implementer documents), covering every
  scenario in `docs/specs/interactive-copy-script.feature.md`.
- The existing "Check template copy smoke test" CI step, unmodified,
  confirming flag-driven use still works exactly as before.
- `python3 scripts/check-contract-consistency.py --repo .` (regression
  check; this work plan touches no contract file).
- Manual interactive run by the Design & Review group's own separate-
  context Reviewer pass (not just a diff read), per this session's own
  mandate — the Reviewer runs the changed script itself, in a real
  terminal, to confirm the prompts behave as specified.
