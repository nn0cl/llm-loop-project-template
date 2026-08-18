# Backlog item: item-0006-quality-gate-hooks-and-review-perspectives-doc

## Metadata

- Item ID: item-0006
- Title: Mandatory pre-commit quality-gate hooks, branch/route coverage
  policy, and a living design/review-perspectives document
- Status: promoted
- Created: 2026-08-18
- Updated: 2026-08-18
- Priority hint: high
- Suggested planning size: TBD
- Owner/agent (optional): unassigned

## Summary

Three related quality-assurance requirements to add to this template's
contract:

1. **Pre-commit quality-gate hooks, per implementation language.** Require
   that adopting projects wire actual hooks (not just documented commands
   run manually) that block a commit unless linting, compilation/build,
   unit tests, and coverage all pass. Today
   `docs/architecture/tooling.md`'s stack-specific table is all `_TBD_`
   placeholders, and verification is "run the command, paste the output" —
   there is no requirement that it runs automatically before a commit can
   land.
2. **Branch/route coverage policy, with an anti-gaming rule.** Line/statement
   coverage percentage alone is not sufficient:
   - A test that exercises only one side of a branch (e.g. only the `if`,
     never the `else`) does not count as covering that branch.
   - When a function has multiple routes/paths, tests must be added to
     cover every route, not a representative subset chosen to hit a
     numeric target.
   - Implementation must not be written merely to make a coverage number
     pass (e.g. adding trivial/dead branches, or code shaped to be
     "easy to cover" rather than correct) — coverage is evidence of
     testing thoroughness, not a target to optimize directly.
   `docs/architecture/testing-strategy.md` currently has no coverage policy
   at all.
3. **A living "design & review perspectives" document.** Every time a
   source-code review (self-review or the work-plan-level Reviewer pass)
   surfaces a finding, its result must be introspected at a meta level: not
   just "what was wrong here," but "what class of design/implementation
   perspective would have caught this, and is it generalizable." That
   analysis is recorded in a dedicated, curated document — distinct from
   `docs/collaboration/findings-reuse.md`, which tracks individual findings
   as issues, not generalized perspectives. This document must be
   *refined*, not merely appended to, each time a new perspective is added
   — it should grow into a genuinely sophisticated reference on what to
   watch for in design and implementation, not a flat chronological log.
   It becomes required reading during design intake and implementation,
   alongside `docs/collaboration/source-code-quality.md`.

## Why it might matter

Without (1) and (2), "deterministic verification" (required throughout this
template's Definition of Done) can be satisfied by a shallow or gamed test
suite. Without (3), the same class of design mistake can recur across work
plans because review findings are tracked individually (per
`findings-reuse.md`) but the generalizable lesson behind them is never
distilled or fed back into future design intake.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes (prefer coverage/lint
  tooling with no mandatory paid tier)
- Boundaries or non-goals (tentative, to confirm during planning):
  - This repository itself (the template) has no fixed implementation
    language of its own — `CLAUDE.md`'s "Selected Stack" section is an
    unfilled placeholder. Item (1) and (2) likely land as: (a) a stronger
    contract requirement in `docs/architecture/tooling.md` /
    `docs/collaboration/definition-of-done.md` that adopting projects must
    configure enforcing hooks, and (b) a strengthened tooling-setup prompt
    in `scripts/init-loop-settings.sh` that asks for hook wiring
    explicitly, not just command discovery. Needs confirmation before
    planning.
  - Interaction with `docs/collaboration/findings-reuse.md` needs to be
    made explicit so the two documents (per-finding issue tracking vs.
    the generalized perspectives document) do not duplicate or contradict
    each other.

## Uncertainty

- [ ] Spec can be written now
- [x] Spike required first (options, feasibility, or quality unknown) —
      which hook mechanism (native git hooks, a task runner, a
      language-specific tool like pre-commit/husky/lefthook) to recommend
      per stack, and where the perspectives document should live and how
      it should be structured to actually "grow" rather than become an
      unreadable append-only log.
- [x] Human decision required (value, policy, budget, legal) — how strict
      the branch/route coverage requirement should be (e.g. is a numeric
      floor still useful alongside the branch-coverage rule, and does this
      apply retroactively to existing template-native Python scripts under
      `scripts/`).

## Links

- Spike case: none yet
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none yet — related existing documents:
  `docs/architecture/tooling.md`, `docs/architecture/testing-strategy.md`,
  `docs/collaboration/definition-of-done.md`,
  `docs/collaboration/source-code-quality.md`,
  `docs/collaboration/findings-reuse.md`

## Promotion notes

- Date: 2026-08-18
- Decision: Promoted, in the Backlog-layer thread, after WP-0002 closed.
  Per ADR 0016 Rule 2, this approval is the single design-phase gate — the
  Design & Review group proceeds autonomously from here: resolve the
  Uncertainty spike (hook mechanism per stack, where the perspectives
  document lives) and the Known-constraints boundary questions (this
  template has no fixed language of its own; interaction with
  `findings-reuse.md`) through its own judgment, then build the work plan,
  spec, and design agreement, without a further live dialogue turn with the
  Director for this item.
- Reason: Well-specified direction already captured; ready to run.
