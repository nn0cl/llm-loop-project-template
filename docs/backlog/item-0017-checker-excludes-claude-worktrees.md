# Backlog item: item-0017-checker-excludes-claude-worktrees

## Metadata

- Item ID: item-0017
- Title: `check-contract-consistency.py` must exclude `.claude/worktrees/`
  from its file scan
- Status: promoted
- Created: 2026-08-20
- Updated: 2026-08-20
- Priority hint: high
- Suggested planning size: S
- Owner/agent (optional): unassigned

## Summary

`scripts/check-contract-consistency.py`'s `scanned_files()` walks the
repository with `os.walk(repo)`, excluding only `.git`:

```python
dirnames[:] = [d for d in dirnames if d != ".git"]
```

`.claude/worktrees/<agent-id>/` directories — created by this environment's
Agent-tool worktree isolation, each a full nested checkout of the
repository — are not excluded. When multiple sub-agent worktrees exist
simultaneously under the main repository's own working directory (the
normal, expected state throughout this session's whole two/three-layer
loop, per ADR 0016/0017) and the checker is run directly from the main
worktree root (not from an isolated `/tmp` checkout), every file the
checker scans is found duplicated once per active nested worktree, and any
check that expects a unique answer for a referenced filename reports it as
ambiguous. Confirmed directly this session: running the checker from the
main worktree while 3 worktrees were present under `.claude/worktrees/`
produced over 20,000 characters of "which N files answer to this... write
the path" noise for filenames that are genuinely unambiguous in the actual
tracked repository content.

This went undetected all session because every independent verification
this session performed used a fresh, isolated `git worktree add --detach
/tmp/verify-...` checkout (which never contains a `.claude/worktrees/`
subdirectory of its own), never the main worktree directly while sibling
agent worktrees were active.

## Why it might matter

A Backlog-thread or Design & Review session that runs the checker directly
from the main worktree — a completely normal, expected action, and in fact
the Director's own default expectation absent the `/tmp`-isolation
workaround this session happened to adopt — gets a wall of false-positive
noise that could mask a real failure, or train whoever's running it to
distrust the checker's output. `.claude/` is local, ephemeral,
harness-managed scratch state; it should never have been in scope for a
contract-consistency check about this repository's actual tracked content.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes — one-line-shaped fix
  to `scanned_files()`'s existing exclusion pattern.
- Boundaries or non-goals:
  - Do not change what counts as a real, in-scope reference failure —
    this only removes ephemeral harness-local directories from the scan,
    it doesn't relax any actual check.
  - Consider whether other harness-local or tool-local directories beyond
    `.claude/` need the same treatment (e.g. anything else this
    environment or an adopter's own tooling might place at the repo root)
    — Design & Review's call on how broad to make the exclusion.
  - `scripts/check-contract-consistency.py` is not itself an ADR-0006
    contract file, but treat it with the review rigor already established
    for every change to this script this session (it has a six-round
    review history in this repository, per the 2026-08-02 records).

## Uncertainty

- [x] Spec can be written now — reproducible, narrow, root cause identified
      with the exact line.
- [ ] Spike required first
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none — related: `scripts/check-contract-consistency.py`
  (`scanned_files()`), discovered while verifying item-0016's spike work

## Promotion notes

- Date: 2026-08-20
- Decision: Promoted, in the Backlog-layer thread, immediately at capture
  (found and confirmed directly by the Backlog thread while verifying
  item-0016's spike results). Per ADR 0016 Rule 2, Design & Review
  proceeds autonomously from here.
- Reason: Narrow, well-evidenced, root cause already identified; ready to
  run.
