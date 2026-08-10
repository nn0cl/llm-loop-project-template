# Backlog item: item-0001-contract-reviewer-v230

## Metadata

- Item ID: item-0001
- Title: Separate-context Reviewer for v2.3.0 contract change
- Status: ready-for-planning
- Created: 2026-08-10
- Updated: 2026-08-10
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

- Date:
- Decision: subordinate follow-up to v2.3.0 land
- Reason: Director asked to land incomplete work as dependents and commit
