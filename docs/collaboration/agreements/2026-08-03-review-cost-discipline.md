# Design Agreement: Review Cost Discipline

## Identity

- Agreement ID: DA-2026-08-03-02
- Date: 2026-08-03
- Director: nn0cl
- Reached through: chat dialogue (diagnosis presented, confirmed, then "はい。
  修正して。今回はレビューをスキップして即反映。")

## Direction

Fix the cost problem diagnosed in dialogue: self-authored process records
(design agreements, traces, Preflight records) were written at full weight
regardless of change size, and multi-round independent review resumed the
same Reviewer agent across rounds rather than a fresh, scoped invocation each
time — both confirmed with concrete numbers and file evidence from this
repository's own session history.

## Scope

- In: `docs/templates/self-review.md` (new, short + full forms);
  `docs/architecture/adr/0015-review-cost-discipline.md`; propagation into
  the nine contract files, `llm-cost-reduction.md`, `README.md`, the ADR
  count bump (14→15), and CI's file list.
- Out: no change to the three approval constraints themselves, no change to
  ADR 0006 (contract changes still need a separate-context Reviewer — this
  one excepted per the next line), no change to how work-plan-level Reviewer
  approval works.

## Agreement and the exception

- **Director**: the diagnosis and the fix described above are correct;
  apply immediately.
- **Explicit exception, this instance only**: independent Reviewer approval
  is skipped for this change, per direct Director instruction. This does not
  change ADR 0006 going forward — the next contract change still requires
  one. This change is unreviewed by a separate context and is recorded as
  such, not backfilled with a review that did not happen.
- **AI**: executable without further interpretation; the diagnosis already
  named every location that needed to change.
