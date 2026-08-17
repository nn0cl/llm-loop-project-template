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
| LISS-0019 | proposed | M | M | AIP-0019-001 | - | LISS-0020..0026 | process/adr-0016-two-group-topology |
| LISS-0020 | proposed | S | S | - | LISS-0019 | - | process/personas-group-mapping |
| LISS-0021 | proposed | M | M | AIP-0021-001 | LISS-0019 | - | process/ai-human-scheme-loop-update |
| LISS-0022 | proposed | M | M | AIP-0022-001 | LISS-0019 | - | process/cross-session-messaging-protocol |
| LISS-0023 | proposed | S | S | - | LISS-0019 | - | process/session-start-standing-pair |
| LISS-0024 | proposed | S | S | - | LISS-0019 | - | process/implementation-group-worktree-rule |
| LISS-0025 | proposed | M | M | AIP-0025-001 | LISS-0019 | - | process/design-agreement-backlog-gate |
| LISS-0026 | proposed | S | S | - | LISS-0019 | - | process/backlog-readme-bulk-gate |

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

- Issue: LISS-0019
- Reason it is unblocked: no dependencies; it is the root of this work plan.
- Reopening request needed: no.

## Minor Fix Path

Not applicable to the initial execution of this work plan (every issue here
is Architecture Path, several touching contract files under ADR 0006). The
Minor Fix Path may apply later to small corrections against this work plan's
accepted result.

## Preflight Validation

- Result: not yet run.
- Checks: `scripts/check-contract-consistency.py`; targeted `grep` sweep
  confirming ADR 0001/0014 clauses this work plan supersedes are marked as
  such wherever restated; confirmation that `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` remain consistent in effective content (per
  `docs/collaboration/prompt-instruction-change-control.md`), since this
  work plan changes shared phase/gate rules.
- Scope result: pending.
- Next action: run once every issue above is self-reviewed and complete.

## Work-Plan Review

Reviewer's approval record: pending — link once recorded under
`docs/collaboration/reviews/`.

Six of the eight issues (LISS-0020, 0021, 0022, 0023, 0024, 0025) change
agent operating contract files under ADR 0006 and therefore require the
Reviewer's approval to explicitly address each contract-file change (reason,
trace presence, cross-file consistency), not only the work plan's
specification conformance in general — mirroring
`docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`'s
Task 4 precedent, where one work-plan-level Reviewer pass covered
propagation across nine contract files.

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

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
