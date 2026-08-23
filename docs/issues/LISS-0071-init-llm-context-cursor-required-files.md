# LISS-0071: `init-llm-context.sh` does not check for Cursor mirror files

## Metadata

- Local issue ID: LISS-0071
- GitHub issue: none
- Status: ready
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: Fast Path
- Type: bug
- Priority: low
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0026-mirror-file-parity-gaps.md`)
- Related branch: process/promote-item-0022

## Summary

`scripts/init-llm-context.sh`'s `required_files` array (lines 48-62)
checks for `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
all three `.grok/rules/*.md` files, and several `docs/` files, but has no
entry for any `.cursor/rules/*.mdc` file. Confirmed by direct read of the
script. A repository missing its Cursor mirror entirely would not be
caught by this script's guard, unlike a repository missing its Grok
mirror (which would be caught).

## Acceptance Notes

Add exactly three entries to `required_files` in
`scripts/init-llm-context.sh`, immediately after the existing
`.grok/rules/*.md` block, matching that block's existing style:

```bash
required_files=(
  "AGENTS.md"
  "CLAUDE.md"
  ".github/copilot-instructions.md"
  ".grok/rules/01-quickstart.md"
  ".grok/rules/02-architecture-boundaries.md"
  ".grok/rules/03-collaboration-and-completion.md"
  ".cursor/rules/01-quickstart.mdc"
  ".cursor/rules/02-architecture-boundaries.mdc"
  ".cursor/rules/03-collaboration-and-completion.mdc"
  "docs/architecture/agent-quickstart.md"
  "docs/at-tdd/process.md"
  "docs/collaboration/ai-human-scheme.md"
  "docs/collaboration/personas.md"
  "docs/architecture/ai-request-routing.md"
  "docs/architecture/io-reasoning-contracts.md"
  "docs/architecture/implementation-readiness.md"
)
```

Do not change the check loop logic (lines 64-75) or anything else in the
script — this is a pure data addition to the existing array.

### Required reproduction (before and after)

1. Copy this repository to a throwaway target
   (`scripts/copy-ai-collaboration-files.sh --target <tmp> ...`, matching
   the invocation `.github/workflows/ci.yml`'s smoke-test step uses, or a
   plain `cp -r` of the tracked tree if simpler for this specific
   reproduction — either way, produce a target that has a real
   `.cursor/rules/` directory to start from).
2. Remove one `.cursor/rules/*.mdc` file from the throwaway target (for
   example, delete `.cursor/rules/02-architecture-boundaries.mdc`).
3. Run `scripts/init-llm-context.sh <tmp>` against the **pre-fix**
   script version. Paste the output — expected: it does *not* report the
   missing Cursor file (exits 0 as if the target were complete), since
   the pre-fix `required_files` array has no `.cursor` entry to check.
4. Apply the fix.
5. Re-run the same command against the same throwaway target (still
   missing the same file). Paste the output — expected: `Missing
   required file: .cursor/rules/02-architecture-boundaries.mdc` on
   stderr, and a non-zero exit code.
6. Restore the removed file (or use a fresh copy) and re-run
   `scripts/init-llm-context.sh <tmp>` once more — expected: succeeds
   (prints the normal prompt output), confirming the fix does not
   false-positive against a complete target.
7. Run `scripts/init-llm-context.sh .` (or equivalent, against this
   issue's own real worktree) to confirm no regression against the real,
   complete repository.

## Dependencies

- Parent: `docs/work-plans/WP-0026-mirror-file-parity-gaps.md`
- Depends on: none
- Blocks: none
- Related: `docs/backlog/item-0022-mirror-file-parity-gaps.md`,
  `scripts/init-llm-context.sh`

## Decisions Not Settled by the Design Agreement

- None — scope is fully settled by
  `docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`.

## Context

- Included: `docs/backlog/item-0022-...md`'s full text; direct read of
  `scripts/init-llm-context.sh`'s current `required_files` array and
  check loop.
- Omitted: the rest of the script (the tooling-prompt generation logic
  below the check loop) — unaffected, pure data addition.
- Assumptions: none — the exact array contents and insertion point were
  independently confirmed by reading the current script before writing
  this issue.

## References

- `docs/backlog/item-0022-mirror-file-parity-gaps.md`
- `docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`
- `scripts/init-llm-context.sh`

## Work Notes

- 2026-08-23 — Design & Review group (Planner/Specifier persona). Issue
  opened as part of WP-0026, scoped per the design agreement. Not yet
  dispatched. Independently confirmed via direct read that the gap is
  real and current before writing this issue.

## Verification

- Before-fix reproduction: script does not flag a missing
  `.cursor/rules/*.mdc` file (pasted, not summarized).
- After-fix: same reproduction now flags it correctly, with non-zero
  exit.
- Confirmed no false positive against a complete target.
- Confirmed no regression against the real repository.
