# LISS-0069: Add Antigravity to the contract-file list and Per-Agent-Tool Rule Applicability Registry

## Metadata

- Local issue ID: LISS-0069
- GitHub issue: none
- Status: ready
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: Architecture Path
- Type: architecture
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A — first attempt. `M` because it edits an
  agent operating contract file (ADR 0006 governance: separate-context
  Reviewer plus mandatory AI work trace) even though the actual content
  is narrowly scoped and fully specified below.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0025-ai-tool-support-status-survey.md`)
- Related branch: process/item-0021-status-survey (this issue's own
  execution branch is created off it, per the work plan)

## Summary

`docs/spike/case-0004-ai-tool-support-status-survey/case.md` found
Antigravity reads `AGENTS.md` natively (confirmed via
`ai.google.dev/gemini-api/docs/antigravity-agent`, a Google-official
domain) — the same file this repository already maintains as its
cross-tool canonical source, the same situation Codex is already in.
`docs/collaboration/prompt-instruction-change-control.md`'s own "Agent
Operating Contract Files" list and "Per-Agent-Tool Rule Applicability
Registry" table do not currently name Antigravity at all. This issue adds
it, stated explicitly rather than left implicit — matching this
repository's own discipline of never leaving a tool's support status to
be inferred.

## Acceptance Notes

### Before editing: independently re-verify the status report's own key citations

This issue's own scope includes a genuine, separate-context fact-check —
do not treat `docs/architecture/ai-tool-support-status.md` and
`docs/spike/case-0004-.../case.md` as already-verified just because they
were produced by the Design & Review group. Re-fetch at least these two
URLs directly and confirm the quotes match:

1. `https://ai.google.dev/gemini-api/docs/antigravity-agent` — confirm it
   states Antigravity reads `AGENTS.md` for project instructions.
2. `https://antigravity.google/docs/subagents/` — confirm the "maximum
   nesting depth of 10 levels" claim and the "peer agents whose ID is
   known" quote.

If either does not match what the status report or spike case claims,
STOP and report the discrepancy — do not silently correct the document
yourself or proceed as if the mismatch does not matter.

### The edit itself

In `docs/collaboration/prompt-instruction-change-control.md`:

1. Add a new bullet to the "Agent Operating Contract Files" list (after
   the existing `docs/templates/*.md` bullet, or wherever reads most
   naturally — this file's own convention, not a fixed position):

   ```markdown
   - `AGENTS.md` is also read natively by Codex CLI and by Google
     Antigravity (confirmed via primary source,
     `docs/spike/case-0004-ai-tool-support-status-survey/case.md`) —
     neither needs its own dedicated mirror file for this reason.
   ```

2. Add a new row to the "Per-Agent-Tool Rule Applicability Registry"
   table:

   ```markdown
   | Canonical source (also read directly, no mirror needed) | Codex CLI, Google Antigravity | Both tools read `AGENTS.md` natively — confirmed via primary source for Antigravity in `docs/spike/case-0004-ai-tool-support-status-survey/case.md`; no `.antigravity/` or equivalent mirror file exists or is needed for this reason. |
   ```

   Place it in the existing table, after the existing `Canonical source`
   row for `AGENTS.md` itself (or merge into that same row if that reads
   more naturally as a table edit — either is acceptable, state which was
   chosen in this issue's own Work Notes).

Do not touch any other row, bullet, or section of this file.

### Mandatory AI work trace

Create
`docs/collaboration/traces/2026-08-20-ai-tool-support-status-survey.md`
using `docs/templates/ai-work-trace.md`. State: which contract file
changed (`prompt-instruction-change-control.md`), why (Antigravity's own
confirmed `AGENTS.md`-native status, found by `case-0004`'s survey, was
previously undocumented), and what agent behavior is expected to change
(a future session working with Antigravity now has an explicit,
documented answer that no dedicated mirror file is needed for it, instead
of the gap being silently absent).

## Dependencies

- Parent: `docs/work-plans/WP-0025-ai-tool-support-status-survey.md`
- Depends on: `docs/spike/case-0004-ai-tool-support-status-survey/case.md`
  (`Status: closed`)
- Blocks: none
- Related: `docs/architecture/ai-tool-support-status.md`,
  `docs/backlog/item-0021-ai-tool-support-status-survey.md`

## Decisions Not Settled by the Design Agreement

- None — fully settled by
  `docs/collaboration/agreements/2026-08-20-ai-tool-support-status-survey.md`
  (`DA-2026-08-20-08`).

## Context

- Included: `docs/spike/case-0004-...md`'s full research log,
  `docs/architecture/ai-tool-support-status.md`'s full text,
  `docs/collaboration/prompt-instruction-change-control.md`'s current
  "Agent Operating Contract Files" and "Per-Agent-Tool Rule Applicability
  Registry" sections.
- Omitted: nothing else — this is a narrow, fully-specified addition.
- Assumptions: none — the exact text to insert is given verbatim above;
  the independent re-verification step is a genuine check, not a
  formality.

## References

- `docs/spike/case-0004-ai-tool-support-status-survey/case.md`
- `docs/architecture/ai-tool-support-status.md`
- `docs/collaboration/prompt-instruction-change-control.md`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0025, scoped per the design agreement. Not yet dispatched.

## Verification

- Independent re-fetch of the two named URLs, confirming the quotes
  match.
- `python3 scripts/check-contract-consistency.py` — no regression.
- `git diff` confined to
  `docs/collaboration/prompt-instruction-change-control.md`, the new
  trace file, and this issue's/work plan's own tracking files.
