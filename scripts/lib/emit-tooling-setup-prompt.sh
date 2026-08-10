# shellcheck shell=bash
# Emit a paste-ready prompt that asks an AI agent to set up deterministic
# loop-engineering tools for a target repository. Sourced by init scripts.
#
# Requires: target (absolute path), optional language (ISO 639-1).

emit_tooling_setup_prompt() {
  local target="${1:?target required}"
  local language="${2:-en}"
  local detected=""
  local hints=""

  append_hint() {
    local label="$1"
    local path="$2"
    if [ -e "$target/$path" ]; then
      detected="${detected}${detected:+, }${label}"
      hints="${hints}
- Found \`${path}\` → consider ${label}-appropriate tools."
    fi
  }

  append_hint "Rust" "Cargo.toml"
  append_hint "Node/JS/TS" "package.json"
  append_hint "Python" "pyproject.toml"
  append_hint "Python" "requirements.txt"
  append_hint "Go" "go.mod"
  append_hint "Java/Kotlin (Maven)" "pom.xml"
  append_hint "Java/Kotlin (Gradle)" "build.gradle"
  append_hint "Java/Kotlin (Gradle)" "build.gradle.kts"
  append_hint "Swift" "Package.swift"
  append_hint "Ruby" "Gemfile"
  append_hint "PHP" "composer.json"
  append_hint "Dart/Flutter" "pubspec.yaml"
  if find "$target" -maxdepth 2 -name '*.sln' 2>/dev/null | grep -q .; then
    detected="${detected}${detected:+, }C#/.NET"
    hints="${hints}
- Found \`*.sln\` → consider .NET-appropriate tools."
  fi

  if [ -z "$detected" ]; then
    detected="none yet (stack not detected from common manifests)"
    hints="
- No common language manifest found at repo root. Infer stack from README,
  AGENTS.md placeholders, and directory layout — or stop and ask the Director
  which stack is intended before installing tools."
  fi

  local settings_note="docs/collaboration/loop-settings.toml missing — prefer free tools; write records in language \"${language}\"."
  if [ -f "$target/docs/collaboration/loop-settings.toml" ]; then
    local lang_from_file
    lang_from_file="$(
      awk -F'"' '/^language[[:space:]]*=/ { print $2; exit }' \
        "$target/docs/collaboration/loop-settings.toml" 2>/dev/null || true
    )"
    if [ -n "${lang_from_file:-}" ]; then
      language="$lang_from_file"
    fi
    settings_note="Read docs/collaboration/loop-settings.toml (docs.language=${language}). Honor [selection].prefer_zero_mandatory_spend and allow_internet_research."
  fi

  cat <<PROMPT
================================================================================
PASTE THE FOLLOWING INTO AN AI CODING AGENT (tooling setup)
================================================================================

You are setting up **deterministic quality and loop-engineering tools** for this
repository (not product features):

Repository: ${target}

## Context to read first

1. AGENTS.md (project name, stack placeholders, external resources).
2. docs/collaboration/loop-settings.toml and docs/collaboration/loop-settings.md
3. docs/architecture/dependency-policy.md
4. docs/architecture/testing-strategy.md
5. docs/architecture/project-structure.md
6. docs/collaboration/post-hoc-audit.md (verification output must be recordable)
7. docs/templates/examples/ (deny.toml, dependency-cruiser.config.cjs patterns)
8. Existing CI: .github/workflows/ci.yml

Settings note: ${settings_note}

## Detected stack signals (heuristic only — verify on disk)

Detected: ${detected}
${hints}

## Your task (Architecture Path / design-intake first)

Propose and, after a compact design note naming persona **Implementer** or
**Planner**, install only what this project actually needs for a closed AI
loop. Prefer **zero mandatory paid spend** when quality is acceptable; use
internet research against official docs; do not invent vendor claims.

### A. Language / formatter / linter / type checker

Match the real stack (examples — pick what fits, do not install all):

| Ecosystem | Typical free tools |
| --- | --- |
| Rust | rustfmt, clippy, cargo test |
| TypeScript/JS | eslint or biome, prettier or biome, tsc --noEmit |
| Python | ruff (lint+format), mypy or pyright, pytest |
| Go | gofmt, golangci-lint, go test |
| Other | equivalent maintained open tools |

Wire scripts or Makefile/just targets so one command runs the suite and prints
output suitable to paste into self-review / preflight records.

### B. Static analysis and architecture boundaries

- Import/boundary checker when multiple layers exist (e.g. dependency-cruiser,
  import-linter) — see docs/architecture/dependency-policy.md
- Package audit when a manifest exists (cargo-deny, npm audit, pip-audit,
  osv-scanner, …)
- Optional: secret scanning, license policy — only if justified

Copy patterns from docs/templates/examples/ when relevant; adapt, do not force
Rust/TS tools onto the wrong stack.

### C. Loop-engineering support (this template)

Ensure these remain usable and documented in
\`docs/architecture/tooling.md\` (update the stack-specific table; the
template-native section already ships):

- scripts/check-contract-consistency.py
- scripts/init-loop-settings.sh / scripts/init-llm-context.sh
- Preflight-friendly commands (list exact shell commands for CI and local)
- How agents should record command output (post-hoc audit)
- Spike/backlog locations: docs/spike/, docs/backlog/

### D. CI

Extend .github/workflows/ci.yml (or stack CI) so:

- formatter/linter/typecheck/tests run when the stack exists
- contract/template sanity checks from this collaboration template remain
- jobs that need a manifest are **conditional** until the project has that
  manifest (do not fail empty template-only repos without code)

### E. Cost and quality bar

- Default to free/open tools with good maintenance and docs
- If recommending a paid SaaS scanner, record fee model, why free options fail,
  and that Director approval is required before adoption
- Do not add speculative tools "for later"

## Deliverables

1. Compact design note (scope, stack detected, tools chosen, omitted tools).
2. Config files and CI changes on a dedicated branch if issue work applies;
   for bootstrap-only tooling with no feature issue, document the exception
   in the design note.
3. docs/architecture/tooling.md listing commands:
   - install/bootstrap
   - lint
   - typecheck / static analysis
   - test
   - contract check
   - full preflight bundle
4. Run each command once and paste deterministic output into the design note
   or a short trace under docs/collaboration/traces/.
5. Write narrative records in language **${language}** (field labels may stay
   English).

## Stop conditions

- Stack is ambiguous and AGENTS.md still has unfilled placeholders that block
  tool choice → reopening request / ask Director; do not guess a paid stack.
- A tool would change architecture boundaries or force a provider → ADR or
  design agreement, not silent install.
- You must not implement product domain features in this session.

When finished, summarize: tools added, commands for agents to run every phase,
and any follow-up spikes (docs/spike/case-NNNN-…) for undecided options.

================================================================================
END PROMPT
================================================================================
PROMPT
}
