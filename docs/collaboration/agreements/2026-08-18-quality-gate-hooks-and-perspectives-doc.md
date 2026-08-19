# Design Agreement: Mandatory Quality-Gate Hooks, Branch/Route Coverage Policy, and a Living Design/Review Perspectives Document

## Identity

- Agreement ID: DA-2026-08-18-05
- Date: 2026-08-18
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md`
(`Status: promoted`), whose Promotion notes are this agreement's Director
authorization under ADR 0016 Rule 2, three related quality-assurance
requirements:

1. **Mandatory pre-commit quality-gate hooks, per implementation language.**
   Adopting projects must wire actual hooks (not just documented commands)
   that block a commit unless linting, compilation/build, unit tests, and
   coverage all pass.
2. **Branch/route coverage policy with an anti-gaming rule.** Line/statement
   percentage alone is insufficient; every branch/route needs a test, and
   implementation must not be shaped merely to make a coverage number pass.
3. **A living "design & review perspectives" document.** Every review
   finding gets a meta-level pass — what generalizable perspective would
   have caught this — recorded in a document that is refined, not merely
   appended to, distinct from `docs/collaboration/findings-reuse.md`'s
   per-finding issue tracking.

## Spike Result (run by the Design & Review group before this agreement)

Confirmed by direct reading, per item-0006's own Uncertainty checkboxes:

- `docs/architecture/tooling.md`'s stack-specific table is entirely `_TBD_`
  placeholders (confirmed — this template has no fixed language of its own,
  matching item-0006's own "Known constraints" note).
- `docs/architecture/testing-strategy.md` has no coverage policy of any
  kind (confirmed by full read).
- `scripts/lib/emit-tooling-setup-prompt.sh` (the tooling-setup prompt every
  adopting project's first session pastes into an agent) already asks
  Section A to "wire scripts... so one command runs the suite" and Section D
  to "extend CI... so formatter/linter/typecheck/tests run" — but nowhere
  requires that these run automatically *before a commit can land locally*;
  CI alone runs after push, which is exactly the gap item-0006 names.
- No `docs/collaboration/*.md` file resembling a "design & review
  perspectives" document exists; `findings-reuse.md` is confirmed, by
  reading it in full, to track individual findings as issues only, with no
  generalization/refinement step.

## Scope

- In scope:
  - A new ADR (tentatively `0018` — see "Settled Ambiguities" for the
    numbering coordination rule with the concurrently in-flight WP-0004,
    which claims `0017`) recording: the mandatory pre-commit hook
    requirement (contract-level, stack-agnostic — *what* must be true, not
    *which* hook tool); the branch/route coverage anti-gaming rule; the
    living perspectives document's existence, purpose, and relationship to
    `findings-reuse.md`.
  - `docs/architecture/tooling.md`: add a stated requirement that the
    stack-specific table, once filled, must name the actual hook mechanism
    wired (not just the command), and that CI alone does not satisfy this
    item's requirement.
  - `docs/architecture/testing-strategy.md`: add a "Coverage Policy"
    section stating the branch/route anti-gaming rule as a mandatory,
    qualitative requirement (see Settled Ambiguities for why no universal
    numeric floor is mandated by the template itself).
  - `docs/collaboration/definition-of-done.md`: add the hook-wiring and
    coverage-policy requirements to the relevant Done criteria (Phase 2/3
    Done, Universal Done) — this file is an ADR-0006 contract file.
  - `scripts/lib/emit-tooling-setup-prompt.sh`: strengthen Section A/D so
    the paste-ready prompt explicitly asks the adopting project's agent to
    wire an enforcing pre-commit hook (naming the mechanism per detected
    stack — native git hooks, husky/lefthook for Node, pre-commit for
    Python, cargo-husky-style for Rust, etc.) and to state the branch/route
    coverage approach, not only to "wire scripts" and "extend CI." This
    script is not itself in the ADR-0006 contract-file list.
  - A new `docs/collaboration/design-review-perspectives.md` (living
    document, ADR-0006 contract file since it is a new
    `docs/collaboration/*.md` file), seeded with real, already-available
    generalizable perspectives distilled from this repository's own
    existing `docs/collaboration/reviews/*.md` history (not left as an
    empty template) — format fixed in "Settled Ambiguities."
  - `docs/architecture/agent-quickstart.md`'s "Required Area Documents" and
    `CLAUDE.md`'s reading list: add the new perspectives document alongside
    `source-code-quality.md`, per item-0006's own "becomes required reading
    during design intake" requirement — both are contract files.
  - AI work traces for every contract-file change (`definition-of-done.md`,
    the new perspectives document, `CLAUDE.md`).
  - Preflight and separate-context Reviewer pass.
- Explicitly out of scope:
  - Actually installing a hook tool or coverage tool in *this* template
    repository (it has no fixed stack of its own — this item changes the
    *contract* adopting projects must satisfy, not this repository's own
    tooling; `scripts/` is template-native Python with no test suite today,
    and retrofitting that is not this item's job — see Settled Ambiguities).
  - Mandating one specific numeric coverage floor across all stacks — see
    Settled Ambiguities.
  - Rewriting `docs/collaboration/findings-reuse.md`'s existing per-finding
    lifecycle; this item only states, in both documents, how they relate.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Write ADR 0018 (or the confirmed next-free number) | Implementer | Architecture Path | States all three rules (hooks, coverage anti-gaming, perspectives doc) as testable requirements; states the numeric-floor non-decision and the no-retroactive-application-to-`scripts/` decision, both with grounds; cites the spike findings above | read-through; not an ADR-0006 contract file, no trace required |
| 2 | Update `docs/architecture/tooling.md` and `docs/architecture/testing-strategy.md` | Implementer | Architecture Path | Hook-wiring requirement and Coverage Policy section added; neither file is an ADR-0006 contract file so no trace required for this task alone, but content must not contradict the ADR | read-through diff |
| 3 | Update `docs/collaboration/definition-of-done.md` | Implementer | Architecture Path | Phase 2/3 Done and Universal Done gain the hook/coverage requirements without weakening any existing criterion | `scripts/check-contract-consistency.py`; read-through diff |
| 4 | Strengthen `scripts/lib/emit-tooling-setup-prompt.sh` | Implementer | Architecture Path | Section A/D explicitly requires naming and wiring an enforcing pre-commit hook mechanism and a branch/route coverage approach, per detected stack; existing detection/sections otherwise unchanged | manual read-through; running `scripts/init-loop-settings.sh --prompt-only` and confirming the new language appears in its output |
| 5 | Create `docs/collaboration/design-review-perspectives.md`, seeded from real review history | Implementer | Architecture Path | At least 3 real, generalizable perspectives distilled from actual `docs/collaboration/reviews/*.md` entries (not invented examples), each stating: the originating finding(s), the generalized perspective, and when to apply it; explicitly distinguished from `findings-reuse.md` | `scripts/check-contract-consistency.py`; read-through |
| 6 | Wire the new document into required reading (`agent-quickstart.md`, `CLAUDE.md`) | Implementer | Architecture Path | Both files list the new document alongside `source-code-quality.md` | `scripts/check-contract-consistency.py`; read-through |
| 7 | AI work traces for Tasks 3, 5, 6 (contract-file changes) | Implementer | Architecture Path | One trace per contract file touched, or one combined trace naming all three if the Implementer judges them one cohesive change — Implementer's call, but must name every contract file changed | trace file(s) exist under `docs/collaboration/traces/` |
| 8 | Self-review Tasks 1-7 | Implementer | Architecture Path | Full form per `docs/templates/self-review.md` (planning size `M`, multiple areas) | self-review record in the relevant issue's Work Notes |
| 9 | Preflight Validation | Implementer / deterministic tool | Architecture Path | `pass` recorded with command output | Preflight section in WP-0006 |
| 10 | Separate-context Reviewer pass | Reviewer (Design & Review group, separate context) | Architecture Path | Review record explicitly addresses each contract-file change under ADR 0006, and confirms the perspectives document's seeded content is genuinely drawn from real review history, not fabricated | review record under `docs/collaboration/reviews/` |

Sequencing: Task 1 blocks 2-6 (all cite the ADR). Task 5 should read a
representative sample of `docs/collaboration/reviews/2026-08-02-*.md` and
`2026-08-18-*.md` before writing, not invent examples. Task 7 follows 3, 5,
6. Task 8 follows 1-7. Task 9 follows 8. Task 10 follows 9.

## Specifications

- None. Process/governance change; no application specification.

## Boundaries

- ADR 0006's separate-context Reviewer and traceability rules apply in full
  to `definition-of-done.md`, the new perspectives document, and
  `CLAUDE.md`.
- No hook tool or coverage tool is actually installed in this template
  repository itself.
- The new perspectives document must not duplicate `findings-reuse.md`'s
  per-finding tracking — it generalizes, `findings-reuse.md` tracks
  individual findings.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` until the
  Director's own work-plan-close action.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Item-0006 flagged "[x] Human decision required... how strict the branch/route coverage requirement should be (is a numeric floor still useful..., does this apply retroactively to `scripts/`)." Does this block the whole item? | No — narrowed to what actually needs a value judgment. The *qualitative* anti-gaming rule (every branch/route needs a test; no coverage-shaped implementation) is not a value call — it is unambiguously correct and already fully specified in item-0006's own Summary, points 1-2; this agreement adopts it as mandatory. Whether to *additionally* mandate one universal numeric floor across every possible adopting stack genuinely has no single correct answer (item-0006's own text raises the tension: a floor is a useful backstop but is also exactly the kind of number the anti-gaming rule warns against optimizing toward) — this agreement does not mandate one; each adopting project's own tooling-setup session (per the strengthened `emit-tooling-setup-prompt.sh`) may choose a floor as a *local* decision, recorded there, not fixed by the template contract. Retroactive application to this template's own `scripts/` directory is answered no, by ordinary scoping judgment, not a value call: this item establishes the *contract adopting projects' own stacks must satisfy*, not a retrofit obligation for this template repository's own zero-test-coverage Python scripts today; retrofitting `scripts/` with tests to satisfy a policy this same item just invented is a separate, unscoped body of work item-0006's text does not ask for. | Design & Review group (Planner), narrowing the flagged human-decision item to its genuinely open sub-question and resolving the rest by ordinary judgment, with grounds stated |
| ADR number | Tentatively `0018`. `DA-2026-08-18-03` (WP-0004, item-0007, dispatched earlier and already in progress) claims `0017`. The Implementer must run `ls docs/architecture/adr/` immediately before creating this ADR to confirm the true next-free number at execution time; if `0017` is still free (WP-0004 has not yet landed it) and `0018` collides with something else, or if both are already taken by the time this issue executes, this is a reopening-worthy numbering conflict between two concurrently in-flight work plans (ADR 0016 Rule 3 names this exact class of risk) — report it rather than silently renumbering. | Design & Review group (Planner) |
| Perspectives document format | `docs/collaboration/design-review-perspectives.md`. Structure: organized by *perspective* (a named, generalizable lens — e.g. "verify claimed authority independently of its own claim," "a numeric target invites shaping the artifact to hit the number rather than to be correct"), not chronologically by finding. Each entry: the perspective, when to apply it, and the originating finding(s)/review(s) that revealed it (linked, not restated). New entries are integrated into the existing structure (merged into a related perspective, or added as a new one) rather than appended as a flat log — this is what "refined, not merely appended to" requires operationally. | Design & Review group (Planner), operationalizing item-0006's own "grow into a genuinely sophisticated reference... not a flat chronological log" requirement |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should a specific numeric coverage floor recommendation (not requirement) be added to `docs/templates/examples/` per ecosystem, as a non-binding starting point for adopting projects? | A future backlog item, if adopting projects report the fully-open "choose your own floor" guidance is insufficiently actionable in practice |
| Should `findings-reuse.md` itself be edited to cross-reference the new perspectives document, beyond what this item's Task 5/6 already add from the perspectives document's own side? | Only if the Reviewer or a future finding shows a one-directional cross-reference (perspectives -> findings-reuse, not the reverse) is actually confusing in practice — not assumed necessary now |

## Verification

- `scripts/check-contract-consistency.py` after the contract-file edits.
- `scripts/init-loop-settings.sh --prompt-only` output, confirmed to
  contain the strengthened hook/coverage language.
- Confirmation that `docs/collaboration/traces/` contains trace(s) covering
  every contract file touched.
- Separate-context Reviewer approval, explicitly confirming the
  perspectives document's seeded entries trace to real review records.

## Falsification Criteria

- The template mandates one specific numeric coverage floor as a hard
  requirement for every adopting stack.
- `scripts/` in this template repository is required to gain retroactive
  test coverage as part of this item.
- The perspectives document's initial entries are invented rather than
  drawn from this repository's actual review history.
- The perspectives document duplicates `findings-reuse.md`'s per-finding
  lifecycle tracking instead of generalizing from it.
- Any contract-file change lands without a trace or without
  separate-context Reviewer approval.
- Two work plans (this one and WP-0004) claim the same ADR number without
  either being flagged as a reopening-worthy conflict.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2. The
      Promotion notes direct the Design & Review group to resolve the
      Uncertainty spike and Known-constraints boundary questions "through
      its own judgment"; this agreement extends that same judgment to the
      narrow sub-question left under the item's "[x] Human decision
      required" flag, with explicit grounds recorded above rather than
      silently assumed, per "Settled Ambiguities."
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan and the spike result above.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
