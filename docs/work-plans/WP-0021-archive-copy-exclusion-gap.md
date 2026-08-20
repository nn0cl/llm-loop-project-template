# Work Plan: `docs/archive/` copy-exclusion gap

## Goal

- Add `docs/archive/*` to `scripts/lib/collaboration-template-paths.sh`'s
  `collaboration_template_exclude_paths` array so
  `scripts/check-contract-consistency.py`'s copy-exclusion exemption logic
  (`_copy_exclusion_patterns()`/`_is_copy_excluded_reference()`, from
  item-0011/LISS-0040) recognizes a reference to a `docs/archive/` file as
  expected-absent on a copied/adopter target, unblocking PR #21 (WP-0019's
  merge) which is currently failing CI's "Check template copy smoke test"
  with 26 dangling-reference failures.

## Scope

- In:
  - One array entry added to `scripts/lib/collaboration-template-paths.sh`.
  - Before/after reproduction of the actual CI failure, using the same
    copy mechanism `.github/workflows/ci.yml`'s "Check template copy smoke
    test" step uses.
  - Correcting `docs/backlog/item-0018-...md`'s own premise that this
    closes `LISS-0044` (already closed; a different, already-resolved
    mechanism) — recorded, not acted on by reopening that issue.
- Out:
  - Any change to `collaboration_template_paths` (the copy-inclusion
    list) — `docs/archive` must not start being copied.
  - Any change to `scripts/check-contract-consistency.py`'s own Python
    logic — the fix is entirely data-driven from the shell array that
    script already parses.
  - Reopening or editing `docs/issues/LISS-0044-...md`.
  - Any other check function or exclusion mechanism.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0059 | ready | S | S | N/A | - | - | process/promote-item-0018 |

## Recommended Order

1. LISS-0059 (the only issue) — reproduce the real CI failure locally
   first, apply the one-line fix, re-verify.

## Current Next Issue

- Issue: LISS-0059
- Reason it is unblocked: no dependency; scope is fully settled by the
  design agreement; root cause already confirmed against the actual CI
  log and the actual current source of both scripts involved.
- Reopening request needed: no.

## Minor Fix Path

Not used formally (this is a new issue against a confirmed, CI-reproduced
bug, not a correction to previously accepted work), but the change itself
is Minor-Fix-Path-shaped in size and risk: planning size `S`, a single
one-line array addition, one attempt expected, no specification, ADR,
port, data model, or architecture boundary changed.

## Preflight Validation

Recorded 2026-08-20 by the Implementation group (Implementer persona), on
branch `wp-0021-execution` (created off `process/promote-item-0018`, reset
onto merge commit `54f73c7` after the coordinating session merged
`process/promote-item-0016`'s archival content into it so the reproduction
had real `docs/archive/` content to reproduce against). Result: **pass**.

1. Before/after copy-smoke-test reproduction, using the exact
   `scripts/copy-ai-collaboration-files.sh --target <tmp> --project-name
   "Smoke App" --domain-summary "template smoke test" --stack "test
   stack"` invocation `.github/workflows/ci.yml`'s "Check template copy
   smoke test" step uses, followed by `python3
   scripts/check-contract-consistency.py --repo <tmp>`:

   Before fix (26 failures, all `docs/archive/...` dangling-reference
   shape, matching PR #21's own CI run count exactly):

   ```
   references:
     docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md:23 names 'docs/archive/work-plans/WP-0002-two-group-send-message-loop.md', which does not exist
     docs/collaboration/design-review-perspectives.md:66 names 'docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md', which does not exist
     docs/collaboration/design-review-perspectives.md:169 names 'docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md', which does not exist
     docs/collaboration/restoration-ledger.md:46 names 'docs/archive/work-plans/WP-0001-review-issues-minor-fix-path.md', which does not exist
     docs/collaboration/restoration-ledger.md:47 names 'docs/archive/issues/LISS-0001-review-issues-minor-fix-path.md', which does not exist
     docs/collaboration/restoration-ledger.md:48 names 'docs/archive/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md', which does not exist
     docs/collaboration/restoration-ledger.md:49 names 'docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md', which does not exist
     docs/collaboration/restoration-ledger.md:50 names 'docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path-arbiter.md', which does not exist
     docs/collaboration/restoration-ledger.md:51 names 'docs/archive/work-plans/WP-0002-two-group-send-message-loop.md', which does not exist
     docs/collaboration/restoration-ledger.md:52 names 'docs/archive/issues/LISS-0019-adr-0016-two-group-topology.md', which does not exist
     docs/collaboration/restoration-ledger.md:53 names 'docs/archive/issues/LISS-0020-personas-group-mapping.md', which does not exist
     docs/collaboration/restoration-ledger.md:54 names 'docs/archive/issues/LISS-0021-ai-human-scheme-loop-update.md', which does not exist
     docs/collaboration/restoration-ledger.md:55 names 'docs/archive/issues/LISS-0022-cross-session-messaging-protocol.md', which does not exist
     docs/collaboration/restoration-ledger.md:56 names 'docs/archive/issues/LISS-0023-session-start-standing-pair.md', which does not exist
     docs/collaboration/restoration-ledger.md:57 names 'docs/archive/issues/LISS-0024-implementation-group-worktree-rule.md', which does not exist
     docs/collaboration/restoration-ledger.md:58 names 'docs/archive/issues/LISS-0025-design-agreement-backlog-gate-reconciliation.md', which does not exist
     docs/collaboration/restoration-ledger.md:59 names 'docs/archive/issues/LISS-0026-backlog-readme-bulk-gate.md', which does not exist
     docs/collaboration/restoration-ledger.md:60 names 'docs/archive/issues/LISS-0027-at-tdd-process-adr-0016-qualification.md', which does not exist
     docs/collaboration/restoration-ledger.md:61 names 'docs/archive/collaboration/traces/2026-08-18-liss-0020-personas-group-mapping.md', which does not exist
     docs/collaboration/restoration-ledger.md:62 names 'docs/archive/collaboration/traces/2026-08-18-liss-0021-ai-human-scheme-loop-update.md', which does not exist
     docs/collaboration/restoration-ledger.md:63 names 'docs/archive/collaboration/traces/2026-08-18-liss-0022-cross-session-messaging-protocol.md', which does not exist
     docs/collaboration/restoration-ledger.md:64 names 'docs/archive/collaboration/traces/2026-08-18-liss-0023-session-start-standing-pair.md', which does not exist
     docs/collaboration/restoration-ledger.md:65 names 'docs/archive/collaboration/traces/2026-08-18-liss-0024-implementation-group-worktree-rule.md', which does not exist
     docs/collaboration/restoration-ledger.md:66 names 'docs/archive/collaboration/traces/2026-08-18-liss-0025-design-agreement-backlog-gate-reconciliation.md', which does not exist
     docs/collaboration/restoration-ledger.md:67 names 'docs/archive/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md', which does not exist
     docs/collaboration/restoration-ledger.md:68 names 'docs/archive/collaboration/reviews/2026-08-18-liss-0027-at-tdd-process-adr-0016-qualification-review.md', which does not exist

   contract consistency: 26 failure(s)
   ```

   After fix (fresh throwaway target, same invocation):

   ```
   contract consistency: all checks passed
   ```

   Note: an earlier attempt against `process/promote-item-0018` at commit
   `95f3eab` (before the coordinating session's merge) showed zero
   `docs/archive/...` failures even pre-fix, because that commit did not
   yet contain the WP-0019/archival-batch commits that create
   `docs/archive/` content at all. That was correctly reported back rather
   than treated as "fix unnecessary," per the design agreement's own
   Falsification Criteria; the reproduction above, against the corrected
   base (`54f73c7`), is the one that governs this Preflight result.

2. `python3 scripts/check-contract-consistency.py` (real repository, no
   `--repo` flag), run against this worktree after the fix was committed:

   ```
   contract consistency: all checks passed
   ```

   No regression.

3. `git diff scripts/lib/collaboration-template-paths.sh` (captured before
   commit, reproduced here against the merged fix commit `3164778` vs. its
   parent):

   ```
   diff --git a/scripts/lib/collaboration-template-paths.sh b/scripts/lib/collaboration-template-paths.sh
   index 0236e46..69e99a9 100644
   --- a/scripts/lib/collaboration-template-paths.sh
   +++ b/scripts/lib/collaboration-template-paths.sh
   @@ -46,6 +46,7 @@ collaboration_template_exclude_paths=(
      "docs/backlog/item-*.md"
      "docs/work-plans/WP-*.md"
      "docs/collaboration/loop-settings.toml"
   +  "docs/archive/*"
    )

    is_collaboration_template_excluded() {
   ```

   Exactly one line added, nothing else touched.

4. `find <target> -path '*docs/archive*'` against the post-fix copied
   target returned no output — `docs/archive` remains un-copied; the fix
   did not touch `collaboration_template_paths`.

**Scope result**: matches the design agreement's Scope section exactly —
one array entry added to `collaboration_template_exclude_paths`;
`collaboration_template_paths` untouched; no Python logic changed;
`docs/issues/LISS-0044-...md` not touched.

**Next action**: submit to the work-plan-level Reviewer, in a separate
context, per the design agreement's Plan step 5.

## Review Summary Packet

Filled in by the Implementation group once Preflight passes.

- **Scope**: added one array entry
  (`scripts/lib/collaboration-template-paths.sh`'s
  `collaboration_template_exclude_paths`) so the checker's existing
  copy-exclusion exemption logic recognizes `docs/archive/*` references as
  expected-absent on a copied target; unblocks PR #21.
- **Current canonical documents**: none newly established;
  `scripts/lib/collaboration-template-paths.sh` is not an ADR-0006
  contract file, but is treated with the same reproduction rigor as any
  checker-affecting change in this repository's history.
- **Changed files**: `scripts/lib/collaboration-template-paths.sh` only.
- **Findings**: none opened; corrects (without editing)
  `docs/backlog/item-0018-...md`'s own premise about `LISS-0044`'s status.
- **Disposition**: Preflight pass. The one-line fix is applied, committed
  (`3164778` on `wp-0021-execution`), and verified: the real CI-shaped
  failure was reproduced before the fix (26 `docs/archive/...`
  dangling-reference failures, matching PR #21's own CI run) and shown
  resolved after it, with no regression on the real repository and
  `docs/archive` confirmed still un-copied. Ready for the work-plan-level
  Reviewer pass.
- **Remaining blockers**: none found. (Process note, not a blocker: the
  first reproduction attempt, against `process/promote-item-0018` at
  `95f3eab` before the coordinating session merged
  `process/promote-item-0016` into it, could not show the real failure
  because that commit did not yet contain the archived content the bug
  depends on — reported back rather than guessed past; superseded by the
  reproduction above once the branch carried the archival content.)
- **Verification result**: see this file's own Preflight Validation
  section above, populated with full pasted before/after output.
- **Next approval required**: evidence-sufficiency (is the CI failure
  genuinely reproduced locally and genuinely fixed, with real pasted
  output) — the one approval type most directly at stake for a one-line
  data fix; specification-conformance, phase-correctness, and
  boundary-conformance are secondary since no specification, phase, or
  architecture boundary is touched.

## Work-Plan Review

Reviewer's approval record: <link, filled in after the Reviewer pass>

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves — not performed by
the Design & Review group itself.

- Date:
- Result read:
- Next direction:
- New design agreement (if any):

## Risks

- A fixture/reproduction that does not use the exact same
  `copy-ai-collaboration-files.sh` invocation CI uses could produce a
  different result than the real CI failure. Mitigated by requiring
  LISS-0059's own reproduction to read `.github/workflows/ci.yml`'s own
  step before reproducing, and to use the identical flags.
- This work plan is explicitly blocking PR #21's own merge; a delay here
  has a direct downstream effect. Mitigated by the fix's own narrow,
  one-line scope and already-confirmed root cause (no open design
  question remains).

## Verification Plan

- Before/after copy-smoke-test reproduction (pasted output).
- `python3 scripts/check-contract-consistency.py` against the real
  repository, before and after (no regression).
- `git diff` confirming a one-line change.
- Confirmation `docs/archive` remains un-copied.
- Independent work-plan-level Reviewer approval, in a separate context.
