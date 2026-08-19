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

- 2026-08-19 — Implementer (Claude Sonnet 5, Claude Code): self-review,
  full form (planning size `L`, per
  `docs/architecture/adr/0015-review-cost-discipline.md` and WP-0014's own
  Plan table). Covers Tasks 1-4 of `DA-2026-08-19-06`'s Plan (creating
  `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `docs/collaboration/restoration-ledger.md`, the cross-reference
  paragraph in `docs/collaboration/local-issue-planning.md`, and the AI
  work trace at
  `docs/collaboration/traces/2026-08-19-liss-0043-document-log-lifecycle-model.md`).
  Full form per `docs/templates/self-review.md`, using
  `docs/templates/review-record.md`'s "Deterministic Verification Output"
  and "Falsification Search" sections, filled out as the Implementer.

  ### Deterministic Verification Output

  Diff of each transcribed file against `DA-2026-08-19-06`'s own "Exact
  Content to Produce" text (extracted from the agreement file by exact
  line range, then diffed byte-for-byte against the created/edited file):

  ```text
  $ sed -n '99,368p' docs/collaboration/agreements/2026-08-19-document-log-lifecycle-model.md > /tmp/expected_adr0020.md
  $ diff /tmp/expected_adr0020.md docs/architecture/adr/0020-document-and-log-lifecycle-model.md
  (no output — files identical)

  $ sed -n '374,419p' docs/collaboration/agreements/2026-08-19-document-log-lifecycle-model.md > /tmp/expected_ledger.md
  $ diff /tmp/expected_ledger.md docs/collaboration/restoration-ledger.md
  (no output — files identical)

  $ sed -n '429,433p' docs/collaboration/agreements/2026-08-19-document-log-lifecycle-model.md > /tmp/expected_para.md
  $ sed -n '219,223p' docs/collaboration/local-issue-planning.md > /tmp/actual_para.md
  $ diff /tmp/expected_para.md /tmp/actual_para.md
  (no output — identical)

  $ git diff docs/collaboration/local-issue-planning.md
  --- a/docs/collaboration/local-issue-planning.md
  +++ b/docs/collaboration/local-issue-planning.md
  @@ -216,6 +216,12 @@ Use:
   - `done`
   - `wont_do`

  +This is the issue's own lifecycle status, not the same field as the
  +document-lifecycle role (Entry/Canonical/Evidence/Archive) and status
  +vocabulary `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
  +defines. The two are independent: an issue can be `done` long before it is
  +eligible for archival under ADR 0020's Rule 2.
  +
   ## Phase Values

   Use:
  (single hunk — exactly one paragraph inserted, nothing else in the file
  touched)

  $ python3 scripts/check-contract-consistency.py
  references:
    docs/architecture/adr/0020-document-and-log-lifecycle-model.md:151 names 'trace-topic-register.md', which does not exist

  ADR range:
    README.md states 0019 where 0020 is expected (pattern: 'ADRs included here \(0001-(\d{4})\)')
    README.md states 0020 where 0021 is expected (pattern: 'own decisions from (\d{4}) up')
    QUICKSTART.md states 0019 where 0020 is expected (pattern: '`docs/architecture/adr/0001-\*\.md` through `(\d{4})-\*\.md`')
    QUICKSTART.md states 0020 where 0021 is expected (pattern: 'keep any ADR your\s+project numbered afterward \((\d{4}) and up\)')
    QUICKSTART.md states 0019 where 0020 is expected (pattern: 'records" asserts ADRs 0001[-–](\d{4})')
    QUICKSTART.ja.md states 0019 where 0020 is expected (pattern: '`docs/architecture/adr/0001-\*\.md` から `(\d{4})-\*\.md` までは')
    QUICKSTART.ja.md states 0020 where 0021 is expected (pattern: 'ADR（(\d{4}) 以降）')
    QUICKSTART.ja.md states 0019 where 0020 is expected (pattern: 'ADR 0001〜(\d{4}) を検査')

  contract consistency: 9 failure(s)
  exit code: 1

  $ git status --porcelain
   M docs/collaboration/local-issue-planning.md
  ?? docs/architecture/adr/0020-document-and-log-lifecycle-model.md
  ?? docs/collaboration/restoration-ledger.md
  ?? docs/collaboration/traces/2026-08-19-liss-0043-document-log-lifecycle-model.md
  ```

  ### Falsification Search

  | # | Failure scenario searched for | Grounds it does not occur | Result |
  |---|---|---|---|
  | 1 | Transcribed content diverges from `DA-2026-08-19-06`'s "Exact Content to Produce" (File 1, ADR 0020), including internal cross-references (e.g. the ADR's own references to `DA-2026-08-19-06`, LISS-0043, WP-0014, item-0012, case-0001) | `diff` against the agreement's own text (lines 99-368) produced no output — byte-identical | not reproduced |
  | 2 | Transcribed content diverges from File 2 (`restoration-ledger.md`), including the nested `git show` code-fence (outer/inner fence nesting) | `diff` against the agreement's own text (lines 374-419) produced no output — byte-identical, fence nesting preserved | not reproduced |
  | 3 | Transcribed content diverges from File 3's cross-reference paragraph, or is placed in the wrong location within `local-issue-planning.md` | `diff` against the agreement's own text (lines 429-433) produced no output; `git diff` shows a single hunk inserting the paragraph directly after the `wont_do` bullet and before `## Phase Values`, matching the specified insertion point exactly | not reproduced |
  | 4 | An existing repository document outside the one named paragraph (any `docs/issues/`, `docs/work-plans/`, `docs/collaboration/traces/`, `docs/collaboration/reviews/`, `docs/collaboration/agreements/`, or other `docs/architecture/adr/` file) was moved, archived, deleted, or edited | `git status --porcelain` before this Work Notes edit lists only 2 untracked new files (`0020-...md`, `restoration-ledger.md`) plus the trace file and 1 modified file (`local-issue-planning.md`); `git diff` on the modified file shows exactly one inserted hunk and no deletions or moves anywhere else | not reproduced |
  | 5 | The restoration ledger's Ledger table contains a data row | `tail -3 docs/collaboration/restoration-ledger.md` shows only the header, separator, and the literal placeholder row `_(no entries yet — ...)_ \| \| \| \| \| \|` — no populated row | not reproduced |
  | 6 | `CLAUDE.md` or a mirror file (`AGENTS.md`, `.cursor/rules/*`, `.grok/rules/*`, `.gemini/*`, etc.) was touched | `git status --porcelain` does not list `CLAUDE.md`, `AGENTS.md`, or any mirror path among the 4 changed files | not reproduced |
  | 7 | `scripts/check-contract-consistency.py`'s 9 findings indicate an actual transcription defect requiring correction | Findings inspected individually: the 1 `references` finding is the checker's `CODE_PATH` heuristic tripping on a backtick-wrapped external-repository filename (`trace-topic-register.md`, a `qpex` file cited by the spike, not a local path) present verbatim in the agreement's own specified text; the 8 `ADR range` findings are `README.md`/`QUICKSTART.md`/`QUICKSTART.ja.md` stating a now-stale ADR count, which is the exact, named, deliberately deferred gap in ADR 0020's own Consequences section (facet 5, a later separate work plan) and is outside `DA-2026-08-19-06`'s Scope (only 3 files are in scope; these mirror/README files are not among them, and are separately covered by the Boundaries section's `CLAUDE.md`-and-mirrors prohibition) | not reproduced (both are pre-existing/anticipated, not a content defect) |

  ### Scenarios Not Searched

  - Substantive soundness of ADR 0020's reasoning (four-layer mapping,
    consolidation triggers, archive mechanism) — this is explicitly the
    work-plan-level Reviewer's job per `DA-2026-08-19-06`'s Plan Task 7
    ("confirms the ADR's substantive soundness, not only mechanical
    transcription accuracy"), not the Implementer's self-review, which is
    scoped to transcription accuracy and scope-boundary conformance.
  - Whether ADR 0020's own internal claims (e.g. "19 ADRs," specific line
    references to other ADRs) are independently correct — these are
    design-authored claims from the covering design agreement, not
    Implementer-introduced content, and fall under the Reviewer's
    substantive-soundness check, not this self-review.

- 2026-08-19 — Implementer (Claude Sonnet 5, Claude Code): **correction
  cycle**, same day, following the Design & Review group's independent
  Preflight run. Preflight reproduced the same 9
  `scripts/check-contract-consistency.py` findings this self-review's
  Falsification Search row 7 (above) had judged pre-existing/anticipated,
  and treated both as real defects requiring a fix rather than a note.
  `DA-2026-08-19-06` and WP-0014 were amended on
  `origin/process/backlog-item-0012-and-0013` (commit `be1d857`) to bring
  the fix into scope: a Scope "Addendum" adding `README.md`/
  `QUICKSTART.md`/`QUICKSTART.ja.md`'s ADR-range statements as routine
  `check_adr_range` maintenance (not item-0012's own retroactive-
  application rules), a corrected Rule 4 citation in "File 1" (the bare
  `` `trace-topic-register.md` `` backtick reference replaced with the
  full external absolute path
  `` `/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md` ``,
  explicitly marked as a different, external repository's file), and a new
  "File 4" giving the exact old-text -> new-text string-replacement pairs.

  Row 7's original "not reproduced" verdict is superseded by this entry,
  per Invariant 2 (the failed-then-fixed sequence stays visible, not
  smoothed over) — left in place above rather than edited.

  Both corrections applied on this branch from the amended agreement text
  (`be1d857`): ADR 0020's Rule 4 sentence updated (verified byte-identical
  by `diff` against the amended agreement's own File 1 text; only that one
  sentence changed, confirmed by `git diff 874c6ce` below showing a
  4-line change in the ADR file); the 7 exact string replacements from
  "File 4" applied to `README.md` (2 sentences + 1 tree-diagram comment),
  `QUICKSTART.md` (3), and `QUICKSTART.ja.md` (3), matched by exact
  old-text string per the agreement's own instruction.

  ```text
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed
  exit code: 0

  $ git diff 874c6ce --stat
   QUICKSTART.ja.md                                               | 6 +++---
   QUICKSTART.md                                                  | 6 +++---
   README.md                                                      | 6 +++---
   docs/architecture/adr/0020-document-and-log-lifecycle-model.md | 4 +++-
   4 files changed, 12 insertions(+), 10 deletions(-)

  $ git status --porcelain
   M QUICKSTART.ja.md
   M QUICKSTART.md
   M README.md
   M docs/architecture/adr/0020-document-and-log-lifecycle-model.md
  ```

  Exactly the 4 files the amended agreement's Addendum and corrected File 1
  named changed; no other file. `CLAUDE.md` and its four mirrors were not
  touched — `README.md`/`QUICKSTART.md`/`QUICKSTART.ja.md` are not among
  them (confirmed against ADR 0006's mirror list). No ledger data row
  added; no other existing repository document moved, archived, deleted,
  or edited.

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
