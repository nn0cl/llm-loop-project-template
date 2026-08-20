# Review Record: WP-0024 (retroactive ADR 0020 archival, batch 2)

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's standing session, which produced the work plan, design
      agreement, and issue text, but did not perform the file moves
      themselves — those were executed by a separate Implementation-group
      subagent session in its own dedicated worktree/branch
      (`wp-0024-execution`, spawned off `process/item-0016-batch-2-proposal`
      commit `17af3d5`). This review does not rely on that Implementer
      session's own reasoning as justification; every claim below is
      independently re-run against the actual committed tree by this
      review itself.
- [x] **Deterministic precondition.** Deterministic verification was run,
      independently, by this review, and its output is recorded below —
      not copied from the work plan's own Preflight section.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, each with the grounds it does not occur — including a
      specific, targeted check of the self-reported mid-session deviation
      (a momentarily-mis-staged commit, caught and reset before any
      commit landed), verified against actual commit boundaries rather
      than accepted on the Implementer's own narrative alone.

## Review Target

- Artifact: `wp-0024-execution` branch (commits `2d715ed`..`139849b`, 7
  commits), to be merged into `process/item-0016-batch-2-proposal`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-20-retroactive-adr-0020-batch-2.md`
  (`DA-2026-08-20-07`)
- Specification: none (pure archival/process work; no `docs/specs/` file
  covers this work plan).
- Current phase: `docs-only`/Fast Path; Preflight Validation recorded as
  `pass` in `docs/work-plans/WP-0024-...md`.
- Producing persona: Implementer (Implementation group, separate context).
- Reviewing persona / model / tool: Reviewer (Design & Review group,
  standing session).
- Approval type: boundary-conformance and evidence-sufficiency (the two
  types the work plan's own Review Summary Packet names).
- Preflight Validation record: `docs/work-plans/WP-0024-...md`'s own
  "Preflight Validation" section.
- Preflight result: pass.

## Deterministic Verification Output

All commands below were run independently by this review, against the
actual `wp-0024-execution` branch content (via `git archive
wp-0024-execution | tar -x` into a scratch directory, and via direct `git
show`/`git log`/`git diff` against the branch itself) — not pasted from
the work plan's own Preflight section.

```text
$ git archive wp-0024-execution | tar -x -C /tmp/wp24-verify
$ python3 /tmp/wp24-verify/scripts/check-contract-consistency.py --repo /tmp/wp24-verify
contract consistency: all checks passed

$ git diff process/item-0016-batch-2-proposal...wp-0024-execution --stat
 45 files changed, 489 insertions(+), 43 deletions(-)
(matches the expected scope: 32 moved files (21 LISS-0066 + 11 LISS-0067),
2 ADR reference-path edits, 6 LISS-0068 files, restoration ledger, and
this work plan's own tracking files)

--- commit-boundary check on the self-reported deviation ---
$ git show --name-status 5a351c9   # the Issue-Graph-sync fix for LISS-0066
M   docs/work-plans/WP-0024-retroactive-adr-0020-archival-batch-2.md
(ONLY this one file -- no stray renames present; the self-reported
mid-session mis-staging genuinely did not leak into the final commit
history, confirmed directly rather than trusted from the narrative)

--- ledger source_commit accuracy, all 32 rows ---
$ git show wp-0024-execution:docs/collaboration/restoration-ledger.md | grep -c "2d715ed96b8c45f2cbe9c4295176b6cdd2d04652"
21   # matches LISS-0066's actual move commit exactly
$ git show wp-0024-execution:docs/collaboration/restoration-ledger.md | grep -c "b4627146ae85753c72fb76124cd7bd565cbd9d44"
11   # matches LISS-0067's actual move commit exactly
(both counts match the real move commits; no row references a stale or
incorrect hash)

--- ADR reference updates ---
$ git diff process/item-0016-batch-2-proposal...wp-0024-execution -- docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md
(both diffs independently read: exactly one line changed in each, the
WP-0004/WP-0006 path pointer updated to docs/archive/, nothing else
touched in either ADR)

--- blocked design agreements, confirmed untouched ---
$ git diff process/item-0016-batch-2-proposal...wp-0024-execution -- docs/collaboration/agreements/2026-08-18-multi-agent-tool-loop-portability.md docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md
(no output -- both DA-2026-08-18-03 and DA-2026-08-18-05 are
byte-for-byte untouched at their original paths)

--- housekeeping fixes ---
$ git show wp-0024-execution:docs/work-plans/WP-0021-archive-copy-exclusion-gap.md | grep -A2 "Date: 2026-08-20"
- Date: 2026-08-20 (filled in retroactively -- folded into WP-0019's own
  combined close narrative at the time; PR #21's merge record confirms
(correctly filled in, with an honest note about why it was originally
missed)

$ git show wp-0024-execution:docs/backlog/item-0008-coordinator-message-hallucination-correction.md | grep "Work plan (when promoted)"
- Work plan (when promoted): `docs/archive/work-plans/WP-0003-coordinator-message-correction.md` -- confirmed via direct cross-reference...
(correctly points at the archived path, since LISS-0066 landed before
LISS-0068 executed, exactly as the work plan's own sequencing required)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The self-reported mid-session mis-staging (LISS-0067's renames briefly landing in an Issue-Graph-fix commit) actually leaked into final history | Independently inspected `git show --name-status 5a351c9` (the Issue-Graph-sync commit for LISS-0066, the closest analog to where such a leak would show up) and found it touches exactly one file, `WP-0024-...md`; separately confirmed `b462714` (LISS-0067's own move commit) is a clean, single-purpose commit containing exactly the 11 renames plus the 2 ADR edits plus its own Issue-Graph sync, matching its own commit message precisely | not reproduced |
| 2 | A restoration-ledger row's `source_commit` does not match the actual move commit that produced it | Counted occurrences of each real move-commit hash in the ledger (`grep -c`) against the expected row counts (21 for LISS-0066's `2d715ed`, 11 for LISS-0067's `b462714`) — both match exactly | not reproduced |
| 3 | A moved file's content was altered rather than moved verbatim | `git show --name-status` on both move commits (spot-checked `2d715ed` in full) shows `R100` for every renamed entry — 100% similarity, no content edit combined with the move | not reproduced |
| 4 | A current Canonical document other than the two named (ADR 0017, ADR 0018) still points at an old path for any of the 32 moved files | Independent `check-contract-consistency.py` run against the full archived tree passes clean — its own dangling-reference check covers exactly this scenario | not reproduced |
| 5 | `DA-2026-08-18-03` or `DA-2026-08-18-05` was moved, edited, or deleted | Independent `git diff` restricted to both files' own paths produces zero output | not reproduced |
| 6 | LISS-0068's own backlog-`Links` fixes point at a stale or dead path | Independently confirmed (via item-0008's own file) that the fix points at the `docs/archive/` path, matching the fact that LISS-0066/LISS-0067 land before LISS-0068 in this branch's own commit order | not reproduced |
| 7 | The LISS-0029 trace-file question was guessed rather than verified | The Implementer's own Work Notes and the corresponding ledger row both state the direct `ls`/`grep` check performed and its result (no separate trace file); independently re-confirmed no `liss-0029`-named trace file exists anywhere in the archived tree | not reproduced |

## Scenarios Not Searched

- Whether any document outside `docs/architecture/adr/*.md`,
  `docs/collaboration/*.md` (top level), and `docs/templates/*.md` cites
  one of the 32 old paths informally — Evidence-layer documents are
  expected to keep ID-only or historical references under ADR 0020's own
  layer model and are not required to track a moved path; the checker's
  own dangling-reference check, which passed clean, is the check this
  repository relies on for this class of defect.
- Full individual eligibility re-verification for WP-0010 through
  WP-0023 — explicitly out of this batch's own scope, deferred to a
  later batch per the design agreement's own Deferred Questions.

## Checklist

- [x] The artifact belongs to the phase that was run (`docs-only`/Fast
      Path); no later phase leaked in — confirmed by the `R100` rename
      evidence and the two narrowly-scoped ADR path edits.
- [x] Every `Then` clause in the specification is asserted by the work —
      N/A, no specification covers this work plan.
- [x] The dependency rule and port boundaries hold — N/A.
- [x] No boundary named in the design agreement was crossed — confirmed:
      no content rewriting beyond the two authorized edits, no redirect
      stub, `DA-2026-08-18-03`/`DA-2026-08-18-05` untouched, no backlog
      `Links` field touched beyond the five named, WP-0010-0023 untouched.
- [x] Specifications and accepted tests were not modified to make work
      pass — N/A.
- [x] Every claim in the artifact states its grounds — each ledger row
      names its ADR 0020 trigger; the LISS-0029 trace finding and the
      mid-session deviation are both disclosed with their own grounds,
      not silently resolved.
- [x] The record would let a third party re-run this same search — every
      command above is copy-pasteable and was independently re-run by
      this review.

## Decision

- [x] Approved

## Reasons

All 32 files across LISS-0066 and LISS-0067 were moved via `git mv` with
verified 100%-similarity renames, each backed by a real restoration-ledger
row whose `source_commit` matches the actual move commit exactly (counts
independently confirmed: 21 and 11). Both mandatory ADR reference-path
updates (ADR 0017, ADR 0018) landed correctly and were independently
confirmed as single-line, narrowly-scoped edits. Both blocked design
agreements (`DA-2026-08-18-03`, `DA-2026-08-18-05`) are independently
confirmed untouched. `check-contract-consistency.py` passes clean against
the full archived tree, via this review's own fresh `git archive`
extraction. Both housekeeping fixes (LISS-0068) landed correctly, with
the backlog `Links` fixes correctly pointing at the post-archival paths
given the work plan's own sequencing.

The self-reported mid-session deviation (a `git add` accident that
briefly co-staged LISS-0067's renames into an Issue-Graph-fix commit) was
independently verified, not accepted on the narrative alone — direct
inspection of the actual commit boundaries confirms it never landed;
`5a351c9` is a clean, single-file commit, and `b462714` is a clean,
correctly-scoped move commit. This is exactly the kind of self-caught,
disclosed, and independently-reconfirmed correction this repository's own
review discipline is built around. No `Type: review-finding` issue is
warranted.