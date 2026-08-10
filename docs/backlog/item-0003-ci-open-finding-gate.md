# Backlog item: item-0003-ci-open-finding-gate

## Metadata

- Item ID: item-0003
- Title: Deterministic CI/preflight gate for open review-findings
- Status: captured
- Created: 2026-08-10
- Updated: 2026-08-10
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

- Date:
- Decision: subordinate to v2.3.0
- Reason: policy first; enforcement second
