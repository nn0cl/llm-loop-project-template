# Review Record: WP-0018 Interactive copy script

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's own session, which did not write any of the code, tests, or
      CI step under review — that was produced by an Implementation-group
      subagent in its own isolated `git worktree` (`agentId
      a84ca59310c2cbece`, branch `process/interactive-copy-script`), spawned
      by this session but never given this review's own findings or
      reasoning. Only the merged artifacts (diff, commits, Work Notes,
      self-reviews) and the deterministic tool outputs below were used —
      the Implementer's own reasoning is not relied on as justification
      anywhere in this record; every claim below is re-derived from an
      independently re-run command or a live manual terminal session, not
      copied from the Implementer's pasted output.
- [x] **Deterministic precondition.** Deterministic verification was run
      (independently, in this session's own worktree, after merging) and
      its output is recorded below and in
      `docs/work-plans/WP-0018-interactive-copy-script.md`'s own Preflight
      Validation section (`pass`).
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, including one (EOF/Ctrl-D at the required-target prompt) not
      named anywhere in the Implementer's own stated verification gap —
      each with the grounds on which it does not occur.

## Review Target

- Artifact: `scripts/copy-ai-collaboration-files.sh` (interactive
  prompting), `scripts/tests/test_copy_ai_collaboration_files_interactive.py`
  (new), `.github/workflows/ci.yml` (one new step)
- Covering design agreement: `docs/collaboration/agreements/2026-08-20-interactive-copy-script.md`
  (`DA-2026-08-20-01`)
- Specification: `docs/specs/interactive-copy-script.feature.md`
- Current phase: Work-Plan Review (after Preflight `pass`)
- Producing persona: Implementer (Implementation-group subagent, isolated
  worktree, branch `process/interactive-copy-script`, merged
  fast-forward into `process/promote-item-0015` at `b3dd9a2`)
- Reviewing persona / model / tool: Reviewer, Claude Code (Claude Sonnet
  5), this Design & Review group session
- Approval type: Specification conformance, Evidence sufficiency (per
  WP-0018's Review Summary Packet's "Next approval required")
- Preflight Validation record: `docs/work-plans/WP-0018-interactive-copy-script.md`,
  "Preflight Validation" section
- Preflight result: pass

## Deterministic Verification Output

All commands below were re-run directly by this Reviewer session, in its
own worktree, after merging — not copied from the Implementer's pasted
transcript (per this repository's own "re-verify state that could have
changed underneath you" review perspective).

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
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed
```

Two live, manual pty-driven runs of the actual changed script (not the
automated test suite) — per this session's own mandate to actually run the
script interactively rather than rely on a diff read alone:

**Live run 1** (target + project name supplied, domain-summary/stack left
empty, real copy — not `--dry-run`):

```text
Target repository directory (required): <tmp target path>
Project name (optional, press Enter to skip): Manual Reviewer Check
One-line domain summary (optional, press Enter to skip):
Stack (optional, press Enter to skip):
copy AGENTS.md
copy CLAUDE.md
...
Done.
```
Exit code: 0. Confirmed directly in the copied files: `CLAUDE.md` line 8
reads `**Manual Reviewer Check**.` (the `<PROJECT_NAME: one-line
description...>` placeholder was replaced with the bare name, since
domain-summary was left empty — exactly the settled "empty prompt == empty
flag" equivalence), and the stack placeholder
(`<FILL IN: e.g. backend language, frontend framework, package manager>`)
remained untouched in the copied `CLAUDE.md`, confirming the empty stack
response was correctly treated as skipped.

**Live run 2** (target left empty twice, then supplied; `--dry-run`):

```text
Target repository directory (required):
A target directory is required.
Target repository directory (required):
A target directory is required.
Target repository directory (required): <tmp target path>
Project name (optional, press Enter to skip):
One-line domain summary (optional, press Enter to skip):
Stack (optional, press Enter to skip):
copy AGENTS.md
...
Done.
```
Exit code: 0. Confirmed the re-prompt loop correctly re-prompts on repeated
empty input and terminates cleanly once given a non-empty value; no hang,
no error, no double-processing of the eventually-supplied value.

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | A flag-supplied value is prompted for anyway (breaks the "additive only" falsification criterion in `DA-2026-08-20-01`). | Every prompt is gated by `[ -z "$var" ]`; a flag-supplied value is never empty at that point. `test_supplied_flags_are_never_prompted_for` passes, and the pre-existing flag-driven "Check template copy smoke test" CI content, re-run manually in this session, produced no prompt text and completed identically to before this change. | not reproduced |
| 2 | A non-interactive or `--non-interactive` invocation blocks on stdin (breaks the "never hang a scripted/CI caller" falsification criterion). | `is_interactive_tty()` requires `[ "$non_interactive" != true ] && [ -t 0 ] && [ -t 1 ]`; `test_non_interactive_shell_skips_all_prompting` and `test_non_interactive_flag_forces_flag_only_behavior` both pass with no timeout, and the existing CI smoke-test step (never allocates a pty) is unaffected. | not reproduced |
| 3 | The re-prompt loop never terminates, or terminates on the wrong condition. | `test_reprompts_target_on_empty_response` (automated) and Live run 2 (manual, above) both show exactly two re-prompts on two empty responses, then correct termination on the third, non-empty response, exit 0. | not reproduced |
| 4 | EOF (Ctrl-D) at the required-target prompt, rather than an empty line, causes a tight busy-loop or a crash — a scenario neither the spec's "operator presses Enter with no input" wording nor the Implementer's own stated verification gap names explicitly. | Manually driven with a real pty, sending a single `0x04` byte at the target prompt: the script printed the re-prompt exactly once, then blocked waiting for further input — the same way a real interactive shell's `read` behaves on a single Ctrl-D in canonical terminal mode (EOF is delivered once per keypress, not as a permanent fd closure) — not a busy loop, not a crash, not an early wrong-branch exit. | not reproduced |
| 5 | The `issue status sync` contract-consistency failure the Implementer's own Work Notes flagged as expected turns out to be masking a second, unrelated failure. | Re-ran `check-contract-consistency.py` before and after updating WP-0018's own Issue Graph row for LISS-0054: exactly one failure before (naming precisely the field pair the Implementer predicted), zero after. No other category fired. | not reproduced |
| 6 | Domain-summary given without project-name behaves differently under prompting than it already does under flags (a new interactive-mode-only inconsistency). | Traced `replace_placeholders()`: `project_replacement` starts as `"$project_name"`; the combined-format branch requires both to be non-empty. An empty `project_name` with a non-empty `domain_summary` leaves `project_replacement` empty either way the values were supplied (flag or prompt) — pre-existing behavior, unchanged and not newly divergent between the two input paths. Confirmed by inspection of the unmodified `replace_placeholders()` function, which this change does not touch. | not reproduced |
| 7 | `--force`/`--dry-run` gained a prompt path despite the design agreement settling they should not. | Grep of the diff (`scripts/copy-ai-collaboration-files.sh`) confirms neither `force` nor `dry_run` appears inside either new `is_interactive_tty` block; `test_force_and_dry_run_stay_flag_only_never_prompted` passes. | not reproduced |
| 8 | The new CI step could silently no-op (YAML indentation error placing it outside the job, or swallowing a nonzero exit). | Read the full updated `.github/workflows/ci.yml`; the new step matches the existing steps' exact shape (`- name: / shell: bash / run: |`) at the same indentation, under `set -euo pipefail`, with no `\|\| true` suppression; `unittest.main()`'s own default behavior exits nonzero on any failure. | not reproduced |

## Scenarios Not Searched

- Behavior under a genuinely unusual/non-UTF-8 terminal encoding, or a
  terminal that does not support `read -r -p`'s prompt echoing normally
  (e.g. certain restricted CI runner shells that still report `-t 0`/`-t 1`
  true). Judged low-risk: the same `is_interactive_tty()`/`read -r -p`
  shape is already in production use via
  `scripts/update-ai-collaboration-files.sh` with no reported issue of this
  kind.
- Concurrent/parallel invocations of the script against the same target
  directory. Out of scope for this work plan and not a new risk this
  change introduces (the underlying `copy_path`/`replace_placeholders`
  logic is unchanged).
- Locale-specific behavior of `read -r -p` prompt rendering (e.g.
  right-to-left terminals). Not previously covered by
  `update-ai-collaboration-files.sh`'s own precedent either; no regression
  risk specific to this change.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase
      leaked in. (Red tests exist and were shown genuinely failing before
      Green; Green made no test edits; Refactor changed no behavior —
      confirmed by re-running the same 9/9-pass suite unchanged across
      Green and Refactor commits.)
- [x] Every `Then` clause in `docs/specs/interactive-copy-script.feature.md`
      is asserted by the work — verified scenario-by-scenario against the
      9 test methods in `scripts/tests/test_copy_ai_collaboration_files_interactive.py`,
      1:1, plus two independent live manual runs covering the same ground.
- [x] The dependency rule and port boundaries hold. N/A in the Clean
      Architecture sense — this change is to this repository's own process
      tooling (a bash script), not the application stack
      `docs/architecture/project-structure.md` governs, as stated in
      `DA-2026-08-20-01`'s Boundaries section.
- [x] No boundary named in the design agreement was crossed. Confirmed by
      Preflight's own Scope result: every changed/added file is within
      WP-0018's stated Scope; `docs/collaboration/adoption-guide.md` and
      `scripts/update-ai-collaboration-files.sh` are untouched.
- [x] Specifications and accepted tests were not modified to make work
      pass. `docs/specs/interactive-copy-script.feature.md` is unchanged
      since this session wrote it, before the Implementer started; the
      test file's 9 assertions are unchanged from Red through Refactor
      (confirmed: the Green and Refactor commits' diffs touch only
      `scripts/copy-ai-collaboration-files.sh`,
      `.github/workflows/ci.yml`, and `docs/issues/LISS-0054-*.md` — never
      the test file itself, per `git diff 8824ef3..b3dd9a2 --stat` on the
      Implementer's own branch history).
- [x] Every claim in the artifact states its grounds. Both self-review
      records (Full form, per planning size `M`) name the command run and
      the actual output for every claim.
- [x] The record would let a third party re-run this same search. Every
      command above is copy-pasteable; the two live manual runs used
      `scripts/tests/test_copy_ai_collaboration_files_interactive.py`'s own
      `run_interactive()` helper, so a third party can reproduce them with
      the same short driver script shape.

## Decision

- [x] Approved

## Reasons

- Every Gherkin scenario in `docs/specs/interactive-copy-script.feature.md`
  has a passing automated test and, for the highest-risk TTY-gated paths,
  independent live-terminal confirmation — satisfying `DA-2026-08-20-01`'s
  own Verification section, which explicitly required a real interactive
  run rather than a diff read alone.
- Backward compatibility is verified, not assumed: the pre-existing
  flag-driven CI smoke test was re-run manually against the Green
  implementation and produces byte-for-byte the same outcome.
- The one contract-consistency mismatch found during Preflight
  (`issue status sync`) was correctly anticipated by the Implementer's own
  Work Notes as this group's own bookkeeping responsibility, not a defect
  in the Implementer's work, and was resolved cleanly by updating WP-0018's
  Issue Graph.
- The falsification search went past what the Implementer's own stated
  verification gap named (EOF/Ctrl-D at the required prompt; the
  domain-summary-without-project-name interaction with the unmodified
  `replace_placeholders()` logic) and found no defect in either case.
- No boundary in the design agreement was crossed; no contract file was
  touched; the one incidental `.gitignore` addition (`__pycache__/`,
  `*.pyc`) is a minor, directly-related, non-contract-file fix this
  Reviewer session made itself while verifying the new Python test
  infrastructure, not a Reviewer finding against the Implementer's work.
