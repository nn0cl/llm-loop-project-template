# AI Tool Support Status

This document reports, per AI coding tool, how well this repository's
agent collaboration model — personas
(`docs/collaboration/personas.md`), phase discipline, ADR 0016's standing
two-group topology, ADR 0017's portable baseline handoff and file-based
intervention fallback, and ADR 0006's mirrored instruction files — is
actually supported today. It is a status report, not a design document:
it states what each tool does and does not support, with a source for
every claim, and points at ADR 0017 and
`docs/collaboration/prompt-instruction-change-control.md` for the rules
themselves.

Full research, sources, and the raw comparison table this report
summarizes: `docs/spike/case-0004-ai-tool-support-status-survey/case.md`.

**Limitation stated once, applying to every tool below except Claude
Code**: every finding is documentation-based. This report was produced
from a Claude Code session, which has no way to run Codex, Cursor, Grok
Build, or Antigravity live to confirm behavior directly — the same
limitation this repository's existing `.cursor/`/`.grok/` mirror files
were already produced under. Where a primary source is silent on a
question, that is stated as "not documented," not filled in by inference.

## Claude Code

The reference implementation this whole contract is written against.

- **Instruction file**: `CLAUDE.md`, native.
- **Subagent model**: parent-child fan-out, with per-child `git worktree`
  isolation as this repository's own established convention (ADR
  0016/0017).
- **Peer-messaging**: `SendMessage`/`ListAgents` — a standing, arbitrary-
  time, peer-to-peer discovery-and-messaging primitive between
  independently-started sessions. This is the one capability ADR 0017
  found no equivalent for in any other tool surveyed.
- **Mirror file currency**: N/A — this is the canonical model, not a
  mirror of anything else.

## Codex CLI

- **Instruction file**: `AGENTS.md`, native (the same file this
  repository already maintains as its cross-tool canonical source).
- **Subagent model**: parent-child fan-out only. Codex "handles
  orchestration across agents, including spawning new subagents, routing
  follow-up instructions, waiting for results, and closing agent
  threads... Codex waits until all requested results are available, then
  returns a consolidated response" (`learn.chatgpt.com/docs/agent-configuration/subagents`,
  re-fetched 2026-08-20 — matches ADR 0017's own 2026-08-18 finding
  exactly). Worktree-isolation behavior is not documented on this page,
  the same gap ADR 0017 already noted.
- **Peer-messaging**: none documented.
- **Mirror file currency**: no dedicated mirror needed — `AGENTS.md` is
  Codex's own native convention.

## Cursor

- **Instruction file**: `AGENTS.md` (native, read in Chat/Composer/Agent
  modes since Cursor 0.48) **and** `.cursor/rules/*.mdc` — Cursor "reads
  both and merges their context" (per `cursor.com/docs/rules` and related
  official guidance, confirmed 2026-08-20). Cursor's CLI additionally
  reads `CLAUDE.md` directly at the project root (redundant with
  `AGENTS.md`, since `CLAUDE.md` is a literal full mirror of it, but not
  previously documented in this repository).
- **Subagent model**: agents run in isolated git worktrees, **opt-in**
  per agent (via the Agents Window, or configured through
  `.cursor/worktrees.json`) — "When you start or move an agent into a
  worktree from the Agents Window, Cursor creates a separate checkout for
  that agent" (`cursor.com/docs/configuration/worktrees`, a primary
  source fetched for the first time in this survey; ADR 0017 previously
  had only secondary/blog sources for Cursor).
- **Peer-messaging**: none documented.
- **Mirror file currency**: `.cursor/rules/*.mdc` — **confirmed current**.
  `scripts/check-contract-consistency.py`'s own mirror-parity check
  (deterministic, already part of this repository's CI) passes clean
  against the file as it exists today, and the underlying mechanism
  description in `docs/collaboration/prompt-instruction-change-control.md`'s
  "Per-Agent-Tool Rule Applicability Registry" (Union: complement +
  native auto-apply) matches this survey's own fresh primary-source
  finding exactly. No content update needed.

## Grok Build

- **Instruction file**: `.grok/rules/*.md` (this repository's own
  mirror). Grok Build's own native project-instruction-file convention
  was not independently re-derived beyond confirming the existing
  mirror's continued checker-parity pass in this round.
- **Subagent model**: parent-child fan-out only, with a **hard limit of
  one level of nesting** — "Only the top-level session spawns subagents.
  A subagent cannot spawn its own subagents: the maximum nesting depth is
  one" (`github.com/xai-org/grok-build/.../16-subagents.md`, re-fetched
  2026-08-20 — word-for-word match to ADR 0017's own 2026-08-18 quote).
  Worktree isolation is **opt-in** per call (`isolation: worktree`), not
  automatic — confirmed against the primary source directly, overriding a
  secondary blog source found during this survey that incorrectly claimed
  worktree isolation is now a default.
- **Peer-messaging**: none documented.
- **Mirror file currency**: `.grok/rules/*.md` — **confirmed current**
  (same checker-parity evidence as Cursor, above). No content update
  needed.

## Antigravity (Google)

New to this repository — no prior coverage, no existing mirror file.

- **Instruction file**: `AGENTS.md`, native — "you can mount files like
  `AGENTS.md` for instructions and skills under `.agents/skills/`
  directly into the sandbox" (`ai.google.dev/gemini-api/docs/antigravity-agent`,
  a Google-official domain, fetched 2026-08-20). No alternate top-level
  file name (e.g. `ANTIGRAVITY.md`) was found. Same convention as Codex —
  it reads the file this repository already maintains natively.
- **Subagent model**: parent-child fan-out, but with a materially deeper
  nesting allowance than any other tool surveyed — "a maximum nesting
  depth of 10 levels... is strictly enforced" (`antigravity.google/docs/subagents/`,
  fetched 2026-08-20). Worktree isolation is opt-in, one of three
  explicit modes per subagent: `inherit` (shared workspace), `branch`
  (isolated git worktree — the closest analog to this repository's own
  `isolation: worktree` convention), or `share` (shared directory
  storage). On completion, a subagent "sent a result message to its
  parent agent, and paused execution" — the same parent-child completion
  shape every other tool surveyed uses.
- **Peer-messaging**: **partial, and reported precisely rather than
  overclaimed.** Antigravity's own documentation states "Agents can
  communicate with parent agents, subagents, or **peer agents whose ID is
  known**" — the one finding among all five tools that names something
  beyond pure parent-child fan-out. However, this survey found **no
  primary-source confirmation of a `ListAgents`-equivalent discovery
  mechanism** for independently-started, unrelated standing sessions. The
  documented `/agents` panel (`antigravity.google/docs/cli/commands/agents/`)
  lists a session's own spawned subagent threads plus static, available
  role/type definitions — not a general registry of arbitrary live
  sessions. Antigravity also documents an A2A (Agent2Agent) protocol, but
  that is a cross-vendor, open, HTTP/SSE/JSON-RPC standard aimed at
  connecting to agents "deployed in external systems" (its own canonical
  example: a purchasing-concierge agent calling a remote seller agent) —
  a materially different use case from two local CLI sessions on one
  machine discovering each other. **Conclusion**: closer to
  `SendMessage`/`ListAgents` than Codex, Cursor, or Grok Build, but not
  confirmed equivalent — genuinely open, not resolved by guessing.
- **Mirror file currency**: **no dedicated mirror file exists, and none
  is needed** — Antigravity reads `AGENTS.md` natively, the same file
  this repository already maintains as its cross-tool canonical source,
  the same situation as Codex. The concrete update this survey's own
  findings support is adding Antigravity to
  `docs/collaboration/prompt-instruction-change-control.md`'s "Agent
  Operating Contract Files" list and "Per-Agent-Tool Rule Applicability
  Registry" as a `Canonical source` reader (alongside `AGENTS.md`
  itself), stating this explicitly rather than leaving Antigravity's
  status implicit.

## Summary table

| Tool | Instruction file | Subagent nesting | Worktree isolation | Peer-messaging | Mirror status |
| --- | --- | --- | --- | --- | --- |
| Claude Code | `CLAUDE.md` | parent-child (this repo's own model) | native, per-child | `SendMessage`/`ListAgents` | N/A (reference) |
| Codex CLI | `AGENTS.md` | parent-child only | not documented | none | no dedicated mirror needed |
| Cursor | `AGENTS.md` + `.cursor/rules/*.mdc` (+ `CLAUDE.md`) | not documented this round | opt-in | none | current, checker-verified |
| Grok Build | `.grok/rules/*.md` | max depth 1 | opt-in | none | current, checker-verified |
| Antigravity | `AGENTS.md` | max depth 10 | opt-in (3 modes) | partial, not confirmed equivalent | no dedicated mirror needed; registry entry added |

## Related documents

- `docs/spike/case-0004-ai-tool-support-status-survey/case.md` — full
  research log, every source URL, and the open risks this report
  inherits.
- `docs/architecture/adr/0017-portable-three-layer-loop-and-file-based-intervention-fallback.md`
  — the governing rules this report's findings confirm remain accurate
  for Codex, Cursor, and Grok Build.
- `docs/collaboration/prompt-instruction-change-control.md` — the
  mirror-file list and Per-Agent-Tool Rule Applicability Registry this
  report's own findings update (Antigravity added).
- `docs/collaboration/adoption-guide.md` — the adoption context this
  status report exists to keep accurate for a team choosing a tool other
  than Claude Code.
