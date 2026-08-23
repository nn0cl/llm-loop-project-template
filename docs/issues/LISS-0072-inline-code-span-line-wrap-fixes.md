# LISS-0072: Inline code spans split across a Markdown line break

## Metadata

- Local issue ID: LISS-0072
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

Four docs each have one or more inline code spans (a
`` `docs/path/to/file.md` `` reference) whose backtick-delimited content is
split across a hard Markdown line break — e.g. `` `docs/architecture/adr/
``, with the rest of the path on the next line before the closing
backtick. This is cosmetic (renders fine in GitHub's own renderer;
`scripts/check-contract-consistency.py` does not flag it as a broken
reference), but can break rendering in Markdown renderers that do not
reflow inline code spans across newlines.

Independently re-verified (per the backlog item's own instruction to
re-check before fixing, not trust its list as-is) against current file
content. All four files it names still have the defect, totaling six
instances:

1. `docs/architecture/external-resource-adoption-contract.md:14-15` —
   `` `docs/architecture/adr/\n0002-input-output-reasoning-contracts.md` ``
2. `docs/architecture/external-resource-adoption-contract.md:106-107` —
   `` `docs/collaboration/\nmodel-tool-capability-matrix.md` ``
3. `docs/architecture/external-resource-adoption-contract.md:124-125` —
   `` `docs/collaboration/\nai-failure-recovery.md` ``
4. `docs/architecture/io-reasoning-contracts.md:25-26` —
   `` `docs/architecture/\nexternal-resource-adoption-contract.md` ``
5. `docs/collaboration/ai-failure-recovery.md:8-9` —
   `` `docs/collaboration/\nrunner-cli-contract.md` ``
6. `docs/collaboration/model-tool-capability-matrix.md:75-76` —
   `` `docs/architecture/adr/\n0010-ai-failure-recovery-and-runner-cli-contract.md` ``

No other file was searched for this defect beyond these four — per the
backlog item's own explicit boundary against letting this cosmetic fix
expand into a repository-wide Markdown-formatting pass.

## Acceptance Notes

For each of the six instances above, rewrap the surrounding paragraph so
the inline code span is not split by a hard line break — move the wrap
point to before the opening backtick (or after the closing one), keeping
the paragraph's prose wording and meaning completely unchanged. Do not
reflow lines elsewhere in the same file beyond what is needed to fix the
specific split span (avoid an unrelated whole-file rewrap that would
inflate the diff and make the Reviewer's job harder).

### Required reproduction (before and after)

For each of the four files, run:

```bash
grep -n '`[A-Za-z0-9/_.-]*/$' <file>
```

Before the fix: this returns the line(s) listed above (one per instance
in that file). After the fix: this returns no output for any of the four
files (confirms no split-code-span line-wrap remains at the specific
spots this issue found — this pattern is not a general Markdown linter,
so a clean result here means these six instances are fixed, not that the
file has no other unrelated formatting issue).

Also paste `git diff` for each of the four files and confirm every hunk
is a pure line-rewrap with identical rendered text (no wording added,
removed, or changed).

## Dependencies

- Parent: `docs/work-plans/WP-0026-mirror-file-parity-gaps.md`
- Depends on: none
- Blocks: none
- Related: `docs/backlog/item-0022-mirror-file-parity-gaps.md`

## Decisions Not Settled by the Design Agreement

- None — scope is fully settled by
  `docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`.

## Context

- Included: `docs/backlog/item-0022-...md`'s full text; direct `grep`/read
  of all six instances' full surrounding paragraph in each of the four
  files, confirming the exact split and the exact intended unsplit
  reading.
- Omitted: any other file in the repository — explicitly out of scope per
  the design agreement's Boundaries section.
- Assumptions: none — every instance was independently re-verified
  against current content before writing this issue; none were assumed
  present from the backlog item's list alone.

## References

- `docs/backlog/item-0022-mirror-file-parity-gaps.md`
- `docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`
- `docs/architecture/external-resource-adoption-contract.md`
- `docs/architecture/io-reasoning-contracts.md`
- `docs/collaboration/ai-failure-recovery.md`
- `docs/collaboration/model-tool-capability-matrix.md`

## Work Notes

- 2026-08-23 — Design & Review group (Planner/Specifier persona). Issue
  opened as part of WP-0026, scoped per the design agreement.
  Independently re-verified all six instances by reading each file's
  actual current content (not the backlog item's list alone) before
  writing this issue's acceptance notes; found the backlog item's file
  list still fully current, with no fifth file needing this fix and none
  of the four already fixed.

## Verification

- Before-fix `grep -n` output for all four files (pasted, showing the six
  instances).
- After-fix `grep -n` output for all four files, showing zero matches.
- `git diff` per file reviewed, confirming pure rewrap with unchanged
  wording.
