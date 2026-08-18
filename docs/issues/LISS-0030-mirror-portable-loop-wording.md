# LISS-0030: Propagate portable three-layer loop wording to contract mirrors

## Metadata

- Local issue ID: LISS-0030
- GitHub issue: none
- Status: ready
- Phase: phase-0-design (contract-file propagation, no application code)
- Type: contract-propagation
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/mirror-portable-loop-wording

## Summary

- Add equivalent-effective-content, portable wording to `AGENTS.md`,
  `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md`, and
  `.cursor/rules/*.mdc` (per ADR 0006's mirror-parity rule) stating: the
  three-layer concept from ADR 0016 (Backlog / Design & Review /
  Implementation); the portable baseline handoff (parent-child subagent
  spawn, dedicated worktree per child, native completion signal); that the
  live-session `SendMessage`/`ListAgents` handoff and Director intervention
  channel are Claude-Code-specific, described in full only in
  `docs/collaboration/cross-session-messaging.md`; and that the default
  intervention-channel fallback everywhere else is the
  `docs/collaboration/handoffs/WP-NNNN-status.md` file convention ADR 0017
  defines. Cross-reference ADR 0017 by path from each mirror.

## Acceptance Notes

- `scripts/check-contract-consistency.py` passes.
- Read-through confirms all five files carry equivalent effective content
  on this new section (not necessarily identical text — Cursor's own
  effective-content composition rule from
  `docs/collaboration/prompt-instruction-change-control.md` still applies).
- No existing rule in any of the five files is weakened, removed, or
  contradicted.
- New section is proportionate to each file's existing style/length (do not
  import the full ADR 0016 text into each mirror — a compact pointer plus
  the portable rule statement is sufficient, mirroring how these files
  already summarize other ADRs rather than reproducing them).
- AI work trace exists under `docs/collaboration/traces/` naming all five
  files, the reason, and the expected agent-behavior change.
- Self-review recorded (short form is appropriate — one cohesive
  propagation change across five files, same pattern in every file).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0007-multi-agent-tool-loop-portability.md
- Depends on: LISS-0029 (cites ADR 0017 by number/path)
- Blocks: none
- Related: `docs/architecture/adr/0006-prompt-instruction-change-control.md`
  (governs the mirror-parity rule itself)

## Decisions Not Settled by the Design Agreement

- Exact prose/wording per file is left to the Implementer, bounded by the
  acceptance criteria above and the "equivalent effective content" rule —
  this is execution-level phrasing, not a planning ambiguity, per
  `docs/collaboration/design-agreement.md`'s existing pattern of leaving
  "exact SendMessage template wording" etc. to Implementer discretion.

## Context

- Included: ADR 0017 (once LISS-0029 lands), `DA-2026-08-18-03`, all five
  mirror files' current content, `docs/collaboration/prompt-instruction-change-control.md`.
- Omitted: the full text of ADR 0016 and `cross-session-messaging.md` —
  mirrors point at them, they do not reproduce them.
- Assumptions: none beyond LISS-0029's ADR 0017 existing and being stable
  before this issue starts editing (enforced by the dependency above).

## AI Planning Records

### AIP-0030-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Sonnet 5 via Claude Code, Design & Review
    group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: not surfaced in this environment
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Implementation-group agent, Architecture Path,
  five coordinated file edits plus one trace
- Compatibility state: Verified — confirmed via `grep` that none of the
  five files currently mention the two-group topology at all, so this is a
  pure addition, not a reconciliation of drifted content
- Intended scope: `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md` (3 files),
  `.cursor/rules/*.mdc` (3 files) — effectively up to 9 files depending on
  which `.grok`/`.cursor` rule file is the right home for this content;
  Implementer decides, consistent with how those directories are already
  organized (01-quickstart / 02-architecture-boundaries /
  03-collaboration-and-completion)
- Estimated token range: 6,000-15,000 tokens
- Estimated token midpoint: 10,000
- Token metric: approximate output tokens across all edited files plus the
  trace
- Estimation basis: WP-0002's own mirror-parity precedent
  (`docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`,
  Task 4, "propagation across nine contract files") as an order-of-magnitude
  reference, scaled down since this is one small section, not a full
  propagation pass
- Assumptions: single execution attempt
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/collaboration/prompt-instruction-change-control.md`
- `docs/architecture/adr/0006-prompt-instruction-change-control.md`
- `docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`
  (mirror-propagation precedent)

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0007-*.md`'s promotion. Confirmed via
  `grep -rln "session group\|two-group\|cross-session-messaging\|SendMessage\|ListAgents" AGENTS.md CLAUDE.md .github/copilot-instructions.md .grok/rules/ .cursor/rules/`
  (no matches) that none of the five files currently describe the
  two-group topology — this issue is a pure addition. Dispatched to the
  Implementation group together with LISS-0029.

## Verification

- Pending Implementation-group execution.
