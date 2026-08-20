# Feature: Interactive prompting in the collaboration-template copy script

`scripts/copy-ai-collaboration-files.sh` (first-time template adoption) is
flag-driven only today. This feature adds interactive prompting for
required/optional values that were not supplied as flags, mirroring the
interactive-terminal precedent already established in
`scripts/update-ai-collaboration-files.sh` (`is_interactive_tty()`, an
explicit stated default per prompt, and a `--non-interactive` override).
Flag-driven, non-interactive use is unchanged and still fully overrides or
skips every prompt.

## EARS

When `--target` is not supplied as a flag and the script is running with an
interactive terminal (stdin and stdout both TTYs, and `--non-interactive` was
not passed), the script shall prompt for the target repository directory and
re-prompt on an empty response, since no default value is possible for a
required path.

When `--project-name`, `--domain-summary`, or `--stack` is not supplied as a
flag and the script is running with an interactive terminal, the script
shall prompt for each missing value once, stating that the field is optional
and that an empty response skips placeholder replacement for that field.

If the script is not running with an interactive terminal (no TTY on stdin
or stdout, or `--non-interactive` was passed), the script shall skip all
prompting and preserve exactly today's flag-only behavior, including the
existing `--target is required.` error and exit code `2` when `--target` is
still unset after flag parsing.

If a value was supplied as a flag, the script shall not prompt for that
value, regardless of terminal interactivity.

While `--dry-run` is set, the script shall still prompt for any missing
value exactly as it would without `--dry-run` — the collected values simply
have no visible effect on the dry-run's printed plan, the same way passing
them as flags today already has no effect under `--dry-run` (`replace_placeholders`
already no-ops under `--dry-run`).

## Gherkin

```gherkin
Scenario: Prompt for the required target directory when omitted, interactively
  Given an interactive terminal (stdin and stdout are both TTYs)
  And no --target flag was supplied
  And --non-interactive was not passed
  When the script runs
  Then it prints a prompt asking for the target repository directory
  And it does not exit with the "--target is required." error

Scenario: Re-prompt when the target prompt receives an empty response
  Given an interactive terminal
  And the target prompt is showing
  When the operator presses Enter with no input
  Then the script prints that a target directory is required
  And it prompts again for the target repository directory

Scenario: Prompt for each missing optional value once, stating it is optional
  Given an interactive terminal
  And --target was supplied (as a flag or from the prior prompt)
  And --project-name, --domain-summary, and --stack were not supplied
  When the script reaches the point where it previously required these as
    flags
  Then it prompts once for the project name, stating the field is optional
  And it prompts once for the one-line domain summary, stating the field is
    optional
  And it prompts once for the stack, stating the field is optional

Scenario: Empty response to an optional prompt skips placeholder replacement
  Given an interactive terminal
  And the project name prompt is showing
  When the operator presses Enter with no input
  Then the script proceeds without treating the field as supplied
  And no placeholder replacement is attempted for that field, the same as
    when the matching flag is omitted entirely today

Scenario: A supplied flag is never prompted for
  Given --target, --project-name, --domain-summary, and --stack are all
    supplied as flags
  And an interactive terminal is present
  When the script runs
  Then no prompt is printed for any of the four values
  And the script's output is unchanged from today's flag-only run

Scenario: Non-interactive shell skips all prompting
  Given stdin or stdout is not a TTY (for example, the script's stdin is
    piped or redirected)
  And --target was not supplied
  When the script runs
  Then it does not print any prompt
  And it exits with the existing "--target is required." message and exit
    code 2, unchanged from today

Scenario: --non-interactive forces flag-only behavior even in a real terminal
  Given an interactive terminal (stdin and stdout are both TTYs)
  And --non-interactive was passed
  And --target was not supplied
  When the script runs
  Then it does not print any prompt
  And it exits with the existing "--target is required." message and exit
    code 2

Scenario: Prompts still fire under --dry-run
  Given an interactive terminal
  And --dry-run was passed
  And --target, --project-name, --domain-summary, or --stack were not
    supplied
  When the script runs
  Then it prompts for the missing values exactly as it would without
    --dry-run
  And the collected values have no visible effect on the dry-run's printed
    plan, matching today's behavior when those values are instead passed as
    flags under --dry-run

Scenario: --force and --dry-run stay flag-only, never prompted
  Given an interactive terminal
  And neither --force nor --dry-run was passed
  When the script runs
  Then the script never prompts for --force or --dry-run
  And both remain off by default, unchanged from today's flag-only behavior
```

## External Dependencies

- The controlling terminal's TTY state (`[ -t 0 ]`, `[ -t 1 ]`) — read only,
  no port needed; this mirrors `scripts/update-ai-collaboration-files.sh`'s
  own `is_interactive_tty()` helper exactly.
- Deterministic verification for this feature drives a real pseudo-terminal
  using Python's standard-library `pty` module (already available wherever
  `python3` is available, which this repository's tooling already requires
  for `scripts/check-contract-consistency.py`) — this is test-only
  infrastructure, not a new runtime dependency of the shipped script, which
  remains bash-only per the backlog item's stated constraint.

## Out of Scope

- Any change to `--force` or `--dry-run` becoming prompted values — both
  stay flag-only opt-ins (see the design agreement's Settled Ambiguities for
  the grounds).
- Re-validating a prompted `--target` path for existence before the
  script's single existing existence check — the prompt loop only rejects
  an *empty* response; an invalid-but-non-empty path still fails at the
  same existing "Target directory does not exist" check flag-driven use
  hits today, not a new re-prompt loop.
- Wording changes to `docs/collaboration/adoption-guide.md` — not required
  by the backlog item, and touching it would pull in ADR 0006 contract-file
  governance (trace + mandatory separate-context Reviewer pass) for a
  change this item does not ask for.
- Any change to `scripts/update-ai-collaboration-files.sh` itself — it is
  the precedent being mirrored, not a target of this change.

## Ambiguities

- None outstanding — the two judgment calls the backlog item left open
  (`--force`/`--dry-run` prompting; empty-optional-prompt-skips-replacement)
  are settled in the design agreement's Settled Ambiguities, with grounds
  recorded there.
