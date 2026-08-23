# LISS-0070: Cursor quickstart missing 3 bullets; Grok sentence omits Cursor

## Metadata

- Local issue ID: LISS-0070
- GitHub issue: none
- Status: done
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

`.cursor/rules/01-quickstart.mdc` is the only one of the five agent
mirrors (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
`.grok/rules/01-quickstart.md`, `.cursor/rules/01-quickstart.mdc`) missing
three cross-references the other four already carry in their own
reading-list section: "External resource adoption contract"
(`docs/architecture/external-resource-adoption-contract.md`), "AI failure
and recovery" (`docs/collaboration/ai-failure-recovery.md`), and "Slow AI
job runner CLI contract" (`docs/collaboration/runner-cli-contract.md`).
Confirmed by direct `grep -n` across all five files — see the covering
design agreement's "Settled Ambiguities" table for the exact line numbers
in the other four files.

Separately, `.grok/rules/01-quickstart.md` line 14's sentence "This
repository is prepared for multiple AI coding agents (Claude, Copilot,
Codex, Grok, etc.)" does not name Cursor, even though
`.cursor/rules/01-quickstart.mdc`'s own equivalent sentence (line 20-21)
already lists all five tools including itself. Cursor support was added
after Grok's mirror was written and this sentence was never backfilled.

## Acceptance Notes

1. In `.cursor/rules/01-quickstart.mdc`, find the "Cursor-side reminders
   that must stay visible with this rule set" bulleted list near the end
   of the file (currently 4 bullets: loop-settings.toml, tooling-setup
   prompt, findings/post-hoc-audit, spikes/backlog). Add three more
   bullets to that list:
   - `docs/architecture/external-resource-adoption-contract.md` (External
     resource adoption contract).
   - `docs/collaboration/ai-failure-recovery.md` (AI failure and
     recovery).
   - `docs/collaboration/runner-cli-contract.md` (Slow AI job runner CLI
     contract).
   Match the terse, one-line-per-bullet style already used by the
   existing four bullets in that section — do not restate full prose from
   `AGENTS.md`'s own equivalent entries (this section is explicitly a
   Cursor-specific complement, not a full restatement, per this file's
   own "Shared operating contract" section above it, and per
   `docs/collaboration/prompt-instruction-change-control.md`'s "Union"
   sync mode row for `.cursor/rules/*.mdc`).
2. In `.grok/rules/01-quickstart.md` line 14, change "(Claude, Copilot,
   Codex, Grok, etc.)" to name Cursor as well, and check whether the
   adjacent sentence (naming which files mirror which) also needs
   updating — `.cursor/rules/01-quickstart.mdc`'s own equivalent sentence
   (line 20-25) is the reference for what a fully backfilled version
   looks like. Do not change any other sentence in this file.

### Required reproduction (before and after)

1. `grep -n "external-resource-adoption-contract\|ai-failure-recovery\|runner-cli-contract" .cursor/rules/01-quickstart.mdc` —
   before: no matches (or matches only from an unrelated context); after:
   three matches, one per new bullet.
2. `grep -n "Claude, Copilot, Codex, Grok" .grok/rules/01-quickstart.md` —
   before: matches, without "Cursor"; after: either no match (sentence
   reworded) or a match that includes "Cursor".
3. Paste the full diff of both files (`git diff .cursor/rules/01-quickstart.mdc .grok/rules/01-quickstart.md`)
   and confirm no line outside the stated bullets/sentence changed.

## Dependencies

- Parent: `docs/work-plans/WP-0026-mirror-file-parity-gaps.md`
- Depends on: none
- Blocks: none
- Related: `docs/backlog/item-0022-mirror-file-parity-gaps.md`,
  `docs/collaboration/prompt-instruction-change-control.md`

## Decisions Not Settled by the Design Agreement

- None — scope is fully settled by
  `docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`.

## Context

- Included: `docs/backlog/item-0022-...md`'s full text; direct `grep`/read
  of all five quickstart mirror files' current content;
  `docs/collaboration/prompt-instruction-change-control.md`'s
  Per-Agent-Tool Rule Applicability Registry (Union sync mode for Cursor).
- Omitted: `.cursor/rules/02-architecture-boundaries.mdc` and
  `03-collaboration-and-completion.mdc` (not in scope for this issue).
- Assumptions: none — the exact bullet wording style and exact sentence
  location were independently confirmed by reading the current file
  content before writing this issue, not assumed from the backlog item's
  description alone.

## References

- `docs/backlog/item-0022-mirror-file-parity-gaps.md`
- `docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`
- `.cursor/rules/01-quickstart.mdc`
- `.grok/rules/01-quickstart.md`
- `docs/collaboration/prompt-instruction-change-control.md`

## Work Notes

- 2026-08-23 — Design & Review group (Planner/Specifier persona). Issue
  opened as part of WP-0026, scoped per the design agreement. Not yet
  dispatched. Independently confirmed via direct `grep`/read that gap 1's
  actual footprint (per the backlog item) was stale for 4 of 5 mirrors —
  only this file needs it — before writing this issue's acceptance notes.
- 2026-08-23 — Implementer persona. Applied both edits exactly as scoped.

  Phase/finding: Fast Path implementation.
  Command run and result (before):
  ```
  $ grep -n "external-resource-adoption-contract\|ai-failure-recovery\|runner-cli-contract" .cursor/rules/01-quickstart.mdc
  (no output — zero matches)
  $ grep -n "Claude, Copilot, Codex, Grok" .grok/rules/01-quickstart.md
  14:This repository is prepared for multiple AI coding agents (Claude, Copilot,
  ```
  Edits applied: added the 3 bullets to `.cursor/rules/01-quickstart.mdc`'s
  "Cursor-side reminders" section; reworded `.grok/rules/01-quickstart.md`
  line 14 to name Cursor and updated its adjacent mirror-list sentence
  (lines 16-18) to also name `.cursor/rules/*.mdc`, per the issue's own
  instruction to check that adjacent sentence.
  Command run and result (after):
  ```
  $ grep -n "external-resource-adoption-contract\|ai-failure-recovery\|runner-cli-contract" .cursor/rules/01-quickstart.mdc
  162:  `docs/architecture/external-resource-adoption-contract.md`.
  163:- AI failure and recovery: `docs/collaboration/ai-failure-recovery.md`.
  164:- Slow AI job runner CLI contract: `docs/collaboration/runner-cli-contract.md`.

  $ grep -n "Claude, Copilot, Codex, Grok" .grok/rules/01-quickstart.md
  (no output — sentence reworded, now reads "Grok, Cursor, etc.")
  ```
  `git diff` reviewed: confined to the 3 new bullet lines in
  `.cursor/rules/01-quickstart.mdc` and the two sentences (line 14's
  parenthetical, lines 16-18's mirror list) in `.grok/rules/01-quickstart.md`
  — no other line changed in either file.
  Risks considered: (1) the new bullets might duplicate `AGENTS.md` prose
  instead of staying terse — checked against the existing 4-bullet style,
  matched it (one line each, file name plus short label). (2) editing near
  the `.mdc` YAML frontmatter might corrupt it — the edit is far below the
  frontmatter (line ~158 of ~164), frontmatter untouched. (3) rewording the
  grok "mirror list" sentence might drift from `.cursor/rules/01-quickstart.mdc`'s
  own equivalent sentence shape — compared directly, wording now matches
  (both list `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  and the other tool's mirror-file glob).
  Why each does not occur: (1) verified by direct comparison of the new
  bullets' line length/style against the existing 4. (2) confirmed by
  `git diff` showing no change above line 158. (3) confirmed by side-by-side
  read of both files' equivalent sentences after the edit.

## Verification

- `grep -n` before/after showing the three new bullets present in
  `.cursor/rules/01-quickstart.mdc`.
- `grep -n` before/after showing Cursor now named in
  `.grok/rules/01-quickstart.md`'s sentence.
- `git diff` confined to the stated bullets/sentence in the two files.
