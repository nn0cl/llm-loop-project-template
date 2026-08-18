# Work Plan: Correct the "coordinator" Confabulation Record

## Goal

- Correct `docs/collaboration/cross-session-messaging.md`'s "Confirmed
  failure mode" section and the WP-0002 review record's "Provenance
  verification" section to state that the four unverified in-band
  "coordinator" messages received during WP-0002 were most likely
  model-side confabulation, not confirmed external injection — per
  `docs/backlog/item-0008-coordinator-message-hallucination-correction.md`
  and `docs/collaboration/agreements/2026-08-18-coordinator-message-correction.md`
  (`DA-2026-08-18-02`).

## Scope

- In: the two file edits above, an AI work trace for the contract-file
  change, self-review, Preflight, and separate-context Reviewer
  confirmation.
- Out: any change to `SendMessage`/`ListAgents` usage rules; re-litigating
  WP-0002's Decision; any file beyond the two named above.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0028 | ready | S | S | - | - | - | process/coordinator-message-correction |

## Plan-Owned Bug Records

None.

## AI Planning Records

None required — planning size `S`, first attempt.

## Recommended Order

1. LISS-0028 (single issue, Minor Fix Path).

## Current Next Issue

- Issue: LISS-0028
- Reason it is unblocked: no dependencies; design agreement `DA-2026-08-18-02`
  covers it fully.
- Reopening request needed: no.

## Minor Fix Path

Applies to LISS-0028 in full: planning size `S`, preserves the accepted
WP-0002 Decision (adds a corrective addendum, does not retract it), changes
no specification, ADR, port, data model, dependency, or architecture
boundary, and is expected to finish in one attempt. Per CLAUDE.md, this
still requires: a compact design note (this work plan plus
`DA-2026-08-18-02`), the minimum correction (self-reviewed), deterministic
verification, and separate Reviewer confirmation — and, because
`cross-session-messaging.md` is an ADR-0006 contract file, its own AI work
trace and a separate-context Reviewer pass regardless of Minor Fix Path use.

## Preflight Validation

- Result: pass
- Checks and command output:
  ```text
  $ python3 scripts/check-contract-consistency.py
  contract consistency: all checks passed
  ```
  Also re-run for Task 1 (independent evidence reconfirmation, per
  `DA-2026-08-18-02`'s Plan table), pasted in full in LISS-0028's Work Notes:
  a repo-wide `grep -rni "coordinator"` (working tree), a search for
  `*settings*.json` and `*hook*` files, and a `git grep -il "coordinator"`
  sweep across every local and remote-tracking branch — all consistent with
  `docs/backlog/item-0008-*.md`'s own claim; no discrepancy found.
- Scope result: pass — only `docs/collaboration/cross-session-messaging.md`'s
  "Confirmed failure mode" section and
  `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`'s
  "Provenance verification" section (addendum only) were touched, matching
  this work plan's Scope; no other section of either file, and no other
  file, was edited.
- Next action: submit to the Design & Review group's separate-context
  Reviewer pass (direction 3, Trigger B, per
  `docs/collaboration/cross-session-messaging.md`).

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: _pending Director action_
- Result read:
- Next direction:
- New design agreement (if any):

## Risks

- The correction could be misread as retracting WP-0002's approval instead
  of only correcting the stated likely cause of the coordinator messages;
  mitigated by requiring the addendum to be clearly marked as added-after,
  not an edit to the original Decision.
- `cross-session-messaging.md` is read during design intake by every future
  Design & Review and Implementation session; an imprecise correction here
  propagates. Mitigated by the separate-context Reviewer pass required
  regardless of Minor Fix Path size.

## Verification Plan

- Repo-wide `coordinator` grep (working tree and all branches) and
  `.claude/settings*.json` / `*hook*` file search, re-run independently.
- `scripts/check-contract-consistency.py`.
- Trace file existence check under `docs/collaboration/traces/`.
- Separate-context Reviewer approval.
