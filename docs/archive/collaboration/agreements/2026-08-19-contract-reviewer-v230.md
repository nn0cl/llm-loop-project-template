# Design Agreement: Separate-Context Reviewer Pass for v2.3.0

## Identity

- Agreement ID: DA-2026-08-19-01
- Date: 2026-08-19
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0001-contract-reviewer-v230.md` (`Status: promoted`),
whose Promotion notes are this agreement's Director authorization under ADR
0016 Rule 2: obtain Reviewer approval from a separate context for the
v2.3.0 agent operating contract and collaboration-doc changes, per ADR 0006.
`CHANGELOG.md`'s own v2.3.0 entry states explicitly this edition is
"landed, not Reviewer-closed" — confirmed still true by this agreement's own
spike (below), not assumed from the backlog item's framing alone.

## Spike Result (run by the Design & Review group before this agreement)

- `CHANGELOG.md`'s v2.3.0 section states outright: "Separate-context
  Reviewer for the contract change remains open as backlog `item-0001`
  (ADR 0006) — this tag records the landed edition; it does not close that
  review," and lists `item-0001` in its own "Subordinate follow-ups" table
  as still open.
- Searched `docs/collaboration/reviews/` for any record referencing
  "v2.3.0" or "loop-ledger": none found.
- Read `docs/collaboration/traces/2026-08-10-loop-ledgers-and-settings.md`
  in full: its own "Covering design agreement" field states "Director
  session direction 2026-08-10 (no separate DA file); independent Reviewer
  still required — backlog `item-0001`," and its "Context Ledger" explicitly
  lists "Reviewer outcome for this land" as an open decision.
- **Conclusion: the gap is genuinely still fully open**, exactly as
  item-0001 assumed, not partially addressed. No review record, no design
  agreement file exists for the original v2.3.0 land.

## Scope

- In scope:
  - A separate-context Reviewer pass over the actual `v2.2.0..v2.3.0` diff
    (45 files, ~1,900 insertions — the loop-ledger/settings/mirror
    edition), addressing mirror parity, CI required-files coverage, and
    general contract soundness for the new vocabulary this edition
    introduced.
  - A review record under `docs/collaboration/reviews/`.
  - Updating `CHANGELOG.md`'s v2.3.0 entry to reflect the review outcome
    (closing the "landed, not Reviewer-closed" caveat, or recording
    findings if any).
  - This agreement itself, covering the Reviewer activity — since no
    design agreement exists for the *original* v2.3.0 work and item-0001's
    own boundary explicitly does not ask this item to retroactively
    manufacture one for content already landed and in continuous
    production use since 2026-08-10.
- Explicitly out of scope:
  - Re-opening v2.3.0's feature design or content, per item-0001's own
    "does not re-open feature design; review artifacts only" boundary.
  - Re-tagging or a patch release, unless the Reviewer pass finds a defect
    requiring one (per item-0001's own metadata note).

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Separate-context Reviewer pass over the v2.2.0..v2.3.0 diff | Reviewer (Design & Review group) | Architecture Path | Review record names failure scenarios searched (mirror parity, CI coverage, cross-document consistency for the new vocabulary) and their grounds; approves, or opens `Type: review-finding` issues for any defect | review record under `docs/collaboration/reviews/` |
| 2 | Update `CHANGELOG.md`'s v2.3.0 entry | Reviewer/Implementer (same session, documentation-only) | Fast Path | Caveat updated to reflect the actual review outcome | read-through diff |

Sequencing: Task 1 blocks Task 2.

## Specifications

- None. Retroactive governance review of an already-landed edition; no new
  application specification.

## Boundaries

- Does not alter v2.3.0's actual landed content beyond `CHANGELOG.md`'s own
  status caveat, unless a finding requires a correction — in which case
  that correction follows the normal Minor Fix Path / escalation rules,
  as its own tracked issue.
- This review, being over content this session did not author (landed
  2026-08-10, well before this session began), satisfies context
  separation directly — no Implementation-group dispatch is needed for the
  review itself.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does the missing original design-agreement file for the v2.3.0 land block this item? | No — item-0001's own scope is the Reviewer pass specifically, not retroactively manufacturing a design agreement for six-week-old, already-in-continuous-use content. This agreement (`DA-2026-08-19-01`) covers the Reviewer activity itself, and the review record will disclose the missing original design agreement as a named historical gap rather than silently ignore or fabricate one. | Design & Review group (Planner) |
| Does the Reviewer pass require dispatching to a separate Implementation-group session? | No — the content under review was authored by a session well before this one existed; this standing session reviewing it satisfies context separation on its own terms, the same way WP-0002's Reviewer review, run in this same standing session lineage, reviewed Implementation-group output it did not itself produce. | Design & Review group (Planner) |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should a standing rule be added requiring every future edition tag to have its Reviewer pass complete before tagging (rather than after, as happened here)? | A future backlog item, if the Director judges this worth codifying — out of this item's own narrow scope |

## Verification

- `python3 scripts/check-contract-consistency.py` re-run against the
  current tree (which still contains all v2.3.0 content).
- Mirror-parity spot check for the new "Loop Settings, Spikes, Backlog, and
  Findings" section across all four full-mirror files.
- CI `required_files` list cross-checked against the new files this
  edition introduced.

## Falsification Criteria

- The review approves without recording any deterministic verification
  output.
- A genuine mirror-parity or CI-coverage gap in the v2.3.0 diff is found
  and not tracked as a `Type: review-finding` issue.
- `CHANGELOG.md` is updated to claim Reviewer approval without a
  corresponding review record existing.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0001-contract-reviewer-v230.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan and the spike result above.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
