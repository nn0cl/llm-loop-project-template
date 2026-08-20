# LISS-0058: `check-contract-consistency.py` must exclude `.claude/` from its file scan

## Metadata

- Local issue ID: LISS-0058
- GitHub issue: none
- Status: done
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
- 2026-08-20 — Implementation group (Implementer persona), on branch
  `wp-0020-execution` (created off `process/promote-item-0017`). Executed
  Fast Path per the work plan's Plan table (tasks 1-3).

  Approach chosen: factored the exclusion list into a shared module-level
  constant, `EXCLUDED_DIRS = (".git", ".claude")`, placed immediately after
  `SCANNED_SUFFIXES` (around line 331), and used it at both `os.walk` prune
  sites (`scanned_files()` line ~397, `check_references()` line ~452) in
  place of the duplicated `d != ".git"` literal — rather than duplicating
  the tuple literal at each site, per the work plan's stated either-is-
  acceptable choice.

  Fixture location convention: a throwaway directory under this session's
  own scratchpad path
  (`/private/tmp/claude-501/.../scratchpad/liss-0058-fixture`), built by
  `git archive HEAD | tar -x` into the fixture root and again into
  `<fixture>/.claude/worktrees/fake-sibling/`, per the design agreement's
  Settled Ambiguities and LISS-0058's own "Required reproduction" steps.
  The fixture directory was removed (`rm -rf`) immediately after the
  post-fix verification runs completed; confirmed removed by listing the
  scratchpad directory afterward and observing it no longer appears (only
  pre-existing, unrelated scratch files from other sessions remain). No
  fixture content was committed to the repository.

  Self-review (short form, per `docs/templates/self-review.md`):

  ```
  Phase / finding: Fast Path (single-attempt bug fix, WP-0020 tasks 1-3)
  Command run (before fix, fixture): python3 scripts/check-contract-consistency.py --repo <fixture>
  Result: "contract consistency: 906 failure(s)", exit code 1; 806 of the
    906 lines are ambiguous-basename "... which 2 files answer to ...
    Write the path." entries, each pairing a top-level file with its
    identical nested .claude/worktrees/fake-sibling/ copy (e.g.
    ".claude/worktrees/fake-sibling/CHANGELOG.md:123 names
    '2026-08-03-work-plan-scoped-governance-review.md', which 2 files
    answer to (.claude/worktrees/fake-sibling/docs/collaboration/reviews/...,
    docs/collaboration/reviews/...). Write the path."). Full 911-line
    output captured this session; genuine reproduction of the bug as
    described, not a synthetic or assumed result.
  Command run (after fix, same fixture): python3 scripts/check-contract-consistency.py --repo <fixture>
  Result: "contract consistency: all checks passed", exit code 0 — all 806
    ambiguous-basename lines and all other duplication-driven noise gone.
  Command run (after fix, real repository): python3 scripts/check-contract-consistency.py
  Result: "contract consistency: all checks passed", exit code 0 — identical
    to the real-repository run captured before the fix was applied (also
    "all checks passed", exit code 0); no regression, no new failure, no
    newly hidden failure (there were none to hide).
  Risks considered:
    - A real, tracked reference could coincidentally target a path or
      filename that collides with the literal string ".claude", causing
      the fix to silently exclude genuine content.
    - The broader fix (excluding the whole .claude/ subtree, not only
      .claude/worktrees/) could lose some other, currently-untracked but
      contract-relevant file living elsewhere under .claude/.
    - Factoring the tuple into a shared EXCLUDED_DIRS constant could
      accidentally change behavior at one call site but not the other, or
      leave the .git exclusion behavior altered.
    - The fixture might not faithfully reproduce the real bug shape (e.g.
      too shallow to trigger ambiguous-basename detection).
  Why each does not occur:
    - ".claude" is matched as an exact `dirnames` entry (a directory
      basename equality check, not a substring or pattern match), and
      `git ls-tree -r --name-only HEAD` confirms nothing tracked lives at
      or under any path component literally named ".claude" — so no real,
      tracked reference can be affected.
    - Confirmed directly per the design agreement's Settled Ambiguities:
      `git ls-tree -r --name-only HEAD | grep "^\.claude/"` returns
      nothing, i.e. nothing under `.claude/` anywhere is tracked, so
      excluding the whole subtree loses no real, contract-relevant content
      regardless of what else might later be placed there.
    - `git diff scripts/check-contract-consistency.py` (pasted in the
      Preflight Validation section of WP-0020) shows the constant applied
      identically at both prune sites, and the post-fix real-repository
      run reproduces the exact same "all checks passed" baseline as the
      pre-fix run, confirming the .git exclusion itself is unchanged in
      effect.
    - The fixture was built from this repository's actual tracked working-
      tree content (via `git archive HEAD | tar -x`, not synthetic minimal
      files), duplicated once under `.claude/worktrees/fake-sibling/`,
      exactly per LISS-0058's own "Required reproduction" steps and the
      design agreement's Settled Ambiguities — and it did in fact produce
      906 genuine failures pre-fix, confirming it faithfully reproduces
      the bug shape.
  ```

## Verification

- Pre-fix fixture run showing real ambiguous-basename noise (pasted, not
  summarized).
- Post-fix fixture run showing the noise is gone (pasted).
- Post-fix run against this issue's own real worktree
  (`python3 scripts/check-contract-consistency.py`) showing no new failure.
- `git diff` showing the change is confined to the two named `os.walk`
  prune lines.
