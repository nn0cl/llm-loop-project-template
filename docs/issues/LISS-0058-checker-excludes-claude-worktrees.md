# LISS-0058: `check-contract-consistency.py` must exclude `.claude/` from its file scan

## Metadata

- Local issue ID: LISS-0058
- GitHub issue: none
- Status: ready
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: Fast Path
- Type: bug
- Priority: high
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0020-checker-excludes-claude-worktrees.md`)
- Related branch: process/promote-item-0017 (this issue's own execution
  branch is created off it, per the work plan)

## Summary

`scripts/check-contract-consistency.py` has two `os.walk(repo)` sites —
`scanned_files()` (line ~388) and `check_references()`'s own internal walk
(line ~435) — that each exclude only `.git` from traversal:

```python
dirnames[:] = [d for d in dirnames if d != ".git"]
```

Neither excludes `.claude/`, the harness-local, untracked-by-git directory
this environment's Agent-tool worktree isolation uses for
`.claude/worktrees/<agent-id>/` — each a full nested checkout of the
repository. Confirmed directly (`git ls-tree -r --name-only HEAD | grep
"^\.claude/"` returns nothing; `.gitignore` has no `.claude` entry either —
it is real, on-disk, harness-managed scratch state that plain `os.walk`
still sees, gitignore or not). When the checker runs from a location that
has one or more active sibling worktrees under `.claude/worktrees/` (the
normal, expected state throughout this session's whole two/three-layer
loop, per ADR 0016/0017), every scanned file is duplicated once per active
nested worktree, and `check_references()`'s ambiguous-basename detection
reports false-positive "which N files answer to this... write the path"
noise for filenames that are genuinely unambiguous in the actual tracked
repository content.

## Acceptance Notes

Fix both `os.walk` exclusion sites to also prune `.claude` from `dirnames`
at the point where `dirpath == repo` and `name == ".claude"` (i.e., exclude
the whole top-level `.claude` directory, not only its `worktrees`
subdirectory — confirmed via `git ls-tree` above that nothing under
`.claude/` anywhere is tracked, so excluding the whole subtree loses no
real contract-relevant content and is simpler and more future-proof than
special-casing `.claude/worktrees` alone against whatever else this
harness or another adopter's tooling might place under `.claude/` later,
per the item's own "Design & Review's call" on how broad to make the
exclusion):

```python
dirnames[:] = [d for d in dirnames if d not in (".git", ".claude")]
```

Apply the identical change at both sites (`scanned_files()` and
`check_references()`). Do not change `SCANNED_SUFFIXES`, `RECORD_DIRS`, or
any other existing exclusion/inclusion logic — this is scoped to the two
named `os.walk` prune lines only, per the item's own boundary ("this only
removes ephemeral harness-local directories from the scan, it doesn't
relax any actual check").

### Required reproduction (before and after)

Per the item's own "Why it might matter" and this work plan's Verification
Plan: reproduce the false-positive noise first, in a controlled fixture (do
not depend on whatever sibling worktrees happen to exist under the real
repository root at execution time — that state is transient and not a
reliable, re-runnable reproduction):

1. Build a throwaway fixture directory (e.g., under a scratch/tmp path):
   copy this repository's actual tracked working-tree content into it,
   then create `<fixture>/.claude/worktrees/fake-sibling/` and copy the
   same tracked content into that nested path too — this faithfully
   reproduces "a full nested checkout of the repository under
   `.claude/worktrees/`," the exact mechanism the bug report describes,
   without depending on real sibling agent worktrees' transient state.
2. Run `python3 scripts/check-contract-consistency.py --repo <fixture>`
   against the **pre-fix** script and paste the actual output, confirming
   real ambiguous-basename noise is produced (this is the "confirm the
   noise" step).
3. Apply the fix.
4. Re-run the same command against the same fixture and paste the actual
   output, confirming the noise is gone (this is the "confirm it's gone
   after the fix" step) and that no other check regressed.
5. Also run the fixed script normally, `python3 scripts/check-contract-consistency.py`
   (default `--repo .`, i.e. against this issue's own real worktree, which
   has no nested `.claude/worktrees/` of its own — see Context below),
   confirming it still reports `all checks passed` (or the same baseline
   result as before this change) on real repository content.

## Dependencies

- Parent: `docs/work-plans/WP-0020-checker-excludes-claude-worktrees.md`
- Depends on: none
- Blocks: none
- Related: `docs/backlog/item-0017-checker-excludes-claude-worktrees.md`,
  `scripts/check-contract-consistency.py`

## Decisions Not Settled by the Design Agreement

- None — scope is fully settled by
  `docs/collaboration/agreements/2026-08-20-checker-excludes-claude-worktrees.md`.

## Context

- Included: `scripts/check-contract-consistency.py`'s full `scanned_files()`
  and `check_references()` functions, `docs/backlog/item-0017-...md`'s full
  text, direct `git ls-tree`/`.gitignore` confirmation that nothing under
  `.claude/` is tracked.
- Omitted: the rest of the checker's other check functions (unaffected by
  this change — the fix only prunes `os.walk`'s traversal, it does not
  touch any check's own logic).
- Assumptions: none. Note for whoever executes this issue — your own
  Implementation-group worktree (created under `.claude/worktrees/` of the
  main repository) will not itself contain a `.claude/` subdirectory at its
  own root (confirmed directly: `.claude/worktrees/<id>/` is where a
  worktree *lives*, not something replicated *inside* it), so running the
  fixed checker against your own real worktree (`--repo .`, no flag) will
  not by itself exercise the fix — the fixture in "Required reproduction"
  above is what actually demonstrates the bug and the fix.

## References

- `docs/backlog/item-0017-checker-excludes-claude-worktrees.md`
- `scripts/check-contract-consistency.py`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0020, scoped per the design agreement. Not yet dispatched.

## Verification

- Pre-fix fixture run showing real ambiguous-basename noise (pasted, not
  summarized).
- Post-fix fixture run showing the noise is gone (pasted).
- Post-fix run against this issue's own real worktree
  (`python3 scripts/check-contract-consistency.py`) showing no new failure.
- `git diff` showing the change is confined to the two named `os.walk`
  prune lines.
