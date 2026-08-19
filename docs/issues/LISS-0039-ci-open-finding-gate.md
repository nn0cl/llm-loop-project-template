# LISS-0039: Deterministic gate for open review-finding issues

## Metadata

- Local issue ID: LISS-0039
- GitHub issue: none
- Status: ready
- Phase: phase-0-design
- Type: tooling-enhancement
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/ci-open-finding-gate

## Summary

- Add `check_open_findings_gate` to `scripts/check-contract-consistency.py`:
  for each `docs/work-plans/WP-*.md` whose "Work-Plan Close" section states
  a non-placeholder `Date:`, read its "Work-Plan Review" findings table;
  for each listed issue ID, read the issue's own live `Status:`; if
  `[findings].block_work_plan_done_on_open_findings` is `true` (from
  `docs/collaboration/loop-settings.toml`, default `true` when absent) and
  the status is neither `closed` nor `wont_do`, report a failure.

## Acceptance Notes

- Clean pass against current `HEAD`.
- Constructed synthetic failure case (open finding, flag `true`) correctly
  flagged, with actual command output pasted.
- Constructed synthetic pass case (same finding, flag `false`) correctly
  passes, confirming the flag is actually read, not ignored.
- Module docstring's numbered check list updated.
- Reuses existing script helpers (`read`, `glob`) rather than new
  infrastructure or a separate script.
- Self-review recorded (full form — planning size `M`).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0003-ci-open-finding-gate.md
- Depends on: none
- Blocks: none
- Related: `docs/collaboration/findings-reuse.md`,
  `docs/collaboration/loop-settings.toml`, WP-0007/LISS-0035 (the sibling
  infrastructure this issue extends)

## Decisions Not Settled by the Design Agreement

- None identified.

## Context

- Included: `docs/backlog/item-0003-*.md`, `DA-2026-08-19-03`,
  `scripts/check-contract-consistency.py` (whole file), every current
  `docs/work-plans/WP-*.md`'s "Work-Plan Review"/"Work-Plan Close" section
  shape, `docs/collaboration/loop-settings.toml`,
  `docs/collaboration/findings-reuse.md`.
- Omitted: `docs/issues/LISS-0003-*.md`'s own correction (explicitly out of
  scope).
- Assumptions: none beyond the design agreement's own settled points.

## AI Planning Records

### AIP-0039-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Sonnet 5 via Claude Code, Design & Review
    group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: not surfaced in this environment
- Created at: 2026-08-19
- Planning size: M
- Intended execution route: Implementation-group agent, Architecture Path,
  one new function plus its wiring
- Compatibility state: Verified — confirmed the exact findings-table shape
  by reading several real work-plan files
- Intended scope: `scripts/check-contract-consistency.py` only
- Estimated token range: 6,000-14,000 tokens
- Estimated token midpoint: 9,000
- Token metric: approximate output tokens including synthetic-test
  construction
- Estimation basis: comparable to WP-0007's individual check functions
- Assumptions: single execution attempt
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/collaboration/agreements/2026-08-19-ci-open-finding-gate.md`
  (`DA-2026-08-19-03`)

## Work Notes

- 2026-08-19 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0003-*.md`'s promotion. Found `LISS-0003` as a real,
  currently-live `Type: review-finding`/`Status: resolved` case during the
  spike, confirmed it does not trigger the new gate (not referenced in any
  work plan's findings table) and disclosed that explicitly rather than
  silently. Dispatched to the Implementation group.

## Verification

- Pending Implementation-group execution.
