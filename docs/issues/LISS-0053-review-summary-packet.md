# LISS-0053: Review summary packet (item-0012 facet 6)

## Metadata

- Local issue ID: LISS-0053
- GitHub issue: none
- Status: ready
- Phase: docs-only
- Type: process
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: Design & Review group (Planner/Specifier) for design;
  Implementation group for file creation/edits.
- Related branch: process/review-summary-packet

## Summary

- item-0012 facet 6 ("Review records as summary packets") asks that the
  Reviewer's canonical review input be a small packet — `scope, current
  canonical documents, changed files, findings, disposition, remaining
  blockers, verification result, next approval required` — not every
  trace/self-review/issue file read in full, with detailed traces linked
  as evidence rather than used as the review's own entry point.
- Delivered as: a new "Review Summary Packet" section in
  `docs/templates/work-plan.md` (the exact 8 fields, in order), filled in
  once Preflight passes, before Reviewer submission; and a new "Review
  Summary Packet" section in `docs/collaboration/design-agreement.md`
  stating the rule and its relationship to the Reviewer's existing
  falsification/deterministic-precondition/context-separation
  constraints (the packet changes where review starts, not how
  rigorously it must search).
- This session's own prior Reviewer dispatches (WP-0013 through WP-0016)
  told each Reviewer to read the full work plan, issue, trace, and
  backlog item — exactly the pattern facet 6 exists to reduce. This issue
  does not retroactively redo those dispatches (out of scope, matching
  item-0012's own no-retroactive-application boundary); the new
  convention applies going forward, starting with this work plan's own
  future dispatches.

## Acceptance Notes

- `docs/templates/work-plan.md` gains a new "## Review Summary Packet"
  section, positioned between "Preflight Validation" and "Work-Plan
  Review," with exactly the 8 fields item-0012 names, in the order named.
- `docs/collaboration/design-agreement.md` gains a new "## Review Summary
  Packet" section, positioned between "Reopening the agreement" and
  "Closing a work plan," stating the rule and preserving the Reviewer's
  existing constraints explicitly.
- No new template file (`docs/templates/review-summary-packet.md`) is
  created — the packet is embedded as a section within the existing work
  plan document, matching this repository's own established convention
  (e.g., "AI Planning Records" is an embedded section, not a separate
  template file) rather than adding a redundant new file/location.
- No edit to `CLAUDE.md` or its four mirrors.
- `scripts/check-contract-consistency.py` passes.
- AI work trace recorded — both touched files are ADR-0006 contract
  files (`docs/templates/*.md`, `docs/collaboration/*.md`).

## Review Finding Record

N/A — not a review-finding issue.

## Dependencies

- Parent: none
- Depends on: none
- Blocks: none
- Related: `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
  `docs/templates/work-plan.md`, `docs/collaboration/design-agreement.md`

## Decisions Not Settled by the Design Agreement

- None — the covering design agreement's Settled Ambiguities section
  resolves the "separate template file or embedded section" question.

## Context

- Included: item-0012's facet 6 paragraph, `docs/templates/work-plan.md`
  in full, `docs/collaboration/design-agreement.md` in full, `CLAUDE.md`'s
  "Approval Model" section (for the "next approval required" field's four
  approval-type vocabulary).
- Omitted: facets 1-5 (separate, already-closed work plans); the
  retroactive-application work plan's own scope (not designed here).
- Assumptions: none beyond what item-0012 states directly.

## AI Planning Records

Not required — planning size `S`, first attempt.

## References

- `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
- `docs/templates/work-plan.md`
- `docs/collaboration/design-agreement.md`
- `docs/spike/case-0001-document-log-lifecycle-management/case.md`
  (its own "Decomposition and sequencing" table names this as the
  facet-6 work plan)

## Work Notes

- 2026-08-19 — Design & Review group (Planner/Specifier): local issue,
  work plan (`WP-0017`), and design agreement (`DA-2026-08-19-09`)
  drafted directly on `process/item-0012-remaining-facets`. Exact content
  for both files specified verbatim in the design agreement for the
  Implementation group to transcribe.
- 2026-08-19 — Implementer self-review (short form, planning size `S`),
  per `docs/templates/self-review.md`:

  ```markdown
  Phase / finding: Architecture Path, docs-only content transcription
    (Implementer, DA-2026-08-19-09 Tasks 1-2)
  Command run: python3 scripts/check-contract-consistency.py
  Result:
    contract consistency: all checks passed
  Risks considered:
    (a) transcribed content does not match "Exact Content to Produce"
      verbatim, or lands at the wrong insertion point, in either file.
    (b) some other part of either file was touched beyond the specified
      insertion.
    (c) the new design-agreement.md section weakens or is read as
      weakening the Reviewer's three existing constraints (context
      separation, deterministic precondition, falsification burden).
    (d) CLAUDE.md, a mirror file, or an already-closed work plan
      (WP-0013 through WP-0016) was touched.
  Why each does not occur:
    (a) `git diff -- docs/templates/work-plan.md
      docs/collaboration/design-agreement.md` was read through line by
      line against DA-2026-08-19-09's "File 1" and "File 2" blocks; both
      inserted sections match character for character, and each lands
      immediately after the exact paragraph named in the agreement
      ("...it never replaces the separate-context Reviewer." in
      work-plan.md; "...the agreement is reopened with the gap named."
      in design-agreement.md) and immediately before the exact next
      heading named (`## Work-Plan Review`; `## Closing a work plan`).
    (b) the same diff shows only one contiguous insertion hunk per file,
      with no other lines changed; `git status --porcelain` lists only
      `docs/collaboration/design-agreement.md` and
      `docs/templates/work-plan.md` as modified.
    (c) the new design-agreement.md section's own text was read back: it
      states explicitly "This does not weaken the Reviewer's own
      falsification burden or the deterministic-precondition/
      context-separation constraints in `CLAUDE.md`'s 'Constraints'" and
      that a Reviewer with doubt "still reads the underlying trace or
      issue file directly... independently re-run[s] a deterministic
      check rather than trust a pasted claim" — the packet changes only
      where review starts, not how rigorously it searches, matching
      DA-2026-08-19-09's Falsification Criteria.
    (d) `git status --porcelain` after both edits lists only the two
      target files (plus, once added, this trace/Work-Notes update and
      the new trace file) — `CLAUDE.md`, its mirrors, and
      `docs/work-plans/WP-0013*.md` through `WP-0016*.md` do not appear
      in the diff or status output at any point.
  ```

## Verification

- `scripts/check-contract-consistency.py` — recorded in WP-0017's
  Preflight Validation section.
- Read-through diff confirming both changes match the design agreement's
  "Exact Content to Produce" verbatim, and that no other repository file
  changed.
- Work-plan-level Reviewer approval, separate context, per ADR 0006.
