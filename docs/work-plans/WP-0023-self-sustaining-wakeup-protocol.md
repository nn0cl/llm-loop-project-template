# Work Plan: Check-and-spawn wake protocol (item-0020's settled decision)

## Goal

- Document the Director's settled check-and-spawn / queue-continuation
  wake protocol (recorded verbatim in `docs/issues/LISS-0062-...md`'s
  Work Notes) precisely in ADR 0016 and
  `docs/collaboration/cross-session-messaging.md`, replacing the current
  vague "standing"/"autonomous" language that never specified an actual
  wake-up mechanism.

## Scope

- In:
  - A new `Rule 7` in ADR 0016's Decision section, plus a Status-section
    sentence and two new Enforcement bullets, per LISS-0063's own exact
    text.
  - New/updated content in `docs/collaboration/cross-session-messaging.md`
    (directions 1 and 2, plus a new "Queue continuation and
    resume-before-duplicate-spawn" section), per LISS-0063's own exact
    text.
  - The mandatory AI work trace for both contract-file edits.
- Out:
  - Any change to ADR 0016 Rules 1-6 or any other existing content in
    either file beyond what LISS-0063 names.
  - Any change to ADR 0020, `docs/collaboration/prompt-instruction-change-control.md`,
    or any other contract file.
  - Any actual code/script implementation — this is a docs-only protocol
    statement; the protocol itself is executed by whichever session
    (Backlog thread, Design & Review, Implementation) performs the
    `ListAgents`/`SendMessage`/Agent-tool actions it describes, not by a
    new script this work plan would author. (Confirmed during planning:
    no existing script or helper in `scripts/` currently orchestrates
    cross-session spawning/messaging — that is done by whichever session
    is acting, directly via its own tool calls, so there is no code
    surface for this work plan to add a helper to; if the Implementer
    finds otherwise during execution, that is a scope question to flag,
    not resolve unilaterally.)
  - Actually creating any scheduled task or `.claude/settings.json` hook
    — the spike's own Selection (case-0003) explicitly avoided both
    (recurring cost, untested capability); the Director's settled
    decision uses only already-confirmed-working tools.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0063 | done | M | M | N/A | LISS-0062 | - | process/promote-item-0020 |

## Recommended Order

1. LISS-0063 (the only issue) — apply both contract-file edits, write the
   trace, verify.

## Current Next Issue

- Issue: LISS-0063
- Reason it is unblocked: its only dependency, LISS-0062, is `Status: done`
  (Director's settled decision recorded there); every sentence to insert
  is specified verbatim in LISS-0063's own Acceptance Notes.
- Reopening request needed: no.

## Minor Fix Path

Not applicable — both edited files are agent operating contract files
under ADR 0006; per `docs/collaboration/prompt-instruction-change-control.md`
and `CLAUDE.md`'s own "Preflight Validation" section, a contract-file
change is never self-reviewed and always requires a separate-context
Reviewer plus a trace, regardless of size or Director-level urgency.

## Preflight Validation

Recorded by the Implementation group, LISS-0063 self-reviewed and complete
(commit `6125931` on `wp-0023-execution`, branched from
`process/promote-item-0020` at `954abf1`). Result: **pass**.

1. `python3 scripts/check-contract-consistency.py` — full output:

   ```text
   $ python3 scripts/check-contract-consistency.py
   contract consistency: all checks passed
   ```

   No regression.

2. `grep -n "Rule 7" docs/architecture/adr/0016-...md` and equivalent
   confirmation for `cross-session-messaging.md`'s new/updated sections:

   ```text
   $ grep -n "Rule 7" docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md
   24:Rule 7 (the check-and-spawn wake protocol) is covered by a
   235:### Rule 7 — Check-and-spawn wake protocol
   375:  (Rule 7) — including a role recovering from a session that just failed
   378:  already-approved-but-unstarted work it did not check for (Rule 7,

   $ grep -n "Queue continuation and resume-before-duplicate-spawn" docs/collaboration/cross-session-messaging.md
   259:## Queue continuation and resume-before-duplicate-spawn (ADR 0016 Rule 7)

   $ grep -n "Wake mechanic" docs/collaboration/cross-session-messaging.md
   170:- **Wake mechanic**: per ADR 0016 Rule 7, the Design & Review group

   $ grep -n "required, per ADR 0016 Rule 7" docs/collaboration/cross-session-messaging.md
   145:- **Message**: required, per ADR 0016 Rule 7. On approving a backlog
   ```

   Every piece of LISS-0063's own required content landed with the exact
   headings/labels specified.

3. `git diff` scope check — confined to the two contract files, the new
   trace file, and this work plan's own tracking files (LISS-0063,
   WP-0023 itself):

   ```text
   $ git diff process/promote-item-0020...HEAD --stat
    ...wo-group-topology-and-backlog-gated-autonomy.md |  70 ++++++
    docs/collaboration/cross-session-messaging.md      |  59 ++++-
    .../2026-08-20-check-and-spawn-wake-protocol.md    | 256 +++++++++++++++++++++
    .../LISS-0063-check-and-spawn-wake-protocol.md     |  66 +++++-
    4 files changed, 442 insertions(+), 9 deletions(-)
   ```

   Confirmed: only ADR 0016, `cross-session-messaging.md`, the new trace,
   and `LISS-0063-...md` changed. This file (WP-0023) is edited in a
   separate, subsequent commit for this Preflight/Review Summary Packet
   section only, per the covering design agreement's own sequencing.

4. Confirmation the new trace file
   (`docs/collaboration/traces/2026-08-20-check-and-spawn-wake-protocol.md`)
   exists and states which files changed, why, and what behavior changes —
   confirmed by direct reading: its "Changed Files" section names both
   contract files and states the reason (closing the gap named in
   `docs/backlog/item-0020-...md` and its spike, per the Director's settled
   decision in `docs/issues/LISS-0062-...md`) and the expected behavior
   change (a spawning party checks `ListAgents` before spawning and resumes
   a surviving worktree/branch instead of duplicating it; a standing loop
   checks its own queue before going idle).

**Next action**: submit to the work-plan-level Reviewer pass, in a separate
context, per ADR 0006's contract-file governance.

## Review Summary Packet

Filled in by the Implementation group once Preflight passes.

- **Scope**: added ADR 0016 Rule 7 and corresponding
  `cross-session-messaging.md` updates, documenting the Director's
  settled check-and-spawn wake protocol; no code or new automation
  surface added.
- **Current canonical documents**: ADR 0016 and
  `docs/collaboration/cross-session-messaging.md` are amended in place
  (both already Canonical/Accepted); this work plan does not supersede
  either, only completes a previously-acknowledged gap in both.
- **Changed files**:
  `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`,
  `docs/collaboration/cross-session-messaging.md`,
  `docs/collaboration/traces/2026-08-20-check-and-spawn-wake-protocol.md`.
- **Findings**: none opened or resolved by this work plan.
- **Disposition**: Preflight **pass**. Both contract-file edits landed
  verbatim per LISS-0063's own Acceptance Notes, confirmed by direct
  `git diff` comparison; no existing sentence in either file was altered
  or removed; the mandatory trace exists and states all three required
  facts. Ready for submission to the work-plan-level Reviewer pass.
- **Remaining blockers**: none found.
- **Verification result**: see this file's own "Preflight Validation"
  section above, populated with full command output (all four required
  checks, `pass`).
- **Next approval required**: boundary-conformance (did the edit land
  exactly the text LISS-0063 specifies, touching nothing else) and
  evidence-sufficiency (does the trace correctly document the two
  contract-file edits) — the two approval types most directly at stake
  for a fully-specified contract-file documentation change;
  specification-conformance and phase-correctness are secondary since no
  specification or AT-TDD phase content is touched.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-20-wp-0023-self-sustaining-wakeup-protocol-review.md`
— **Approved** (2026-08-20, Reviewer persona, Design & Review group
standing session, separate context from the Implementation-group subagent
session that executed LISS-0063 in its own worktree/branch). Every
inserted sentence in ADR 0016 and `cross-session-messaging.md` was
independently confirmed, by line-by-line diff comparison, to match
LISS-0063's own verbatim specification exactly, and Rules 1-6 were
independently confirmed provably untouched (zero deletion lines in the
ADR 0016 diff).

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
| LISS-0064 | closed | The Reviewer's own independent re-verification (not trusting the Implementer's pasted Preflight output) found `check_issue_status_sync` genuinely failing against the actual committed state — this work plan's own Issue Graph row for LISS-0063 was never synced from `ready` to `done`. Third occurrence of this exact defect class this session (WP-0021: `LISS-0060`; WP-0022: self-caught). Routed via the Minor Fix Path back to the Implementation group; corrected in commit `4c4d861`; independently re-confirmed clean by a fresh reproduction. |

One finding was opened and resolved during this review.

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves — not performed
by the Design & Review group itself.

- Date: 2026-08-20
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-20-wp-0023-self-sustaining-wakeup-protocol-review.md`,
  Approved — all three constraints satisfied) via the Backlog thread,
  which independently re-verified from a fresh, isolated
  `git worktree add --detach` checkout of `process/promote-item-0020`
  (tip `d6690fc`) before presenting this close: a clean
  `check-contract-consistency.py` run, ADR 0016 Rule 7 and
  `cross-session-messaging.md`'s new "Queue continuation and
  resume-before-duplicate-spawn" section both present by direct `grep`,
  LISS-0062/LISS-0063 at `Status: done` and LISS-0064 at
  `Status: closed`, WP-0023's own Issue Graph row correctly showing
  LISS-0063 as `done`, and a scope diff against `main` confined to the
  12 expected files (no unrelated file touched).
- Next direction: closed with "承認。続けて" (approved; proceed) —
  merging `process/promote-item-0020` into `main` and pushing now.
- New design agreement (if any): none opened by this close. One
  non-blocking follow-up was flagged during review (not acted on): the
  `to: "general-purpose"` → `to: "main"` grandchild-routing nuance
  observed during this work plan's own execution is worth a future,
  separately-governed addition to `cross-session-messaging.md`'s
  documented-failure-modes section — left for a later backlog item, not
  this close.

## Risks

- A contract-file edit that drifts from LISS-0063's own exact specified
  text (even in ways that seem like harmless paraphrasing) would not
  faithfully carry the Director's own decision forward. Mitigated by
  LISS-0063 giving the exact insertion text verbatim, and by this work
  plan's own Preflight requiring a direct `grep`-based confirmation of
  each piece landing, not only a general checker pass.
- The protocol this work plan documents is not itself enforced by any
  new deterministic check (no script verifies a spawning party actually
  called `ListAgents` first) — it is a documented rule for sessions to
  follow, the same category as most of this repository's own process
  rules. Not a defect in this work plan; named here as an honest
  limitation, consistent with the spike's own finding that no automated
  enforcement mechanism was investigated or adopted.

## Verification Plan

- `python3 scripts/check-contract-consistency.py` after the issue lands.
- Targeted `grep` confirmation that every piece of LISS-0063's own
  required content landed verbatim.
- Confirmation the mandatory trace exists and is complete.
- Independent work-plan-level Reviewer approval, in a separate context.
