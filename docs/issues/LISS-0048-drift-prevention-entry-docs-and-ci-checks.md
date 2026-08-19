# LISS-0048: Drift-prevention entry documents and CI checks (item-0012 facet 5, scoped)

## Metadata

- Local issue ID: LISS-0048
- GitHub issue: none
- Status: ready
- Phase: docs-only (script change is deterministic tooling, no application
  architecture)
- Type: process
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: Design & Review group (Planner/Specifier) for design;
  Implementation group for file creation/edits.
- Related branch: process/drift-prevention-entry-docs-and-ci-checks

## Summary

- item-0012 facet 5 ("Prevent spec drift from stale documents") asks for
  two things: (A) Entry documents should show the Current/Historical
  distinction, canonical documents, a terminology migration table, the
  standard reading order, and which areas must not be entered from an old
  ADR directly; (B) five proposed deterministic CI checks (no retired
  terminology in current documents; no Archive document referenced from an
  Entry document; no more than one document claims "current" for the same
  theme; issue/work-plan status agreement — already exists,
  `check_issue_status_sync`, item-0009/WP-0007, not rebuilt; every
  Canonical document carries a source/evidence link).
- **This issue deliberately scopes down (B)** to the two checks that can
  be built and verified now without a prerequisite design decision: no
  retired terminology (new `docs/collaboration/terminology-migration.md` +
  `check_retired_terminology`), and no Archive-referenced-from-Entry
  (`check_no_archive_reference_from_entry`). The remaining two new checks
  — single-canonical-per-theme, and canonical-document-source-link — both
  need a "theme" registry concept this repository does not have yet, and
  are deferred (see Deferred Questions in the covering design agreement)
  rather than rushed.
- **Also resolves `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`**
  (the WP-0014 Reviewer's own tracked finding): adds `docs/archive/` to
  `scripts/check-contract-consistency.py`'s `RECORD_DIRS`, verified against
  a synthetic archived-file test case (created, exercised, then removed —
  this work plan does not itself create any real `docs/archive/` content,
  matching ADR 0020 Rule 7's "rules only" posture; retroactive application
  remains the later, separate work plan).
- (A) is delivered as a new section in `docs/architecture/agent-quickstart.md`
  (Entry-layer, not a `CLAUDE.md` mirror, per WP-0008's own established
  precedent for where new standing rules go to avoid mirror-sync burden).

## Acceptance Notes

- `docs/collaboration/terminology-migration.md` exists, documents its own
  schema, starts with zero rows (no retroactive backfill).
- `scripts/check-contract-consistency.py` gains `check_retired_terminology`
  and `check_no_archive_reference_from_entry`, both registered in `main()`
  and the module docstring's numbered check list (items 10 and 11), and
  `RECORD_DIRS` gains a `"docs/archive/"` entry.
- `docs/architecture/agent-quickstart.md` gains the "Document Currency and
  Canonical Reading" section, cross-referencing ADR 0020, the new
  terminology table, and `CLAUDE.md`'s own Reading Sequence — not
  duplicating any of them.
- `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` is
  triaged and closed once the `RECORD_DIRS` fix is verified against a
  synthetic case (outbound link from a mock archived file not flagged;
  inbound link from a current file to that mock archived path still
  resolves) — the synthetic case is removed before the final commit.
- `python3 scripts/check-contract-consistency.py` passes on the real repo
  tree (all new checks are no-ops against real content today — the
  terminology table is empty, no Entry document references
  `docs/archive/` yet — by design, per ADR 0020 Rule 7's "rules only, no
  retroactive application" posture carried into this facet too).
- Each new check function is also independently verified against a
  constructed synthetic failing case (per this repository's own
  established precedent, `docs/work-plans/WP-0007-document-consistency-drift-checks.md`'s
  Preflight: "verified in isolation: clean pass on HEAD, and a
  demonstrated failure against a constructed synthetic case per check"),
  with the actual command output pasted into the self-review — not merely
  asserted.
- No edit to `CLAUDE.md` or its four mirrors.
- AI work trace recorded — `docs/collaboration/terminology-migration.md`
  is an ADR-0006 contract file (`docs/collaboration/*.md`, not an
  excluded record directory).

## Review Finding Record

N/A — not itself a review-finding issue (though it resolves one,
LISS-0044).

## Dependencies

- Parent: none
- Depends on: none (does not depend on WP-0015/facet 4)
- Blocks: none directly, but the deferred single-canonical-per-theme and
  canonical-source-link checks remain open against facet 5's own full
  scope — see the covering design agreement's Deferred Questions.
- Related: `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
  `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` (resolved
  by this issue), `docs/work-plans/WP-0007-document-consistency-drift-checks.md`
  (verification-pattern precedent)

## Decisions Not Settled by the Design Agreement

- None — the covering design agreement's Settled Ambiguities and Deferred
  Questions sections resolve the scoping question (why B3/B5 are deferred)
  explicitly.

## Context

- Included: `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
  (facet 5 only), `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
  in full, `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` in
  full, `scripts/check-contract-consistency.py` in full (all ~1071 lines,
  read to confirm exact existing patterns: `RECORD_DIRS`'s one usage site,
  `read`/`read_optional`/`scanned_files`/`Failures.add` signatures, the
  module docstring's numbered list, `main()`'s registration order),
  `docs/work-plans/WP-0007-document-consistency-drift-checks.md` (the
  established verification-pattern precedent for adding new checks to
  this script).
- Omitted: item-0012 facets 4 and 6 (separate work plans); the later
  retroactive-application work plan's own scope (not designed here).
- Assumptions: none beyond what ADR 0020, item-0012, and LISS-0044 state
  directly.

## AI Planning Records

Required — planning size `M`. See below.

### AIP-0048-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI, Design & Review group standing
    session
  - Model as displayed: claude-sonnet-5
  - Reasoning setting as displayed: N/A (not surfaced to this session)
  - N/A reason: not surfaced by this harness
- Created at: 2026-08-19
- Planning size: M
- Intended execution route: Design & Review group authors the exact code
  for both new check functions, the `RECORD_DIRS`/docstring/`main()`
  edits, the new terminology-migration table file, and the
  agent-quickstart.md section, all specified verbatim in the design
  agreement; Implementation group transcribes and additionally performs
  the synthetic-case verification (create, exercise, capture output,
  remove) since that step requires actually running the script against a
  constructed case, not pure transcription; Design & Review group runs
  Preflight, then a separate-context Reviewer pass.
- Compatibility state: N/A (no dependency/version claim)
- Intended scope: one new contract file, one edited script (two new
  functions + three small edits), one edited Entry document (non-contract,
  non-mirror), plus closing LISS-0044. No existing repository document
  beyond `docs/architecture/agent-quickstart.md` and LISS-0044 itself is
  edited; no `docs/archive/` directory persists after this issue closes.
- Estimated token range: N/A — not tracked in this environment
- Estimated token midpoint: N/A
- Token metric: N/A
- Estimation basis: N/A — harness does not surface token counts
- Assumptions: the two new check functions' exact code is fully specified
  by this planning record's covering design agreement; the Implementation
  group's own judgment is needed only for running and capturing the
  synthetic-case verification output, not for designing the checks
  themselves.
- Confidence: high on the `RECORD_DIRS`/LISS-0044 fix (narrow, already
  diagnosed by the WP-0014 Reviewer, single-line-plus-verification);
  medium-high on the two new check functions (new code, but following an
  established, well-precedented pattern in the same file); explicitly
  deferred, not attempted at low confidence, on the two harder checks
  (single-canonical-per-theme, canonical-source-link) that would need a
  theme-registry design this issue does not invent.
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
- `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
- `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`
- `docs/work-plans/WP-0007-document-consistency-drift-checks.md`
- `scripts/check-contract-consistency.py`

## Work Notes

- 2026-08-19 — Design & Review group (Planner/Specifier): local issue,
  work plan (`WP-0016`), and design agreement drafted, with exact code
  for both new check functions, the terminology table, and the
  agent-quickstart.md section specified verbatim for the Implementation
  group to transcribe and verify.

## Verification

- `scripts/check-contract-consistency.py` — recorded in WP-0016's
  Preflight Validation section, both the real-tree clean run and each new
  check's isolated synthetic-case verification.
- Read-through diff confirming all changes match the design agreement's
  "Exact Content to Produce" verbatim, and that no other repository file
  changed.
- Work-plan-level Reviewer approval, separate context, per ADR 0006 (the
  new terminology-migration.md file is a contract file).
