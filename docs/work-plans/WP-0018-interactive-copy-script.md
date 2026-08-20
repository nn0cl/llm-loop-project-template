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
| LISS-0054 | done | M | M | AIP-0054-001 | - | - | process/interactive-copy-script (merged, fast-forward, into `process/promote-item-0015` at `b3dd9a2`) |

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

Run by the Design & Review group (this session), independently re-executed
in this session's own worktree — not copied from the Implementer's pasted
output — after fast-forward-merging `process/interactive-copy-script`
(commit `b3dd9a2`) into the shared branch `process/promote-item-0015`
(`git merge --ff-only`, no merge commit; `HEAD` is now `b3dd9a2`).

- Result: `pass`
- Checks and command output:

  ```console
  $ bash -n scripts/copy-ai-collaboration-files.sh
  $ echo $?
  0
  ```

  ```console
  $ python3 scripts/tests/test_copy_ai_collaboration_files_interactive.py -v
  test_empty_optional_response_skips_placeholder_replacement ... ok
  test_force_and_dry_run_stay_flag_only_never_prompted ... ok
  test_non_interactive_flag_forces_flag_only_behavior ... ok
  test_non_interactive_shell_skips_all_prompting ... ok
  test_prompts_for_each_missing_optional_value_once ... ok
  test_prompts_for_missing_target_when_omitted_interactively ... ok
  test_prompts_still_fire_under_dry_run ... ok
  test_reprompts_target_on_empty_response ... ok
  test_supplied_flags_are_never_prompted_for ... ok

  ----------------------------------------------------------------------
  Ran 9 tests in 7.194s

  OK
  ```

  ```console
  $ scripts/copy-ai-collaboration-files.sh --target <fresh tmp dir> \
      --project-name "Smoke App" --domain-summary "template smoke test" \
      --stack "test stack"
  $ echo $?
  0
  ```
  (the pre-existing "Check template copy smoke test" CI step content,
  reproduced manually against a fresh `mktemp -d` target; every `test -f`
  and placeholder-leftover check the CI step itself performs was also
  re-run and passed — flag-driven use is unmodified.)

  ```console
  $ python3 scripts/check-contract-consistency.py --repo .
  ```
  First run (before this Preflight updated WP-0018's own Issue Graph):
  ```text
  issue status sync:
    docs/issues/LISS-0054-interactive-copy-script.md states Status: done, but docs/work-plans/WP-0018-interactive-copy-script.md's Issue Graph lists LISS-0054 as 'ready'

  contract consistency: 1 failure(s)
  ```
  Root cause: exactly as the Implementer's own Work Notes entry
  anticipated — the Issue Graph update is this group's own responsibility,
  not the Implementer's, per this work plan's own Scope/Plan. Fixed by
  updating this file's Issue Graph row for LISS-0054 to `done` (see above).
  Re-run after that edit:
  ```text
  contract consistency: all checks passed
  ```

  A real, manual, live-terminal interactive run was also performed in this
  session (not only the automated pty test suite) — see "Manual Reviewer
  verification" under Work-Plan Review below for the two live transcripts
  and what each confirmed.

- Scope result: `git diff 522f5cf..HEAD --stat` (`522f5cf` is
  `docs/backlog/item-0015-interactive-copy-script.md`'s promotion commit,
  the base this whole work plan started from):
  ```text
   .github/workflows/ci.yml                           |   6 +
   .../2026-08-20-interactive-copy-script.md          | 155 +++++++++
   docs/issues/LISS-0054-interactive-copy-script.md   | 370 +++++++++++++++++++++
   docs/specs/interactive-copy-script.feature.md      | 157 +++++++++
   docs/work-plans/WP-0018-interactive-copy-script.md | 145 ++++++++
   scripts/copy-ai-collaboration-files.sh             |  38 +++
   .../test_copy_ai_collaboration_files_interactive.py | 355 ++++++++++++++++++++
   7 files changed, 1226 insertions(+)
  ```
  Every changed/added file is within this work plan's stated Scope; no
  file outside it (`docs/collaboration/adoption-guide.md`,
  `scripts/update-ai-collaboration-files.sh`, or any other
  `docs/collaboration/*.md` contract file) was touched.
- Next action: submit to the work-plan-level Reviewer (this session,
  separate context from the Implementer subagent that wrote the code).

## Review Summary Packet

Filled in once Preflight Validation passes, before submitting to the
work-plan-level Reviewer.

- **Scope**: `scripts/copy-ai-collaboration-files.sh` now prompts
  interactively for `--target` (required, re-prompts on empty), and
  `--project-name`/`--domain-summary`/`--stack` (each optional, single
  prompt, empty response = same as an omitted flag) when a real terminal
  is present and the value was not supplied as a flag; a new
  `--non-interactive` flag forces the old flag-only behavior even in a
  real terminal. Purely additive — flag-driven, non-interactive use is
  byte-for-byte unchanged. Backed by a new pty-based test suite (9 tests,
  one per Gherkin scenario) and a new CI step running it.
- **Current canonical documents**: `docs/specs/interactive-copy-script.feature.md`
  becomes the current behavior spec for `scripts/copy-ai-collaboration-files.sh`'s
  interactive mode; no ADR or contract file is added or amended by this
  work plan.
- **Changed files**: `.github/workflows/ci.yml` (+6, one new CI step);
  `docs/collaboration/agreements/2026-08-20-interactive-copy-script.md`
  (new, 155 lines); `docs/issues/LISS-0054-interactive-copy-script.md`
  (new, 370 lines); `docs/specs/interactive-copy-script.feature.md` (new,
  157 lines); `docs/work-plans/WP-0018-interactive-copy-script.md` (this
  file, new, 145+ lines before this Preflight/Review pass's own edits);
  `scripts/copy-ai-collaboration-files.sh` (+38); `scripts/tests/test_copy_ai_collaboration_files_interactive.py`
  (new, 355 lines). Matches Preflight's own Scope result exactly (`git diff
  522f5cf..HEAD --stat`).
- **Findings**: none opened or resolved by this work plan.
- **Disposition**: resolved cleanly — no blockers, no deferred rework,
  single execution attempt (Red → Green → Refactor, each self-reviewed;
  the one contract-consistency mismatch found during Preflight was this
  group's own expected bookkeeping step, not a defect returned to the
  Implementer).
- **Verification result**: this section's own Preflight Validation output
  above (independently re-run in this session, not copied from the
  Implementer's pasted transcript) — `bash -n` clean, 9/9 pty tests pass,
  the pre-existing flag-driven smoke test unaffected,
  `check-contract-consistency.py` clean after this group's own Issue Graph
  update.
- **Next approval required**: `Specification conformance` (does the
  implementation match every scenario in
  `docs/specs/interactive-copy-script.feature.md`) and `Evidence
  sufficiency` (does the pty-based test suite genuinely exercise the
  TTY-gated branches, not just the flag-driven path the pre-existing smoke
  test already covered, and does a real live-terminal run — not only the
  automated harness — confirm the same behavior).

## Work-Plan Review

Reviewer's approval record: `docs/collaboration/reviews/2026-08-20-wp-0018-interactive-copy-script-review.md`
— **Approved** (Specification conformance, Evidence sufficiency), separate
context from the Implementer subagent. Falsification search included one
scenario not named in the Implementer's own stated verification gap
(EOF/Ctrl-D at the required-target prompt) and two independent live
manual interactive runs of the script, per this session's own mandate.

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
| none | N/A | Reviewer approved with no findings; the one contract-consistency mismatch surfaced during Preflight was expected bookkeeping (WP-0018's own Issue Graph update), not a review finding against the Implementer's work. |

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
