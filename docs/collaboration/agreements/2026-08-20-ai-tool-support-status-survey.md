# Design Agreement: AI tool support status survey

Store the completed record at
`docs/collaboration/agreements/2026-08-20-ai-tool-support-status-survey.md`.

See `docs/collaboration/design-agreement.md` for the rules this record
implements.

## Identity

- Agreement ID: DA-2026-08-20-08
- Date: 2026-08-20
- Director: per ADR 0016 Rule 2, backlog-item-level agreement — see
  "Agreement" below.
- Planner / Specifier personas (model or tool used): Design & Review
  group, standing session (Claude Code, Planner/Specifier persona).
- Supersedes agreement (if any): none.

## Direction

`docs/backlog/item-0021-ai-tool-support-status-survey.md`
(`Status: promoted`, "Promoted, in the Backlog-layer thread"): survey this
template's support status across Claude Code, Codex, Cursor, Grok, and
Antigravity; produce a status report; update instruction/mirror files
where feasible. The required-first spike
(`docs/spike/case-0004-ai-tool-support-status-survey/case.md`) confirmed
existing Codex/Grok/Copilot research is still current, and fully
investigated Antigravity from primary sources (no prior coverage in this
repository).

## Scope

- In scope: `docs/architecture/ai-tool-support-status.md` (the status
  report), `docs/spike/case-0004-...md` (the spike record), and the one
  concrete, fixable gap the survey found — adding Antigravity's
  `AGENTS.md`-native status to
  `docs/collaboration/prompt-instruction-change-control.md` (LISS-0069).
- Explicitly out of scope: any redesign of ADR 0016/0017's own topology;
  any new mirror file for Codex or Antigravity (neither needs one); any
  content change to `.cursor/rules/*.mdc` or `.grok/rules/*.md` (both
  confirmed current); live-testing inside any non-Claude-Code tool.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Survey all five tools via primary-source research | Planner | Spike | `case-0004` closed with a sourced finding per tool | `docs/spike/case-0004-...md`'s own Research log |
| 2 | Draft the status report | Planner/Specifier | docs-only | Report accurately summarizes the spike's own sourced findings | Direct comparison against the spike's own Research log |
| 3 | Independently re-verify the report's own key citations; add the Antigravity contract-registry entry | Implementer | Architecture Path | LISS-0069's Acceptance Notes fully satisfied | Independent URL re-fetch; `git diff` scope check |
| 4 | Preflight Validation over the whole work plan | Implementer | Preflight | All checks recorded with real output | WP-0025's own Preflight Validation section |
| 5 | Work-plan-level Reviewer pass | Reviewer | Review | Approval record addressing evidence-sufficiency and boundary-conformance explicitly | `docs/collaboration/reviews/2026-08-20-wp-0025-....md` |

Sequencing and dependencies: 1 -> 2 -> 3 -> 4 -> 5, strictly.

## Specifications

No `docs/specs/` file covers this work plan — a research/status-report
deliverable plus one narrow contract-file addition, not application
behavior.

## Boundaries

- No rewrite of the spike's own Research log to make the report read
  differently than what was actually found.
- No touch to any file other than
  `docs/collaboration/prompt-instruction-change-control.md`, the new
  trace file, and this work plan's own tracking files, beyond the report
  and spike case themselves.
- Per ADR 0006: the `prompt-instruction-change-control.md` edit requires
  separate-context Reviewer approval and the trace named in LISS-0069 —
  non-negotiable regardless of the Director's own request having
  originated this work.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does Antigravity need its own dedicated mirror file, the way Cursor and Grok Build have? | No — it reads `AGENTS.md` natively, the same situation Codex is already in; the fix is a contract-registry entry stating this explicitly, not a new mirror file | Design & Review group (Planner), per `case-0004`'s own primary-source finding |
| Is Antigravity's peer-messaging capability equivalent to `SendMessage`/`ListAgents`? | Not confirmed — reported precisely as "partial, closer than the other three tools, but no confirmed discovery-mechanism equivalent," per the spike's own explicit refusal to overclaim from an ambiguous primary source | Design & Review group (Planner), per `case-0004`'s own Research log |
| Should the status report itself go through the same separate-context Reviewer process as the contract-file edit? | The report itself is not an ADR-0006 contract file, so it is not independently gated the same way — but this work plan still requires an independent re-fetch check of its own key citations (LISS-0069's own Acceptance Notes) before the Reviewer pass, and the Reviewer independently re-verifies again, so no single context's claim about the report's own accuracy goes unchecked | Design & Review group (Planner), recorded in WP-0025's own Risks section |

## Deferred Questions

None — this is a fully bounded, fully specified work plan.

## Verification

- Independent URL re-fetch confirming the report's own key citations
  (LISS-0069's own Acceptance Notes).
- `python3 scripts/check-contract-consistency.py` — no regression.
- `git diff` confirming the contract-file edit's own narrow scope.

## Falsification Criteria

This design was wrong if, after execution:

- An independent re-fetch of either named URL contradicts the status
  report's or spike case's own quoted claim.
- The contract-file edit touches any row, bullet, or section beyond what
  LISS-0069 names.
- No AI work trace exists for the contract-file edit, or it omits any of
  the three required facts.

## Agreement

- [x] **Director**: this plan and these specifications describe what I
      want built, and the stated boundaries are the right ones. — Per
      ADR 0016 Rule 2's backlog-item-level agreement:
      `docs/backlog/item-0021-...md`'s own Promotion notes state
      "Promoted, in the Backlog-layer thread... Design & Review proceeds
      autonomously from here, starting with the spike," matching exactly
      what this work plan executes.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Nothing in them requires guessing at a
      rule that was never stated. — Design & Review group (Planner),
      2026-08-20. The report's own content, the exact contract-file
      insertion text, and the independent-verification requirement are
      all specified explicitly, not left for the Implementer to guess.

If the AI cannot make its statement, the design phase is not finished,
regardless of the Director's readiness to proceed.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
