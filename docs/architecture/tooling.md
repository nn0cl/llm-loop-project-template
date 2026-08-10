# Tooling

Deterministic tools that support the closed AI loop. Agents paste command
output into self-review, preflight, and review records
(`docs/collaboration/post-hoc-audit.md`).

Bootstrap: run `scripts/init-loop-settings.sh` and paste its tooling-setup
prompt into an agent so this file is filled for the project's real stack.
Until then, only template-native checks apply.

## Template-native (always)

| Purpose | Command |
| --- | --- |
| Contract mirror / reference consistency | `python3 scripts/check-contract-consistency.py --repo .` |
| Create loop settings | `scripts/init-loop-settings.sh --language <en\|ja>` |
| Reprint tooling-setup AI prompt | `scripts/init-loop-settings.sh --prompt-only` |
| First-session agent prompt | `scripts/init-llm-context.sh .` |
| First-session + tooling prompt | `scripts/init-llm-context.sh --tooling .` |

## Stack-specific (fill after init)

Replace with the project's formatter, linter, type checker, tests, import
boundary checker, and package audit. Prefer zero mandatory paid spend when
quality allows. See `docs/architecture/dependency-policy.md` and
`docs/templates/examples/`.

| Purpose | Command | Notes |
| --- | --- | --- |
| Format | _TBD_ | |
| Lint | _TBD_ | |
| Typecheck / static analysis | _TBD_ | |
| Unit / acceptance tests | _TBD_ | |
| Import / architecture boundary | _TBD_ | |
| Package audit | _TBD_ | |
| Full preflight bundle | _TBD_ | single entry preferred |

## CI

List which of the above run in `.github/workflows/ci.yml` (or stack CI) and
which jobs are conditional on a language manifest.
