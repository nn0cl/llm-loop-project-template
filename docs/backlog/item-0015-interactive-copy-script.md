# Backlog item: item-0015-interactive-copy-script

## Metadata

- Item ID: item-0015
- Title: Make `scripts/copy-ai-collaboration-files.sh` interactive
- Status: promoted
- Created: 2026-08-20
- Updated: 2026-08-20
- Priority hint: medium
- Suggested planning size: M
- Owner/agent (optional): unassigned

## Summary

`scripts/copy-ai-collaboration-files.sh` (first-time template adoption into
a new/existing repository) is entirely flag-driven today: `--target`,
`--project-name`, `--domain-summary`, `--stack`, `--force`, `--dry-run` — a
new adopter must know every relevant flag up front, with no prompting.
`scripts/update-ai-collaboration-files.sh` (pulling later template updates
into an already-adopted repo) already has a partial interactive precedent:
when a file was deleted locally but changed again upstream, it asks
whether to restore it (default: restore) when run with an interactive
terminal, falling back to the default under `--non-interactive` or a
non-interactive shell.

Director request: make the copy script interactive too — when required
information isn't supplied as flags (at minimum `--target`; likely also
`--project-name`, `--domain-summary`, `--stack`), prompt for it instead of
requiring it all up front, the way `create-*`-style scaffolding tools
typically do. Flags should still work non-interactively for scripted/CI use
(mirroring `update-ai-collaboration-files.sh`'s own `--non-interactive`
pattern) — this is additive, not a replacement for flag-driven use.

## Why it might matter

Lowers the barrier for a new adopter's very first run, which is the
highest-friction point in onboarding a new project onto this template
(`docs/collaboration/adoption-guide.md` already exists to soften this, but
a script that walks someone through the same choices interactively removes
a step).

## Known constraints

- Free / zero-mandatory-spend preference applies: yes — bash-only, no new
  dependency.
- Boundaries or non-goals:
  - Do not remove or change existing flag-driven behavior — flags must
    still fully override/skip prompts (a CI or scripted caller should never
    be blocked waiting on stdin). Detect a non-interactive shell
    (`[ -t 0 ]`, mirroring how `update-ai-collaboration-files.sh` already
    does this) and skip prompting automatically in that case, same as the
    existing script's own convention.
  - `--force` and `--dry-run` are booleans, not values needing a prompted
    string — decide whether these should also get a yes/no prompt, or stay
    flag-only opt-ins (leaning toward flag-only, since defaulting them
    interactively risks surprising overwrite behavior; Design & Review's
    call).
  - Consider whether `--project-name`/`--domain-summary`/`--stack` should
    have empty-input-skips-placeholder-replacement behavior when prompted
    (an adopter may not have decided the stack yet), consistent with how
    these are already optional flags today.

## Uncertainty

- [x] Spec can be written now — the existing `update-ai-collaboration-files.sh`
      prompt pattern (interactive-terminal detection, explicit default,
      `--non-interactive` override) is a concrete precedent to mirror.
- [ ] Spike required first
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none — related: `scripts/copy-ai-collaboration-files.sh`,
  `scripts/update-ai-collaboration-files.sh` (interactive-prompt
  precedent), `docs/collaboration/adoption-guide.md`

## Promotion notes

- Date: 2026-08-20
- Decision: Promoted, in the Backlog-layer thread ("承認"). Per ADR 0016
  Rule 2, Design & Review proceeds autonomously from here.
- Reason: Well-specified, concrete precedent already exists in this repo
  to mirror; ready to run.
