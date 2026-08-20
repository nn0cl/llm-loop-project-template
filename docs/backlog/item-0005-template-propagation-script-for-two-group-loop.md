# Backlog item: item-0005-template-propagation-script-for-two-group-loop

## Metadata

- Item ID: item-0005
- Title: Extend template propagation tooling to cover the two-group loop
  documents
- Status: promoted
- Created: 2026-08-18
- Updated: 2026-08-18
- Priority hint: medium
- Suggested planning size: TBD
- Owner/agent (optional): unassigned

## Summary

The Director wants a script that rolls this template's collaboration setup
out to other (adopter) projects — including whatever the two-group
`send_message` loop work (item-0004 / WP-0002) ultimately adds: ADR 0016,
`cross-session-messaging.md`, and the updated `personas.md`,
`ai-human-scheme.md`, `session-start-and-resume.md`,
`branch-commit-pr-discipline.md`, `design-agreement.md`, and
`docs/backlog/README.md`.

This repository already has propagation-related tooling
(`scripts/copy-ai-collaboration-files.sh`, ADR 0008
"template-update-propagation") — check whether it already picks up new
files under `docs/collaboration/*.md` and `docs/architecture/adr/*.md`
automatically, or whether it needs an explicit update once item-0004's
documents exist.

## Why it might matter

Without this, adopter projects that already copied this template would not
receive the new two-group process unless someone manually diffs and copies
the new/changed files.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes
- Boundaries or non-goals: not yet scoped — depends on what
  `scripts/copy-ai-collaboration-files.sh` and ADR 0008 already cover.

## Uncertainty

- [ ] Spec can be written now
- [x] Spike required first (options, feasibility, or quality unknown) —
      needs a short read of the existing propagation script and ADR 0008
      before this can be sized or specified.
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none yet
- Work plan (when promoted): `docs/archive/work-plans/WP-0005-template-propagation-work-plan-exclusion.md` — confirmed via direct cross-reference; this item's own `Links` field was never updated when the work landed (see `docs/issues/LISS-0065-...md`'s own cross-reference table).
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: `docs/architecture/adr/0008-template-update-propagation.md` (existing,
  related)

## Promotion notes

- Date: 2026-08-18
- Decision: Promoted, in the Backlog-layer thread, after WP-0002/item-0004
  closed. Per ADR 0016 Rule 2, this approval is the single design-phase
  gate — the Design & Review group proceeds autonomously from here
  (spike/read `scripts/copy-ai-collaboration-files.sh` and ADR 0008 first,
  since Uncertainty above marks a spike as required), building its own work
  plan, spec, and design agreement, without a further live dialogue turn
  with the Director for this item.
- Reason: Explicitly out of WP-0002's scope, raised as a distinct concern;
  now approved on its own terms.
