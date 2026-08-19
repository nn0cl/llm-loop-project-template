# Work Plan: Exclude Work-Plan History From Template Propagation

## Goal

- Confirm (already done in `DA-2026-08-18-04`'s Spike Result — no code
  change needed) that new `docs/collaboration/*.md` and
  `docs/architecture/adr/*.md` files already propagate automatically, and
  fix the adjacent gap the same empirical test surfaced: `docs/work-plans/
  WP-*.md` is copied into adopter repositories as if it were reusable
  template content, unlike the equivalent `docs/issues/LISS-*.md` and
  `docs/backlog/item-*.md` exclusions.

## Scope

- In: `scripts/lib/collaboration-template-paths.sh` exclusion list;
  `.github/workflows/ci.yml` smoke-test assertion; re-run of the empirical
  copy+update test; self-review; Preflight; separate-context Reviewer pass.
- Out: Tier 1/Tier 2 classification logic; any document content; the
  separate CI hardcoded-ADR-number-list gap (flagged elsewhere).

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0031 | done | S | S | - | - | - | process/template-propagation-work-plan-exclusion |

## Plan-Owned Bug Records

None.

## AI Planning Records

None required — planning size `S`, first attempt.

## Recommended Order

1. LISS-0031 (single issue).

## Current Next Issue

- Issue: LISS-0031
- Reason it is unblocked: no dependencies; `DA-2026-08-18-04` covers it
  fully, including the exact exclusion pattern and CI assertion location.
- Reopening request needed: no.

## Minor Fix Path

Not formally invoked (this is a fresh work plan, not a correction against an
already-approved one), but the single issue is planning size `S`, one
mechanical exclusion-list addition plus a matching CI assertion, one attempt
expected, and touches no specification/ADR/port/data-model/architecture
boundary.

## Preflight Validation

- Result: `pass`
- Checks and command output:
  - Fix diff (`scripts/lib/collaboration-template-paths.sh`,
    `.github/workflows/ci.yml`, commit `891b304` on
    `process/template-propagation-work-plan-exclusion`):
    ```diff
    diff --git a/.github/workflows/ci.yml b/.github/workflows/ci.yml
    index 4bbe5d9..9b2949d 100644
    --- a/.github/workflows/ci.yml
    +++ b/.github/workflows/ci.yml
    @@ -210,6 +210,7 @@ jobs:
               ! ls "$tmp/target/docs/specs/"*.md >/dev/null 2>&1
               ! ls -d "$tmp/target/docs/spike/"case-* >/dev/null 2>&1
               ! ls "$tmp/target/docs/backlog/"item-*.md >/dev/null 2>&1
    +          ! ls "$tmp/target/docs/work-plans/"WP-*.md >/dev/null 2>&1
               test -f "$tmp/target/scripts/check-contract-consistency.py"
               (cd "$tmp/target" && python3 scripts/check-contract-consistency.py --repo .)
               if grep -R -n -i -E '<PROJECT_NAME: one-line description|<FILL IN: e\.g\. backend' \
    diff --git a/scripts/lib/collaboration-template-paths.sh b/scripts/lib/collaboration-template-paths.sh
    index c6293dd..0236e46 100644
    --- a/scripts/lib/collaboration-template-paths.sh
    +++ b/scripts/lib/collaboration-template-paths.sh
    @@ -44,6 +44,7 @@ collaboration_template_exclude_paths=(
       "docs/specs/*.md"
       "docs/spike/case-*"
       "docs/backlog/item-*.md"
    +  "docs/work-plans/WP-*.md"
       "docs/collaboration/loop-settings.toml"
     )
    ```
  - `bash -n scripts/lib/collaboration-template-paths.sh` (mirrors CI's
    "Check script syntax" step): no output, exit 0.
  - `python3 scripts/check-contract-consistency.py --repo .` run directly
    against this checkout (mirrors CI's "Check contract consistency" step):
    ```
    contract consistency: all checks passed
    ```
  - Empirical copy+update re-test (same method as `DA-2026-08-18-04`'s
    Spike Result — scratch adopter from commit `6c78217`, updated against
    this fixed checkout, `891b304`):
    ```
    Source: <this checkout> (6c78217beb01145c40b20dcdbc52096805c7092c -> 891b30461f0e29b2f0cf454ca9a340b88e5371e0)
    Target: /tmp/liss-0031-scratch-target

    Added (new upstream files):
      - docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md
      - docs/collaboration/cross-session-messaging.md
    Updated (Tier 1 or 2, target had not diverged from the template):
      - .github/workflows/ci.yml
      - docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md
      - docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md
      - docs/at-tdd/process.md
      - docs/collaboration/design-agreement.md
      - docs/collaboration/session-start-and-resume.md
      - docs/collaboration/personas.md
      - docs/collaboration/ai-human-scheme.md
      - docs/collaboration/branch-commit-pr-discipline.md
      - docs/backlog/README.md
      - scripts/lib/collaboration-template-paths.sh
    Unchanged: 96 file(s)
    ```
    `docs/work-plans/WP-*.md` does not appear under "Added" (before the
    fix, `DA-2026-08-18-04`'s Spike Result showed `WP-0002`, `WP-0003`,
    `WP-0004` all listed there). `test -f
    /tmp/liss-0031-scratch-target/docs/work-plans/.gitkeep` succeeded — no
    over-exclusion. `docs/architecture/adr/0016-*.md` and
    `docs/collaboration/cross-session-messaging.md` still auto-discover
    correctly, confirming the original item-0005 question (already
    answered "no code change needed" in `DA-2026-08-18-04`) remains true
    after this fix. `docs/architecture/adr/0017-*.md` was not present in
    this checkout at test time (a concurrent, unrelated work plan had not
    yet landed it) — noted per the task instruction, not a problem.
  - CI smoke-test step's full command sequence, run locally against a
    fresh scratch copy from this fixed checkout: every `test -f`, `grep
    -q`, and `! ls` assertion passed, including the new
    `! ls "$tmp/target/docs/work-plans/"WP-*.md >/dev/null 2>&1` line. The
    fresh-copy log itself shows the fix operating directly:
    ```
    merge docs/work-plans
    skip template-history docs/work-plans/WP-0002-two-group-send-message-loop.md
    skip template-history docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md
    skip template-history docs/work-plans/WP-0003-coordinator-message-correction.md
    skip template-history docs/work-plans/WP-0001-review-issues-minor-fix-path.md
    skip template-history docs/work-plans/WP-0005-template-propagation-work-plan-exclusion.md
    ```
    One sub-step within that same sequence,
    `(cd "$tmp/target" && python3 scripts/check-contract-consistency.py --repo .)`,
    fails against the freshly-copied target (4 "which does not exist"
    reference errors: ADR 0016 and `cross-session-messaging.md` reference
    `docs/collaboration/agreements/*.md`, `docs/backlog/item-*.md`, and
    (newly, from this fix) `docs/work-plans/WP-0002-*.md` paths that are
    intentionally excluded from the copy). Re-running the identical check
    against commit `3929c4b` (immediately before this fix) reproduced 3 of
    those 4 failures already — confirming this is a pre-existing gap this
    fix extends by one instance, not a regression this fix introduces. Full
    before/after output is in LISS-0031's Work Notes. Out of
    `DA-2026-08-18-04`'s scope (document-content changes are explicitly
    excluded); flagged as a separate follow-up task for the Design & Review
    group rather than fixed here.
- Scope result: Tasks 1-4 of `DA-2026-08-18-04`'s Plan complete and match
  their acceptance criteria exactly. No change to Tier 1/Tier 2
  classification logic, document content, or any boundary outside this
  item's stated scope. No push, PR, or merge performed.
- Next action: submit to the Design & Review group's separate-context
  Reviewer pass (Task 7). The pre-existing `check-contract-consistency.py`
  vs. copied-target gap noted above is out of scope for that Reviewer pass
  and is tracked as its own follow-up task, not a blocker for this work
  plan's close.

## Work-Plan Review

Reviewer's approval record: _pending_

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

- Date: 2026-08-18
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-18-wp-0005-template-propagation-work-plan-exclusion-review.md`,
  Approved — the Reviewer independently re-ran the full empirical
  copy/update test from scratch rather than reusing the Implementer's
  fixtures) via the Backlog thread, which independently confirmed the fix,
  the review record, and a clean `scripts/check-contract-consistency.py`
  run from a detached checkout before presenting this close.
- Next direction: closed with "はい。Close". Merged into
  `process/two-group-send-message-loop-design` (commit `456680d`, together
  with WP-0004/0007/0008). Push and PR remain separate explicit actions.
- New design agreement (if any): none opened by this close.

## Risks

- Over-broad exclusion pattern could accidentally exclude
  `docs/work-plans/.gitkeep` or a future non-`WP-NNNN`-numbered file in
  that directory; mitigated by the exact-pattern acceptance criterion
  (`docs/work-plans/WP-*.md` only) and Task 3's explicit re-check that
  `.gitkeep` still copies.

## Verification Plan

- Empirical copy+update test re-run against a scratch adopter, before and
  after the fix.
- `.github/workflows/ci.yml`'s existing smoke-test command sequence, run
  locally.
- Separate-context Reviewer approval.
