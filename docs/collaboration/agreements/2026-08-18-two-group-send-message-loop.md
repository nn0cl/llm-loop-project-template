# Design Agreement: Standing Two-Group Loop over send_message

## Identity

- Agreement ID: DA-2026-08-18-01
- Date: 2026-08-18
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code
- Supersedes agreement (if any): none directly. Supersedes, in effect, ADR
  0001's per-work-plan Planner-Director dialogue requirement (Decision, point
  2) and ADR 0014's restatement of it (Decision, clause 1), and ADR 0014
  clause 5's "the next work plan does not start without [close]" as applied
  across concurrently in-flight work plans, via the new ADR (0016) this
  agreement covers. (Corrected from an earlier draft's "clause 6" — the
  blocking phrase is in clause 5; clause 6 states the two-touchpoint count,
  which ADR 0016 does not change. See ADR 0016's own "Supersession,
  precisely" table.)

## Direction

The Director's framing, reached through dialogue across several turns:

- Add the recently released `send_message` cross-session capability to this
  template's loop. Split the closed execution loop into two groups: a
  Design & Review group and an Implementation group. Work plans and issues
  are pulled from the Design & Review side, executed by the Implementation
  group, and returned to the Design & Review group for review and approval.
- Human approval remains exactly two points: design approval, and approval
  of the finished product. Human approval must not block the loop.
- Clarified, on what "must not block" means: the Director and AI reach
  agreement/approval on requirements at the backlog level. Once a backlog
  item is approved, requirement organization, research, and method/approach
  study inside the development loop proceed without further human approval.
  The Director may intervene in the development loop at any time. Proceeding
  without per-step approval is conditioned on operating within the project's
  operational rules and applicable law. Recorded verbatim: "人間とAIはバック
  ログに積まれた要件に対して合意と承認をおこなうので、開発ループに入った、要
  件整理や、調査、方式検討などについては人間の承認無く進めることが出来る。
  ただし、人間は開発ループに対して随時介入できる。また、承認無く進めること
  は出来るが、それはプロジェクトの運用規約や法律を守る前提で運用される。"
- Clarified, on session topology: a standing session pair — one session (or
  small session group) per side, started once and kept alive, not
  reconstituted per work plan. Recorded verbatim: "常設セッションペア(推奨)".
- Clarified, on git isolation: the Implementation group works in a dedicated
  `git worktree` and branch per work plan; the Design & Review group works
  against `main`. Recorded verbatim: "Implementation側は専用worktree/branch
  (推奨)".
- Clarified, on this work plan's scope: process documents only — a new ADR
  and updates to the affected collaboration documents. No automation script
  or launcher is built in this pass. Recorded verbatim: "プロセス文書のみ
  (推奨・小さく始める)".
- Approved the full restated plan (two groups mapped onto existing personas,
  backlog-gated design phase, non-blocking multi-work-plan close, standing
  session pair, dedicated Implementation-group worktree, process-docs-only
  scope) with: "承認。介入は各グループに人間がチャットを送信することで始め
  る。人間がチャットに入力をしたら解消するまで人間と作業を進め、指示が出る
  まで作業を進め、指示が出るまでループを続行しない。"
- Refined, after the above, what "does not continue the loop" means during
  an active intervention: it does not mean the affected work stops outright.
  It means the specific in-flight item becomes work that requires human
  approval at each step; the development loop and review continue on that
  item, gated by the Director's approval, until a resolving instruction is
  given. Recorded verbatim: "ループを続行しないというのは作業が人間の承認を
  必要とする作業になるという意味で、開発ループ・レビューなどは自体は人間の
  承認を得ながら進める。" This refines, and does not contradict, the prior
  turn's statement — intervention gates the specific item to per-step
  approval rather than freezing it, and other concurrent work in either
  group is unaffected.

## Scope

- In scope:
  - A new ADR (LISS-0019 / ADR 0016) recording: the two standing groups and
    their persona mapping; the backlog-item-level design gate replacing a
    mandatory per-work-plan live dialogue; non-blocking concurrency across
    work plans awaiting the Director's closing checkpoint; the Director
    intervention channel and its per-item, per-step-approval effect;
    the standing compliance-boundary constraint (operational rules, law).
  - Every collaboration document the new rule touches: `personas.md`
    (LISS-0020), `ai-human-scheme.md` (LISS-0021), a new
    `cross-session-messaging.md` (LISS-0022), `session-start-and-resume.md`
    (LISS-0023), `branch-commit-pr-discipline.md` (LISS-0024),
    `design-agreement.md` (LISS-0025), and `docs/backlog/README.md`
    (LISS-0026).
- Explicitly out of scope:
  - Any automation script or launcher that starts, supervises, or restarts
    either group's session. This agreement authorizes the process model
    only.
  - ADR 0006's contract-file governance itself (separate-context Reviewer
    requirement, traceability rule) — unchanged, and six of the eight
    issues in this plan are reviewed under it, not around it.
  - The Reviewer's three constraints (context separation, deterministic
    precondition, falsification burden), the Implementer's self-review
    requirements, and the three invariants — unchanged.
  - Any application-level specification, code, or behavior change.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Write ADR 0016 (two-group topology, backlog gate, non-blocking close, intervention channel) | Specifier | Architecture Path | States each of the six rules in LISS-0019 as a testable rule; names which ADR 0001/0014 clauses are superseded | read-through against this Direction |
| 2 | Map personas to groups in `personas.md` | Implementer | Architecture Path | Session Groups section added; diagram shows the group boundary; no persona's five required fields changed | `scripts/check-contract-consistency.py`; read-through |
| 3 | Update the loop diagram and gate description in `ai-human-scheme.md` | Implementer | Architecture Path | Backlog gate, non-blocking concurrency, and per-item intervention effect all stated; Reviewer/self-review/invariants untouched | `scripts/check-contract-consistency.py`; read-through |
| 4 | Write `cross-session-messaging.md` protocol | Implementer | Architecture Path | Every handoff direction states trigger, message content, and the file that carries the record; `ListAgents` failure treated as a reopening-worthy blocker | `scripts/check-contract-consistency.py`; read-through |
| 5 | Add the standing-pair session type to `session-start-and-resume.md` | Implementer | Architecture Path | Fourth session type added, cross-referencing the protocol doc; artifact-only continuity restated | `scripts/check-contract-consistency.py`; read-through |
| 6 | Add Implementation-group worktree rule to `branch-commit-pr-discipline.md` | Implementer | Architecture Path | Worktree creation/cleanup timing stated; no existing branch/PR rule weakened | `scripts/check-contract-consistency.py`; read-through |
| 7 | Reconcile `design-agreement.md` with the backlog-level gate | Implementer | Architecture Path | Backlog approval can satisfy the Director's agreement statement for the work plan it authorizes; "silence is not agreement" preserved; intervention-gated provisional-record rule stated | `scripts/check-contract-consistency.py`; read-through |
| 8 | State the bulk gate and compliance boundary in `docs/backlog/README.md` | Implementer | Architecture Path | Bulk-gate rule and compliance boundary stated once each, cross-referenced rather than duplicated | read-through |
| 9 | Preflight Validation over the whole work plan | Implementer / deterministic tool | Architecture Path | `pass` recorded with command output, scope result, and next action | Preflight record in WP-0002 |
| 10 | Independent Reviewer pass addressing each contract-file change under ADR 0006 | Reviewer (separate context) | Architecture Path | Review record names searched failure scenarios and grounds; explicitly addresses each of the six contract-file changes, not only overall specification conformance | review record under `docs/collaboration/reviews/` |

Sequencing and dependencies: Task 1 blocks Tasks 2–8 (all read ADR 0016's
Decision section). Task 7 should follow Task 3 in practice, since its
wording depends on the loop diagram's final phrasing, even though the
formal dependency graph in WP-0002 only names Task 1. Task 9 runs only after
Tasks 2–8 are each self-reviewed and complete. Task 10 runs only after Task
9 passes.

## Specifications

- None. This is a governance/process change; there is no application
  specification.

## Boundaries

- ADR 0006 (contract-file change control) is not altered or weakened. Six of
  the eight documents this plan touches (`personas.md`, `ai-human-scheme.md`,
  the new `cross-session-messaging.md`, `session-start-and-resume.md`,
  `branch-commit-pr-discipline.md`, `design-agreement.md`) remain subject to
  its separate-context Reviewer requirement and its traceability rule
  (`docs/collaboration/traces/`), regardless of work-plan self-review.
  `docs/architecture/adr/0016-*.md` and `docs/backlog/README.md` are not
  contract files under ADR 0006's list and are reviewed under the ordinary
  work-plan-level Reviewer pass only.
- The Reviewer's three constraints, the Implementer's self-review
  requirements (deterministic precondition, falsification burden), and the
  three invariants (every decision produces a document, every executed fact
  leaves evidence, every claim states its grounds) are unchanged in
  substance.
- The two human gates (design agreement, work-plan close) are not removed.
  Only their cadence (batched at the backlog-item level rather than
  per-work-plan live dialogue) and their blocking behavior across
  concurrently in-flight work plans change.
- Autonomous progress after backlog approval remains bounded by the
  project's operational rules and applicable law. A case that would require
  exceeding either is a reopening request, not a judgment call.
- A `SendMessage` payload is never itself the deterministic record of a
  decision; it is a trigger referencing a file already written to the
  repository (Invariant 1).

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| How should "human approval must not block the loop" be realized? | Director/AI agreement happens at the backlog-item level; once approved, requirement organization, research, and method study proceed without further human approval; the Director can intervene at any time; autonomous progress is conditioned on following operational rules and law. | Director, confirmed explicitly in dialogue |
| How are the two groups started and kept running? | A standing session pair, started once per group, not reconstituted per work plan. | Director |
| How is concurrent repository access by both groups isolated? | The Implementation group works in a dedicated `git worktree` and branch per work plan; the Design & Review group works against `main`. | Director |
| What is this work plan's build scope? | Process documents and the new ADR only; no automation script or launcher in this pass. | Director |
| What does intervention actually stop? | Not all progress by the receiving group — only the specific in-flight item the message arrived during. That item's development loop and review continue, but gated by the Director's per-step approval, until a resolving instruction. Other concurrent work in either group is unaffected. | Director, refined in a follow-up clarification |
| Does this change how contract-file changes themselves are reviewed? | No. ADR 0006 governs contract-file changes independently and is untouched; six of this plan's eight documents are reviewed under it. | Planner, from reading `prompt-instruction-change-control.md`'s scope list |
| Which documents in this plan are, and are not, ADR 0006 contract files? | `personas.md`, `ai-human-scheme.md`, `cross-session-messaging.md`, `session-start-and-resume.md`, `branch-commit-pr-discipline.md`, and `design-agreement.md` are (all under `docs/collaboration/*.md`). The new ADR (under `docs/architecture/adr/`) and `docs/backlog/README.md` are not. | Planner, from reading `prompt-instruction-change-control.md`'s file list |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Exact `SendMessage` template wording for each handoff | Left to Implementer discretion at execution (LISS-0022 settles required content, not phrasing); revisit if the Reviewer finds a handoff ambiguous in practice |
| Should work-plan size be bounded, now compounded by multiple concurrent work plans across two groups? | Evidence from running under this model — whether defects reaching work-plan-level review correlate with plan size or with the number of concurrently in-flight plans (inherits ADR 0014's own deferred question) |
| What concretely checks the "operational rules and law" compliance boundary before autonomous progress proceeds? | The first backlog item where this boundary is actually load-bearing — decide then whether an existing gate (e.g. `dependency-policy.md`, `privacy-context-budget-policy.md`) already covers it or a new check is needed |
| Should the two-group process gain automation (a launcher script, a supervisor)? | A future backlog item, once this process-only model has run for at least one full work plan and the Director judges the manual-start pattern is a bottleneck |

## Verification

- `scripts/check-contract-consistency.py` after all eight issues land.
- Targeted `grep` sweep for the superseded ADR 0001/0014 phrasing across all
  updated documents, confirming none remain describing the pre-ADR-0016
  behavior as current.
- Confirmation that each of the six contract-file issues (LISS-0020, 0006,
  0007, 0008, 0009, 0010) has an accompanying trace under
  `docs/collaboration/traces/`.
- CI's repository-sanity steps reproduced locally.
- Independent Reviewer approval, in a separate context, explicitly
  addressing each contract-file change under ADR 0006.

## Falsification Criteria

- Any of the six contract-file documents describes the pre-ADR-0016 blocking
  model (mandatory per-work-plan live dialogue; next work plan blocked on
  prior close) as still current.
- Intervention is documented, anywhere, as halting the receiving group's
  other concurrent work rather than gating only the specific in-flight item.
- A work plan under this model is reported closed without a
  separate-context Reviewer approval that explicitly addresses each
  contract-file change, relying only on general specification-conformance
  language.
- The design-agreement gate is documented as removed rather than relocated
  to the backlog-item level.
- Autonomous progress is documented anywhere as unconstrained by the
  project's operational rules or applicable law.
- A `SendMessage` chat transcript is treated as the record of a decision
  with no corresponding file.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation.

Recorded basis: a multi-turn dialogue in which the Director stated the
direction, the AI restated the plan back in full (mapped onto existing
personas, with an explicit list of settled and open points) before any
document was written, the Director answered four structured questions and
then approved with "承認。介入は各グループに人間がチャットを送信することで
始める。人間がチャットに入力をしたら解消するまで人間と作業を進め、指示が出
るまでループを続行しない。", and refined the intervention semantics once
more with "ループを続行しないというのは作業が人間の承認を必要とする作業に
なるという意味で、開発ループ・レビューなどは自体は人間の承認を得ながら進
める。" before any contract file was touched.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
| 2026-08-18 | Preflight found `docs/at-tdd/process.md` (an ADR-0006 contract file) carries the same unqualified pre-ADR-0016 phrasing already fixed in `design-agreement.md` and `ai-human-scheme.md` ("the next work plan does not start without this"), but the file was not named in this agreement's Scope, so it was correctly left unedited and reported as an out-of-scope finding rather than silently fixed. | Director extended Scope, in the Backlog-layer thread, to include this fix: qualify the phrase in `docs/at-tdd/process.md` with the same ADR 0016 Rule 3 cross-reference already used in the other two files (non-blocking only across *unrelated, concurrently in-flight* work plans; the checkpoint for the one work plan being closed is unchanged). Tracked as LISS-0027, Minor Fix Path (single contract file, mirrors an already-reviewed pattern, one attempt expected) — still requires its own AI work trace and separate-context Reviewer confirmation per ADR 0006, self-review does not apply. |
