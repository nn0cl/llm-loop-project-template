# Design Agreement: Portable Three-Layer Loop Across AI Coding Tools

## Identity

- Agreement ID: DA-2026-08-18-03
- Date: 2026-08-18
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0007-multi-agent-tool-loop-portability.md`
(`Status: promoted`), whose Promotion notes are this agreement's Director
authorization under ADR 0016 Rule 2, and whose body already records the
Director's narrowed direction (2026-08-18, after push-back on the item's
original overclaim):

- The baseline Design & Review <-> Implementation handoff, across all AI
  coding tools this template mirrors, is parent-child subagent spawning,
  each child in its own dedicated `git worktree`/branch, using each tool's
  own native parent-child completion signal — not a requirement that every
  tool have a `SendMessage`/`ListAgents`-equivalent.
- `SendMessage`/`ListAgents` stay in the model, scoped narrowly to the
  Director's intervention channel (ADR 0016 Rule 4), which is a
  Claude-Code-specific capability that does not need to be portable the same
  way the baseline handoff does.
- ADR 0016 and `docs/collaboration/cross-session-messaging.md` are not
  changed by this item (explicit non-goal in the backlog item); this item
  updates the contract *mirror* files (`AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`,
  `.cursor/rules/*.mdc`) so a tool without `SendMessage` is not left
  describing a mechanism it cannot execute.
- A file-based fallback is needed for the intervention channel (Rule 4) on
  tools without live cross-session messaging, consistent with this
  template's existing artifact-only-continuity model
  (`docs/collaboration/session-start-and-resume.md`).

## Spike Result (run by the Design & Review group before this agreement)

Primary-vendor-doc verification, per item-0007's own narrowed Uncertainty:

- **GitHub Copilot CLI fleet mode** (`docs.github.com/en/copilot/how-tos/copilot-sdk/features/fleet-mode`,
  fetched 2026-08-18): "the parent session can create clear units of work,
  assign one owner per unit... one parent session should coordinate several
  workers, collect their results, and continue the conversation with the
  combined context." Parent-child fan-out only; no peer discovery. Worktree
  behavior not documented on this page.
- **xAI Grok Build subagents** (`github.com/xai-org/grok-build/.../16-subagents.md`,
  fetched 2026-08-18): "Only the top-level session spawns subagents. A
  subagent cannot spawn its own subagents: the maximum nesting depth is
  one." Worktree isolation is opt-in per call (`isolation: worktree`), not
  automatic. Completion signal: "The parent receives the child's output --
  usually a summary -- when the child finishes," plus an appended
  `Subagent completed/failed/cancelled in Xs` block for blocking calls.
- **OpenAI Codex CLI subagents** (`learn.chatgpt.com/docs/agent-configuration/subagents`,
  fetched 2026-08-18, redirected from `developers.openai.com/codex/subagents`):
  "Codex handles orchestration across agents, including spawning new
  subagents, routing follow-up instructions, waiting for results, and
  closing agent threads... Codex waits until all requested results are
  available, then returns a consolidated response." Parent-child fan-out
  only.
- **Cursor** (secondary/blog sources only, no primary Cursor doc URL
  fetched in this spike — treated as corroborating, not conclusive): "Since
  Cursor 2.0, agents run inside isolated git worktrees... each agent
  instance has its own branch and file system."
- **Conclusion**: all four tools examined implement single-orchestrator
  parent-child fan-out with a parent-side completion signal; none expose a
  documented peer-to-peer primitive equivalent to `SendMessage`/`ListAgents`
  (independently-started standing sessions discovering each other and
  exchanging messages at arbitrary times). This confirms, rather than
  overturns, the Director's already-decided direction above — the spike
  found no primary-source reason to revisit it.

## Scope

- In scope:
  - A new ADR (`docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`,
    LISS-0029) recording: the three-layer concept (Backlog / Design &
    Review / Implementation) is tool-agnostic; the portable baseline
    handoff is parent-child spawn + dedicated worktree per child, using
    each tool's own completion signal; `SendMessage`/`ListAgents` remain
    Claude Code's own implementation of the routine handoff and the sole
    implementation of the Director's intervention channel; for tools
    without an equivalent, the intervention-channel fallback is a
    file-based status signal under a new `docs/collaboration/handoffs/`
    directory (format fixed in "Settled Ambiguities" below).
  - Mirror propagation (LISS-0030): add a compact, portable two/three-layer
    section to `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
    `.grok/rules/*.md`, and `.cursor/rules/*.mdc`, scoping the live-session
    handoff mechanism explicitly to environments where `SendMessage`/
    `ListAgents` (or an equivalent) are available, naming the file-based
    fallback as the default everywhere else, per ADR 0017.
  - AI work trace(s) for the mirror-file changes (LISS-0030) — all five are
    ADR-0006 contract files.
  - Preflight and separate-context Reviewer pass.
- Explicitly out of scope:
  - Any change to ADR 0016 or `docs/collaboration/cross-session-messaging.md`
    (explicit non-goal in `item-0007`; those documents stay Claude-Code
    -oriented, per the Director's own narrowed direction).
  - A new cross-tool live-notification/messaging bridge. The fallback is
    file/artifact-based only.
  - Wiring the new `docs/collaboration/handoffs/` convention into
    `docs/collaboration/session-start-and-resume.md`'s own session-type
    table — deferred (see "Deferred Questions"); this agreement authorizes
    the convention's existence and its use in the mirror files' portable
    wording, not a rewrite of that file.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Write ADR 0017 | Implementer | Architecture Path | States the three tool-agnostic elements (layer concept, parent-child+worktree baseline, file-based intervention fallback) as testable rules; fixes the `docs/collaboration/handoffs/` file format exactly as pinned in Settled Ambiguities; cites the spike's primary-source findings above; states explicitly that ADR 0016/`cross-session-messaging.md` are unchanged | read-through against this Direction; not an ADR-0006 contract file, so no trace required (mirrors ADR 0016's own precedent) |
| 2 | Propagate portable wording into `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.grok/rules/*.md`, `.cursor/rules/*.mdc` | Implementer | Architecture Path | Each file gains equivalent effective content (per ADR 0006's "agreement means equivalent effective content" rule) stating the three-layer concept and the parent-child+worktree baseline; the live-handoff/`SendMessage` description is explicitly scoped to environments where it exists; the file-based fallback is named as the default; no existing rule in any mirror is weakened or removed | `scripts/check-contract-consistency.py`; read-through diff of all five files side by side |
| 3 | AI work trace for Task 2 | Implementer | Architecture Path | Trace names all five files, the reason, and the expected agent-behavior change | trace file exists under `docs/collaboration/traces/` |
| 4 | Self-review Tasks 1-3 | Implementer | Architecture Path | Short-form self-review (single cohesive propagation change) per `docs/templates/self-review.md` | self-review record in LISS-0030 Work Notes |
| 5 | Preflight Validation | Implementer / deterministic tool | Architecture Path | `pass` recorded with command output | Preflight section in WP-0004 |
| 6 | Separate-context Reviewer pass | Reviewer (Design & Review group, separate context) | Architecture Path | Review record explicitly addresses each of the five mirror-file changes under ADR 0006, and confirms ADR 0017's own content against this Direction | review record under `docs/collaboration/reviews/` |

Sequencing: Task 1 blocks Task 2 (mirror wording should cite ADR 0017 by
number, so it must exist first). Task 3 follows Task 2. Task 4 follows 1-3.
Task 5 follows 4. Task 6 follows 5.

## Specifications

- None. Process/governance change; no application specification.

## Boundaries

- ADR 0006's separate-context Reviewer and traceability rules apply in full
  to the five mirror-file edits, regardless of Architecture Path structure.
- ADR 0016 and `docs/collaboration/cross-session-messaging.md` are not
  edited by this work plan (see Scope). A discovered need to edit either is
  a reopening trigger, not a judgment call.
- No new live cross-tool messaging mechanism is built. The fallback is
  strictly a file a session reads/writes as part of its existing
  artifact-recovery reading, not a poller, daemon, or scheduled job.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` until the
  Director's own work-plan-close action.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Exact `docs/collaboration/handoffs/` file format for the intervention-channel fallback | One file per in-flight work plan: `docs/collaboration/handoffs/WP-NNNN-status.md`, containing at minimum: `Work plan`, `Current stage` (one of: `design-agreed`, `implementation-in-progress`, `preflight-pass`, `review-pending`, `reviewer-approved`, `director-intervention-active`), `Director intervention gate` (`none`, or `active` with reason/date/affected item per ADR 0016 Rule 4), `Last updated`, `Updated by` (persona and session). A tool without `SendMessage` reads this file as part of ordinary session-start artifact recovery (already required by `docs/collaboration/session-start-and-resume.md`'s existing model); the Director (or an assisting tool acting on the Director's instruction) edits the `Director intervention gate` field directly to signal intervention. This is a read/write file, not a new automation surface. | Design & Review group (Planner), consistent with the backlog item's own "status field or small file... polled for at the start of a fresh session" suggestion |
| Does this item change ADR 0016 or `cross-session-messaging.md`? | No — explicit non-goal; ADR 0017 references them but does not alter them. | Backlog item-0007's own stated boundary |
| ADR number | 0017 (confirmed as the next-free ADR number by directory listing before drafting) | Implementer, to confirm at execution time before Task 1 |
| Which mirror files get how much content | All five get equivalent effective content per ADR 0006's existing "equivalent effective content, not literal text match" rule — Cursor's own effective-content rule (root `AGENTS.md` auto-apply plus `.mdc` complements) already governs how Cursor's copy differs in form from the four literal-mirror files; this item does not change that governing rule, only what portable two/three-layer content gets propagated through it. | Implementer, applying `docs/collaboration/prompt-instruction-change-control.md`'s existing rule, not inventing a new one |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should `docs/collaboration/session-start-and-resume.md` gain its own explicit cross-reference to the `docs/collaboration/handoffs/` convention (beyond what ADR 0017 itself states)? | A future backlog item, once the convention has actually been used at least once by a non-Claude-Code tool session or by a Director intervention on a tool lacking `SendMessage` — premature to wire deeper before real use |
| Should Cursor get its own primary-source-verified spike entry (this agreement's Spike Result relied on secondary/blog sources for Cursor only)? | If a future Reviewer or Director judges the secondary-source corroboration insufficient; not blocking for this item since the Direction was already decided independent of this spike's outcome |

## Verification

- `scripts/check-contract-consistency.py` after the mirror edits.
- Read-through diff confirming all five mirror files still agree in
  effective content on the new portable section.
- Confirmation that `docs/collaboration/traces/` contains a trace for the
  mirror-file change.
- Separate-context Reviewer approval addressing each mirror-file change
  under ADR 0006 explicitly, and confirming ADR 0017 does not silently
  alter ADR 0016 or `cross-session-messaging.md`.

## Falsification Criteria

- Any mirror file, after this work plan, describes `SendMessage`/
  `ListAgents` as available or required in an environment that does not
  provide them, without the file-based fallback named as the default.
- ADR 0016 or `cross-session-messaging.md` is edited by this work plan.
- The `docs/collaboration/handoffs/` mechanism grows into a live
  notification system (a daemon, a poller, a scheduled job) rather than a
  file read/written as part of existing session-start artifact recovery.
- A mirror-file change lands without a trace or without separate-context
  Reviewer approval.
- `scripts/check-contract-consistency.py` fails after the mirror edits and
  the work plan proceeds anyway.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0007-multi-agent-tool-loop-portability.md`,
      `Status: promoted`, Promotion notes and body (including the
      Director's own narrowed "Direction decided" paragraph), per ADR 0016
      Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan and the spike result above.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
