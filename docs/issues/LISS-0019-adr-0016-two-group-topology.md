# LISS-0019: Write ADR 0016 — standing two-group session topology and backlog-gated autonomy

## Metadata

- Local issue ID: LISS-0019
- GitHub issue: none
- Status: review
- Phase: process-only
- Type: architecture
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: n/a
- Owner/agent: unassigned (persona: Specifier)
- Related branch: process/adr-0016-two-group-topology

## Summary

- Write `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  using `docs/templates/adr.md`.
- The ADR must state, as a testable rule:
  1. Two standing session groups connected via the `SendMessage` /
     `ListAgents` cross-session tools: the **Design & Review group** (Planner,
     Specifier, Reviewer, Arbiter) and the **Implementation group**
     (Implementer). Persona-to-group mapping is fixed; see LISS-0020.
  2. Director approval is granted at the `docs/backlog/item-NNNN-*.md` level.
     Once a backlog item is approved, the Design & Review group may
     autonomously perform requirement organization, research (including
     spikes under `docs/spike/`), method/approach study, and produce the
     work plan, specifications, and the design-agreement record for that
     item — with no further blocking Planner-Director dialogue per work
     plan. This supersedes ADR 0001's requirement that every design
     agreement is reached through a live Planner-Director dialogue turn by
     turn; the dialogue may now happen once, at backlog-item approval, with
     downstream planning delegated.
  3. Multiple work plans may be in flight concurrently across both groups.
     A work plan awaiting the Director's closing checkpoint (ADR 0014) does
     not block the Design & Review group from continuing design work on the
     next backlog item, nor the Implementation group from continuing
     execution on another already-agreed work plan. This supersedes ADR
     0014 clause 5's "the next work plan does not start without [close]"
     (corrected from an earlier draft's "clause 6" — see ADR 0016's own
     "Supersession, precisely" table).
  4. **Intervention channel.** At any time, the Director may send a chat
     message directly into either group's standing session. Receipt of such
     a message converts the specific in-flight item being worked at that
     moment — not the group's other concurrent work — into a human-approval
     -gated mode: the group continues its development-loop and review work
     on that item, but each subsequent step requires the Director's explicit
     approval before proceeding. This gated mode persists until the
     Director gives a resolving instruction, which either restores
     autonomous progress on that item or redirects it. Other concurrently
     in-flight work plans or backlog items in either group are unaffected
     and continue under the standing backlog-level authorization.
  5. Autonomous progress under this ADR remains bounded by the project's
     operational rules and applicable law; this is a standing constraint,
     not a per-item checkbox.
  6. The two existing human gates (design agreement, work-plan close) are
     unchanged in kind; only their blocking behavior across concurrent work
     plans, and the backlog-level batching of the design-agreement dialogue,
     change.
- State explicitly which ADR 0001 and ADR 0014 clauses are superseded, and
  which parts remain in force (the three invariants, the Reviewer's three
  constraints, the Implementer's self-review requirements, ADR 0006's
  contract-file governance — none of these are altered).

## Acceptance Notes

- ADR file exists at the path above, `Status: Accepted`, citing the covering
  design agreement (`docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`)
  once recorded.
- Read-through confirms the Decision section states each of the six points
  above as a testable rule, not prose description.
- Status section of ADR 0001 and ADR 0014 updated (or a note added) pointing
  forward to ADR 0016 for the clauses it supersedes, mirroring how ADR 0001's
  own Status section already points to ADR 0014.

## Dependencies

- Parent: WP-0002
- Depends on: none
- Blocks: LISS-0020, LISS-0021, LISS-0022, LISS-0023, LISS-0024, LISS-0025,
  LISS-0026
- Related: docs/architecture/adr/0001, docs/architecture/adr/0014

## Decisions Not Settled by the Design Agreement

- None known. Escalate to a reopening request if ADR drafting surfaces a
  rule the design agreement does not settle.

## Context

- Included: ADR 0001, ADR 0014, `docs/collaboration/personas.md`,
  `docs/collaboration/ai-human-scheme.md`,
  `docs/collaboration/design-agreement.md`, the Director dialogue recorded in
  the covering design agreement's Direction section.
- Omitted: application-level specs (this is a governance/process change with
  no application specification).
- Assumptions: the next available ADR number is 0016 (0001–0015 exist at
  planning time).

## AI Planning Records

### AIP-0019-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Code CLI
  - Model as displayed: claude-sonnet-5
  - Reasoning setting as displayed: N/A
  - N/A reason: reasoning-effort setting is not surfaced to this session by
    the harness
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Specifier persona, single agent, single attempt
- Compatibility state: N/A (no dependency/version claim)
- Intended scope: one new ADR file; no code changes
- Estimated token range: 3,000–8,000
- Estimated token midpoint: 5,000
- Token metric: output tokens for the ADR draft plus one revision pass
- Estimation basis: comparable to ADR 0014's length and the prior agreement's
  Task 1 scope
- Assumptions: no dependency-adoption evidence section needed (no library
  selection)
- Confidence: medium — the supersession wording for two prior ADRs at once is
  more intricate than a single-ADR supersession
- Revises: none
- Revision reason: n/a
- Superseded by: none

## References

- `docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md`
- `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`
- `docs/collaboration/agreements/2026-08-03-work-plan-scoped-governance.md`
  (structural precedent for a governance-superseding ADR plus propagation)

## Work Notes

- 2026-08-18 (Specifier, Design & Review group, first standing session):
  drafted `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
  with `Status: Accepted`, citing `DA-2026-08-18-01`. Kept the "two-group"
  filename/title deliberately — see the ADR's own Context section,
  "The three-layer correction" — because the decision still names exactly
  two standing session groups with personas; Backlog is a third layer by
  design, not a third group, and Rule 1 states that distinction explicitly.
  Added forward-pointer notes to ADR 0001's and ADR 0014's Status sections.
  Corrected a clause-citation slip in `DA-2026-08-18-01` (Identity section:
  "ADR 0014 clause 6" -> "clause 5" for the blocking-close phrase) so the
  design agreement and this ADR cite the same clause for the same fact.
  Reviewed WP-0002, `DA-2026-08-18-01`, and this issue's own prior text for
  two-layer-only claims that the three-layer clarification would make
  wrong; found none needing correction beyond the citation slip above and
  the matching slip in this issue's own point 3 (also corrected: "clause
  6" -> "clause 5"). See the Self-Review block below for the grep evidence.
- Also updated, as a mechanical consequence of ADR 0016 now existing as a
  sixteenth template process ADR: `README.md` (two spots), `QUICKSTART.md`
  (two spots), `QUICKSTART.ja.md` (two spots), and
  `.github/workflows/ci.yml`'s "Check architecture decision records" step —
  all previously asserted the process-ADR range as 0001-0015 /
  "your project's own decisions from 0016 up"; now 0001-0016 /
  "...from 0017 up". Found via `scripts/check-contract-consistency.py`'s
  "ADR range" check, which failed on these six spots before the fix and
  passes after (see Self-Review below).
- Branch note: this issue's designated branch per WP-0002's Issue Graph is
  `process/adr-0016-two-group-topology`. This work landed instead as
  commits directly on `process/two-group-send-message-loop-design` (the
  work-plan's own design branch), per this session's explicit operating
  instructions for its first run. This is a session-mechanics deviation
  from the Issue Graph's branch column, not a design-content change; noted
  here so a later reader is not confused by the mismatch. Whether
  per-issue branches are needed for Design & Review's own (non-Implementer)
  output is a question for LISS-0024 / `branch-commit-pr-discipline.md`,
  not resolved here.

### Self-Review (Specifier, this issue's phase transition — design note to drafted ADR)

Per `docs/templates/self-review.md` (short form; per this session's explicit
instruction, notwithstanding this issue's `M` planning size — the search
below is scoped as if it were the only check this ADR gets before Preflight
and the separate-context Reviewer, per the short-form rule that size bounds
the record, not the search).

```text
Phase / finding: Architecture Path design note -> drafted ADR 0016 (+ forward-
  pointers on ADR 0001/0014, + a citation-precision fix on DA-2026-08-18-01
  and this issue's own text, + ADR-range consistency fixes)

Command run: python3 scripts/check-contract-consistency.py
Result (before the ADR-range fixes to README.md/QUICKSTART.md/QUICKSTART.ja.md/
  .github/workflows/ci.yml):
  references:
    docs/architecture/adr/0016-...md:192 names 'docs/collaboration/cross-session-messaging.md', which does not exist
    docs/architecture/adr/0016-...md:284 names 'docs/collaboration/cross-session-messaging.md', which does not exist
  ADR range:
    README.md states 0015 where 0016 is expected (...)
    README.md states 0016 where 0017 is expected (...)
    QUICKSTART.md states 0015 where 0016 is expected (...) [x2]
    QUICKSTART.ja.md states 0015 where 0016 is expected (...) [x2]
  contract consistency: 10 failure(s)

Result (after the fixes above):
  references:
    docs/architecture/adr/0016-...md:192 names 'docs/collaboration/cross-session-messaging.md', which does not exist
    docs/architecture/adr/0016-...md:284 names 'docs/collaboration/cross-session-messaging.md', which does not exist
  contract consistency: 2 failure(s)

Risks considered:
  1. ADR 0016 fails to state one of LISS-0019's six required points as a
     testable rule (prose only, not a rule).
  2. WP-0002 / DA-2026-08-18-01 / LISS-0019 contain text that asserts, or
     could be read to assert, that there are only two layers total, or that
     the Backlog thread is itself the Design & Review group.
  3. The ADR's stated supersessions misidentify which ADR 0001/0014 clause
     is superseded, leaving the ADR and the design agreement disagreeing
     with each other about which clause governs a given fact.
  4. The ADR breaks `scripts/check-contract-consistency.py` by introducing
     a reference to a file that does not exist, or by leaving the
     newly-invalidated ADR-range assertions in README.md/QUICKSTART.md/
     QUICKSTART.ja.md/ci.yml unfixed.
  5. The ADR silently weakens something Task 1's Boundaries section says is
     unchanged (the three invariants, the Reviewer's three constraints, the
     Implementer's self-review requirements, or ADR 0006).
  6. The ADR (or my edits to WP-0002/DA/LISS-0019) pre-empts LISS-0020-0026
     by editing one of their target files, or by resolving an ambiguity the
     design agreement does not settle.
  7. I mark the branch/commit deviation from WP-0002's Issue Graph silently
     instead of naming it, which would leave a future reader unable to tell
     why the file paths do not match the plan.

Why each does not occur:
  1. Read-through: ADR 0016's Decision has six numbered rules (Rules 1-6),
     each mapping one-to-one onto LISS-0019's six summary points (Rule 1 =
     point 1, extended for the three-layer correction; Rule 2 = point 2;
     Rule 3 = point 3; Rule 4 = point 4; Rule 5 = point 5; Rule 6 = point 6's
     "which parts remain in force" instruction). Each rule states an
     obligation ("Director approval is granted at...", "does not block...",
     "converts the specific in-flight item... into a human-approval-gated
     mode") rather than description-only prose.
  2. `grep -rn "two.layer\|2-layer\|two total layers" docs/` found no such
     claim in WP-0002, DA-2026-08-18-01, or LISS-0019 (the one unrelated hit,
     in a 2026-08-02 review record, is about an unrelated checker rule's
     "two layers", not session topology). All three documents already scope
     "two groups" to the two execution-loop session groups and describe
     backlog approval separately at the "backlog-item level" / "backlog
     level" throughout — confirmed by a full read of all three files and a
     targeted `grep -n -i "layer\|two.group\|backlog" ` sweep across them
     before any edit was made.
  3. Re-derived each clause number directly from ADR 0001's and ADR 0014's
     own Decision section text (not from the earlier drafts' citations),
     found the "next work plan does not start without it" phrase actually
     sits in ADR 0014 Decision clause 5, not clause 6 as the original
     DA-2026-08-18-01 and LISS-0019 drafts stated; corrected both to clause
     5 and added a "Supersession, precisely" table in the ADR itself,
     stating clause 6 is explicitly *not* superseded, to foreclose the same
     mix-up recurring.
  4. `scripts/check-contract-consistency.py` run twice (before/after, output
     above). The `cross-session-messaging.md` reference failures are
     expected and out of my scope to fix — that file is LISS-0022's own
     target, and creating it here would pre-empt the Implementation group's
     work under LISS-0022, which this session was explicitly told not to do.
     The ADR-range failures were fixed (README.md, QUICKSTART.md,
     QUICKSTART.ja.md, .github/workflows/ci.yml) and the checker now shows
     only the two expected, explained failures.
  5. Rule 6 states each of the four items explicitly ("None of the following
     are altered by this ADR"); cross-checked each bullet against ADR 0001,
     ADR 0014, `docs/collaboration/personas.md`, and
     `docs/collaboration/prompt-instruction-change-control.md` — none of
     those source documents' relevant clauses were edited by this session
     except the two precise, cited supersessions in Rules 2 and 3.
  6. Confirmed via `git status --short` that none of LISS-0020-0026's own
     target files — `docs/collaboration/personas.md`, `ai-human-scheme.md`,
     `cross-session-messaging.md` (new), `session-start-and-resume.md`,
     `branch-commit-pr-discipline.md`, `docs/collaboration/design-agreement.md`
     (the rules document LISS-0025 will edit), or `docs/backlog/README.md`
     (LISS-0026) — were created or modified by this session. The one
     agreement-namespace file this session did edit,
     `docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md`
     (`DA-2026-08-18-01`), is a different file from
     `docs/collaboration/design-agreement.md` — it is the signed *record
     instance* under `docs/collaboration/agreements/`, not the rules
     document, and is excluded from ADR 0006's contract-file list by
     `docs/collaboration/prompt-instruction-change-control.md`'s own text
     ("Files under `docs/collaboration/traces/`, `docs/collaboration/reviews/`,
     and `docs/collaboration/agreements/` are records... not part of the
     contract itself"). Editing it was therefore never inside the "must not
     touch" boundary for this session, which named LISS-0020-0026's *target*
     files, not the pre-existing DA record this ADR itself cites. No
     decision the design agreement leaves unsettled was resolved silently;
     the one open branch-topology question (above) was surfaced, not
     decided.
  7. Recorded explicitly in the "Branch note" bullet above, naming both the
     planned branch and the branch actually used, and the reason.
```


- Read-through against the design agreement's Direction and Settled
  Ambiguities sections.
- `scripts/check-contract-consistency.py` (run after LISS-0020–0011 also
  land, since consistency is a whole-work-plan property).
