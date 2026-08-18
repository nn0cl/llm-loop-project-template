# LISS-0032: Mandatory quality-gate hooks and branch/route coverage policy

## Metadata

- Local issue ID: LISS-0032
- GitHub issue: none
- Status: review
- Phase: phase-0-design (produces an ADR and non-application-code contract
  updates)
- Type: architecture-decision
- Priority: high
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/quality-gate-hooks-and-coverage-policy

## Summary

- Write a new ADR (tentatively `0018`, confirm at execution time — see
  `DA-2026-08-18-05`'s Settled Ambiguities on the numbering coordination
  with WP-0004's `0017`) stating: (1) adopting projects must wire an
  actual, commit-blocking pre-commit hook per language — not merely
  document commands to run manually — covering lint, build/compile, unit
  tests, and coverage; (2) a branch/route coverage anti-gaming rule:
  partial-branch tests do not count, every route needs a test, and
  implementation must not be shaped merely to hit a coverage number; (3) no
  universal numeric coverage floor is mandated by the template — each
  adopting project may choose one locally, recorded in its own
  tooling-setup session.
- Update `docs/architecture/tooling.md` (hook-wiring requirement stated),
  `docs/architecture/testing-strategy.md` (new "Coverage Policy" section
  with the anti-gaming rule), `docs/collaboration/definition-of-done.md`
  (Universal/Phase 2/3 Done criteria gain the hook/coverage requirements —
  ADR-0006 contract file), and
  `scripts/lib/emit-tooling-setup-prompt.sh` (Section A/D explicitly ask
  for hook wiring and a coverage approach, with concrete per-stack
  examples).

## Acceptance Notes

- ADR states all three rules as testable requirements, with the
  numeric-floor non-decision and no-retroactive-`scripts/`-application
  decision both stated with grounds (per `DA-2026-08-18-05`'s Settled
  Ambiguities — copy the reasoning, do not re-derive it differently).
- `tooling.md`/`testing-strategy.md` changes do not require a trace (not
  ADR-0006 contract files) but must not contradict the ADR.
- `definition-of-done.md` change requires a trace; no existing Done
  criterion is weakened.
- `scripts/check-contract-consistency.py` passes.
- `scripts/init-loop-settings.sh --prompt-only` output visibly contains the
  strengthened hook/coverage language after the change.
- Self-review recorded (full form — planning size `M`, multiple files).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0006-quality-gate-hooks-and-review-perspectives-doc.md
- Depends on: none
- Blocks: LISS-0033 (perspectives document cites this ADR)
- Related: `docs/architecture/adr/0016-*.md` (numbering-coordination
  precedent, not content)

## Decisions Not Settled by the Design Agreement

- Exact ADR number: confirm at execution time (see Summary above). If
  genuinely conflicting with WP-0004's concurrent claim on `0017`, report
  as a reopening-worthy finding rather than silently resolving.

## Context

- Included: `docs/backlog/item-0006-*.md`, `docs/architecture/tooling.md`,
  `docs/architecture/testing-strategy.md`,
  `docs/collaboration/definition-of-done.md`,
  `scripts/lib/emit-tooling-setup-prompt.sh`, `DA-2026-08-18-05`.
- Omitted: `docs/collaboration/design-review-perspectives.md` (LISS-0033's
  own deliverable — read only its planned existence, not its content,
  which does not exist yet when this issue starts).
- Assumptions: none beyond the design agreement's own settled points.

## AI Planning Records

### AIP-0032-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Sonnet 5 via Claude Code, Design & Review
    group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: not surfaced in this environment
- Created at: 2026-08-18
- Planning size: M
- Intended execution route: Implementation-group agent, Architecture Path,
  one new ADR plus four coordinated file edits
- Compatibility state: Verified — confirmed by direct read that
  `tooling.md`'s stack table is all placeholders, `testing-strategy.md` has
  no coverage section, and `emit-tooling-setup-prompt.sh` does not mention
  hook enforcement
- Intended scope: `docs/architecture/adr/0018-*.md` (number pending),
  `docs/architecture/tooling.md`, `docs/architecture/testing-strategy.md`,
  `docs/collaboration/definition-of-done.md`,
  `scripts/lib/emit-tooling-setup-prompt.sh`
- Estimated token range: 8,000-18,000 tokens
- Estimated token midpoint: 12,000
- Token metric: approximate output tokens across the ADR and four file
  edits
- Estimation basis: comparable in scope to WP-0004's LISS-0029+LISS-0030
  combined (one ADR plus multi-file propagation), scaled for one fewer
  file but a more substantive prompt-script edit
- Assumptions: single execution attempt
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/collaboration/agreements/2026-08-18-quality-gate-hooks-and-perspectives-doc.md`
  (`DA-2026-08-18-05`)
- `docs/architecture/adr/0008-template-update-propagation.md` (sibling
  precedent for a template-contract-level ADR with tiered/deferred
  specifics)

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0006-*.md`'s promotion, after resolving its flagged
  "[x] Human decision required" item to its narrow genuinely-open
  sub-question (see `DA-2026-08-18-05`'s Settled Ambiguities). Dispatched
  to the Implementation group together with LISS-0033.
- 2026-08-18 (Implementer, Implementation group): executed on branch
  `process/quality-gate-hooks-and-coverage-policy` (created from `57af72e`).
  **ADR numbering**: ran `ls docs/architecture/adr/` at execution time —
  highest present was `0016`; `0017` was not present in this branch's tree
  (it exists only on a separate, unmerged branch,
  `process/adr-0017-portable-loop`, belonging to WP-0004's own
  Implementation session — confirmed via
  `git log --all --oneline --grep="0017"` and
  `git merge-base --is-ancestor <that-commit> 57af72e` returning false).
  Confirmed via `git log --all --oneline --grep="0018"` that no ADR `0018`
  exists anywhere in this repository's history. Per `DA-2026-08-18-05`'s
  Settled Ambiguities, this is the anticipated common case (`0017` free,
  `0018` collides with nothing) and not a reopening-worthy conflict, so
  wrote the ADR as `0018` as tentatively named. **Downstream consequence,
  flagged explicitly**: adding `0018` without `0017` present creates a
  temporary numbering gap on this branch alone. `scripts/check-contract-consistency.py`'s
  `ADR range` check is anchored to the actual highest ADR file present, so
  keeping it passing required updating `README.md`, `QUICKSTART.md`, and
  `QUICKSTART.ja.md`'s registered ADR-range statements (last = `0018`,
  next-adopter-number = `0019`) and `.github/workflows/ci.yml`'s hardcoded
  ADR-existence loop (added `0018`, left `0017` out with a comment
  explaining why) — none of these four files were in LISS-0032's originally
  enumerated file list, but all four are a mechanical, unavoidable
  consequence of adding a new ADR file while `check-contract-consistency.py`
  is required to pass; each edit states the gap explicitly in its own prose
  rather than silently implying a contiguous `0001`-`0018` sequence exists.
  **The Design & Review group must reconcile this gap when merging this
  branch with WP-0004's `0017` branch** — expect (and do not silently
  resolve) merge conflicts on these same four files' ADR-range statements,
  since WP-0004's own branch independently edits the same lines to state
  its own range ending at `0017`.

### Self-review (full form, planning size M)

**Command run:**

```text
$ python3 scripts/check-contract-consistency.py --repo .
references:
  docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md:50 names 'docs/collaboration/design-review-perspectives.md', which does not exist
contract consistency: 1 failure(s)
```

**Result:** the only failure is the forward reference to LISS-0033's own
not-yet-created deliverable (`docs/collaboration/design-review-perspectives.md`),
which this issue's own Context section names as intentionally omitted at
this stage (LISS-0032 precedes LISS-0033 in the Recommended Order). This
reference resolves once LISS-0033 lands, in the same work plan. Before ADR
0018 was added, the same command reported `contract consistency: all checks
passed` (baseline, recorded before any edit in this issue).

```text
$ bash scripts/init-loop-settings.sh --prompt-only | grep -c "ADR 0018"
4
```
(The strengthened prompt names ADR 0018 four times: the hook-wiring
mandate, the coverage-approach mandate, and the CI-is-additive note — see
the excerpt in this issue's own References/Verification and in the work
plan's Preflight section for the full text.)

**Risks considered, and why each does not occur:**

1. *Does the ADR's numeric-floor non-decision read as permissive rather
   than as a deliberate, grounded choice?* Re-read ADR 0018's Rule 3 and
   `testing-strategy.md`'s "No universal numeric floor" subsection side by
   side with `DA-2026-08-18-05`'s Settled Ambiguities: both state the same
   two-part reasoning (a floor is a useful backstop, but is also exactly
   the number-optimization target Rule 2 warns against) and both make Rule
   2's anti-gaming requirement explicitly independent of whether a floor is
   adopted — "The anti-gaming rule above applies regardless of whether a
   project adopts a local floor." This is not silence about coverage; it is
   an explicit, mandatory qualitative rule paired with an explicit,
   reasoned non-decision about one specific number. Does not occur.
2. *Does the hook-wiring requirement stay stack-agnostic and not
   accidentally assume a specific tool?* Re-read Rule 1 of ADR 0018: it
   states "an enforcement mechanism... appropriate to their own stack," not
   any named tool, and explicitly separates the *requirement* (Rule 1) from
   the *Dependency Adoption Evidence* section, which states plainly that no
   library/tool is selected by this ADR. The per-stack examples in
   `tooling.md` and `emit-tooling-setup-prompt.sh` are introduced with
   "examples — pick what fits, do not install all," matching the existing
   convention already used for the formatter/linter table in Section A. Does
   not occur.
3. *Does `definition-of-done.md`'s edit weaken any existing criterion?*
   Diffed the file: every change is either a new bullet or an appended
   clause to an existing bullet's own sentence; no existing bullet's
   original text was deleted or narrowed. Checked specifically that
   "deterministic verification was run or explicitly marked not applicable"
   still stands as the base requirement, with the ADR-0018 hook clause
   added as a qualification of what "run" means once a project has ADR
   0018's hook wired — a project without a wired hook yet is not
   retroactively marked non-compliant by this wording; it still satisfies
   the base criterion by running the check manually until it wires a hook.
   Does not occur.
4. *Does the ADR-numbering gap (0017 missing, 0018 present) silently
   mislead a reader into believing the ADR sequence is contiguous?*
   Checked every place the range is stated (README.md, QUICKSTART.md,
   QUICKSTART.ja.md, ci.yml, ADR 0018's own "Numbering note"): each one
   explicitly names the gap and points to ADR 0018's "Numbering note" for
   the explanation, rather than silently stating "0001-0018" with no
   caveat. Reproduced as a real, disclosed condition — not hidden — and
   explicitly flagged above and in this report for the Design & Review
   group's merge-time reconciliation. This is a real, temporary
   inconsistency (an implied-contiguous range that is not actually
   contiguous on this branch), disclosed rather than concealed, and
   resolved at the point where it can actually be resolved (branch merge).
5. *Did the heredoc-backtick defect (self-inflicted, described in the
   `definition-of-done.md` trace's "Rework caused by AI output" field)
   silently corrupt any other part of the emitted prompt beyond Section A's
   new table?* Re-ran `scripts/init-loop-settings.sh --prompt-only` after
   the fix and read the full output (not just Section A) end to end;
   confirmed no other section shows truncated text, injected command
   output, or missing lines. Does not occur, after the fix.

## Verification

```text
$ python3 scripts/check-contract-consistency.py --repo .
references:
  docs/architecture/adr/0018-mandatory-quality-gate-hooks-and-coverage-policy.md:50 names 'docs/collaboration/design-review-perspectives.md', which does not exist
contract consistency: 1 failure(s)
```

Only remaining failure is the forward reference to LISS-0033's deliverable,
expected to resolve once that issue lands in this same work plan (see this
issue's Work Notes self-review for the full explanation and the baseline
passing run recorded before ADR 0018 was added).
