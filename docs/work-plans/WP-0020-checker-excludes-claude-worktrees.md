# Work Plan: `check-contract-consistency.py` excludes `.claude/`

## Goal

- Fix `scripts/check-contract-consistency.py`'s two `os.walk` sites so
  they exclude the harness-local, untracked `.claude/` directory the same
  way they already exclude `.git/`, eliminating false-positive ambiguous-
  reference noise when the checker runs from a location with active
  sibling agent worktrees under `.claude/worktrees/`.

## Scope

- In:
  - `scripts/check-contract-consistency.py`'s `scanned_files()` and
    `check_references()` `os.walk` prune lines (both currently exclude
    only `.git`).
  - A controlled fixture-based reproduction of the false positive, before
    and after the fix.
- Out:
  - Any other check function's own logic.
  - `SCANNED_SUFFIXES`, `RECORD_DIRS`, or any other existing
    exclusion/inclusion constant.
  - Any change to what counts as a genuine, in-scope reference failure.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0058 | done | S | S | N/A | - | - | process/promote-item-0017 |

## Recommended Order

1. LISS-0058 (the only issue) — reproduce the false positive in a fixture,
   apply the fix, re-verify.

## Current Next Issue

- Issue: LISS-0058
- Reason it is unblocked: no dependency; scope is fully settled by the
  design agreement, and the backlog item itself states the fix is
  "reproducible, narrow, root cause identified with the exact line."
- Reopening request needed: no.

## Minor Fix Path

Not used formally (this is a new issue against a confirmed bug, not a
correction to previously accepted work), but the change itself is
Minor-Fix-Path-shaped in size and risk: planning size `S`, a single
narrowly-scoped file, one attempt expected, no specification, ADR, port,
data model, or architecture boundary changed.

## Preflight Validation

Recorded by the Implementation group, 2026-08-20, after LISS-0058 was
self-reviewed and complete. All three required checks below: **pass**.

### Check 1 — fixture-based before/after reproduction

Fixture built at a throwaway scratch path (`<fixture>` below), per LISS-0058's
"Required reproduction": `git archive HEAD | tar -x -C <fixture>`, then the
same archive extracted again into `<fixture>/.claude/worktrees/fake-sibling/`.

**Before the fix** — `python3 scripts/check-contract-consistency.py --repo <fixture>`
(script at commit `08e0a36`, i.e. before this work plan's own fix commit):

```
references:
  .claude/worktrees/fake-sibling/CHANGELOG.md:123 names '2026-08-03-work-plan-scoped-governance-review.md', which 2 files answer to (.claude/worktrees/fake-sibling/docs/collaboration/reviews/2026-08-03-work-plan-scoped-governance-review.md, docs/collaboration/reviews/2026-08-03-work-plan-scoped-governance-review.md). Write the path.
  .claude/worktrees/fake-sibling/CHANGELOG.md:124 names '2026-08-03-work-plan-scoped-governance-review-2.md', which 2 files answer to (.claude/worktrees/fake-sibling/docs/collaboration/reviews/2026-08-03-work-plan-scoped-governance-review-2.md, docs/collaboration/reviews/2026-08-03-work-plan-scoped-governance-review-2.md). Write the path.
  ... [806 ambiguous-basename lines total, each pairing a top-level file
      with its identical nested .claude/worktrees/fake-sibling/ copy] ...
  docs/collaboration/session-start-and-resume.md:62 names 'init-loop-settings.sh', which 2 files answer to (.claude/worktrees/fake-sibling/scripts/init-loop-settings.sh, scripts/init-loop-settings.sh). Write the path.
  docs/collaboration/session-start-and-resume.md:62 names 'init-llm-context.sh', which 2 files answer to (.claude/worktrees/fake-sibling/scripts/init-llm-context.sh, scripts/init-llm-context.sh). Write the path.
  docs/collaboration/session-start-and-resume.md:211 names 'init-llm-context.sh', which 2 files answer to (.claude/worktrees/fake-sibling/scripts/init-llm-context.sh, scripts/init-llm-context.sh). Write the path.

contract consistency: 906 failure(s)
```

Exit code: `1`. 911 lines of output total; 806 are ambiguous-basename
"Write the path" lines (`grep -c "Write the path"` on the captured output).
Genuine reproduction of the reported bug, confirmed real, not assumed.

**After the fix** — same command, same fixture, fixed script:

```
contract consistency: all checks passed
```

Exit code: `0`. All 806 ambiguous-basename lines and all other duplication-
driven noise gone.

Fixture removed (`rm -rf <fixture>`) immediately after this check; confirmed
removed by re-listing the scratch directory. Not committed to the repository.

### Check 2 — real repository, no regression

**Before the fix** (script at `08e0a36`), from this worktree's own root:

```
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

Exit code: `0`.

**After the fix** (script at `a12e8a7`), same command:

```
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

Exit code: `0`. Identical baseline before and after — no new failure, no
newly hidden failure (none existed to hide). This worktree has no nested
`.claude/worktrees/` copy of its own (worktrees live *under*
`.claude/worktrees/<id>/` of the main repository, not replicated inside
themselves), so this run does not itself exercise the fix — Check 1's
fixture is what demonstrates the bug and the fix; this check only confirms
no regression against real, tracked content.

### Check 3 — diff scope

`git diff scripts/check-contract-consistency.py` (commit `a12e8a7`):

```
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
         for name in filenames:
             if name.endswith(SCANNED_SUFFIXES):
                 out.append(os.path.relpath(os.path.join(dirpath, name), repo))
@@ -441,7 +450,7 @@ def check_references(repo: str, failures: Failures) -> None:
     copy_exclusion_patterns = _copy_exclusion_patterns(repo)
     basemap: dict[str, list[str]] = {}
     for dirpath, dirnames, filenames in os.walk(repo):
-        dirnames[:] = [d for d in dirnames if d != ".git"]
+        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
         for name in filenames:
             rel_path = os.path.relpath(os.path.join(dirpath, name), repo)
             basemap.setdefault(name, []).append(rel_path)
```

Scope: confined to the two named `os.walk` prune lines plus one new shared
module-level constant (`EXCLUDED_DIRS`) the Implementer chose to factor the
exclusion list into, per the work plan's own either-is-acceptable note (see
LISS-0058's Work Notes for the stated reason). No other check function,
constant (`SCANNED_SUFFIXES`, `RECORD_DIRS`, etc.), or logic touched.

### Preflight result

**Pass.** All three checks recorded above with real command output. No
open `review-finding` issues affect this area; no implementation issue in
this work plan is blocked on an open spike case. Next action: submit to
the work-plan-level Reviewer, in a separate context.

## Review Summary Packet

Filled in by the Implementation group once Preflight passes.

- **Scope**: fixed two `os.walk` exclusion sites in
  `scripts/check-contract-consistency.py` to also prune `.claude`,
  eliminating false-positive ambiguous-reference noise from nested sibling
  worktrees under `.claude/worktrees/`.
- **Current canonical documents**: none — `scripts/check-contract-consistency.py`
  is tooling, not an ADR-0006 contract file (confirmed by the backlog
  item's own "Known constraints" note), though this work plan treats the
  change with the same review rigor as this script's own six-round
  2026-08-02 review history, per that same note.
- **Changed files**: `scripts/check-contract-consistency.py` only.
- **Findings**: none opened or resolved by this work plan.
- **Disposition**: Preflight passed. LISS-0058 self-reviewed and complete;
  ready for submission to the work-plan-level Reviewer, in a separate
  context. Not yet submitted by the Implementation group (out of scope for
  this dispatch, per the work plan's own "Do not attempt the work-plan-level
  Reviewer pass yourself" instruction).
- **Remaining blockers**: none found. No open `review-finding` issue
  affects this area; no issue in this work plan is blocked on an open
  spike case.
- **Verification result**: see this file's own "Preflight Validation"
  section above — all three required checks (fixture before/after,
  real-repository no-regression, diff-scope) recorded with full pasted
  command output, all passing.
- **Next approval required**: evidence-sufficiency (is the false positive
  genuinely reproduced and genuinely fixed, with real pasted output) —
  the one approval type most directly at stake for a bug-fix this narrow;
  specification-conformance, phase-correctness, and boundary-conformance
  are secondary since no specification, phase, or architecture boundary is
  touched.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-20-wp-0020-checker-excludes-claude-worktrees-review.md`
— **Approved** (2026-08-20, Reviewer persona, Design & Review group
standing session, separate context from the Implementation-group subagent
session that executed LISS-0058 in its own worktree/branch). The review
independently built its own fresh fixture and reproduced the identical
906-failure/806-ambiguous-basename-line signature before the fix, and
confirmed it fully resolved after, rather than trusting the Implementer's
own pasted output.

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

No `Type: review-finding` issues were opened — the review found no defect
requiring correction.

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves.

- Date: 2026-08-20
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-20-wp-0020-checker-excludes-claude-worktrees-review.md`,
  Approved — the Reviewer built its own independent fixture reproducing
  the identical pre-fix failure signature, 906 failures/806 ambiguous-basename
  lines, confirmed fully resolved post-fix, no regression on the real
  repository) via the Backlog thread, which independently confirmed the
  `EXCLUDED_DIRS` fix, a clean `scripts/check-contract-consistency.py` run
  from a detached checkout, and caught and fixed one more status-sync gap
  (LISS-0058's Issue Graph row was still `ready`) before this close.
- Next direction: closed with "はい". Merged content sits on
  `process/promote-item-0017`. Push/PR/merge-to-main are separate explicit
  actions, pending.
- New design agreement (if any): none opened by this close.

## Risks

- A fixture reproduction that does not faithfully mirror the real bug
  (e.g., too small to trigger the ambiguous-basename check, or missing the
  nested full-checkout structure) could produce a false "no noise before
  the fix either" result. Mitigated by requiring the fixture to copy this
  repository's own real tracked content into both the top-level and the
  nested `.claude/worktrees/fake-sibling/` path, not synthetic minimal
  files.
- Excluding the whole `.claude` top-level directory (rather than only
  `.claude/worktrees`) is a broader exclusion than the backlog item's own
  literal title names. Mitigated by direct `git ls-tree` confirmation nothing
  under `.claude/` is tracked, and the item's own text explicitly leaves
  "how broad to make the exclusion" as "Design & Review's call."

## Verification Plan

- Fixture-based before/after reproduction (pasted output).
- `python3 scripts/check-contract-consistency.py` against the real
  repository, before and after (no regression).
- `git diff` confirming a narrowly-scoped change.
- Independent work-plan-level Reviewer approval, in a separate context.
