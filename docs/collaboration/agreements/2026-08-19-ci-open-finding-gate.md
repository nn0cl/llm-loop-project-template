# Design Agreement: Deterministic Gate for Open Review-Finding Issues

## Identity

- Agreement ID: DA-2026-08-19-03
- Date: 2026-08-19
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0003-ci-open-finding-gate.md` (`Status: promoted`):
add a deterministic check that fails when a work plan being closed still
lists a `Type: review-finding` issue that is not `closed` or `wont_do`, when
`[findings].block_work_plan_done_on_open_findings` is `true` in
`docs/collaboration/loop-settings.toml`. Per the backlog item's own
Promotion notes, reuse WP-0007/item-0009's new
`scripts/check-contract-consistency.py` infrastructure rather than building
a parallel mechanism.

## Spike Result

- Read `docs/collaboration/findings-reuse.md`'s "Work-plan gate" section:
  "Work-plan Done requires every finding from that plan's Reviewer pass to
  be `closed` or `wont_do` (with Arbiter)."
- Read `docs/collaboration/loop-settings.toml`: `[findings].must_apply =
  true` and `[findings].block_work_plan_done_on_open_findings = true` are
  both set (the defaults this repository currently runs under).
- **Real, currently-live test case found**: `docs/issues/LISS-0003-*.md`
  is genuinely `Type: review-finding`, `Status: resolved` (not `closed`) —
  a real, pre-existing gap in this repository's own housekeeping (the
  finding was fixed but never given its final separate-context Reviewer
  closure step). It is not referenced in any work plan's own "Work-Plan
  Review" findings table, so it does not, by itself, trigger the gate this
  item builds (which anchors on a work plan's own findings table, per
  "Settled Ambiguities" below) — but it is real evidence that
  `resolved`-not-`closed` findings genuinely occur in this repository, not
  a hypothetical.
- Every work plan file already in this repository (`WP-0001` through
  `WP-0009`) carries a "Work-Plan Review" section with a fixed-shape
  findings table: `| Issue | Status | Resolution |`. This is the anchor
  point WP-0007's `check_issue_status_sync` already reads a comparable
  table shape from (its Issue Graph parsing) — the same technique applies
  directly, reusing the existing `read`/`glob` helpers rather than adding
  new infrastructure.

## Scope

- In scope:
  - A new check function, `check_open_findings_gate`, in
    `scripts/check-contract-consistency.py`: for each `docs/work-plans/
    WP-*.md` whose "Work-Plan Close" section states a non-placeholder
    `Date:` (i.e., the plan has been, or is being, closed), read its
    "Work-Plan Review" findings table; for each listed issue ID, read that
    issue's own live `Status:` field; if `[findings].block_work_plan_done_on_open_findings`
    is `true` (read from `docs/collaboration/loop-settings.toml`, default
    `true` when the file or key is absent, matching the contract's own
    stated default) and the issue's Status is neither `closed` nor
    `wont_do`, report a failure naming the work plan, the issue, and its
    actual Status.
  - Wire it into `main()` and the module docstring's numbered check list,
    same pattern as WP-0007's three additions.
  - Not an ADR-0006 contract file — no trace required.
- Explicitly out of scope:
  - Any change to `findings-reuse.md`'s lifecycle or must-apply rule.
  - Retroactively forcing `LISS-0003` to `closed` — out of this item's own
    scope (it does not trigger the new gate, since no work plan's findings
    table currently lists it; fixing that pre-existing housekeeping gap is
    a separate, optional finding this review may flag, not a requirement
    of item-0003 itself).
  - Replacing the separate-context Reviewer with automation — explicit
    non-goal, per item-0003's own "Known constraints."

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Add `check_open_findings_gate` | Implementer | Architecture Path | Detects a closed work plan with an open (non-`closed`/`wont_do`) listed finding, via a constructed synthetic case; passes clean on current `HEAD`; honors the `loop-settings.toml` flag (both `true` and `false`, tested) | clean pass on `HEAD`; synthetic failure case; synthetic pass case with the flag set `false` |
| 2 | Wire into `main()` and the docstring | Implementer | Architecture Path | Check runs as part of the normal script invocation; docstring lists it | read-through |
| 3 | Self-review | Implementer | Architecture Path | Short-form self-review (single new function, one integration point) | self-review record in LISS-0039 Work Notes |
| 4 | Preflight | Implementer / deterministic tool | Architecture Path | `pass` recorded | Preflight section in WP-0011 |
| 5 | Work-plan-level Reviewer pass | Reviewer (Design & Review group, separate context) | Architecture Path | Independently constructs its own synthetic failure case, not only re-reads the Implementer's | review record under `docs/collaboration/reviews/` |

Sequencing: Task 1 blocks 2. Task 2 blocks 3. Task 3 blocks 4. Task 4 blocks
5.

## Specifications

- None. Tooling extension; no application specification.

## Boundaries

- Reuses `scripts/check-contract-consistency.py`'s existing helpers
  (`read`, `glob`-based file discovery) rather than a parallel script or
  mechanism.
- Does not replace the separate-context Reviewer's own judgment — this is
  a mechanical precondition check, the same status the script's other
  checks already hold.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` until the
  Director's own work-plan-close action.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| What does "the active work plan" mean for a static, non-interactive check with no notion of session state? | A work plan whose own "Work-Plan Close" section states a non-placeholder `Date:` — i.e., a plan that has been (or is actively being) closed. This is the same signal a human reader already uses, present in every existing work-plan file, and avoids inventing a new "active" concept the file format does not already carry. | Design & Review group (Planner) |
| How does the check know which findings belong to which work plan? | Each work plan's own "Work-Plan Review" section already carries a `| Issue | Status | Resolution |` findings table — this check reads that table directly, the same anchor-on-existing-structure technique WP-0007's checks already use, rather than inferring the link from a finding's own free-text content. | Design & Review group (Planner) |
| Does `LISS-0003`'s real `resolved`-not-`closed` state get flagged by this new check? | No — it is not listed in any work plan's findings table, so the check has no anchor to it. This is disclosed explicitly, not silently assumed to be "handled," and may be worth a separate housekeeping fix later, out of this item's own scope. | Design & Review group (Planner), confirmed by direct inspection |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should `LISS-0003` be retroactively linked into its owning work plan's findings table (if one can be identified) so this new gate would actually cover it? | A future finding or housekeeping pass — not blocking for this item, which builds the mechanism, not a retroactive data-cleanup pass over pre-existing untracked findings |

## Verification

- Clean pass on current `HEAD`.
- Synthetic failure case (open finding in a closed work plan, flag `true`).
- Synthetic pass case (same open finding, flag `false`) — confirms the
  check actually reads the setting rather than always failing/passing.
- Work-plan-level Reviewer approval, independently reconstructing at least
  one synthetic case.

## Falsification Criteria

- The check infers a finding-to-work-plan link from free text instead of
  the work plan's own structured findings table.
- The check ignores `[findings].block_work_plan_done_on_open_findings`
  and always/never fires regardless of its value.
- The check is built as a separate script/mechanism instead of extending
  `scripts/check-contract-consistency.py`.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0003-ci-open-finding-gate.md`, `Status: promoted`,
      Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
