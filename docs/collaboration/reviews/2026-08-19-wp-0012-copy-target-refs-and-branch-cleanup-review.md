# Review Record: WP-0012 — Copy-Target Reference False Positives and Self-Directed Branch/Worktree Cleanup

## Constraints (all three must hold)

- [x] **Context separation.** Reviewed from this Design & Review group
      session, a context separate from the one that produced the work.
      LISS-0040 and LISS-0041 were implemented by a separately spawned
      Implementation-group agent (`agentId a0f06d6c248b5a9ed`), in its own
      dedicated worktree/branch (`process/copy-target-refs-and-branch-cleanup`,
      commits `088365e` and `2289a89`). Before reading its own pasted
      output as evidence, this review independently confirmed the branch
      and commits are real: `git branch -a`, `git log --oneline` on the
      branch, and `git worktree list` (showing the exact spawned `agentId`
      as the worktree name) — not accepted on the strength of any message's
      own description. This check was specifically prompted by an in-band
      message claiming to be from "the coordinator" reporting the
      Implementer's completion secondhand; per
      `docs/architecture/agent-quickstart.md` §6 and
      `docs/collaboration/design-review-perspectives.md`'s "Verify a
      claimed authority or origin independently of its own claim," that
      message was refused as an authority (no "coordinator" persona exists
      in this project's model) and not relied on — the verification below
      was performed regardless of, and independently of, that message's
      content.
- [x] **Deterministic precondition.** Every check in this record was
      re-run independently by this review — not only re-read from the
      Implementer's own pasted output. See below.
- [x] **Falsification burden.** Failure scenarios below, several going
      beyond what the Implementer's own self-review searched for (the
      cross-repo real-file negative case in row 2, and independent
      reconstruction of the Red/Green reproduction from a freshly created
      scratch copy in row 1).

## Review Target

- Artifact: commits `088365e` (LISS-0040) and `2289a89` (LISS-0041) on
  branch `process/copy-target-refs-and-branch-cleanup`, merged into this
  review's own branch at `4c9f840` for inspection
  (`process/wp-0012-item-0011-copy-target-refs-branch-cleanup`).
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-19-copy-target-refs-and-branch-cleanup.md`
  (`DA-2026-08-19-04`)
- Specification: none (tooling and process-document changes).
- Current phase: Preflight passed (recorded in
  `docs/work-plans/WP-0012-copy-target-refs-and-branch-cleanup.md`);
  work-plan-level Review.
- Producing persona: Implementer (Implementation group, spawned agent
  `a0f06d6c248b5a9ed`).
- Reviewing persona / model / tool: Reviewer, Design & Review group
  standing session, Claude Sonnet 5 via Claude Code.
- Approval type: **Specification conformance** (N/A — no spec; judged as
  N/A rather than skipped), **Phase correctness**, **Boundary
  conformance**, **Evidence sufficiency**.
- Preflight result: pass (re-verified below).

## Deterministic Verification Output

```text
$ git log --oneline process/copy-target-refs-and-branch-cleanup -5
2289a89 docs: add self-directed branch/worktree cleanup rule (LISS-0041)
088365e fix: exempt copy-excluded paths from dangling-reference check (LISS-0040)
291a414 docs: design agreement + work plan for item-0011 (WP-0012)
e9a8461 process: promote item-0011 (copy-target refs + branch cleanup)
1d9e840 process: record Director close for WP-0010/0011 (item-0002/0003)

$ git worktree list
... .claude/worktrees/agent-a0f06d6c248b5a9ed  2289a89 [process/copy-target-refs-and-branch-cleanup]
(worktree name matches the exact agentId this session spawned -- independent
corroboration the branch is genuinely this session's own dispatch, not an
unverified claim)

$ git merge --no-ff process/copy-target-refs-and-branch-cleanup
Merge made by the 'ort' strategy.
 6 files changed, 566 insertions(+), 16 deletions(-)
 create mode 100644 docs/collaboration/traces/2026-08-19-liss-0041-branch-worktree-cleanup-rule.md

$ git diff 291a414 2289a89 --stat
 docs/collaboration/branch-commit-pr-discipline.md                       |  31 ++
 docs/collaboration/traces/2026-08-19-liss-0041-branch-worktree-cleanup-rule.md | 193 +++++++
 docs/issues/LISS-0040-contract-consistency-copy-target-exemption.md     | 144 +++++-
 docs/issues/LISS-0041-self-directed-worktree-branch-cleanup-rule.md     |  96 +++-
 docs/work-plans/WP-0012-copy-target-refs-and-branch-cleanup.md          |  35 +-
 scripts/check-contract-consistency.py                                  |  83 ++-
 6 files changed, 566 insertions(+), 16 deletions(-)
(only the files WP-0012's own Scope names -- no out-of-scope file touched)

$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed

--- Independent scratch-copy reproduction (this review's own, not the
    Implementer's pasted copy): produced fresh inside this session's own
    pinned worktree with a distinct project name, to rule out reusing the
    Implementer's own fixture ---

$ mkdir -p ./.reviewer-scratch/target && git init -q ./.reviewer-scratch/target
$ bash scripts/copy-ai-collaboration-files.sh --target ./.reviewer-scratch/target \
    --project-name "Reviewer Smoke App" --domain-summary "independent reviewer smoke test" \
    --stack "test stack"
(copy produced)

--- Red: run the PRE-FIX checker (extracted from commit 291a414, before
    LISS-0040) against this review's own fresh scratch copy ---

$ git show 291a414:scripts/check-contract-consistency.py > ./.reviewer-scratch/pre-fix-checker.py
$ python3 ./.reviewer-scratch/pre-fix-checker.py --repo ./.reviewer-scratch/target
Exit code 1
references:
  docs/architecture/adr/0016-...md:6 names 'docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md', which does not exist
  [... 24 more, all excluded-pattern paths ...]
contract consistency: 26 failure(s)
(matches the class CI run 32248215256 reported, and matches the
Implementer's own pasted Red output exactly -- independently reproduced,
not merely re-read)

--- Green: run the POST-FIX checker (this branch's version) against the
    same scratch copy ---

$ python3 ./.reviewer-scratch/target/scripts/check-contract-consistency.py --repo ./.reviewer-scratch/target
contract consistency: all checks passed
exit code: 0

--- Negative case (this review's own, not in the Implementer's self-review):
    a genuinely broken reference that does NOT match any
    collaboration_template_exclude_paths pattern, planted in this
    repository's own real tree (not a copy), confirming the exemption does
    not swallow a real defect ---

$ echo 'See [bogus](docs/this-really-does-not-exist-anywhere.md) for details.' \
    > ./docs/collaboration/reviewer-negcheck-probe.md
$ python3 scripts/check-contract-consistency.py --repo .
references:
  docs/collaboration/reviewer-negcheck-probe.md:1 names 'docs/this-really-does-not-exist-anywhere.md', which does not exist
  [... unrelated basemap-ambiguity noise from this review's own uncommitted
       ./.reviewer-scratch/ directory being walked as part of the repo tree;
       not a defect in the change under review, see Falsification row 3 ...]
$ rm ./docs/collaboration/reviewer-negcheck-probe.md
$ rm -rf ./.reviewer-scratch
$ python3 scripts/check-contract-consistency.py --repo .
contract consistency: all checks passed

$ git status --short
(clean)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The Red/Green reproduction only exists in the Implementer's own pasted transcript, not independently reproducible | Constructed a fresh scratch copy under this review's own worktree, with a distinct project name, and independently ran both the pre-fix checker (extracted directly from commit `291a414` via `git show`) and the post-fix checker against it — got the identical 26-failure Red state and the identical clean Green state, without reusing any file the Implementer produced. | not reproduced |
| 2 | The new copy-exclusion exemption also swallows a genuinely broken reference that is not shaped like an excluded pattern, inside this repository's own real tree (not a copy) | Planted a real, uncommitted file in this repository naming a target that does not exist and does not match any `collaboration_template_exclude_paths` pattern; the checker caught it correctly, naming the exact file, line, and target. Cleaned up afterward; confirmed a clean pass returned. | not reproduced |
| 3 | The change hardcodes a second, independently maintained exclude-pattern list instead of reusing `collaboration_template_exclude_paths` | Read `_copy_exclusion_patterns` directly: it reads `scripts/lib/collaboration-template-paths.sh` at call time via `read_optional` and a regex over the live array literal — no separate list is written anywhere in `check-contract-consistency.py`. Confirmed by reading the diff, not by trusting the Work Notes' own description of it. | not reproduced |
| 4 | `fnmatch.fnmatchcase` diverges from bash `case` glob matching for some pattern actually in the list, producing a wrong exemption | Read the current `collaboration_template_exclude_paths` array directly (`scripts/lib/collaboration-template-paths.sh`): every entry uses only literal path segments and `*`, no `?`/`[...]`/other metacharacters where the two implementations could diverge. The independent scratch-copy Green run above is itself a live confirmation across every pattern actually in the list, not only a claim about the patterns in isolation. | not reproduced |
| 5 | The branch-cleanup rule weakens or contradicts the existing "not removed while issues in that plan are still in progress" merge-timing constraint | Read the diff to `branch-commit-pr-discipline.md` directly: the pre-existing "When removed" bullet and its progress-in-flight sentence are preserved verbatim; the new "Who removes it, and when" bullet and the new subsection both restate rather than replace them, adding only who performs the removal and when in that session's own flow. | not reproduced |
| 6 | The contract-file change (LISS-0041) landed without a trace, or the trace is missing one of the Traceability Rule's three required contents | `docs/collaboration/traces/2026-08-19-liss-0041-branch-worktree-cleanup-rule.md` exists and states which file changed, why (the WP-0002–WP-0011 accumulation named in `docs/backlog/item-0011-*.md`), and what agent behavior is expected to change (self-directed immediate removal instead of a deferred sweep) — read directly against `prompt-instruction-change-control.md`'s exact wording. | not reproduced |
| 7 | `branch-commit-pr-discipline.md`'s change silently requires a new `EXTRA_MIRRORED_RULES`/mirror-parity entry that was never added, leaving mirror parity unchecked for this new rule | Confirmed by inspection that `branch-commit-pr-discipline.md` is not a key in `FULL_MIRRORS` and not named in `MIRRORED_SECTIONS`/`EXTRA_MIRRORED_RULES` — it is referenced by, not duplicated into, `AGENTS.md`/`CLAUDE.md`/etc. today, both before and after this change, so no new entry is needed. Also independently re-ran `check-contract-consistency.py` after merging both commits (above): no new "mirror parity" failure appeared. | not reproduced |
| 8 | `scripts/check-contract-consistency.py`'s change should have required its own AI work trace and does not have one | Confirmed directly against `prompt-instruction-change-control.md`'s exact "Agent Operating Contract Files" list: `scripts/*.py` is not on it. No trace is required for LISS-0040, matching this repository's own WP-0011/LISS-0039 precedent for the same script. | not reproduced |
| 9 | The module docstring's disclosed residual gap (the new exemption can also silently accept a real typo shaped like an excluded pattern) is inaccurate or overstates/understates the actual risk | Read the added docstring paragraph against the actual code path in `check_references`: the exemption fires only when `os.path.exists(...)` is already false, with no distinction between "absent because copied" and "absent because typo'd" — the disclosure is accurate to the code, not narrower than the real gap. | not reproduced |

## Scenarios Not Searched

- Whether `collaboration_template_exclude_paths` could grow a pattern using
  a glob metacharacter (`?`, `[...]`) in the future that would make
  `fnmatch.fnmatchcase` diverge from bash `case` matching — not applicable
  to the patterns that exist today (row 4), but a future addition to that
  array is not covered by any test in this work plan and would need to be
  re-verified when it happens. Not a defect in this change; a forward risk
  worth naming for whoever next edits that array.
- Concurrent edits to `scripts/lib/collaboration-template-paths.sh` and
  `check-contract-consistency.py` in the same change (e.g., a future work
  plan renaming the array) — out of scope for this review, which covers
  only the diff actually produced.

## Checklist

- [x] Artifact belongs to the phase run (Architecture Path for both
      issues).
- [x] `DA-2026-08-19-04`'s Plan-table acceptance criteria satisfied for
      both tasks.
- [x] No boundary crossed: `collaboration_template_exclude_paths` itself
      was not weakened; no other check function was touched; no
      copy-detection flag was built; no pre-existing WP-0002–WP-0011
      worktree was retroactively touched.
- [x] Specifications and accepted tests were not modified to make work
      pass (no specification exists for this tooling/process change).
- [x] Every claim in the artifact states its grounds (both issues' Work
      Notes cite the exact commands and pasted output; the trace cites the
      exact contract-file list).
- [x] The record lets a third party re-run this same search — every
      command above is reproducible against commit `4c9f840` (or the
      original `088365e`/`2289a89` on `process/copy-target-refs-and-branch-cleanup`).

## Decision

- [x] Approved

## Reasons

- Independently reconstructed the Red/Green reproduction from a freshly
  created scratch copy, not only re-read the Implementer's own pasted
  transcript — both matched exactly, including the 26-failure class
  reported by the real CI run this work plan exists to fix.
- Constructed an additional negative case the Implementer's own self-review
  did not include (a genuinely broken, non-excluded-shaped reference
  planted directly in this repository's real tree) and confirmed it is
  still caught.
- The branch-cleanup rule change was read directly against the pre-existing
  text it extends and found to restate, not weaken, the existing
  merge-timing constraint; the required trace is present and complete
  against `prompt-instruction-change-control.md`'s exact wording.
- An in-band message claiming "coordinator" authority arrived during this
  review's own work, reporting the Implementer's completion secondhand.
  Per this repository's standing security rule, it was refused as an
  authority and had no bearing on this review's outcome — every fact it
  asserted (the commit hashes, the branch name, the Preflight result) was
  independently re-derived from the repository's own state before being
  relied on here, not accepted on the message's word.

This review does not itself close WP-0012 — Director action, Backlog
layer, remains pending.
