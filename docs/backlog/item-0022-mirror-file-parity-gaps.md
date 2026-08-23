# Backlog item: item-0022-mirror-file-parity-gaps

## Metadata

- Item ID: item-0022
- Title: Fix 5 remaining agent-instruction mirror-parity gaps (Cursor
  behind the other mirrors, missing cross-references)
- Status: captured
- Created: 2026-08-23
- Updated: 2026-08-23
- Priority hint: low
- Suggested planning size: S
- Owner/agent (optional): unassigned

## Summary

While investigating an old, never-merged branch
(`process/2026-07-13-cross-agent-contract-drift-fix`, since deleted — its
own file references pre-date this repository's "reset the repository's
record artifacts to the initial state" commit, `9fcb2d2`/PR #4, and are
themselves obsolete) the Backlog thread found 5 small, still-current
mirror-file parity gaps in the actual, current `main` content. None of
these were fixed by that old branch merging (it was not merged); they are
independently confirmed against today's files.

1. **"External resource adoption contract" cross-reference missing from
   every mirror's own reading list.**
   `docs/architecture/external-resource-adoption-contract.md` exists and
   is a real, current document, but none of `AGENTS.md`, `CLAUDE.md`,
   `.github/copilot-instructions.md`, `.grok/rules/01-quickstart.md`, or
   `.cursor/rules/01-quickstart.mdc` lists it in their own "Relevant
   architecture documents" / reading-sequence section, the way each
   already lists `docs/collaboration/ai-failure-recovery.md` and
   `docs/collaboration/runner-cli-contract.md`.
2. **`.cursor/rules/01-quickstart.mdc` is behind every other mirror.** It
   is missing all three of: the "AI failure and recovery" bullet, the
   "Slow AI job runner CLI contract" bullet, and (per point 1) the
   "External resource adoption contract" bullet — all three already
   present in `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
   and `.grok/rules/01-quickstart.md`. Confirmed via direct `grep` across
   all five mirror files.
3. **`.grok/rules/01-quickstart.md`'s own "prepared for multiple AI coding
   agents" sentence does not mention Cursor.** It names "Claude, Copilot,
   Codex, Grok, etc." but Cursor support (`.cursor/rules/*.mdc`) already
   exists in this repository (added after Grok's own mirror was written)
   and was never backfilled into this sentence, nor into the adjacent
   sentence listing which files must mirror which other files.
4. **`scripts/init-llm-context.sh`'s required-files check does not verify
   `.cursor/rules/*.mdc` files exist.** It checks for `AGENTS.md`,
   `.grok/rules/*.md`, and others, but has no entry for
   `.cursor/rules/01-quickstart.mdc`, `02-architecture-boundaries.mdc`, or
   `03-collaboration-and-completion.mdc` — so a repository missing its
   Cursor mirror entirely would not be caught by this script.
5. **A markdown line-wrap defect in a handful of docs** (at least
   `docs/architecture/external-resource-adoption-contract.md`,
   `docs/architecture/io-reasoning-contracts.md`,
   `docs/collaboration/ai-failure-recovery.md`,
   `docs/collaboration/model-tool-capability-matrix.md`) where an inline
   code span (a `` `docs/path/to/file.md` `` reference) is split across a
   line break in the raw Markdown source (e.g. `` `docs/architecture/adr/
   0002-....md` `` wrapping mid-span). This can break rendering in some
   Markdown renderers that do not reflow inline code spans across
   newlines. Cosmetic, not a broken reference (the checker does not flag
   these, and they render fine in GitHub's own renderer), but worth a
   pass since the old branch had already found and fixed each instance.

## Why it might matter

Cursor is a supported tool per this repository's own
`docs/architecture/ai-tool-support-status.md` (item-0021), and per
`docs/collaboration/prompt-instruction-change-control.md`'s own
ADR-0006 contract-file list, all of these are agent operating contract
files expected to mirror each other. A Cursor user of this template is
currently working from a mirror that is missing 3 real cross-references
the other four tools' mirrors already have, and the init script that is
supposed to catch a missing/incomplete mirror does not check Cursor's
files at all.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes — documentation-only
  edits and one script's required-files list, no new dependency.
- Boundaries or non-goals:
  - Do not merge or resurrect the old deleted branch
    (`process/2026-07-13-cross-agent-contract-drift-fix`) — its own
    issue/work-plan/trace file references are obsolete pre-reset
    numbering; re-derive each fix fresh against current `main` content
    instead.
  - Do not touch `docs/research/` or anything related to the separately
    -discussed rationale-essay branch (`docs/research-rationale-essays`,
    also deleted) — Director confirmed that content is preserved
    elsewhere (a sibling `llm-project-template` repository) and is
    out of scope here.
  - Item 5 (line-wrap) is genuinely cosmetic — do not let it expand scope
    into a broader Markdown-formatting pass across the whole repository;
    fix only the specific files/spans this item names, if any are still
    reproducible at execution time.

## Uncertainty

- [x] Spec can be written now — every gap is concretely named above with
      the exact files and exact missing content; each is a small,
      mechanical addition/correction, not a design question.
- [ ] Spike required first
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none — related:
  `docs/collaboration/prompt-instruction-change-control.md` (mirror-file
  contract list), `docs/architecture/ai-tool-support-status.md`
  (item-0021, Cursor's current support status)

## Promotion notes

Filled when status becomes `promoted` or `spiked` or `dropped`.

- Date:
- Decision:
- Reason:
