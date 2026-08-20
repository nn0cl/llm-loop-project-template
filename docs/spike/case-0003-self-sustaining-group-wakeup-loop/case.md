# Spike Case: case-0003-self-sustaining-group-wakeup-loop

## Metadata

- Case ID: case-0003
- Title: What wake-up/self-scheduling primitives are actually available to
  a spawned sub-agent session in this environment
- Status: closed
- Created: 2026-08-20
- Closed: 2026-08-20
- Owner/agent: Design & Review group (Planner), standing session — this
  very session, investigating its own actual capabilities directly rather
  than delegating the investigation
- Related work plan: none yet — this spike's own Next action opens a
  human-decision issue, not a work plan (see Next action)
- Related local issue (LISS): LISS-0062 (human-decision issue this spike
  opens, see Next action)
- Related backlog item:
  `docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md`
- Supersedes case: none
- Superseded by case: none

## Question

Does a spawned sub-agent session (a Design & Review or Implementation
group standing session) in this environment have access to any primitive
that lets it go dormant and later resume — or spawn equivalent follow-up
work — without an external party (the Backlog thread, a Director message,
or another session's own `SendMessage`) having to notice and explicitly
re-invoke it?

## Why a spike (not immediate implementation)

`docs/backlog/item-0020-...md`'s own Known Constraints are explicit: "Do
not assume a literal infinite-polling loop is technically available to a
spawned sub-agent session in this environment — that needs to be
investigated, not presumed." This session (the Design & Review group) is
itself exactly the kind of spawned sub-agent session in question, so this
spike investigates its own actual, directly-observed tool surface and
constraints, rather than reasoning abstractly about what "should" exist.
The item also names its own fallback if true self-sustaining polling is
not available: document the Backlog-thread-relay pattern honestly instead
of overstating autonomy that does not exist.

## Constraints

- Must remain free of mandatory paid spend unless justified below: yes —
  every candidate below is either already-available tooling in this
  environment or a documentation-only change; no new paid service is
  considered.
- Architecture / port boundaries to respect: none — no application
  architecture is touched; this is an investigation into this
  environment's own agent-orchestration primitives.
- Out of scope for this spike:
  - Actually configuring a harness-level hook, cron task, or any
    persistent automation as production behavior — this spike identifies
    and evaluates candidates; adopting one is a separate design/ADR
    decision (see Next action).
  - Re-litigating ADR 0016 Rule 2's own judgment autonomy (Design &
    Review not needing live Director dialogue once a backlog item is
    promoted) — already working as intended, per the item's own boundary
    note; this spike is scoped to the wake-up mechanism only.
  - Testing whether the Implementation group (a different standing
    session) has an *identical* tool surface to this Design & Review
    session — not directly testable from inside this session; assumed
    equivalent per ADR 0016's own "both are standing sessions in the same
    environment" framing, and flagged as an assumption below, not
    confirmed by direct observation of an Implementation-group session's
    own tool list.

## Candidates

Not a vendor/library selection — the "candidates" are four possible
wake-up mechanisms, each evaluated against what this session actually
observed or could actually invoke.

| ID | Option | License / cost model | Source (URL or doc) | Notes |
| --- | --- | --- | --- | --- |
| A | Rely only on background-agent completion notifications (today's de facto mechanism) | free — built into the Agent tool | This session's own tool descriptions (`Agent` tool: "you will be automatically notified when it completes") | Real and already working, but only while at least one dispatched background agent is still in flight; goes silent once the dispatch queue is empty — exactly this session's own dozens of observed idle periods this whole thread |
| B | `mcp__scheduled-tasks__*` / the "schedule" skill — cron or one-time fresh-session tasks | free — built into this environment | Tool description read directly in this session (see Evidence); empirically invoked (`list_scheduled_tasks`) from inside this spawned session | Reachable and callable from a spawned sub-agent context (confirmed by direct call, not assumed); each firing starts a **new, stateless session** ("Each run starts fresh with no memory of this conversation"), not a resume of the session that scheduled it |
| C | A harness-level hook (e.g., a `Stop` event in `.claude/settings.json`) that shells out to resume/notify on session idle | free — built into the harness, if it exists as described | Inferred only from two of this session's own available-skill descriptions (`update-config`, `keybindings-help`) referencing "when claude stops show X" and hook-based hooks in `settings.json` — **not independently tested or confirmed reachable from inside this spawned worktree-isolated session** | Plausible building block, but unverified in this spike; would require `settings.json` configuration outside a spawned sub-agent's ordinary file-editing scope, and is a system/automation-configuration change, not something a running conversational turn can adopt on its own |
| D | A literal in-turn blocking loop (`sleep` in Bash, or `Monitor` with `persistent: true`) that keeps this exact session's turn open indefinitely, polling for new backlog items | free | This session's own tool descriptions, read directly (see Evidence) | Explicitly ruled out by the tools' own documented constraints, not by assumption — see Research log |

## Evaluation criteria

| Criterion | Why it matters | How measured |
| --- | --- | --- |
| Actually reachable from a spawned sub-agent session (not just the top-level/interactive session) | The item's own question is specifically about spawned sessions, not the Backlog thread, which already has whatever the top-level app provides | Direct tool call from inside this session, or direct reading of the tool's own description for scope restrictions, the same way `EnterWorktree`/`ExitWorktree`'s pinned-subagent restrictions were discovered earlier this session by direct testing, not by assumption |
| Resumes *this* session's own live state, vs. starts something new | The Director's original intent, quoted verbatim in the backlog item, is each group sustaining a watch loop "over its own queue" — closer to "this standing session keeps going" than "a new session gets spawned periodically" | Read each candidate's own documented semantics for whether prior conversational state survives a firing |
| Requires a new, separate configuration/automation surface vs. usable from inside an ordinary tool-calling turn | A mechanism a spawned session can invoke on its own is a smaller, more honestly-scoped change than one requiring separate harness/OS-level setup outside any single conversation | Whether the candidate was actually invoked with a normal tool call in this session, or only inferred from other skills' descriptions |
| Fits this repository's own existing Session Entry model | `CLAUDE.md`'s own "Session Entry" section already requires every new session to "recover state from repository artifacts... not chat memory" — a candidate that produces fresh, stateless sessions is not automatically a mismatch if the repository's own resumption model already assumes exactly that | Compare each candidate's own state-handling against `CLAUDE.md`'s "Session Entry" section, read directly |

## Research log

| Date | Query or source | Finding | URL |
| --- | --- | --- | --- |
| 2026-08-20 | This session's own `Agent` tool description, read directly | Background agents spawned via `run_in_background` do notify the spawning session automatically on completion — a genuine, already-functioning wake trigger, confirmed by this session's own repeated experience resuming after each of its own dispatched Implementation-group subagents finished. But it only fires for agents already dispatched; it creates no mechanism to discover *new* backlog items or *newly* Preflight-passed work plans on its own. | local tool description, this session |
| 2026-08-20 | This session's own available deferred-tool list, containing `mcp__scheduled-tasks__list_scheduled_tasks`, `create_scheduled_task`, `update_scheduled_task`, `delete_scheduled_task`, and the "schedule" skill's own description ("Create, update, list, or run scheduled cloud agents (routines) that execute on a cron schedule") | Loaded via `ToolSearch` from inside this spawned session (not the top-level Backlog thread) — confirms the schema is at least discoverable from a spawned context. `create_scheduled_task`'s own description states tasks are stored at a fixed OS path, `/Users/<user>/.claude/scheduled-tasks/`, and "Scheduled tasks run while this app is open... Each run starts fresh with no memory of this conversation, so the prompt must be fully self-contained." | local tool schema, this session, loaded via `ToolSearch` |
| 2026-08-20 | Direct empirical test: called `mcp__scheduled-tasks__list_scheduled_tasks` from inside this spawned, worktree-isolated session | Succeeded (returned `"No scheduled tasks found. Use create_scheduled_task to create one."`) rather than erroring or being unreachable — confirms the scheduled-tasks API is genuinely callable from a spawned sub-agent context, not merely from the top-level interactive session. This is the one candidate this spike could confirm by direct action rather than by reading a description alone. No task was actually created (out of scope for this spike — see Constraints); only reachability was tested. | direct tool call, this session, see `evidence/scheduled-tasks-list-output.txt` |
| 2026-08-20 | This session's own `Monitor` tool description, read directly | `Monitor` explicitly streams events *into the current turn* while the session stays active; its own description states "the monitor runs until you call `TaskStop` or **the session ends**" and caps `timeout_ms` at 3,600,000ms (1 hour) even before `persistent: true` is considered. This confirms `Monitor` cannot outlive a session going idle — it is a within-turn waiting primitive, not a hibernate-and-resume mechanism. | local tool description, this session |
| 2026-08-20 | This session's own `Bash` tool description, read directly | States explicitly: "Do not sleep between commands that can run immediately," "Do not retry failing commands in a sleep loop," and "Long leading `sleep` commands are blocked... Do not chain shorter sleeps to work around the block." Confirms candidate D (a blocking in-turn polling loop) is not merely discouraged by convention — the tool itself is documented as actively preventing this pattern. | local tool description, this session |
| 2026-08-20 | This session's own available-skills listing: `update-config` ("Automated behaviors... require hooks configured in `settings.json` - the harness executes these, not Claude... For simple settings like theme/model, suggest the `/config` command") and `keybindings-help` (references rebinding session behavior, implying a broader `settings.json`-driven automation surface) | Both skill descriptions reference a harness-level hook system (`settings.json`), including an example phrase "when claude stops show X" implying a `Stop`-type event exists. This spike did **not** invoke `update-config` or attempt to write or read any `settings.json` file — doing so would configure a real, standing automation surface, which is out of this spike's own Constraints (investigation only). This candidate (C) is therefore recorded as **plausible but unverified**, inferred only from two skills' own one-line descriptions, not from direct testing. | local skill descriptions, this session — no file read or written |
| 2026-08-20 | `CLAUDE.md`'s own "Session Entry" section, read directly (this repository's own contract, already in force) | States: "Treat each new session as having no prior chat context. Before acting, recover state from repository artifacts... not from assumed chat history." This is the repository's own existing design for how any new session — spawned fresh or otherwise — is expected to resume work, and it already assumes no persisted conversational memory across sessions. A scheduled, stateless, fresh-session check of repository state (candidate B) is therefore not a mismatch with how this repository already expects sessions to recover state; it is arguably the closest fit among the reachable candidates. | local file, this repository, read in full |
| 2026-08-20 | This session's own entire observed history in this thread (not a citation — a direct empirical record) | Every time this session's own dispatch queue emptied (no background agents in flight), it went idle and required an explicit external `SendMessage` (via the Backlog thread) to resume — this happened repeatedly (each of the four backlog items in this thread: 0016 batch 1, 0017, 0018, 0019, and now 0020, all required an external nudge after the prior queue emptied). This is direct, first-hand confirmation that candidate A alone (background-agent notifications) does not close the gap the backlog item describes — it is real, but insufficient on its own for a fully self-sustaining loop. | this session's own transcript |

## Comparison

| Criterion | A (background-agent notifications only) | B (scheduled fresh-session tasks) | C (harness `Stop` hook) | D (in-turn blocking poll) |
| --- | --- | --- | --- | --- |
| Reachable from a spawned sub-agent session | Yes — already in continuous use this session | **Yes, directly confirmed** by a real tool call from this exact spawned context | Unverified — inferred only from other skills' descriptions, not tested | N/A — ruled out by the tool's own documented behavior before reachability is even relevant |
| Resumes *this* session's own live state | Yes, while it fires | No — each firing is an explicitly fresh, stateless session | Unknown — depends entirely on what script the hook would run, not tested | Would have resumed live state, if it worked, which it does not |
| Usable from inside an ordinary tool-calling turn, no separate configuration surface | Yes | Yes — `create_scheduled_task` is an ordinary tool call | No — requires `settings.json` changes, a system/automation-configuration surface outside a normal conversational turn | Yes, if it worked |
| Fits `CLAUDE.md`'s own Session Entry model (stateless, artifact-based recovery) | N/A (does not produce new sessions) | Yes — a fresh, stateless session reading repository state on each firing is exactly what Session Entry already assumes | Unknown | N/A |
| Closes the actual observed gap (dozens of idle periods needing an external nudge this session) | No, by itself — confirmed insufficient by this session's own repeated experience | Partially — could periodically re-check the queue without an external party's attention, but is architecturally a *different* mechanism (new sessions, not a persisting one) than what ADR 0016's "standing" language implies today | Possibly, if configured and if it works as inferred — not confirmed | No — not a working mechanism at all |

## Cost and quality judgment

- Free / zero-mandatory-spend options considered: all four; none has a
  mandatory paid dimension. Candidate B (scheduled tasks) does introduce
  a *recurring autonomous execution* dimension (each firing consumes
  model usage even with no new work to do) that the other candidates do
  not — a real operational-cost consideration, distinct from license
  cost, that this spike surfaces but does not decide (see Next action).
- Quality bar applied: does the candidate actually work as described,
  confirmed by this session's own direct observation wherever possible,
  rather than accepted on a tool's own marketing-style description alone?
  Candidate B passed this bar (directly invoked, succeeded); candidate C
  did not (not invoked, flagged as unverified rather than presumed
  working, per the backlog item's own explicit instruction not to
  presume); candidate D failed this bar directly (its own tool
  descriptions rule it out).
- No paid option is in play; not applicable.

## Selection

- Selected: human-decision
- Rationale: This spike closes the narrow technical question item-0020's
  own Uncertainty section asked ("determine what wake-up/self-scheduling
  primitives are actually available") — the answer is neither a clean
  "yes, an equivalent exists" nor a clean "no, document manual relay
  only," but a real middle finding: **no primitive lets a specific
  dormant standing session revive itself with live memory and no
  external trigger** (candidates C and D do not deliver this, C
  unverified and D actively ruled out), **but a real, empirically
  confirmed primitive exists that could reduce — not eliminate — the
  Backlog thread's manual-relay burden**, by periodically spawning a
  fresh, stateless session that recovers state from repository artifacts
  the same way this repository's own Session Entry model already
  requires (candidate B). Choosing whether to adopt candidate B as the
  new documented mechanism, accept and honestly document candidate A's
  manual-relay reality as permanent instead, or invest in verifying
  candidate C before deciding, is a judgment call with real operational-
  cost and autonomy-boundary consequences (an unattended, cron-triggered
  agent session running with no human present, at a cadence someone must
  choose) — exactly the kind of value/policy question
  `docs/backlog/item-0020-...md`'s own text names as requiring
  investigation to *inform* a decision, not to make the decision itself.
  This is also squarely an Architecture Path matter under
  `docs/architecture/agent-quickstart.md`'s own "Stop Conditions" (a
  change touching ADR 0016's own topology model and introducing a new
  automation/cost surface), not a Fast- or Feature-Path judgment call
  this spike should resolve unilaterally.
- Discard reasons:
  - A alone: directly, empirically confirmed insufficient by this
    session's own repeated experience this entire thread — real, but not
    self-sustaining on its own.
  - D: ruled out by the tools' own documented constraints, not a
    candidate worth further investigation.
  - Neither B nor C is discarded outright — both remain live options for
    the Director/Backlog thread to choose between (or to defer), which
    is exactly why this spike's own Next action is a human-decision issue
    rather than a spec/ADR authored unilaterally.

## Evidence

- `docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md` (full
  text, read directly)
- `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  and `docs/collaboration/cross-session-messaging.md` (both read in full
  to confirm the item's own characterization of what they do and do not
  currently specify)
- `CLAUDE.md`'s own "Session Entry" section (read directly, this
  repository's existing, already-accepted contract)
- This session's own tool descriptions for `Agent`, `Monitor`, `Bash`,
  and `mcp__scheduled-tasks__*` (read directly, quoted verbatim above)
- `evidence/scheduled-tasks-list-output.txt` — the actual output of the
  one direct empirical test this spike performed
  (`mcp__scheduled-tasks__list_scheduled_tasks`, called from inside this
  spawned, worktree-isolated session)
- This session's own transcript, this entire thread, as first-hand
  evidence that candidate A alone does not close the observed gap

## Next action (exactly one)

- [x] Human decision issue (`Type: decision`): **LISS-0062** — presents
      this spike's own findings (no full self-sustaining single-session
      revival mechanism exists; a real, reachable, but architecturally
      different fresh-session scheduled-polling mechanism does exist; a
      harness-hook-based alternative is plausible but unverified) and
      asks the Backlog thread to choose: (1) adopt scheduled-task-based
      periodic fresh-session polling for one or both standing groups,
      with a cadence to decide; (2) accept the Backlog-thread-relay
      pattern as the permanent, intended mechanism and correct ADR
      0016/`cross-session-messaging.md` to state this honestly instead of
      the current implied-but-unspecified autonomy; (3) authorize a
      further, narrowly-scoped follow-up spike specifically to test
      candidate C (harness `Stop` hooks) before deciding between (1) and
      (2); or (4) hold this item open for further discussion. No ADR or
      work plan is opened by this spike — per the item's own mandate,
      that happens only after the Backlog thread responds to LISS-0062.

## Open risks after close

- Candidate C (harness `Stop` hooks) was evaluated only from two other
  skills' own one-line descriptions, never invoked or tested directly —
  if the Director wants it seriously considered, it needs its own,
  separate, narrowly-scoped spike that actually attempts to configure and
  observe one, which this spike deliberately did not do (writing to
  `settings.json` is a standing-automation-surface change, out of this
  investigation-only spike's own Constraints).
- This spike's assumption that the Implementation group's own tool
  surface matches this Design & Review session's tool surface exactly
  was not independently confirmed by testing from inside an
  Implementation-group session — a reasonable inference from both being
  "standing sessions in the same environment" per ADR 0016, but not
  first-hand evidence for that specific session type.
- If candidate B (scheduled tasks) is eventually adopted, its own
  operational-cost dimension (recurring model usage even when no new work
  exists to pick up) was named but not quantified by this spike — a
  concrete cadence proposal and cost estimate would need to be part of
  whatever design agreement follows the Backlog thread's response to
  LISS-0062, not assumed free merely because the underlying tool has no
  license fee.
