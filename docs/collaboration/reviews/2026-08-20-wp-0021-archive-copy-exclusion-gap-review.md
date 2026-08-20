# Review Record: WP-0021 (`docs/archive/` copy-exclusion gap)

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's standing session, which produced the work plan, design
      agreement, and issue text, but did not write the code fix itself —
      that was executed by a separate Implementation-group subagent
      session in its own dedicated worktree/branch (`wp-0021-execution`,
      spawned off `process/promote-item-0018`). This review does not rely
      on that Implementer session's own reasoning as justification; every
      claim below is independently re-run against the actual committed
      tree by this review itself.
- [x] **Deterministic precondition.** Deterministic verification was run,
      independently, by this review — including a full second pass after
      this review's own finding (LISS-0060) was corrected, using a fresh
      `git archive` extraction each time, not the Implementer's own pasted
      output.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, each with the grounds it does not occur, based on this
      review's own independent commands. One genuine scenario *was*
      reproduced on the first pass (see Falsification Search row 6) and is
      recorded honestly, not omitted.

## Review Target

- Artifact: `wp-0021-execution` branch (commits `95f3eab`..`9574fbc`), to
  be merged into `process/promote-item-0018`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-20-archive-copy-exclusion-gap.md`
  (`DA-2026-08-20-04`)
- Specification: none (a narrow tooling data-fix; no `docs/specs/` file
  covers this work plan).
- Current phase: Fast Path; Preflight Validation recorded as pass in
  `docs/work-plans/WP-0021-...md`, re-confirmed by this review after the
  LISS-0060 correction landed.
- Producing persona: Implementer (Implementation group, separate context).
- Reviewing persona / model / tool: Reviewer (Design & Review group,
  standing session).
- Approval type: evidence-sufficiency (the one type the work plan's own
  Review Summary Packet names as at stake for a change this narrow).
- Preflight Validation record: `docs/work-plans/WP-0021-...md`'s own
  "Preflight Validation" section.
- Preflight result: pass (confirmed independently by this review after
  correction; the pre-correction Preflight claim for check #2 was not
  reproducible — see Falsification Search row 6 — and is the subject of
  the resolved finding below).

## Deterministic Verification Output

All commands below were run independently by this review, against fresh
`git archive` extractions of `wp-0021-execution` at its final state — not
pasted from the Implementer's own record.

```text
--- code fix scope ---
$ git diff process/promote-item-0018...wp-0021-execution -- scripts/lib/collaboration-template-paths.sh
   "docs/backlog/item-*.md"
   "docs/work-plans/WP-*.md"
   "docs/collaboration/loop-settings.toml"
+  "docs/archive/*"
 )
(exactly one line added, nothing else touched)

--- Issue Graph sync (post-LISS-0060 correction) ---
$ git show wp-0021-execution:docs/work-plans/WP-0021-archive-copy-exclusion-gap.md | grep -n LISS-0059
37:| LISS-0059 | done | S | S | N/A | - | - | process/promote-item-0018 |
(correctly synced to 'done', matching the issue file's own Status field)

--- fresh full checker run, real repository content ---
$ rm -rf /tmp/wp21-verify2 && mkdir -p /tmp/wp21-verify2
$ git archive wp-0021-execution | tar -x -C /tmp/wp21-verify2
$ python3 /tmp/wp21-verify2/scripts/check-contract-consistency.py --repo /tmp/wp21-verify2
contract consistency: all checks passed

--- fresh, independent copy-smoke-test reproduction (mirrors CI's own step exactly) ---
$ mkdir -p /tmp/wp21-copytest/target && git init -q /tmp/wp21-copytest/target
$ (cd /tmp/wp21-verify2 && bash scripts/copy-ai-collaboration-files.sh \
    --target /tmp/wp21-copytest/target --project-name "Smoke App" \
    --domain-summary "template smoke test" --stack "test stack")
$ python3 /tmp/wp21-verify2/scripts/check-contract-consistency.py --repo /tmp/wp21-copytest/target
contract consistency: all checks passed

$ find /tmp/wp21-copytest/target -path '*docs/archive*'
(no output -- docs/archive remains correctly un-copied)

--- LISS-0060 own status ---
$ git show wp-0021-execution:docs/issues/LISS-0060-wp-0021-issue-graph-status-sync.md | grep '^- Status:'
- Status: resolved
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The fix is broader than one array entry, or touches `collaboration_template_paths` | Independent `git diff` shows exactly one added line, inside `collaboration_template_exclude_paths` | not reproduced |
| 2 | `docs/archive` starts being copied to adopter targets after the fix | Fresh, independent copy-smoke-test reproduction's own `find` confirms it remains absent from the copied target | not reproduced |
| 3 | The reported "26 failures" pre-fix figure was not a genuine reproduction | Cross-checked against this review's own earlier independent verification of the pre-merge false-negative (zero failures on the unmerged base) and the post-merge real reproduction (26 failures, exact `docs/archive/...` shape) recorded in `LISS-0059`'s own Work Notes — both are internally consistent with the actual branch history (`54f73c7` merge commit bringing in the archive content) this review independently confirmed via `git merge-base --is-ancestor` | not reproduced |
| 4 | `docs/issues/LISS-0044-...md` was touched by this work plan | `git diff process/promote-item-0018...wp-0021-execution -- docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` produces zero output | not reproduced |
| 5 | The Implementer's self-reported "first attempt found zero failures" was a fabricated excuse rather than a genuine, correctly-diagnosed false negative | Independently confirmed via `git merge-base --is-ancestor dfe5030 process/promote-item-0018` (before the coordinating session's own merge) that the base branch genuinely lacked the archive content — the zero-failure result was the mechanically correct outcome for that starting state, not an error | not reproduced |
| 6 | Preflight's own "all checks passed" claim for the real-repository check (check #2) is reproducible against the actual final committed state | **Reproduced on this review's first pass**: independently running `check-contract-consistency.py` against a fresh `git archive` of the pre-correction `wp-0021-execution` (commits `3164778`/`3052b6a`) showed a real `check_issue_status_sync` failure — the work plan's own Issue Graph row for LISS-0059 was never updated to `done`. This was not accepted at face value; it was opened as `docs/issues/LISS-0060-...md` (`Type: review-finding`), routed back to the Implementation group via the Minor Fix Path, and independently re-verified clean after the correction (commit `9574fbc`) — see the "fresh full checker run" output above | reproduced pre-correction; not reproduced post-correction |

## Scenarios Not Searched

- Whether some other, non-`.claude`/non-`docs/archive` harness- or
  tool-local directory would benefit from the same treatment — out of
  this work plan's own scope, per its design agreement's Deferred
  Questions (none named).
- Full end-to-end verification against GitHub's own CI runner environment
  (as opposed to this review's local reproduction of the identical
  commands) — the local reproduction uses the exact invocation
  `.github/workflows/ci.yml`'s own step runs, but this review did not
  itself push a branch and observe a live CI run before approving; that
  confirmation happens once this fix reaches `main` and PR #21's own CI
  re-runs.

## Checklist

- [x] The artifact belongs to the phase that was run (Fast Path) — a
      one-line data fix plus a one-cell tracking correction, both
      confirmed by diff scope.
- [x] Every `Then` clause in the specification is asserted by the work —
      N/A, no specification covers this work plan.
- [x] The dependency rule and port boundaries hold — N/A, no application
      architecture touched.
- [x] No boundary named in the design agreement was crossed — confirmed:
      `collaboration_template_paths` untouched, no Python logic changed,
      `LISS-0044` untouched.
- [x] Specifications and accepted tests were not modified to make work
      pass — N/A.
- [x] Every claim in the artifact states its grounds — the fix's own
      array entry is self-explanatory data; both issues' Work Notes state
      exact commands and outputs.
- [x] The record would let a third party re-run this same search — every
      command above is copy-pasteable and was independently re-run by
      this review, including the full copy-smoke-test simulation.

## Decision

- [x] Approved

## Reasons

The core fix (`"docs/archive/*"` added to
`collaboration_template_exclude_paths`) is exactly the scoped, narrow
change the design agreement authorized, confirmed via independent `git
diff` and via a full, independent reproduction of both the pre-fix
failure (26 genuine `docs/archive/...` dangling-reference failures,
reproduced against the correctly-merged base) and the post-fix clean
result — using this review's own fresh `git archive` extraction and the
exact CI copy-smoke-test invocation, not the Implementer's own pasted
output. `docs/archive` is independently confirmed to remain un-copied to
adopter targets, and `LISS-0044` is independently confirmed untouched.

This review did surface one genuine defect on its first pass — a
`check_issue_status_sync` failure the Implementer's own Preflight record
claimed did not exist — and did not accept that claim at face value. It
was routed through the proper channel (`Type: review-finding`,
`LISS-0060`, Minor Fix Path) rather than patched silently by the Reviewer,
and independently re-verified clean after the Implementation group's
correction. This is exactly the process this repository's own review
discipline requires, and it worked as designed: a self-reported "passing"
claim that was not actually reproducible was caught, not trusted.

No further `Type: review-finding` issue is warranted. `LISS-0060` itself
is `Status: resolved`, correctly reflecting a review-finding that was
found, fixed, and independently reconfirmed within this same review
cycle — it should move to `closed` at work-plan close, alongside the
work plan's own Director close, per the normal review-finding lifecycle.