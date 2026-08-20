# Design Agreement: Check-and-spawn wake protocol

Store the completed record at
`docs/collaboration/agreements/2026-08-20-self-sustaining-wakeup-protocol.md`.

See `docs/collaboration/design-agreement.md` for the rules this record
implements.

## Identity

- Agreement ID: DA-2026-08-20-06
- Date: 2026-08-20
- Director: direct decision, given verbatim in the Backlog-layer thread
  and quoted in full in `docs/issues/LISS-0062-self-sustaining-wakeup-mechanism-decision.md`'s
  Work Notes — not a backlog-item-level delegation under ADR 0016 Rule 2
  in the usual sense, since the Director stated the exact mechanism
  directly rather than leaving Design & Review to design it; see
  "Agreement" below.
- Planner / Specifier personas (model or tool used): Design & Review
  group, standing session (Claude Code, Planner/Specifier persona).
- Supersedes agreement (if any): none. This agreement is additive to
  `DA-2026-08-18-01` (ADR 0016 Rules 1-6) — it covers only the new Rule 7
  this work plan adds; it does not reopen or restate Rules 1-6.

## Direction

`docs/backlog/item-0020-self-sustaining-group-wakeup-loop.md`
(`Status: promoted`) asked whether a spawned sub-agent session can wake
itself up without external help. The required-first spike
(`docs/spike/case-0003-self-sustaining-group-wakeup-loop/case.md`,
`Status: closed`, Selection: human-decision) found no such primitive
exists, and asked the Director to choose among several options. The
Director's actual direction — given directly, not chosen from the
spike's own menu — is the check-and-spawn / queue-continuation protocol
quoted verbatim in `docs/issues/LISS-0062-...md`'s Work Notes: waking the
next layer becomes the responsibility of the event that produces new
approved work (the Backlog thread on backlog approval; Design & Review on
work-plan approval), each standing loop checks its own queue before going
idle, and any spawning party checks for and resumes a surviving
worktree/branch — including one left by a session that just failed —
before creating a duplicate.

## Scope

- In scope: the exact text specified in
  `docs/issues/LISS-0063-check-and-spawn-wake-protocol.md`'s Acceptance
  Notes, added to ADR 0016 (a new Rule 7, a Status-section sentence, two
  Enforcement bullets) and to
  `docs/collaboration/cross-session-messaging.md` (updates to directions
  1 and 2, plus a new section); the mandatory AI work trace for both
  contract-file edits.
- Explicitly out of scope: any change to ADR 0016 Rules 1-6, any other
  existing content in either file, any other contract file, any new
  script/helper/automation surface, and any scheduled-task or
  `.claude/settings.json` hook (the spike's own Selection deliberately
  avoided both; the Director's decision uses only already-confirmed tools).

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Add ADR 0016 Rule 7, Status-section sentence, and two Enforcement bullets, verbatim per LISS-0063 | Implementer | Architecture Path | Text matches LISS-0063's own specification exactly; no other ADR 0016 content touched | `grep`/`git diff` against LISS-0063's own quoted text |
| 2 | Update `cross-session-messaging.md` directions 1/2 and add the new "Queue continuation and resume-before-duplicate-spawn" section, verbatim per LISS-0063 | Implementer | Architecture Path | Text matches LISS-0063's own specification exactly; no other content touched | `grep`/`git diff` |
| 3 | Write the mandatory AI work trace | Implementer | Architecture Path | Trace states which files changed, why, what behavior changes | Direct reading against `docs/templates/ai-work-trace.md`'s required sections |
| 4 | Preflight Validation over the whole work plan | Implementer | Preflight | All checks in WP-0023's own Preflight Validation section recorded with real output | WP-0023's own Preflight Validation section |
| 5 | Work-plan-level Reviewer pass | Reviewer | Review | Approval record addressing boundary-conformance and evidence-sufficiency explicitly, per ADR 0006's contract-file governance (separate context, mandatory regardless of urgency) | `docs/collaboration/reviews/2026-08-20-wp-0023-....md` |

Sequencing and dependencies: 1 and 2 may proceed in either order (disjoint
files) but both must land before 3 (the trace documents both edits
together); 4 only after 1-3 land; 5 only after 4 records a `pass`.

## Specifications

No `docs/specs/` file covers this work plan — a process/contract
documentation change, not application behavior.

## Boundaries

- No change to ADR 0016 Rules 1-6 or any other existing sentence in
  either file.
- No change to any other contract file
  (`docs/collaboration/prompt-instruction-change-control.md`,
  `AGENTS.md`, `CLAUDE.md`, etc.).
- No new script, helper, scheduled task, or `.claude/settings.json` hook.
- Per ADR 0006 (`docs/collaboration/prompt-instruction-change-control.md`):
  this contract-file change requires separate-context Reviewer approval
  and the trace named above — non-negotiable regardless of the
  Director's own direct involvement in producing the content, per that
  document's own "No Director instruction waives this rule" statement.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does this agreement supersede `DA-2026-08-18-01` (ADR 0016's original Rules 1-6 agreement)? | No — additive only. `DA-2026-08-18-01` continues to cover Rules 1-6 unchanged; this agreement covers only the new Rule 7 | Design & Review group (Planner), stated in this agreement's own Identity section |
| Is a code/script surface needed for this protocol (a helper that performs the `ListAgents` check automatically)? | No existing script in `scripts/` orchestrates cross-session spawning/messaging today — every prior handoff this session performed the check-and-act directly via its own tool calls, not through a helper script. This work plan documents the protocol as a rule for sessions to follow, the same category as most of this repository's other process rules; it does not add new tooling. If the Implementer finds an existing code surface this should hook into, that is a scope question to flag via a reopening request, not resolve unilaterally by expanding scope | Design & Review group (Planner), recorded in WP-0023's own Scope "Out" list |
| Was the specific claim that LISS-0062 was "uncommitted" at the time of the Director's addendum accurate? | No — independently verified via `git log` that it was already committed (`6c797ca`) before that message arrived. The addendum's own underlying rule (check for and resume a surviving worktree/branch before spawning a duplicate) is adopted on its own merits regardless of this one incident's precise accuracy — recorded as a correction in LISS-0062's own Work Notes, not silently accepted | Design & Review group (Planner/Reviewer), recorded in LISS-0062's Work Notes |

## Deferred Questions

None — this is a fully bounded, fully specified documentation change with
every inserted sentence given verbatim in LISS-0063's own Acceptance
Notes.

## Verification

- `python3 scripts/check-contract-consistency.py` — no regression.
- `grep`-based confirmation that every piece of LISS-0063's own required
  text landed exactly as specified, in both files.
- Confirmation the mandatory trace exists and states all three required
  facts.
- Independent, separate-context Reviewer approval, addressing
  boundary-conformance and evidence-sufficiency explicitly.

## Falsification Criteria

This design was wrong if, after execution:

- Any inserted text differs in substance from what LISS-0063 specifies
  verbatim (not counting trivial whitespace/formatting normalization).
- ADR 0016 Rules 1-6, or any other existing sentence in either file, is
  altered.
- Any file other than the two contract files, the new trace, and this
  work plan's own tracking files is changed.
- No AI work trace exists for the two contract-file edits, or the trace
  omits any of the three required facts (which files, why, what behavior
  changes).

## Agreement

- [x] **Director**: this plan and these specifications describe what I
      want built, and the stated boundaries are the right ones. — The
      Director gave the exact protocol text directly (quoted verbatim in
      `docs/issues/LISS-0062-...md`'s Work Notes and reproduced exactly
      in `docs/issues/LISS-0063-...md`'s Acceptance Notes); this
      agreement's Plan implements that direction with no interpretation
      beyond formatting it into ADR/contract-document prose.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Nothing in them requires guessing at a
      rule that was never stated. — Design & Review group (Planner),
      2026-08-20. Every inserted sentence is given verbatim; the one
      genuinely open question this scope raised (whether a code surface
      is needed) is settled above as "no, unless the Implementer finds
      otherwise, which is a reopening question not a silent scope
      expansion."

If the AI cannot make its statement, the design phase is not finished,
regardless of the Director's readiness to proceed.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
