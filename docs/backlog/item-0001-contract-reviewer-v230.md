# Backlog item: item-0001-contract-reviewer-v230

## Metadata

- Item ID: item-0001
- Title: Separate-context Reviewer for v2.3.0 contract change
- Status: promoted
- Created: 2026-08-10
- Updated: 2026-08-18
- Note: `v2.3.0` was tagged on Director instruction while this Reviewer
  pass remains open. Completing this item closes the ADR 0006 gap for the
  edition; it does not re-tag unless findings require a patch release.
- Priority hint: high
- Suggested planning size: M
- Owner/agent (optional):

## Summary

Obtain Reviewer approval from a separate context for the v2.3.0 agent
operating contract and collaboration-doc changes, per ADR 0006 and
`docs/collaboration/prompt-instruction-change-control.md`.

## Why it might matter

Contract-file changes are never self-reviewed. Landing without independent
Reviewer leaves the edition unclosed for adopters who require a reviewed
contract.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes
- Boundaries or non-goals: does not re-open feature design; review artifacts
  only.

## Uncertainty

- [x] Spec can be written now
- [ ] Spike required first (options, feasibility, or quality unknown)
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case:
- Work plan (when promoted):
- Design agreement (when promoted):
- Local issue (LISS):
- Spec:
- ADR: ADR 0006
- Parent edition: CHANGELOG v2.3.0

## Promotion notes

- Date: 2026-08-18
- Decision: Promoted, in the Backlog-layer thread, as part of a batch
  clearing this repo's pre-existing backlog. Per ADR 0016 Rule 2, this
  approval is the single design-phase gate — the Design & Review group
  proceeds autonomously from here: confirm the v2.3.0 contract change's
  actual current review state before assuming it is still open, then build
  the work plan, spec, and design agreement.
- Reason: Well-specified, high-priority, real ADR-0006 governance gap; ready
  to run.
