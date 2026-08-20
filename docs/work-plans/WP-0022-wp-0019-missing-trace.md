# Work Plan: WP-0019's missing AI work trace

## Goal

- Add one AI work trace under `docs/collaboration/traces/` documenting
  WP-0019's two agent-operating-contract-file edits
  (`docs/collaboration/design-review-perspectives.md`,
  `docs/collaboration/restoration-ledger.md`), satisfying
  `docs/collaboration/prompt-instruction-change-control.md`'s
  Traceability Rule and unblocking PR #21's "Check agent operating
  contract change traceability" CI step, which fails without one.

## Scope

- In:
  - One new trace file,
    `docs/collaboration/traces/2026-08-20-wp-0019-contract-file-edits.md`,
    using `docs/templates/ai-work-trace.md`, documenting the two already-
    completed contract-file edits.
- Out:
  - Any change to `docs/collaboration/design-review-perspectives.md`,
    `docs/collaboration/restoration-ledger.md`, or any of WP-0019's own
    23 archived/moved files — this is retroactive evidence, not a redo.
  - Re-litigating WP-0019's own Reviewer approval — it already covers
    the substance of these two edits; this trace only supplies the
    evidentiary artifact the Traceability Rule separately requires.
  - Any change to `docs/collaboration/prompt-instruction-change-control.md`
    itself (including whether `restoration-ledger.md` should be
    reclassified as a non-contract record — named as a real ambiguity in
    LISS-0061's own text, deliberately not resolved here).

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0061 | done | S | S | N/A | - | - | process/promote-item-0016 |

## Recommended Order

1. LISS-0061 (the only issue) — write the trace, verify the CI check's
   own condition is satisfied locally, confirm no regression.

## Current Next Issue

- Issue: LISS-0061
- Reason it is unblocked: no dependency beyond WP-0019 itself (already
  Director-closed); scope is fully settled by the design agreement; root
  cause already confirmed against the actual CI log and the actual CI
  step logic.
- Reopening request needed: no.

## Minor Fix Path

Not used formally (a new issue against a confirmed, CI-reproduced gap,
not a correction to previously accepted work), but shaped identically in
size and risk: planning size `S`, a single new file, one attempt
expected, no specification, ADR, port, data model, or architecture
boundary changed — and, per
`docs/collaboration/prompt-instruction-change-control.md`'s own text,
adding a trace file is explicitly *not itself* a contract change ("Files
under `docs/collaboration/traces/`... are records produced by following
the contract, not part of the contract itself. Changing one is not a
contract change and does not require its own trace").

## Preflight Validation

Run by the Implementation group on branch `wp-0022-execution` (created
from local branch `process/promote-item-0016` at commit `1c6a28a`) after
LISS-0061 landed (commit `d190dd7`) and was self-reviewed (short form, in
LISS-0061's own Work Notes). **Result: pass.** All three required checks
below were run for real against the actual committed tree; full output
pasted, not summarized.

1. `python3 scripts/check-contract-consistency.py` — full output:

   ```text
   $ python3 scripts/check-contract-consistency.py
   contract consistency: all checks passed
   ```

   (One regression was found and fixed before this pass: LISS-0061's
   `Status: done` was initially out of sync with this file's own Issue
   Graph row, which still read `ready`. Corrected in the Issue Graph table
   above, as part of this same Preflight step — not silently pre-fixed.)

2. `git diff --name-only main HEAD` (mirroring `.github/workflows/ci.yml`'s
   own "Check agent operating contract change traceability" step
   invocation, using `main` — this worktree's available local stand-in for
   the PR's actual base — against this branch's current head):

   ```text
   $ git diff --name-only main HEAD | grep '^docs/collaboration/traces/'
   docs/collaboration/traces/2026-08-20-wp-0019-contract-file-edits.md
   ```

   The new trace file's path is present, confirming the CI check's own
   `trace_added` condition is satisfied. Cross-checked against the
   `contract_changed` side of the same condition:

   ```text
   $ git diff --name-only main HEAD | grep -E '^docs/collaboration/[^/]+\.md$'
   docs/collaboration/design-review-perspectives.md
   docs/collaboration/restoration-ledger.md
   ```

   Both contract files this trace documents are indeed in the diff
   (`contract_changed=true`), and the new trace file is also in the diff
   (`trace_added=true`) — the exact combination the CI step requires and
   that this work plan exists to satisfy.

3. Confirmation, by direct reading, that the new trace's content
   accurately cites real commits, issues, and review records: performed
   directly by the Implementer while writing the trace (see
   `docs/collaboration/traces/2026-08-20-wp-0019-contract-file-edits.md`'s
   own Verification section) — `git show 81ddf2a` and `git show dfe5030`
   were read in full, and every factual claim in the trace (line numbers
   66/169 in `design-review-perspectives.md`; row counts 5+18=23 in
   `restoration-ledger.md`; the two source commit hashes) was independently
   reproduced by direct command output against the real committed tree,
   not copied unverified from LISS-0061's or WP-0019's own prose. Not a
   separate-context check (Preflight does not require context separation
   from the Implementer, only from the work-plan-level Reviewer that
   follows it) — the deterministic commands themselves are the check.

## Review Summary Packet

Filled in by the Implementation group once Preflight passes.

- **Scope**: added one AI work trace documenting WP-0019's two contract-
  file edits, satisfying the Traceability Rule; unblocks PR #21's second
  CI failure.
- **Current canonical documents**: none newly established or amended —
  this work plan adds only an Evidence-layer trace record, per
  `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
  Rule 1's own layer model.
- **Changed files**:
  `docs/collaboration/traces/2026-08-20-wp-0019-contract-file-edits.md`
  only.
- **Findings**: none opened or resolved by this work plan.
- **Disposition**: Preflight Validation passed (all 3 required checks, full
  output in this file's own "Preflight Validation" section above);
  LISS-0061 is `Status: done` with a short-form self-review record in its
  own Work Notes. Ready for the work-plan-level Reviewer pass in a separate
  context.
- **Remaining blockers**: none found. One non-blocking sync gap was found
  and corrected during this Preflight step itself, not silently pre-fixed:
  this file's own Issue Graph row for LISS-0061 still read `ready` after
  the issue's `Status` was set to `done`, which
  `scripts/check-contract-consistency.py`'s issue-status-sync check
  correctly flagged; corrected in the Issue Graph table above, and the
  checker now passes clean.
- **Verification result**: see this file's own "Preflight Validation"
  section above — all 3 required checks passed with full output pasted.
- **Next approval required**: evidence-sufficiency (does the trace
  accurately and completely document the two contract-file edits it
  claims to) — the one approval type most directly at stake for a pure
  evidentiary addition; specification-conformance, phase-correctness,
  and boundary-conformance are secondary since no specification, phase,
  or architecture boundary is touched.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-20-wp-0022-wp-0019-missing-trace-review.md`
— **Approved** (2026-08-20, Reviewer persona, Design & Review group
standing session, separate context from the Implementation-group subagent
session that executed LISS-0061 in its own worktree/branch). Every
factual claim in the new trace (cited line numbers, ledger row count,
commit hashes) was independently re-verified against the real committed
tree, and the CI check's own failure condition was independently
reproduced as resolved.

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

No `Type: review-finding` issues were opened. Notably, the Implementer
independently caught and self-corrected, during its own Preflight, the
same class of Issue Graph sync defect the Reviewer had to catch as
LISS-0060 during WP-0021's review — recorded in this work plan's own
Preflight Validation section.

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves — not
performed by the Design & Review group itself.

- Date:
- Result read:
- Next direction:
- New design agreement (if any):

## Risks

- A trace written without care could restate facts inaccurately (e.g.,
  citing the wrong commit hash or issue). Mitigated by LISS-0061's own
  Acceptance Notes naming the exact commits, issues, and review records
  to cite, and by this work plan's own Preflight requiring direct
  confirmation of the trace's factual accuracy, not only its existence.
- This work plan is the second, independent thing blocking PR #21's own
  merge (after item-0018's fix). Mitigated by its own narrow,
  already-confirmed scope — no open design question remains.

## Verification Plan

- `python3 scripts/check-contract-consistency.py` — no regression.
- `git diff --name-only` reproduction confirming the CI check's own
  condition is satisfied.
- Direct factual accuracy check of the new trace's content.
- Independent work-plan-level Reviewer approval, in a separate context.
