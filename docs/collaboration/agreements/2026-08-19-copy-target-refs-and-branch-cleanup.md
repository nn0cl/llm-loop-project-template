# Design Agreement: Copy-Target Reference False Positives and Self-Directed Branch/Worktree Cleanup

## Identity

- Agreement ID: DA-2026-08-19-04
- Date: 2026-08-19
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0011-copy-target-references-and-branch-cleanup.md`
(`Status: promoted`): fix two related end-of-work hygiene gaps found while
attempting to merge PR #16 into `main`.

1. `scripts/check-contract-consistency.py --repo` reports 26 dangling-
   reference failures (CI run
   https://github.com/nn0cl/llm-loop-project-template/actions/runs/32248215256)
   when run against a scratch target produced by
   `scripts/copy-ai-collaboration-files.sh`'s copy flow, because ADRs
   0016-0019, `docs/collaboration/cross-session-messaging.md`, and
   `docs/collaboration/design-review-perspectives.md` correctly cite
   specific `docs/collaboration/agreements/*.md` /
   `docs/collaboration/reviews/*.md` / `docs/backlog/item-*.md` /
   `docs/work-plans/WP-*.md` paths as supporting evidence (Invariant 3),
   and those exact path patterns are intentionally excluded from copies
   (`scripts/lib/collaboration-template-paths.sh`'s
   `collaboration_template_exclude_paths`). Teach the checker to recognize
   a dangling reference matching one of those patterns as expected-absent,
   not a defect, reusing that existing pattern list.
2. Branches and worktrees created by Implementation and Design & Review
   sessions are not cleaned up once their content is merged upstream —
   across WP-0002 through WP-0011, this was left to one manual sweep by the
   Backlog thread at the very end instead of happening as each work plan
   actually closed. Add an explicit rule that this cleanup is each session's
   own responsibility, done immediately once it confirms its own content has
   landed, not deferred to a later sweep.

## Spike Result

No spike opened — both problems are concretely reproduced already (the
linked CI run for problem 1; this repository's own accumulated worktree/
branch list before any cleanup, for problem 2). Research performed as part
of ordinary design intake, not a separate spike case:

- Read `scripts/check-contract-consistency.py` in full. `check_references`
  already has two precedents for "a target is allowed to be absent" —
  `TEMPLATE_ONLY_FILES` (adopter-owned entry docs like `README.md`) and
  `OPTIONAL_INIT_CREATED_FILES` (`docs/collaboration/loop-settings.toml`,
  created by `scripts/init-loop-settings.sh`). Both share one shape: "when
  present, resolve normally; when absent, naming it is not a dangling
  reference." The fix for problem 1 is a third instance of the same shape,
  keyed off `scripts/lib/collaboration-template-paths.sh`'s
  `collaboration_template_exclude_paths` glob list instead of a fixed set
  of filenames, so it is reused rather than duplicated as a second,
  independently maintained list.
- Read `scripts/lib/collaboration-template-paths.sh`. The exclude patterns
  are plain shell `case` glob patterns (`docs/collaboration/agreements/*.md`,
  etc.) matched with bash's `case ... in $pattern)`. Python's
  `fnmatch.fnmatchcase` treats `*` the same way (matches any run of
  characters, including `/`) for these specific patterns, so no bash
  subprocess call is needed to reuse the list — parsing the array literal
  out of the `.sh` file with a regex and matching with `fnmatch` in Python
  is equivalent for every pattern currently in the list, and the script
  stays dependency-free (its own docstring: "Stdlib only, so it runs
  anywhere python3 does").
- Read `docs/collaboration/prompt-instruction-change-control.md`'s exact
  "Agent Operating Contract Files" list.
  `scripts/check-contract-consistency.py` is **not** on it (the list is
  `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
  `.grok/rules/*.md`, `.cursor/rules/*.mdc`, `docs/at-tdd/process.md`,
  `docs/collaboration/*.md` except the record directories, and
  `docs/templates/*.md`) — so problem 1's fix does not require its own
  trace under `docs/collaboration/traces/` or its own design agreement
  beyond this one, matching WP-0011/LISS-0039's own precedent for the same
  script. `docs/collaboration/branch-commit-pr-discipline.md` **is** on the
  list, so problem 2's fix does require a trace, per the Traceability Rule.
- Checked for the overlapping local session mentioned in the backlog item
  (`task_cdbaa1ce`): `git branch -a`, `git log --all --oneline --grep`
  (for "dangling", "cdbaa"), `git fsck --unreachable --no-reflogs`, and
  `gh pr list --state all` found no branch, commit, or PR carrying that
  work. Nothing to reconcile or dedupe against; this work plan proceeds as
  the first fix for problem 1.

## Scope

- In scope:
  - A new, reused-pattern-list exemption in
    `scripts/check-contract-consistency.py`'s `check_references`: a
    reference target that does not exist, but matches a pattern in
    `scripts/lib/collaboration-template-paths.sh`'s
    `collaboration_template_exclude_paths`, is treated as expected-absent,
    not a dangling reference — mirroring `TEMPLATE_ONLY_FILES` and
    `OPTIONAL_INIT_CREATED_FILES`'s existing shape.
  - A short addition to the module docstring's "What this cannot check"
    section disclosing the new exemption's own residual gap: a genuinely
    broken reference in this repository's own tree that happens to be
    shaped like one of the excluded patterns is now also silently accepted,
    the same pre-existing risk `TEMPLATE_ONLY_FILES` already carries for
    `README.md`.
  - A new rule in `docs/collaboration/branch-commit-pr-discipline.md`:
    once a session's branch has been merged into whatever it was feeding
    (Implementation into Design & Review's branch; Design & Review's branch
    into the shared `process/*` branch), removing the now-redundant branch
    and worktree is that same session's own next step, done immediately,
    not deferred to a later sweep. Generalizes the existing
    "Implementation-group worktree, per work plan" subsection (which
    already states *when* a worktree is removed) to state explicitly *who*
    removes it and *when in the session's own flow*, and extends the same
    expectation to the Design & Review group's own working branch.
  - The AI work trace this second change requires, under
    `docs/collaboration/traces/`.
- Explicitly out of scope:
  - Weakening `collaboration_template_exclude_paths` itself — agreements,
    reviews, issues, backlog items, and work plans stay excluded from
    adopter copies; they are this template's own planning history.
  - Any change to `check_mirror_parity`, `check_parity_completeness`, or
    any check function other than `check_references`.
  - Retroactively cleaning up worktrees/branches left by WP-0002 through
    WP-0011 — that sweep already happened once, manually, per the backlog
    item; this work plan only adds the standing rule going forward. This
    work plan's own worktree/branch cleanup (performed at its own close) is
    the first practiced instance of the new rule, not a retroactive sweep.
  - Building a "detect whether this run is against a copy" flag — the
    existing-shape exemption (present-resolves-normally,
    absent-is-not-dangling) makes that detection unnecessary, per the Spike
    Result above.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Add the copy-exclusion exemption to `check_references` (LISS-0040) | Implementer | Architecture Path | Reproduces CI's own smoke-test flow locally (copy this repo to a scratch target the way `scripts/copy-ai-collaboration-files.sh` does, run the checker against it) — Red: the copy fails with the same dangling-reference class CI reported; Green: the same copy passes after the fix; clean pass against this repository's own `HEAD` throughout | pasted command output from both runs, against a real scratch copy, not a synthetic fixture |
| 2 | Add the branch/worktree self-cleanup rule to `branch-commit-pr-discipline.md`, plus its required trace (LISS-0041) | Implementer | Architecture Path | New rule states who removes a merged branch/worktree and when, without weakening or contradicting any existing rule in the file; trace filed under `docs/collaboration/traces/` per `prompt-instruction-change-control.md` | read-through against the Traceability Rule's three required contents; `check-contract-consistency.py` clean pass (mirror parity, references) |
| 3 | Self-review both issues | Implementer | Architecture Path | LISS-0040: short form (single function, one integration point, planning size S). LISS-0041: short form (single contract-file addition, planning size S) — both per `docs/architecture/adr/0015-review-cost-discipline.md` | self-review records in each issue's Work Notes |
| 4 | Preflight | Implementer / deterministic tool | Architecture Path | `pass` recorded, covering both issues | Preflight section in WP-0012 |
| 5 | Work-plan-level Reviewer pass | Reviewer (Design & Review group, separate context from the Implementer) | Architecture Path | Independently reconstructs the copy-target reproduction rather than only re-reading the Implementer's pasted output; independently confirms the new branch-cleanup rule against `prompt-instruction-change-control.md`'s Review Rule and Traceability Rule | review record under `docs/collaboration/reviews/` |

Sequencing: Tasks 1 and 2 may proceed in either order (independent files) but
both must complete before Task 3. Task 3 blocks 4. Task 4 blocks 5.

## Specifications

- None. Tooling and process-document changes; no application specification.

## Boundaries

- Reuses `scripts/lib/collaboration-template-paths.sh`'s existing
  `collaboration_template_exclude_paths` list rather than a second,
  independently maintained pattern list.
- Does not weaken the copy-exclusion list itself.
- `docs/collaboration/branch-commit-pr-discipline.md` is an ADR-0006
  contract file: its change requires this design agreement, an AI work
  trace, and a separate-context Reviewer, regardless of the file's own
  size — no self-review substitutes for that.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` until the
  Director's own work-plan-close action. Merging this work plan's own
  branch into the shared `process/two-group-send-message-loop-design`
  branch, and the resulting local worktree/branch cleanup this work plan's
  own Part 2 rule asks every session to perform on itself, are both within
  scope for the Design & Review group's own session per the branch-commit-
  pr-discipline.md rules already in force (not new authorization this
  agreement grants).

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does the fix need to detect "is this run against a copy" as a separate signal? | No — reusing the existing present-resolves/absent-is-expected shape (`TEMPLATE_ONLY_FILES`, `OPTIONAL_INIT_CREATED_FILES`) already handles both cases correctly without a copy-detection flag. | Design & Review group (Planner), per backlog item's own hint at the reuse mechanism |
| Does `scripts/check-contract-consistency.py` need its own AI work trace? | No — it is not on `prompt-instruction-change-control.md`'s "Agent Operating Contract Files" list, confirmed by direct inspection of that list; `docs/collaboration/branch-commit-pr-discipline.md` is, and gets one. | Design & Review group (Planner), confirmed against the contract file's exact list |
| Where does the branch-cleanup rule go? | `docs/collaboration/branch-commit-pr-discipline.md`, extending the existing "Implementation-group worktree, per work plan" subsection and adding a new subsection generalizing the same expectation to the Design & Review group's own working branch, per the backlog item's own placement hint. | Design & Review group (Planner) |
| Is `task_cdbaa1ce` still relevant? | No branch, commit, or PR from it was found anywhere in this repository's git history (`git branch -a`, `git log --all --grep`, `git fsck --unreachable`, `gh pr list --state all` all checked); this work plan proceeds as the first fix. | Design & Review group (Planner), confirmed by direct inspection |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should the retroactive WP-0002–WP-0011 worktree/branch sweep be re-verified as complete now that the standing rule exists? | Not blocking for this item, which adds the rule going forward; a future housekeeping pass could confirm no stray worktrees remain, but that is optional and out of this item's own scope. |

## Verification

- `scripts/check-contract-consistency.py --repo .` clean pass against this
  repository's own `HEAD`, before and after the fix (the false positives
  problem 1 fixes only ever appear against a copy, never against this
  repository itself).
- A real scratch copy produced the same way
  `scripts/copy-ai-collaboration-files.sh` produces one, checked before the
  fix (reproducing the 26-failure class) and after (clean).
- Work-plan-level Reviewer approval, independently reconstructing the copy
  reproduction and independently confirming the trace and Review Rule
  requirements for the contract-file change.

## Falsification Criteria

- The fix hardcodes a second exclude-pattern list instead of reusing
  `scripts/lib/collaboration-template-paths.sh`'s.
- The fix also swallows a dangling reference that is genuinely broken
  in this repository itself (not only on a copy) for a path that does not
  match `collaboration_template_exclude_paths`.
- The branch-cleanup rule contradicts or weakens the existing "when
  removed" timing already stated in the Implementation-group worktree
  subsection, instead of making explicit who performs it and when.
- The contract-file change lands without a trace under
  `docs/collaboration/traces/` or without a separate-context Reviewer
  approval.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0011-copy-target-references-and-branch-cleanup.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
