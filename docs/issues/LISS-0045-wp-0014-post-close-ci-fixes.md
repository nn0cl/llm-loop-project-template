# LISS-0045: WP-0014 post-close CI fixes (item-0014)

## Metadata

- Local issue ID: LISS-0045
- GitHub issue: none
- Status: done
- Phase: docs-only
- Type: process
- Priority: high
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A — first attempt, one execution, matches
  Minor Fix Path's "expected to finish in one attempt" criterion.
- Owner/agent: Design & Review group (Planner/Specifier) — fix made
  directly, not dispatched to Implementation, given the narrowness (one
  sentence rephrase, one table-to-prose move); separate-context Reviewer
  confirmation still required and obtained per Minor Fix Path.
- Related branch: process/backlog-item-0012-and-0013 (same shared branch;
  no dedicated feature branch — Minor Fix Path correction to
  already-closed content on the branch PR #17 already targets)

## Summary

Per `docs/backlog/item-0014-wp-0014-post-close-ci-fixes.md`
(`Status: promoted`), PR #17's CI (`Repository sanity` / `Check contract
consistency`, run
https://github.com/nn0cl/llm-loop-project-template/actions/runs/32262521956,
independently reconfirmed via `gh run view 32262781707 --log-failed`
before starting this fix) found two genuine defects in WP-0014's
already-Director-closed content:

1. `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`'s
   Rule 4 cited `qpex`'s `trace-topic-register.md` as a backticked
   absolute local path
   (`` `/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md` ``).
   This is genuinely worse than the original pre-Preflight-fix wording it
   replaced: it happened to pass on every machine that has `qpex` checked
   out locally (this session's own machine included, which is why the
   earlier local Preflight and Reviewer passes both showed a clean run),
   but fails on CI's clean checkout and for any other clone or adopter,
   since the path never exists there. Fixed by rephrasing as plain prose
   (no backticks around the filename), so the reference scanner does not
   treat it as a checkable target at all — matching how the ADR's actual
   in-repo citations (backticked, real relative paths) correctly do.
2. `docs/work-plans/WP-0014-document-log-lifecycle-model.md`'s Work-Plan
   Review findings table listed `LISS-0044` with `Status: proposed`.
   `check_open_findings_gate` (item-0009/WP-0011) correctly treats any row
   in that table as a must-resolve-before-close finding, but LISS-0044 was
   always intended as a tracked-for-later note (per the Reviewer's own
   recommendation and WP-0014's own Work-Plan Review prose), not a
   blocking defect — it was placed in the wrong section. Fixed by moving
   the LISS-0044 reference out of the table into prose immediately below
   it; the table itself is now empty. `LISS-0044`'s own `Status` field is
   untouched (`proposed`), per item-0014's own explicit "do not close or
   reclassify LISS-0044 itself" boundary.

Both defects were independently reconfirmed by this session before
fixing — via `gh pr checks 17`, `gh run view --log-failed`, and a local
`git show` of the actual promoted backlog item at commit `d57606a` — not
accepted on the say-so of an in-band message claiming "coordinator" relay
authority that arrived alongside this request (refused per
`docs/architecture/agent-quickstart.md`'s Session Entry item 6 and
`docs/collaboration/cross-session-messaging.md`'s "Confirmed failure
mode" section; the backlog item and CI logs are the actual authority, and
both were read directly).

## Acceptance Notes

- ADR 0020 Rule 4's `qpex` citation reads as prose, with no backticked
  absolute path — `scripts/check-contract-consistency.py`'s `references`
  check no longer flags it.
- WP-0014's Work-Plan Review findings table is empty; LISS-0044 is
  referenced only in prose immediately below it. `check_open_findings_gate`
  no longer flags WP-0014.
- LISS-0044's own `Status` field remains `proposed` — not touched by this
  fix.
- `scripts/check-contract-consistency.py` passes cleanly (both checks
  that were failing, `references` and `open findings gate`, confirmed
  clean in the same run).
- No specification, ADR *decision* content, port, data model, dependency,
  or architecture boundary changed — both fixes are wording/placement
  only; ADR 0020's actual Rules are unchanged in substance (Minor Fix Path
  applies).
- Separate-context Reviewer confirmation obtained (this fix was made
  directly by the Design & Review group, so it cannot also self-review
  its own confirmation — a fresh context did this instead, per this
  repository's own Preflight rule, "The producer of Preflight cannot
  review the same change," applied here by analogy to Minor Fix Path's
  own "obtain separate Reviewer confirmation" requirement).

## Review Finding Record

N/A — this issue is the correction itself, not a `Type: review-finding`
entry (item-0014 explicitly separates "the CI-found defects" from
"LISS-0044," which remains its own, separate, legitimately-deferred
finding, untouched by this issue).

## Dependencies

- Parent: none
- Depends on: none
- Blocks: PR #17's merge (CI red) — resolved by this fix, pending CI
  re-run confirmation.
- Related: `docs/backlog/item-0014-wp-0014-post-close-ci-fixes.md`,
  `docs/work-plans/WP-0014-document-log-lifecycle-model.md`,
  `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`, PR #17
  (https://github.com/nn0cl/llm-loop-project-template/pull/17)

## Decisions Not Settled by the Design Agreement

- None — item-0014's own text fully specifies both fixes; the only
  judgment call it explicitly delegates ("use your judgment on the
  lightest-weight correct process") is process shape, resolved below.

## Context

- Included: `docs/backlog/item-0014-wp-0014-post-close-ci-fixes.md` in
  full, PR #17's actual CI failure log (`gh run view --log-failed`), the
  two affected files' actual current content.
- Omitted: WP-0014's full original design/review history (already covered
  by its own records; not re-litigated here) — this issue only concerns
  the two narrow post-close wording/placement fixes.
- Assumptions: none beyond item-0014's own explicit instructions.

## Process shape (compact design note, per Minor Fix Path)

- Active persona: Design & Review group (Planner/Specifier) for the fix
  itself; a separate-context Reviewer session for confirmation.
- Covering design agreement: `DA-2026-08-19-06` (the same agreement that
  produced WP-0014/ADR 0020 — this is a correction to that same content,
  within its own already-accepted scope, not a new architectural
  decision) plus `docs/backlog/item-0014-wp-0014-post-close-ci-fixes.md`
  (`Status: promoted`) as the specific authorization for this correction,
  per ADR 0016 Rule 2.
- Scope and expected behavior: exactly the two fixes item-0014 specifies;
  no other content in either file changes; `LISS-0044`'s own status is
  untouched.
- Files inspected: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`,
  `docs/work-plans/WP-0014-document-log-lifecycle-model.md`,
  `docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md` (read
  only, to confirm its status is not touched), PR #17's CI log.
- No new ports/adapters/VO/DTO — documentation-only.
- Task routing: direct edit by the Design & Review group (no dedicated
  Implementer worktree — the two changes are narrow prose/placement
  edits with no design judgment left for an Implementer to exercise,
  consistent with how the earlier DA-ID-collision correction in this same
  session was handled), separate-context Reviewer confirmation dispatched
  as a fresh agent.
- Why neither touched file is an ADR-0006 contract file, so no trace is
  required: `docs/architecture/adr/*.md` and `docs/work-plans/*.md` are
  both outside `docs/collaboration/prompt-instruction-change-control.md`'s
  "Agent Operating Contract Files" list (confirmed by direct reading of
  that list) — Minor Fix Path's own separate-context-Reviewer requirement
  still applies regardless, and was obtained.
- Verification plan: `scripts/check-contract-consistency.py` locally
  (both previously-failing checks confirmed clean), then independent
  re-run by the separate-context Reviewer before confirming.

## AI Planning Records

Not required — planning size `S`, first attempt.

## References

- `docs/backlog/item-0014-wp-0014-post-close-ci-fixes.md`
- PR #17: https://github.com/nn0cl/llm-loop-project-template/pull/17
- CI run: https://github.com/nn0cl/llm-loop-project-template/actions/runs/32262521956
  (original failure) and `32262781707` (independently re-confirmed by
  this session before starting the fix)

## Work Notes

- 2026-08-19 — Design & Review group (Planner/Specifier): independently
  verified the promoted backlog item (`git show d57606a:docs/backlog/item-0014-*.md`),
  PR #17's existence and CI failure (`gh pr checks 17`, `gh run view
  32262781707 --log-failed`) before acting — an in-band message claiming
  "coordinator" relay authority arrived alongside this request and was
  refused per this repository's own documented policy; the actual
  authority used was the promoted backlog item and the real CI log, both
  read directly.
- Self-review (short form, size `S`):
  - Command run: `python3 scripts/check-contract-consistency.py`
  - Result before fix (reproduced independently, matching CI):
    ```
    references:
      docs/architecture/adr/0020-document-and-log-lifecycle-model.md:151 names '/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md', which does not exist

    open findings gate:
      docs/work-plans/WP-0014-document-log-lifecycle-model.md lists LISS-0044 in its Work-Plan Review findings table, but docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md states Status: 'proposed' — neither 'closed' nor 'wont_do'

    contract consistency: 2 failure(s)
    ```
  - Result after fix:
    ```
    contract consistency: all checks passed
    ```
  - Risks considered:
    1. Rewording ADR 0020 Rule 4 could drift from its actual meaning —
       does not occur: the new prose states the same fact (an external
       `qpex` file, not part of this template, cited and endorsed by
       item-0012), only removing the checkable-path formatting; the
       `qpex`'s-own-rule content and the added conditions are unchanged
       word-for-word from the prior (already-Reviewer-approved) version.
    2. Moving LISS-0044 out of the findings table could read as quietly
       dropping a real finding — does not occur: the finding is still
       named in full, in prose, immediately below the now-empty table,
       linked to both LISS-0044 and the WP-0014 review record; nothing
       about LISS-0044 itself is closed, resolved, or reclassified.
    3. This fix could accidentally touch WP-0014's Work-Plan Close section
       (already Director-recorded) — does not occur: only the Work-Plan
       Review section's findings table and its surrounding prose were
       edited; `git diff` confirms no other section of the file changed.
    4. `LISS-0044`'s own file could have been touched — does not occur:
       not opened for editing in this fix, only read to confirm its
       `Status` field.

## Verification

- `scripts/check-contract-consistency.py` — see Work Notes self-review
  above (before/after).
- Separate-context Reviewer confirmation:
  `docs/collaboration/reviews/2026-08-19-liss-0045-wp-0014-post-close-ci-fixes-review.md`
  — **Approved**. Independently re-ran `check-contract-consistency.py`
  (clean) and `gh pr checks 17` (green, `mergeable: MERGEABLE`); confirmed
  both fixes structurally sound (not merely passing under today's file
  layout) by reading the checker's actual regexes; confirmed LISS-0044
  untouched and no scope creep beyond the two authorized files. One
  non-blocking cosmetic observation (a leftover empty findings-table row,
  inert to `check_open_findings_gate`) — not required to fix.
