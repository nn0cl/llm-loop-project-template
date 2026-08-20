# Design Agreement: `docs/archive/` copy-exclusion gap

Store the completed record at
`docs/collaboration/agreements/2026-08-20-archive-copy-exclusion-gap.md`.

See `docs/collaboration/design-agreement.md` for the rules this record
implements.

## Identity

- Agreement ID: DA-2026-08-20-04
- Date: 2026-08-20
- Director: per ADR 0016 Rule 2, backlog-item-level agreement — see
  "Agreement" below.
- Planner / Specifier personas (model or tool used): Design & Review group,
  standing session (Claude Code, Planner/Specifier persona).
- Supersedes agreement (if any): none.

## Direction

`docs/backlog/item-0018-archive-copy-exclusion-gap.md`
(`Status: promoted`, "Promoted, in the Backlog-layer thread, immediately
at capture"): fix PR #21's CI failure (26 dangling-reference failures, all
`docs/archive/...` paths, from the "Check template copy smoke test" step)
by adding `docs/archive/*` to `scripts/lib/collaboration-template-paths.sh`'s
`collaboration_template_exclude_paths` array, which
`scripts/check-contract-consistency.py`'s existing `_copy_exclusion_patterns()`
mechanism (item-0011/LISS-0040) already parses as its own single source of
truth. Per ADR 0016 Rule 2, this item was never a check-in item; Design &
Review proceeds fully autonomously. This work plan directly unblocks PR
#21 (WP-0019's own merge to `main`), which cannot pass CI without it.

## Scope

- In scope: the one-line array addition; a before/after reproduction using
  the exact copy invocation CI's own smoke-test step uses; correcting (in
  this issue's own text only, not by editing that file) the backlog
  item's premise that this closes `LISS-0044`, which independent
  verification shows is already `Status: closed` via a different,
  already-completed mechanism (WP-0016/LISS-0048's `RECORD_DIRS` fix).
- Explicitly out of scope: adding `docs/archive` to
  `collaboration_template_paths` (it must remain un-copied); any Python
  logic change in `check-contract-consistency.py`; reopening or editing
  `LISS-0044`'s own file; any other check function.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Reproduce the real CI failure locally, using the exact `scripts/copy-ai-collaboration-files.sh` invocation `.github/workflows/ci.yml`'s smoke-test step uses | Implementer | Fast Path | Real `docs/archive/...` dangling-reference failures reproduced, pasted in full | `python3 scripts/check-contract-consistency.py --repo <copied target>` |
| 2 | Apply the fix (add `"docs/archive/*"` to `collaboration_template_exclude_paths`) | Implementer | Fast Path | `git diff` shows exactly one added line | `git diff scripts/lib/collaboration-template-paths.sh` |
| 3 | Re-run the same reproduction, confirm the failures are gone; confirm `docs/archive` is still not copied; confirm no regression on the real repository | Implementer | Fast Path | Zero `docs/archive/...` dangling-reference failures on the copy; `docs/archive` absent from the copied tree; real-repo run unchanged | Same commands, pasted output |
| 4 | Preflight Validation over the whole work plan | Implementer | Preflight | All checks above recorded with real output | WP-0021's own Preflight Validation section |
| 5 | Work-plan-level Reviewer pass | Reviewer | Review | Approval record addressing evidence-sufficiency explicitly | `docs/collaboration/reviews/2026-08-20-wp-0021-....md` |

Sequencing and dependencies: strictly 1 -> 2 -> 3 -> 4 -> 5; the fix must
not be applied before the pre-fix reproduction is captured.

## Specifications

No `docs/specs/` file covers this work plan — a narrow tooling data-fix,
not application or process behavior with its own acceptance spec.

## Boundaries

- No change to `collaboration_template_paths` (the copy-inclusion list).
- No change to any Python logic in `check-contract-consistency.py`.
- No edit to `docs/issues/LISS-0044-...md`.
- No touch to any file other than
  `scripts/lib/collaboration-template-paths.sh` (plus, transiently, a
  throwaway reproduction target directory, not committed).

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does this issue actually close `LISS-0044`, as the backlog item states? | No — independently verified `LISS-0044` is already `Status: closed`, resolved by WP-0016/LISS-0048's separate `RECORD_DIRS` fix (present-tense outbound-content scanning against the real tree), which is a different mechanism from this issue's own gap (the copy-simulation's inbound-reference exemption list). This issue does not reopen or edit `LISS-0044`'s file; the correction is recorded in LISS-0059's own text. | Design & Review group (Planner), verified by direct reading of `LISS-0044-...md`'s current `Status` field and `check-contract-consistency.py`'s current `RECORD_DIRS` contents |
| Should `docs/archive` be added to `collaboration_template_paths` (copied to adopters) as well as excluded? | No — `docs/archive` should never be copied at all (matching `docs/issues`'-and-siblings' own historical-content treatment, but more so: adopters get no `docs/archive` scaffold, since ADR 0020's own Rule 1 places Archive-layer content off the normal reading path and it holds only this template's own history). Confirmed via direct reading of `copy-ai-collaboration-files.sh`'s `copy_path()`: only `collaboration_template_paths` entries are ever visited, so an unlisted `docs/archive` is already fully un-copied; the exclude-list entry is needed only for the Python-side exemption parsing, not for the shell copy behavior itself | Design & Review group (Planner), verified by direct reading of `scripts/copy-ai-collaboration-files.sh` |

## Deferred Questions

None — this is a fully bounded, single-issue work plan with no open
question left for later.

## Verification

- Before/after copy-smoke-test reproduction (pasted output, both runs),
  using the exact invocation CI's own step uses.
- `python3 scripts/check-contract-consistency.py` (real repository) —
  no regression.
- `git diff scripts/lib/collaboration-template-paths.sh` confined to one
  added line.
- Confirmation `docs/archive` remains absent from the copied target tree.

## Falsification Criteria

This design was wrong if, after execution:

- The reproduction does not actually show the real CI failure shape
  before the fix (meaning the root-cause diagnosis is wrong).
- The reproduction still shows `docs/archive/...` dangling-reference
  failures after the fix.
- `docs/archive` starts appearing in the copied target tree after the
  fix (an over-broad change that also touched
  `collaboration_template_paths`).
- The diff touches any file, function, or constant beyond the one stated
  array entry.
- `docs/issues/LISS-0044-...md` is edited by this work plan.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. — Per ADR 0016
      Rule 2's backlog-item-level agreement:
      `docs/backlog/item-0018-archive-copy-exclusion-gap.md`'s own
      Promotion notes state "Promoted, in the Backlog-layer thread,
      immediately at capture... Design & Review proceeds autonomously from
      here," with the root cause already identified precisely and the fix
      already reproducible via PR #21's own CI failure.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Nothing in them requires guessing at a rule
      that was never stated. — Design & Review group (Planner), 2026-08-20.
      The exact one-line fix, the exact reproduction methodology, and the
      one factual correction this scope required (the `LISS-0044` premise)
      are all settled above, not left for the Implementer to guess.

If the AI cannot make its statement, the design phase is not finished,
regardless of the Director's readiness to proceed.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
