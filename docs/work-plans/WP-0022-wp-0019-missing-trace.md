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
| LISS-0061 | ready | S | S | N/A | - | - | process/promote-item-0016 |

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

To be recorded here by the Implementation group once LISS-0061 is
self-reviewed and complete, before requesting the work-plan-level
Reviewer pass. Required checks, at minimum:

1. `python3 scripts/check-contract-consistency.py` — full output,
   confirming no regression.
2. `git diff --name-only <base> <head>` (mirroring
   `.github/workflows/ci.yml`'s own "Check agent operating contract
   change traceability" step invocation, using the same base/head this
   branch will actually merge against) shows the new trace file's path
   present — confirming the CI check's own `trace_added` condition is
   satisfied.
3. Confirmation, by direct reading, that the new trace's content
   accurately cites real commits, issues, and review records (not
   invented or approximate).

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
- **Disposition**: <filled in at Preflight>
- **Remaining blockers**: none expected; state any found.
- **Verification result**: <pointer to this file's own Preflight
  Validation section, populated above>.
- **Next approval required**: evidence-sufficiency (does the trace
  accurately and completely document the two contract-file edits it
  claims to) — the one approval type most directly at stake for a pure
  evidentiary addition; specification-conformance, phase-correctness,
  and boundary-conformance are secondary since no specification, phase,
  or architecture boundary is touched.

## Work-Plan Review

Reviewer's approval record: <link, filled in after the Reviewer pass>

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

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
