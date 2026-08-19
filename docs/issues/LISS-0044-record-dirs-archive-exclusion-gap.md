# LISS-0044: `check-contract-consistency.py`'s `RECORD_DIRS` does not exempt `docs/archive/`

## Metadata

- Local issue ID: LISS-0044
- GitHub issue: none
- Status: proposed
- Phase: docs-only
- Type: review-finding
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: unassigned — actionable only once a work plan first creates
  content under `docs/archive/`.
- Related branch: none yet

## Summary

- `docs/collaboration/reviews/2026-08-19-wp-0014-document-log-lifecycle-model-review.md`
  (Reviewer's own recommendation, "Non-Blocking Observations") found that
  `scripts/check-contract-consistency.py`'s `RECORD_DIRS` constant — the
  checker's own list of directories holding "dated statements about the
  past," exempt from present-tense reference/consistency checks — does not
  include `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`'s
  new `docs/archive/` directory, even though ADR 0020's own Rule 1 defines
  Archive-layer content as exactly this kind of dated, historical, no-
  longer-present-tense record.
- Since ADR 0020's Rule 3 requires archived files to be moved verbatim (no
  content rewriting), any internal link an archived file already contained
  will be scanned by `check_references` as if the file were still current,
  producing dangling-reference noise on content the checker's own stated
  design principle says should be exempt.
- Not actionable today: no `docs/archive/` directory exists yet (WP-0014
  is rules-only, per ADR 0020's own Rule 7 — no retroactive application).
  This issue becomes actionable once the retroactive-application work plan
  (named in `docs/backlog/item-0012-document-and-log-lifecycle-management.md`'s
  Promotion notes) or facet 5 (drift-prevention entry documents and CI
  checks, per the spike's own decomposition table) first creates content
  under `docs/archive/`.

## Acceptance Notes

- `scripts/check-contract-consistency.py`'s `RECORD_DIRS` gains a
  `docs/archive/` entry, or an equivalent, more targeted exclusion — the
  Reviewer's own note flags a nuance worth resolving at implementation
  time: an *inbound* reference *to* an archived file from a still-current
  document is exactly what ADR 0020's Rule 3 already requires updating
  when the move happens, and probably should stay checked (a fully blanket
  `docs/archive/` exemption might be too broad if it also stops checking
  those inbound references) — the fix should distinguish an archived
  file's own *outbound* links (should be exempt, matching the ADR's
  "moved verbatim" design) from other documents' *inbound* links to it
  (should very likely remain checked).
- `check_id_range_collisions` was confirmed by the Reviewer to be **not**
  vulnerable to the analogous gap (it compares against full `git log
  --all` history, not current directory listings) — this issue is scoped
  to `check_references` / `RECORD_DIRS` only, not a broader audit of every
  check in the script.
- Whichever work plan resolves this records deterministic verification
  (a real archived file with both an outbound and an inbound link,
  confirming the fix behaves as described) before closing this issue.

## Review Finding Record

- Originating review record:
  `docs/collaboration/reviews/2026-08-19-wp-0014-document-log-lifecycle-model-review.md`
  (Falsification Search #13; Non-Blocking Observations)
- Affected artifact: `scripts/check-contract-consistency.py` (`RECORD_DIRS`
  constant and `check_references`'s use of it)
- Failure scenario: an archived file under a future `docs/archive/`
  directory, moved verbatim per ADR 0020 Rule 3, contains an internal link
  that `check_references` scans as if the file were still a live,
  present-tense document — producing dangling-reference noise on content
  ADR 0020's own Rule 1 defines as historical and exempt from present-tense
  consistency.
- Reviewer grounds: `RECORD_DIRS`'s own source comment states its purpose
  ("[d]irectories holding records rather than contract... dated statements
  about the past... not held to present-tense consistency") and `docs/archive/`
  is not on the list, confirmed by direct reading of the script's current
  source at the time of WP-0014's review.
- Dispute raised by: none — recorded as a non-blocking finding by the
  Reviewer, not disputed by the Design & Review group; opened as a
  tracked issue per the Reviewer's own explicit recommendation and
  `docs/collaboration/findings-reuse.md`'s "must change the system or be
  explicitly declined" rule, rather than left as an unrecorded note.
- Arbiter decision record: none — no deadlock; the Reviewer's Approved
  decision for WP-0014 already accounts for this being non-blocking.
- Changed files: none yet — not actionable until a work plan first creates
  `docs/archive/` content.
- Deterministic verification output: none yet.
- Separate Reviewer closure record: none yet.

## Dependencies

- Parent: none
- Depends on: the retroactive-application work plan or facet 5
  (drift-prevention entry documents and CI checks) — whichever first
  creates content under `docs/archive/`; this issue is not independently
  actionable before then.
- Blocks: none (informational until actionable)
- Related: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `docs/backlog/item-0012-document-and-log-lifecycle-management.md`,
  `docs/spike/case-0001-document-log-lifecycle-management/case.md`

## Decisions Not Settled by the Design Agreement

- The exact shape of the `RECORD_DIRS`/`check_references` fix (blanket
  directory exemption vs. outbound-only exemption preserving inbound-link
  checking) is left to whichever work plan resolves this issue — the
  Reviewer's own note states this as an open implementation-time choice,
  not a settled design.

## Context

- Included: the WP-0014 review record in full, `scripts/check-contract-consistency.py`'s
  `RECORD_DIRS` definition and `check_references` function, ADR 0020's
  Rule 1 and Rule 3.
- Omitted: the retroactive-application work plan's own scope (not yet
  designed) and facet 5's own scope (not yet designed) — this issue does
  not pre-decide which of the two resolves it first.
- Assumptions: none beyond what the review record states directly.

## AI Planning Records

Not required — planning size `S`, not yet started (blocked on a
prerequisite work plan existing).

## References

- `docs/collaboration/reviews/2026-08-19-wp-0014-document-log-lifecycle-model-review.md`
- `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
- `scripts/check-contract-consistency.py`

## Work Notes

- 2026-08-19 — Design & Review group (Planner): opened this issue directly
  from the WP-0014 Reviewer's own explicit recommendation, to satisfy
  `docs/collaboration/findings-reuse.md`'s rule that a finding "must change
  the system or be explicitly declined," not be left as a verbal note that
  depends on someone rereading the review record to be rediscovered.
  `Status: proposed` rather than `accepted`/`in_progress`, since the finding
  is real but not yet actionable (no `docs/archive/` content exists to fix
  against) — will move to `accepted` once a work plan is ready to pick it
  up alongside the first `docs/archive/`-creating change.

## Verification

- Not yet run — blocked on this issue becoming actionable.
