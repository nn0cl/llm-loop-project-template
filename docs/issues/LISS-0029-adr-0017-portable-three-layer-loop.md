# LISS-0029: Write ADR 0017 (portable three-layer loop, file-based intervention fallback)

## Metadata

- Local issue ID: LISS-0029
- GitHub issue: none
- Status: ready
- Phase: phase-0-design (produces an Architecture Path artifact, not
  application code)
- Type: architecture-decision
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/adr-0017-portable-loop

## Summary

- Write `docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`
  stating: (1) the three-layer concept (Backlog / Design & Review /
  Implementation, per ADR 0016 Rule 1) is tool-agnostic; (2) the portable
  baseline handoff across AI coding tools is parent-child subagent spawning,
  each child in its own dedicated `git worktree`/branch, using each tool's
  own native completion signal; (3) `SendMessage`/`ListAgents` remain Claude
  Code's own implementation of the routine handoff and the sole
  implementation of the Director's intervention channel (ADR 0016 Rule 4);
  (4) for tools without an equivalent, the intervention-channel fallback is
  a file-based status signal under `docs/collaboration/handoffs/`, in the
  exact format `DA-2026-08-18-03` pins down (one file per in-flight work
  plan: `docs/collaboration/handoffs/WP-NNNN-status.md`).

## Acceptance Notes

- States which ADR 0001/0014/0016 clauses this ADR adds to versus leaves
  untouched (it should add a portability layer, not supersede anything —
  confirm no supersession language is needed, since this is additive).
- Explicitly states ADR 0016 and `cross-session-messaging.md` are unchanged
  by this ADR.
- Cites the primary-source spike findings recorded in `DA-2026-08-18-03`'s
  "Spike Result" section (Copilot fleet mode, Grok Build subagents.md,
  Codex CLI subagents docs).
- Fixes the `docs/collaboration/handoffs/WP-NNNN-status.md` field list
  exactly as `DA-2026-08-18-03`'s Settled Ambiguities table states.
- Not an ADR-0006 contract file (mirrors ADR 0016's own precedent — no
  trace required for this issue).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0007-multi-agent-tool-loop-portability.md
- Depends on: none
- Blocks: LISS-0030 (mirror wording cites this ADR by number)
- Related: ADR 0016, `docs/collaboration/cross-session-messaging.md`
  (referenced, not edited)

## Decisions Not Settled by the Design Agreement

- The exact ADR number is pinned as 0017 in `DA-2026-08-18-03`, but the
  Implementer must confirm it is still the next-free number at execution
  time (`ls docs/architecture/adr/` before creating the file) in case
  another concurrent work plan has since claimed it — if so, this is a
  reopening-worthy conflict, not a silent renumbering.

## Context

- Included: ADR 0016, `docs/collaboration/cross-session-messaging.md`,
  `docs/collaboration/session-start-and-resume.md`,
  `docs/backlog/item-0007-*.md`, `DA-2026-08-18-03`.
- Omitted: WP-0002's per-issue traces — not needed to write a new,
  additive ADR.
- Assumptions: the spike's primary-source findings (recorded in
  `DA-2026-08-18-03`) are accurate as of 2026-08-18; if the Implementer
  finds reason to doubt them, that is a reopening trigger.

## AI Planning Records

### AIP-0029-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Sonnet 5 via Claude Code, Design & Review
    group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A (not surfaced in this environment)
  - N/A reason: this environment does not display a reasoning-effort label
    to the session itself
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Implementation-group agent, Architecture Path,
  single ADR document
- Compatibility state: Verified — ADR template and numbering convention
  read directly from `docs/templates/adr.md` and `docs/architecture/adr/`
  directory listing
- Intended scope: one new file under `docs/architecture/adr/`
- Estimated token range: 3,000-8,000 tokens
- Estimated token midpoint: 5,000
- Token metric: approximate output tokens for drafting one ADR of similar
  length to ADR 0016
- Estimation basis: ADR 0016 itself is roughly 6,000-7,000 tokens rendered;
  ADR 0017 is additive and narrower in scope, expected similar or smaller
- Assumptions: single execution attempt; no major restructuring needed
  after self-review
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
- `docs/backlog/item-0007-multi-agent-tool-loop-portability.md` — cites,
  fetch-verified 2026-08-18: `docs.github.com/en/copilot/how-tos/copilot-sdk/features/fleet-mode`,
  `github.com/xai-org/grok-build/.../16-subagents.md`,
  `learn.chatgpt.com/docs/agent-configuration/subagents`
- `docs/templates/adr.md`

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0007-*.md`'s promotion, after running the primary-source
  spike recorded in `DA-2026-08-18-03`. Dispatched to the Implementation
  group together with LISS-0030.

## Verification

- Pending Implementation-group execution.
