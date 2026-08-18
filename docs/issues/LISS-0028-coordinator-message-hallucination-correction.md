# LISS-0028: Correct the "coordinator" confabulation record

## Metadata

- Local issue ID: LISS-0028
- GitHub issue: none
- Status: ready
- Phase: process-only
- Type: process-correction
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/coordinator-message-correction

## Summary

- Correct `docs/collaboration/cross-session-messaging.md`'s "Confirmed
  failure mode" section and
  `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`'s
  "Provenance verification" section: the four unverified in-band
  "coordinator" messages received during WP-0002 were most likely
  model-side confabulation (triggered by legitimate 2026-08-02 review-record
  prose reusing the word "coordinator"), not confirmed external injection.
  No repository mechanism capable of injecting content was found anywhere
  (no `.claude/settings*.json`, no hook files, no trace in git history on
  any branch).

## Acceptance Notes

- `cross-session-messaging.md`'s section states the likely-confabulation
  explanation while preserving, unchanged in substance: the `ListAgents`
  absence finding, the confirmed `to: "main"` working address, and the
  "verify independently before trusting, regardless of source" rule.
- The WP-0002 review record gets a clearly-marked addendum, not an edit to
  its original Decision/checklist/falsification table.
- `scripts/check-contract-consistency.py` passes after the edit.
- An AI work trace exists under `docs/collaboration/traces/` naming the file,
  the reason, and the expected agent-behavior change.
- Self-review recorded (short form).
- Separate-context Reviewer confirmation recorded.

## Review Finding Record

N/A — not a `Type: review-finding` issue. See
`docs/collaboration/agreements/2026-08-18-coordinator-message-correction.md`'s
"Settled Ambiguities" for why the Minor Fix Path still applies by the
backlog item's own explicit direction.

## Dependencies

- Parent: docs/backlog/item-0008-coordinator-message-hallucination-correction.md
- Depends on: none
- Blocks: none
- Related: LISS-0022 (cross-session-messaging.md original authorship),
  LISS-0027 (prior Minor Fix Path precedent against a then-still-open
  agreement — this issue's own agreement is new, not a reopening, per
  `DA-2026-08-18-02`'s Settled Ambiguities)

## Decisions Not Settled by the Design Agreement

- None identified at design time. If the independent re-confirmation (Task 1
  of `DA-2026-08-18-02`'s Plan) finds evidence contradicting item-0008's
  claim, that is a reopening trigger per the agreement's Falsification
  Criteria, not a judgment call to resolve silently.

## Context

- Included: `docs/backlog/item-0008-*.md`,
  `docs/collaboration/cross-session-messaging.md`,
  `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`,
  `docs/collaboration/agreements/2026-08-18-coordinator-message-correction.md`.
- Omitted: WP-0002's other seven issues' individual traces/self-reviews —
  not needed to correct this one section.
- Assumptions: item-0008's own repo-wide search claim is accurate; verified
  independently as Task 1 before any edit, per the agreement's Boundaries.

## AI Planning Records

Not required — planning size `S`, first attempt expected.

## References

- `docs/backlog/item-0008-coordinator-message-hallucination-correction.md`
- `docs/collaboration/agreements/2026-08-18-coordinator-message-correction.md`
  (`DA-2026-08-18-02`)
- `docs/collaboration/prompt-instruction-change-control.md`

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0008-*.md`'s promotion. Independent evidence
  re-confirmation already run by the Design & Review group in this same
  session, ahead of dispatch, as a design-intake sanity check (not a
  substitute for the Implementer's own Task-1 re-run inside this issue):

  ```text
  $ grep -rni "coordinator" --include="*.md" --include="*.json" --include="*.py" --include="*.sh" .
  ```

  Result: only pre-existing 2026-08-02 review-record prose, WP-0002's own
  retrospective note, and item-0008's own backlog file — no other hits.

  ```text
  $ find . -iname "*settings*.json" -not -path "*/node_modules/*"
  ```

  Result: no matches.

  ```text
  $ find . -iname "*hook*" -not -path "*/.git/*" -not -path "*/node_modules/*"
  ```

  Result: one match, `docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md`
  (item-0006's own backlog file, about a *future* quality-gate hooks
  proposal — not an existing hook mechanism).

  This matches item-0008's own claim. Dispatched to the Implementation group
  to re-run independently (Task 1) and perform the edit (Tasks 2-6).

## Verification

- Pending Implementation-group execution; see WP-0003's Preflight Validation
  section.
