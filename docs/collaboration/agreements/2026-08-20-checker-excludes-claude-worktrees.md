# Design Agreement: `check-contract-consistency.py` excludes `.claude/`

Store the completed record at
`docs/collaboration/agreements/2026-08-20-checker-excludes-claude-worktrees.md`.

See `docs/collaboration/design-agreement.md` for the rules this record
implements.

## Identity

- Agreement ID: DA-2026-08-20-03
- Date: 2026-08-20
- Director: per ADR 0016 Rule 2, backlog-item-level agreement — see
  "Agreement" below.
- Planner / Specifier personas (model or tool used): Design & Review group,
  standing session (Claude Code, Planner/Specifier persona).
- Supersedes agreement (if any): none.

## Direction

`docs/backlog/item-0017-checker-excludes-claude-worktrees.md`
(`Status: promoted`, promoted "immediately at capture" by the Backlog
thread, per its own Promotion notes): fix `scripts/check-contract-consistency.py`'s
`scanned_files()` (and, by the same root cause, `check_references()`'s own
identical `os.walk` exclusion) so `.claude/worktrees/<agent-id>/` — full
nested repository checkouts this environment's Agent-tool worktree
isolation creates — are excluded from the file scan, the same way `.git`
already is. Per ADR 0016 Rule 2, this item was never a check-in item (only
item-0016 carries that exception); Design & Review proceeds fully
autonomously.

## Scope

- In scope: the two `os.walk` prune-line fixes in
  `scripts/check-contract-consistency.py`; a fixture-based before/after
  reproduction of the false positive.
- Explicitly out of scope: any other check function's logic;
  `SCANNED_SUFFIXES`/`RECORD_DIRS`/any other exclusion constant; any
  relaxation of a genuine reference-failure check.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Build a fixture reproducing the false positive (nested `.claude/worktrees/` copy of real tracked content) and confirm the noise against the pre-fix script | Implementer | Fast Path | Real ambiguous-basename failures reported, pasted in full | `python3 scripts/check-contract-consistency.py --repo <fixture>` |
| 2 | Apply the fix (exclude `.claude` alongside `.git` at both `os.walk` sites) | Implementer | Fast Path | `git diff` confined to the two prune lines (or a shared constant factoring them) | `git diff scripts/check-contract-consistency.py` |
| 3 | Re-run the same fixture and the real repository, confirm no more false-positive noise and no regression | Implementer | Fast Path | Fixture run shows the noise gone; real-repo run shows no new failure | Same command, pasted output, before/after diff |
| 4 | Preflight Validation over the whole work plan | Implementer | Preflight | All checks above recorded with real output | WP-0020's own Preflight Validation section |
| 5 | Work-plan-level Reviewer pass | Reviewer | Review | Approval record addressing evidence-sufficiency explicitly | `docs/collaboration/reviews/2026-08-20-wp-0020-....md` |

Sequencing and dependencies: strictly 1 -> 2 -> 3 -> 4 -> 5; the fix must
not be applied before the pre-fix reproduction is captured, or the "before"
evidence is lost.

## Specifications

No `docs/specs/` file covers this work plan — a narrow tooling bug fix, not
application or process behavior with its own acceptance spec.

## Boundaries

- No change to any check function's own logic beyond the two named
  `os.walk` prune lines.
- No change to what counts as a genuine, in-scope reference failure.
- No touch to any file other than `scripts/check-contract-consistency.py`
  (plus, transiently, the throwaway fixture directory, which is not part of
  the repository and is not committed).

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Should the fix exclude only `.claude/worktrees`, or the whole `.claude` top-level directory? | The whole `.claude` directory — confirmed via `git ls-tree -r --name-only HEAD \| grep "^\.claude/"` that nothing under `.claude/` anywhere is tracked, so the broader exclusion loses no real content and is simpler/more future-proof than special-casing one subdirectory; the backlog item's own text explicitly leaves this breadth choice to Design & Review | Design & Review group (Planner), recorded in LISS-0058's Acceptance Notes |
| How should the false positive be reproduced, given neither the Design & Review nor the Implementation session can necessarily run the checker from the actual main-repo root with real sibling worktrees present (worktree-isolated sandboxing)? | A controlled fixture: copy real tracked content into a throwaway directory, then copy it again into `<fixture>/.claude/worktrees/fake-sibling/`, and run the checker with `--repo <fixture>` — faithfully reproduces the nested-full-checkout mechanism without depending on transient real sibling-worktree state | Design & Review group (Planner), recorded in LISS-0058's "Required reproduction" section |

## Deferred Questions

None — this is a fully bounded, single-issue work plan with no open
question left for later.

## Verification

- Fixture-based before/after reproduction (pasted output, both runs).
- `python3 scripts/check-contract-consistency.py` (default `--repo .`)
  against the real repository, before and after — no regression.
- `git diff scripts/check-contract-consistency.py` confined to the stated
  scope.

## Falsification Criteria

This design was wrong if, after execution:

- The fixture's pre-fix run does not actually reproduce ambiguous-basename
  noise (meaning the fixture does not faithfully model the real bug, or the
  bug does not exist as described).
- The fixture's post-fix run still shows noise (fix incomplete).
- The real-repository run after the fix shows a new failure that did not
  exist before (regression from the fix itself, e.g. a real reference
  legitimately living under a name coincidentally excluded).
- The diff touches any file, function, or constant beyond what this
  agreement's Scope names.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. — Per ADR 0016
      Rule 2's backlog-item-level agreement:
      `docs/backlog/item-0017-checker-excludes-claude-worktrees.md`'s own
      Promotion notes state the item was "Promoted, in the Backlog-layer
      thread, immediately at capture... Design & Review proceeds
      autonomously from here," with the bug already "confirmed directly
      this session" including the exact reproduction evidence quoted in
      the backlog item's own Summary.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Nothing in them requires guessing at a rule
      that was never stated. — Design & Review group (Planner), 2026-08-20.
      The exact code change, the exact reproduction methodology, and the
      one genuinely open breadth question (whole `.claude` vs. only
      `.claude/worktrees`) are all settled above, not left for the
      Implementer to guess.

If the AI cannot make its statement, the design phase is not finished,
regardless of the Director's readiness to proceed.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
