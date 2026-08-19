# Work Plan: Document and Log Lifecycle Model

## Goal

- Produce ADR 0020, an empty restoration ledger, and a small disambiguating
  cross-reference edit, closing facets 1-3 of
  `docs/backlog/item-0012-document-and-log-lifecycle-management.md`
  (four-layer document model, status vocabulary and consolidation
  conditions, trace lifecycle), per
  `docs/spike/case-0001-document-log-lifecycle-management/case.md`
  (Status: closed, Selection: Option B) and
  `docs/collaboration/agreements/2026-08-19-document-log-lifecycle-model.md`
  (`DA-2026-08-19-06`).

## Scope

- In: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
  (new), `docs/collaboration/restoration-ledger.md` (new, empty),
  `docs/collaboration/local-issue-planning.md` (one short cross-reference
  paragraph added to its "Status Values" section), `README.md`/
  `QUICKSTART.md`/`QUICKSTART.ja.md`'s ADR-range statements (0019 -> 0020;
  addendum added after `check_adr_range` correctly failed on the first
  Implementation attempt — routine maintenance any new ADR requires, not
  retroactive application of item-0012's own rules), the required AI work
  trace (`local-issue-planning.md` is an ADR-0006 contract file),
  self-review, Preflight, work-plan-level Reviewer pass.
- Out: any move, archive, deletion, or content edit of an existing
  `docs/issues/`, `docs/work-plans/`, `docs/collaboration/traces/`,
  `docs/collaboration/reviews/`, `docs/collaboration/agreements/`, or
  other `docs/architecture/adr/` file — retroactive application is a
  separate, later work plan, per the Director's own sequencing decision
  at item-0012's promotion. Facets 4 (contract-sync diff record), 5
  (drift-prevention entry documents and CI checks), and 6
  (review-summary packets) — sequenced as later, separate work plans per
  the spike's own decomposition table. Any edit to `CLAUDE.md` or its four
  mirrors (ADR 0020 is self-contained, following the ADR 0018 precedent
  of no companion policy doc or required-reading-list entry; confirmed by
  grep that no mirror file references ADR numbers directly).

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0043 | done | L | L | AIP-0043-001 | case-0001 (closed) | later item-0012 facet-4/5/6 work plans | process/document-log-lifecycle-model |

## Plan-Owned Bug Records

None.

## AI Planning Records

See LISS-0043's own AIP-0043-001 (required, planning size `L`).

## Recommended Order

1. LISS-0043 (single issue).

## Current Next Issue

- Issue: LISS-0043
- Reason it is unblocked: its one dependency (spike case-0001) is closed;
  `DA-2026-08-19-06` covers it fully, including the exact ADR text,
  ledger content, and cross-reference paragraph.
- Reopening request needed: no.

## Minor Fix Path

Does not apply — this is Architecture Path work (a new ADR), not a minor
fix or review-finding correction. Full design-agreement + work-plan +
Reviewer-pass cycle applies, matching ADR 0016/0018/0019's own precedent
for how this repository lands a new ADR.

## Preflight Validation

- Result: `pass`
- Checks and command output:

  ```console
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed
  ```

  Exit code: 0. First Preflight attempt (recorded, not silently discarded,
  per Invariant 2) correctly `fail`ed with 9 findings: a false-positive-
  triggering bare-filename citation of an external `qpex` file in ADR
  0020's own Rule 4, plus 8 stale `check_adr_range` findings across
  `README.md`/`QUICKSTART.md`/`QUICKSTART.ja.md` (not updated for the new
  ADR 0020 on the first Implementation pass). `DA-2026-08-19-06` and
  WP-0014 were amended with the exact corrections (see their own Scope
  "Addendum" and "Exact Content to Produce" -> "File 4"), sent back to the
  same Implementation-group session, and re-applied (commit `1d177d2`).
  This second, independently re-run check (above) is against the merged
  result, not copied from either the Implementer's or any other party's
  report — fetched the Implementer's actual branch directly from its own
  worktree, diffed it against the corrected agreement text (matched
  exactly), and ran the check in this session's own worktree before
  merging.
- Scope result: `git diff 0a38d6c..HEAD --stat` (`0a38d6c` is WP-0014's own
  design-intake commit, before any Implementation work) shows exactly the
  expected 10 files: the two new docs (ADR 0020, restoration ledger), the
  one edited contract file (`local-issue-planning.md`), the three
  ADR-range-maintenance files (`README.md`, `QUICKSTART.md`,
  `QUICKSTART.ja.md`), the new trace file, LISS-0043's Work Notes
  addition, and the design-agreement/work-plan correction commits
  themselves. No existing `docs/issues/`, `docs/work-plans/`,
  `docs/collaboration/traces/`, `docs/collaboration/reviews/`,
  `docs/collaboration/agreements/`, or other `docs/architecture/adr/` file
  was moved, archived, deleted, or edited. No `CLAUDE.md`/mirror file
  touched. No open `Type: review-finding` issue affects this area (all
  `docs/issues/LISS-*.md` `Status` fields checked; none `proposed` or
  `in_progress`).
- Next action: submit to the Design & Review group's work-plan-level
  Reviewer pass, in a context separate from both the Planner/Specifier
  context that wrote the design agreement/ADR text and the Implementer
  context that transcribed and corrected it.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-19-wp-0014-document-log-lifecycle-model-review.md`
— **Approved**, separate-context Reviewer session, all three constraints
satisfied. 16 failure scenarios searched (10 mechanical, 6 substantive —
this review covered both transcription accuracy and the ADR's own
reasoning, since this work plan lands a genuine new architecture
decision, not only a documentation edit). One scenario reproduced as a
real, non-blocking finding: `scripts/check-contract-consistency.py`'s
`RECORD_DIRS` exclusion list does not yet cover the new `docs/archive/`
directory ADR 0020's Rule 3 introduces — not actionable against this work
plan (no `docs/archive/` content exists here, per Rule 7), tracked as
LISS-0044 for whichever later work plan first creates archive content.

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

No finding blocks this work plan's Done. `LISS-0044` was opened from this
Reviewer's own recommendation as a tracked-for-later note, not a
must-resolve-before-close finding — it is deliberately not listed in the
table above (which `check_open_findings_gate` treats as blocking until
each row is `closed`/`wont_do`). It stays `Status: proposed`, legitimately
deferred to whichever later work plan (the retroactive-application work
plan, or facet 5 — drift-prevention entry documents and CI checks) first
creates content under `docs/archive/`, since it is not actionable before
then. See `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` and
`docs/collaboration/reviews/2026-08-19-wp-0014-document-log-lifecycle-model-review.md`'s
own Non-Blocking Observations for the full record.

## Work-Plan Close

- Date: 2026-08-19
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-19-wp-0014-document-log-lifecycle-model-review.md`,
  Approved — 16 falsification scenarios covering both mechanical accuracy
  and ADR 0020's reasoning, one genuine finding opened as LISS-0044 rather
  than fixed or ignored) via the Backlog thread, which independently
  confirmed ADR 0020, the restoration ledger, the review record, and a
  clean `scripts/check-contract-consistency.py` run from a detached
  checkout before presenting this close. The Backlog thread also caught
  and fixed a status-sync gap this close itself surfaced: LISS-0043 was
  still `Status: ready` despite being self-reviewed and Reviewer-approved
  — corrected to `done` as part of recording this close.
- Next direction: closed with "はい". Merged content sits on
  `process/backlog-item-0012-and-0013` (together with WP-0013, already
  closed). Push/PR/merge-to-main remain separate explicit actions. Facets
  4 (contract-sync diff record), 5 (drift-prevention CI checks — must also
  pick up LISS-0044), and 6 (review-summary packets) remain queued as
  their own later work plans. Retroactive application to this repository's
  own history stays a separate, later work plan after all rule-defining
  facets close, per the Director's sequencing decision at promotion.
- New design agreement (if any): none opened by this close — the later
  facet-4/5/6 work plans each get their own when reached.

## Risks

- Medium (planning size `L`, new ADR). Main risk: Rule 2's illustrative,
  non-exhaustive per-type consolidation triggers may need refinement once
  the later retroactive-application work plan actually applies them —
  named explicitly in ADR 0020's own Consequences section, not hidden.
  Secondary risk: scope creep into touching `CLAUDE.md`/mirrors or an
  existing repository document — explicitly fenced off in this work
  plan's own Scope and in ADR 0020's Rule 7, and checked directly in
  Preflight's scope-result step.
