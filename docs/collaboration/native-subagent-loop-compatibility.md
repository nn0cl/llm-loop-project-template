# Native subagent loop compatibility

This optional companion helps adopters evaluate native tools against the existing
loop. It adds no mandatory reading sequence or new approval authority. The
current contracts, accepted agreement and work plan remain authoritative;
ADR 0016/0017 describe the portable baseline and intervention fallback.
Use [agent-tool-conformance](../templates/agent-tool-conformance.md) to record a
bounded disposable fixture before claiming full-loop adoption.

## Status and scope

Assessment date: 2026-10-01. Candidate means documented support worth testing,
not a successful live run. **Inferred** means official documentation grounds a
capability; **Verified** requires recorded execution on the named surface and
version; **Unknown** means unavailable or insufficient evidence. Installed
versions and help output do not certify entitlement or behavior. Native spawn,
fresh context, isolated worktree and reliable continuation are distinct claims.

The research baseline observed Codex CLI 0.153.4, Grok Build 1.0.41 and Cursor
editor 3.20.21; Claude Code was absent from PATH. Other authenticated surfaces
were unavailable. Codex CLI help exposes `agents` and `queue --thread <THREAD>
--message <TEXT>`; that is discovery/message syntax evidence only, not proof of
idle wake or client-exit delivery. Desktop native children and installed CLI
are different surfaces. Versioned Codex releases [C6/C7/C8] describe CLI 0.156.0 and
0.159.x capabilities beyond the installed version. Their page date labels are
September 22 (0.156.0) and September 29 (0.159.0/0.159.1), 2026. C4 is navigation
only and may omit CLI release entries. Recheck versions before use.

No complete eight-stage live certification is issued here. A later partial
probe must name exactly the tested primitives and keep the other stages Unknown.

## Per-stage coverage matrix

N = native primitive candidate; A = repository artifacts plus auxiliary/manual
handling required; U = unconfirmed. X = unsupported by the named mechanism.
Every cell below has live status **Unknown** until its corresponding fixture
has recorded outputs. N is documentation-derived **Inferred**, never approval.
Tool-specific source keys below ground the primitives; R means existing repository
contracts (agreement, phase discipline, findings and Director close).

| Stage | Codex | Claude Code | Cursor | Grok Build | GitHub Copilot | Antigravity |
| --- | --- | --- | --- | --- | --- | --- |
| 1 Approved backlog intake | A/R | A/R | A/R | A/R | A/R | A/R |
| 2 Design dispatch | N+C1; A/R agreement | N+L1; A/R | N+U1; A/R | N+G1; A/R | N+H3; A/R | N+T1; A/R |
| 3 Isolated implementation | N+C2 opt-in | N+L1 opt-in | N+U1 opt-in | N+G2 opt-in | N+H1 fresh worktree; U fleet worker isolation | N+T1,T2 branch mode |
| 4 Tests/evidence/self-review | A/R commands | A/R commands | A/R commands | A/R commands | A/R commands | A/R commands |
| 5 Independent review | N+C1 fresh input; A allowlist | N+L1 ordinary child; A allowlist | N+U1 clean input; A allowlist | N+G1 fresh input; A allowlist | A+H1 fresh session; U fleet input | N+T1 fresh input; A allowlist |
| 6 Finding correction | N+C1 follow-up; A/R lifecycle | N+L1 resume; A/R | N+U1 dispatch; A/R | N+G1,G3 dispatch/resume; A/R | A+H1,H3 dispatch; A/R | N+T1 message; A/R |
| 7 Continuation/recovery | N+C1 active wait; U idle/exit wake | N+L1 background handback; U exit wake | N+U2 bounded hook; U exit wake | X+G4 passive-hook continuation; A+G3 manual resume | N+H2 bounded stop; U exit wake | N+T3 stop continuation; U exit wake |
| 8 Director close/lifecycle | A/R human | A/R human | A/R human | A/R human | A/R human | A/R human |

The per-cell A work cannot be inferred from N. Stage 7 includes tests with parent
turn ended, client open, client closed, and interrupted worker; record these
separately. A hook event alone is not a continuation guarantee.

## Common local setup and artifact envelope

Confirm existing account coverage before calls. Keep cloud/API, purchased overages,
new subscriptions, upgrades, schedules and hosted orchestration deferred unless a
later agreement and confirmed entitlement cover them. Model fallback and quota
exhaustion must be recorded. No platform subscription is presumed to cover an API.

In a disposable Git repository, record a clean base commit and branch before
dispatch. Use native worktree isolation explicitly where documented; defaults
can be shared, detached or based on a different ref. If the native surface cannot
select the required base, create a dedicated worktree with ordinary Git and open
that directory as a new local session. Example with adopter-selected values:

```sh
git status --short
git rev-parse HEAD
git worktree add -b codex/fixture-implementation /tmp/fixture-implementation <base-commit>
git -C /tmp/fixture-implementation rev-parse HEAD
git -C /tmp/fixture-implementation branch --show-current
```

Verify the child working directory, base SHA, branch and changed-file boundary.
Never rely on a prompt to turn a shared checkout into an isolated one. Keep every
worker's branch/worktree distinct; preserve changes before cleanup. Non-Git
folders need separate copied storage or a recorded manual limitation.

Provide the Implementer an envelope containing persona, agreement, issue/work
plan, operating path, phase, acceptance, base/worktree/branch, intervention gate,
allowed files, expected output paths and deterministic commands. A completion
must identify issue/phase, attempt ID, child ID, result, artifacts and command
output. Producer explanations are evidence claims requiring grounds.

For the Reviewer, start a **new context**, never a fork of the producer or its
parent history. Allowlist: current contract files, agreement, specifications,
work plan/issues/findings, relevant ADRs, target diff/files, recorded raw command
outputs, and concise artifact manifest with hashes/paths. Exclude chat transcripts,
forked history, hidden reasoning, producer rationale used as justification,
unrelated files and secrets. A native transcript path in an event is metadata;
it is not permission to send its content to the Reviewer. A fresh context that
can access shared transcripts still needs an explicit exclusion and input audit.
Give the Reviewer independent rerun access and a review-record output path.

## Local tool routes

These are bounded setup/dispatch/resume instructions, not installed configuration
or verified guarantees. Use the portable manual fallback when a documented field
or command is absent on the installed version. Do not guess replacement flags.

### Codex

Request a native child explicitly with the artifact envelope; select no inherited
conversation where the surface supports context selection. Use native follow-up
and wait for active-session handback [C1]. Select managed worktree mode explicitly
or open the prepared Git worktree [C2]. For review, dispatch another fresh child
with only the allowlist. Recover recorded child/session IDs before follow-up;
CLI help discovery/queue is a separate untested surface. Check installed help
and [C3/C4] rather than assuming desktop and CLI parity. A fork fails independence.

### Claude Code

Use `/agents` to create a project subagent, or a Markdown definition under
`.claude/agents/` with `name`, `description`, and `isolation: worktree` for the
Implementer. Explicitly request an ordinary child with the envelope [L1]. Do not
use a fork for review. Verify the base because native worktrees may start from
the default branch. Resume the recorded agent ID where supported; agent-type and
version restrictions apply. Experimental teams are optional and not this baseline;
resuming their parent does not restore in-process teammates [L2]. Background
completion and hook transcript paths [L3] require recorded observation, not trust.

### Cursor

Create a Markdown definition named `loop-implementer` under `.cursor/agents/` with YAML `name`, `description` and
`model: inherit`; invoke `/loop-implementer` with the envelope. Create a distinct
Reviewer definition and provide only allowlisted inputs [U1]. Choose local
worktree isolation explicitly or open the prepared worktree; shared checkout is
not sufficient. Use the native task result for foreground completion. Record the
background child ID/card before later follow-up; if resume is unavailable, recover
manually from artifacts. Optional `subagentStop` continuation uses documented
`followup_message` and a default five-continuation limit; errors/aborts and hook
failure policy need explicit recovery [U2]. Cloud VM adoption remains deferred.

### Grok Build

Request separate native children with artifact envelopes [G1]. Select worktree
mode with an explicit clean ref and record the resulting branch: detached or
uncommitted-content defaults must not contaminate the fixture [G2]. Use saved
session IDs for documented resume, not a history-inheriting fork [G3]. Passive
hooks ignore stdout and do not schedule a next task; only the documented blocking
hook can gate its applicable operation [G4]. After completion, have the active
parent inspect artifacts or manually reopen the recorded session. Do not invent
a `SubagentStop` continuation response. Existing Build entitlement is unconfirmed.

### GitHub Copilot

Use local CLI `/new worktree` for an empty session, verify its base/branch, then
supply the envelope. Use another empty session for Reviewer: `/fork worktree`
inherits context and is disallowed for independence [H1]. Use recorded exact
session IDs and documented resume controls; recover manually if unavailable.
Fleet/custom-agent coordination [H3/H4] is a candidate whose per-worker checkout
and Reviewer input isolation still require proof. Stop hooks can request bounded
continuation (at most eight consecutive blocks); the built-in general-purpose
agent omits subagent lifecycle events, so that event cannot be the only recovery
signal [H2]. Autopilot is optional, bounded and consumes credits [H5].

### Google Antigravity

Dispatch a fresh native child with workspace option `branch`, not `inherit` or
`share`, and the envelope [T1]. Verify the base/branch and Git project worktree
selection [T2]. Request a separate fresh Reviewer with the allowlist; do not send
shared transcripts. Record known child IDs, then use native messaging/idle-child
wake only for those known children. If discovery/resume is unavailable, reopen
from the artifact manifest manually. Optional Stop continuation [T3] does not
establish parent wake after client exit. Confirm plan/quota coverage [T4] first.

## Completion handling and graceful recovery

Record one ledger entry per work-plan/issue/phase/attempt ID, with child/session
ID, event ID (or explicit unavailable value), output paths and completed base SHA.
Before dispatch, read the intervention gate and recover any existing worker.
Before consuming completion, verify matching identity, artifacts, commands and
phase preconditions. Record the consumed event/attempt and next action durably;
a repeated delivery must not dispatch twice. Stale events cannot advance a newer
attempt. Missing IDs or ambiguous state require manual inspection, not blind spawn.

On interruption, failed permission/quotas/hooks, missing completion or client
shutdown, preserve logs and partial files; mark the attempt interrupted/failed.
Inspect native active-session state if available, then recover from issue/plan,
status file and worktree. Resume the same recorded worker only when supported and
its identity is confirmed. Otherwise record that it is stopped/unavailable before
creating one replacement attempt. Rerun incomplete verification. Never turn
missing output into pass or skip a phase. This is a manual/documented protocol,
not a newly shipped idempotent event consumer or scheduler.

Exercise a deliberate Reviewer rejection in the disposable fixture. Record a
`Type: review-finding` issue, correction and raw re-verification; get separate
Reviewer confirmation. Contract-file fixes always need independent review.
After all findings are closed (or grounded Arbiter `wont_do`), present the approved
result to the Director. Only the Director's recorded next direction/end closes
the work plan; then synchronize backlog disposition and linked records.

## Official source register

Retrieved 2026-10-01; URLs are capability grounds, not live results. Revisit them
when the surface/version changes; do not copy release facts to another surface.

- C1: https://learn.chatgpt.com/docs/agent-configuration/subagents
- C2: https://learn.chatgpt.com/docs/environments/git-worktrees
- C3: https://learn.chatgpt.com/docs/reference/troubleshooting
- C4 (navigation only): https://learn.chatgpt.com/docs/changelog
- C6 (0.156.0 release): https://github.com/openai/codex/releases/tag/rust-v0.156.0
- C7 (0.159.0 release): https://github.com/openai/codex/releases/tag/rust-v0.159.0
- C8 (0.159.1 release): https://github.com/openai/codex/releases/tag/rust-v0.159.1
- C5 (deferred API surface): https://developers.openai.com/api/docs/guides/responses-multi-agent
- L1: https://code.claude.com/docs/en/sub-agents
- L2: https://code.claude.com/docs/en/agent-teams
- L3: https://code.claude.com/docs/en/hooks
- L4: https://code.claude.com/docs/en/costs
- U1: https://cursor.com/docs/subagents
- U2: https://cursor.com/docs/hooks
- U3: https://cursor.com/docs/models-and-pricing
- G1: https://docs.x.ai/build/features/subagents
- G2: https://docs.x.ai/build/features/worktrees
- G3: https://docs.x.ai/build/features/sessions
- G4: https://docs.x.ai/build/features/hooks
- G5: https://docs.x.ai/console/billing
- H1: https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference
- H2: https://docs.github.com/en/copilot/reference/hooks-reference
- H3: https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/fleet-mode
- H4: https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/custom-agents
- H5: https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot
- T1: https://www.antigravity.google/docs/subagents/
- T2: https://www.antigravity.google/docs/projects/
- T3: https://www.antigravity.google/docs/hooks/
- T4: https://www.antigravity.google/docs/plans/
