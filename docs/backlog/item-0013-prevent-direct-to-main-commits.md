# Backlog item: item-0013-prevent-direct-to-main-commits

## Metadata

- Item ID: item-0013
- Title: Prevent the Backlog thread (or any session) from committing
  directly to `main`/trunk
- Status: promoted
- Created: 2026-08-19
- Updated: 2026-08-19
- Priority hint: high
- Suggested planning size: S
- Owner/agent (optional): unassigned

## Summary

Incident, this session: after PR #16 merged and the local checkout was
switched to `main` to pick up the merge, the Backlog thread committed and
pushed `docs/backlog/item-0012-*.md` directly onto `main` — no dedicated
branch, no PR, no review. Caught immediately by the Director, reverted
(`git revert`, commit `b6c8961`, pushed), and item-0012 was recreated on a
proper feature branch. No contract file was touched, so no ADR-0006 gap
resulted, but this violates
`docs/collaboration/branch-commit-pr-discipline.md` and
`docs/collaboration/local-issue-planning.md`'s existing rule ("Agents must
not implement issue work directly on `main` or the trunk branch") — which
today only names *issue work*, not explicitly *any* commit including
Backlog-layer records like backlog items.

Root cause: nothing in the operating contract requires an agent to check
which branch it is actually on before running `git commit`/`git push`.
Switching to `main` for a legitimate reason (reading the post-merge state)
left the working tree checked out to `main`, and the next commit landed
there by default with no guard catching it.

Add an explicit, checkable rule: before any commit, confirm the current
branch is not `main`/the trunk branch; if it is, create or switch to a
dedicated branch first. State this for every kind of record this
repository's process produces (backlog items included, not just "issue
work"), since the incident was specifically a backlog item, which the
existing wording arguably does not clearly cover.

## Why it might matter

A direct-to-main commit bypasses every gate this template's own process
exists to enforce — no branch, no PR, no CI run, no review — for whatever
content happens to land there. This time it was a backlog item (low risk),
but the same failure mode applied to a contract-file edit would be a real
ADR-0006 violation reaching `main` unreviewed.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes — documentation/
  process-wording fix, possibly paired with a cheap deterministic check
  (e.g., a `scripts/check-contract-consistency.py` addition or a local git
  hook) if Design & Review judges one is warranted, but the core ask is the
  written rule, not necessarily new tooling.
- Boundaries or non-goals:
  - Does not relitigate whether Backlog-layer records (backlog items,
    local issues, work plans) need separate-context Reviewer approval the
    way ADR-0006 contract files do — they still don't; the fix is about
    branch discipline, not approval requirements.
  - `docs/collaboration/branch-commit-pr-discipline.md` and
    `docs/collaboration/local-issue-planning.md` are both ADR-0006
    contract files — any edit needs its own trace and separate-context
    Reviewer confirmation, Minor Fix Path or not.

## Uncertainty

- [x] Spec can be written now — narrow, single incident, clear root cause.
- [ ] Spike required first
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none — related:
  `docs/collaboration/branch-commit-pr-discipline.md`,
  `docs/collaboration/local-issue-planning.md`, revert commit `b6c8961`

## Promotion notes

- Date: 2026-08-19
- Decision: Promoted, in the Backlog-layer thread ("revertしてブランチを
  切った後に対策を運用規約に反映、継続して"). Per ADR 0016 Rule 2, Design
  & Review proceeds autonomously from here.
- Reason: Direct incident, root cause clear, narrow S-sized fix; ready to
  run.
