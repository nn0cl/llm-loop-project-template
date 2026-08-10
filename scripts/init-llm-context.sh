#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/init-llm-context.sh [TARGET_REPOSITORY]
  scripts/init-llm-context.sh [--tooling] [TARGET_REPOSITORY]

Prints a compact initial prompt for an LLM agent after this collaboration
template has been copied into a repository. The script does not call an LLM,
read secrets, or make project architecture decisions.

With --tooling, also print the paste-ready prompt that asks the agent to set
up linters, static analysis, and other loop-engineering tools for this stack
(same text as: scripts/init-loop-settings.sh --prompt-only).
USAGE
}

target="."
with_tooling=false

while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    --tooling)
      with_tooling=true
      shift
      ;;
    *)
      target="$1"
      shift
      ;;
  esac
done

if [ ! -d "$target" ]; then
  echo "Target directory does not exist: $target" >&2
  exit 1
fi

target="$(cd "$target" && pwd)"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

required_files=(
  "AGENTS.md"
  "CLAUDE.md"
  ".github/copilot-instructions.md"
  ".grok/rules/01-quickstart.md"
  ".grok/rules/02-architecture-boundaries.md"
  ".grok/rules/03-collaboration-and-completion.md"
  "docs/architecture/agent-quickstart.md"
  "docs/at-tdd/process.md"
  "docs/collaboration/ai-human-scheme.md"
  "docs/collaboration/personas.md"
  "docs/architecture/ai-request-routing.md"
  "docs/architecture/io-reasoning-contracts.md"
  "docs/architecture/implementation-readiness.md"
)

missing=false
for rel in "${required_files[@]}"; do
  if [ ! -f "$target/$rel" ]; then
    echo "Missing required file: $rel" >&2
    missing=true
  fi
done

if [ "$missing" = true ]; then
  echo "Install the template files before generating the LLM setup prompt." >&2
  exit 1
fi

settings_line="missing — run scripts/init-loop-settings.sh before design work"
if [ -f "$target/docs/collaboration/loop-settings.toml" ]; then
  lang="$(
    awk -F'"' '/^language[[:space:]]*=/ { print $2; exit }' \
      "$target/docs/collaboration/loop-settings.toml" 2>/dev/null || true
  )"
  if [ -n "${lang:-}" ]; then
    settings_line="present (docs.language=$lang)"
  else
    settings_line="present (read docs/collaboration/loop-settings.toml)"
  fi
fi

cat <<PROMPT
You are working in this repository:
$target

Loop settings: $settings_line
(see docs/collaboration/loop-settings.md, post-hoc-audit.md, findings-reuse.md)

Before implementing anything:
1. Read AGENTS.md.
2. Read docs/architecture/agent-quickstart.md.
3. Read docs/collaboration/loop-settings.toml if present; if missing, stop and
   ask the Director to run scripts/init-loop-settings.sh (choose docs language).
4. Write new collaboration record bodies in [docs].language from that file.
5. Select the smallest safe operating path:
   - Fast Path for mechanical, local, deterministic work.
   - Feature Path for AT-TDD Phase 1, 2, or 3 feature work.
   - Architecture Path for ADRs, process changes, prompt changes, privacy-sensitive routing, or boundary decisions.
6. Read only the documents required by that path.
7. Read docs/architecture/io-reasoning-contracts.md when AI or model output is involved.
8. Check docs/architecture/implementation-readiness.md before Phase 1, 2, or 3.
9. At design intake, list prior Type: review-finding issues that affect the area
   and how this work applies or honors them (findings must be applied, not noted).
10. Prefer post-hoc auditability: paste deterministic verification output; do not
    rely on chat memory for continuity.

Use a compact design note for Fast Path work. Use the full [DESIGN CHECK] scaffold
for Feature Path and Architecture Path work.
Execute only the phase named for the task in the plan under the covering design
agreement (docs/collaboration/agreements/). State the active persona; the
persona definitions are in docs/collaboration/personas.md. Issue no approval
without recorded deterministic verification output, and never approve work
produced by the same context. Reviewer decisions are recorded under
docs/collaboration/reviews/ using docs/templates/review-record.md.
Do not introduce target-project domain behavior, datastore choices, provider
choices, or stack-specific architecture unless an accepted specification or ADR
requires it.

If no covering design agreement, target specification, phase, or persona has
been provided yet, stop after design intake and return a reopening request
naming what is missing.

For later sessions and resume patterns, see
docs/collaboration/session-start-and-resume.md.

If deterministic tooling (linter, formatter, typechecker, import-boundary
checker, package audit, preflight command list) is not yet set up for this
project's stack, run or paste:
  scripts/init-loop-settings.sh --prompt-only
or re-run this script with --tooling.
PROMPT

if [ "$with_tooling" = true ]; then
  # shellcheck source=lib/emit-tooling-setup-prompt.sh
  source "$script_dir/lib/emit-tooling-setup-prompt.sh"
  lang="en"
  if [ -f "$target/docs/collaboration/loop-settings.toml" ]; then
    lang="$(
      awk -F'"' '/^language[[:space:]]*=/ { print $2; exit }' \
        "$target/docs/collaboration/loop-settings.toml" 2>/dev/null || true
    )"
    lang="${lang:-en}"
  fi
  echo ""
  emit_tooling_setup_prompt "$target" "$lang"
fi
