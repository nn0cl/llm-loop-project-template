# Loop Settings

Target-owned collaboration settings live at:

```text
docs/collaboration/loop-settings.toml
```

Create or refresh that file with:

```bash
scripts/init-loop-settings.sh
scripts/init-loop-settings.sh --language ja
scripts/init-loop-settings.sh --target /path/to/repo --language en --force
```

After writing settings, the script **prints a paste-ready AI prompt** that
asks an agent to set up project-appropriate linters, formatters, type
checkers, static/boundary analysis, package audit, CI hooks, and a
`docs/architecture/tooling.md` command list. Options:

```bash
scripts/init-loop-settings.sh --no-prompt          # settings only
scripts/init-loop-settings.sh --prompt-only        # tooling prompt only
scripts/init-llm-context.sh --tooling              # first-session + tooling
```

The blank form is `docs/templates/loop-settings.toml`. The live file is
**not** overwritten by `scripts/update-ai-collaboration-files.sh` (it is
target history, like local issues). Re-run the init script with `--force`
only when you intend to replace local choices.

## Who reads it

Every agent session, before design intake or implementation:

1. Read `docs/collaboration/loop-settings.toml` if present.
2. If missing, run or ask the Director to run `scripts/init-loop-settings.sh`,
   then continue. Do not invent a language or audit policy silently.
3. Honor `[docs].language`, `[audit]`, `[findings]`, and `[selection]`.

## Sections

### `[docs].language`

Language for **new** collaboration records produced by agents (narratives in
traces, design notes, self-reviews, handoffs, review records, spike cases,
backlog items, issue summaries).

| Value | Meaning |
| --- | --- |
| `en` | English body text |
| `ja` | Japanese body text |
| other ISO 639-1 | Allowed when agents can write that language reliably |

Field labels in templates may stay English for grep stability. Body prose
follows this setting. Shipped dual files such as `README.md` / `README.ja.md`
are distribution docs, not a substitute for this setting.

### `[audit]`

The Director is often absent inside the work plan. Later humans and agents
must reconstruct what happened from the repository alone. See
`docs/collaboration/post-hoc-audit.md`.

### `[findings]`

Review findings must be applied or explicitly declined with grounds. See
`docs/collaboration/findings-reuse.md`.

### `[selection]`

Spike and dependency selection posture (prefer zero mandatory spend when
quality allows; internet research allowed). See `docs/spike/README.md`.
