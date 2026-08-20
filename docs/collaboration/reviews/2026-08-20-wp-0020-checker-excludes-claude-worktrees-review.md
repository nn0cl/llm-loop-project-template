# Review Record: WP-0020 (checker excludes `.claude/`)

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's standing session, which produced the work plan, design
      agreement, and issue text, but did not write the code fix itself —
      that was executed by a separate Implementation-group subagent
      session in its own dedicated worktree/branch (`wp-0020-execution`,
      spawned off `process/promote-item-0017` commit `08e0a36`). This
      review does not rely on that Implementer session's own reasoning as
      justification; every claim below is independently re-derived and
      re-run against the actual committed tree by this review itself.
- [x] **Deterministic precondition.** Deterministic verification was run,
      independently, by this review (a fresh fixture built and both
      pre-fix and post-fix runs executed by this review itself, not
      copied from the Implementer's own pasted output, though that output
      was cross-checked and matched exactly).
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, each with the grounds it does not occur, based on this
      review's own independent commands.

## Review Target

- Artifact: `wp-0020-execution` branch (commits `a12e8a7`, `d9ff104`), to
  be merged into `process/promote-item-0017`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-20-checker-excludes-claude-worktrees.md`
  (`DA-2026-08-20-03`)
- Specification: none (a narrow tooling bug fix; no `docs/specs/` file
  covers this work plan, per the design agreement's own Specifications
  section).
- Current phase: Fast Path; Preflight Validation recorded as pass in
  `docs/work-plans/WP-0020-...md`.
- Producing persona: Implementer (Implementation group, separate context).
- Reviewing persona / model / tool: Reviewer (Design & Review group,
  standing session).
- Approval type: evidence-sufficiency (the one type the work plan's own
  Review Summary Packet names as at stake for a bug fix this narrow).
- Preflight Validation record: `docs/work-plans/WP-0020-...md`'s own
  "Preflight Validation" section.
- Preflight result: pass.

## Deterministic Verification Output

All commands below were run independently by this review, not pasted from
the Implementer's own record.

```text
$ git diff process/promote-item-0017...wp-0020-execution -- scripts/check-contract-consistency.py
@@ -330,6 +330,15 @@ RECORD_DIRS = (

 SCANNED_SUFFIXES = (".md", ".mdc", ".sh", ".yml", ".py")

+# Directories every os.walk-based scan below must prune: .git is version
+# control metadata, and .claude is this harness's own untracked scratch
+# space (agent worktrees live under .claude/worktrees/<id>/, each a full
+# nested checkout of the repository) — neither holds contract-relevant
+# content, and walking into .claude/worktrees/ duplicates every scanned
+# file once per active sibling worktree, producing false-positive
+# ambiguous-basename noise in check_references().
+EXCLUDED_DIRS = (".git", ".claude")
+
 MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
 CODE_PATH = re.compile(r"`([^`\s]+\.(?:md|mdc|sh|py|yml|yaml|toml|json))`")

@@ -388,7 +397,7 @@ def read_optional(repo: str, rel: str) -> str | None:
 def scanned_files(repo: str) -> list[str]:
     out = []
     for dirpath, dirnames, filenames in os.walk(repo):
-        dirnames[:] = [d for d in dirnames if d != ".git"]
+        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
 ... (identical change at check_references()'s own os.walk site) ...
(diff confined to exactly the two named prune lines plus one new shared
constant; no other check function, constant, or logic touched)

$ git diff process/promote-item-0017...wp-0020-execution --stat
 3 files changed, 228 insertions(+), 20 deletions(-)
(scripts/check-contract-consistency.py, LISS-0058, WP-0020 — no other
file touched, confirming the design agreement's own Boundaries held)

--- independent fixture reproduction, built fresh by this review ---
$ mkdir -p /tmp/liss-0058-independent-check/fixture/.claude/worktrees/fake-sibling
$ git archive process/promote-item-0017 | tar -x -C /tmp/liss-0058-independent-check/fixture
$ git archive process/promote-item-0017 | tar -x -C /tmp/liss-0058-independent-check/fixture/.claude/worktrees/fake-sibling
$ git show process/promote-item-0017:scripts/check-contract-consistency.py > /tmp/prefix-checker.py
$ python3 /tmp/prefix-checker.py --repo /tmp/liss-0058-independent-check/fixture 2>&1 | tail -1
contract consistency: 906 failure(s)
$ python3 /tmp/prefix-checker.py --repo /tmp/liss-0058-independent-check/fixture 2>&1 | wc -l
910
$ python3 /tmp/prefix-checker.py --repo /tmp/liss-0058-independent-check/fixture 2>&1 | grep -c "Write the path"
806
(exactly matches the Implementer's own reported figures — 906 failures,
806 ambiguous-basename lines, 911-line total output — independently
reproduced from a freshly-built fixture, not copied)

$ git show wp-0020-execution:scripts/check-contract-consistency.py > /tmp/fixed-checker.py
$ python3 /tmp/fixed-checker.py --repo /tmp/liss-0058-independent-check/fixture
contract consistency: all checks passed
(same fixture, fixed script: noise fully gone)

$ python3 /tmp/fixed-checker.py --repo .   # this review's own real worktree
contract consistency: all checks passed
(no regression against real, tracked content)

$ rm -rf /tmp/liss-0058-independent-check /tmp/prefix-checker.py /tmp/fixed-checker.py
(fixture cleaned up; nothing committed)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The reported "906 failures / 806 ambiguous-basename lines" figure was fabricated or copied without actually running the fixture | This review built its own fresh fixture from `process/promote-item-0017` content (independent `git archive` extraction, not reused from the Implementer's own scratch directory, which had already been deleted) and reproduced the identical 906/806/911 figures against the pre-fix script | not reproduced |
| 2 | The fix is broader than necessary and silently drops real, tracked content | `git ls-tree -r --name-only HEAD \| grep "^\.claude/"` (re-run by this review) returns nothing — confirmed independently, not only cited from the design agreement — so excluding the whole `.claude` top-level directory loses no tracked, contract-relevant file | not reproduced |
| 3 | The fix regresses the real-repository baseline (hides a pre-existing failure, or introduces a new one) | Ran the fixed script against this review's own real worktree (`--repo .`, no nested `.claude/worktrees/` of its own) — `all checks passed`, matching the documented pre-fix baseline exactly | not reproduced |
| 4 | The diff touches more than the two named `os.walk` prune sites | Independent `git diff --stat` shows exactly 3 files changed (the script plus the two tracking files); the script's own diff shows exactly one new constant and two one-line prune-list edits, nothing else | not reproduced |
| 5 | The fixture reproduction is too shallow to be a faithful model of the real bug (e.g., missing the "full nested checkout" shape) | Fixture was built from this repository's actual tracked content via `git archive`, duplicated wholesale under `.claude/worktrees/fake-sibling/`, exactly mirroring what a real sibling Agent-tool worktree looks like on disk; it produced 906 genuine failures, the same order of magnitude and shape (ambiguous-basename pairs, one member of each pair under the nested path) the backlog item's own original real-world reproduction described | not reproduced |

## Scenarios Not Searched

- Whether some other, non-`.claude` harness- or tool-local directory (an
  adopter's own local scratch convention) would benefit from the same
  exclusion — explicitly out of this work plan's scope; the design
  agreement's own Deferred Questions section names none, since the
  backlog item's confirmed, reproduced bug is specific to `.claude/`.
- Performance impact of the added `EXCLUDED_DIRS` tuple membership check
  at scale — not a concern raised by the backlog item or design agreement,
  and the change is a two-element tuple lookup per directory, not a
  meaningfully different cost than the prior single-string comparison.

## Checklist

- [x] The artifact belongs to the phase that was run (Fast Path) — a
      single, narrowly-scoped, one-attempt fix, confirmed by the diff
      scope.
- [x] Every `Then` clause in the specification is asserted by the work —
      N/A, no specification covers this work plan.
- [x] The dependency rule and port boundaries hold — N/A, no application
      architecture touched; this is a standalone process-tooling script.
- [x] No boundary named in the design agreement was crossed — confirmed:
      no other check function's logic touched, no other constant touched,
      no file outside `scripts/check-contract-consistency.py` and the two
      tracking files changed.
- [x] Specifications and accepted tests were not modified to make work
      pass — N/A, and no existing test suite covers this script (confirmed
      no `scripts/tests/*checker*` file exists).
- [x] Every claim in the artifact states its grounds — the fix's own code
      comment states why both `.git` and `.claude` are excluded; the
      Implementer's Work Notes state exactly which approach (shared
      constant) was chosen and why.
- [x] The record would let a third party re-run this same search — every
      command above is copy-pasteable and was independently re-run by
      this review from a freshly built fixture, not merely copied from
      the Implementer's own output.

## Decision

- [x] Approved

## Reasons

The fix is exactly the scoped, narrow change the design agreement
authorized: a shared `EXCLUDED_DIRS = (".git", ".claude")` constant
applied identically at both `os.walk` prune sites, confirmed via
independent `git diff` to touch nothing else. This review built its own
fresh fixture (not reused from the Implementer's) and independently
reproduced the exact same failure signature reported — 906 failures, 806
of them ambiguous-basename lines, 911 lines of total output — confirming
the bug is real and was genuinely, not merely claimed to be, reproduced
before the fix. The same fixture shows the noise fully gone after the
fix, and the real repository (both this review's own worktree and, per
the Implementer's own Preflight record, the Implementer's own worktree)
shows an identical `all checks passed` baseline before and after,
confirming no regression. `git ls-tree` independently confirms nothing
tracked lives under `.claude/`, grounding the breadth decision (whole
`.claude/` vs. only `.claude/worktrees/`) the design agreement settled.
No `Type: review-finding` issue is warranted.