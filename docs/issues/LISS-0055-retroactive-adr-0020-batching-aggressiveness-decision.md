# LISS-0055: Retroactive ADR 0020 application — batching-aggressiveness decision

## Metadata

- Local issue ID: LISS-0055
- GitHub issue: none
- Status: proposed
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: docs-only
- Type: decision
- Priority: medium
- Initial planning size: TBD (this issue records a decision, not
  implementation work; the resulting execution work plan gets its own
  planning size once opened)
- Current planning size: TBD
- Reclassification reason: N/A — first attempt, no reclassification.
- Owner/agent: unassigned — awaiting Director/Backlog-thread response
- Related branch: none — this issue records a decision checkpoint, not
  code or document changes

## Summary

`docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`
(`Status: promoted`) is the deliberately-deferred second half of item-0012:
apply `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`'s
four-layer model, status vocabulary, and archival mechanism to this
repository's own existing history. Its Uncertainty section names two
required-first steps: a spike on batching strategy and ledger scale, and a
human decision on how aggressive the first archival pass should be. Its
Promotion notes are explicit that this is one genuine exception to ADR
0016 Rule 2's usual full autonomy: "Design & Review should propose a
concrete batching plan and check with the Backlog thread before executing
a large first sweep, rather than archiving this repository's entire
qualifying history in one pass unprompted."

The required-first spike,
`docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`
(`Status: closed`, Selection: Option B), is now closed. This issue is the
recorded checkpoint that spike's own "Next action" opens: **no document has
been moved, archived, or edited by either the spike or this issue** — that
happens only after the Director/Backlog thread responds here, per the
item's own mandate.

## Acceptance Notes

This issue is resolved when the Director/Backlog thread states a decision
recorded below, and either:

- a follow-up work plan and design agreement are opened to execute the
  authorized first batch (per the item's own "Standard mandate otherwise
  applies once you're past the check-in" instruction), or
- the Director redirects the batching approach, scope, or sequencing, and
  this issue records that redirection before any execution work plan
  opens.

## Proposed batching plan (from case-0002)

- **Batching unit**: by work plan (Director-closed work plan, oldest
  first), not a single full-history sweep and not batched by artifact
  type. The work plan is the unit ADR 0020 Rule 2's own per-type triggers
  ultimately resolve against — a trace, review record, or design agreement
  attached to a work plan inherits that work plan's own archival
  eligibility, so batching any other way risks an inconsistent
  intermediate state.
- **Zero ADRs move in this or any near-term batch.** No ADR in this
  repository has ever had every one of its Decision clauses explicitly
  named as superseded (ADR 0020's own Rule 2 trigger for ADRs) — confirmed
  directly against every ADR's own Status section and against ADR 0016's
  "Supersession, precisely" table, the only concrete supersession
  precedent in this repository's history, which is itself only partial.
  ADR 0020 itself already names this as an expected, accepted trade-off.
  The Canonical/ADR layer is out of scope for the first batch, and likely
  for a long time after.
- **First-batch candidate**: WP-0001 (`docs/work-plans/WP-0001-review-issues-minor-fix-path.md`)
  — its own file already records its one issue, LISS-0001, at terminal
  `Status: done` with "Current Next Issue: none... LISS-0001 is complete."
  It predates the "Director close" commit-message convention this
  repository later standardized on, but the terminal-status evidence is
  present in the file itself; treating it as archival-eligible on that
  basis is a judgment call ADR 0020 Rule 2 itself anticipates the
  retroactive-application work plan recording explicitly.
- **WP-0002 is a concrete open question, found by the spike, not an ADR
  0020 gap**: WP-0002 (the founding two-group-loop work plan) is
  Director-closed, but its own nine issues (LISS-0019 through LISS-0027)
  are still `Status: review`, not `done`. Rule 2's literal wording ("every
  issue in it is `done` or `wont_do`") is not yet satisfied. Two ways
  forward, either acceptable, but the Director/Backlog thread's steer on
  which is welcome:
  1. Correct those nine issues' Status fields to `done` (reflecting their
     actual already-reviewed-and-closed reality) before archiving WP-0002,
     as ordinary bookkeeping ahead of the archive move; or
  2. Record an explicit judgment call in the execution work plan treating
     a Director-closed work plan's frozen pre-terminal issue statuses as
     equivalent to `done` for archival-eligibility purposes only, without
     editing the individual issue files.
- **WP-0003 through WP-0018**: each has its own Director-close commit; the
  spike did not re-verify every one's issue-level and open-review-finding
  detail individually (that is explicitly the execution work plan's own
  Preflight job, not pre-done by the spike). A plausible second and later
  batch, once the Director authorizes a first batch and it lands cleanly:
  work-plan-oldest-first through WP-0018, each batch small enough to stay
  in one reviewable commit, re-verifying eligibility fresh at batch time
  rather than trusting this spike's now-dated spot-check.
- **Ledger format**: confirmed to scale at this volume — the seven-column
  schema (`date, source_path, source_commit, source_tag,
  canonical_destination, classification, reason`) fixed by case-0001 and
  ADR 0020 Rule 5 held up cleanly against a drafted (not committed) sample
  row for the WP-0001 candidate; see case-0002's own "Sample ledger row"
  subsection.
- **Known, already-scoped drift-prevention risk**: LISS-0052 (open,
  low-priority) — a fenced-code-block gap in
  `check_no_archive_reference_from_entry` — is low risk for a first small
  batch (no Entry document today cites any archived path) but should be
  re-checked before a larger, later batch. LISS-0044's earlier
  `RECORD_DIRS` exclusion gap is already resolved in the current tree.

## What is being asked of the Backlog thread

Exactly the question item-0016's own Uncertainty section reserved: how
aggressive should the first archival pass be? Concretely:

1. Authorize the proposed first batch (WP-0001 only, or WP-0001 plus
   WP-0002 once its issue-status question is resolved per one of the two
   options above) — with later work-plan-scoped batches to follow as
   separate, later executions, each re-verified fresh; or
2. Direct a different scope for the first batch (e.g., a larger cutoff
   such as "through WP-0009," or a smaller one such as "WP-0001 only, no
   WP-0002 in this round"); or
3. Direct that WP-0002's issue-status question be resolved a specific way
   before either work plan is archived; or
4. Hold this item open for further discussion before any batch executes.

## Dependencies

- Parent: `docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`
- Depends on: `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`
  (`Status: closed`)
- Blocks: the retroactive-application execution work plan (not yet opened)
- Related: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `docs/collaboration/restoration-ledger.md` (still empty),
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`,
  `docs/issues/LISS-0052-entry-archive-reference-fenced-code-block-gap.md`

## Decisions Not Settled by the Design Agreement

- No design agreement covers this item yet beyond the backlog-item-level
  approval (`docs/backlog/item-0016-...md`, `Status: promoted`) — per that
  item's own Promotion notes, the batching-aggressiveness decision this
  issue asks for is explicitly reserved as a human-decision point before
  the execution work plan's own design agreement is produced.

## Context

- Included: item-0016's full text, ADR 0020's full text, direct git-history
  and file-content inspection of the candidate work plans and their
  issues, the existing drift-prevention checker's current archive-related
  logic.
- Omitted: full per-issue re-verification of WP-0003 through WP-0018 (left
  to the execution work plan's own Preflight, as stated above).
- Assumptions: none beyond what case-0002 records; no assumption is used
  in place of an unresolved question — every open question above is
  surfaced explicitly rather than guessed past.

## References

- `docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`
- `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
- `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`
- `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Spike case-0002
  closed with Selection: Option B (conservative, work-plan-scoped
  batches). This issue opened as the recorded check-in point per item-0016's
  own Promotion notes, before any document is moved or archived. No
  Implementation work has been dispatched. Awaiting Director/Backlog-thread
  response before opening the execution work plan and design agreement.

## Verification

- N/A — this issue records a decision checkpoint, not executable or
  testable work. Deterministic verification applies to the later execution
  work plan once authorized.
