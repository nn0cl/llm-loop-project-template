# Backlog item: item-0003-ci-open-finding-gate

## Metadata

- Item ID: item-0003
- Title: Deterministic CI/preflight gate for open review-findings
- Status: promoted
- Created: 2026-08-10
- Updated: 2026-08-18
- Priority hint: medium
- Suggested planning size: S
- Owner/agent (optional):

## Summary

Add a deterministic check (script and/or CI step) that fails when
`Type: review-finding` issues remain open for the active work plan while
`[findings].block_work_plan_done_on_open_findings` is true in loop-settings.

## Why it might matter

Today findings must-apply is contractual and Preflight text; it is not
machine-enforced. Automation reduces silent drift.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes
- Boundaries or non-goals: do not replace the separate-context Reviewer.

## Uncertainty

- [x] Spec can be written now
- [ ] Spike required first
- [ ] Human decision required

## Links

- Parent edition: CHANGELOG v2.3.0
- Related: `docs/collaboration/findings-reuse.md`,
  `docs/collaboration/loop-settings.toml` / template

## Promotion notes

- Date: 2026-08-18
- Decision: Promoted, in the Backlog-layer thread, as part of a batch
  clearing this repo's pre-existing backlog. Per ADR 0016 Rule 2, this
  approval is the single design-phase gate — the Design & Review group
  proceeds autonomously from here. Note the overlap with item-0009's new
  `check_issue_status_sync`/consistency-checker work (WP-0007, closed) —
  reuse that infrastructure rather than building a parallel mechanism.
- Reason: Well-specified, S-sized, deterministic enforcement of an existing
  contractual rule; ready to run.
