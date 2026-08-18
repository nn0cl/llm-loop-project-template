# Work Plan: Standing Two-Group Loop over send_message

## Goal

- Introduce a standing two-group session topology — a Design & Review group
  (Planner, Specifier, Reviewer, Arbiter) and an Implementation group
  (Implementer) — connected via the `SendMessage` / `ListAgents` tools, with
  the Director's design-phase gate relocated to `docs/backlog/` item
  approval and the loop's two human gates (design agreement, work-plan
  close) made non-blocking across concurrently in-flight work plans. This is
  a process/governance change only: no application code changes.

## Scope

- In:
  - A new ADR (0016) recording the topology, the backlog-level gate, the
    non-blocking multi-work-plan behavior, and the Director intervention
    channel.
  - Updates to `docs/collaboration/personas.md`, `ai-human-scheme.md`,
    `session-start-and-resume.md`, `branch-commit-pr-discipline.md`,
    `design-agreement.md`, a new `cross-session-messaging.md`, and
    `docs/backlog/README.md`.
- Out:
  - Any automation script or launcher for starting the two groups (deferred;
    see the covering design agreement's Deferred Questions).
  - Changes to the Reviewer's three constraints, the Implementer's
    self-review requirements, the three invariants, or ADR 0006 itself.
  - Any application-level specification or code.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0019 | review | M | M | AIP-0019-001 | - | LISS-0020..0026 | process/adr-0016-two-group-topology |
| LISS-0020 | review | S | S | - | LISS-0019 | - | process/personas-group-mapping |
| LISS-0021 | review | M | M | AIP-0021-001 | LISS-0019 | - | process/ai-human-scheme-loop-update |
| LISS-0022 | review | M | M | AIP-0022-001 | LISS-0019 | - | process/cross-session-messaging-protocol |
| LISS-0023 | review | S | S | - | LISS-0019 | - | process/session-start-standing-pair |
| LISS-0024 | review | S | S | - | LISS-0019 | - | process/implementation-group-worktree-rule |
| LISS-0025 | review | M | M | AIP-0025-001 | LISS-0019 | - | process/design-agreement-backlog-gate |
| LISS-0026 | review | S | S | - | LISS-0019 | - | process/backlog-readme-bulk-gate |

## Plan-Owned Bug Records

None.

## AI Planning Records

See each issue's own `AI Planning Records` section (LISS-0019, LISS-0021,
LISS-0022, LISS-0025). LISS-0020, LISS-0023, LISS-0024, LISS-0026 are
planning size `S` and do not require one at this stage.

## Recommended Order

1. LISS-0019 (ADR 0016) — everything else reads its Decision section.
2. LISS-0020, LISS-0021, LISS-0022 in any order (each touches a distinct
   file; LISS-0022 is the largest surface).
3. LISS-0023, LISS-0024 in any order.
4. LISS-0025 (depends conceptually on LISS-0021's loop-diagram wording being
   stable, so sequence it after LISS-0021 even though the formal dependency
   graph only names LISS-0019).
5. LISS-0026 last, since it cross-references the updated
   `design-agreement.md` (LISS-0025) and ADR 0016 (LISS-0019).

## Current Next Issue

- Issue: none — all eight issues (LISS-0019 through LISS-0026) are
  self-reviewed and complete. Next step is Preflight Validation (below),
  then the work-plan-level Reviewer pass (Task 10), which this
  Implementation-group session does not perform itself.
- Reopening request needed: no.

## Minor Fix Path

Not applicable to the initial execution of this work plan (every issue here
is Architecture Path, several touching contract files under ADR 0006). The
Minor Fix Path may apply later to small corrections against this work plan's
accepted result.

## Preflight Validation

- Result: **pass** (2026-08-18, Implementer, Implementation group, first
  standing session), scoped to this work plan's own In-scope documents.
- Checks and command output:

  1. `python3 scripts/check-contract-consistency.py`, run once as a
     baseline before any issue landed, once more after each issue, and
     once more as the final Preflight run:

     ```text
     $ python3 scripts/check-contract-consistency.py
     contract consistency: all checks passed
     ```

     (Baseline, before LISS-0020, showed exactly the 2 expected failures —
     both references to `docs/collaboration/cross-session-messaging.md`,
     which did not yet exist — matching what LISS-0019's own self-review
     predicted. LISS-0022 creating that file resolved both, plus 2 more
     that LISS-0021's own new cross-references to the same file had added
     in the interim. Every run from LISS-0022 onward shows zero failures.)

  2. Targeted `grep` sweep for the superseded ADR 0001/0014 phrasing across
     all documents this work plan touches, plus a full-repository sweep as
     a wider check:

     ```text
     $ grep -rn "does not start without" --include="*.md" . | grep -v "/traces/\|/reviews/"
     docs/collaboration/design-agreement.md:164:This specific work plan's own successor does not start without this — the
     docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md:13:  clause 5's "the next work plan does not start without [close]" as applied
     docs/at-tdd/process.md:198:   work plan does not start without this.
     docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md:13:does not start without [close]") as applied *across concurrently in-flight
     docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md:92:   optional reading: the next work plan does not start without it. It
     docs/issues/LISS-0019-adr-0016-two-group-topology.md:41:     0014 clause 5's "the next work plan does not start without [close]"
     docs/issues/LISS-0019-adr-0016-two-group-topology.md:251:     found the "next work plan does not start without it" phrase actually
     docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md:13:("the next work plan does not start without [close]") as it applies across
     docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md:235:| ADR 0014, Decision, clause 5 (blocking clause) | ... | Rule 3: does not block *other, concurrently in-flight* work plans. ... |
     docs/work-plans/WP-0002-two-group-send-message-loop.md:140:  work plan does not start without [close]") across all updated documents,
     docs/issues/LISS-0025-design-agreement-backlog-gate-reconciliation.md:120:  phrasing ("the next work plan does not start without [close]") found
     ```

     Two genuine hits required correction during this Preflight pass (both
     already fixed, see LISS-0021's and LISS-0025's Work Notes for the
     detail): `design-agreement.md`'s "Closing a work plan" closing
     paragraph, and `ai-human-scheme.md`'s "Roles > Director >
     Responsibilities" list, both of which stated the pre-ADR-0016 model
     with no qualification. Both now cite ADR 0016 Rule 2 or 3 by name and
     scope the statement correctly. All ADR 0014/0016 hits themselves are
     the documents *stating* the supersession, not describing it as still
     current. `docs/at-tdd/process.md:198` is a genuine unqualified
     restatement of the same pre-ADR-0016 model — **but that file is not
     in this work plan's Scope** (it is not one of the seven documents
     `DA-2026-08-18-01` and WP-0002's Scope name). Per the hard boundary
     against silently resolving out-of-scope ambiguity, this was not
     edited here; see "Scope result" below.

  3. Confirmed each of the six contract-file issues (LISS-0020 through
     LISS-0025) has an accompanying trace under `docs/collaboration/traces/`:

     ```text
     $ ls docs/collaboration/traces/2026-08-18-liss-002*.md
     docs/collaboration/traces/2026-08-18-liss-0020-personas-group-mapping.md
     docs/collaboration/traces/2026-08-18-liss-0021-ai-human-scheme-loop-update.md
     docs/collaboration/traces/2026-08-18-liss-0022-cross-session-messaging-protocol.md
     docs/collaboration/traces/2026-08-18-liss-0023-session-start-standing-pair.md
     docs/collaboration/traces/2026-08-18-liss-0024-implementation-group-worktree-rule.md
     docs/collaboration/traces/2026-08-18-liss-0025-design-agreement-backlog-gate-reconciliation.md
     ```

     All six present. LISS-0026 (`docs/backlog/README.md`) has none by
     design — not an ADR 0006 contract file; stated explicitly in its own
     Work Notes.

  4. `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
     `.grok/rules/*.md`, and `.cursor/rules/*.mdc` mirror-consistency check:
     **not applicable to this work plan's changes.** This work plan does not
     touch any shared phase, dependency, or read-order rule that those
     mirror files restate — it adds session-group topology, a new handoff
     protocol document, and a worktree rule, none of which those five
     mirror files currently describe at all (confirmed by `grep -rln
     "session group\|two-group\|cross-session-messaging"
     AGENTS.md CLAUDE.md .github/copilot-instructions.md .grok/rules/
     .cursor/rules/` returning no matches). No mirror-consistency
     regression is possible from content those files do not mention.

- Scope result: **pass, within WP-0002's own stated Scope.** One
  out-of-scope finding surfaced and is *not* resolved by this Preflight
  pass: `docs/at-tdd/process.md` (an ADR 0006 contract file per its own
  listing) line 197-198 states the pre-ADR-0016 blocking model
  unqualified, the same defect this work plan fixed in
  `design-agreement.md` and `ai-human-scheme.md` — but `process.md` is not
  named in `DA-2026-08-18-01`'s Scope or WP-0002's Scope, so editing it
  here would exceed this work plan's authorized boundary. This is recorded
  as a finding for the Design & Review group / Director to decide how to
  address (a follow-up backlog item, or a scope amendment to this work
  plan via reopening), not guessed past silently.
- Next action: submit to the work-plan-level Reviewer (Task 10), per
  `docs/collaboration/cross-session-messaging.md` direction 3 (Trigger B) —
  this Implementation-group session sends the handoff message naming this
  Preflight section and requests the Reviewer pass; it does not attempt
  the Reviewer pass itself.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`
— **Approved** (2026-08-18, Reviewer persona, Design & Review group standing
session, separate context from the Implementation group session that
produced LISS-0020–0026).

Six of the eight issues (LISS-0020, 0021, 0022, 0023, 0024, 0025) change
agent operating contract files under ADR 0006 and therefore require the
Reviewer's approval to explicitly address each contract-file change (reason,
trace presence, cross-file consistency), not only the work plan's
specification conformance in general — mirroring
`docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`'s
Task 4 precedent, where one work-plan-level Reviewer pass covered
propagation across nine contract files. The review record's Falsification
Search table addresses each of the six individually.

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

No `Type: review-finding` issues were opened — the review found no defect
requiring correction. Two out-of-scope observations (not review findings
against this work plan) are carried to the Director in this session's
report rather than resolved here: `docs/at-tdd/process.md`'s unqualified
pre-ADR-0016 phrasing (already noted in this work plan's own Preflight
section above), and a nested-`isolation: worktree`-spawn environment
interaction noted in the review record's "Scenarios Not Searched" section.

## Work-Plan Close

- Date: pending
- Result read: pending
- Next direction: pending
- New design agreement (if any): pending

## Risks

- Two prior ADRs (0001, 0014) are superseded on more than one clause each;
  imprecise wording risks leaving a contradiction between what ADR 0016
  claims and what the six updated contract files actually say. Mitigated by
  Preflight's consistency sweep and the Reviewer's explicit per-file check.
- The "intervention gates only the specific in-flight item" rule is new and
  has no prior operational precedent in this repository; its precise
  behavior is likely to need a Deferred Question follow-up once it is
  exercised in practice (see the design agreement's Deferred Questions).
- Contract-file traceability: six issues each need their own AI work trace
  under `docs/collaboration/traces/` per
  `docs/collaboration/prompt-instruction-change-control.md`; omitting one
  blocks that issue's contract-file review regardless of content quality.

## Verification Plan

- `scripts/check-contract-consistency.py` after all eight issues land.
- Targeted `grep` sweep for the superseded ADR 0001/0014 phrasing
  ("per-work-plan... dialogue" as a hard blocking requirement; "the next
  work plan does not start without [close]") across all updated documents,
  confirming none remain describing the pre-ADR-0016 behavior as current.
- Confirmation that each of the six contract-file issues has an
  accompanying trace under `docs/collaboration/traces/`.
- Independent Reviewer approval, in a separate context, addressing each
  contract-file change under ADR 0006 explicitly.
