#!/usr/bin/env bash
# Create or refresh docs/collaboration/loop-settings.toml for an adopting
# (or template) repository, and print a paste-ready AI prompt to set up
# linters, static analysis, and other loop-engineering tools.
# Does not call network APIs or store secrets.
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  scripts/init-loop-settings.sh [options]

Create docs/collaboration/loop-settings.toml from the shipped template and
apply user choices (documentation language, etc.). By default, also print a
paste-ready prompt that asks an AI agent to set up project-appropriate
linters, static analysis, CI hooks, and loop-engineering tooling.

Options:
  --target DIR       Repository root (default: current directory)
  --language CODE    ISO 639-1 code for agent-written records (default: en)
                     Built-in: en, ja. Others allowed if agents can write them.
  --force            Overwrite an existing loop-settings.toml
  --dry-run          Print actions without writing
  --no-prompt        Do not print the tooling-setup AI prompt
  --prompt-only      Only print the tooling-setup prompt (no settings write)
  -h, --help         Show this help

Examples:
  scripts/init-loop-settings.sh
  scripts/init-loop-settings.sh --language ja
  scripts/init-loop-settings.sh --target ~/dev/my-app --language en --force
  scripts/init-loop-settings.sh --prompt-only
  scripts/init-loop-settings.sh --prompt-only | pbcopy   # macOS: copy prompt
USAGE
}

target="."
language="en"
force=false
dry_run=false
print_prompt=true
prompt_only=false

while [ $# -gt 0 ]; do
  case "$1" in
    --target)
      target="${2:-}"
      shift 2
      ;;
    --language)
      language="${2:-}"
      shift 2
      ;;
    --force)
      force=true
      shift
      ;;
    --dry-run)
      dry_run=true
      shift
      ;;
    --no-prompt)
      print_prompt=false
      shift
      ;;
    --prompt-only)
      prompt_only=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [ -z "$target" ] || [ ! -d "$target" ]; then
  echo "Target directory does not exist: $target" >&2
  exit 1
fi

target="$(cd "$target" && pwd)"

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
template_repo="$(cd "$script_dir/.." && pwd)"
# shellcheck source=lib/emit-tooling-setup-prompt.sh
source "$script_dir/lib/emit-tooling-setup-prompt.sh"

if [ "$prompt_only" = true ]; then
  if [ "$dry_run" = true ]; then
    echo "Dry run: would print tooling-setup prompt for $target (language=$language)."
    exit 0
  fi
  emit_tooling_setup_prompt "$target" "$language"
  exit 0
fi

template=""
for candidate in \
  "$target/docs/templates/loop-settings.toml" \
  "$template_repo/docs/templates/loop-settings.toml"
do
  if [ -f "$candidate" ]; then
    template="$candidate"
    break
  fi
done

if [ -z "$template" ]; then
  echo "Missing template: docs/templates/loop-settings.toml" >&2
  echo "Copy the collaboration template into the target first." >&2
  exit 1
fi

if ! printf '%s' "$language" | grep -Eq '^[a-z]{2}$'; then
  echo "Invalid --language '$language' (expected two-letter ISO 639-1, e.g. en, ja)." >&2
  exit 1
fi

case "$language" in
  en|ja) ;;
  *)
    echo "Note: language '$language' is not in the built-in set (en, ja)." >&2
    echo "Proceeding; ensure agents can write records in this language." >&2
    ;;
esac

dest_dir="$target/docs/collaboration"
dest="$dest_dir/loop-settings.toml"

if [ ! -d "$dest_dir" ]; then
  echo "Missing directory: docs/collaboration (is the template installed?)" >&2
  exit 1
fi

echo "Template: $template"
echo "Target:   $dest"
echo "Language: $language"

if [ -f "$dest" ] && [ "$force" != true ]; then
  if [ "$dry_run" = true ]; then
    echo "Dry run: would refuse write (file exists; need --force)."
    exit 0
  fi
  echo "Already exists: $dest" >&2
  echo "Re-run with --force to replace, or edit the file in place." >&2
  echo "To print the tooling-setup prompt only: $0 --prompt-only --target \"$target\"" >&2
  exit 1
fi

if [ "$dry_run" = true ]; then
  echo "Dry run: no file written."
  if [ "$print_prompt" = true ]; then
    echo "Dry run: would also print tooling-setup AI prompt."
  fi
  exit 0
fi

tmp="$(mktemp)"
awk -v lang="$language" '
  BEGIN { done = 0 }
  /^language[[:space:]]*=/ && done == 0 {
    print "language = \"" lang "\""
    done = 1
    next
  }
  { print }
  END {
    if (done == 0) {
      print "init-loop-settings: could not find language = in template" > "/dev/stderr"
      exit 1
    }
  }
' "$template" >"$tmp"

mv "$tmp" "$dest"

cat <<EOF

Created $dest

Agents will:
  - write new collaboration record bodies in language "$language"
  - keep post-hoc audit artifacts (traces, verification output)
  - apply review findings (must_apply) and reuse them at design intake

Next:
  - Review and edit flags under [audit], [findings], [selection] if needed
  - Paste the tooling-setup prompt below into an AI agent (or re-run with --prompt-only)
  - Optionally run scripts/init-llm-context.sh for the general first-session prompt
  - See docs/collaboration/loop-settings.md
EOF

if [ "$print_prompt" = true ]; then
  echo ""
  emit_tooling_setup_prompt "$target" "$language"
fi
