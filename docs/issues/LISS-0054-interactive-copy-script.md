# LISS-0054: Interactive prompting for `scripts/copy-ai-collaboration-files.sh`

## Metadata

- Local issue ID: LISS-0054
- GitHub issue: none
- Status: done
- Phase: phase-0-design
- Type: feature
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (Implementer persona)
- Related branch: process/interactive-copy-script (Implementation-group
  worktree branch, merged into the shared branch
  `process/promote-item-0015`)

## Summary

- `scripts/copy-ai-collaboration-files.sh` is flag-driven only: a new
  adopter must know `--target`, `--project-name`, `--domain-summary`, and
  `--stack` up front. `scripts/update-ai-collaboration-files.sh` already has
  a working interactive-prompt precedent (`is_interactive_tty()`, an
  explicit stated default per prompt, `--non-interactive` override) that
  this issue mirrors.
- Add: an `is_interactive_tty()` helper identical in shape to the one in
  `scripts/update-ai-collaboration-files.sh` (checks
  `[ "$non_interactive" != true ] && [ -t 0 ] && [ -t 1 ]`); a new
  `--non-interactive` flag; and, when interactive and a value was not
  supplied as a flag, a prompt for each of `--target` (required — loops on
  an empty response, since no default is possible), `--project-name`,
  `--domain-summary`, and `--stack` (each optional — a single prompt,
  stating the field is optional, empty response accepted and treated
  exactly as if the flag were omitted).
- `--force` and `--dry-run` stay flag-only, never prompted (see the design
  agreement's Settled Ambiguities for the grounds).
- Exact prompt text, flow placement, and every scenario this must satisfy:
  `docs/specs/interactive-copy-script.feature.md`.
- Deterministic verification: a new Python test file driving the script
  through a real pseudo-terminal via the standard-library `pty` module
  (test-only infrastructure; the shipped script stays bash-only). Add it as
  a new CI step alongside the existing "Check template copy smoke test"
  step in `.github/workflows/ci.yml`, so the interactive behavior is
  actually exercised in CI, not only exercised by a flag-driven smoke test
  that never engages the TTY-gated code path.

## Acceptance Notes

- Every Gherkin scenario in `docs/specs/interactive-copy-script.feature.md`
  has a passing, deterministic test exercising it (pty-based for the
  TTY-gated scenarios; a plain non-TTY invocation is sufficient for the
  "non-interactive shell skips all prompting" scenario, since the existing
  CI runner already provides that condition for free).
- `bash -n scripts/copy-ai-collaboration-files.sh` passes.
- The existing "Check template copy smoke test" CI step continues to pass
  unmodified — this is additive, not a replacement for flag-driven use.
- `python3 scripts/check-contract-consistency.py --repo .` passes (this
  issue touches no contract file, so this is a regression check, not an
  expected-change check).
- `scripts/copy-ai-collaboration-files.sh --help` documents `--non-interactive`
  and states that missing values are prompted for interactively.
- Self-review recorded at each phase transition (Red to Green, Green to
  Refactor), per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`;
  full-form self-review per `docs/architecture/adr/0015-review-cost-discipline.md`
  (planning size `M`).

## Review Finding Record

N/A — `Type` is `feature`, not `review-finding`.

## Dependencies

- Parent: docs/work-plans/WP-0018-interactive-copy-script.md
- Depends on: none
- Blocks: none
- Related: `docs/backlog/item-0015-interactive-copy-script.md`,
  `scripts/update-ai-collaboration-files.sh` (the interactive-prompt
  precedent mirrored here), `docs/collaboration/adoption-guide.md` (read
  for context, not changed — see spec's Out of Scope)

## Decisions Not Settled by the Design Agreement

- None identified — both judgment calls the backlog item flagged
  (`--force`/`--dry-run` prompting; empty-optional-prompt behavior) are
  settled in `DA-2026-08-20-01`'s Settled Ambiguities, and the exact prompt
  contract is pinned down in the spec referenced above. If the Implementer
  finds a case the spec does not cover, that is a reopening request, not a
  judgment call to resolve unilaterally.

## Context

- Included: `docs/backlog/item-0015-interactive-copy-script.md` (whole
  file), `scripts/copy-ai-collaboration-files.sh` (whole file, current
  state), `scripts/update-ai-collaboration-files.sh` (whole file, as the
  precedent — specifically `is_interactive_tty()` and
  `ask_restore_or_keep_deleted()`), `.github/workflows/ci.yml`'s "Check
  template copy smoke test" step, `docs/specs/interactive-copy-script.feature.md`.
- Omitted: `scripts/lib/collaboration-template-paths.sh` and
  `scripts/init-llm-context.sh` (unrelated to prompting; not touched),
  `docs/collaboration/adoption-guide.md`'s full body (only its two lines
  naming the copy script were checked, per the spec's Out of Scope).
- Assumptions: `python3` is available in every environment this script
  already runs in, since `scripts/check-contract-consistency.py` already
  requires it and CI already invokes `python3` directly — using it for
  test-only pty driving adds no new environment requirement.

## AI Planning Records

### AIP-0054-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code (Design & Review group session)
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A (not surfaced by this harness)
  - N/A reason: this environment does not display a separate reasoning-effort
    label to the session itself.
- Created at: 2026-08-20
- Planning size: M
- Intended execution route: Implementation-group subagent, isolated git
  worktree, branch `process/interactive-copy-script`, merged back into the
  shared branch `process/promote-item-0015` on completion.
- Compatibility state: Verified — `is_interactive_tty()`'s shape and the
  pty-driving approach (`python3 -c` with `pty.fork()`) were both smoke-
  tested directly in this session before this plan was written.
- Intended scope: `scripts/copy-ai-collaboration-files.sh`,
  `.github/workflows/ci.yml` (one new step), one new pty-based Python test
  file under `scripts/tests/`.
- Estimated token range: 40,000-90,000
- Estimated token midpoint: 65,000
- Token metric: cumulative input+output tokens across the Implementer
  subagent's Red+Green+Refactor turns, as reported by that session's own
  usage accounting.
- Estimation basis: comparable in surface area to WP-0016's
  drift-prevention CI-check issues (new script logic plus one new CI step
  plus a dedicated test artifact), scaled down since no new architecture
  document is involved.
- Assumptions: single execution attempt; no dependency-adoption note
  needed (python3's `pty` module is standard library, not a new
  dependency).
- Confidence: medium — the prompt-flow design itself is fully pinned down
  by the spec, but pty-based test flakiness (timing-sensitive reads) is a
  known general risk class for this approach and could require a second
  attempt at the test file specifically.
- Revises: N/A
- Revision reason: N/A
- Superseded by: N/A

## References

- `scripts/update-ai-collaboration-files.sh` (this repository, current
  branch) — the interactive-prompt precedent mirrored by this issue.
- Python standard library `pty` module documentation
  (https://docs.python.org/3/library/pty.html) — used for the pseudo-
  terminal test harness; standard library only, no external package.

## Work Notes

- 2026-08-20: Issue created by the Design & Review group (Planner/Specifier
  persona) under `DA-2026-08-20-01`, following ADR 0016 Rule 2 autonomous
  planning from `docs/backlog/item-0015-interactive-copy-script.md`'s
  promotion.
- 2026-08-20 (Implementer persona, Phase 1 Red): Added
  `scripts/tests/test_copy_ai_collaboration_files_interactive.py` (pty-based,
  one test per Gherkin scenario in
  `docs/specs/interactive-copy-script.feature.md`, 9 tests total) and ran it
  against the current, unmodified `scripts/copy-ai-collaboration-files.sh`.
  Self-review (Full form, per `docs/templates/self-review.md` and
  `docs/templates/review-record.md`, planning size `M`):

  **Command run**: `python3
  scripts/tests/test_copy_ai_collaboration_files_interactive.py -v`

  **Deterministic Verification Output** (test names and outcomes; full
  transcript captured in this session's own record):

  ```text
  test_empty_optional_response_skips_placeholder_replacement ... ok
  test_force_and_dry_run_stay_flag_only_never_prompted ... ok
  test_non_interactive_flag_forces_flag_only_behavior ... FAIL
  test_non_interactive_shell_skips_all_prompting ... ok
  test_prompts_for_each_missing_optional_value_once ... FAIL
  test_prompts_for_missing_target_when_omitted_interactively ... FAIL
  test_prompts_still_fire_under_dry_run ... FAIL
  test_reprompts_target_on_empty_response ... FAIL
  test_supplied_flags_are_never_prompted_for ... ok

  Ran 9 tests in 7.410s
  FAILED (failures=5)
  ```

  **Falsification Search** (why each of the 5 failures is a genuine Red, and
  why each of the 4 passes is not a false/gamed Red rather than a real gap):

  | # | Scenario | Result | Grounds |
  |---|---|---|---|
  | 1 | Prompt for missing target interactively | FAIL | Script exits 2 with `--target is required.` before any prompt text can appear -- no prompting code exists yet; genuine Red for what task 2 must add. |
  | 2 | Re-prompt on empty target response | FAIL | Same `--target is required.` exit; `A target directory is required.` is never printed -- the re-prompt loop does not exist yet. |
  | 3 | Prompt for each missing optional value once | FAIL (`PROJECT_NAME_PROMPT` count `0 != 1`) | The three optional-value prompts do not exist yet; the unmodified script silently treats an omitted flag as `""` and completes a full copy with no prompt. |
  | 4 | Prompts still fire under `--dry-run` | FAIL | Same root cause as #1 (no `--target` flag was passed and no prompt exists to collect it) -- this scenario specifically needs the prompting code path task 2 adds. |
  | 5 | `--non-interactive` forces flag-only behavior | FAIL, via a different mechanism than #1-#4: the unmodified script has no `--non-interactive` flag, so argument parsing itself rejects it (`Unknown option: --non-interactive`, exit 2) rather than reaching `--target is required.` | This is the expected Red shape for this scenario specifically, named in advance in this task's own instructions -- confirms `--non-interactive` truly does not exist pre-implementation, not an assertion bug. |
  | 6 | A supplied flag is never prompted for | PASS (trivially) | With no prompting code present at all, no prompt can ever be printed, so "no prompt" assertions hold vacuously -- a regression guard for task 2, not evidence the feature already works. |
  | 7 | Non-interactive shell skips all prompting | PASS (trivially) | Same vacuous-truth reasoning as #6: the unmodified script already never prompts, under any condition. |
  | 8 | `--force`/`--dry-run` stay flag-only, never prompted | PASS (trivially) | Same vacuous-truth reasoning as #6 -- and stays true after Green too, since no force/dry-run prompt is ever added (settled ambiguity in `DA-2026-08-20-01`). |
  | 9 | Empty optional response skips placeholder replacement | PASS, not vacuously | The unmodified script already implements "empty value = no placeholder replacement" for *flag-omitted* values (`replace_placeholders`'s `[ -n "$project_name" ]` guards). This test supplies `--target` as a flag and never triggers a prompt (none exists), so the three optional fields stay `""` by flag-omission -- behaviorally identical to what an empty *prompted* response should produce once Green lands. Expected to keep passing unchanged through Green: a real regression guard proving the two "empty" paths (omitted flag, empty prompt response) stay equivalent, per `DA-2026-08-20-01`'s Settled Ambiguities. |

  **Risks considered and why each does not invalidate this Red state**:
  - A "FAIL" could be a broken test (assertion bug) rather than a genuine
    behavior gap. Does not occur: each failure's captured output was
    inspected above and traces to "prompting code does not exist yet" (an
    immediate `--target is required.` exit, or `Unknown option` for the
    not-yet-recognized `--non-interactive` flag), not a Python-side harness
    error -- the harness ran the script to completion in all 9 cases with
    the exit-code shape expected for each pre-implementation branch.
  - A "PASS" could be a false negative hiding an actual gap (test not
    exercising what it claims to). Does not occur: traced per scenario
    (6-9) above -- each pass is either vacuous non-prompting truth, or
    (scenario 9) an intentional equivalence the design agreement itself
    settles, not an assertion that silently no-ops.
  - Pty timing flakiness (named in WP-0018's own "Risks" section) could
    produce a spurious FAIL or a hang. Does not occur here: the harness
    polls with `select.select(..., 0.2)` against a wall-clock budget rather
    than a single fixed sleep, and this run completed in 7.4s across all 9
    tests with no `ScriptTimeout` raised.

  Self-reviewed and accepted as the Red state. Proceeding to Phase 2 Green.

- 2026-08-20 (Implementer persona, Phase 2 Green): Implemented the smallest
  change satisfying every test from task 1, in
  `scripts/copy-ai-collaboration-files.sh`: `non_interactive=false` beside
  `force`/`dry_run`; a `--non-interactive)` case in the existing flag-parsing
  loop; `is_interactive_tty()` (identical shape to
  `scripts/update-ai-collaboration-files.sh`'s own helper); the required-target
  prompt loop and the three optional-value prompts, both inserted between the
  end of flag parsing and the existing (untouched) `if [ -z "$target" ]...
  exit 2` / `if [ ! -d "$target" ]... exit 1` checks; and a `usage()` update
  documenting `--non-interactive` and the new interactive-prompting behavior.
  No test was edited to pass. Self-review (Full form):

  **Command run 1**: `bash -n scripts/copy-ai-collaboration-files.sh`
  **Result**: exit 0, no output (syntax valid).

  **Command run 2**: `python3
  scripts/tests/test_copy_ai_collaboration_files_interactive.py -v`
  **Result**:
  ```text
  test_empty_optional_response_skips_placeholder_replacement ... ok
  test_force_and_dry_run_stay_flag_only_never_prompted ... ok
  test_non_interactive_flag_forces_flag_only_behavior ... ok
  test_non_interactive_shell_skips_all_prompting ... ok
  test_prompts_for_each_missing_optional_value_once ... ok
  test_prompts_for_missing_target_when_omitted_interactively ... ok
  test_prompts_still_fire_under_dry_run ... ok
  test_reprompts_target_on_empty_response ... ok
  test_supplied_flags_are_never_prompted_for ... ok

  Ran 9 tests in 7.647s
  OK
  ```
  All 9 tests pass, including the 5 that were genuinely Red in task 1.

  **Command run 3**: the exact block from `.github/workflows/ci.yml`'s
  "Check template copy smoke test" step, pasted into a local shell against a
  fresh `mktemp -d` target (adjusted only to `cd` into this worktree first).
  **Result**: every `test -f` / `! ls` assertion passed, `python3
  scripts/check-contract-consistency.py --repo .` inside the copied target
  printed `contract consistency: all checks passed`, the placeholder-leftover
  grep found nothing, and the script printed `SMOKE_TEST_PASSED` at the end.
  No prompt text appeared anywhere in the transcript (flags supplied all four
  values, confirming the additive-only requirement holds under an actual,
  non-pty shell invocation too, not just the pty harness).

  **Falsification Search**:

  | # | Risk considered | Grounds it does not occur |
  |---|---|---|
  | 1 | The new prompting code could fire even when a value was supplied as a flag (breaking the "additive only" falsification criterion in `DA-2026-08-20-01`). | Every prompt is guarded by `[ -z "$<var>" ]` (target) or nested `if [ -z "$<var>" ]` per optional field; a flag-supplied value is never empty at that point in the script, so the guard skips the prompt. Directly exercised by `test_supplied_flags_are_never_prompted_for` (pass) and the manual smoke-test run above (no prompt text in output). |
  | 2 | The prompting code could run and block even without a real TTY (breaking the "never hang a scripted/CI caller" falsification criterion). | `is_interactive_tty()` requires `[ -t 0 ] && [ -t 1 ]`; `run_non_interactive()` in the test harness redirects stdin from `/dev/null` (never a TTY), and CI's own smoke-test step never allocates a pty either. Exercised by `test_non_interactive_shell_skips_all_prompting` (pass, no timeout) and the smoke-test run (completed without hanging). |
  | 3 | `--non-interactive` could fail to override a real TTY (breaking the same falsification criterion from the other direction). | `is_interactive_tty()`'s first condition is `[ "$non_interactive" != true ]`; with the flag set this short-circuits false before the `-t` checks run, regardless of terminal state. Exercised by `test_non_interactive_flag_forces_flag_only_behavior` (pass, no timeout despite running under a real pty). |
  | 4 | The existing "Check template copy smoke test" CI step could start failing (the design agreement's explicit falsification criterion for backward compatibility). | Re-ran the exact step content manually against this Green implementation; see Command run 3 above -- passed unchanged, ending in `SMOKE_TEST_PASSED`. |
  | 5 | The re-prompt loop on empty target input could go infinite or exit incorrectly instead of looping. | `while [ -z "$target" ]; do read -r -p ... target || true; ... done` re-evaluates `$target` each iteration; `test_reprompts_target_on_empty_response` sends one empty response then a real path and asserts the prompt is printed exactly twice and the process still exits 0 -- pass, so the loop terminates on the first non-empty input rather than looping forever or falling through early. |
  | 6 | Empty optional responses could still trigger `replace_placeholders`'s substitutions (breaking the settled "empty prompt == omitted flag" equivalence). | `replace_placeholders()`'s guards (`[ -n "$project_name" ]`, etc.) are unchanged by this diff; an empty `read -r -p` response leaves the variable `""`, identical to an omitted flag. Exercised end-to-end (real copy, not `--dry-run`) by `test_empty_optional_response_skips_placeholder_replacement` (pass): the copied `CLAUDE.md` still contains the literal `<PROJECT_NAME:` placeholder. |
  | 7 | `--force`/`--dry-run` could have accidentally gained a prompt (out of scope per the design agreement). | No code path in the diff reads or prompts for `force` or `dry_run` at all -- grep of the diff confirms neither identifier appears inside either new `if is_interactive_tty` block. Exercised by `test_force_and_dry_run_stay_flag_only_never_prompted` (pass). |

  Self-reviewed and accepted as the Green state. Proceeding to Phase 3
  Refactor.

- 2026-08-20 (Implementer persona, Phase 3 Refactor): Added a "Check
  interactive copy script prompting" CI step to
  `.github/workflows/ci.yml`, immediately after the existing "Check template
  copy smoke test" step, running
  `python3 scripts/tests/test_copy_ai_collaboration_files_interactive.py`
  (plain invocation -- `unittest.main()`'s own default exit behavior already
  gives a nonzero exit code on any failure, so no extra assertion wrapper is
  needed). No refactor of `scripts/copy-ai-collaboration-files.sh` itself was
  made: the Green diff is already small, the two new prompting blocks read
  clearly as "required value, loops" vs. "three optional values, single
  prompt each", and merging them into one block would reduce rather than
  improve readability for no behavior gain. Self-review (Full form):

  **Command run 1**: `bash -n scripts/copy-ai-collaboration-files.sh`
  **Result**: exit 0, no output (syntax still valid; unchanged from Phase 2's
  own run since this phase did not touch the script).

  **Command run 2**: `python3 scripts/check-contract-consistency.py --repo .`
  **Result**:
  ```text
  issue status sync:
    docs/issues/LISS-0054-interactive-copy-script.md states Status: in_progress, but docs/work-plans/WP-0018-interactive-copy-script.md's Issue Graph lists LISS-0054 as 'ready'

  contract consistency: 1 failure(s)
  ```
  This is a real, deterministic failure, not suppressed here -- and it is
  not a defect in this issue's own work. Root cause: this task's own scope
  explicitly requires progressing LISS-0054's `Status:` field (ready ->
  in_progress -> done, recorded above) while explicitly forbidding any edit
  to `docs/work-plans/WP-0018-interactive-copy-script.md`'s Issue Graph --
  that table's Status column is the Design & Review group's own
  responsibility, updated at Preflight/merge time (WP-0018's own Plan table,
  task 4, names Preflight as run by "Design & Review group (not the
  Implementer's own context)"). The two boundaries together mean this
  specific mismatch is structurally guaranteed on this branch, in either
  direction (`in_progress` vs. `ready`, and now `done` vs. `ready` after this
  entry's own Status update above), until the Design & Review group merges
  this branch and updates WP-0018's Issue Graph accordingly -- a step this
  issue's own scope places outside the Implementer's authority. Re-running
  the check after this Work Notes entry (with `Status: done` in the Metadata
  above) reproduces the same single failure, now naming `'done'` instead of
  `'in_progress'` as the mismatched value -- confirming the mismatch is
  exactly this one field pair, not a second, independent problem.

  **Falsification Search**:

  | # | Risk considered | Grounds it does not occur |
  |---|---|---|
  | 1 | The new CI step's command could exit 0 even when a test genuinely fails (a silently-broken gate). | `unittest.main()` calls `sys.exit()` with a nonzero code whenever any test fails or errors, by its own standard-library contract; the CI step has no `\|\| true` or other suppression, and `set -euo pipefail` is active, so a nonzero exit from the `python3` invocation fails the step. |
  | 2 | Adding the CI step could itself be a YAML syntax error, silently skipping the step rather than running it. | Read back the full `.github/workflows/ci.yml` after the edit (see diff); the new step follows the same `- name: ... / shell: bash / run: \|` shape as every existing step in the same job, at the same indentation level. |
  | 3 | The contract-consistency failure above could be masking a second, unrelated contract violation this change actually introduced. | The failure list contains exactly one entry (`issue status sync`), and its message is fully explained by the `Status:` field edit this Work Notes entry itself makes -- no ADR-sequence, required-file, retired-terminology, or other category fired. This change touches no file `check-contract-consistency.py` treats as a contract file (`docs/collaboration/*.md`, `docs/templates/*.md`, ADRs); `scripts/copy-ai-collaboration-files.sh`, `.github/workflows/ci.yml`, and `scripts/tests/*.py` are not contract files under that script's own rules. |
  | 4 | The refactor decision (no code change) could be hiding a real readability problem a Reviewer would flag. | Re-read the full script after Green (`scripts/copy-ai-collaboration-files.sh`, 257 lines); the two prompting blocks are 8 and 11 lines respectively, each single-purpose, matching the existing file's own style (small top-level blocks, no nested abstraction) -- consistent with `docs/collaboration/source-code-quality.md`'s "small functions, straightforward names" guidance already read at session start. |

  **Verification gap this Phase 3 leaves for the work-plan-level Reviewer**:
  the `issue status sync` contract-consistency failure above is expected to
  persist until WP-0018's Issue Graph is updated at merge/Preflight time (not
  an Implementer action per this issue's own scope) -- Preflight Validation
  should confirm the failure clears once that update happens, rather than
  independently re-deriving that it is expected.

  Self-reviewed and accepted as the Refactor state.

## Verification

- Phase 1 Red: `python3
  scripts/tests/test_copy_ai_collaboration_files_interactive.py -v` against
  the unmodified script -- 5 genuine failures, 4 trivial/regression-guard
  passes (see Work Notes above for the full breakdown and grounds).
- Phase 2 Green: `bash -n scripts/copy-ai-collaboration-files.sh` (pass);
  `python3 scripts/tests/test_copy_ai_collaboration_files_interactive.py -v`
  (9/9 pass); the exact CI "Check template copy smoke test" step content, run
  manually (pass, `SMOKE_TEST_PASSED`).
- Phase 3 Refactor: `bash -n scripts/copy-ai-collaboration-files.sh` (pass);
  `python3 scripts/check-contract-consistency.py --repo .` -- 1 expected
  failure (`issue status sync`, LISS-0054 `Status:` vs. WP-0018's Issue
  Graph; see Work Notes above for why this is expected and out of this
  issue's own scope to fix, and needs the Design & Review group's WP-0018
  update at merge/Preflight time to clear).
- This issue's own remaining verification is complete. Preflight Validation
  and the work-plan-level Reviewer pass are recorded in
  `docs/work-plans/WP-0018-interactive-copy-script.md` by the Design &
  Review group, not here.
