# Branch, Commit, and PR Discipline

This document defines Git workflow for AI-TDD collaboration.

## Branches

Create branches by feature or process task.

Recommended branch names:

```text
feature/<short-feature-name>
test/<short-behavior-name>
refactor/<short-area-name>
docs/<short-topic>
process/<short-process-topic>
chore/<short-maintenance-topic>
```

Rules:

- one branch should represent one feature, process change, or reviewable unit.
- direct pushes to `main` or the trunk branch are prohibited; all changes must
  arrive through a pull request that carries a Reviewer approval record.
- feature branches should be tied to a local issue, GitHub issue, or a task
  named in the covering design agreement.
- work on any local issue (`docs/issues/LISS-*`) or GitHub Issue must happen on
  a dedicated branch; do not implement issue work directly on `main` or the
  trunk branch, even for a single commit.
- do not mix unrelated documentation, tests, implementation, and refactor work.
- do not start Phase 2 implementation on a branch whose Phase 1 tests have not
  been reviewed.
- branch names should describe user-visible feature or process purpose, not the
  AI tool used.
- keep branches short-lived: merge or close a branch as soon as its reviewable
  unit (one Phase, one issue, one process change) is accepted, instead of
  accumulating multiple issues or phases on one long-running branch.
- automated maintenance branches (for example, the
  `process/update-collab-template-*` branches created by
  `scripts/update-ai-collaboration-files.sh`, see
  `docs/architecture/adr/0008-template-update-propagation.md`) are exempt from
  the local/GitHub issue requirement above, but must still go through a PR and
  the CI gate before merging; they must never commit to `main` directly.

## Continuous Integration Gate

- a branch must pass CI before it merges into `main` or the trunk branch; do
  not merge on a red or skipped pipeline.
- repository hosting settings should protect `main` or the trunk branch from
  direct pushes and require the applicable pull-request checks and reviews;
  repository documents alone cannot enforce this server-side restriction.
- when PR volume or contributor count makes race conditions between merges
  likely, adopt a merge queue (or equivalent serialized-merge mechanism) so
  each merge is tested against the current state of `main` before landing.
  Which merge-queue tool to use is a stack-specific choice, not a template
  assumption.

## Parallel Agent Work (Worktrees)

When more than one agent or session works on this repository at the same
time:

- give each in-flight issue its own branch and its own `git worktree` (or
  equivalent isolated checkout) rather than sharing one working directory
  across agents.
- do not let two agents write to the same worktree/branch concurrently.
- keep the number of concurrent agent worktrees within what the Reviewer
  persona can actually review before they go stale; more parallel branches than
  the review capacity defeats the point of short-lived branches.

### Implementation-group worktree, per work plan

Per `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`,
the Implementation group (Implementer) works each work plan in its own
dedicated `git worktree`, on top of the existing feature-unit branch
convention above — this is a mechanic added for the standing two-group
topology, not a replacement for the branch-naming or PR rules already
stated in this document.

- **Why**: the Design & Review group (Planner, Specifier, Reviewer, Arbiter)
  works against `main` — producing docs, specs, ADRs, and review records —
  while the Implementation group executes an agreed work plan concurrently.
  A dedicated worktree keeps the Implementation group's in-progress,
  uncommitted or unmerged edits isolated from the Design & Review group's
  own concurrent reads and writes against `main`.
- **When created**: at the "Design agreement recorded -> Implementation
  group" handoff (per
  `docs/collaboration/cross-session-messaging.md`), before Phase 0 Design
  Intake starts for the work plan's first issue.
- **Naming convention**: the worktree directory is named after the work
  plan's feature branch (e.g. a work plan branching as
  `process/<short-process-topic>` uses a worktree directory named for that
  same branch), consistent with the branch-naming convention above — a
  worktree name should let a reader tell which branch, and therefore which
  work plan, it holds without opening it.
- **When removed**: after the work plan's branch merges, or the work plan
  closes (per `docs/collaboration/design-agreement.md`'s "Closing a work
  plan"), whichever happens first under this repository's existing merge
  timing. A worktree for a work plan that has not yet closed is not removed
  while issues in that plan are still in progress.
- **Who removes it, and when**: the session whose content the worktree/branch
  held is responsible for removing both, immediately, as part of that same
  session's own completion step, once it has confirmed its own content
  actually landed upstream (the merge it was waiting on happened, or the
  work plan closed) — not something deferred to a later sweep by a
  different thread. See "Self-directed branch and worktree cleanup at merge
  time" below for the same expectation, stated generally, across both
  groups in this repository's two-group topology.
- This does not change branch-naming, the CI gate, the feature-unit branch
  creation steps, or any other rule in this document — it only states where
  the Implementation group's checkout lives while it works.

### Self-directed branch and worktree cleanup at merge time

This generalizes the "who removes it, and when" rule above beyond the
Implementation group specifically. In this repository's standing two-group
topology (per
`docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`),
any session whose branch is merged into whatever it was feeding —
Implementation group work merged into the Design & Review group's own
branch; the Design & Review group's own working branch merged into the
shared `process/*` branch — removes its own now-redundant branch and
worktree as its own next step, immediately after confirming the merge
landed, not deferred to a later sweep by another thread or session.

This does not change the merge-timing constraint already stated above: a
worktree or branch is not removed before its content has actually merged,
or before the work plan it belongs to closes, and never while issues in
that work plan are still in progress. It only makes explicit that
performing the removal is each session's own responsibility, done as part
of its own completion step, not a separate housekeeping task left for
someone else to do later. See
`docs/collaboration/cross-session-messaging.md` for the full handoff
protocol between the two groups this expectation generalizes over.

## Stacked Branches for Phase Splitting

A single issue's Red, Green, and Refactor phases may be submitted as stacked
branches/PRs (each based on the previous phase's branch) instead of one large
PR, as long as:

- each stacked branch still targets `main` as its eventual destination and is
  still checked by the same CI/branch-protection rules as a normal PR.
- the stack order matches phase order: Red before Green before Refactor.
- the PR description states where each branch sits in the stack and which phase
  it represents, so a reader who was not in the producing context can tell.

## Commits

Prefer commits by phase:

```text
docs: add design intake for <topic>
test: add red tests for <behavior>
feat: implement <behavior>
refactor: clarify <area>
chore: update process tooling
```

Rules:

- keep commits reviewable.
- do not hide test changes inside implementation commits.
- when issue status changes, include the matching issue/documentation synchronization and any applicable work-plan update in the same reviewable unit.
- mention AI assistance in PR notes when it materially shaped the change.
- never commit secrets or full exports of private data.

## Pull Requests

PRs should identify:

- current phase.
- Reviewer approval records, with the failure scenarios searched for.
- changed files.
- deterministic verification.
- whether tests were reviewed before implementation.
- whether AI payload included private context.
- CI status (must be passing before merge; see Continuous Integration Gate
  above).

## Feature-Unit Branch Creation

When starting a new feature:

1. create or update local issue and work plan files.
2. verify issue dependencies are resolved or waived.
3. create or update the design intake.
4. create a feature branch.
5. add Phase 1 tests only.
6. self-review the Red state — deterministic output, named failure scenarios.
7. continue with Phase 2 on the same feature branch or a clearly linked
   branch. The separate-context Reviewer sees the whole work plan once, at
   its close — see
   `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`.

Recommended command shape:

```text
git switch -c feature/<short-feature-name>
```

Use `docs/architecture/agent-quickstart.md` before making changes on the branch.

See `docs/collaboration/local-issue-planning.md` for local issue and dependency
rules.
