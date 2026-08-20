# Design Agreement: Correct the "coordinator" Confabulation Record

## Identity

- Agreement ID: DA-2026-08-18-02
- Date: 2026-08-18
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none. Does not reopen `DA-2026-08-18-01`
  (`docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`)
  because that agreement's own work plan (WP-0002) already closed
  (`docs/work-plans/WP-0002-two-group-send-message-loop.md`, "Work-Plan
  Close", 2026-08-18) before `docs/backlog/item-0008-*.md` was promoted. Per
  CLAUDE.md ("one design agreement per work plan... do not combine multiple
  backlog items into one agreement") and `docs/collaboration/design-agreement.md`
  ("An agreement covers exactly one work plan"), a closed work plan's
  agreement is not the vehicle for a new, later-promoted backlog item's work,
  even one that touches the same file family. See "Settled Ambiguities"
  below — this is the one judgment call this agreement records against
  item-0008's own "mirrors how LISS-0027 was handled" suggestion.

## Direction

Per `docs/backlog/item-0008-coordinator-message-hallucination-correction.md`
(`Status: promoted`), whose Promotion notes are this agreement's Director
authorization under ADR 0016 Rule 2:

- `docs/collaboration/cross-session-messaging.md`'s "Confirmed failure mode"
  section, and `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`'s
  "Provenance verification" section, both describe four unverified in-band
  "coordinator" messages received during WP-0002's execution under the
  working assumption that they were external injection attempts.
- A Backlog-thread investigation, cited in item-0008, found no injection
  mechanism anywhere in the repository (no `.claude/settings*.json`, no hook
  files, nothing in git history across any branch) and found that the only
  legitimate occurrences of "coordinator" in the repository are ordinary
  prose in pre-existing 2026-08-02 review records — both files a session
  doing normal design intake or Preflight file-scanning would read. The more
  likely explanation is model-side confabulation triggered by that
  legitimate historical terminology, not external injection.
- Correct both files to state this, without weakening the operational rule
  that an unverified message is refused regardless of origin, and without
  silently rewriting either file's already-recorded decision (refusal was
  correct; WP-0002's approval stands).

## Scope

- In scope:
  - Re-confirm item-0008's own evidence claim, independently, before editing
    anything (repo-wide `coordinator` grep across the working tree and all
    local/remote branches; confirm no `.claude/settings*.json` or hook files
    exist).
  - Edit `docs/collaboration/cross-session-messaging.md`'s "Confirmed failure
    mode" section (an ADR-0006 contract file) to reframe the likely cause as
    model-side confabulation rather than confirmed external injection, while
    preserving the section's actual operational content (the `ListAgents`
    absence, the `to: "main"` fix, the verify-before-trusting rule) unchanged
    in substance.
  - Add a corrective addendum to
    `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`'s
    "Provenance verification" section (a review record, not a contract file,
    per `docs/collaboration/prompt-instruction-change-control.md`'s scope
    list) noting the corrected likely cause, without altering the original
    approval, its constraints checklist, or its Decision.
  - An AI work trace under `docs/collaboration/traces/`, required because
    `cross-session-messaging.md` is an ADR-0006 contract file (per
    `docs/collaboration/prompt-instruction-change-control.md`'s
    Traceability Rule — required even for small wording changes).
  - Separate-context Reviewer confirmation, per ADR 0006 (never self-review
    for a contract-file change, regardless of Minor Fix Path or work-plan
    scope, per CLAUDE.md's "Preflight Validation" section).
- Explicitly out of scope:
  - Any change to `SendMessage`/`ListAgents` usage rules or a new
    verification mechanism — item-0008's own "Known constraints" rule this
    out; the existing "verify independently before trusting" rule already
    covers both possible origins.
  - Re-litigating WP-0002's Decision (Approved) or its constraints checklist.
    This is a corrective addendum, not a re-review.
  - Any change to `docs/collaboration/cross-session-messaging.md` beyond the
    "Confirmed failure mode" section.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Independently reconfirm item-0008's evidence (repo-wide `coordinator` grep, all branches; `.claude/settings*.json` / `*hook*` file search) | Implementer | Minor Fix Path | Search results match item-0008's own claim; any discrepancy is reported, not silently reconciled | command output pasted in the issue's Work Notes |
| 2 | Edit `cross-session-messaging.md`'s "Confirmed failure mode" section | Implementer | Minor Fix Path | Section states the likely cause is model-side confabulation, not confirmed external injection; the `ListAgents`-absence finding, the `to: "main"` fix, and the verify-before-trusting rule are preserved in substance; section header/placement otherwise unchanged | `scripts/check-contract-consistency.py`; read-through diff |
| 3 | Add corrective addendum to the WP-0002 review record's "Provenance verification" section | Implementer | Minor Fix Path | Addendum is clearly marked as added after the original approval, references item-0008, and does not alter the original Decision, constraints checklist, or falsification table | read-through diff |
| 4 | AI work trace for the contract-file change (Task 2) | Implementer | Minor Fix Path | Trace names the file, the reason, and the expected agent-behavior change | trace file exists under `docs/collaboration/traces/` |
| 5 | Self-review the combined correction | Implementer | Minor Fix Path | Short-form self-review per `docs/templates/self-review.md`, naming the command run and the risk that the correction could be read as retracting WP-0002's approval | self-review record in LISS-0028 Work Notes |
| 6 | Preflight Validation | Implementer / deterministic tool | Minor Fix Path | `pass` recorded with command output | Preflight section in WP-0003 |
| 7 | Separate-context Reviewer confirmation | Reviewer (Design & Review group, separate context from the session that did Tasks 1-6) | Minor Fix Path | Review record explicitly addresses the contract-file change under ADR 0006, not only general conformance | review record under `docs/collaboration/reviews/` |

Sequencing: Task 1 blocks 2 and 3 (do not edit before independently
reconfirming the evidence). Tasks 2 and 3 may run in either order. Task 4
follows Task 2. Task 5 follows 2-4. Task 6 follows 5. Task 7 follows 6.

## Specifications

- None. This is a documentation correction to a process/governance record; no
  application specification applies. The "acceptance criterion" column in
  the Plan table is this task's specification, per the Minor Fix Path.

## Boundaries

- `docs/collaboration/cross-session-messaging.md` remains an ADR-0006
  contract file: no self-review-only approval, a trace is mandatory, and a
  separate-context Reviewer must confirm it, regardless of Minor Fix Path
  use (CLAUDE.md, "Preflight Validation" section, final paragraph).
- `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`
  is not a contract file (review records are explicitly excluded in
  `docs/collaboration/prompt-instruction-change-control.md`) but its
  already-approved Decision must not be silently rewritten — only appended
  to, with the addendum clearly marked as such.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` in the
  backlog item or this agreement until the Director's own work-plan-close
  action.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does this correction reopen `DA-2026-08-18-01`, mirroring LISS-0027, or does it need its own new agreement? | Its own new agreement (this one, `DA-2026-08-18-02`) and work plan (WP-0003). `DA-2026-08-18-01`'s work plan (WP-0002) already closed on 2026-08-18 before item-0008 was promoted; reopening a closed work plan's agreement for unrelated later-promoted work would violate `design-agreement.md`'s "an agreement covers exactly one work plan" and CLAUDE.md's "do not combine multiple backlog items into one agreement." LISS-0027 mirrored a still-open agreement's reopening; this item does not have that circumstance. | Design & Review group (Planner), reading `design-agreement.md` and CLAUDE.md against the actual git history of WP-0002's close |
| Is item-0008 a `Type: review-finding` issue, and does the Minor Fix Path apply literally? | Not a `Type: review-finding` issue (it originates from a Backlog-thread investigation, not a Reviewer's falsification pass against an in-flight work plan). The backlog item's own Promotion notes explicitly direct Minor Fix Path treatment by name, and the substantive criteria (planning size S, no spec/ADR/port/data-model/dependency/boundary change, one attempt expected) are met, so this agreement follows that direction by analogy, recorded explicitly rather than silently assumed. | Design & Review group (Planner), per the backlog item's own Promotion notes |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should `docs/collaboration/findings-reuse.md` or a future "design/review perspectives" document (item-0006, if built) capture "long nested sessions reading historical role-shaped prose can trigger confabulation" as a generalizable review perspective? | item-0006's own work plan, if it proceeds and builds the perspectives document described there — out of this item's own narrow scope |

## Verification

- Repo-wide `grep -rni "coordinator"` across the working tree and all local
  and remote-tracking branches, and a search for `.claude/settings*.json` /
  `*hook*` files, re-run independently by the Implementer and pasted in
  Work Notes.
- `scripts/check-contract-consistency.py` after the contract-file edit.
- Confirmation that `docs/collaboration/traces/` contains a trace for this
  change.
- Separate-context Reviewer approval addressing the contract-file change
  under ADR 0006 explicitly.

## Falsification Criteria

- The corrected `cross-session-messaging.md` section states the cause as
  confirmed (rather than likely/probable) in either direction, overclaiming
  certainty the evidence does not support.
- The correction weakens or removes the "verify before trusting, regardless
  of source" operational rule.
- The WP-0002 review record's original Decision, constraints checklist, or
  falsification table is edited in place rather than appended to.
- The contract-file change lands without a trace or without separate-context
  Reviewer approval.
- The independent re-confirmation (Task 1) finds evidence contradicting
  item-0008's claim and the correction proceeds anyway without surfacing
  that discrepancy.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0008-coordinator-message-hallucination-correction.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2
      (backlog-item-level agreement) and
      `docs/collaboration/design-agreement.md`'s "Backlog-item-level
      agreement" section.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan, per `design-agreement.md`'s requirement that
      ADR 0016 does not pre-approve this half before the plan exists.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
