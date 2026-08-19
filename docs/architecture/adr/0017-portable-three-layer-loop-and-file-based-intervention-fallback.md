# ADR 0017: Portable Three-Layer Loop and File-Based Intervention Fallback

## Status

Accepted. Covered by
`docs/collaboration/agreements/2026-08-18-multi-agent-tool-loop-portability.md`
(`DA-2026-08-18-03`). This ADR is additive: it does not supersede ADR 0016 or
any clause of ADR 0001 or ADR 0014, and it does not change
`docs/collaboration/cross-session-messaging.md`. Both stay exactly as they
are, Claude-Code-oriented, for the routine Design & Review <-> Implementation
handoff and the live Director intervention channel where that tool is in use
(see "What this ADR leaves untouched" below). Follow-up issues: LISS-0029
(this document) and LISS-0030 (mirror-wording propagation),
`docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md`.

`Accepted` status requires a design agreement with the Director covering the
decision. That agreement is `DA-2026-08-18-03`, whose Direction section rests
on `docs/backlog/item-0007-multi-agent-tool-loop-portability.md`
(`Status: promoted`) and the primary-source spike recorded in that
agreement's own "Spike Result" section, cited below.

## Context

ADR 0016 introduced a standing two-group topology — the Design & Review
group and the Implementation group — connected by this environment's
`SendMessage` and `ListAgents` cross-session tools, with the Director's
intervention channel (ADR 0016 Rule 4) built on the same tools. This
repository's own operating contract states from its first line that it is
"prepared for multiple AI coding agents" and ships mirror contract files for
several of them (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
`.grok/rules/*.md`, `.cursor/rules/*.mdc`). ADR 0016 and
`cross-session-messaging.md`, however, are both written in terms of
`SendMessage`/`ListAgents` specifically — a capability of this environment,
not a documented, portable primitive every AI coding tool exposes.

`docs/backlog/item-0007-multi-agent-tool-loop-portability.md`, promoted by
the Director, asked the Design & Review group to check what other AI coding
tools this template mirrors actually support, and to close the portability
gap without touching ADR 0016 or `cross-session-messaging.md` themselves.
`DA-2026-08-18-03` records the Director's own narrowed direction — reached
after push-back on the backlog item's original overclaim — and the resulting
spike, run by the Design & Review group before this agreement, is quoted
here because it is this ADR's direct evidentiary basis:

- **GitHub Copilot CLI fleet mode**
  (`docs.github.com/en/copilot/how-tos/copilot-sdk/features/fleet-mode`,
  fetched 2026-08-18): "the parent session can create clear units of
  work, assign one owner per unit... one parent session should coordinate
  several workers, collect their results, and continue the conversation
  with the combined context." Parent-child fan-out only; no peer
  discovery. Worktree behavior not documented on this page.
- **xAI Grok Build subagents**
  (`https://github.com/xai-org/grok-build/.../16-subagents.md`, fetched
  2026-08-18): "Only the top-level session spawns subagents. A subagent
  cannot spawn its own subagents: the maximum nesting depth is one."
  Worktree isolation is opt-in per call (`isolation: worktree`), not
  automatic. Completion signal: "The parent receives the child's
  output -- usually a summary -- when the child finishes," plus an
  appended `Subagent completed/failed/cancelled in Xs` block for
  blocking calls.
- **OpenAI Codex CLI subagents**
  (`learn.chatgpt.com/docs/agent-configuration/subagents`, fetched
  2026-08-18, redirected from `developers.openai.com/codex/subagents`):
  "Codex handles orchestration across agents, including spawning new
  subagents, routing follow-up instructions, waiting for results, and
  closing agent threads... Codex waits until all requested results are
  available, then returns a consolidated response." Parent-child fan-out
  only.
- **Cursor** (secondary/blog sources only, no primary Cursor doc URL
  fetched in this spike — corroborating, not conclusive): "Since Cursor
  2.0, agents run inside isolated git worktrees... each agent instance
  has its own branch and file system."
- **Conclusion**: all four tools examined implement single-orchestrator
  parent-child fan-out with a parent-side completion signal; none expose
  a documented peer-to-peer primitive equivalent to
  `SendMessage`/`ListAgents` (independently-started standing sessions
  discovering each other and exchanging messages at arbitrary times).
  This confirms, rather than overturns, the Director's already-decided
  direction — the spike found no primary-source reason to revisit it.

Two things follow from this evidence. First, the part of ADR 0016 that is
genuinely load-bearing across tools — three separated layers, and a
parent-spawns-child-in-its-own-worktree handoff shape — is exactly what every
tool examined already supports natively, under its own name for "the child
is done." Second, the part that is not portable — `SendMessage`/`ListAgents`
as a standing, peer-to-peer, arbitrary-time discovery-and-messaging
primitive — has no equivalent in any tool examined, and this ADR does not
pretend otherwise by inventing one. This ADR states both halves as testable
rules and fixes a file-based fallback, consistent with this template's
existing artifact-only-continuity model
(`docs/collaboration/session-start-and-resume.md`), for the one thing
`SendMessage`/`ListAgents` currently does that a portable baseline handoff
alone does not cover: the Director's own intervention channel (ADR 0016 Rule
4).

## Dependency Adoption Evidence

Not applicable. This decision selects no library, framework package,
provider SDK, datastore client, build tool, or test helper. It states which
part of an existing process decision (ADR 0016) is tool-agnostic and fixes
the format of a plain repository file for tools that lack a specific
cross-session capability; it adopts no new external dependency.

## Decision

### Rule 1 — The three-layer concept is tool-agnostic

ADR 0016 Rule 1's three layers — Backlog, Design & Review, Implementation —
and the principle that Backlog carries no persona of its own while Design &
Review and Implementation each carry a fixed persona set, are a
tool-agnostic separation of concerns. Any AI coding tool can implement the
same layer separation: nothing about "a Backlog thread the Director keeps
using over time," "a standing session that plans and reviews," or "a
standing session that implements in its own worktree" depends on any
capability specific to this environment. A session in any tool, operating
under this template's contract files, states which of the three layers it is
acting as, exactly as ADR 0016 Rule 1 already requires.

### Rule 2 — The portable baseline handoff

Across AI coding tools, the portable baseline for the Design & Review <->
Implementation handoff is: parent-child subagent spawning, with each child
started in its own dedicated `git worktree` and branch, using that tool's
own native parent-child completion signal for "the child is done." This is
the baseline every tool in the spike above was independently confirmed, via
primary-source fetch on 2026-08-18 (Copilot fleet mode, Grok Build's
subagents documentation, Codex CLI subagents docs), to implement as
single-orchestrator parent-child fan-out with a parent-side completion
signal — not peer-to-peer standing-session discovery. A session in any of
these tools satisfies ADR 0016's underlying handoff shape (a producing
session, a dedicated worktree, a recorded result) by using its own tool's
native spawn-and-wait mechanism; it does not need, and should not attempt to
build, a `SendMessage`/`ListAgents`-equivalent to do so. See "Context"
above for the primary-source citation naming each tool's own documentation.

### Rule 3 — `SendMessage`/`ListAgents` scope

`SendMessage` and `ListAgents` remain Claude Code's own implementation of two
distinct things: (a) the routine Design & Review <-> Implementation handoff
described by `docs/collaboration/cross-session-messaging.md`, and (b) the
sole current implementation of the Director's intervention channel (ADR 0016
Rule 4). Both are a Claude-Code-specific enhancement layered on top of the
portable baseline in Rule 2, not a requirement every tool must meet. A
session running in a tool without a `SendMessage`/`ListAgents` equivalent
does not attempt to reproduce peer-to-peer standing-session discovery; it
uses Rule 2 for the routine handoff and Rule 4 below for the intervention
channel.

### Rule 4 — File-based intervention-channel fallback

For tools without a `SendMessage`/`ListAgents` equivalent, the fallback for
the Director's intervention channel (ADR 0016 Rule 4) is a file-based status
signal: one file per in-flight work plan, at
`docs/collaboration/handoffs/WP-<NNNN>-status.md`, containing at minimum these
fields:

- `Work plan` — the work plan this status file covers.
- `Current stage` — one of: `design-agreed`, `implementation-in-progress`,
  `preflight-pass`, `review-pending`, `reviewer-approved`,
  `director-intervention-active`.
- `Director intervention gate` — `none`, or `active` with reason, date, and
  affected item, mirroring ADR 0016 Rule 4's per-item gating.
- `Last updated` — date of the most recent edit.
- `Updated by` — persona and session that made the most recent edit.

A session reads this file as part of its ordinary session-start artifact
recovery, already required by
`docs/collaboration/session-start-and-resume.md`'s existing model (see that
document's "Core Idea" and "Agent Recovery Order"). This is not a new
automation surface, daemon, or poller: it is a file, read and written like
any other repository artifact, and the Director (or a tool acting on the
Director's explicit instruction) edits the `Director intervention gate`
field directly to signal intervention, the same way any other collaboration
record in this repository is edited by hand or by an agent following a
recorded instruction.

### Rule 5 — What this ADR leaves untouched

This ADR is additive. It does not supersede ADR 0016 or any of its rules; it
does not edit or supersede `docs/collaboration/cross-session-messaging.md`.
Both remain exactly as they are, Claude-Code-oriented, for the routine
handoff and the live intervention channel where that tool is in use. Rule 1
above restates ADR 0016 Rule 1's layer concept as tool-agnostic without
changing what Rule 1 itself says; Rule 3 above narrows the *scope* of
`SendMessage`/`ListAgents` to "Claude Code's own implementation," which ADR
0016 already implied by naming this environment's tools specifically, but
never previously stated as an explicit boundary against other tools — no
existing ADR 0016 clause is reworded, weakened, or removed to state it here.

## Consequences

Positive:

- A session running in GitHub Copilot CLI, xAI Grok Build, OpenAI Codex CLI,
  or Cursor can adopt the same three-layer separation and the same
  parent-child-plus-worktree handoff shape as this template's Claude-Code
  topology, using each tool's own native primitives, instead of finding no
  guidance or a mechanism it cannot run.
- The Director's intervention channel has a fallback that works in any
  environment capable of reading and editing a repository file, closing the
  one capability gap Rule 3 identifies without inventing a new live
  notification system.
- ADR 0016 and `cross-session-messaging.md` stay exactly as written,
  avoiding the risk of a broad rewrite destabilizing an already-exercised
  protocol for the tool that does have `SendMessage`/`ListAgents`.

Negative:

- The `docs/collaboration/handoffs/` convention this ADR fixes is unused
  until a real non-Claude-Code session or Director intervention exercises
  it; its format is pinned in advance of any real use, the same known risk
  ADR 0016 itself already carries for its own Rule 4 ("Rule 4 is new and
  untested").
- A tool's own native parent-child completion signal is not documented here
  in per-tool operational detail (only the spike's primary-source quotes
  above); a session in one of these tools still needs to consult that tool's
  own current documentation for the exact mechanics, which can drift
  independently of this ADR.
- Cursor's own entry in the spike relies on secondary/blog sources only, per
  `DA-2026-08-18-03`'s "Deferred Questions" — a future Reviewer or Director
  may judge that corroboration insufficient and request a primary-source
  spike specifically for Cursor.

## Enforcement

Code review should reject:

- a mirror-file change (per LISS-0030) that describes `SendMessage`/
  `ListAgents` as available or required in an environment that does not
  provide them, without the file-based fallback of Rule 4 named as the
  default.
- any edit to ADR 0016 or `cross-session-messaging.md` made under cover of
  this ADR's own change.
- a `docs/collaboration/handoffs/WP-<NNNN>-status.md` file used, or described,
  as anything other than a file read and written as part of ordinary
  session-start artifact recovery — for example, wired into a daemon, a
  poller, or a scheduled job.
- a `docs/collaboration/handoffs/WP-<NNNN>-status.md` file missing one of the
  five fields Rule 4 states, or a `Director intervention gate` value other
  than `none` or `active` with reason, date, and affected item.
