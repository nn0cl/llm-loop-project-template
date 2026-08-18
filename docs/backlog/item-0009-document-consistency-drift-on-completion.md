# Backlog item: item-0009-document-consistency-drift-on-completion

## Metadata

- Item ID: item-0009
- Title: Catch cross-document consistency drift automatically when a
  workflow/CI job or an issue completes, instead of relying on an agent to
  notice by hand
- Status: promoted
- Created: 2026-08-18
- Updated: 2026-08-18
- Priority hint: high
- Suggested planning size: TBD
- Owner/agent (optional): unassigned

## Summary

Across WP-0002 through WP-0006 in this session, the same class of problem
recurred repeatedly: a completion event (an issue landing, a new ADR being
added, a work plan closing) silently left some *other* document out of
sync, and it was only caught because an agent happened to check by hand —
not because a deterministic tool flagged it. Concrete instances from this
session alone:

1. **ADR-number-range checks break on every new ADR.** Adding ADR 0016 broke
   hardcoded "0001-0015" ranges in `README.md`, `QUICKSTART.md`,
   `QUICKSTART.ja.md`, and `.github/workflows/ci.yml`'s ADR-existence loop.
   This recurred identically when ADR 0017 was added (WP-0004), and a
   follow-up task (`task_76618661`) had to be spawned just to bump the CI
   check again.
2. **ID-range collisions with retired history.** `docs/issues/LISS-*.md`
   and `docs/backlog/item-*.md` only show currently-live files; numbers used
   by since-deleted history are invisible without a full `git log --all`
   search. This session assigned LISS-0004 through LISS-0011 by mistake
   (already used up to LISS-0018 in git history) before catching it and
   renumbering to LISS-0019+.
3. **Issue-status double bookkeeping drifts.** A `docs/issues/LISS-*.md`
   file's own `Status` field and its row in the owning work plan's Issue
   Graph table are two separate places recording the same fact; this
   session found them disagreeing (LISS-0028 was `review` in the issue file
   but `ready` in WP-0003's Issue Graph) and had to fix both by hand.
4. **Superseding-phrasing propagation is incomplete by default.** When ADR
   0016 superseded specific ADR 0001/0014 clauses, three separate files
   (`design-agreement.md`, `ai-human-scheme.md`, `docs/at-tdd/process.md`)
   each needed the same qualifying phrase added, and each was caught only
   by a manual grep sweep at Preflight time — not by a check that runs
   automatically when a superseding ADR is accepted.
5. **Template-copy exclusion lists miss new document classes.** WP-0005
   found `docs/work-plans/WP-*.md` was never added to
   `scripts/copy-ai-collaboration-files.sh`'s exclusion list alongside
   `LISS-*.md` and `item-*.md`, so template history leaked into adopter
   copies — and the fix itself exposed a second, still-open gap
   (`check-contract-consistency.py` failing against a copied target because
   excluded paths are still referenced; `task_cdbaa1ce`).

## Why it might matter

`scripts/check-contract-consistency.py` already exists as the deterministic
tool for contract-mirror consistency, but none of the five patterns above
are actually checks it runs — they were each caught reactively, by an agent
doing a manual grep or noticing a mismatch while working on something else.
Relying on that is exactly what `docs/collaboration/loop-settings.toml`'s
`[audit]` section and this template's own Prime Directive ("every executed
fact leaves evidence") argue against: deterministic tooling should catch
what model judgment currently catches by luck.

## Known constraints

- Free / zero-mandatory-spend preference applies: yes — extend the existing
  Python checker rather than adopt a new dependency.
- Boundaries or non-goals:
  - Not a request to rebuild `check-contract-consistency.py` from scratch —
    extend it with new check functions for each pattern above.
  - Overlaps with, but is distinct from, `item-0006` (quality-gate hooks +
    review-perspectives document): item-0006 is about *application* code
    quality (lint/build/test/coverage) for adopting projects; this item is
    about *this template's own* collaboration-document consistency. Note
    the overlap explicitly when planning so the two aren't built twice.
  - Should reuse `docs/collaboration/traces/`,
    `docs/collaboration/reviews/`, and the two already-spawned follow-up
    tasks (`task_76618661`, `task_cdbaa1ce`) as inputs/precedent, not
    duplicate their fixes.

## Uncertainty

- [ ] Spec can be written now
- [x] Spike required first (options, feasibility, or quality unknown) —
      survey `check-contract-consistency.py`'s current check structure to
      decide whether these five patterns fit as new functions in the same
      script or need a separate tool; confirm which checks can run in CI
      today vs. which need a new trigger point (e.g., a check that fires
      specifically when a new ADR file is added, not just on every commit).
- [ ] Human decision required (value, policy, budget, legal)

## Links

- Spike case: none yet
- Work plan (when promoted): none yet
- Design agreement (when promoted): none yet
- Local issue (LISS): none yet
- Spec: none yet
- ADR: none yet — related existing tooling:
  `scripts/check-contract-consistency.py`,
  `docs/collaboration/definition-of-done.md` ("Issue Status
  Synchronization" section, already states the rule this item would help
  enforce automatically)

## Promotion notes

- Date: 2026-08-18
- Decision: Promoted, in the Backlog-layer thread, immediately at capture
  time ("承認"). Per ADR 0016 Rule 2, this approval is the single
  design-phase gate — the Design & Review group proceeds autonomously from
  here: run the Uncertainty spike (survey `check-contract-consistency.py`'s
  structure) itself, decide the overlap boundary with item-0006 noted
  above, then build the work plan, spec, and design agreement, without a
  further live dialogue turn with the Director for this item.
- Reason: Well-evidenced by five concrete instances from this session;
  ready to run.
