# LISS-0043: Document and log lifecycle model (ADR 0020)

## Metadata

- Local issue ID: LISS-0043
- GitHub issue: none
- Status: ready
- Phase: docs-only
- Type: process
- Priority: high
- Initial planning size: L
- Current planning size: L
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: Design & Review group (Planner/Specifier) for design and
  ADR authorship; Implementation group for file creation/edits.
- Related branch: process/document-log-lifecycle-model

## Summary

- Create ADR 0020 (`docs/architecture/adr/0020-document-and-log-lifecycle-model.md`),
  covering facets 1-3 of `docs/backlog/item-0012-document-and-log-lifecycle-management.md`:
  the four-layer document model (Entry/Canonical/Evidence/Archive) adapted
  onto this template's existing five-artifact-type structure, a
  document-status vocabulary and consolidation trigger conditions, the
  archive mechanism (in-tree `docs/archive/` move, not `qpex`-style
  working-tree deletion), and the trace-lifecycle rule (one representative
  trace per topic).
- Create `docs/collaboration/restoration-ledger.md` (empty — header and
  schema only; no existing document is moved by this issue).
- Add a short, disambiguating cross-reference in
  `docs/collaboration/local-issue-planning.md`'s "Status Values" section,
  pointing to ADR 0020's own, separate document-lifecycle status
  vocabulary.
- Grounded in the required-first spike,
  `docs/spike/case-0001-document-log-lifecycle-management/case.md`
  (`Status: closed`, Selection: Option B — adapt `qpex`'s model, don't
  adopt its aggressive mechanics wholesale).

## Acceptance Notes

- ADR 0020 exists, Status: Accepted, covered by `DA-2026-08-19-06`, and
  contains, at minimum: the four-layer-to-five-artifact-type mapping
  (Rule 1), consolidation trigger conditions per artifact type (Rule 2),
  the archive mechanism (Rule 3), the trace-lifecycle rule (Rule 4), the
  restoration-ledger schema (Rule 5), the relationship to each type's own
  existing status field (Rule 6), and the explicit "rules only, no
  retroactive application in this work plan" scope boundary (Rule 7).
- `docs/collaboration/restoration-ledger.md` exists, documents its own
  schema and recovery command, and its Ledger table has no data rows (only
  the "no entries yet" placeholder).
- `docs/collaboration/local-issue-planning.md`'s Status Values section
  gains one short paragraph distinguishing issue lifecycle status from
  ADR 0020's document-lifecycle status vocabulary — no other part of that
  file changes.
- No existing repository document (`docs/issues/`, `docs/work-plans/`,
  `docs/collaboration/traces/`, `docs/collaboration/reviews/`,
  `docs/collaboration/agreements/`, other `docs/architecture/adr/` files)
  is moved, archived, deleted, or content-edited by this issue —
  retroactive application is explicitly out of scope, per the Director's
  own sequencing decision at item-0012's promotion.
- `scripts/check-contract-consistency.py` passes.
- AI work trace recorded under `docs/collaboration/traces/` — ADR 0020
  itself is not a `docs/collaboration/*.md` contract file (ADRs are not on
  ADR-0006's contract-file list, confirmed by the same check WP-0008 ran
  for `agent-quickstart.md`), but `docs/collaboration/local-issue-planning.md`
  is, so a trace is required for this issue regardless.

## Review Finding Record

N/A — not a review-finding issue.

## Dependencies

- Parent: none
- Depends on: `docs/spike/case-0001-document-log-lifecycle-management/case.md`
  (`Status: closed`) — satisfied.
- Blocks: the later, separate work plans for item-0012 facets 4
  (contract-sync diff record), 5 (drift-prevention entry documents and CI
  checks), and 6 (review-summary packets) all reference ADR 0020's
  vocabulary and are sequenced after this issue, per the spike's own
  "Decomposition and sequencing" table.
- Related: `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
  `docs/spike/case-0001-document-log-lifecycle-management/case.md`

## Decisions Not Settled by the Design Agreement

- None — the spike (case-0001) closed both questions item-0012's own
  Uncertainty section named (taxonomy mapping, restoration-ledger
  location/format); `DA-2026-08-19-06` carries those answers forward as
  settled.

## Context

- Included: `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
  `docs/spike/case-0001-document-log-lifecycle-management/case.md` in
  full, this template's own `docs/architecture/adr/` (19 files, titles
  only) and `docs/collaboration/` directory listing,
  `docs/collaboration/local-issue-planning.md`,
  `docs/collaboration/design-agreement.md`,
  `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  (as a style/structure precedent for this ADR).
- Omitted: the four external `qpex` files' full bodies beyond what the
  spike already extracted and cited — not re-read in full for this issue;
  the spike's own Research Log and Selection sections are the carried-forward
  record. This repository's own existing `docs/issues/`, `docs/work-plans/`,
  `docs/collaboration/traces/` file *contents* (only directory listings
  and counts were read) — full retroactive inventory is explicitly the
  later work plan's job, not this issue's.
- Assumptions: none beyond the spike's own recorded Selection and
  Settled Ambiguities.

## AI Planning Records

Required — planning size `L`. See below.

### AIP-0043-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI, Design & Review group standing
    session
  - Model as displayed: claude-sonnet-5
  - Reasoning setting as displayed: N/A (not surfaced to this session)
  - N/A reason: not surfaced by this harness
- Created at: 2026-08-19
- Planning size: L
- Intended execution route: Design & Review group authors the full ADR 0020
  text, the restoration-ledger file content, and the exact
  local-issue-planning.md cross-reference paragraph in the design
  agreement's Plan section (Specifier output, minimizing Implementer
  interpretation); Implementation group creates the three files/edits
  exactly as specified, in its own worktree/branch, with a required AI
  work trace (local-issue-planning.md is an ADR-0006 contract file);
  Design & Review group runs Preflight, then a separate-context Reviewer
  pass.
- Compatibility state: N/A (no dependency/version claim)
- Intended scope: one new ADR file, one new restoration-ledger file, one
  short cross-reference paragraph in an existing contract file, one trace
  file. No existing repository document moved or edited beyond the one
  named paragraph.
- Estimated token range: N/A — not tracked in this environment
- Estimated token midpoint: N/A
- Token metric: N/A
- Estimation basis: N/A — harness does not surface token counts to this
  session
- Assumptions: the ADR's own content (four-layer mapping, consolidation
  triggers, archive mechanism, trace-lifecycle rule, ledger schema) is
  fully specified by this planning record's covering design agreement,
  leaving the Implementation group only file-creation/transcription work,
  not independent design judgment — consistent with how WP-0013 handled
  its own two-file contract edit.
- Confidence: high that the taxonomy mapping and ledger design are sound
  (grounded directly in the spike's own comparison against this
  template's actual current state); medium on whether Rule 2's
  illustrative per-type triggers will need refinement once the later
  retroactive-application work plan actually applies them to real
  documents — explicitly flagged as a Consequences-section risk in ADR
  0020 itself, not hidden.
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
- `docs/spike/case-0001-document-log-lifecycle-management/case.md`
- `/Users/nn0cl/Documents/git/qpex/docs/work-plans/WP-0090-documentation-canonicalization.md`
  (external, read-only reference, cited via the spike)
- `/Users/nn0cl/Documents/git/qpex/docs/work-plans/WP-0091-decision-theme-canonicalization.md`
  (external, read-only reference, cited via the spike)
- `/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md`
  (external, read-only reference, cited via the spike)
- `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  (structure/style precedent)

## Work Notes

- 2026-08-19 — Design & Review group (Planner/Specifier): local issue,
  work plan (`WP-0014`), and design agreement
  (`docs/collaboration/agreements/2026-08-19-document-log-lifecycle-model.md`,
  `DA-2026-08-19-06`) drafted on the shared branch
  `process/backlog-item-0012-and-0013`, with the full ADR 0020 text,
  restoration-ledger content, and cross-reference paragraph specified
  verbatim in the design agreement's Plan section. Dispatched to the
  Implementation group on branch `process/document-log-lifecycle-model`.

## Verification

- `scripts/check-contract-consistency.py` — recorded in WP-0014's
  Preflight Validation section.
- Read-through diff confirming the three changes match the design
  agreement's Plan section verbatim (ADR content, ledger content,
  cross-reference paragraph) and that no other repository file changed.
- Work-plan-level Reviewer approval, separate context, per ADR 0006 (the
  contract-file edit requires this regardless of size; the ADR itself is
  reviewed in the same pass for substantive soundness even though it is
  not independently an ADR-0006 contract file).
