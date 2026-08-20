# LISS-0065: Retroactive ADR 0020 application — batch 2 proposal

## Metadata

- Local issue ID: LISS-0065
- GitHub issue: none
- Status: proposed
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: docs-only
- Type: decision
- Priority: medium
- Initial planning size: TBD (this issue records a proposal and decision
  checkpoint, not implementation work; the resulting execution work plan
  gets its own planning size once opened)
- Current planning size: TBD
- Reclassification reason: N/A — first attempt.
- Owner/agent: unassigned — awaiting Backlog-thread response
- Related branch: none — this issue records a proposal and decision
  checkpoint, not code or document changes

## Summary

`docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`'s
Promotion notes (updated 2026-08-20, commit `63a08eb`) authorize Design &
Review to propose a concrete batch-2 archival plan via a new check-in
issue mirroring `docs/issues/LISS-0055-...md`'s own shape — the same
process batch 1 used. This is that issue. **No document is moved by this
issue** — per the same mandate as batch 1, the batch-2 scope decision
itself is reserved for the Backlog thread's response, recorded in this
issue's own Work Notes, before any execution work plan opens.

Batch 1 (`WP-0019`) archived WP-0001 and WP-0002. `docs/work-plans/`
currently holds WP-0003 through WP-0023 (21 work plans) unarchived. This
proposal covers a conservative next slice, oldest-first, and explicitly
defers the rest — matching case-0002's own Option-B rationale (bounded,
reviewable batches, each re-verified fresh, rather than one large sweep).

## Proposed batch-2 scope: WP-0003 through WP-0009 (7 work plans)

### Eligibility, independently re-verified against the actual files (not assumed from case-0002's now-dated spot-check)

| Work plan | Director-close date | Owned issue(s) | Issue status | Open review-finding naming it |
| --- | --- | --- | --- | --- |
| WP-0003 (coordinator-message-correction) | 2026-08-18 | LISS-0028 | done | none found |
| WP-0004 (multi-agent-tool-loop-portability) | 2026-08-18 | LISS-0029, LISS-0030 | done, done | none found |
| WP-0005 (template-propagation-work-plan-exclusion) | 2026-08-18 | LISS-0031 | done | none found |
| WP-0006 (quality-gate-hooks-and-perspectives-doc) | 2026-08-18 | LISS-0032, LISS-0033 | done, done | none found |
| WP-0007 (document-consistency-drift-checks) | 2026-08-18 | LISS-0035 | done | none found |
| WP-0008 (coordinator-role-inoculation-rule) | 2026-08-18 | LISS-0036 | done | none found |
| WP-0009 (contract-reviewer-v230) | 2026-08-19 | LISS-0037 | done | none found |

Open-review-finding check performed by `grep -rl "Type: review-finding"
docs/issues/` cross-checked against each matched file's own `Type:` field
directly (not string-matched alone) — the same methodology `LISS-0057`
used for batch 1. No genuine open `Type: review-finding` issue names any
of WP-0003 through WP-0009 or their own LISS numbers.

**All seven work plans are Rule-2-eligible for their own file and owned
issues.**

### Design agreements: two are blocked by ADR 0020 Rule 2's general clause, same pattern as batch 1

Independently checked every one of these seven work plans' own covering
design agreement against every current ADR's own Status/body text for a
normative citation (the same check that found `DA-2026-08-02-04` and
`DA-2026-08-18-01` blocked in batch 1):

| Work plan | Design agreement | Cited normatively by a current ADR? | Archival disposition |
| --- | --- | --- | --- |
| WP-0003 | `DA-2026-08-18-02` | No | Eligible |
| WP-0004 | `DA-2026-08-18-03` | **Yes** — ADR 0017's own Status section: "Accepted status requires a design agreement... That agreement is `DA-2026-08-18-03`" | **Blocked** — stays in place |
| WP-0005 | `DA-2026-08-18-04` | No | Eligible |
| WP-0006 | `DA-2026-08-18-05` | **Yes** — ADR 0018's own Status section: "Covered by `DA-2026-08-18-05`" | **Blocked** — stays in place |
| WP-0007 | `DA-2026-08-18-06` | No | Eligible |
| WP-0008 | `DA-2026-08-18-07` | No | Eligible |
| WP-0009 | `DA-2026-08-19-01` | No | Eligible |

Same grounds as batch 1's `DA-2026-08-02-04`/`DA-2026-08-18-01` finding:
ADR 0020 Rule 2's opening clause blocks archival of any document "a
current Canonical document still references by more than a passing
mention," regardless of the document's own terminal status. `DA-2026-08-18-03`
and `DA-2026-08-18-05` are each a current, Accepted ADR's own
Accepted-status grounding citation — normative, not passing. The
execution work plan's own LISS issues must name this exclusion
explicitly, the same way `LISS-0056`/`LISS-0057` did.

### Batching unit and traces/reviews

Same batching unit as batch 1 (the work plan, per case-0002's own
rationale — a trace, review record, or design agreement's own eligibility
is defined against its owning/reviewed work plan's archival state, not
independently). The execution work plan's own issues must enumerate the
exact trace and review-record file list per work plan (mirroring
`LISS-0056`/`LISS-0057`'s own per-file tables) — not fully enumerated in
this proposal, consistent with case-0002's own precedent of deferring
exhaustive per-file listing to the execution issue itself, not the
check-in proposal.

### Explicitly deferred to a later batch (not this one)

- **WP-0010 through WP-0023** (14 work plans) — each has its own
  Director-close commit (spot-checked directly for this proposal: all
  show a real, non-empty "Date:" in their own Work-Plan Close section
  except one gap noted below), but full issue-level and
  open-review-finding-level re-verification was not performed for this
  range, the same "defer to a later batch, re-verify fresh at batch time"
  posture case-0002 itself recommended for WP-0003 through WP-0018 as a
  whole. A third batch can cover a further slice once this one lands
  cleanly.
- **WP-0019 through WP-0023 specifically** — these are the archival
  mechanism's own bootstrapping work plans (batch 1 itself, plus the
  three bug-fix/protocol work plans batch 1's own execution surfaced:
  item-0018's copy-exclusion fix, item-0019's missing trace, item-0020's
  wake protocol). Recommend holding these out of archival consideration
  for longer than the rest of WP-0010-0018, even once a later batch
  reaches that range — they are the most direct, still-actively-relevant
  explanatory record of how the archival mechanism itself was built and
  debugged, and their own design agreements (`DA-2026-08-20-02` through
  `-06`) are only hours old as of this proposal, with no chance yet to
  observe whether a future ADR cites any of them normatively the way
  `DA-2026-08-18-01`/`-03`/`-05` and `DA-2026-08-02-04` turned out to be.
  This is a judgment call, not a hard rule — noted for the Backlog
  thread's own view, not silently decided here.

### Real gap found, unrelated to this batch's own scope but worth recording

`docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`'s own "Work-Plan
Close" section has an **empty** `Date:` field — never filled in, even
though the work is merged and functionally Director-closed (folded into
`WP-0019`'s own combined close narrative without WP-0021's own section
being updated). This means WP-0021 is not itself Rule-2-eligible as
things currently stand (Director-closed, per its own file, is not yet
true) — not relevant to this proposal's own WP-0003-0009 scope, since
WP-0021 is already excluded above, but worth a small housekeeping fix
(filling in the real date, which is known — 2026-08-20, per PR #21's own
merge record) whenever WP-0010-0023 range is eventually addressed, rather
than being rediscovered fresh at that time.

## Separately resolved: backlog items 0005-0009's own true status

The Design & Review group's own prior message (before this proposal) flagged
uncertainty about whether `docs/backlog/item-0005` through `item-0009`
represent genuinely unstarted queued work or merely have a stale `Links`
field. Independently checked, by direct cross-reference rather than
guessing:

| Backlog item | Own `Status` | Own `Links: Work plan` field | Actual resolution |
| --- | --- | --- | --- |
| item-0005 (template-propagation-script-for-two-group-loop) | promoted | "none yet" (stale) | Resolved by `WP-0005` — confirmed by direct cross-reference in `WP-0005`'s own text ("confirming the original item-0005 question") |
| item-0006 (quality-gate-hooks-and-review-perspectives-doc) | promoted | "none yet" (stale) | Resolved by `WP-0006` — confirmed by explicit citation in `WP-0006`'s own file |
| item-0007 (multi-agent-tool-loop-portability) | promoted | "none yet" (stale) | Resolved by `WP-0004` and ADR 0017 — confirmed by explicit citation in both files |
| item-0008 (coordinator-message-hallucination-correction) | promoted | "none yet — likely a Minor Fix Path addendum..." (stale) | Resolved by `WP-0003` — confirmed by explicit citation in `WP-0003`'s own file |
| item-0009 (document-consistency-drift-on-completion) | promoted | "none yet" (stale) | Resolved by `WP-0007` — confirmed by explicit citation in `WP-0007`'s own file |

**None of these five backlog items represent genuinely unstarted queue
work.** All five are done, each via a real work plan already Director-closed;
their own `Links` sections were simply never updated to point back at the
resulting work plan — a real, low-priority documentation-accuracy gap
across five files, not a functional gap. Not fixed by this issue (out of
its own scope, and per `docs/backlog/README.md`'s own status model,
backlog items do not carry a terminal status field of their own — "promoted"
is expected to persist even after the resulting work is done; only the
`Links` field staleness is the actual defect). Worth a small, separate,
low-risk housekeeping issue if the Backlog thread wants it fixed, not
opened here.

## Acceptance Notes

This issue is resolved when the Backlog thread states a decision recorded
below, and either:

- a follow-up work plan and design agreement are opened to execute the
  authorized batch-2 scope (WP-0003 through WP-0009, as proposed, or a
  Backlog-thread-redirected scope), or
- the Backlog thread redirects the scope, and this issue records that
  redirection before any execution work plan opens.

## What is being asked of the Backlog thread

1. Authorize the proposed batch-2 scope (WP-0003 through WP-0009, 7 work
   plans, excluding their 2 normatively-blocked design agreements) — with
   later batches (WP-0010 onward) to follow as separate, later,
   fresh-re-verified executions, same as batch 1's own precedent; or
2. Direct a different scope (larger, smaller, or a different grouping —
   e.g., by theme rather than strictly chronological); or
3. Direct whether WP-0019-0023's own longer-hold recommendation above is
   agreed or should be revisited; or
4. Direct that the stale-`Links` housekeeping across items 0005-0009 be
   folded into this same batch's own work plan, or left as a separate,
   later issue; or
5. Hold this item open for further discussion.

## Dependencies

- Parent: `docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`
- Depends on: `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`
  (`Status: closed`), the batch-2 authorization entry in item-0016's own
  Promotion notes (commit `63a08eb`)
- Blocks: the batch-2 execution work plan (not yet opened)
- Related: `docs/issues/LISS-0055-retroactive-adr-0020-batching-aggressiveness-decision.md`
  (batch-1 precedent), `docs/work-plans/WP-0019-retroactive-adr-0020-archival-batch-1.md`

## Decisions Not Settled by the Design Agreement

- No design agreement covers this item yet beyond item-0016's own
  backlog-level approval and the batch-2 proposal authorization
  (`63a08eb`) — per that entry's own text, the batch-2 scope decision
  itself is explicitly reserved for this issue's own Work Notes, the same
  way LISS-0055 reserved batch 1's.

## Context

- Included: item-0016's full text (including the new batch-2
  authorization entry), case-0002's full text, direct file-level
  re-verification of all 21 currently-unarchived work plans' own
  Work-Plan Close sections, direct issue-graph and review-finding checks
  for the proposed 7-work-plan batch, direct ADR-citation checks for all
  7 covering design agreements, direct cross-reference resolution of
  backlog items 0005-0009's own true completion status.
- Omitted: full per-issue re-verification of WP-0010 through WP-0023 (left
  to a later batch's own check-in, per case-0002's own established
  posture); exhaustive trace/review-record file enumeration for WP-0003
  through WP-0009 (left to the execution work plan's own issues, matching
  how LISS-0056/LISS-0057 did the exhaustive listing at execution time,
  not proposal time).
- Assumptions: none beyond what is stated explicitly above; every open
  question is surfaced, not guessed past.

## References

- `docs/backlog/item-0016-retroactive-adr-0020-lifecycle-application.md`
- `docs/issues/LISS-0055-retroactive-adr-0020-batching-aggressiveness-decision.md`
- `docs/spike/case-0002-retroactive-adr-0020-lifecycle-application/case.md`
- `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
- `docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`
- `docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Proposal drafted
  per item-0016's own new Promotion-notes entry (commit `63a08eb`)
  authorizing this exact step. Independently re-verified every claim
  above against the actual files (Director-close dates, issue statuses,
  open-review-finding search, ADR-citation search for each design
  agreement, and the backlog-items-0005-0009 cross-reference resolution)
  rather than assuming case-0002's now-dated spot-check generalizes. No
  document moved. Awaiting Backlog-thread response before opening the
  execution work plan and design agreement.
- 2026-08-20 — Backlog-thread decision received: option 1 combined with
  option 4 from "What is being asked of the Backlog thread" above. The
  proposed batch-2 scope (WP-0003 through WP-0009, 7 work plans, excluding
  the 2 normatively-blocked design agreements `DA-2026-08-18-03` and
  `DA-2026-08-18-05`) is authorized, oldest-first, same footing as batch
  1's precedent. Additionally, fold into this same batch's execution work
  plan: (a) the stale `Links: Work plan` field fix across
  `docs/backlog/item-0005-*.md` through `item-0009-*.md` (pointing each at
  its actual resolving work plan — WP-0005, WP-0006, WP-0004, WP-0003, and
  WP-0007 respectively, per this issue's own cross-reference table above),
  and (b) `docs/work-plans/WP-0021-archive-copy-exclusion-gap.md`'s own
  empty Work-Plan Close `Date:` field, filled in as `2026-08-20` per PR
  #21's own merge record (already named as the known, correct value in
  this issue's "Real gap found" section above). Option 3 (the WP-0019-0023
  longer-hold recommendation) is agreed as proposed — no redirection.
  Standard mandate otherwise applies once past this check-in: open the
  execution work plan and design agreement, proceed autonomously per ADR
  0016 Rule 2/7.

## Verification

- N/A — this issue records a proposal and decision checkpoint, not
  executable or testable work. Deterministic verification applies to the
  later execution work plan once authorized.
