# Backlog item: item-0019-wp-0019-missing-trace

## Metadata

- Item ID: item-0019
- Title: Add the missing AI work trace for WP-0019's contract-file edits
- Status: promoted
- Created: 2026-08-20
- Updated: 2026-08-20
- Priority hint: high
- Suggested planning size: S
- Owner/agent (optional): unassigned

## Summary

PR #21's CI ("Check agent operating contract change traceability") fails:
the PR's total diff modifies two ADR-0006 contract files —
`docs/collaboration/design-review-perspectives.md` (reference-path updates
for archived files) and `docs/collaboration/restoration-ledger.md` (23 new
rows added by WP-0019's archival) — but adds no new file under
`docs/collaboration/traces/`. The CI check is correct: WP-0019's own
LISS-0056/LISS-0057 issue files confirm no new trace was created for these
two edits (only old, now-archived traces were moved, and moving a file is
not creating a trace for new work). Per
`docs/collaboration/prompt-instruction-change-control.md`'s Traceability
Rule, this is required "even for small wording changes to a contract
file" — the tiny-documentation-only-change exception does not apply to
files on the contract list.

This is item-0018's PR #21 all over again in shape (a genuine post-close CI
gap in already-Director-closed WP-0019 content, same as item-0014 was for
WP-0014) — a second, independent gap in the same work plan, not a
duplicate of item-0018.

## Why it might matter

Blocks PR #21's merge (again, after item-0018's fix already landed on the
same branch). Also a real process gap worth naming: WP-0019's own
work-plan-level Reviewer pass approved the work plan without catching this
ADR-0006 traceability requirement — worth a note in
`docs/collaboration/design-review-perspectives.md` itself (once its trace
exists) about explicitly checking the Traceability Rule whenever a
contract file is touched, even inside an otherwise-unrelated work plan
like an archival batch.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes — one new trace file
  (or two, if the two edits are judged separate enough to need their own),
  no code change.
- Boundaries or non-goals:
  - Do not touch the archival content itself (the 23 moved files, the
    ledger rows' substance) — only add the missing trace documenting the
    two contract-file edits.
  - One trace covering both edits (they're both part of the same WP-0019
    archival work) is likely sufficient — Design & Review's call, per the
    same judgment `docs/collaboration/traces/` entries elsewhere in this
    session have used for multi-file single-purpose edits.

## Uncertainty

- [x] Spec can be written now — reproducible via PR #21's own CI failure,
      root cause identified precisely.
- [ ] Spike required first
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none — related:
  `docs/collaboration/prompt-instruction-change-control.md`,
  `docs/issues/LISS-0056-archive-wp-0001-under-adr-0020.md`,
  `docs/issues/LISS-0057-archive-wp-0002-under-adr-0020.md`, PR #21 CI run
  (https://github.com/nn0cl/llm-loop-project-template/actions/runs/32342134917)

## Promotion notes

- Date: 2026-08-20
- Decision: Promoted, in the Backlog-layer thread, immediately at capture.
  Per ADR 0016 Rule 2, Design & Review proceeds autonomously from here.
- Reason: Blocking PR #21's merge (second, independent gap after
  item-0018); narrow, well-evidenced; ready to run.
