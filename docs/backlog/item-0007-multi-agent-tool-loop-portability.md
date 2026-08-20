# Backlog item: item-0007-multi-agent-tool-loop-portability

## Metadata

- Item ID: item-0007
- Title: Make the standing multi-layer loop (ADR 0016) adoptable by AI coding
  tools other than Claude Code
- Status: promoted
- Created: 2026-08-18
- Updated: 2026-08-18
- Priority hint: medium
- Suggested planning size: TBD
- Owner/agent (optional): unassigned

## Summary

This template mirrors its agent operating contract across multiple AI coding
tools (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`,
`.grok/rules/*.md`, `.cursor/rules/*.mdc` — see ADR 0006's "Per-vendor
grounds"). ADR 0016 (item-0004 / WP-0002, in flight) defines a standing
three-layer loop (Backlog / Design & Review / Implementation) whose
handoffs are meant to run over `SendMessage` / `ListAgents` — cross-session
tools specific to this environment's Claude Code harness.

**Correction (2026-08-18, after Director push-back on the original claim
below):** a web check across current vendor documentation and coverage
shows every tool this template mirrors now ships some form of
subagent/parallel-agent orchestration as of 2026 — this was not true when
the original wording below was drafted and should not be repeated as
written:

- Cursor shipped Subagents in January 2026 (up to 10 parallel on paid
  plans) plus a local-to-cloud session handoff.
- OpenAI Codex CLI's subagents reached general availability March 14,
  2026 — one manager agent coordinating multiple specialized agents, up to
  6 parallel by default.
- GitHub Copilot CLI's `/fleet` and VS Code's "Multi-agent" (public
  preview) dispatch parallel subagents from an orchestrator; the Copilot
  desktop app runs parallel agent sessions, each in its own git worktree.
- xAI's Grok Build (beta, May 2026) runs up to 8 parallel sub-agents, each
  in its own worktree, and documents native `CLAUDE.md` support.

**What remains genuinely uncertain** (not resolved by the sources above,
which are third-party blog coverage, not primary vendor docs): all four
examples above read as *one orchestrator session fanning out child
subagents for a single task*, not necessarily *two independently-started,
long-running standing sessions that discover each other and exchange
messages at arbitrary times* — which is specifically what ADR 0016's
Design & Review <-> Implementation handoff model needs (the equivalent of
`SendMessage` + `ListAgents`, not just parallel task fan-out). Whether any
of these tools expose that peer-messaging primitive (versus only
parent-child fan-out) is unconfirmed and needs primary-source verification,
not blog summaries, before this item is planned.

**Direction decided (2026-08-18):** rather than treat this as fully open,
the Director decided the baseline Design & Review <-> Implementation
handoff should be the **portable pattern**: parent-child subagent
spawning, each child in its own dedicated git worktree/branch — which is
exactly what Cursor/Codex/Copilot/Grok Build all already support (see the
Correction above) — using each tool's own parent-child completion signal
for the routine "the child is done" notification. `SendMessage`/
`ListAgents` stay in the model, but scoped narrowly to the Director's
intervention channel (ADR 0016 Rule 4 — the Director reaching into an
already-running session at an arbitrary time), which is a Claude-Code
-specific capability the ADR already scopes narrowly and does not need to
be portable the same way the baseline handoff does. This significantly
narrows this item's remaining scope.

Work needed (narrowed):

- Confirm ADR 0016 and `cross-session-messaging.md` (LISS-0022, in
  progress under WP-0002) actually reflect parent-child-spawn-plus-worktree
  as the baseline once that work lands, rather than requiring `SendMessage`
  for the routine handoff.
- Determine which parts of ADR 0016's model are Claude-Code-specific
  (the Director's intervention channel via `SendMessage`) versus
  tool-agnostic (the three-layer concept itself: Backlog gate, Design &
  Review autonomy, parent-child Implementation execution in a dedicated
  worktree, non-blocking concurrency, the compliance boundary — all of
  which now look portable given the vendor research above).
- Decide a fallback for the intervention channel specifically, for tools
  without live cross-session messaging —
  most likely a **file-based handoff signal** (e.g. a status field or a
  small file under a new `docs/collaboration/handoffs/` directory) that any
  tool's agent can poll for at the start of a fresh session, consistent
  with this template's existing artifact-only-continuity model
  (`docs/collaboration/session-start-and-resume.md`) and with
  `cross-session-messaging.md`'s own rule that a message is a trigger, not
  the record — a file-based trigger already satisfies both roles and is
  portable across tools.
- Update the contract mirrors (`AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, `.grok/rules/*.md`,
  `.cursor/rules/*.mdc`) so a tool without `SendMessage` is not left
  describing a mechanism it cannot execute — likely: the three-layer
  *concept* mirrors everywhere, but the *live-session* handoff mechanism is
  scoped explicitly to environments where `SendMessage`/`ListAgents` (or an
  equivalent) are available, with the file-based fallback as the default
  for everything else.

## Why it might matter

Without this, adopting projects that use Cursor, Copilot, or a Codex-family
agent instead of (or alongside) Claude Code would have a contract file
describing a loop they cannot actually run, which is exactly the kind of
contract/tool mismatch ADR 0006 exists to prevent.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes
- Boundaries or non-goals:
  - Not a request to change ADR 0016 itself or WP-0002's current scope —
    ADR 0016 stays Claude-Code-oriented for now; this item is about
    portability afterward.
  - Not a request to build a new cross-tool messaging bridge — the fallback
    is expected to be file/artifact-based, not a new live-notification
    mechanism for other tools.

## Uncertainty

- [ ] Spec can be written now
- [x] Spike required first (options, feasibility, or quality unknown) —
      now narrowed to: (a) confirm each tool's parent-child subagent +
      worktree mechanics from primary vendor docs closely enough match
      what ADR 0016 assumes (dedicated worktree per child, a completion
      signal the parent can act on) to mirror the contract files without
      overclaiming; (b) decide the intervention-channel fallback (ADR 0016
      Rule 4) for tools without a `SendMessage`-equivalent — most likely a
      file/status-based signal a running session polls for, consistent
      with this template's existing artifact-only-continuity model.
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none yet
- Work plan (when promoted): `docs/archive/work-plans/WP-0004-multi-agent-tool-loop-portability.md` — confirmed via direct cross-reference; this item's own `Links` field was never updated when the work landed (see `docs/issues/LISS-0065-...md`'s own cross-reference table).
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: `docs/architecture/adr/0006-prompt-instruction-change-control.md`
  (existing, per-vendor grounds); `docs/architecture/adr/0016-*.md`
  (existing, depends on `SendMessage`/`ListAgents`)

## Promotion notes

- Date: 2026-08-18
- Decision: Promoted, in the Backlog-layer thread, after WP-0002/item-0004
  closed (ADR 0016's final wording, its baseline, now exists). Per ADR 0016
  Rule 2, this approval is the single design-phase gate — the Design &
  Review group proceeds autonomously from here: run the Uncertainty spike
  (primary-vendor-doc verification of whether Cursor/Codex/Copilot/Grok
  Build support peer cross-session messaging or only single-orchestrator
  fan-out) itself, then build the work plan, spec, and design agreement,
  without a further live dialogue turn with the Director for this item.
- Reason: Sequencing condition (ADR 0016 landed) is satisfied.
