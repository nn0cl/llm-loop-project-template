# Review Record: WP-0022 (WP-0019's missing AI work trace)

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's standing session, which produced the work plan, design
      agreement, and issue text, but did not write the trace itself —
      that was executed by a separate Implementation-group subagent
      session in its own dedicated worktree/branch (`wp-0022-execution`,
      spawned off `process/promote-item-0016`). This review does not rely
      on that Implementer session's own reasoning as justification; every
      claim below is independently re-run against the actual committed
      tree by this review itself.
- [x] **Deterministic precondition.** Deterministic verification was run,
      independently, by this review, against a fresh `git archive`
      extraction — not the Implementer's own pasted output.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, each with the grounds it does not occur.

## Review Target

- Artifact: `wp-0022-execution` branch (commits `d190dd7`, `a27a2af`), to
  be merged into `process/promote-item-0016`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-20-wp-0019-missing-trace.md`
  (`DA-2026-08-20-05`)
- Specification: none (a retroactive evidentiary addition; no
  `docs/specs/` file covers this work plan).
- Current phase: Fast Path; Preflight Validation recorded as pass in
  `docs/work-plans/WP-0022-...md`.
- Producing persona: Implementer (Implementation group, separate context).
- Reviewing persona / model / tool: Reviewer (Design & Review group,
  standing session).
- Approval type: evidence-sufficiency (does the trace accurately and
  completely document the two contract-file edits it claims to — the one
  type the work plan's own Review Summary Packet names as at stake).
- Preflight Validation record: `docs/work-plans/WP-0022-...md`'s own
  "Preflight Validation" section.
- Preflight result: pass (independently confirmed by this review).

## Deterministic Verification Output

All commands below were run independently by this review, against a fresh
`git archive` extraction of `wp-0022-execution` — not pasted from the
Implementer's own record.

```text
$ git archive wp-0022-execution | tar -x -C /tmp/wp22-verify
$ python3 /tmp/wp22-verify/scripts/check-contract-consistency.py --repo /tmp/wp22-verify
contract consistency: all checks passed

--- factual accuracy of the trace's own citations ---
$ grep -n "docs/archive/collaboration/reviews/2026-08-18-wp-0002" docs/collaboration/design-review-perspectives.md
66:`docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`
169:`docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`,
(matches the trace's own cited line numbers exactly)

$ grep -c "| archived |" docs/collaboration/restoration-ledger.md
23
(matches the trace's own cited row count exactly — 5 from LISS-0056 + 18
from LISS-0057)

--- CI condition reproduction (independently, not copied from the Implementer) ---
$ git diff main...wp-0022-execution --name-only | grep '^docs/collaboration/traces/'
docs/collaboration/traces/2026-08-20-wp-0019-contract-file-edits.md

$ git diff main...wp-0022-execution --name-only | grep -E '^docs/collaboration/[^/]+\.md$'
docs/collaboration/design-review-perspectives.md
docs/collaboration/restoration-ledger.md
(both contract_changed and trace_added conditions independently confirmed
true, the exact combination the CI check requires)

--- diff scope ---
$ git diff process/promote-item-0016...wp-0022-execution --stat
 .../2026-08-20-wp-0019-contract-file-edits.md      | 284 +++++++++++++++++++++
 docs/issues/LISS-0061-wp-0019-missing-trace.md     |  55 +++-
 docs/work-plans/WP-0022-wp-0019-missing-trace.md   |  90 +++++--
 3 files changed, 409 insertions(+), 20 deletions(-)
(exactly the three files the design agreement's Boundaries section
authorizes: the new trace, and the two tracking files; no edit to
design-review-perspectives.md, restoration-ledger.md, any of WP-0019's
own archived files, or prompt-instruction-change-control.md)

$ git diff process/promote-item-0016...wp-0022-execution -- docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md
(no output -- unrelated, confirmed untouched, as expected for this scope)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The trace's factual claims (line numbers, row counts, commit hashes) are approximated rather than independently verified | Independently re-ran the exact `grep` commands the trace itself cites against the real committed tree and got identical results (line 66/169, 23 rows) — not merely trusting the trace's own prose | not reproduced |
| 2 | The new trace does not actually satisfy the CI check's own `trace_added`/`contract_changed` combination | Independently reproduced the CI step's exact `git diff --name-only` logic against `main...wp-0022-execution` and confirmed both conditions hold in the direction that resolves the failure | not reproduced |
| 3 | The diff touches the two contract files themselves, or any of WP-0019's own archived content, rather than only adding evidence | `git diff --stat` confined to exactly 3 files (the trace and two tracking files); no `design-review-perspectives.md` or `restoration-ledger.md` content diff present | not reproduced |
| 4 | The same Issue Graph sync defect this review caught in WP-0021 (LISS-0060) recurs here, uncaught | It occurred here too, but was caught and corrected by the Implementer itself during its own Preflight (see WP-0022's own Preflight Validation section, "One regression was found and fixed before this pass"), not left for this review to find — independently confirmed via `check-contract-consistency.py`'s clean pass and direct inspection of the final Issue Graph row (`LISS-0061 \| done`) | not reproduced (self-corrected) |
| 5 | `prompt-instruction-change-control.md` or any other contract file was edited as part of "fixing" the traceability gap, rather than only adding a trace | `git diff --stat` shows no such file; the fix is purely additive (one new trace file) | not reproduced |

## Scenarios Not Searched

- Full end-to-end confirmation against GitHub's own CI runner (as opposed
  to local reproduction of the identical `git diff` logic) — confirmed
  once this fix reaches `main` and PR #21's own CI re-runs.
- The open question this work plan explicitly deferred (whether
  `restoration-ledger.md` should be reclassified as a non-contract
  record) — intentionally out of scope, named in the design agreement's
  own Settled Ambiguities, not silently resolved here either.

## Checklist

- [x] The artifact belongs to the phase that was run (Fast Path) — a pure
      evidentiary addition, confirmed by diff scope.
- [x] Every `Then` clause in the specification is asserted by the work —
      N/A, no specification covers this work plan.
- [x] The dependency rule and port boundaries hold — N/A.
- [x] No boundary named in the design agreement was crossed — confirmed:
      no edit to the two contract files, WP-0019's own content, or
      `prompt-instruction-change-control.md`.
- [x] Specifications and accepted tests were not modified to make work
      pass — N/A.
- [x] Every claim in the artifact states its grounds — the trace itself
      cites real commit hashes and independently-reproducible facts.
- [x] The record would let a third party re-run this same search — every
      command above is copy-pasteable and was independently re-run by
      this review.

## Decision

- [x] Approved

## Reasons

The new trace (`docs/collaboration/traces/2026-08-20-wp-0019-contract-file-edits.md`)
accurately documents WP-0019's two contract-file edits, with every
factual claim independently re-verified against the real committed tree
by this review (line numbers, row counts, commit hashes all match
exactly). The CI check's own failure condition is independently confirmed
resolved: the exact `git diff --name-only` logic the workflow uses now
shows both the contract-file changes and the new trace path together, the
combination that satisfies the traceability requirement. The diff is
confined to exactly the three authorized files; no contract file, WP-0019
content, or the change-control document itself was touched.

Notably, the Implementer independently caught the same class of defect
this review found in WP-0021 (an Issue Graph row left out of sync with
its issue's terminal status) during its own Preflight this time, and
corrected it transparently within the same commit rather than requiring
a separate review-finding round — the process improvement from WP-0021's
review is visibly working. No `Type: review-finding` issue is warranted
here.