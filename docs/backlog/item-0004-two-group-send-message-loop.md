# Backlog item: item-0004-two-group-send-message-loop

## Metadata

- Item ID: item-0004
- Title: Standing three-layer loop over send_message (Backlog / Design &
  Review / Implementation)
- Status: promoted
- Created: 2026-08-18
- Updated: 2026-08-18
- Priority hint: high
- Suggested planning size: L
- Owner/agent (optional): unassigned

## Summary

Adopt the recently released `send_message` / `ListAgents` cross-session
tools to run this repository's closed execution loop across standing,
separate sessions instead of one undifferentiated session doing every
persona's work:

- **Backlog layer**: a Director-facing thread (this one) where direction is
  captured and backlog items are approved. Not tied to any single work plan
  — the Director can keep adding unrelated items here over time.
- **Design & Review layer**: its own separate standing sub-agent session
  (Planner, Specifier, Reviewer, Arbiter). Pulls approved backlog items,
  produces the work plan/specs/design agreement autonomously, and later
  reviews the Implementation layer's output in a separate context.
- **Implementation layer**: its own separate standing sub-agent session
  (Implementer). Executes work plans handed off by the Design & Review
  layer, self-reviewing each issue, in a dedicated `git worktree`/branch.

Human approval stays at exactly two points — design approval (now satisfied
at backlog-item approval, batched rather than per-work-plan) and completion
approval (work-plan close) — and neither blocks the loop across
concurrently in-flight work plans. The Director may intervene in either
sub-agent session at any time by sending it a chat message directly; this
gates only the specific in-flight item to per-step human approval until a
resolving instruction, not the whole session's other concurrent work.
Autonomous progress is bounded by the project's operational rules and
applicable law.

## Why it might matter

Removes the Backlog-thread Director from being consumed as the de facto
Design & Review session for the duration of one work plan, so the Director
can keep using this thread for other, unrelated backlog intake while
Design & Review and Implementation run independently in the background.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes (no new paid
  dependency; reuses tools already available in this environment)
- Boundaries or non-goals:
  - No automation script/launcher for starting either sub-agent session in
    this pass — manual start via the Agent tool for now.
  - Does not change ADR 0006's contract-file governance, the Reviewer's
    three constraints, the Implementer's self-review requirements, or the
    three invariants.

## Uncertainty

- [ ] Spec can be written now
- [x] Human decision required (value, policy, budget, legal) — settled
      through direct Director dialogue; see the design agreement's Settled
      Ambiguities for the recorded answers, including the 3-layer
      clarification this item's title reflects.

## Links

- Spike case: none
- Work plan (when promoted): `docs/work-plans/WP-0002-two-group-send-message-loop.md`
- Design agreement (when promoted): `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
  (`DA-2026-08-18-01`)
- Local issue (LISS): LISS-0019 through LISS-0026
- Spec: none (governance/process change)
- ADR: `docs/architecture/adr/0016-*.md` (not yet written)

## Promotion notes

- Date: 2026-08-18
- Decision: promoted directly from Director dialogue in this Backlog-layer
  thread, without a separate live Planner dialogue turn for this specific
  work plan (the dialogue that produced WP-0002 and DA-2026-08-18-01
  happened in this same thread, ahead of standing up a separate Design &
  Review session — a bootstrap exception, not the standing pattern this
  item itself defines going forward).
- Reason: this is the founding work plan for the very topology it
  introduces, so no separate standing Design & Review session existed yet
  to do that work independently. The Director confirmed, after WP-0002 and
  the design agreement were already drafted in this thread, that the
  3-layer split (with Design & Review as its own separate sub-agent
  session) is the intended standing model — so a Design & Review sub-agent,
  spawned separately from this Backlog thread, is expected to review and,
  where its own judgment calls for it, revise WP-0002, the local issues,
  and the design agreement's wording before drafting ADR 0016 and
  propagating the affected documents. This thread does not resolve that
  judgment call itself.
