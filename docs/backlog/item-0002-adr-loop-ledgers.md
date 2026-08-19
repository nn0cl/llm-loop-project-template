# Backlog item: item-0002-adr-loop-ledgers

## Metadata

- Item ID: item-0002
- Title: Process ADR for spike, backlog, loop-settings, findings-reuse
- Status: promoted
- Created: 2026-08-10
- Updated: 2026-08-18
- Priority hint: medium
- Suggested planning size: M
- Owner/agent (optional):

## Summary

Promote the docs-first loop ledger rules (spike cases, backlog promotion,
loop-settings, post-hoc audit, findings must-apply) into an accepted process
ADR so adopters can cite a single decision record.

## Why it might matter

Today the rules live in collaboration docs and agent mirrors. An ADR would
stabilize numbering and supersession for later process changes.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes
- Boundaries or non-goals: must not rewrite ADR 0012–0015 without grounds.

## Uncertainty

- [x] Spec can be written now
- [ ] Spike required first
- [ ] Human decision required

## Links

- Parent edition: CHANGELOG v2.3.0
- Related: `docs/spike/README.md`, `docs/backlog/README.md`,
  `docs/collaboration/loop-settings.md`,
  `docs/collaboration/findings-reuse.md`,
  `docs/collaboration/post-hoc-audit.md`

## Promotion notes

- Date: 2026-08-18
- Decision: Promoted, in the Backlog-layer thread, as part of a batch
  clearing this repo's pre-existing backlog. Per ADR 0016 Rule 2, this
  approval is the single design-phase gate — the Design & Review group
  proceeds autonomously from here, including confirming no conflict with
  ADR 0012-0015's existing numbering/supersession.
- Reason: Well-specified, docs-first hardening; ready to run.
