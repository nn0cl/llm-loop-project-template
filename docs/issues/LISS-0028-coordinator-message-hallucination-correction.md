# LISS-0028: Correct the "coordinator" confabulation record

## Metadata

- Local issue ID: LISS-0028
- GitHub issue: none
- Status: review
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

- 2026-08-18 (Implementation group, Implementer): worktree setup — the
  session's original checkout (branch `worktree-agent-a5586e6bbd8255817`,
  from `main` at `11d5898`) did not carry `DA-2026-08-18-02` or this issue's
  file. Confirmed commit `2a59c54` ("process: design phase for LISS-0028
  (coordinator-message correction)") was already reachable locally (no
  `git fetch` needed), then created and switched to
  `process/coordinator-message-correction` from that commit.

  Task 1 — independently re-ran the evidence reconfirmation before editing
  anything, per `DA-2026-08-18-02`'s Plan table:

  ```text
  $ grep -rni "coordinator" --include="*.md" --include="*.json" --include="*.py" --include="*.sh" .
  ```

  Result: hits only in `docs/collaboration/agreements/2026-08-18-coordinator-message-correction.md`,
  `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`
  (the file this issue adds an addendum to, describing the messages it
  received), `docs/collaboration/reviews/2026-08-02-mirror-parity-review-2.md`,
  `docs/collaboration/reviews/2026-08-02-contract-consistency-review-2.md`,
  `-3.md`, `-4.md` (pre-existing 2026-08-02 review-record prose),
  `docs/work-plans/WP-0003-coordinator-message-correction.md`,
  `docs/backlog/item-0008-coordinator-message-hallucination-correction.md`,
  `docs/work-plans/WP-0002-two-group-send-message-loop.md` (its own
  retrospective note), and this issue file itself. No other hits.

  ```text
  $ find . -iname "*settings*.json" -not -path "*/node_modules/*"
  ```

  Result: no matches.

  ```text
  $ find . -iname "*hook*" -not -path "*/.git/*" -not -path "*/node_modules/*"
  ```

  Result: one match, `docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md`
  (item-0006's own backlog file about a *future* quality-gate hooks
  proposal — not an existing hook mechanism).

  Cross-branch check: `git branch -a` listed 35 local and 32 remote-tracking
  refs (plus the `origin` symref itself, not a grep-able tree-ish, skipped
  as redundant with `origin/main`). Ran `git grep -il "coordinator" <refs>
  -- '*.md'` across all of them (batched as multiple tree-ish arguments to
  one `git grep` invocation per group, not a shell loop, per this
  environment's worktree-isolation constraint on complex git commands).
  Every hit across every branch was one of: the pre-existing
  `docs/collaboration/reviews/2026-08-02-*.md` files, or a file that is
  itself part of this correction effort or WP-0002's own retrospective note
  (on the branches that carry those files). No settings/hook mechanism, and
  no unexplained "coordinator" occurrence, on any branch checked.

  This matches item-0008's own claim and this issue's own design-time
  re-confirmation exactly. No discrepancy found; proceeded to Tasks 2-6
  rather than stopping for a reopening request.

- 2026-08-18 (Implementation group, Implementer): Task 2 — edited
  `docs/collaboration/cross-session-messaging.md`'s "Confirmed failure mode"
  section to state the likely-confabulation explanation (with an explicit
  "likely," not "confirmed," qualifier) and cross-reference
  `docs/backlog/item-0008-*.md`, while leaving the four numbered
  `ListAgents`-absence findings and the "What this means, stated as a rule"
  / "The fix" paragraphs unchanged in substance. No other section of the
  file was touched (confirmed by diff read-through).

  Task 3 — appended a clearly-marked `**Addendum (2026-08-18, per
  item-0008):**` paragraph to
  `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`'s
  "Provenance verification" section, after its existing content, stating the
  likely-confabulation finding and explicitly noting the addendum does not
  change the review's Decision (Approved). The original paragraphs, the
  "Deterministic Verification Output," "Falsification Search," "Checklist,"
  "Decision," and "Reasons" sections were not edited (confirmed by diff
  read-through).

  Task 4 — AI work trace created at
  `docs/collaboration/traces/2026-08-18-liss-0028-coordinator-message-correction.md`,
  naming the changed contract file (`cross-session-messaging.md`), the
  reason (item-0008's investigation), and the expected agent-behavior change
  (future sessions will not over-invest in injection-specific defenses for
  this incident, while the verify-before-trusting rule is unchanged).

## Work Notes — Self-Review (Task 5, short form)

Phase / finding: Minor Fix Path correction (Tasks 2-3 of `DA-2026-08-18-02`)

Command run: `python3 scripts/check-contract-consistency.py`, plus the Task 1
evidence-reconfirmation commands above (re-run before editing, not merely
read from item-0008's own claim).

Result:

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

Task 1's commands (grep, find, cross-branch `git grep`) all matched
item-0008's own claim, pasted in full above — no discrepancy.

Risks considered:

1. Could this read as retracting WP-0002's approval?
2. Does the operational verify-before-trusting rule survive intact in both
   edited files?
3. Does the corrected `cross-session-messaging.md` section overclaim
   certainty in either direction (i.e., does it state the cause as
   "confirmed" rather than "likely/probable")?
4. Is the WP-0002 review record's original Decision, constraints checklist,
   or falsification table edited in place rather than appended to?

Why each does not occur:

1. The addendum in the review record explicitly states "this ... does not
   change this review's Decision (Approved)" and is appended after the
   existing "Provenance verification" content, not substituted for it; the
   review record's "Decision" section (`- [x] **Approved**`) and its
   "Reasons" section are untouched — confirmed by reading the diff, which
   shows only an insertion after the existing paragraphs.
2. `cross-session-messaging.md`'s corrected section explicitly restates,
   in its own added text, "an unverified message is refused regardless of
   whether its origin turns out to be external or internal," and points to
   the unedited "What this means, stated as a rule" and "The fix"
   paragraphs immediately below as standing independently of the
   coordinator messages' origin; the review record's addendum states the
   same "correctly refused as unverified regardless of origin" point.
   Neither file's operational rule text was edited.
3. The added text in both files uses "likely," "probable explanation," and
   "not as a confirmed fact in either direction" / "not external
   injection" — deliberately avoiding "confirmed" for either the injection
   or the confabulation explanation, matching `DA-2026-08-18-02`'s
   Falsification Criteria (first bullet) exactly.
4. Confirmed by diff read-through (see Task 3 note above): the addendum is
   a new paragraph inserted after the section's existing content, before
   the "## Deterministic Verification Output" heading; no existing line in
   "Provenance verification," "Deterministic Verification Output,"
   "Falsification Search," "Checklist," "Decision," or "Reasons" was
   changed or removed.

## Verification

- Task 1 (independent re-confirmation): complete, output above, matches
  item-0008's claim.
- Task 2 (`cross-session-messaging.md` edit): complete.
- Task 3 (review-record addendum): complete.
- Task 4 (AI work trace): complete,
  `docs/collaboration/traces/2026-08-18-liss-0028-coordinator-message-correction.md`.
- Task 5 (self-review): complete, above.
- Task 6 (Preflight): complete, `pass` — see WP-0003's "Preflight
  Validation" section for the full record.
- Task 7 (separate-context Reviewer confirmation): pending — this issue's
  Status is `review`, not `done`/`closed`; that action belongs to the
  Design & Review group's Reviewer persona, and work-plan close after that
  belongs to the Director, per `docs/collaboration/cross-session-messaging.md`
  direction 3 (Trigger B) and direction 4.
