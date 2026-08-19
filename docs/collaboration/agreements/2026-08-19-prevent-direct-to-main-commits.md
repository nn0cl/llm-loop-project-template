# Design Agreement: Prevent Direct-to-Main Commits

## Identity

- Agreement ID: DA-2026-08-19-01
- Date: 2026-08-19
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0013-prevent-direct-to-main-commits.md`
(`Status: promoted`), whose Promotion notes are this agreement's Director
authorization under ADR 0016 Rule 2: add an explicit, checkable rule
requiring any session to confirm its current branch is not `main`/trunk
before committing anything, stated for every kind of record this
repository's process produces — including Backlog-layer records such as
backlog items, which the existing wording in
`docs/collaboration/local-issue-planning.md` only names as "issue work" and
arguably does not clearly cover. This corrects the gap that let the
Backlog thread commit `docs/backlog/item-0012-*.md` directly to `main`
after a post-merge branch switch (caught, reverted as commit `b6c8961`).

## Scope

- In scope:
  - A new "Pre-Commit Branch Confirmation" rule in
    `docs/collaboration/branch-commit-pr-discipline.md`'s "Branches"
    section: before any `git commit`, confirm the current branch is not
    `main`/trunk (e.g., `git branch --show-current`); if it is, create or
    switch to a dedicated branch first; states explicitly that this
    applies to every record kind, including Backlog-layer records, not
    only AT-TDD issue work; distinguishes reading `main` (fine) from
    committing while still checked out on it (the actual failure); cites
    the incident.
  - A broadening edit to `docs/collaboration/local-issue-planning.md`'s
    "Dependency Rules" section: its existing "Agents must not implement
    issue work directly on `main` or the trunk branch" sentence is widened
    to cover any repository record, including Backlog-layer records, and
    cross-references the new general rule instead of restating it.
  - The required AI work trace under `docs/collaboration/traces/` (both
    files are ADR-0006 contract files) and separate-context Reviewer
    approval, regardless of the `S` planning size.
- Explicitly out of scope:
  - Any new deterministic tooling (git hook, CI check) enforcing the rule
    — item-0013's own "Known constraints" states the core ask is the
    written rule, not necessarily new tooling; recorded as a Deferred
    Question below.
  - Relitigating whether Backlog-layer records need separate-context
    Reviewer approval the way ADR-0006 contract files do — they still
    don't; this fix is branch discipline only, per item-0013's own
    "Boundaries or non-goals."
  - Any edit to `CLAUDE.md` or its four mirrors — neither touched file is
    part of that literal-mirror text-identity set (confirmed by grep
    before this agreement was written: no mirror file inlines either
    document's text, only links to it), so no mirror-sync obligation is
    raised.
  - item-0012 (document/log lifecycle management) — a separate, unrelated
    backlog item; not bundled into this work plan.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Add "Pre-Commit Branch Confirmation" rule to `branch-commit-pr-discipline.md` | Implementer | Fast Path (mechanical, narrow, no behavior/architecture change — a process-discipline documentation addition) | States the confirm-before-commit rule, names Backlog-layer records explicitly, distinguishes read vs. commit, cites the incident | read-through diff |
| 2 | Broaden `local-issue-planning.md`'s issue-work-only sentence to cross-reference the new rule | Implementer | Fast Path | No longer reads as scoping the prohibition to issue work only; cross-references rather than duplicates | read-through diff |
| 3 | AI work trace under `docs/collaboration/traces/` | Implementer | Fast Path | States which contract files changed, why, and what agent behavior changes | trace file present, `docs/templates/ai-work-trace.md` fields filled |
| 4 | Self-review | Implementer | Fast Path | Short-form self-review per `docs/templates/self-review.md`, recorded in LISS-0042 Work Notes | self-review record |
| 5 | Preflight Validation | Implementer / deterministic tool | Fast Path | `pass` recorded with `scripts/check-contract-consistency.py` output | Preflight section in WP-0013 |
| 6 | Work-plan-level Reviewer pass | Reviewer (Design & Review group, separate context) | Fast Path | Review record confirms the two edits are accurate, narrow, correctly scoped (not extending to Backlog-layer approval requirements), and the trace is present and accurate | review record under `docs/collaboration/reviews/` |

Sequencing: Tasks 1 and 2 may proceed together (independent files). Both
block Task 3. Task 3 blocks 4. Task 4 blocks 5. Task 5 blocks 6.

## Specifications

- None. Documentation/process-only change; no application specification.

## Boundaries

- Both touched files are ADR-0006 contract files — trace and
  separate-context Reviewer approval are mandatory, regardless of the `S`
  planning size and regardless of Minor Fix Path applying in substance to
  everything else about this change.
- No change to `CLAUDE.md` or its four mirrors.
- No change to Backlog-layer approval requirements (this fix does not make
  backlog items subject to separate-context Reviewer approval).
- No new tooling (hook/CI) in this work plan.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` (in the
  Director-facing sense) until the Director's own work-plan-close action —
  this work plan stops at Reviewer approval, on the shared branch
  `process/backlog-item-0012-and-0013`, and reports readiness.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Which file(s) carry the new rule — `branch-commit-pr-discipline.md`, `local-issue-planning.md`, or both (item-0013 leaves this to Design & Review's judgment)? | Both: the general rule lives in `branch-commit-pr-discipline.md` (the document that already owns branch/commit mechanics), and `local-issue-planning.md`'s existing narrower sentence is broadened to cross-reference it rather than left to read as issue-work-only. This avoids duplicating the rule's substance in two places while still closing the specific gap item-0013 names in `local-issue-planning.md`'s own wording. | Design & Review group (Planner), per the item's own explicit delegation |
| Does this need a new deterministic check (hook/CI)? | Not in this work plan — item-0013's own "Known constraints" states the core ask is the written rule; a hook is recorded as a Deferred Question so it is not silently dropped, but is not required to close this item quickly, matching the Director's stated priority for this item ("small, well-scoped... get it merged/closed quickly"). | Design & Review group (Planner) |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should a git pre-commit hook or CI check enforce the branch-confirmation rule automatically, rather than relying on the written rule alone? | Only if a future incident shows the written rule alone was insufficient (a session read it and still committed to `main`), or a later work plan judges the marginal cost of a hook worth it — not assumed necessary now. |

## Verification

- `scripts/check-contract-consistency.py` (regression check; neither file
  is part of the mirror-parity machinery, so expected unaffected).
- Read-through diff confirming both edits are narrow, accurate, and do not
  duplicate or contradict each other or existing wording.
- Work-plan-level Reviewer approval, separate context.

## Falsification Criteria

- The new rule is stated only for AT-TDD "issue work" and does not
  explicitly name Backlog-layer records — the exact gap this item exists
  to close.
- The edit is worded so that it appears to newly require separate-context
  Reviewer approval for Backlog-layer records themselves (out of scope,
  per item-0013's own "Boundaries or non-goals").
- `CLAUDE.md` or a mirror file is edited despite this agreement's explicit
  scope.
- No AI work trace is recorded for this contract-file change.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0013-prevent-direct-to-main-commits.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
