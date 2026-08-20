# Design Agreement: Interactive copy script

## Identity

- Agreement ID: DA-2026-08-20-01
- Date: 2026-08-20
- Director: sgry57 (Backlog-layer approval of
  `docs/backlog/item-0015-interactive-copy-script.md`, per ADR 0016 Rule 2 —
  see "Agreement" below for how this satisfies the Director's half)
- Planner / Specifier personas (model or tool used): Design & Review group,
  Claude Code (Claude Sonnet 5), this session
- Supersedes agreement (if any): none

## Direction

State the Director's framing, as recorded in
`docs/backlog/item-0015-interactive-copy-script.md`: make
`scripts/copy-ai-collaboration-files.sh` interactive — when required
information is not supplied as flags (at minimum `--target`; likely also
`--project-name`, `--domain-summary`, `--stack`), prompt for it instead of
requiring everything up front, the way `create-*`-style scaffolding tools
typically do. `scripts/update-ai-collaboration-files.sh` already has a
working precedent to mirror: interactive-terminal detection (`[ -t 0 ]`),
an explicit stated default when prompting, and a `--non-interactive` flag
to force non-interactive behavior even in a real terminal. Flags must still
fully work non-interactively and override prompts — this is additive only,
never a replacement for flag-driven use.

## Scope

- In scope: `scripts/copy-ai-collaboration-files.sh` (new
  `is_interactive_tty()` helper, new `--non-interactive` flag, prompting
  for `--target` — required, loops on empty input — and `--project-name`,
  `--domain-summary`, `--stack` — each optional, single prompt, empty
  response skips placeholder replacement for that field, exactly as an
  omitted flag does today); a new pty-based deterministic test file; one
  new CI step exercising it; the spec this agreement covers
  (`docs/specs/interactive-copy-script.feature.md`).
- Explicitly out of scope: any change to
  `scripts/update-ai-collaboration-files.sh` itself; any change to
  `docs/collaboration/adoption-guide.md`; `--force`/`--dry-run` becoming
  prompted values; re-validating a prompted `--target` path's existence
  beyond the script's single existing check.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Write failing pty-based tests for every scenario in `docs/specs/interactive-copy-script.feature.md` | Implementer | Phase 1 Red | Tests exist, are self-reviewed, and fail against the current (unmodified) script for the TTY-gated scenarios | `python3 scripts/tests/test_copy_ai_collaboration_files_interactive.py` (or equivalent invocation), output recorded |
| 2 | Implement `is_interactive_tty()`, `--non-interactive`, and the four prompts in `scripts/copy-ai-collaboration-files.sh`; update `usage()` | Implementer | Phase 2 Green | All tests from task 1 pass; the pre-existing "Check template copy smoke test" CI step still passes unmodified | Same test file, plus `bash -n scripts/copy-ai-collaboration-files.sh`, both outputs recorded |
| 3 | Add the new CI step; refactor for readability if warranted; state remaining verification gap | Implementer | Phase 3 Refactor | Behavior unchanged from Green; CI step added and syntactically valid; `python3 scripts/check-contract-consistency.py --repo .` still passes | CI step content pasted; contract-consistency output recorded |
| 4 | Preflight Validation over the whole work plan | Design & Review group (not the Implementer's own context) | Preflight | `pass` recorded with command output, scope result, next action | `docs/work-plans/WP-0018-interactive-copy-script.md`'s own Preflight Validation section |
| 5 | Work-plan-level Reviewer pass, including a real interactive run of the changed script (not only a diff read) | Reviewer (Design & Review group, separate context from the Implementer subagent) | Review | Approval or rejection recorded, naming the failure scenarios searched for | `docs/collaboration/reviews/` record |

Sequencing and dependencies:

- Task 1 must be self-reviewed (Red state) before task 2 starts. Task 2 must
  be self-reviewed (Green state) before task 3 starts. Task 3's Refactor
  self-review must be on file before task 4 (Preflight) runs. Task 4 must
  return `pass` before task 5 (Reviewer) begins. All of tasks 1-3 happen
  inside the Implementation group's own isolated worktree/branch,
  `process/interactive-copy-script`, merged into the shared branch
  `process/promote-item-0015` before task 4 runs.

## Specifications

Specification files this agreement covers:

- `docs/specs/interactive-copy-script.feature.md`

## Boundaries

- No change to Clean Architecture layering — this repository's own tooling
  scripts are process/meta-tooling, not the application stack the
  domain/application/ports/adapters split in
  `docs/architecture/project-structure.md` governs; that document is
  unaffected by this work plan.
- No new external dependency for the shipped script — it remains bash-only,
  per the backlog item's own stated constraint.
- No contract-file change (per ADR 0006) is authorized by this agreement.
  If implementation reveals that a contract file genuinely must change
  (for example, to document the new flag somewhere in
  `docs/collaboration/`), that is a reopening request against this
  agreement, not a judgment call to make unilaterally — `docs/collaboration/adoption-guide.md`
  was deliberately scoped out for exactly this reason (see spec's Out of
  Scope).
- python3's standard-library `pty` module may be used for test-only
  infrastructure (see Settled Ambiguities below); it must not become a
  runtime dependency of the shipped script itself.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Should `--force`/`--dry-run` get their own yes/no prompts, or stay flag-only opt-ins? | Stay flag-only. Grounds: both are already safe by default without a flag (existing files are skipped; nothing is copied). A yes/no prompt for a boolean that should almost always stay "no" adds a prompt cycle without addressing the item's actual friction point (an adopter not knowing the four *value* flags exist) — the item's own stated leaning, and this agreement agrees with its reasoning rather than overriding it. | Design & Review group (Planner), per item-0015's own recorded leaning |
| Should empty prompted input for `--project-name`/`--domain-summary`/`--stack` skip placeholder replacement? | Yes — empty prompted input is treated identically to an omitted flag: no placeholder replacement is attempted for that field. This preserves exactly today's optional-flag semantics and avoids a second, different "skip" convention existing only in interactive mode. | Design & Review group (Planner/Specifier) |
| Should prompts still fire when `--dry-run` is set, given `replace_placeholders` already no-ops under `--dry-run`? | Yes, unconditionally — special-casing "skip these three prompts under `--dry-run`" adds a second branch to reason about for a cosmetic gain (the answers are already inert under `--dry-run` today when passed as flags, so the same inertness under prompting is not a new inconsistency). Documented as an explicit spec scenario so it is tested behavior, not an undefined corner case. | Design & Review group (Planner) |
| Should a prompted `--target` path be re-validated for existence beyond the script's single existing check? | No — the prompt loop only rejects an *empty* response. An invalid-but-non-empty path still fails at the same existing "Target directory does not exist" check that flag-driven use hits today. Adding a re-prompt-on-invalid-path loop is real added complexity for a case flag-driven callers already tolerate as a hard failure. | Design & Review group (Planner) |
| Is python3's `pty` module an acceptable test-only tool, given the item's "bash-only, no new dependency" constraint? | Yes — that constraint governs the *shipped script*, which stays bash-only with no new runtime dependency. `python3` is already a required tool in this repository's own toolchain (`scripts/check-contract-consistency.py`, invoked directly by CI); using its standard library for test-only pty driving introduces no new environment requirement. Confirmed by directly smoke-testing `pty.fork()` in this session before writing this plan. | Design & Review group (Planner) |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should `docs/collaboration/adoption-guide.md` gain a line noting the copy script can now prompt interactively? | Deferred to a future backlog item or Minor Fix Path pass, if the Director or a later reader finds the omission confusing in practice. Not required by item-0015's own stated scope, and out of scope here specifically to avoid pulling in ADR 0006 contract-file governance for an unrequested change. |

## Verification

- `bash -n scripts/copy-ai-collaboration-files.sh`.
- The new pty-based Python test file covering every Gherkin scenario in
  `docs/specs/interactive-copy-script.feature.md`.
- The pre-existing "Check template copy smoke test" CI step, unmodified,
  still passing.
- `python3 scripts/check-contract-consistency.py --repo .`.
- A real, manual interactive run of the changed script by the Reviewer
  (separate context from the Implementer), confirming prompt behavior
  first-hand rather than from a diff read alone.

## Falsification Criteria

This design would be shown wrong if any of the following is observed:

- A flag-driven invocation (all four values supplied as flags) prompts for
  anything, in any terminal state — this would mean the change is not
  purely additive.
- A non-interactive invocation (no TTY, or `--non-interactive` passed)
  ever blocks waiting on stdin — this would mean a scripted/CI caller could
  hang, which the item explicitly rules out.
- The existing "Check template copy smoke test" CI step starts failing
  after this change — this would mean backward compatibility was broken.
- The pty-based tests pass but a real manual interactive run (Reviewer
  pass) shows different behavior — this would mean the tests do not
  actually reflect real terminal behavior, and Preflight's `pass` result
  would not be trustworthy evidence.

## Agreement

- [x] **Director**: this plan and this specification describe what I want
      built, and the stated boundaries are the right ones. Basis: the
      Director's approval of `docs/backlog/item-0015-interactive-copy-script.md`
      (`Status: promoted`, "Promotion notes" section, 2026-08-20), per ADR
      0016 Rule 2's backlog-item-level agreement — this work plan does not
      go beyond what that backlog item states.
- [x] **AI**: this plan and this specification are executable without
      further interpretation. Nothing in them requires guessing at a rule
      that was never stated — every prompt's trigger condition, wording
      requirement, and fallback behavior is pinned down in
      `docs/specs/interactive-copy-script.feature.md`, and both judgment
      calls the backlog item left open are settled above with grounds.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
