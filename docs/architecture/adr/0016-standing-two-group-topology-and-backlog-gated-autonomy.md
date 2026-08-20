# ADR 0016: Standing Two-Group Topology and Backlog-Gated Autonomy

## Status

Accepted. Covered by
`docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
(`DA-2026-08-18-01`). Supersedes ADR 0001's Decision, point 2 ("Detailed
planning" as a live, per-work-plan Planner-Director dialogue turn) and, in
consequence, ADR 0014's Decision, clause 1's restatement of that requirement
("Starting a new work plan means reaching a new design agreement — the
Director's initial-direction dialogue with the Planner, as under ADR 0001,
unchanged"). Also supersedes ADR 0014's Decision, clause 5's blocking rule
("the next work plan does not start without [close]") as it applies across
*concurrently in-flight* work plans. See "Decision", rules 2 and 3, and
"Supersession, precisely" below for the exact scope of each. Forward-pointer
notes are added to ADR 0001's and ADR 0014's own Status sections, mirroring
how ADR 0001's Status section already points forward to ADR 0014.

`Accepted` status requires a design agreement with the Director covering the
decision. That agreement is `DA-2026-08-18-01`, reached through the
multi-turn dialogue quoted in its own Direction section, including the
three-layer clarification quoted in "Context" below. Follow-up issues:
LISS-0020 through LISS-0026 (`docs/archive/work-plans/WP-0002-two-group-send-message-loop.md`).
Rule 7 (the check-and-spawn wake protocol) is covered by a
separate, later design agreement, `DA-2026-08-20-06`, following
`docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md`'s own
promotion and the required-first spike
(`docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`);
Rules 1-6 remain covered by `DA-2026-08-18-01` as before.

## Context

ADR 0001 and ADR 0014 were written assuming one undifferentiated session did
every persona's work across the whole loop — Director dialogue, planning,
specification, implementation, and review all happened in whatever session
the human was talking to at the time, with the Reviewer's context separation
achieved by starting a fresh conversation for that one pass. That assumption
was reasonable before cross-session tools existed: there was no way for two
long-running AI sessions to hand work to each other without a human relaying
messages between them.

This repository's environment now provides `SendMessage` and `ListAgents`
cross-session tools. The Director's direction, recorded across several turns
in `DA-2026-08-18-01`, is to use them to split the closed execution loop into
two **standing** AI session groups — started once, not reconstituted per
work plan — connected by those tools, so that:

- the Design & Review group (Planner, Specifier, Reviewer, Arbiter) can pull
  an approved backlog item and autonomously produce its work plan,
  specifications, and design-agreement record, without a further live
  per-work-plan Director dialogue turn;
- the Implementation group (Implementer) can execute an agreed work plan in
  its own dedicated `git worktree`/branch, self-reviewing each issue, and
  hand the result back for review;
- multiple work plans can be in flight across both groups at once, so that
  one work plan awaiting the Director's closing checkpoint does not stall
  either group's other work;
- the Director can intervene directly in either group's session at any time,
  without that intervention halting the group's other concurrent work.

**The three-layer correction.** After the Director's initial direction
produced a draft work plan (`WP-0002`), design agreement (`DA-2026-08-18-01`),
and this ADR's own issue (`LISS-0019`) — drafted in the Backlog-layer thread
itself, as a bootstrap exception, because no separate Design & Review session
existed yet to do that work independently — the Director added three further
clarifications in that same thread, quoted verbatim because they are the
direct authority for this ADR's topology section:

1. "階層としては3層かも？(このスレッド)バックログ(backlog) - 設計レビュー
   (design) - 実装(implementation)" — the intended topology is three layers:
   Backlog (this thread), Design & Review, Implementation.
2. "なぜなら今回の実装以外の事も検討したい。バックログにタスクを積むこと
   になるのではと思っている。" — the Backlog thread must stay free to keep
   capturing other, unrelated items over time, not be consumed as the Design
   & Review session for one work plan's duration.
3. "設計・レビューはサブエージェントで別スレッドで運用する想定です。ここは
   バックログ用スレッドにしたい。" — Design & Review runs as a sub-agent in
   its own separate standing thread; the original thread is Backlog-only.

This does not contradict `DA-2026-08-18-01`'s "two groups" language — that
agreement's "two groups" already, and still, refers only to the two standing
*AI session groups inside the closed execution loop* (Design & Review,
Implementation). It never claimed the Backlog thread was one of those two
groups, only that this specific founding work plan happened to draft its own
early artifacts from the Backlog thread before a separate Design & Review
session existed (`docs/backlog/item-0004-two-group-send-message-loop.md`,
"Promotion notes"). What was missing was an explicit statement that Backlog
is its own layer, standing outside both groups, with no persona of its own —
this ADR supplies that statement. The file name and title of this ADR keep
"two-group," deliberately: the decision below still names exactly two
standing *session groups with personas*; Backlog is a third layer by design,
not a third group, and Rule 1 states that distinction explicitly so a future
reader cannot mistake "two-group topology" for "the whole model has only two
layers."

## Dependency Adoption Evidence

Not applicable. This decision selects no library, framework package,
provider SDK, datastore client, build tool, or test helper. `SendMessage` and
`ListAgents` are existing cross-session capabilities of the agent harness
already available in this environment; adopting them here is a process
decision about how personas are distributed across sessions, not a
dependency adoption.

## Decision

### Rule 1 — Three layers; personas map to exactly two of them

There are three layers. Only two of them are standing AI session groups with
assigned personas; the third has no persona of its own.

| Layer | What it is | Personas operating in it |
| --- | --- | --- |
| Backlog | The Director-facing thread where direction is captured and backlog items (`docs/backlog/item-NNNN-*.md`) are approved. Not tied to any single work plan; the Director keeps using it for other, unrelated backlog intake over time. | None. This is the Director's own thread, not an AI persona's operating layer. |
| Design & Review group | A standing sub-agent session (or small session group), started once and kept alive, not reconstituted per work plan. | Planner, Specifier, Reviewer, Arbiter. |
| Implementation group | A standing sub-agent session, started once and kept alive, working in a dedicated `git worktree` and branch per work plan. | Implementer. |

A session in the Design & Review group or the Implementation group is a
"group" under this ADR only if it carries persona responsibilities inside
the closed execution loop. The Backlog thread is never a "group" under this
ADR, regardless of what work happens inside it — a bootstrap exception where
Design & Review's own drafting work temporarily happened in the Backlog
thread does not make the Backlog thread the Design & Review group; it is
recorded as an exception in the backlog item that authorized it and does not
recur once a separate Design & Review session is standing.

### Rule 2 — Backlog-item-level design gate

Director approval is granted at the `docs/backlog/item-NNNN-*.md` level, in
the Backlog layer. Once a backlog item's status is `promoted` (per
`docs/backlog/README.md`), the Design & Review group may autonomously:

- perform requirement organization, research (including spikes under
  `docs/spike/`), and method/approach study;
- produce the work plan, acceptance specifications, and the design-agreement
  record for that item;

without a further live, turn-by-turn Planner-Director dialogue for that work
plan. The backlog-item approval, plus the Design & Review group's own
executability statement recorded in the resulting design-agreement document,
together satisfy both halves of "Reaching agreement" in
`docs/collaboration/design-agreement.md` — Director agreement and AI
executability — for the work plan that backlog item authorizes. A work plan
that goes beyond what the backlog item states is not covered by this rule and
requires a reopening request, per the existing "Reopening the agreement"
rules; backlog-item approval is explicit and scoped, not blanket delegation.

This supersedes ADR 0001's Decision, point 2 ("Detailed planning. The
Director and the Planner persona produce the plan through dialogue. This is
a conversation, not a review of a finished artifact") to the extent it
required that conversation to occur live, turn by turn, for every work plan;
and ADR 0014's Decision, clause 1's restatement of the same requirement
("Starting a new work plan means reaching a new design agreement — the
Director's initial-direction dialogue with the Planner, as under ADR 0001,
unchanged"). The dialogue that produces the Director's agreement may now
happen once, at backlog-item approval, in the Backlog layer; downstream
planning is delegated to the Design & Review group.

### Rule 3 — Non-blocking concurrency across work plans

Multiple work plans may be in flight concurrently, across both groups. A
work plan awaiting the Director's closing checkpoint (ADR 0014) does not
block:

- the Design & Review group from continuing design work on the next
  approved backlog item; nor
- the Implementation group from continuing execution on another
  already-agreed work plan.

This supersedes ADR 0014's Decision, clause 5's blocking statement — "This is
a required checkpoint, not optional reading: the next work plan does not
start without it" — specifically as that statement applies *across
concurrently in-flight work plans*. It does not change what the checkpoint
requires for the one work plan it closes: the Director still must read the
Reviewer-approved result and state the next direction (or end the
engagement) in the same combined action before *that* work plan's own next
direction begins. What changes is only that this checkpoint, for one work
plan, no longer serializes the start of unrelated work on other work plans.

### Rule 4 — Director intervention channel

At any time, the Director may send a chat message directly into either
group's standing session. Receipt of such a message converts the specific
in-flight item being worked at that moment — not the group's other
concurrent work — into a human-approval-gated mode:

- the group continues its development-loop and review work on that item;
- each subsequent step on that item requires the Director's explicit
  approval before proceeding;
- this gated mode persists until the Director gives a resolving instruction,
  which either restores autonomous progress on that item or redirects it;
- other concurrently in-flight work plans or backlog items, in either group,
  are unaffected and continue under the standing backlog-level
  authorization.

Intervention is a per-item mode change, not a session halt. A record of the
gate and its resolution is kept in the affected issue's Work Notes or the
work plan's own record (per `docs/collaboration/cross-session-messaging.md`,
LISS-0022), not only in chat history, per Invariant 1.

### Rule 5 — Standing compliance-boundary constraint

Autonomous progress under this ADR — in either group, on any item not
currently under Rule 4's gated mode — remains bounded by the project's
operational rules (this repository's own contract documents) and applicable
law. This is a standing constraint that applies continuously to every item
in flight, not a checkbox verified once per item. A case that would require
exceeding either boundary is a reopening request, not a judgment call either
group resolves on its own.

### Rule 6 — What is unchanged

None of the following are altered by this ADR:

- The three invariants (every decision produces a document; every executed
  fact leaves evidence; every claim states its grounds).
- The Reviewer's three constraints (context separation, deterministic
  precondition, falsification burden) and the requirement that the
  work-plan-level Reviewer pass happens once, after Preflight, in a context
  separate from the one that produced the work.
- The Implementer's self-review requirements inside a work plan
  (deterministic precondition, falsification burden; context separation
  waived only at that layer, per ADR 0014).
- ADR 0006's contract-file governance: a separate-context Reviewer, a stated
  reason, and a trace under `docs/collaboration/traces/` are still required
  for every agent-operating-contract-file change, regardless of which group
  produces it. No Director instruction waives this rule, per
  `docs/collaboration/prompt-instruction-change-control.md`.
- The two human gates in kind — design agreement and work-plan close still
  exist and are still mutual and explicit. Only their cadence (batched at
  the backlog-item level rather than live per-work-plan dialogue) and their
  blocking behavior across concurrently in-flight work plans change, per
  Rules 2 and 3.

### Rule 7 — Check-and-spawn wake protocol

Neither standing session is expected to revive itself from full dormancy
with no external trigger — no primitive in this environment provides
that (confirmed by direct investigation,
`docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`).
Instead, responsibility for waking the next layer moves to the event that
produces new approved work:

1. **Backlog approval -> Design & Review.** When the Backlog thread
   approves a backlog item (`docs/backlog/item-NNNN-*.md` moves to
   `Status: promoted`), the Backlog thread checks, via `ListAgents`,
   whether a Design & Review session is already running. If one is
   found, it sends the new item to that session via `SendMessage`. If
   none is found, it spawns one (Agent-tool, worktree-isolated, per the
   existing convention this repository already uses for Implementation-
   group dispatch) with the approved item as its task.
2. **Work-plan approval -> Implementation.** When the Design & Review
   group has a work plan ready for implementation (a freshly built plan
   from the Planner, or a Reviewer-approved plan awaiting execution), the
   Design & Review group itself checks, via `ListAgents`, whether an
   Implementation session is already running. If one is found, it sends
   the work plan to that session via `SendMessage`. If none is found, it
   spawns one.
3. **Queue continuation before going idle.** Inside each standing loop
   (Design & Review, Implementation), before going idle after finishing a
   task, the loop checks its own queue for other already-approved-but-
   unstarted work — promoted backlog items not yet picked up, for Design
   & Review; Reviewer-approved work plans not yet implemented, for
   Implementation — and proceeds directly to the next one if any exists.
   A loop goes idle only when its own queue is genuinely empty.
4. **Resume before duplicate-spawn.** Before any party spawns a new
   session for a role (Backlog thread spawning Design & Review, Design &
   Review spawning Implementation, or any session recovering after an
   error), it first checks whether a session already exists for that
   role — including one that has just failed or errored, since its git
   worktree and branch survive the failure and may hold uncommitted or
   unpushed work. If a prior worktree/branch for that role's in-flight
   task exists and has not been merged or cleaned up, the spawning party
   resumes it (`SendMessage` to its `agentId` once reachable, or a new
   session re-pointed at the same worktree/branch) rather than spawning a
   fresh session that would duplicate the worktree or strand the earlier
   content.

This closes the gap
`docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md` named: ADR
0016 and `docs/collaboration/cross-session-messaging.md` previously
described the two groups as "standing" and "autonomous" without
specifying a concrete wake-up mechanism. It does not claim full
self-revival from dormancy is achieved — no primitive in this
environment delivers that (per the spike). The one residual case is
brand-new work arriving while both loops are fully idle and no session
exists to check `ListAgents` on either's behalf; that case still needs
the Backlog thread (or whatever originates the first approval) to
perform rule 1's own check-and-spawn, which is the natural entry point,
not a gap this protocol fails to close.

## Supersession, precisely

| Superseded clause | What it required | What replaces it |
| --- | --- | --- |
| ADR 0001, Decision, point 2 ("Detailed planning") | A live, turn-by-turn Planner-Director dialogue producing the plan for every work plan. | Rule 2: the dialogue happens once, at backlog-item approval; the Design & Review group plans autonomously downstream, within the backlog item's stated scope. |
| ADR 0014, Decision, clause 1 (the plan-per-agreement restatement of ADR 0001 point 2) | "The Director's initial-direction dialogue with the Planner, as under ADR 0001, unchanged" — i.e., live per work plan. | Same as above; clause 1's "one design agreement per work plan" boundary itself is unchanged — only how the underlying dialogue happens. |
| ADR 0014, Decision, clause 5 (blocking clause) | "The next work plan does not start without it [the close]." | Rule 3: does not block *other, concurrently in-flight* work plans. The one work plan being closed still requires the combined Director action clause 5 describes. |

Not superseded, and cited here to foreclose a misreading: ADR 0014's Decision
clause 6 ("no per-phase and no per-issue human gate... exactly two human
touchpoints per work-plan cycle") is unaffected — this ADR does not add a
third per-work-plan human touchpoint; Rule 4's intervention channel is an
optional, Director-initiated exception, not a standing third gate.

## Consequences

Positive:

- The Backlog-layer thread stays available for the Director to keep
  capturing unrelated backlog items, instead of being consumed as the
  standing Design & Review session for the duration of one work plan — the
  problem this ADR exists to fix, per the Director's second clarification
  quoted in Context.
- Throughput is no longer serialized by one work plan's closing checkpoint;
  both groups can make progress on other approved work while one plan
  awaits Director close.
- The Director's intervention channel gives a way to pull a specific
  in-flight item back under per-step approval without needing to halt
  either standing session entirely.
- The layer/group distinction (Rule 1) gives a later reader — human or
  agent — a single place to check which layer a given session belongs to,
  instead of inferring it from how a particular founding work plan happened
  to be bootstrapped.

Negative:

- Removing the live per-work-plan Planner-Director dialogue (Rule 2) means a
  backlog item that is under-specified at approval time now produces a work
  plan with more room for the Design & Review group's own judgment calls
  before the Director sees it again — the design agreement's Deferred
  Questions section is the intended pressure valve, but its effectiveness
  depends on the Design & Review group actually using it rather than
  guessing past a gap.
- Non-blocking concurrency (Rule 3) means more than one work plan's state
  must be tracked at once; a reader recovering session state per
  `docs/collaboration/session-start-and-resume.md` now needs to check which
  of several concurrently in-flight work plans a given artifact belongs to,
  not just whether "the" work plan is open.
- The per-item gated mode (Rule 4) is new and has no prior operational
  precedent in this repository. Its precise behavior in practice — how a
  group resumes autonomous progress cleanly after a resolving instruction —
  is likely to need a follow-up once it is exercised (see
  `DA-2026-08-18-01`'s Deferred Questions).
- A three-layer model with two standing sessions plus a Backlog thread is
  more moving parts to keep consistent than the single-session model ADR
  0001 and ADR 0014 assumed; `docs/collaboration/cross-session-messaging.md`
  (LISS-0022) carries the burden of keeping the handoffs between them
  documented rather than only chat-transcript-based.

## Enforcement

Code review should reject:

- a design agreement produced without a preceding `promoted` backlog item,
  or one that covers scope the backlog item does not state, with no
  reopening request recorded.
- a work plan reported blocked from starting solely because another,
  unrelated work plan has not yet closed.
- an intervention (Rule 4) recorded as halting a group's other concurrent
  work, rather than gating only the specific in-flight item.
- autonomous progress documented anywhere as unconstrained by the project's
  operational rules or applicable law (Rule 5).
- the Backlog layer treated as if it were the Design & Review group — for
  example, a work plan's planning artifacts produced in the Backlog thread
  on an ongoing basis rather than as the one-time bootstrap exception this
  ADR records.
- a contract-file change (per `docs/collaboration/prompt-instruction-change-control.md`)
  approved by self-review, or by either group acting alone without a
  separate-context Reviewer, regardless of which group produced it.
- a `SendMessage` chat transcript treated as the record of a decision with
  no corresponding file, contradicting Invariant 1.
- a spawning party creating a duplicate session/worktree for a role
  without first checking, via `ListAgents`, whether one already exists
  (Rule 7) — including a role recovering from a session that just failed
  or errored, whose worktree/branch may hold undiscovered work.
- a standing loop going idle while its own queue still has
  already-approved-but-unstarted work it did not check for (Rule 7,
  point 3).
