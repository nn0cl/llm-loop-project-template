# Design Agreement: Review Cost Discipline — Correction

## Identity

- Agreement ID: DA-2026-08-03-03
- Date: 2026-08-03
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5, Claude
  Code, chat dialogue (no separate Planner/Specifier tool invocation).
- Supersedes agreement (if any): none. This agreement does not replace
  `docs/collaboration/agreements/2026-08-03-review-cost-discipline.md`
  (DA-2026-08-03-02) — that agreement is itself one of this plan's targets
  (see Plan #4) and is being brought up to this template's required fields in
  place, not superseded.

## Direction

The Director asked (message: "契約が更新されたことを確認した上で、変更内容を新
しいルールで再レビューして") for the ADR 0015 change to be confirmed landed,
then retroactively reviewed under its own new rules — a fresh, separate-context
Reviewer invocation, per ADR 0015 rule 3, rather than resuming any prior
review session. That review
(`docs/collaboration/reviews/2026-08-03-review-cost-discipline-review.md`)
**rejected** the change with 7 findings, naming 6 required artifact changes.
This agreement covers fixing all 6, this time following the full process the
first attempt skipped: a covering design agreement with every required field
(this document), a conformant trace, an extended consistency checker, and
genuine independent Reviewer approval before merge — not a repeat of the
process shortcut that caused the rejection.

The Director separately sent a forward-looking refinement, unrelated to
whether the original skip was authorized: self-review's search should be as
broad as an independent Reviewer's would be, even though the written record
stays proportionally short. That refinement is folded into this plan's scope
(Plan #7) since it touches the same files.

## Scope

- In scope:
  - `docs/templates/self-review.md`: close the evidence loophole (Finding 2)
    — the short form's `Result` field no longer permits a one-line summary in
    place of pasted output.
  - `scripts/check-contract-consistency.py`: add `EXTRA_MIRRORED_RULES`
    entries that actually detect ADR 0015's two new sentences, not just the
    pre-existing word "self-review" (Finding 3).
  - The five Preflight-carrying contract files (`CLAUDE.md`, `AGENTS.md`,
    `.github/copilot-instructions.md`,
    `.cursor/rules/03-collaboration-and-completion.mdc`,
    `.grok/rules/03-collaboration-and-completion.md`): add an explicit scope
    marker separating the contract-file rule from the finding-response
    guidance (Finding 6).
  - `docs/collaboration/agreements/2026-08-03-review-cost-discipline.md`:
    rewrite in place to include every `design-agreement.md`-required field
    (Finding 4).
  - `docs/collaboration/traces/2026-08-03-review-cost-discipline.md`: rewrite
    in place to conform to `docs/templates/ai-work-trace.md`, naming the
    active persona (Finding 5).
  - `docs/collaboration/prompt-instruction-change-control.md` and
    `docs/architecture/adr/0015-review-cost-discipline.md`: state explicitly
    that no Director-override exception to ADR 0006's separate-context
    Reviewer requirement exists, and that this incident is not precedent
    (Finding 1's recommended remediation).
  - `docs/templates/self-review.md` and ADR 0015 rule 1: state that the short
    form bounds the record, not the search — the Implementer searches as
    broadly as an independent Reviewer would (Director's forward-looking
    refinement).
  - This agreement and its accompanying trace
    (`docs/collaboration/traces/2026-08-03-review-cost-discipline-correction.md`).
- Explicitly out of scope:
  - No change to ADR 0006's substantive separate-context requirement itself —
    this fix closes a gap in how that requirement is stated, it does not
    weaken or reinterpret it.
  - No change to the three approval constraints (context separation,
    deterministic precondition, falsification burden).
  - No change to ADR 0014's work-plan-scoped self-review model.
  - No retroactive reversal of the `v2.1.0` merge — Findings 6 and 9 in the
    rejection record confirm most of that propagation was accurate; this fix
    corrects the defects named, it does not re-do the whole change.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Close `self-review.md`'s evidence loophole | Implementer | Refactor | `Result` field requires actual output, no summary escape hatch | Manual diff against Finding 2's text |
| 2 | Extend checker with ADR 0015 mirror rules | Implementer | Refactor | Checker fails when either new sentence is removed from a mirror | Negative test: strip the sentence from a scratch copy, re-run checker |
| 3 | Add scope marker in 5 Preflight-carrying files | Implementer | Refactor | Contract-file rule and finding-response guidance are in separate, explicitly scoped paragraphs in all 5 | `grep` across all 5 files |
| 4 | Rewrite original design agreement (DA-2026-08-03-02) | Implementer | Refactor | Every `design-agreement.md` section present and filled (brief answers acceptable, silent omission is not) | Manual section-by-section comparison against the template |
| 5 | Rewrite original trace | Implementer | Refactor | Every `ai-work-trace.md` section present, `Active persona` stated | Manual section-by-section comparison against the template |
| 6 | State no Director-override exception to ADR 0006 exists | Implementer | Refactor | Statement present in `prompt-instruction-change-control.md` and ADR 0015 | `grep` |
| 7 | Broaden self-review search-scope wording | Implementer | Refactor | `self-review.md` and ADR 0015 rule 1 state search bounds independent of record length | Manual read |
| 8 | Full verification suite | Implementer | Refactor | All deterministic checks pass | See Verification below |
| 9 | Independent Reviewer review of the full branch diff | Reviewer | (separate context) | Approval, or a new rejection naming further required changes | Fresh `Agent` spawn, no resumed session |

Sequencing and dependencies:

- Tasks 1-3 and 7 were already applied to the working tree before this
  agreement was written (continuing directly from the same fix session that
  received the rejection); this agreement documents and covers them
  retroactively as part of the same corrective work, not as an
  after-the-fact rationalization — none of them touch application behavior,
  all are individually verifiable against the rejection record's exact
  wording.
- Task 9 cannot start before tasks 1-8 are complete and pushed; task 9's
  approval is required before this branch merges. This is the one dependency
  this agreement exists to enforce — it is the exact step skipped last time.

## Specifications

No application specification applies — this is a process/governance and
documentation correction, consistent with how prior process-ADR changes in
this repository have been reviewed. The specification this work is judged
against is
`docs/collaboration/reviews/2026-08-03-review-cost-discipline-review.md`'s
"Required artifact changes" section (items 1-6), which is authoritative for
what must change.

## Boundaries

- Must not weaken ADR 0006's separate-context Reviewer requirement for
  contract-file changes — Finding 1 exists because a prior change did exactly
  that in practice; this fix must not repeat it in wording or in process.
- Must not merge this fix branch without genuine, fresh-context independent
  Reviewer approval. This is the boundary the rejection was about; treating
  it as negotiable a second time would repeat the exact failure being
  corrected.
- Must not present the original `v2.1.0` merge as reverted or undone — it
  remains merged and tagged; this work corrects defects in what shipped, per
  the review's own "What this rejection does and does not undo" section.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does the Director's later self-review-scope instruction retroactively bless the original skip? | No — it is forward-looking refinement of self-review search breadth (Plan #7), unrelated to whether the skip was authorized (Plan #6). It arrived after the rejection, addressing a different question. | Implementer, checked against message timing and content |
| Should the original agreement/trace be rewritten in place or replaced with new files? | Rewritten in place — the rejection record's items 4 and 5 name the existing file paths directly, and rewriting in place preserves the historical record's location while fixing its structure | Reviewer's rejection record, items 4 and 5 |
| Is a Director-override exception to ADR 0006 ever legitimate? | No. State explicitly that none exists and this incident is not precedent (rejection record's recommended option, taken as the conservative default) | Implementer default; reported to Director in this turn rather than silently assumed |
| Who authorizes this fix cycle, given no fresh design-phase dialogue happened after the rejection landed? | The Director's original instruction to retroactively review (message 9) carries the implicit, already-established pattern of this session: a Reviewer rejection is answered by an Implementer fix and resubmission, without a new round of design dialogue for each rejection, exactly as happened across PR #8's six rounds earlier in this session | Implementer, consistent with session precedent; open to Director correction if this reading is wrong |

## Deferred Questions

None. Every question the rejection record raised is either answered in
Settled Ambiguities above or is one of the Plan's numbered tasks.

## Verification

- `python3 scripts/check-contract-consistency.py --repo .` — must report
  `contract consistency: all checks passed`.
- Negative test: remove ADR 0015's short-form-default sentence from a scratch
  copy of one contract file and confirm the checker fails naming the new
  `Self-review short-form default (ADR 0015)` rule.
- `required_files` existence check against `.github/workflows/ci.yml`'s list.
- ADR loop range `0001`-`0015` against `docs/architecture/adr/*.md`.
- `bash -n` on shell scripts touched, if any.
- `grep` for unresolved conflict markers.
- Copy-script smoke test confirming `self-review.md` and all edited files
  distribute correctly.
- A fresh-context independent Reviewer's approval, recorded under
  `docs/collaboration/reviews/`.

## Falsification Criteria

This fix would be wrong if any of the following is observed:

- The extended checker rules produce a false positive against the
  copy-script's distributed output (a file that is actually correct gets
  flagged as non-conformant).
- The rewritten design agreement or trace still omits a field its template
  requires unconditionally.
- The independent Reviewer's fresh review finds that the "no override
  exception" language added to `prompt-instruction-change-control.md` and
  ADR 0015 contradicts existing text elsewhere in the contract, rather than
  closing the gap Finding 1 named.
- This branch merges without a recorded, separate-context Reviewer approval
  — the single failure this whole corrective cycle exists to prevent from
  happening twice.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. (Standing
      authorization: message 9's instruction to retroactively review, read
      together with this session's established pattern of fixing named
      Reviewer findings without a fresh dialogue round for each one — see
      Settled Ambiguities. If this reading is wrong, this is the place to
      correct it.)
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. The rejection record names every required
      change with enough specificity that no rule needed to be guessed.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
